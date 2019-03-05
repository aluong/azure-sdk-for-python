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


class AKSProperties(Model):
    """AKS properties.

    :param cluster_fqdn: Cluster full qualified domain name
    :type cluster_fqdn: str
    :param system_services: System services
    :type system_services:
     list[~azure.mgmt.machinelearningservices.models.SystemService]
    :param agent_count: Number of agents
    :type agent_count: int
    :param agent_vm_size: Agent virtual machine size
    :type agent_vm_size: str
    :param ssl_configuration: SSL configuration
    :type ssl_configuration:
     ~azure.mgmt.machinelearningservices.models.SslConfiguration
    """

    _validation = {
        'agent_count': {'minimum': 1},
    }

    _attribute_map = {
        'cluster_fqdn': {'key': 'clusterFqdn', 'type': 'str'},
        'system_services': {'key': 'systemServices', 'type': '[SystemService]'},
        'agent_count': {'key': 'agentCount', 'type': 'int'},
        'agent_vm_size': {'key': 'agentVMSize', 'type': 'str'},
        'ssl_configuration': {'key': 'sslConfiguration', 'type': 'SslConfiguration'},
    }

    def __init__(self, *, cluster_fqdn: str=None, system_services=None, agent_count: int=None, agent_vm_size: str=None, ssl_configuration=None, **kwargs) -> None:
        super(AKSProperties, self).__init__(**kwargs)
        self.cluster_fqdn = cluster_fqdn
        self.system_services = system_services
        self.agent_count = agent_count
        self.agent_vm_size = agent_vm_size
        self.ssl_configuration = ssl_configuration