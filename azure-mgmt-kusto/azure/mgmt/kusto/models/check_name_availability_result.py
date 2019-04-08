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


class CheckNameAvailabilityResult(Model):
    """The result returned from a check name availability request.

    :param name_available: Specifies whether or not the name is available.
     Possible values include: 'Available', 'NotAvailable'
    :type name_available: str or ~azure.mgmt.kusto.models.NameAvailable
    :param name: The name that was checked.
    :type name: str
    :param message: Message indicating an unavailable name due to a conflict,
     or a description of the naming rules that are violated.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.name = kwargs.get('name', None)
        self.message = kwargs.get('message', None)
