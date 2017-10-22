"""Spacebridge module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class Spacebridge(object):
    """Spacebridge class."""

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

    def list_public_keys(self, withdisabled=0):
        """List Public Keys.

        Args:
            withdisabled (int, optional): Set to 1 to include disabled keys.

        Returns:
            dict: the json response as a dictionary.
        """
        if withdisabled not in {0, 1}:
            raise ValueError("`withdisabled` must be either 0 or 1.")
        url = urljoin(self.client.base_url, 'tunnelkeys')
        params = {
            'apikey': self.client.api_key,
            'withdisabled': withdisabled
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
