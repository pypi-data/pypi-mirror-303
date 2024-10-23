import enum
import os

_HOME_PREFIX = "home/"


class Space(enum.Enum):
    """Defines supported predefined workspaces."""

    HOME = enum.auto()
    APP = enum.auto()
    APP_VERSION = enum.auto()
    APP_INSTANCE = enum.auto()

    def prefix(self) -> str:
        """Returns the fully-resolved prefix."""
        if self == Space.HOME:
            return _HOME_PREFIX
        elif self == Space.APP:
            return _get_app_workspace_prefix()
        elif self == Space.APP_VERSION:
            return _get_app_version_workspace_prefix()
        elif self == Space.APP_INSTANCE:
            return _get_app_instance_workspace_prefix()
        else:
            raise ValueError(f"Unsupported prefix: {self}")


def _get_app_workspace_prefix():
    app = _get_app_name()
    return f"{app}/workspace/"


def _get_app_version_workspace_prefix():
    app_version_prefix = _get_app_version_prefix()
    return f"{app_version_prefix}/workspace/"


def _get_app_version_prefix():
    app, version, app_id = _get_app_name(), _get_app_version(), _get_app_id()
    return f"{app}/{app_id}-{version}"


def _get_app_instance_workspace_prefix():
    app_version_prefix = _get_app_version_prefix()
    app_instance_id = _get_app_instance_id()
    return f"{app_version_prefix}/{app_instance_id}/workspace/"


def _get_app_name() -> str:
    app = os.getenv("H2O_CLOUD_APP_NAME")
    if not app:
        raise LookupError(
            "Unable to determine app name. "
            "H2O_CLOUD_APP_NAME environment variable not set."
        )
    return app


def _get_app_version() -> str:
    version = os.getenv("H2O_CLOUD_APP_VERSION")
    if not version:
        raise LookupError(
            "Unable to determine app version. "
            "H2O_CLOUD_APP_VERSION environment variable not set."
        )
    return version


def _get_app_id() -> str:
    app_id = os.getenv("H2O_CLOUD_APP_ID")
    if not app_id:
        raise LookupError(
            "Unable to determine app ID. "
            "H2O_CLOUD_APP_ID environment variable not set."
        )
    return app_id


def _get_app_instance_id() -> str:
    instance_id = os.getenv("H2O_CLOUD_INSTANCE_ID")
    if not instance_id:
        raise LookupError(
            "Unable to determine app instance ID. "
            "H2O_CLOUD_INSTANCE_ID environment variable not set."
        )
    return instance_id
