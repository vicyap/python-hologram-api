#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_hologram_api` package."""

import unittest

from python_hologram_api.client import HologramClient

MOCK_SERVER_BASEURL = 'https://private-anon-0564af53ca-hologram.apiary-mock.com/api/1/'


class TestHologramApi(unittest.TestCase):
    def setUp(self):
        self.client = HologramClient(api_key=None, base_url=MOCK_SERVER_BASEURL)

    def tearDown(self):
        pass


class TestDevices(TestHologramApi):
    def test_list_devices(self):
        """Test List Devices."""
        resp = self.client.devices.list()
        self.assertTrue(resp.get('success'))

    def test_get_device(self):
        """Test Get a Device."""
        deviceid = 1234
        resp = self.client.devices.get(deviceid)
        self.assertTrue(resp.get('success'))


class TestCellularLinks(TestHologramApi):
    def test_activate_sims(self):
        """Test Activate SIMs."""
        sims = ['99990000000012345678']
        plan = 73
        tier = 1
        resp = self.client.cell.activate_sims(sims, plan, tier)
        self.assertTrue(resp.get('success'))

    def test_list_cellular_links(self):
        """Test List Cellular Links."""
        resp = self.client.cell.list_links()
        self.assertTrue(resp.get('success'))

    def test_get_cellular_link(self):
        """Test Get Cellular Link."""
        linkid = 54321
        resp = self.client.cell.get_link(linkid)
        self.assertTrue(resp.get('success'))

    def test_change_plan(self):
        """Test Change Plan."""
        linkid = 54321
        plan = 73
        tier = 1
        resp = self.client.cell.change_plan(linkid, plan, tier)
        self.assertTrue(resp.get('success'))

    def test_change_overage_limit(self):
        """Test Change Overage Limit."""
        linkid = 54321
        limit = 20000
        resp = self.client.cell.change_overage_limit(linkid, limit)
        self.assertTrue(resp.get('success'))

    def test_pause_data(self):
        """Test Pause Data."""
        linkid = 54321
        resp = self.client.cell.pause_link(linkid)
        self.assertTrue(resp.get('success'))

    def test_unpause_data(self):
        """Test Unpause Data."""
        linkid = 54321
        resp = self.client.cell.unpause_link(linkid)
        self.assertTrue(resp.get('success'))


class TestDeviceTags(TestHologramApi):
    def test_list_device_tags(self):
        """Test List Device Tags."""
        resp = self.client.tags.list()
        self.assertTrue(resp.get('success'))

    def test_create_device_tag(self):
        """Test Create Device Tag."""
        name = "My Tag"
        resp = self.client.tags.create(name)
        self.assertTrue(resp.get('success'))

    def test_delete_device_tag(self):
        """Test Delete Device Tag."""
        tagid = 1234
        resp = self.client.tags.delete(tagid)
        self.assertTrue(resp.get('success'))

    def test_link_device_tag(self):
        """Test Link a Device to a Tag."""
        tagid = 1234
        device_ids = [4321]
        resp = self.client.tags.link_devices(tagid, device_ids)
        self.assertTrue(resp.get('success'))

    def test_unlink_device_tag(self):
        """Test Unlink a Device to a Tag."""
        tagid = 1234
        device_ids = [4321]
        resp = self.client.tags.unlink_devices(tagid, device_ids)
        self.assertTrue(resp.get('success'))


class TestDataPlans(TestHologramApi):
    def test_list_data_plans(self):
        """Test List Data Plans."""
        resp = self.client.data_plans.list()
        self.assertTrue(resp.get('success'))

    def test_get_data_plan(self):
        """Test Get Data Plan."""
        planid = 127
        resp = self.client.data_plans.get(planid)
        self.assertTrue(resp.get('success'))


