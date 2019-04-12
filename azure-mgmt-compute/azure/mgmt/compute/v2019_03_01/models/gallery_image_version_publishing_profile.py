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

from .gallery_artifact_publishing_profile_base import GalleryArtifactPublishingProfileBase


class GalleryImageVersionPublishingProfile(GalleryArtifactPublishingProfileBase):
    """The publishing profile of a gallery Image Version.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param target_regions: The target regions where the Image Version is going
     to be replicated to. This property is updatable.
    :type target_regions:
     list[~azure.mgmt.compute.v2019_03_01.models.TargetRegion]
    :param source: Required.
    :type source: ~azure.mgmt.compute.v2019_03_01.models.GalleryArtifactSource
    :param replica_count: The number of replicas of the Image Version to be
     created per region. This property would take effect for a region when
     regionalReplicaCount is not specified. This property is updatable.
    :type replica_count: int
    :param exclude_from_latest: If set to true, Virtual Machines deployed from
     the latest version of the Image Definition won't use this Image Version.
    :type exclude_from_latest: bool
    :ivar published_date: The timestamp for when the gallery Image Version is
     published.
    :vartype published_date: datetime
    :param end_of_life_date: The end of life date of the gallery Image
     Version. This property can be used for decommissioning purposes. This
     property is updatable.
    :type end_of_life_date: datetime
    :param storage_account_type: Specifies the storage account type to be used
     to store the image. This property is not updatable. Possible values
     include: 'Standard_LRS', 'Standard_ZRS'
    :type storage_account_type: str or
     ~azure.mgmt.compute.v2019_03_01.models.StorageAccountType
    """

    _validation = {
        'source': {'required': True},
        'published_date': {'readonly': True},
    }

    _attribute_map = {
        'target_regions': {'key': 'targetRegions', 'type': '[TargetRegion]'},
        'source': {'key': 'source', 'type': 'GalleryArtifactSource'},
        'replica_count': {'key': 'replicaCount', 'type': 'int'},
        'exclude_from_latest': {'key': 'excludeFromLatest', 'type': 'bool'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'end_of_life_date': {'key': 'endOfLifeDate', 'type': 'iso-8601'},
        'storage_account_type': {'key': 'storageAccountType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GalleryImageVersionPublishingProfile, self).__init__(**kwargs)
        self.replica_count = kwargs.get('replica_count', None)
        self.exclude_from_latest = kwargs.get('exclude_from_latest', None)
        self.published_date = None
        self.end_of_life_date = kwargs.get('end_of_life_date', None)
        self.storage_account_type = kwargs.get('storage_account_type', None)
