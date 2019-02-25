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


class Request(Model):
    """Request.

    All required parameters must be populated in order to send to Azure.

    :param series: Required. Time series data points. Points should be sorted
     by timestamp in ascending order to match the anomaly detection result. If
     the data is not sorted correctly or there is duplicated timestamp, the API
     will not work. In such case, an error message will be returned.
    :type series: list[~azure.cognitiveservices.anomalyfinder.models.Point]
    :param granularity: Required. Can only be one of yearly, monthly, weekly,
     daily, hourly or minutely. Granularity is used for verify whether input
     series is valid. Possible values include: 'yearly', 'monthly', 'weekly',
     'daily', 'hourly', 'minutely'
    :type granularity: str or
     ~azure.cognitiveservices.anomalyfinder.models.Granularity
    :param custom_interval: Custom Interval is used to set non-standard time
     interval, for example, if the series is 5 minutes, request can be set as
     {"granularity":"minutely", "customInterval":5}.
    :type custom_interval: int
    :param period: Optional argument, periodic value of a time series. If the
     value is null or does not present, the API will determine the period
     automatically.
    :type period: int
    :param max_anomaly_ratio: Optional argument, advanced model parameter, max
     anomaly ratio in a time series.
    :type max_anomaly_ratio: float
    :param sensitivity: Optional argument, advanced model parameter, between
     0-99, the lower the value is, the larger the margin value will be which
     means less anomalies will be accepted.
    :type sensitivity: int
    """

    _validation = {
        'series': {'required': True},
        'granularity': {'required': True},
    }

    _attribute_map = {
        'series': {'key': 'series', 'type': '[Point]'},
        'granularity': {'key': 'granularity', 'type': 'Granularity'},
        'custom_interval': {'key': 'customInterval', 'type': 'int'},
        'period': {'key': 'period', 'type': 'int'},
        'max_anomaly_ratio': {'key': 'maxAnomalyRatio', 'type': 'float'},
        'sensitivity': {'key': 'sensitivity', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(Request, self).__init__(**kwargs)
        self.series = kwargs.get('series', None)
        self.granularity = kwargs.get('granularity', None)
        self.custom_interval = kwargs.get('custom_interval', None)
        self.period = kwargs.get('period', None)
        self.max_anomaly_ratio = kwargs.get('max_anomaly_ratio', None)
        self.sensitivity = kwargs.get('sensitivity', None)
