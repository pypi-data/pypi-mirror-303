import os
from typing import Tuple

from cs_ai_common.typings.proxy import ProxyProviders


class ProxyApiClient:
    _username: str
    _password: str
    _base_proxy_url: str

    def __init__(self, proxy_provider: ProxyProviders):
        self._username, self._password, self._base_proxy_url = self.get_proxy_auth(proxy_provider)

    def get_proxy_ip(self) -> str:
        return self._base_proxy_url.format(self._username, self._password)
    
    def get_proxy_auth(self, provider: str) -> Tuple[str, str, str]:
        """
        Retrieves proxy authentication credentials from environment variables.
        Args:
            prefix (str): The prefix used to identify the environment variables.
        Returns:
            Tuple[str, str, str]: A tuple containing the username, password, and base proxy URL.
        Raises:
            ValueError: If any of the required environment variables are missing.
        """

        _username = os.getenv(f'{provider}_USERNAME', None)
        _password = os.getenv(f'{provider}_PASSWORD', None)
        _base_proxy_url = os.getenv(f'{provider}_BASE_URL', None)

        if any([_username is None, _password is None, _base_proxy_url is None]):
            raise ValueError('Missing proxy credentials')
        
        return _username, _password, _base_proxy_url