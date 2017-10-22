"""User Account Management module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class User(object):
    """User class.

    Requests to the user account balance endpoints are equivalent to calling
    the organization account balance endpoints with the personal organization.
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def get_info(self):
        """Get Current User.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me')
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def get_balance(self):
        """Get Current Balance.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me/balance')
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def add_balance(self, amount):
        """Add Balance.

        Charge the user's configured billing source and add that amount
        to your account balance.

        Args:
            amount (float): Amount to add to current user balance.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me/balance')
        params = {
            'apikey': self.client.api_key,
            'addamount': amount
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def balance_history(self):
        """Get Balance History.

        Retreive a history of transactions (credits and charges).

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me/balancehistory')
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()
