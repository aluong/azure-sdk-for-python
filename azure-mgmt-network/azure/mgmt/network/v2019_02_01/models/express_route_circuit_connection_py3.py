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

from .sub_resource_py3 import SubResource


class ExpressRouteCircuitConnection(SubResource):
    """Express Route Circuit Connection in an ExpressRouteCircuitPeering resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param express_route_circuit_peering: Reference to Express Route Circuit
     Private Peering Resource of the circuit initiating connection.
    :type express_route_circuit_peering:
     ~azure.mgmt.network.v2019_02_01.models.SubResource
    :param peer_express_route_circuit_peering: Reference to Express Route
     Circuit Private Peering Resource of the peered circuit.
    :type peer_express_route_circuit_peering:
     ~azure.mgmt.network.v2019_02_01.models.SubResource
    :param address_prefix: /29 IP address space to carve out Customer
     addresses for tunnels.
    :type address_prefix: str
    :param authorization_key: The authorization key.
    :type authorization_key: str
    :ivar circuit_connection_status: Express Route Circuit connection state.
     Possible values include: 'Connected', 'Connecting', 'Disconnected'
    :vartype circuit_connection_status: str or
     ~azure.mgmt.network.v2019_02_01.models.CircuitConnectionStatus
    :ivar provisioning_state: Provisioning state of the circuit connection
     resource. Possible values are: 'Succeeded', 'Updating', 'Deleting', and
     'Failed'.
    :vartype provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'circuit_connection_status': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'express_route_circuit_peering': {'key': 'properties.expressRouteCircuitPeering', 'type': 'SubResource'},
        'peer_express_route_circuit_peering': {'key': 'properties.peerExpressRouteCircuitPeering', 'type': 'SubResource'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'authorization_key': {'key': 'properties.authorizationKey', 'type': 'str'},
        'circuit_connection_status': {'key': 'properties.circuitConnectionStatus', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, express_route_circuit_peering=None, peer_express_route_circuit_peering=None, address_prefix: str=None, authorization_key: str=None, name: str=None, **kwargs) -> None:
        super(ExpressRouteCircuitConnection, self).__init__(id=id, **kwargs)
        self.express_route_circuit_peering = express_route_circuit_peering
        self.peer_express_route_circuit_peering = peer_express_route_circuit_peering
        self.address_prefix = address_prefix
        self.authorization_key = authorization_key
        self.circuit_connection_status = None
        self.provisioning_state = None
        self.name = name
        self.etag = None
