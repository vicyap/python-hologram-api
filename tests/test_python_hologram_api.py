#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_hologram_api` package."""

import unittest

import requests

from python_hologram_api.client import HologramClient

MOCK_SERVER_BASEURL = 'https://private-anon-0564af53ca-hologram.apiary-mock.com/api/1/'


class TestHologramApi(unittest.TestCase):
    def setUp(self):
        self.client = HologramClient(None, base_url=MOCK_SERVER_BASEURL)

    def tearDown(self):
        pass


class TestDevices(TestHologramApi):
    def test_list_devices(self):
        """Test List Devices."""
        # self.client.devices.list()
        pass

    def test_get_device(self):
        """Test Get a Device."""
        # self.client.devices.get()
        pass


class TestCellularLinks(TestHologramApi):
    def test_activate_sims(self):
        """Test Activate SIMs."""
        # self.client.cell.activate_sims()
        pass

    def test_list_cellular_links(self):
        """Test List Cellular Links."""
        # self.client.cell.list_links()
        pass

    def test_get_cellular_link(self):
        """Test Get Cellular Link."""
        # self.client.cell.get_links()
        pass

    def test_change_plan(self):
        """Test Change Plan."""
        # self.client.cell.change_plan()
        pass

    def test_change_overage_limit(self):
        """Test Change Overage Limit."""
        # self.client.cell.change_overage_limit()
        pass

    def test_change_cellular_state(self):
        """Test Pause or Unpause Data."""
        # self.client.cell.pause()
        # self.client.cell.unpause()
        pass


class TestDeviceTags(TestHologramApi):
    def test_list_device_tags(self):
        """Test List Device Tags."""
        # self.client.tag.list()
        pass

    def test_create_device_tag(self):
        """Test Create Device Tag."""
        # self.client.tag.create()
        pass

    def test_delete_device_tag(self):
        """Test Delete Device Tag."""
        # self.client.tag.delete()
        pass

    def test_link_device_tag(self):
        """Test Link a Device to a Tag."""
        # self.client.tag.link()
        pass

    def test_unlink_device_tag(self):
        """Test Unlink a Device to a Tag."""
        # self.client.tag.unlink()
        pass


class TestDataPlans(TestHologramApi):
    def test_list_data_plans(self):
        """Test List Data Plans."""
        # self.client.data.list_plans()
        pass

    def test_get_data_plan(self):
        """Test Get Data Plan."""
        # self.client.data.get_plan()
        pass


class TestHologramCloud(TestHologramApi):
    def test_send_csr_message(self):
        """Test Send CSR Message."""
        # self.client.csr.send_message()
        pass

    def test_list_csr_messages(self):
        """Test List CSR Messages."""
        # self.client.csr.list_messages()
        pass

    def test_send_sms_message(self):
        """Test Send SMS Message."""
        # self.client.sms.send_message()
        pass


class TestCloudToDeviceMessaging(TestHologramApi):
    def test_send_message_to_device(self):
        """Test Send Message to Device."""
        # self.client.cloud.send_message()
        pass

    def test_send_message_to_device_webhook(self):
        """Test Send Message to Device via Webhook."""
        # self.client.cloud.trigger_webhook()
        pass


class TestSpacebridge(TestHologramApi):
    def test_add_public_key(self):
        """Test Add Public Key."""
        # self.client.spacebridge.add_key()
        pass

    def test_list_public_keys(self):
        """Test List Public Keys."""
        # self.client.spacebridge.list_keys()
        pass

    def test_disable_key(self):
        """Test Disable a Key."""
        # self.client.spacebridge.disable_key()
        pass

    def test_enable_key(self):
        """Test Enable a Key."""
        # self.client.spacebridge.enable_key()
        pass


class TestAccountManagement(TestHologramApi):
    def test_current_user(self):
        """Test Get User Info."""
        # self.client.user.get_info()
        pass

    def test_user_balance(self):
        """Test User Balance."""
        # self.client.user.get_balance()
        pass

    def test_user_add_balance(self):
        """Test Add Balance."""
        # self.client.user.add_balance()
        pass

    def test_user_balance_history(self):
        """Test Balance History."""
        # self.client.user.balance_history()
        pass


class TestOrganizations(TestHologramApi):
    def test_list_organizations(self):
        """Test List Organizations."""
        # self.client.org.list_orgs()
        pass

    def test_get_organization(self):
        """Test Get Organization."""
        # self.client.org.get_org()
        pass

    def test_org_balance(self):
        """Test Organization Balance."""
        # self.client.org.get_balance()
        pass

    def test_org_add_balance(self):
        """Test Organization Add Balance."""
        # self.client.org.add_balance()
        pass

    def test_org_balance_history(self):
        """Test Organization Balance History."""
        # self.client.org.balance_history()
        pass
