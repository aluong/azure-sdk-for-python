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


class TriggerRolloverRequest(Model):
    """Trigger Rollover Request.

    :param server_certificate: Certificate Data
    :type server_certificate: str
    """

    _attribute_map = {
        'server_certificate': {'key': 'serverCertificate', 'type': 'str'},
    }

    def __init__(self, *, server_certificate: str=None, **kwargs) -> None:
        super(TriggerRolloverRequest, self).__init__(**kwargs)
        self.server_certificate = server_certificate
