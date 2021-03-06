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


class MatchCondition(Model):
    """Define match conditions.

    All required parameters must be populated in order to send to Azure.

    :param match_variables: Required. List of match variables
    :type match_variables:
     list[~azure.mgmt.network.v2018_12_01.models.MatchVariable]
    :param operator: Required. Describes operator to be matched. Possible
     values include: 'IPMatch', 'Equal', 'Contains', 'LessThan', 'GreaterThan',
     'LessThanOrEqual', 'GreaterThanOrEqual', 'BeginsWith', 'EndsWith', 'Regex'
    :type operator: str or
     ~azure.mgmt.network.v2018_12_01.models.WebApplicationFirewallOperator
    :param negation_conditon: Describes if this is negate condition or not
    :type negation_conditon: bool
    :param match_values: Required. Match value
    :type match_values: list[str]
    :param transforms: List of transforms
    :type transforms: list[str or
     ~azure.mgmt.network.v2018_12_01.models.WebApplicationFirewallTransform]
    """

    _validation = {
        'match_variables': {'required': True},
        'operator': {'required': True},
        'match_values': {'required': True},
    }

    _attribute_map = {
        'match_variables': {'key': 'matchVariables', 'type': '[MatchVariable]'},
        'operator': {'key': 'operator', 'type': 'str'},
        'negation_conditon': {'key': 'negationConditon', 'type': 'bool'},
        'match_values': {'key': 'matchValues', 'type': '[str]'},
        'transforms': {'key': 'transforms', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(MatchCondition, self).__init__(**kwargs)
        self.match_variables = kwargs.get('match_variables', None)
        self.operator = kwargs.get('operator', None)
        self.negation_conditon = kwargs.get('negation_conditon', None)
        self.match_values = kwargs.get('match_values', None)
        self.transforms = kwargs.get('transforms', None)
