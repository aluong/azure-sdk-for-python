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


class ContainerSettings(Model):
    """Settings for the container to be downloaded.

    All required parameters must be populated in order to send to Azure.

    :param image_source_registry: Required. Registry to download the container
     from.
    :type image_source_registry:
     ~azure.mgmt.batchai.models.ImageSourceRegistry
    """

    _validation = {
        'image_source_registry': {'required': True},
    }

    _attribute_map = {
        'image_source_registry': {'key': 'imageSourceRegistry', 'type': 'ImageSourceRegistry'},
    }

    def __init__(self, **kwargs):
        super(ContainerSettings, self).__init__(**kwargs)
        self.image_source_registry = kwargs.get('image_source_registry', None)