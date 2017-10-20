#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_hologram_api` package."""

import unittest

import requests

from python_hologram_api.client import HologramClient

MOCK_SERVER_BASEURL = 'https://private-anon-0564af53ca-hologram.apiary-mock.com/api/1/'


class TestDevices(unittest.TestCase):
    def setUp(self):
        self.client = HologramClient(None, base_url=MOCK_SERVER_BASEURL)

    def tearDown(self):
        pass

    def test_000(self):
        """Test list devices."""
        devices = self.client.list_devices()
        self.assertTrue(devices.get('success'))

    def test_001(self):
        """Test get device."""
        device = self.client.get_device(1234)
        self.assertTrue(device.get('success'))
