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


class LogSearchRuleResourcePatch(Model):
    """The log search rule resource for patch operations.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param enabled: The flag which indicates whether the Log Search rule is
     enabled. Value should be true or false. Possible values include: 'true',
     'false'
    :type enabled: str or ~azure.mgmt.monitor.models.Enabled
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LogSearchRuleResourcePatch, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.enabled = kwargs.get('enabled', None)
