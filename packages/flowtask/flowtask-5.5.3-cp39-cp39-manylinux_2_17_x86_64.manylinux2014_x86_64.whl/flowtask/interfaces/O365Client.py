from abc import abstractmethod
from typing import Any
from collections.abc import Callable
import asyncio
from concurrent.futures import ThreadPoolExecutor
import msal
from office365.graph_client import GraphClient
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.auth.client_credential import ClientCredential
from navconfig.logging import logging
from navconfig import config
from ..exceptions import ComponentError
from ..conf import (
    SHAREPOINT_TENANT_NAME,
    O365_CLIENT_ID,
    O365_CLIENT_SECRET,
    O365_TENANT_ID,
)


logging.getLogger('msal').setLevel(logging.INFO)


class O365Client:
    """
    O365Client

    Overview

        The O365Client class is an abstract base class for managing connections to Office 365 services.
        It handles authentication, credential processing, and provides a method for obtaining the
        Office 365 context. It uses the Office 365 Python SDK for authentication and context management.

    .. table:: Properties
    :widths: auto

        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | Name             | Required | Description                                                                                      |
        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | url              |   No     | The base URL for the Office 365 service.                                                         |
        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | no_host          |   No     | A flag indicating if the host should be omitted, defaults to True.                               |
        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | tenant           |   Yes    | The tenant ID for the Office 365 service.                                                        |
        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | site             |   No     | The site URL for the Office 365 service.                                                         |
        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | auth_context     |   Yes    | The authentication context for Office 365.                                                       |
        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | context          |   Yes    | The context object for Office 365 operations.                                                    |
        +------------------+----------+--------------------------------------------------------------------------------------------------+
        | credentials      |   Yes    | A dictionary containing the credentials for authentication.                                      |
        +------------------+----------+--------------------------------------------------------------------------------------------------+

    Return

        The methods in this class manage the authentication and connection setup for Office 365 services,
        providing an abstract base for subclasses to implement specific service interactions.

    """  # noqa
    url: str = None
    no_host: bool = True

    _credentials: dict = {
        "username": str,
        "password": str,
        "client_id": str,
        "client_secret": str,
        "tenant": str,
        "site": str,
    }

    def __init__(self, *args, **kwargs) -> None:
        self.tenant: str = None
        self.tenant_id: str = None
        self.site: str = None
        self.auth_context: Any = None
        self.context: Any = None
        self.credentials: dict = kwargs.get('credentials', {})
        self._environment: Callable = config
        self._access_token: str = None
        self._graph_client: Callable = None
        self._logger = logging.getLogger(__name__)
        self._executor = ThreadPoolExecutor()
        # Default credentials
        self._default_tenant_id = O365_TENANT_ID
        self._default_client_id = O365_CLIENT_ID
        self._default_client_secret = O365_CLIENT_SECRET
        self._default_tenant_name = SHAREPOINT_TENANT_NAME

    def get_env_value(self, key, default: str = None):
        if val := self._environment.get(key, default):
            return val
        else:
            return key

    @abstractmethod
    def get_context(self, url: str, *args):
        pass

    @abstractmethod
    async def _start_(self, **kwargs):
        pass

    async def run_in_executor(self, fn, *args, **kwargs):
        """
        Calling any blocking process in an executor.
        """
        return await asyncio.get_event_loop().run_in_executor(
            self._executor, fn, *args, **kwargs
        )

    def process_office_credentials(self):
        for value, dtype in self._credentials.items():
            try:
                if value in self.credentials:
                    if type(self.credentials[value]) == dtype:  # noqa
                        # can process the credentials, extracted from environment or variables:
                        default = getattr(self, value, self.credentials[value])
                        val = self.get_env_value(
                            self.credentials[value], default=default
                        )
                        self.credentials[value] = val
            except (TypeError, KeyError) as err:
                logging.error(f"{__name__}: Wrong or missing Credentials")
                raise ComponentError(
                    f"{__name__}: Wrong or missing Credentials"
                ) from err
        ## getting Tenant and Site from credentials:
        try:
            self.tenant = self.credentials.get('tenant', self._default_tenant_name)
            self.site = self.credentials["site"] if "site" in self.credentials else None
        except KeyError as e:
            raise RuntimeError(
                f"Office365: Missing Tenant or Site Configuration: {e}."
            ) from e

    def connection(self):
        self.process_office_credentials()
        # calling before run:
        self._start_()
        # Processing The Credentials:
        if hasattr(self, "credentials"):
            username = self.credentials.get("username")
            password = self.credentials.get("password")
            client_id = self.credentials.get(
                "client_id", self._default_client_id
            )
            client_secret = self.credentials.get(
                "client_secret", self._default_client_secret
            )
        else:
            logging.error(
                "Office365: Wrong Credentials or missing Credentials")
            raise RuntimeError(
                "Office365: Wrong Credentials or missing Credentials"
            )
        try:
            if username is not None:
                self.context = ClientContext(self.url).with_credentials(
                    UserCredential(username, password)
                )
                token = self.user_auth(username, password)
                self._access_token = token.get('access_token')
            else:
                self.auth_context = ClientCredential(client_id, client_secret)
                self.context = self.get_context(self.url).with_credentials(
                    self.auth_context
                )
                token = self.acquire_token()
                self._access_token = token.get('access_token')
            # Create Graph client
            self._graph_client = GraphClient(
                acquire_token_callback=lambda: self.access_token
            )
            logging.debug("Office365: Authentication success")
        except Exception as err:
            logging.error(f"Office365: Authentication Error: {err}")
            raise RuntimeError(f"Office365: Authentication Error: {err}") from err
        return self

    def user_auth(self, username: str, password: str, scopes: list = None) -> dict:
        tenant = self.credentials.get('tenant_id', self._default_tenant_id)
        authority_url = f'https://login.microsoftonline.com/{tenant}'
        client_id = self.credentials.get("client_id", self._default_client_id)
        if not scopes:
            scopes = ["https://graph.microsoft.com/.default"]
        app = msal.PublicClientApplication(
            authority=authority_url,
            client_id=client_id,
            client_credential=None
        )
        result = app.acquire_token_by_username_password(
            username,
            password,
            scopes=scopes
        )
        if "access_token" not in result:
            error_message = result.get('error_description', 'Unknown error')
            error_code = result.get('error', 'Unknown error code')
            raise RuntimeError(
                f"Failed to obtain access token: {error_code} - {error_message}"
            )
        return result

    def acquire_token(self, scopes: list = None) -> dict:
        """
        Acquire a Token via MSAL.
        """
        client_id = self.credentials.get("client_id", self._default_client_id)
        client_secret = self.credentials.get("client_secret", self._default_client_secret)
        tenant = self.credentials.get('tenant_id', self._default_tenant_id)
        if not scopes:
            scopes = ["https://graph.microsoft.com/.default"]
        authority_url = f'https://login.microsoftonline.com/{tenant}'
        app = msal.ConfidentialClientApplication(
            authority=authority_url,
            client_id=client_id,
            client_credential=client_secret
        )
        result = app.acquire_token_for_client(
            scopes=scopes
        )
        if "access_token" not in result:
            error_message = result.get('error_description', 'Unknown error')
            error_code = result.get('error', 'Unknown error code')
            raise RuntimeError(
                f"Failed to obtain access token: {error_code} - {error_message}"
            )
        return result
