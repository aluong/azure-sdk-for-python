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

from .proxy_only_resource import ProxyOnlyResource


class DomainPatchResource(ProxyOnlyResource):
    """ARM resource for a domain.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param contact_admin: Administrative contact.
    :type contact_admin: ~azure.mgmt.web.models.Contact
    :param contact_billing: Billing contact.
    :type contact_billing: ~azure.mgmt.web.models.Contact
    :param contact_registrant: Registrant contact.
    :type contact_registrant: ~azure.mgmt.web.models.Contact
    :param contact_tech: Technical contact.
    :type contact_tech: ~azure.mgmt.web.models.Contact
    :ivar registration_status: Domain registration status. Possible values
     include: 'Active', 'Awaiting', 'Cancelled', 'Confiscated', 'Disabled',
     'Excluded', 'Expired', 'Failed', 'Held', 'Locked', 'Parked', 'Pending',
     'Reserved', 'Reverted', 'Suspended', 'Transferred', 'Unknown', 'Unlocked',
     'Unparked', 'Updated', 'JsonConverterFailed'
    :vartype registration_status: str or ~azure.mgmt.web.models.DomainStatus
    :ivar provisioning_state: Domain provisioning state. Possible values
     include: 'Succeeded', 'Failed', 'Canceled', 'InProgress', 'Deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.web.models.ProvisioningState
    :ivar name_servers: Name servers.
    :vartype name_servers: list[str]
    :param privacy: <code>true</code> if domain privacy is enabled for this
     domain; otherwise, <code>false</code>.
    :type privacy: bool
    :ivar created_time: Domain creation timestamp.
    :vartype created_time: datetime
    :ivar expiration_time: Domain expiration timestamp.
    :vartype expiration_time: datetime
    :ivar last_renewed_time: Timestamp when the domain was renewed last time.
    :vartype last_renewed_time: datetime
    :param auto_renew: <code>true</code> if the domain should be automatically
     renewed; otherwise, <code>false</code>. Default value: True .
    :type auto_renew: bool
    :ivar ready_for_dns_record_management: <code>true</code> if Azure can
     assign this domain to App Service apps; otherwise, <code>false</code>.
     This value will be <code>true</code> if domain registration status is
     active and
     it is hosted on name servers Azure has programmatic access to.
    :vartype ready_for_dns_record_management: bool
    :ivar managed_host_names: All hostnames derived from the domain and
     assigned to Azure resources.
    :vartype managed_host_names: list[~azure.mgmt.web.models.HostName]
    :param consent: Legal agreement consent.
    :type consent: ~azure.mgmt.web.models.DomainPurchaseConsent
    :ivar domain_not_renewable_reasons: Reasons why domain is not renewable.
    :vartype domain_not_renewable_reasons: list[str]
    :param dns_type: Current DNS type. Possible values include: 'AzureDns',
     'DefaultDomainRegistrarDns'
    :type dns_type: str or ~azure.mgmt.web.models.DnsType
    :param dns_zone_id: Azure DNS Zone to use
    :type dns_zone_id: str
    :param target_dns_type: Target DNS type (would be used for migration).
     Possible values include: 'AzureDns', 'DefaultDomainRegistrarDns'
    :type target_dns_type: str or ~azure.mgmt.web.models.DnsType
    :param auth_code:
    :type auth_code: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'contact_admin': {'required': True},
        'contact_billing': {'required': True},
        'contact_registrant': {'required': True},
        'contact_tech': {'required': True},
        'registration_status': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'name_servers': {'readonly': True},
        'created_time': {'readonly': True},
        'expiration_time': {'readonly': True},
        'last_renewed_time': {'readonly': True},
        'ready_for_dns_record_management': {'readonly': True},
        'managed_host_names': {'readonly': True},
        'consent': {'required': True},
        'domain_not_renewable_reasons': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'contact_admin': {'key': 'properties.contactAdmin', 'type': 'Contact'},
        'contact_billing': {'key': 'properties.contactBilling', 'type': 'Contact'},
        'contact_registrant': {'key': 'properties.contactRegistrant', 'type': 'Contact'},
        'contact_tech': {'key': 'properties.contactTech', 'type': 'Contact'},
        'registration_status': {'key': 'properties.registrationStatus', 'type': 'DomainStatus'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'name_servers': {'key': 'properties.nameServers', 'type': '[str]'},
        'privacy': {'key': 'properties.privacy', 'type': 'bool'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'properties.expirationTime', 'type': 'iso-8601'},
        'last_renewed_time': {'key': 'properties.lastRenewedTime', 'type': 'iso-8601'},
        'auto_renew': {'key': 'properties.autoRenew', 'type': 'bool'},
        'ready_for_dns_record_management': {'key': 'properties.readyForDnsRecordManagement', 'type': 'bool'},
        'managed_host_names': {'key': 'properties.managedHostNames', 'type': '[HostName]'},
        'consent': {'key': 'properties.consent', 'type': 'DomainPurchaseConsent'},
        'domain_not_renewable_reasons': {'key': 'properties.domainNotRenewableReasons', 'type': '[str]'},
        'dns_type': {'key': 'properties.dnsType', 'type': 'DnsType'},
        'dns_zone_id': {'key': 'properties.dnsZoneId', 'type': 'str'},
        'target_dns_type': {'key': 'properties.targetDnsType', 'type': 'DnsType'},
        'auth_code': {'key': 'properties.authCode', 'type': 'str'},
    }

    def __init__(self, contact_admin, contact_billing, contact_registrant, contact_tech, consent, kind=None, privacy=None, auto_renew=True, dns_type=None, dns_zone_id=None, target_dns_type=None, auth_code=None):
        super(DomainPatchResource, self).__init__(kind=kind)
        self.contact_admin = contact_admin
        self.contact_billing = contact_billing
        self.contact_registrant = contact_registrant
        self.contact_tech = contact_tech
        self.registration_status = None
        self.provisioning_state = None
        self.name_servers = None
        self.privacy = privacy
        self.created_time = None
        self.expiration_time = None
        self.last_renewed_time = None
        self.auto_renew = auto_renew
        self.ready_for_dns_record_management = None
        self.managed_host_names = None
        self.consent = consent
        self.domain_not_renewable_reasons = None
        self.dns_type = dns_type
        self.dns_zone_id = dns_zone_id
        self.target_dns_type = target_dns_type
        self.auth_code = auth_code