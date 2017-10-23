"""Spacebridge module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class Spacebridge(object):
    """Spacebridge class.

    See the Spacebridge guide for details.
    https://hologram.io/docs/guide/cloud/spacebridge-tunnel/
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def add_public_key(self, public_key):
        """Add Public Key.

        Associate an SSH key with your user. This key can then be used to
        tunnel to devices that you control.

        Args:
            public_key (str): SSH public key.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'tunnelkeys')
        params = {
            'apikey': self.client.api_key,
            'public_key': public_key
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def list_public_keys(self, with_disabled=False):
        """List Public Keys.

        Args:
            withdisabled (bool, optional): Set to True to include disabled keys.

        Returns:
            dict: the json response as a dictionary.
        """
        if type(with_disabled) is not bool:
            raise TypeError("`with_disabled` must be a boolean.")
        with_disabled = 1 if with_disabled else 0
        url = urljoin(self.client.base_url, 'tunnelkeys')
        params = {
            'apikey': self.client.api_key,
            'withdisabled': with_disabled
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def disable_key(self, tunnel_key_id):
        """Disable a Key.

        Args:
            tunnel_key_id (int): ID of the tunnel key to disable.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'tunnelkeys/{}/disable'.format(tunnel_key_id))
        params = {
            'apikey': self.client.api_key,
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def enable_key(self, tunnel_key_id):
        """Enable a Key.

        Args:
            tunnel_key_id (int): ID of the tunnel key to enable.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'tunnelkeys/{}/enable'.format(tunnel_key_id))
        params = {
            'apikey': self.client.api_key,
        }
        resp = requests.post(url, json=params)
        return resp.json()
