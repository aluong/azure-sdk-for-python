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


class NextHopResult(Model):
    """The information about next hop from the specified VM.

    :param next_hop_type: Next hop type. Possible values include: 'Internet',
     'VirtualAppliance', 'VirtualNetworkGateway', 'VnetLocal',
     'HyperNetGateway', 'None'
    :type next_hop_type: str or
     ~azure.mgmt.network.v2019_02_01.models.NextHopType
    :param next_hop_ip_address: Next hop IP Address
    :type next_hop_ip_address: str
    :param route_table_id: The resource identifier for the route table
     associated with the route being returned. If the route being returned does
     not correspond to any user created routes then this field will be the
     string 'System Route'.
    :type route_table_id: str
    """

    _attribute_map = {
        'next_hop_type': {'key': 'nextHopType', 'type': 'str'},
        'next_hop_ip_address': {'key': 'nextHopIpAddress', 'type': 'str'},
        'route_table_id': {'key': 'routeTableId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NextHopResult, self).__init__(**kwargs)
        self.next_hop_type = kwargs.get('next_hop_type', None)
        self.next_hop_ip_address = kwargs.get('next_hop_ip_address', None)
        self.route_table_id = kwargs.get('route_table_id', None)
