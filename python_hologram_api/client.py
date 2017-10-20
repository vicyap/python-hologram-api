# -*- coding: utf-8 -*-

"""Main module."""
try:
    # python 3
    from urllib.parse import urljoin
except ImportError:
    # python 2
    from urlparse import urljoin

import requests

HOLOGRAM_API_BASEURL = 'https://dashboard.hologram.io/api/1/'


class HologramClient(object):
    def __init__(self, api_key, base_url=HOLOGRAM_API_BASEURL):
        self.api_key = api_key
        self.base_url = base_url

    def list_devices(self, orgid=None):
        """List Devices.

        Args:
            orgid (int): Only return results for the given organization ID.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.base_url, 'devices')
        params = {
            'apikey': self.api_key,
            'orgid': orgid,
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def get_device(self, deviceid):
        """Get a Device.

        Args:
            deviceid (int): device id.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.base_url, 'devices/{}'.format(deviceid))
        params = {
            'apikey': self.api_key,
        }
        resp = requests.get(url, json=params)
        return resp.json()
