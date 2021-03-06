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


class DataContainer(Model):
    """Information about a container with data for a given resource.

    All required parameters must be populated in order to send to Azure.

    :param workspace: Required. Log Analytics workspace information.
    :type workspace: ~azure.mgmt.monitor.models.WorkspaceInfo
    """

    _validation = {
        'workspace': {'required': True},
    }

    _attribute_map = {
        'workspace': {'key': 'workspace', 'type': 'WorkspaceInfo'},
    }

    def __init__(self, **kwargs):
        super(DataContainer, self).__init__(**kwargs)
        self.workspace = kwargs.get('workspace', None)
