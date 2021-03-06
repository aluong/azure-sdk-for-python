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


class SubscriptionState(Model):
    """Subscription State object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param state: State of Azure Subscription. Possible values include:
     'Registered', 'Unregistered', 'Warned', 'Suspended', 'Deleted'
    :type state: str or ~azure.mgmt.storagesync.models.Reason
    :ivar istransitioning: Is Transitioning
    :vartype istransitioning: bool
    :param properties: Subscription state properties.
    :type properties: object
    """

    _validation = {
        'istransitioning': {'readonly': True},
    }

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'istransitioning': {'key': 'istransitioning', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionState, self).__init__(**kwargs)
        self.state = kwargs.get('state', None)
        self.istransitioning = None
        self.properties = kwargs.get('properties', None)
