import importlib.metadata

from h2o_drive.client import Drive
from h2o_drive.connection import connect
from h2o_drive.connection import create_session
from h2o_drive.core import Bucket
from h2o_drive.core import ObjectSummary
from h2o_drive.core import PrefixedBucket
from h2o_drive.core import PresignedURL
from h2o_drive.prefixes import Space
from h2o_drive.sts import AsyncCredentialProvider
from h2o_drive.sts import StaticTokenProvider
from h2o_drive.sts import TokenProvider

__all__ = [
    "Drive",
    "connect",
    "create_session",
    "Bucket",
    "ObjectSummary",
    "PrefixedBucket",
    "PresignedURL",
    "Space",
    "AsyncCredentialProvider",
    "StaticTokenProvider",
    "TokenProvider",
]

try:
    __version__ = importlib.metadata.version("h2o-drive")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"
