===================
python-hologram-api
===================

Python client for https://dashboard.hologram.io/api.

.. image:: https://img.shields.io/pypi/v/python-hologram-api.svg
        :target: https://pypi.python.org/pypi/python-hologram-api

.. image:: https://img.shields.io/travis/vicyap/python-hologram-api.svg
        :target: https://travis-ci.org/vicyap/python-hologram-api

.. image:: https://coveralls.io/repos/github/vicyap/python-hologram-api/badge.svg?branch=master
		:target: https://coveralls.io/github/vicyap/python-hologram-api?branch=master

.. image:: https://readthedocs.org/projects/python-hologram-api/badge/?version=latest
        :target: https://python-hologram-api.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Installation
------------

``pip install python-hologram-api``

Documentation
-------------

* Python API: https://python-hologram-api.readthedocs.io.
* HTTP API: https://hologram.io/docs/reference/cloud/http/

Usage
-----

``HologramClient`` is the main class you should use. Most of its methods are
sub-categorized based on the endpoint that the method interfaces with. For
example, user account management is under `client.user`.

To use python-hologram-api in a project:

.. code:: python

    import os
    from python_hologram_api.client import HologramClient

    HOLOGRAM_API_KEY = os.environ.get('HOLOGRAM_API_KEY')
    client = HologramClient(HOLOGRAM_API_KEY)

Example Usages:

.. code:: python

    # List Devices
    resp = client.devices.list()
    if resp.get('success'):
        devices = resp.get('data')

    # Get a Device
    device_id = 1234
    resp = client.devices.get(device_id)
    if resp.get('success'):
        device = resp.get('data')

    # Activate SIMs
    sims = ['99990000000012345678']
    plan = 73
    tier = 1
    resp = client.cell.activate_sims(sims, plan, tier)
    assert resp.get('success') is not None

The following submodules are available:

* Device Management

  * ``client.devices``
  * ``client.cell``
  * ``client.tags``
  * ``client.data_plans``

* Hologram Cloud

  * ``client.csr``
  * ``client.sms``
  * ``client.cloud``
  * ``client.spacebridge``

* Account Management

  * ``client.user``
  * ``client.org``

License
-------

* Free software: MIT license
