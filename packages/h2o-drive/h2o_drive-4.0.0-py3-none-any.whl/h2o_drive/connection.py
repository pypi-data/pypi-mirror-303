from typing import Optional

import aiobotocore.session
import h2o_authn.discovery
import h2o_discovery

from h2o_drive import client
from h2o_drive import sts

_STS_DISCOVERY_SERVICE_NAME = "drive-sts"
_USERDRIVE_DISCOVERY_SERVICE_NAME = "userdrive"
_WORKSPACEDRIVE_DISCOVERY_SERVICE_NAME = "workspacedrive"

_DEFAULT_SESSION_DURATION_SECONDS = 3600


def connect(
    *,
    discovery: Optional[h2o_discovery.Discovery] = None,
    userdrive_url: Optional[str] = None,
    workspacedrive_url: Optional[str] = None,
    sts_url: Optional[str] = None,
    token_provider: Optional[sts.TokenProvider] = None,
) -> client.Drive:
    """Connects to H2O Drive.

    Required parameters that are not supplied are determined automatically from the
    environment.

    Args:
        discovery: The h2o_discovery.Discovery object through which to discover
            services for determining connection details.
        userdrive_url: URL to Drive's userdrive service.
        workspacedrive_url: URL to Drive's workspacedrive service.
        sts_url: URL to the STS service.
        token_provider: A token provider generating authentication credentials.

    Raises:
        LookupError: If a required parameter is not specified and cannot be determined
            from the environment.

    Returns:
        A Drive client.
    """

    if discovery is None:
        discovery = h2o_discovery.discover()

    if userdrive_url is None:
        userdrive_url = _lookup_service_uri(
            discovery, _USERDRIVE_DISCOVERY_SERVICE_NAME
        )

    if workspacedrive_url is None:
        workspacedrive_url = _lookup_service_uri(
            discovery, _WORKSPACEDRIVE_DISCOVERY_SERVICE_NAME
        )

    session = create_session(
        discovery=discovery,
        sts_url=sts_url,
        token_provider=token_provider,
    )

    return client.Drive(
        userdrive_url=userdrive_url,
        workspacedrive_url=workspacedrive_url,
        session=session,
    )


def create_session(
    *,
    discovery: Optional[h2o_discovery.Discovery] = None,
    sts_url: Optional[str] = None,
    token_provider: Optional[sts.TokenProvider] = None,
    session_duration_seconds: int = _DEFAULT_SESSION_DURATION_SECONDS,
) -> aiobotocore.session.AioSession:
    """Creates a new aiobotocore session backed with credentials for authenticating to
    H2O Drive.

    Required parameters that are not supplied are determined automatically from the
    environment.

    Args:
        discovery: The h2o_discovery.Discovery object through which to discover
            services for determining connection details.
        sts_url: URL to the STS service.
        token_provider: A token provider generating authentication credentials.
        session_duration_seconds: The duration, in seconds, for which the session should
            be valid.

    Raises:
        LookupError: If a required parameter is not specified and cannot be determined
            from the environment.
    """

    if discovery is None:
        discovery = h2o_discovery.discover()

    if sts_url is None:
        sts_url = _lookup_service_uri(discovery, _STS_DISCOVERY_SERVICE_NAME)

    if token_provider is None:
        token_provider = _lookup_token_provider(discovery)

    session = aiobotocore.session.AioSession()
    provider = sts.AsyncCredentialProvider(
        sts_url=sts_url,
        token_provider=token_provider,
        client_creator=session.create_client,
        session_duration_seconds=session_duration_seconds,
    )
    session.get_component("credential_provider").providers.insert(0, provider)
    return session


def _lookup_service_uri(discovery: h2o_discovery.Discovery, service_name: str) -> str:
    service = discovery.services.get(service_name)
    if service is not None:
        return service.uri

    raise LookupError(
        f"Cannot determine {service_name} URI. Entry missing from Cloud Discovery."
    )


def _lookup_token_provider(discovery: h2o_discovery.Discovery) -> sts.TokenProvider:
    try:
        return h2o_authn.discovery.create(discovery)
    except (KeyError, ValueError) as e:
        raise LookupError(
            "Cannot determine the token provider. If a custom `discovery` object was "
            "provided, ensure it is configured correctly.\n\n"
            "Otherwise, if running from outside of the H2O AI Cloud network, this "
            "error likely indicates:\n"
            "1. If using the H2O CLI, it is not configured correctly.\n"
            "2. If not using the H2O CLI, the H2O_CLOUD_CLIENT_PLATFORM_TOKEN is not "
            "set with the H2O AI Cloud platform token."
        ) from e
