from typing import Optional

import aioboto3
import aiobotocore.session
import botocore.config

from h2o_drive import core

_USERDRIVE_BUCKET_ALIAS = "_my"
_WORKSPACEDRIVE_PERSONAL_BUCKET_ALIAS = "default"

_WORKSPACE_NAME_PREFIX = "workspaces/"
_WORKSPACE_PERSONAL_ALIAS = "default"


class Drive:
    def __init__(
        self,
        *,
        userdrive_url: str,
        workspacedrive_url: str,
        session: aiobotocore.session.AioSession,
        sanitize_session: bool = True,
    ) -> None:
        """Returns a client for interacting with Drive.

        Args:
            userdrive_url: URL to Drive's userdrive service.
            workspacedrive_url: URL to Drive's workspacedrive service.
            session: The aiobotocore session to use for connecting to Drive.
            sanitize_session: Whether to sanitize the session configuration to ensure
                compatibility with Drive.
        """
        self._userdrive_url = userdrive_url
        self._workspacedrive_url = workspacedrive_url
        self._session = session
        self._aioboto3_session = aioboto3.Session(botocore_session=self._session)

        if sanitize_session:
            config = _sanitize_client_config(self._session.get_default_client_config())
            self._session.set_default_client_config(config)

    def user_bucket(self) -> core.Bucket:
        """Returns the bucket associated with the user's personal account.

        The user's bucket is independent of any workspace and is not associated with
        workspaces in any way.

        Access to this bucket is denied to other users; its contents may be shared with
        others exclusively through generated signed URLs which are valid for
        configurable durations.
        """
        return self._open_bucket(_USERDRIVE_BUCKET_ALIAS, self._userdrive_url)

    def workspace_bucket(self, workspace: str) -> core.Bucket:
        """Returns the bucket associated with the specified workspace.

        Args:
            workspace: The name, or identifier, of the workspace for which to retrieve
                the associated bucket.
        """
        if workspace.startswith(_WORKSPACE_NAME_PREFIX):
            workspace = workspace[len(_WORKSPACE_NAME_PREFIX) :]

        bucket_name = workspace
        if workspace == _WORKSPACE_PERSONAL_ALIAS:
            bucket_name = _WORKSPACEDRIVE_PERSONAL_BUCKET_ALIAS

        return self._open_bucket(bucket_name, self._workspacedrive_url)

    def _open_bucket(self, name: str, endpoint_url: str) -> core.Bucket:
        if name.strip() == "":
            raise ValueError("bucket name must not be empty")

        def _client_context_generator():
            return self._aioboto3_session.client("s3", endpoint_url=endpoint_url)

        def _resource_context_generator():
            return self._aioboto3_session.resource("s3", endpoint_url=endpoint_url)

        return core.Bucket(
            name=name,
            client_generator=_client_context_generator,
            resource_generator=_resource_context_generator,
        )


def _sanitize_client_config(
    config: Optional[botocore.config.Config],
) -> botocore.config.Config:
    """Returns a sanitized version of the provided client configuration.

    This is useful for local setups where environments have configurations, meant for
    other vendors, which boto libraries may pick up automatically. Those injected
    configurations might otherwise have the potential to interfere with how Drive is
    communicated with.
    """
    override = botocore.config.Config(
        signature_version="s3v4",
    )
    return config.merge(override) if config is not None else override
