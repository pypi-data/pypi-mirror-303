import datetime
import os
import warnings
from typing import List
from typing import NamedTuple
from typing import Optional

import boto3.s3.transfer

_DEFAULT_PRESIGNED_URL_DURATION_SECONDS = 24 * 60 * 60  # 1 day.


class PresignedURL(str):
    """Defines presigned URL as its own type so it can be extended for integration with
    other service clients (e.g. H2O-3)
    """


class ObjectSummary(NamedTuple):
    """Represents basic information about an object."""

    key: str
    size: int
    last_modified: datetime.datetime


class PrefixedBucket:
    """Implements standard object operations but all keys are automatically prefixed
    with configured prefix.

    Simulates behavior of the bucket within the bucket.
    """

    def __init__(self, *, bucket: "Bucket", prefix: str) -> None:
        self._bucket = bucket
        self._prefix = prefix
        self._prefix_length = len(prefix)

    async def upload_file(self, filename: os.PathLike, key: str):
        """Uploads a local file, resulting in a new object at the specified key in the
        bucket.

        Args:
            filename: The file to upload. The contents of this file will become an
                object in the Drive bucket.
            key: The key at which to store the resulting object. In other words, the
                name attached to the object.
        """
        await self._bucket.upload_file(filename, self._key_with_prefix(key))

    async def download_file(self, key: str, filename: os.PathLike):
        """Downloads the object at the specified key and writes it to the specified
        local file.

        Args:
            key: The key of the object to download.
            filename: The file, on the local filesystem, the object is written to.
        """
        await self._bucket.download_file(self._key_with_prefix(key), filename=filename)

    async def list_objects(self, prefix: Optional[str] = None) -> List[ObjectSummary]:
        """Returns the list of objects in the bucket.

        Args:
            prefix: When specified, only objects at keys starting with the specified
                value are listed.
        """
        filter_prefix = self._prefix
        if prefix is not None:
            filter_prefix = self._key_with_prefix(prefix)

        objects = await self._bucket.list_objects(prefix=filter_prefix)

        result: List[ObjectSummary] = []
        for o in objects:
            if not o.key.startswith(self._prefix):
                raise RuntimeError("Unexpected key: " + o.key)

            key = o.key[self._prefix_length :]
            result.append(
                ObjectSummary(key=key, size=o.size, last_modified=o.last_modified)
            )

        return result

    async def delete_object(self, key: str):
        """Deletes the object at the specified key.

        Args:
            key: The key of the object to delete.
        """
        await self._bucket.delete_object(self._key_with_prefix(key))

    async def generate_presigned_url(
        self,
        key: str,
        *,
        duration_seconds: int = _DEFAULT_PRESIGNED_URL_DURATION_SECONDS,
    ) -> PresignedURL:
        """Generates a presigned URL for accessing the object at the specified key in
        the bucket.

        Presigned URLs will expire after duration_seconds have elapsed, or when the
        underlying Drive session expires, whichever comes first. The underlying session
        duration is controlled when first connecting to Drive.

        Args:
            key: The key to generate a presigned URL for.
            duration_seconds: The duration, in seconds, for which the URL should be
                valid. Maximum allowed is 604800 seconds (7 days). Defaults to 1 day.

        Returns:
            A presigned URL for the object at the specified key.
        """
        return await self._bucket.generate_presigned_url(
            key=self._key_with_prefix(key),
            duration_seconds=duration_seconds,
        )

    def _key_with_prefix(self, key: str) -> str:
        return self._prefix + key


class Bucket:
    def __init__(self, name: str, *, client_generator, resource_generator) -> None:
        self._name = name
        self._client_generator = client_generator
        self._resource_generator = resource_generator

    async def upload_file(self, filename: os.PathLike, key: str):
        """Uploads a local file, resulting in a new object at the specified key in the
        bucket.

        Args:
            filename: The file to upload. The contents of this file will become an
                object in the Drive bucket.
            key: The key at which to store the resulting object. In other words, the
                name attached to the object.
        """
        async with self._client_generator() as s3:
            await s3.upload_file(
                filename,
                self._name,
                key,
                Config=boto3.s3.transfer.TransferConfig(max_io_queue=5),
            )

    async def download_file(self, key: str, filename: os.PathLike):
        """Downloads the object at the specified key and writes it to the specified
        local file.

        Args:
            key: The key of the object to download.
            filename: The file, on the local filesystem, the object is written to.
        """
        async with self._client_generator() as s3:
            await s3.download_file(self._name, key, filename)

    async def list_objects(self, prefix: Optional[str] = None) -> List[ObjectSummary]:
        """Returns the list of objects in the bucket.

        Args:
            prefix: When specified, only objects at keys starting with the specified
                value are listed.
        """
        async with self._resource_generator() as s3:
            bucket = await s3.Bucket(self._name)
            if prefix is not None:
                objects = bucket.objects.filter(Prefix=prefix)
            else:
                objects = bucket.objects.all()
            result: List[ObjectSummary] = []
            async for o in objects:
                result.append(
                    ObjectSummary(
                        key=o.key,
                        size=await o.size,
                        last_modified=await o.last_modified,
                    )
                )
            return result

    async def delete_object(self, key: str):
        """Deletes the object at the specified key.

        Args:
            key: The key of the object to delete.
        """
        async with self._resource_generator() as s3:
            bucket = await s3.Bucket(self._name)
            obj = await bucket.Object(key)
            await obj.delete()

    async def generate_presigned_url(
        self,
        key: str,
        *,
        duration_seconds: int = _DEFAULT_PRESIGNED_URL_DURATION_SECONDS,
    ) -> PresignedURL:
        """Generates a presigned URL for accessing the object at the specified key in
        the bucket.

        Presigned URLs will expire after duration_seconds have elapsed, or when the
        underlying Drive session expires, whichever comes first. The underlying session
        duration is controlled when first connecting to Drive.

        Args:
            key: The key to generate a presigned URL for.
            duration_seconds: The duration, in seconds, for which the URL should be
                valid. Maximum allowed is 604800 seconds (7 days). Defaults to 1 day.

        Returns:
            A presigned URL for the object at the specified key.
        """
        async with self._client_generator() as s3:
            url_str = await s3.generate_presigned_url(
                ClientMethod="get_object",
                Params={"Bucket": self._name, "Key": key},
                ExpiresIn=duration_seconds,
            )
            return PresignedURL(url_str)

    def with_prefix(self, prefix: str) -> PrefixedBucket:
        """Returns a prefixed view of this bucket. All the keys in each of its object
        operations are automatically prefixed with the specified value.

        Args:
            prefix: The key prefix to automatically apply to all object operations.
        """
        if not prefix.endswith("/"):
            warnings.warn(
                "Note that prefixes are commonly specified with a trailing slash "
                + "('/'), which is missing.",
                stacklevel=2,
            )
        return PrefixedBucket(bucket=self, prefix=prefix)
