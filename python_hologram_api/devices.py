"""Devices module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class Devices(object):
    """Devices class."""

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def list(self, orgid=None):
        """List Devices.

        Args:
            orgid (int, optional): Only return results for the given organization ID.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'devices')
        params = {
            'apikey': self.client.api_key,
            'orgid': orgid,
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def get(self, deviceid):
        """Get a Device.

        Args:
            deviceid (int): device id.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'devices/{}'.format(deviceid))
        params = {
            'apikey': self.client.api_key,
        }
        resp = requests.get(url, json=params)
        return resp.json()
