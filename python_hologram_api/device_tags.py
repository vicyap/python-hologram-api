"""Device Tags module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class DeviceTags(object):
    """DeviceTags class.

    Device tags are user-configurable categories that you can use to classify
    your devices. A device may be linked to more than one tag.
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def list(self):
        """List Device Tags.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'devices/tags')
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def create(self, name):
        """Create a Device Tag.

        Args:
            name (str): Name for the new tag.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'devices/tags')
        params = {
            'apikey': self.client.api_key,
            'name': name
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def delete(self, tagid):
        """Delete a Device Tag.

        Args:
            tagid (int): The ID of the tag to delete.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'devices/tags/{}'.format(tagid))
        params = {
            'apikey': self.client.api_key,
        }
        resp = requests.delete(url, json=params)
        return resp.json()

    def link_devices(self, tagid, device_ids):
        """Link a List of Devices to a Tag.

        Args:
            tagid (int): The ID of the tag.
            device_ids (List[int]): List of device IDs to link to this tag.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'devices/tags/{}/link'.format(tagid))
        params = {
            'apikey': self.client.api_key,
            'deviceids': device_ids
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def unlink_devices(self, tagid, device_ids):
        """Unlink a List of Devices to a Tag.

        Args:
            tagid (int): The ID of the tag.
            device_ids (List[int]): List of device IDs to unlink to this tag.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'devices/tags/{}/unlink'.format(tagid))
        params = {
            'apikey': self.client.api_key,
            'deviceids': device_ids
        }
        resp = requests.post(url, json=params)
        return resp.json()
