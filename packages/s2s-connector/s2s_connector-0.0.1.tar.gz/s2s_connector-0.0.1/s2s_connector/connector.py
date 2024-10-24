import logging
from datetime import datetime
import httpx

logger = logging.getLogger(__name__)

class S2SConnector:
    """
    A general-purpose Service-to-Service (S2S) connector for obtaining bearer tokens
    for authentication in service-to-service communication.
    """

    def __init__(self, auth_url, tenant, client_id, client_secret):
        """
        Initializes the S2SConnector with the necessary authentication parameters.

        Args:
            auth_url (str): The base URL of the authentication server.
            tenant (str): The tenant identifier.
            client_id (str): The client identifier (service name).
            client_secret (str): The client secret (API key).
        """
        self.auth_url = auth_url
        self.tenant = tenant
        self.client_id = client_id
        self.client_secret = client_secret
        self.session = httpx.AsyncClient()
        self.s2s_token = None
        self.token_expires = -1

    async def _refresh_access_token(self):
        """
        Refreshes the access token by making a POST request to the authentication server.
        """
        response = await self.session.post(
            f"{self.auth_url}/api/v1.3/auth",
            json={
                "source": {"tenant": self.tenant, "name": self.client_id},
                "apiKey": self.client_secret,
            },
        )
        if response.status_code == 200:
            logger.info("Access token was fetched")
            data = response.json()
            self.s2s_token = data["access"]
            self.token_expires = datetime.now().timestamp() + data["accessExpiresIn"]
        else:
            raise Exception(f"Failed to get access token: {response.text}")

    async def get_token(self):
        """
        Returns a valid access token, refreshing it if necessary.

        Returns:
            str: The access token.
        """
        if datetime.now().timestamp() >= self.token_expires or not self.s2s_token:
            await self._refresh_access_token()
        return self.s2s_token
