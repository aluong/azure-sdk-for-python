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

from .resource import Resource


class ExpressRoutePortsLocation(Resource):
    """ExpressRoutePorts Peering Location.

    Definition of the ExpressRoutePorts peering location resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :ivar address: Address of peering location.
    :vartype address: str
    :ivar contact: Contact details of peering locations.
    :vartype contact: str
    :param available_bandwidths: The inventory of available ExpressRoutePort
     bandwidths.
    :type available_bandwidths:
     list[~azure.mgmt.network.v2019_02_01.models.ExpressRoutePortsLocationBandwidths]
    :ivar provisioning_state: The provisioning state of the
     ExpressRoutePortLocation resource. Possible values are: 'Succeeded',
     'Updating', 'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'address': {'readonly': True},
        'contact': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'address': {'key': 'properties.address', 'type': 'str'},
        'contact': {'key': 'properties.contact', 'type': 'str'},
        'available_bandwidths': {'key': 'properties.availableBandwidths', 'type': '[ExpressRoutePortsLocationBandwidths]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRoutePortsLocation, self).__init__(**kwargs)
        self.address = None
        self.contact = None
        self.available_bandwidths = kwargs.get('available_bandwidths', None)
        self.provisioning_state = None
