"""Cellular Links module."""

try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests


class CellularLinks(object):
    """CellularLinks class."""

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def activate_sims(self, sims, plan, tier):
        """Activate SIMs.

        Args:
            sims (List[str]): array of SIM numbers to activate.
            plan (int): Device data plan. Look up plan IDs with List Data Plans.
            tier (int): Geographic zone. Currently the valid tiers are 1 and 2.
                Higher tiers incur higher costs. See pricing for details.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/bulkclaim')
        params = {
            'apikey': self.client.api_key,
            'sims': sims,
            'plan': plan,
            'tier': tier
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def list_links(self, orgid=None):
        """List Cellular Links

        Args:
            orgid (int, optional): Only return results for the given organization ID.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular')
        params = {
            'apikey': self.client.api_key,
            'orgid': orgid
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def get_link(self, linkid):
        """Get Cellular Link.

        Args:
            linkid (int): Integer ID of the link to retrieve.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}'.format(linkid))
        params = {
            'apikey': self.client.api_key
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def change_plan(self, linkid, plan, tier):
        """Change Plan.

        Args:
            linkid (int): Integer ID of the link to change.
            plan (int): Device data plan. Look up plan IDs with List Data Plans.
            tier (int): Geographic zone. Currently the valid tiers are 1 and 2.
                Higher tiers incur higher costs. See pricing for details.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/changeplan'.format(linkid))
        params = {
            'apikey': self.client.api_key,
            'plan': plan,
            'tier': tier
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def change_overage_limit(self, linkid, limit):
        """Change Overage Limit.

        Args:
            linkid (int): Integer ID of the link to modify.
            limit (int): Number of bytes over the plan limit to allow. Set -1 for no data limit.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/overagelimit'.format(linkid))
        params = {
            'apikey': self.client.api_key,
            'limit': limit
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def pause_link(self, linkid):
        """Pause Data.

        Args:
            linkid (int): Integer ID of the link to modify.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/state'.format(linkid))
        params = {
            'apikey': self.client.api_key,
            'state': 'pause'
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def unpause_link(self, linkid):
        """Unpause Data.

        Args:
            linkid (int): Integer ID of the link to modify.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/state'.format(linkid))
        params = {
            'apikey': self.client.api_key,
            'state': 'live'
        }
        resp = requests.post(url, json=params)
        return resp.json()