class TestCSRMessaging(TestHologramApi):
    def test_send_csr_message(self):
        """Test Send CSR Message."""
        deviceid = 54321
        data = 'Hello, Hologram!'
        resp = self.client.csr.send_message(deviceid, data)
        self.assertTrue(resp.get('success'))

    @unittest.skip('no json could be decoded')
    def test_list_csr_messages(self):
        """Test List CSR Messages."""
        deviceid = 54321
        limit = 100
        orgid = 3222
        topicname = '_RESTAPI_'
        timestampstart = 1480550400
        timestampend = 1480550400
        resp = self.client.csr.list_messages(
            deviceid=deviceid,
            limit=limit,
            orgid=orgid,
            topicname=topicname,
            timestampstart=timestampstart,
            timestampend=timestampend)
        self.assertTrue(resp.get('success'))


class TestSMSMessaging(TestHologramApi):
    def test_send_sms_message(self):
        """Test Send SMS Message."""
        deviceid = 1234
        body = 'Hello world!'
        resp = self.client.sms.send_message(deviceid, body)
        self.assertTrue(resp.get('success'))


class TestCloudToDeviceMessaging(TestHologramApi):
    def test_send_message_to_device(self):
        """Test Send Message to Device."""
        deviceids = [1234, 1236]
        protocol = 'TCP'
        port = 80
        data = 'Hello world!'
        resp = self.client.cloud.send_message(deviceids, protocol, port, data=data)
        self.assertTrue(resp.get('success'))

    def test_send_message_to_device_webhook(self):
        """Test Send Message to Device via Webhook."""
        deviceid = 12345
        webhookguid = 'f56839c23a801251af8bf8c820f28a1f'
        data = 'Hello world!'
        resp = self.client.cloud.trigger_webhook(deviceid, webhookguid, data=data)
        self.assertEqual(200, resp)


class TestSpacebridge(TestHologramApi):
    def test_add_public_key(self):
        """Test Add Public Key."""
        public_key = 'ssh-rsa AAAAB3Nzaasdf... user@example.com'
        resp = self.client.spacebridge.add_public_key(public_key)
        self.assertTrue(resp.get('success'))

    def test_list_public_keys(self):
        """Test List Public Keys."""
        resp = self.client.spacebridge.list_public_keys()
        self.assertTrue(resp.get('success'))

    def test_disable_key(self):
        """Test Disable a Key."""
        tunnel_key_id = 1234
        resp = self.client.spacebridge.disable_key(tunnel_key_id)
        self.assertTrue(resp.get('success'))

    def test_enable_key(self):
        """Test Enable a Key."""
        tunnel_key_id = 1234
        resp = self.client.spacebridge.enable_key(tunnel_key_id)
        self.assertTrue(resp.get('success'))


class TestUserManagement(TestHologramApi):
    def test_current_user(self):
        """Test Get User Info."""
        resp = self.client.user.get_info()
        self.assertTrue(resp.get('success'))

    def test_user_balance(self):
        """Test User Balance."""
        resp = self.client.user.get_balance()
        self.assertTrue(resp.get('success'))

    def test_user_add_balance(self):
        """Test Add Balance."""
        amount = 123.5
        resp = self.client.user.add_balance(amount)
        self.assertTrue(resp.get('success'))

    @unittest.skip('There is a bug in the response json')
    def test_user_balance_history(self):
        """Test Balance History."""
        resp = self.client.user.balance_history()
        self.assertTrue(resp.get('success'))


class TestOrganizationManagement(TestHologramApi):
    @unittest.skip('There is no response from the mock server')
    def test_list_organizations(self):
        """Test List Organizations."""
        resp = self.client.org.list()
        self.assertTrue(resp.get('success'))

    @unittest.skip('There is no response from the mock server')
    def test_get_organization(self):
        """Test Get Organization."""
        org_id = 4321
        resp = self.client.org.get(org_id)
        self.assertTrue(resp.get('success'))

    def test_org_balance(self):
        """Test Organization Balance."""
        org_id = 2345
        resp = self.client.org.get_balance(org_id)
        self.assertTrue(resp.get('success'))

    def test_org_add_balance(self):
        """Test Organization Add Balance."""
        org_id = 54345
        amount = 123.5
        resp = self.client.org.add_balance(org_id, amount)
        self.assertTrue(resp.get('success'))

    @unittest.skip('There is a bug in the response json')
    def test_org_balance_history(self):
        """Test Organization Balance History."""
        org_id = 54345
        resp = self.client.org.balance_history(org_id)
        self.assertTrue(resp.get('success'))
