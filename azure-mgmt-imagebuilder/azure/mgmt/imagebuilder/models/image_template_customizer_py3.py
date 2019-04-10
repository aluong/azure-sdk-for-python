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


class ImageTemplateCustomizer(Model):
    """ImageTemplateCustomizer.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageTemplateShellCustomizer,
    ImageTemplateRestartCustomizer, ImageTemplatePowerShellCustomizer

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Shell': 'ImageTemplateShellCustomizer', 'WindowsRestart': 'ImageTemplateRestartCustomizer', 'PowerShell': 'ImageTemplatePowerShellCustomizer'}
    }

    def __init__(self, *, name: str=None, **kwargs) -> None:
        super(ImageTemplateCustomizer, self).__init__(**kwargs)
        self.name = name
        self.type = None
