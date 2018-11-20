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


class EmailTemplateUpdateParameters(Model):
    """Email Template update Parameters.

    :param subject: Subject of the Template.
    :type subject: str
    :param title: Title of the Template.
    :type title: str
    :param description: Description of the Email Template.
    :type description: str
    :param body: Email Template Body. This should be a valid XDocument
    :type body: str
    :param parameters: Email Template Parameter values.
    :type parameters:
     list[~azure.mgmt.apimanagement.models.EmailTemplateParametersContractProperties]
    """

    _validation = {
        'subject': {'max_length': 1000, 'min_length': 1},
        'body': {'min_length': 1},
    }

    _attribute_map = {
        'subject': {'key': 'properties.subject', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'body': {'key': 'properties.body', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': '[EmailTemplateParametersContractProperties]'},
    }

    def __init__(self, *, subject: str=None, title: str=None, description: str=None, body: str=None, parameters=None, **kwargs) -> None:
        super(EmailTemplateUpdateParameters, self).__init__(**kwargs)
        self.subject = subject
        self.title = title
        self.description = description
        self.body = body
        self.parameters = parameters