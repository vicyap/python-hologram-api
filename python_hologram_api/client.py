# -*- coding: utf-8 -*-

"""Main module."""
from .constants import HOLOGRAM_API_BASEURL

from .cellular import CellularLinks
from .devices import Devices


class HologramClient(object):
    """Hologram API Client class."""

    def __init__(self, api_key, base_url=HOLOGRAM_API_BASEURL):
        """Initialize client.

        Args:
            api_key (str): Hologram API Key. See https://dashboard.hologram.io/account/api.
            base_url (str, optional): Hologram API base url.
        """
        self._api_key = api_key
        self._base_url = base_url

        self.cell = CellularLinks(self)
        self.devices = Devices(self)

    @property
    def api_key(self):
        return self._api_key

    @property
    def base_url(self):
        return self._base_url
