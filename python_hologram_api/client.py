# -*- coding: utf-8 -*-

"""Main module."""
from .constants import HOLOGRAM_API_BASEURL

from .cellular import CellularLinks
from .cloud_messaging import CSRMessaging, SMSMessaging, CloudToDeviceMessaging
from .data_plans import DataPlans
from .devices import Devices
from .device_tags import DeviceTags
from .organization import Organization
from .spacebridge import Spacebridge
from .user import User


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
        self.cloud = CloudToDeviceMessaging(self)
        self.csr = CSRMessaging(self)
        self.data_plans = DataPlans(self)
        self.devices = Devices(self)
        self.org = Organization(self)
        self.sms = SMSMessaging(self)
        self.spacebridge = Spacebridge(self)
        self.tags = DeviceTags(self)
        self.user = User(self)

    @property
    def api_key(self):
        """Return api_key."""
        return self._api_key

    @property
    def base_url(self):
        """Return base_url."""
        return self._base_url
