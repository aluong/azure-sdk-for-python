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


class Operation(Model):
    """Operation entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of the operation. Format:
     {resourceProviderNamespace}/{resourceType}/{read|write|delete|action}
    :vartype name: str
    :ivar display: Operation display values.
    :vartype display: ~azure.mgmt.databox.models.OperationDisplay
    :ivar properties: Operation properties.
    :vartype properties: object
    :ivar origin: Origin of the operation. Can be : user|system|user,system
    :vartype origin: str
    """

    _validation = {
        'name': {'readonly': True},
        'display': {'readonly': True},
        'properties': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'properties': {'key': 'properties', 'type': 'object'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = None
        self.properties = None
        self.origin = None