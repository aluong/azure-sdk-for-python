# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualHubRoute(Model):
    """VirtualHub route.

    :param address_prefixes: List of all addressPrefixes.
    :type address_prefixes: list[str]
    :param next_hop_ip_address: NextHop ip address.
    :type next_hop_ip_address: str
    """

    _attribute_map = {
        'address_prefixes': {'key': 'addressPrefixes', 'type': '[str]'},
        'next_hop_ip_address': {'key': 'nextHopIpAddress', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualHubRoute, self).__init__(**kwargs)
        self.address_prefixes = kwargs.get('address_prefixes', None)
        self.next_hop_ip_address = kwargs.get('next_hop_ip_address', None)
