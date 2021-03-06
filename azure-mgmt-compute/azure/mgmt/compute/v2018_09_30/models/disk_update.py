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


class DiskUpdate(Model):
    """Disk update resource.

    :param os_type: the Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_09_30.models.OperatingSystemTypes
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings_collection: Encryption settings collection used
     be Azure Disk Encryption, can contain multiple encryption settings per
     disk or snapshot.
    :type encryption_settings_collection:
     ~azure.mgmt.compute.v2018_09_30.models.EncryptionSettingsCollection
    :param disk_iops_read_write: The number of IOPS allowed for this disk;
     only settable for UltraSSD disks. One operation can transfer between 4k
     and 256k bytes.
    :type disk_iops_read_write: long
    :param disk_mbps_read_write: The bandwidth allowed for this disk; only
     settable for UltraSSD disks. MBps means millions of bytes per second - MB
     here uses the ISO notation, of powers of 10.
    :type disk_mbps_read_write: int
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku:
    :type sku: ~azure.mgmt.compute.v2018_09_30.models.DiskSku
    """

    _attribute_map = {
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings_collection': {'key': 'properties.encryptionSettingsCollection', 'type': 'EncryptionSettingsCollection'},
        'disk_iops_read_write': {'key': 'properties.diskIOPSReadWrite', 'type': 'long'},
        'disk_mbps_read_write': {'key': 'properties.diskMBpsReadWrite', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'DiskSku'},
    }

    def __init__(self, **kwargs):
        super(DiskUpdate, self).__init__(**kwargs)
        self.os_type = kwargs.get('os_type', None)
        self.disk_size_gb = kwargs.get('disk_size_gb', None)
        self.encryption_settings_collection = kwargs.get('encryption_settings_collection', None)
        self.disk_iops_read_write = kwargs.get('disk_iops_read_write', None)
        self.disk_mbps_read_write = kwargs.get('disk_mbps_read_write', None)
        self.tags = kwargs.get('tags', None)
        self.sku = kwargs.get('sku', None)
