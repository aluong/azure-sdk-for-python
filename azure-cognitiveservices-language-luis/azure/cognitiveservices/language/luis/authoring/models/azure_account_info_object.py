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


class AzureAccountInfoObject(Model):
    """Defines the azure account information object.

    All required parameters must be populated in order to send to Azure.

    :param azure_subscription_id: Required. The id for the azure subscription.
    :type azure_subscription_id: str
    :param resource_group: Required. The azure resource group name.
    :type resource_group: str
    :param account_name: Required. The azure account name.
    :type account_name: str
    """

    _validation = {
        'azure_subscription_id': {'required': True},
        'resource_group': {'required': True},
        'account_name': {'required': True},
    }

    _attribute_map = {
        'azure_subscription_id': {'key': 'azureSubscriptionId', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'account_name': {'key': 'accountName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureAccountInfoObject, self).__init__(**kwargs)
        self.azure_subscription_id = kwargs.get('azure_subscription_id', None)
        self.resource_group = kwargs.get('resource_group', None)
        self.account_name = kwargs.get('account_name', None)
