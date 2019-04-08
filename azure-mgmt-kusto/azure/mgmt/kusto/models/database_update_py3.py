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

from .resource_py3 import Resource


class DatabaseUpdate(Resource):
    """Class representing an update to a Kusto database.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :ivar provisioning_state: The provisioned state of the resource. Possible
     values include: 'Running', 'Creating', 'Deleting', 'Succeeded', 'Failed',
     'Moving'
    :vartype provisioning_state: str or
     ~azure.mgmt.kusto.models.ProvisioningState
    :param soft_delete_period: The time the data should be kept before it
     stops being accessible to queries in TimeSpan.
    :type soft_delete_period: timedelta
    :param hot_cache_period: The time the data should be kept in cache for
     fast queries in TimeSpan.
    :type hot_cache_period: timedelta
    :param statistics: The statistics of the database.
    :type statistics: ~azure.mgmt.kusto.models.DatabaseStatistics
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'soft_delete_period': {'key': 'properties.softDeletePeriod', 'type': 'duration'},
        'hot_cache_period': {'key': 'properties.hotCachePeriod', 'type': 'duration'},
        'statistics': {'key': 'properties.statistics', 'type': 'DatabaseStatistics'},
    }

    def __init__(self, *, location: str=None, soft_delete_period=None, hot_cache_period=None, statistics=None, **kwargs) -> None:
        super(DatabaseUpdate, self).__init__(**kwargs)
        self.location = location
        self.provisioning_state = None
        self.soft_delete_period = soft_delete_period
        self.hot_cache_period = hot_cache_period
        self.statistics = statistics
