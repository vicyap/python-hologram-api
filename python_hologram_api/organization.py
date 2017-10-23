"""Organization Account Management module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class Organization(object):
    """Organization class.

    Organizations allow multiple users to share access to the same devices and
    billing account. See the guide for more information.
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def list(self):
        """List Organizations.

        List all organizations that you are a member of. This includes the
        special "personal" organization tied to your user.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'organizations')
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def get(self, org_id):
        """Get an Organization.

        Args:
            org_id (int): The organization's unique identifier.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'organizations/{}'.format(org_id))
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def get_balance(self, org_id):
        """Get Current Balance.

        Args:
            org_id (int): The organization's unique identifier.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'organizations/{}/balance'.format(org_id))
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def add_balance(self, org_id, amount):
        """Add Balance.

        Charge the organization's configured billing source and add that
        amount to the account balance

        Args:
            org_id (int): The organization's unique identifier.
            amount (float): Amount to add to current user balance.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'organizations/{}/balance'.format(org_id))
        params = {
            'apikey': self.client.api_key,
            'addamount': amount
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def balance_history(self, org_id):
        """Get Balance History.

        Retreive a history of transactions (credits and charges).

        Args:
            org_id (int): The organization's unique identifier.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'organizations/{}/balancehistory'.format(org_id))
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()
