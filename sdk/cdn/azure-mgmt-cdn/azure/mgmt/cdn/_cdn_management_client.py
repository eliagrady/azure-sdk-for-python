# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import CdnManagementClientConfiguration
from .operations import ProfilesOperations
from .operations import EndpointsOperations
from .operations import OriginsOperations
from .operations import OriginGroupsOperations
from .operations import CustomDomainsOperations
from .operations import CdnManagementClientOperationsMixin
from .operations import ResourceUsageOperations
from .operations import Operations
from .operations import EdgeNodesOperations
from .operations import PoliciesOperations
from .operations import ManagedRuleSetsOperations
from . import models


class CdnManagementClient(CdnManagementClientOperationsMixin):
    """Cdn Management Client.

    :ivar profiles: ProfilesOperations operations
    :vartype profiles: azure.mgmt.cdn.operations.ProfilesOperations
    :ivar endpoints: EndpointsOperations operations
    :vartype endpoints: azure.mgmt.cdn.operations.EndpointsOperations
    :ivar origins: OriginsOperations operations
    :vartype origins: azure.mgmt.cdn.operations.OriginsOperations
    :ivar origin_groups: OriginGroupsOperations operations
    :vartype origin_groups: azure.mgmt.cdn.operations.OriginGroupsOperations
    :ivar custom_domains: CustomDomainsOperations operations
    :vartype custom_domains: azure.mgmt.cdn.operations.CustomDomainsOperations
    :ivar resource_usage: ResourceUsageOperations operations
    :vartype resource_usage: azure.mgmt.cdn.operations.ResourceUsageOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cdn.operations.Operations
    :ivar edge_nodes: EdgeNodesOperations operations
    :vartype edge_nodes: azure.mgmt.cdn.operations.EdgeNodesOperations
    :ivar policies: PoliciesOperations operations
    :vartype policies: azure.mgmt.cdn.operations.PoliciesOperations
    :ivar managed_rule_sets: ManagedRuleSetsOperations operations
    :vartype managed_rule_sets: azure.mgmt.cdn.operations.ManagedRuleSetsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = CdnManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.profiles = ProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.origins = OriginsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.origin_groups = OriginGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_usage = ResourceUsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.edge_nodes = EdgeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.managed_rule_sets = ManagedRuleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> CdnManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
