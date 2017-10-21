# -*- coding: utf-8 -*-

"""Main module."""
from .constants import HOLOGRAM_API_BASEURL

from .devices import Devices


class HologramClient(object):
    def __init__(self, api_key, base_url=HOLOGRAM_API_BASEURL):
        self._api_key = api_key
        self._base_url = base_url

        self.devices = Devices(self)

    @property
    def api_key(self):
        return self._api_key

    @property
    def base_url(self):
        return self._base_url
