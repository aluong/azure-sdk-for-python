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


class AuthInfo(Model):
    """The authorization properties for accessing the source code repository.

    All required parameters must be populated in order to send to Azure.

    :param token_type: Required. The type of Auth token. Possible values
     include: 'PAT', 'OAuth'
    :type token_type: str or
     ~azure.mgmt.containerregistry.v2019_04_01.models.TokenType
    :param token: Required. The access token used to access the source control
     provider.
    :type token: str
    :param refresh_token: The refresh token used to refresh the access token.
    :type refresh_token: str
    :param scope: The scope of the access token.
    :type scope: str
    :param expires_in: Time in seconds that the token remains valid
    :type expires_in: int
    """

    _validation = {
        'token_type': {'required': True},
        'token': {'required': True},
    }

    _attribute_map = {
        'token_type': {'key': 'tokenType', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'refresh_token': {'key': 'refreshToken', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'expires_in': {'key': 'expiresIn', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AuthInfo, self).__init__(**kwargs)
        self.token_type = kwargs.get('token_type', None)
        self.token = kwargs.get('token', None)
        self.refresh_token = kwargs.get('refresh_token', None)
        self.scope = kwargs.get('scope', None)
        self.expires_in = kwargs.get('expires_in', None)
