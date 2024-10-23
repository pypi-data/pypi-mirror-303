import typing

import aiobotocore.credentials
import aiobotocore.session
import botocore.credentials

# RoleArn is an arbitrary string from 20 to 2048 characters long.
_ROLE_ARN = "drivedrivedrivedrive"


@typing.runtime_checkable
class TokenProvider(typing.Protocol):
    """Defines the interface of the token provider.

    Token provider is used to obtain access token which is exchanged for a session
    token.
    """

    def __call__(self) -> str:
        """Returns fresh access token for accessing Drive STS."""


class StaticTokenProvider:
    """Implements TokenProvider interface and always returns static token passed."""

    def __init__(self, token: str) -> None:
        self._token = token

    def __call__(self) -> str:
        return self._token


class AsyncCredentialProvider(botocore.credentials.CredentialProvider):
    """Returns a new instance of a credential provider, supplying credentials which
    allow authentication to H2O Drive.

    The provider extends botocore.credentials.CredentialProvider, allowing it to be used
    as a source of credentials within botocore and boto3 sessions.

    The provider itself uses tokens returned by a token provider to authenticate against
    the Drive STS endpoint, where it sources its credentials. Credentials are refreshed
    automatically as needed.

    Args:
        sts_url: URL of Drive STS.
        token_provider: A callable supplying tokens for authenticating to Drive STS.
        client_creator: A callable creating clients for communicating with the STS
            service.
        session_duration_seconds: The duration of each session created, in seconds.
    """

    METHOD = "authenticate-drive-with-token"
    CANONICAL_NAME = "custom-h2o-authenticate-drive-with-token"

    def __init__(
        self,
        sts_url: str,
        token_provider: TokenProvider,
        client_creator,
        session_duration_seconds: int = 3600,
    ):
        super().__init__()
        self._sts_url = sts_url
        self._token_provider = token_provider
        self._client_creator = client_creator
        self._extra_assume_args = {
            "DurationSeconds": session_duration_seconds,
        }

    async def load(self) -> aiobotocore.credentials.AioRefreshableCredentials:
        fetcher = aiobotocore.credentials.AioAssumeRoleWithWebIdentityCredentialFetcher(
            client_creator=self._intercepted_client_creator,
            web_identity_token_loader=self._token_provider,
            role_arn=_ROLE_ARN,
            extra_args=self._extra_assume_args,
        )
        return aiobotocore.credentials.AioDeferredRefreshableCredentials(
            method=self.METHOD,
            refresh_using=fetcher.fetch_credentials,
        )

    # Override the endpoint URL in the client directly as custom URLs can't be supplied
    # to botocore/aiobotocore-implemented fetchers as arguments.
    def _intercepted_client_creator(self, *args, **kwargs):
        updated_kwargs = dict(kwargs, endpoint_url=self._sts_url)
        return self._client_creator(*args, **updated_kwargs)
