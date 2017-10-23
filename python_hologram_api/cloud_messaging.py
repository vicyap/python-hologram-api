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

    def send_message(self, device_id, data, tags=None):
        """Send a CSR Message.

        Args:
            device_id (int): Device ID to associate the message to.
            data (str): Data payload of the message.
            tags (List[str], optional): Additional topics to associate with the message.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'csr/rdm')
        params = {
            'apikey': self.client.api_key,
            'deviceid': device_id,
            'data': data,
            'tags': tags
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def list_messages(
            self,
            device_id=None,
            limit=None,
            org_id=None,
            topic_name=None,
            time_stamp_start=None,
            time_stamp_end=None):
        """List CSR Messages.

        Args:
            device_id (int, optional): Filter for messages originating from one device.
            limit (int, optional): Return a maximum of this many messages. Default is 25.
            org_id (int, optional): Filter for messages from devices belonging to this organization.
            topic_name (str, optional): Filter for messages with a given topic.
            time_stamp_start (int, optional): Only return messages received after this time (Unix timestamp).
            time_stamp_end (int, optional): Only return messages received before this time (Unix timestamp).

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'csr/rdm')
        params = {
            'apikey': self.client.api_key,
            'deviceid': device_id,
            'limit': limit,
            'orgid': org_id,
            'topicname': topic_name,
            'timestampstart': time_stamp_start,
            'timestampend': time_stamp_end
        }
        resp = requests.get(url, json=params)
        return resp.json()


class SMSMessaging(object):
    """SMS Messaging class."""

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def send_message(self, device_id, body, from_number=None):
        """Send SMS Message.

        There is no cost to send SMS messages to Hologram devices via API.

        Args:
            device_id (int): ID of the device to send to.
            body (str): ASCII Text representation of the SMS body.
            from_number (str, optional): Phone number to display as the sender.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'sms/incoming')
        params = {
            'apikey': self.client.api_key,
            'deviceid': device_id,
            'body': body,
            'fromnumber': from_number
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

    def send_message(self, device_ids, protocol, port, data=None, base64_data=None):
        """Send a Message to a List of Devices.

        Must send either data or base64data.

        Args:
            device_ids (List[int]): IDs of devices to send message.
            protocol (str): The protocol to use: 'TCP' or 'UDP'.
            port (int): The port to use.
            data (str): The data to send. Max length of 10k bytes.
            base64_data (str): The data to send, encoded in base64. Max length of 10k bytes.

        Returns:
            dict: the json response as a dictionary.
        """
        if (data is None and base64_data is None) or (data is not None and base64_data is not None):
            raise ValueError('Please provide either `data` or `base64_data`')
        url = urljoin(self.client.base_url, 'devices/messages')
        params = {
            'apikey': self.client.api_key,
            'deviceids': device_ids,
            'protocol': protocol,
            'port': port,
            'data': data,
            'base64data': base64_data
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def trigger_webhook(self, device_id, webhook_guid, data=None, base64_data=None):
        """Send Message to a Device via Webhook.

        This endpoint does not require authentication with your API key, as the
        webhook GUID serves as an authentication token. In order to generate a
        webhook URL, please visit the cloud configuration page for your device.

        Must send either data or base64data.

        Args:
            device_id (int): ID of the device to send to.
            webhook_guid (str): generated UUID for the webhook URL.
            data (str, optional): The data to send. Max length of 10k bytes.
            base64_data (str, optional): The data to send, encoded in base64. Max length of 10k bytes.

        Returns:
            int: Integer Code of responded HTTP Status, e.g. 404 or 200.
        """
        if (data is None and base64_data is None) or (data is not None and base64_data is not None):
            raise ValueError('Please provide either `data` or `base64_data`')
        url = urljoin(self.client.base_url, 'devices/messages/{}/{}'.format(device_id, webhook_guid))
        params = {
            'data': data,
            'base64data': base64_data
        }
        resp = requests.post(url, json=params)
        return resp.status_code
