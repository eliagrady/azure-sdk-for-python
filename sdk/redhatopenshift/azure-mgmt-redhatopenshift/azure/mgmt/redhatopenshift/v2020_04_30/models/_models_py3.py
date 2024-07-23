# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class APIServerProfile(_serialization.Model):
    """APIServerProfile represents an API server profile.

    :ivar visibility: API server visibility (immutable). Known values are: "Private" and "Public".
    :vartype visibility: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.Visibility
    :ivar url: The URL to access the cluster API server (immutable).
    :vartype url: str
    :ivar ip: The IP of the cluster API server (immutable).
    :vartype ip: str
    """

    _attribute_map = {
        "visibility": {"key": "visibility", "type": "str"},
        "url": {"key": "url", "type": "str"},
        "ip": {"key": "ip", "type": "str"},
    }

    def __init__(
        self,
        *,
        visibility: Optional[Union[str, "_models.Visibility"]] = None,
        url: Optional[str] = None,
        ip: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword visibility: API server visibility (immutable). Known values are: "Private" and
         "Public".
        :paramtype visibility: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.Visibility
        :keyword url: The URL to access the cluster API server (immutable).
        :paramtype url: str
        :keyword ip: The IP of the cluster API server (immutable).
        :paramtype ip: str
        """
        super().__init__(**kwargs)
        self.visibility = visibility
        self.url = url
        self.ip = ip


class CloudErrorBody(_serialization.Model):
    """CloudErrorBody represents the body of a cloud error.

    :ivar code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :vartype code: str
    :ivar message: A message describing the error, intended to be suitable for display in a user
     interface.
    :vartype message: str
    :ivar target: The target of the particular error. For example, the name of the property in
     error.
    :vartype target: str
    :ivar details: A list of additional details about the error.
    :vartype details: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.CloudErrorBody]
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["_models.CloudErrorBody"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword code: An identifier for the error. Codes are invariant and are intended to be consumed
         programmatically.
        :paramtype code: str
        :keyword message: A message describing the error, intended to be suitable for display in a user
         interface.
        :paramtype message: str
        :keyword target: The target of the particular error. For example, the name of the property in
         error.
        :paramtype target: str
        :keyword details: A list of additional details about the error.
        :paramtype details: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.CloudErrorBody]
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class ClusterProfile(_serialization.Model):
    """ClusterProfile represents a cluster profile.

    :ivar pull_secret: The pull secret for the cluster (immutable).
    :vartype pull_secret: str
    :ivar domain: The domain for the cluster (immutable).
    :vartype domain: str
    :ivar version: The version of the cluster (immutable).
    :vartype version: str
    :ivar resource_group_id: The ID of the cluster resource group (immutable).
    :vartype resource_group_id: str
    """

    _attribute_map = {
        "pull_secret": {"key": "pullSecret", "type": "str"},
        "domain": {"key": "domain", "type": "str"},
        "version": {"key": "version", "type": "str"},
        "resource_group_id": {"key": "resourceGroupId", "type": "str"},
    }

    def __init__(
        self,
        *,
        pull_secret: Optional[str] = None,
        domain: Optional[str] = None,
        version: Optional[str] = None,
        resource_group_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword pull_secret: The pull secret for the cluster (immutable).
        :paramtype pull_secret: str
        :keyword domain: The domain for the cluster (immutable).
        :paramtype domain: str
        :keyword version: The version of the cluster (immutable).
        :paramtype version: str
        :keyword resource_group_id: The ID of the cluster resource group (immutable).
        :paramtype resource_group_id: str
        """
        super().__init__(**kwargs)
        self.pull_secret = pull_secret
        self.domain = domain
        self.version = version
        self.resource_group_id = resource_group_id


class ConsoleProfile(_serialization.Model):
    """ConsoleProfile represents a console profile.

    :ivar url: The URL to access the cluster console (immutable).
    :vartype url: str
    """

    _attribute_map = {
        "url": {"key": "url", "type": "str"},
    }

    def __init__(self, *, url: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword url: The URL to access the cluster console (immutable).
        :paramtype url: str
        """
        super().__init__(**kwargs)
        self.url = url


class Display(_serialization.Model):
    """Display represents the display details of an operation.

    :ivar provider: Friendly name of the resource provider.
    :vartype provider: str
    :ivar resource: Resource type on which the operation is performed.
    :vartype resource: str
    :ivar operation: Operation type: read, write, delete, listKeys/action, etc.
    :vartype operation: str
    :ivar description: Friendly name of the operation.
    :vartype description: str
    """

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword provider: Friendly name of the resource provider.
        :paramtype provider: str
        :keyword resource: Resource type on which the operation is performed.
        :paramtype resource: str
        :keyword operation: Operation type: read, write, delete, listKeys/action, etc.
        :paramtype operation: str
        :keyword description: Friendly name of the operation.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class IngressProfile(_serialization.Model):
    """IngressProfile represents an ingress profile.

    :ivar name: The ingress profile name.  Must be "default" (immutable).
    :vartype name: str
    :ivar visibility: Ingress visibility (immutable). Known values are: "Private" and "Public".
    :vartype visibility: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.Visibility
    :ivar ip: The IP of the ingress (immutable).
    :vartype ip: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "visibility": {"key": "visibility", "type": "str"},
        "ip": {"key": "ip", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        visibility: Optional[Union[str, "_models.Visibility"]] = None,
        ip: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: The ingress profile name.  Must be "default" (immutable).
        :paramtype name: str
        :keyword visibility: Ingress visibility (immutable). Known values are: "Private" and "Public".
        :paramtype visibility: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.Visibility
        :keyword ip: The IP of the ingress (immutable).
        :paramtype ip: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.visibility = visibility
        self.ip = ip


class MasterProfile(_serialization.Model):
    """MasterProfile represents a master profile.

    :ivar vm_size: The size of the master VMs (immutable). Known values are: "Standard_D2s_v3",
     "Standard_D4s_v3", and "Standard_D8s_v3".
    :vartype vm_size: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.VMSize
    :ivar subnet_id: The Azure resource ID of the master subnet (immutable).
    :vartype subnet_id: str
    """

    _attribute_map = {
        "vm_size": {"key": "vmSize", "type": "str"},
        "subnet_id": {"key": "subnetId", "type": "str"},
    }

    def __init__(
        self, *, vm_size: Optional[Union[str, "_models.VMSize"]] = None, subnet_id: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword vm_size: The size of the master VMs (immutable). Known values are: "Standard_D2s_v3",
         "Standard_D4s_v3", and "Standard_D8s_v3".
        :paramtype vm_size: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.VMSize
        :keyword subnet_id: The Azure resource ID of the master subnet (immutable).
        :paramtype subnet_id: str
        """
        super().__init__(**kwargs)
        self.vm_size = vm_size
        self.subnet_id = subnet_id


class NetworkProfile(_serialization.Model):
    """NetworkProfile represents a network profile.

    :ivar pod_cidr: The CIDR used for OpenShift/Kubernetes Pods (immutable).
    :vartype pod_cidr: str
    :ivar service_cidr: The CIDR used for OpenShift/Kubernetes Services (immutable).
    :vartype service_cidr: str
    """

    _attribute_map = {
        "pod_cidr": {"key": "podCidr", "type": "str"},
        "service_cidr": {"key": "serviceCidr", "type": "str"},
    }

    def __init__(self, *, pod_cidr: Optional[str] = None, service_cidr: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword pod_cidr: The CIDR used for OpenShift/Kubernetes Pods (immutable).
        :paramtype pod_cidr: str
        :keyword service_cidr: The CIDR used for OpenShift/Kubernetes Services (immutable).
        :paramtype service_cidr: str
        """
        super().__init__(**kwargs)
        self.pod_cidr = pod_cidr
        self.service_cidr = service_cidr


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class OpenShiftCluster(TrackedResource):  # pylint: disable=too-many-instance-attributes
    """OpenShiftCluster represents an Azure Red Hat OpenShift cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar provisioning_state: The cluster provisioning state (immutable). Known values are:
     "AdminUpdating", "Creating", "Deleting", "Failed", "Succeeded", and "Updating".
    :vartype provisioning_state: str or
     ~azure.mgmt.redhatopenshift.v2020_04_30.models.ProvisioningState
    :ivar cluster_profile: The cluster profile.
    :vartype cluster_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ClusterProfile
    :ivar console_profile: The console profile.
    :vartype console_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ConsoleProfile
    :ivar service_principal_profile: The cluster service principal profile.
    :vartype service_principal_profile:
     ~azure.mgmt.redhatopenshift.v2020_04_30.models.ServicePrincipalProfile
    :ivar network_profile: The cluster network profile.
    :vartype network_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.NetworkProfile
    :ivar master_profile: The cluster master profile.
    :vartype master_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.MasterProfile
    :ivar worker_profiles: The cluster worker profiles.
    :vartype worker_profiles: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.WorkerProfile]
    :ivar apiserver_profile: The cluster API server profile.
    :vartype apiserver_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.APIServerProfile
    :ivar ingress_profiles: The cluster ingress profiles.
    :vartype ingress_profiles: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.IngressProfile]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "cluster_profile": {"key": "properties.clusterProfile", "type": "ClusterProfile"},
        "console_profile": {"key": "properties.consoleProfile", "type": "ConsoleProfile"},
        "service_principal_profile": {"key": "properties.servicePrincipalProfile", "type": "ServicePrincipalProfile"},
        "network_profile": {"key": "properties.networkProfile", "type": "NetworkProfile"},
        "master_profile": {"key": "properties.masterProfile", "type": "MasterProfile"},
        "worker_profiles": {"key": "properties.workerProfiles", "type": "[WorkerProfile]"},
        "apiserver_profile": {"key": "properties.apiserverProfile", "type": "APIServerProfile"},
        "ingress_profiles": {"key": "properties.ingressProfiles", "type": "[IngressProfile]"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = None,
        cluster_profile: Optional["_models.ClusterProfile"] = None,
        console_profile: Optional["_models.ConsoleProfile"] = None,
        service_principal_profile: Optional["_models.ServicePrincipalProfile"] = None,
        network_profile: Optional["_models.NetworkProfile"] = None,
        master_profile: Optional["_models.MasterProfile"] = None,
        worker_profiles: Optional[List["_models.WorkerProfile"]] = None,
        apiserver_profile: Optional["_models.APIServerProfile"] = None,
        ingress_profiles: Optional[List["_models.IngressProfile"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword provisioning_state: The cluster provisioning state (immutable). Known values are:
         "AdminUpdating", "Creating", "Deleting", "Failed", "Succeeded", and "Updating".
        :paramtype provisioning_state: str or
         ~azure.mgmt.redhatopenshift.v2020_04_30.models.ProvisioningState
        :keyword cluster_profile: The cluster profile.
        :paramtype cluster_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ClusterProfile
        :keyword console_profile: The console profile.
        :paramtype console_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ConsoleProfile
        :keyword service_principal_profile: The cluster service principal profile.
        :paramtype service_principal_profile:
         ~azure.mgmt.redhatopenshift.v2020_04_30.models.ServicePrincipalProfile
        :keyword network_profile: The cluster network profile.
        :paramtype network_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.NetworkProfile
        :keyword master_profile: The cluster master profile.
        :paramtype master_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.MasterProfile
        :keyword worker_profiles: The cluster worker profiles.
        :paramtype worker_profiles: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.WorkerProfile]
        :keyword apiserver_profile: The cluster API server profile.
        :paramtype apiserver_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.APIServerProfile
        :keyword ingress_profiles: The cluster ingress profiles.
        :paramtype ingress_profiles:
         list[~azure.mgmt.redhatopenshift.v2020_04_30.models.IngressProfile]
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.provisioning_state = provisioning_state
        self.cluster_profile = cluster_profile
        self.console_profile = console_profile
        self.service_principal_profile = service_principal_profile
        self.network_profile = network_profile
        self.master_profile = master_profile
        self.worker_profiles = worker_profiles
        self.apiserver_profile = apiserver_profile
        self.ingress_profiles = ingress_profiles


class OpenShiftClusterCredentials(_serialization.Model):
    """OpenShiftClusterCredentials represents an OpenShift cluster's credentials.

    :ivar kubeadmin_username: The username for the kubeadmin user.
    :vartype kubeadmin_username: str
    :ivar kubeadmin_password: The password for the kubeadmin user.
    :vartype kubeadmin_password: str
    """

    _attribute_map = {
        "kubeadmin_username": {"key": "kubeadminUsername", "type": "str"},
        "kubeadmin_password": {"key": "kubeadminPassword", "type": "str"},
    }

    def __init__(
        self, *, kubeadmin_username: Optional[str] = None, kubeadmin_password: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword kubeadmin_username: The username for the kubeadmin user.
        :paramtype kubeadmin_username: str
        :keyword kubeadmin_password: The password for the kubeadmin user.
        :paramtype kubeadmin_password: str
        """
        super().__init__(**kwargs)
        self.kubeadmin_username = kubeadmin_username
        self.kubeadmin_password = kubeadmin_password


class OpenShiftClusterList(_serialization.Model):
    """OpenShiftClusterList represents a list of OpenShift clusters.

    :ivar value: The list of OpenShift clusters.
    :vartype value: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.OpenShiftCluster]
    :ivar next_link: The link used to get the next page of operations.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[OpenShiftCluster]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.OpenShiftCluster"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword value: The list of OpenShift clusters.
        :paramtype value: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.OpenShiftCluster]
        :keyword next_link: The link used to get the next page of operations.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class OpenShiftClusterUpdate(_serialization.Model):
    """OpenShiftCluster represents an Azure Red Hat OpenShift cluster.

    :ivar tags: The resource tags.
    :vartype tags: dict[str, str]
    :ivar provisioning_state: The cluster provisioning state (immutable). Known values are:
     "AdminUpdating", "Creating", "Deleting", "Failed", "Succeeded", and "Updating".
    :vartype provisioning_state: str or
     ~azure.mgmt.redhatopenshift.v2020_04_30.models.ProvisioningState
    :ivar cluster_profile: The cluster profile.
    :vartype cluster_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ClusterProfile
    :ivar console_profile: The console profile.
    :vartype console_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ConsoleProfile
    :ivar service_principal_profile: The cluster service principal profile.
    :vartype service_principal_profile:
     ~azure.mgmt.redhatopenshift.v2020_04_30.models.ServicePrincipalProfile
    :ivar network_profile: The cluster network profile.
    :vartype network_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.NetworkProfile
    :ivar master_profile: The cluster master profile.
    :vartype master_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.MasterProfile
    :ivar worker_profiles: The cluster worker profiles.
    :vartype worker_profiles: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.WorkerProfile]
    :ivar apiserver_profile: The cluster API server profile.
    :vartype apiserver_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.APIServerProfile
    :ivar ingress_profiles: The cluster ingress profiles.
    :vartype ingress_profiles: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.IngressProfile]
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "cluster_profile": {"key": "properties.clusterProfile", "type": "ClusterProfile"},
        "console_profile": {"key": "properties.consoleProfile", "type": "ConsoleProfile"},
        "service_principal_profile": {"key": "properties.servicePrincipalProfile", "type": "ServicePrincipalProfile"},
        "network_profile": {"key": "properties.networkProfile", "type": "NetworkProfile"},
        "master_profile": {"key": "properties.masterProfile", "type": "MasterProfile"},
        "worker_profiles": {"key": "properties.workerProfiles", "type": "[WorkerProfile]"},
        "apiserver_profile": {"key": "properties.apiserverProfile", "type": "APIServerProfile"},
        "ingress_profiles": {"key": "properties.ingressProfiles", "type": "[IngressProfile]"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = None,
        cluster_profile: Optional["_models.ClusterProfile"] = None,
        console_profile: Optional["_models.ConsoleProfile"] = None,
        service_principal_profile: Optional["_models.ServicePrincipalProfile"] = None,
        network_profile: Optional["_models.NetworkProfile"] = None,
        master_profile: Optional["_models.MasterProfile"] = None,
        worker_profiles: Optional[List["_models.WorkerProfile"]] = None,
        apiserver_profile: Optional["_models.APIServerProfile"] = None,
        ingress_profiles: Optional[List["_models.IngressProfile"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: The resource tags.
        :paramtype tags: dict[str, str]
        :keyword provisioning_state: The cluster provisioning state (immutable). Known values are:
         "AdminUpdating", "Creating", "Deleting", "Failed", "Succeeded", and "Updating".
        :paramtype provisioning_state: str or
         ~azure.mgmt.redhatopenshift.v2020_04_30.models.ProvisioningState
        :keyword cluster_profile: The cluster profile.
        :paramtype cluster_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ClusterProfile
        :keyword console_profile: The console profile.
        :paramtype console_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.ConsoleProfile
        :keyword service_principal_profile: The cluster service principal profile.
        :paramtype service_principal_profile:
         ~azure.mgmt.redhatopenshift.v2020_04_30.models.ServicePrincipalProfile
        :keyword network_profile: The cluster network profile.
        :paramtype network_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.NetworkProfile
        :keyword master_profile: The cluster master profile.
        :paramtype master_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.MasterProfile
        :keyword worker_profiles: The cluster worker profiles.
        :paramtype worker_profiles: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.WorkerProfile]
        :keyword apiserver_profile: The cluster API server profile.
        :paramtype apiserver_profile: ~azure.mgmt.redhatopenshift.v2020_04_30.models.APIServerProfile
        :keyword ingress_profiles: The cluster ingress profiles.
        :paramtype ingress_profiles:
         list[~azure.mgmt.redhatopenshift.v2020_04_30.models.IngressProfile]
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.provisioning_state = provisioning_state
        self.cluster_profile = cluster_profile
        self.console_profile = console_profile
        self.service_principal_profile = service_principal_profile
        self.network_profile = network_profile
        self.master_profile = master_profile
        self.worker_profiles = worker_profiles
        self.apiserver_profile = apiserver_profile
        self.ingress_profiles = ingress_profiles


class Operation(_serialization.Model):
    """Operation represents an RP operation.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :ivar display: The object that describes the operation.
    :vartype display: ~azure.mgmt.redhatopenshift.v2020_04_30.models.Display
    :ivar origin: Sources of requests to this operation.  Comma separated list with valid values
     user or system, e.g. "user,system".
    :vartype origin: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display": {"key": "display", "type": "Display"},
        "origin": {"key": "origin", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["_models.Display"] = None,
        origin: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: Operation name: {provider}/{resource}/{operation}.
        :paramtype name: str
        :keyword display: The object that describes the operation.
        :paramtype display: ~azure.mgmt.redhatopenshift.v2020_04_30.models.Display
        :keyword origin: Sources of requests to this operation.  Comma separated list with valid values
         user or system, e.g. "user,system".
        :paramtype origin: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin


class OperationList(_serialization.Model):
    """OperationList represents an RP operation list.

    :ivar value: List of operations supported by the resource provider.
    :vartype value: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.Operation]
    :ivar next_link: The link used to get the next page of operations.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.Operation"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: List of operations supported by the resource provider.
        :paramtype value: list[~azure.mgmt.redhatopenshift.v2020_04_30.models.Operation]
        :keyword next_link: The link used to get the next page of operations.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ServicePrincipalProfile(_serialization.Model):
    """ServicePrincipalProfile represents a service principal profile.

    :ivar client_id: The client ID used for the cluster (immutable).
    :vartype client_id: str
    :ivar client_secret: The client secret used for the cluster (immutable).
    :vartype client_secret: str
    """

    _attribute_map = {
        "client_id": {"key": "clientId", "type": "str"},
        "client_secret": {"key": "clientSecret", "type": "str"},
    }

    def __init__(self, *, client_id: Optional[str] = None, client_secret: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword client_id: The client ID used for the cluster (immutable).
        :paramtype client_id: str
        :keyword client_secret: The client secret used for the cluster (immutable).
        :paramtype client_secret: str
        """
        super().__init__(**kwargs)
        self.client_id = client_id
        self.client_secret = client_secret


class WorkerProfile(_serialization.Model):
    """WorkerProfile represents a worker profile.

    :ivar name: The worker profile name.  Must be "worker" (immutable).
    :vartype name: str
    :ivar vm_size: The size of the worker VMs (immutable). Known values are: "Standard_D2s_v3",
     "Standard_D4s_v3", and "Standard_D8s_v3".
    :vartype vm_size: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.VMSize
    :ivar disk_size_gb: The disk size of the worker VMs.  Must be 128 or greater (immutable).
    :vartype disk_size_gb: int
    :ivar subnet_id: The Azure resource ID of the worker subnet (immutable).
    :vartype subnet_id: str
    :ivar count: The number of worker VMs.  Must be between 3 and 20 (immutable).
    :vartype count: int
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "vm_size": {"key": "vmSize", "type": "str"},
        "disk_size_gb": {"key": "diskSizeGB", "type": "int"},
        "subnet_id": {"key": "subnetId", "type": "str"},
        "count": {"key": "count", "type": "int"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        vm_size: Optional[Union[str, "_models.VMSize"]] = None,
        disk_size_gb: Optional[int] = None,
        subnet_id: Optional[str] = None,
        count: Optional[int] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: The worker profile name.  Must be "worker" (immutable).
        :paramtype name: str
        :keyword vm_size: The size of the worker VMs (immutable). Known values are: "Standard_D2s_v3",
         "Standard_D4s_v3", and "Standard_D8s_v3".
        :paramtype vm_size: str or ~azure.mgmt.redhatopenshift.v2020_04_30.models.VMSize
        :keyword disk_size_gb: The disk size of the worker VMs.  Must be 128 or greater (immutable).
        :paramtype disk_size_gb: int
        :keyword subnet_id: The Azure resource ID of the worker subnet (immutable).
        :paramtype subnet_id: str
        :keyword count: The number of worker VMs.  Must be between 3 and 20 (immutable).
        :paramtype count: int
        """
        super().__init__(**kwargs)
        self.name = name
        self.vm_size = vm_size
        self.disk_size_gb = disk_size_gb
        self.subnet_id = subnet_id
        self.count = count
