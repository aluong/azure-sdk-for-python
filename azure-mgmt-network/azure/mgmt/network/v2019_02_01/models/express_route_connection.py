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

from .sub_resource import SubResource


class ExpressRouteConnection(SubResource):
    """ExpressRouteConnection resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :ivar provisioning_state: The provisioning state of the resource. Possible
     values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.network.v2019_02_01.models.ProvisioningState
    :param express_route_circuit_peering: Required. The ExpressRoute circuit
     peering.
    :type express_route_circuit_peering:
     ~azure.mgmt.network.v2019_02_01.models.ExpressRouteCircuitPeeringId
    :param authorization_key: Authorization key to establish the connection.
    :type authorization_key: str
    :param routing_weight: The routing weight associated to the connection.
    :type routing_weight: int
    :param name: Required. The name of the resource.
    :type name: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'express_route_circuit_peering': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'express_route_circuit_peering': {'key': 'properties.expressRouteCircuitPeering', 'type': 'ExpressRouteCircuitPeeringId'},
        'authorization_key': {'key': 'properties.authorizationKey', 'type': 'str'},
        'routing_weight': {'key': 'properties.routingWeight', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteConnection, self).__init__(**kwargs)
        self.provisioning_state = None
        self.express_route_circuit_peering = kwargs.get('express_route_circuit_peering', None)
        self.authorization_key = kwargs.get('authorization_key', None)
        self.routing_weight = kwargs.get('routing_weight', None)
        self.name = kwargs.get('name', None)
