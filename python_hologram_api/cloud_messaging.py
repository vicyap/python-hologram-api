"""Cloud Messaging module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class CSRMessaging(object):
    """Cloud Services Router (CSR) class."""

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def send_message(self, deviceid, data, tags=None):
        """Send a CSR Message.

        Args:
            deviceid (int): Device ID to associate the message to.
            data (str): Data payload of the message.
            tags (List[str], optional): Additional topics to associate with the message.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'csr/rdm')
        params = {
            'apikey': self.client.api_key,
            'deviceid': deviceid,
            'data': data,
            'tags': tags
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def list_messages(self, deviceid=None, limit=None, orgid=None, topicname=None, timestampstart=None, timestampend=None):
        """List CSR Messages.

        Args:
            deviceid (int, optional): Filter for messages originating from one device.
            limit (int, optional): Return a maximum of this many messages. Default is 25.
            orgid (int, optional): Filter for messages from devices belonging to this organization.
            topicname (str, optional): Filter for messages with a given topic.
            timestampstart (int, optional): Only return messages received after this time (Unix timestamp).
            timestampend (int, optional): Only return messages received before this time (Unix timestamp).

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'csr/rdm')
        params = {
            'apikey': self.client.api_key,
            'deviceid': deviceid,
            'limit': limit,
            'orgid': orgid,
            'topicname': topicname,
            'timestampstart': timestampstart,
            'timestampend': timestampend
        }
        resp = requests.get(url, json=params)
        return resp.json()


class SMSMessaging(object):
    """SMS Messaging class."""

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def send_message(self, deviceid, body, fromnumber=None):
        """Send SMS Message.

        There is no cost to send SMS messages to Hologram devices via API.

        Args:
            deviceid (int): ID of the device to send to.
            body (str): ASCII Text representation of the SMS body.
            fromnumber (str, optional): Phone number to display as the sender.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'sms/incoming')
        params = {
            'apikey': self.client.api_key,
            'deviceid': deviceid,
            'body': body,
            'fromnumber': fromnumber
        }
        resp = requests.post(url, json=params)
        return resp.json()


class CloudToDeviceMessaging(object):
    """Cloud To Device Messaging.

    Send a TCP or UDP message to one or more devices on the Hologram network.
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def send_message(self, deviceids, protocol, port, data=None, base64data=None):
        """Send a Message to a List of Devices.

        Args:
            device_ids (List[int]): IDs of devices to send message.
            protocol (str): The protocol to use: 'TCP' or 'UDP'.
            port (int): The port to use.
            data (str): The data to send. Max length of 10k bytes. Must send either data or base64data.
            base64data (str): The data to send, encoded in base64. Max length of 10k bytes. Must send either data or base64data.

        Returns:
            dict: the json response as a dictionary.
        """
        if (data is None and base64data is None) or (data is not None and base64data is not None):
            raise ValueError('Please provide either `data` or `base64data`')
        url = urljoin(self.client.base_url, 'devices/messages')
        params = {
            'apikey': self.client.api_key,
            'deviceids': deviceids,
            'protocol': protocol,
            'port': port,
            'data': data,
            'base64data': base64data
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def trigger_webhook(self, deviceid, webhookguid, data=None, base64data=None):
        """Send Message to a Device via Webhook.

        Args:
            deviceid (int): ID of the device to send to.
            webhookguid (str): generated UUID for the webhook URL.
            data (str, optional): The data to send. Max length of 10k bytes. Must send either data or base64data.
            base64data (str, optional): The data to send, encoded in base64. Max length of 10k bytes. Must send either data or base64data.

        Returns:
            int: Integer Code of responded HTTP Status, e.g. 404 or 200.
        """
        if (data is None and base64data is None) or (data is not None and base64data is not None):
            raise ValueError('Please provide either `data` or `base64data`')
        url = urljoin(self.client.base_url, 'devices/messages/{}/{}'.format(deviceid, webhookguid))
        params = {
            'data': data,
            'base64data': base64data
        }
        resp = requests.post(url, json=params)
        return resp.status_code
