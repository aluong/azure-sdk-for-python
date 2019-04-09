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


class ApplicationGatewayProbe(SubResource):
    """Probe of the application gateway.

    :param id: Resource ID.
    :type id: str
    :param protocol: The protocol used for the probe. Possible values are
     'Http' and 'Https'. Possible values include: 'Http', 'Https'
    :type protocol: str or
     ~azure.mgmt.network.v2019_02_01.models.ApplicationGatewayProtocol
    :param host: Host name to send the probe to.
    :type host: str
    :param path: Relative path of probe. Valid path starts from '/'. Probe is
     sent to <Protocol>://<host>:<port><path>
    :type path: str
    :param interval: The probing interval in seconds. This is the time
     interval between two consecutive probes. Acceptable values are from 1
     second to 86400 seconds.
    :type interval: int
    :param timeout: The probe timeout in seconds. Probe marked as failed if
     valid response is not received with this timeout period. Acceptable values
     are from 1 second to 86400 seconds.
    :type timeout: int
    :param unhealthy_threshold: The probe retry count. Backend server is
     marked down after consecutive probe failure count reaches
     UnhealthyThreshold. Acceptable values are from 1 second to 20.
    :type unhealthy_threshold: int
    :param pick_host_name_from_backend_http_settings: Whether the host header
     should be picked from the backend http settings. Default value is false.
    :type pick_host_name_from_backend_http_settings: bool
    :param min_servers: Minimum number of servers that are always marked
     healthy. Default value is 0.
    :type min_servers: int
    :param match: Criterion for classifying a healthy probe response.
    :type match:
     ~azure.mgmt.network.v2019_02_01.models.ApplicationGatewayProbeHealthResponseMatch
    :param provisioning_state: Provisioning state of the backend http settings
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the probe that is unique within an Application
     Gateway.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'host': {'key': 'properties.host', 'type': 'str'},
        'path': {'key': 'properties.path', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'int'},
        'timeout': {'key': 'properties.timeout', 'type': 'int'},
        'unhealthy_threshold': {'key': 'properties.unhealthyThreshold', 'type': 'int'},
        'pick_host_name_from_backend_http_settings': {'key': 'properties.pickHostNameFromBackendHttpSettings', 'type': 'bool'},
        'min_servers': {'key': 'properties.minServers', 'type': 'int'},
        'match': {'key': 'properties.match', 'type': 'ApplicationGatewayProbeHealthResponseMatch'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, protocol=None, host: str=None, path: str=None, interval: int=None, timeout: int=None, unhealthy_threshold: int=None, pick_host_name_from_backend_http_settings: bool=None, min_servers: int=None, match=None, provisioning_state: str=None, name: str=None, etag: str=None, type: str=None, **kwargs) -> None:
        super(ApplicationGatewayProbe, self).__init__(id=id, **kwargs)
        self.protocol = protocol
        self.host = host
        self.path = path
        self.interval = interval
        self.timeout = timeout
        self.unhealthy_threshold = unhealthy_threshold
        self.pick_host_name_from_backend_http_settings = pick_host_name_from_backend_http_settings
        self.min_servers = min_servers
        self.match = match
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
        self.type = type
