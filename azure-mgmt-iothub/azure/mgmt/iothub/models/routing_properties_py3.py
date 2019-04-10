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


class RoutingProperties(Model):
    """The routing related properties of the IoT hub. See:
    https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging.

    :param endpoints:
    :type endpoints: ~azure.mgmt.iothub.models.RoutingEndpoints
    :param routes: The list of user-provided routing rules that the IoT hub
     uses to route messages to built-in and custom endpoints. A maximum of 100
     routing rules are allowed for paid hubs and a maximum of 5 routing rules
     are allowed for free hubs.
    :type routes: list[~azure.mgmt.iothub.models.RouteProperties]
    :param fallback_route: The properties of the route that is used as a
     fall-back route when none of the conditions specified in the 'routes'
     section are met. This is an optional parameter. When this property is not
     set, the messages which do not meet any of the conditions specified in the
     'routes' section get routed to the built-in eventhub endpoint.
    :type fallback_route: ~azure.mgmt.iothub.models.FallbackRouteProperties
    :param enrichments: The list of user-provided enrichments that the IoT hub
     applies to messages to be delivered to built-in and custom endpoints. See:
     https://aka.ms/telemetryoneventgrid
    :type enrichments: list[~azure.mgmt.iothub.models.EnrichmentProperties]
    """

    _attribute_map = {
        'endpoints': {'key': 'endpoints', 'type': 'RoutingEndpoints'},
        'routes': {'key': 'routes', 'type': '[RouteProperties]'},
        'fallback_route': {'key': 'fallbackRoute', 'type': 'FallbackRouteProperties'},
        'enrichments': {'key': 'enrichments', 'type': '[EnrichmentProperties]'},
    }

    def __init__(self, *, endpoints=None, routes=None, fallback_route=None, enrichments=None, **kwargs) -> None:
        super(RoutingProperties, self).__init__(**kwargs)
        self.endpoints = endpoints
        self.routes = routes
        self.fallback_route = fallback_route
        self.enrichments = enrichments
