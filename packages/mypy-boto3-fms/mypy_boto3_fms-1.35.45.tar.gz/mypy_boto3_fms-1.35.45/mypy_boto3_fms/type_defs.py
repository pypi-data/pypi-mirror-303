"""
Type annotations for fms service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/type_defs/)

Usage::

    ```python
    from mypy_boto3_fms.type_defs import AccountScopeOutputTypeDef

    data: AccountScopeOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccountRoleStatusType,
    CustomerPolicyScopeIdTypeType,
    CustomerPolicyStatusType,
    DependentServiceNameType,
    DestinationTypeType,
    EntryTypeType,
    EntryViolationReasonType,
    FailedItemReasonType,
    FirewallDeploymentModelType,
    MarketplaceSubscriptionOnboardingStatusType,
    NetworkAclRuleActionType,
    OrganizationStatusType,
    PolicyComplianceStatusTypeType,
    RemediationActionTypeType,
    ResourceSetStatusType,
    RuleOrderType,
    SecurityServiceTypeType,
    StreamExceptionPolicyType,
    TargetTypeType,
    ThirdPartyFirewallAssociationStatusType,
    ThirdPartyFirewallType,
    ViolationReasonType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccountScopeOutputTypeDef",
    "AccountScopeTypeDef",
    "ActionTargetTypeDef",
    "AdminAccountSummaryTypeDef",
    "OrganizationalUnitScopeOutputTypeDef",
    "PolicyTypeScopeOutputTypeDef",
    "RegionScopeOutputTypeDef",
    "AppTypeDef",
    "TimestampTypeDef",
    "AssociateAdminAccountRequestRequestTypeDef",
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "PartialMatchTypeDef",
    "BatchAssociateResourceRequestRequestTypeDef",
    "FailedItemTypeDef",
    "BatchDisassociateResourceRequestRequestTypeDef",
    "ComplianceViolatorTypeDef",
    "DeleteAppsListRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeleteProtocolsListRequestRequestTypeDef",
    "DeleteResourceSetRequestRequestTypeDef",
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    "DiscoveredResourceTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EvaluationResultTypeDef",
    "ExpectedRouteTypeDef",
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    "GetAdminScopeRequestRequestTypeDef",
    "GetAppsListRequestRequestTypeDef",
    "GetComplianceDetailRequestRequestTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetProtocolsListRequestRequestTypeDef",
    "ProtocolsListDataOutputTypeDef",
    "GetResourceSetRequestRequestTypeDef",
    "ResourceSetOutputTypeDef",
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    "GetViolationDetailsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    "ListAdminsManagingAccountRequestRequestTypeDef",
    "ListAppsListsRequestRequestTypeDef",
    "ListComplianceStatusRequestRequestTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "PolicySummaryTypeDef",
    "ListProtocolsListsRequestRequestTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ListResourceSetResourcesRequestRequestTypeDef",
    "ResourceTypeDef",
    "ListResourceSetsRequestRequestTypeDef",
    "ResourceSetSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    "NetworkAclIcmpTypeCodeTypeDef",
    "NetworkAclPortRangeTypeDef",
    "RouteTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "StatefulEngineOptionsTypeDef",
    "StatelessRuleGroupTypeDef",
    "NetworkFirewallPolicyTypeDef",
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    "OrganizationalUnitScopeTypeDef",
    "ThirdPartyFirewallPolicyTypeDef",
    "ResourceTagTypeDef",
    "PolicyTypeScopeTypeDef",
    "PutNotificationChannelRequestRequestTypeDef",
    "RegionScopeTypeDef",
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    "WebACLHasIncompatibleConfigurationViolationTypeDef",
    "WebACLHasOutOfScopeResourcesViolationTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AccountScopeUnionTypeDef",
    "CreateNetworkAclActionTypeDef",
    "EC2AssociateRouteTableActionTypeDef",
    "EC2CopyRouteTableActionTypeDef",
    "EC2CreateRouteActionTypeDef",
    "EC2CreateRouteTableActionTypeDef",
    "EC2DeleteRouteActionTypeDef",
    "EC2ReplaceRouteActionTypeDef",
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    "ReplaceNetworkAclAssociationActionTypeDef",
    "AdminScopeOutputTypeDef",
    "AppsListDataOutputTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "GetProtectionStatusRequestRequestTypeDef",
    "ProtocolsListDataTypeDef",
    "ResourceSetTypeDef",
    "AssociateThirdPartyFirewallResponseTypeDef",
    "DisassociateThirdPartyFirewallResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    "ListAdminAccountsForOrganizationResponseTypeDef",
    "ListAdminsManagingAccountResponseTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "BatchAssociateResourceResponseTypeDef",
    "BatchDisassociateResourceResponseTypeDef",
    "PolicyComplianceDetailTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "PolicyComplianceStatusTypeDef",
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    "GetProtocolsListResponseTypeDef",
    "PutProtocolsListResponseTypeDef",
    "GetResourceSetResponseTypeDef",
    "PutResourceSetResponseTypeDef",
    "ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef",
    "ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef",
    "ListAppsListsRequestListAppsListsPaginateTypeDef",
    "ListComplianceStatusRequestListComplianceStatusPaginateTypeDef",
    "ListMemberAccountsRequestListMemberAccountsPaginateTypeDef",
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    "ListProtocolsListsRequestListProtocolsListsPaginateTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListResourceSetResourcesResponseTypeDef",
    "ListResourceSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    "NetworkAclEntryTypeDef",
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    "StatefulRuleGroupTypeDef",
    "OrganizationalUnitScopeUnionTypeDef",
    "PolicyTypeScopeUnionTypeDef",
    "RegionScopeUnionTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "GetAdminScopeResponseTypeDef",
    "GetAppsListResponseTypeDef",
    "PutAppsListResponseTypeDef",
    "ListAppsListsResponseTypeDef",
    "PutAppsListRequestRequestTypeDef",
    "PutProtocolsListRequestRequestTypeDef",
    "PutResourceSetRequestRequestTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "EntryDescriptionTypeDef",
    "NetworkAclEntrySetOutputTypeDef",
    "NetworkAclEntrySetTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "AdminScopeTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "CreateNetworkAclEntriesActionTypeDef",
    "DeleteNetworkAclEntriesActionTypeDef",
    "EntryViolationTypeDef",
    "NetworkAclCommonPolicyOutputTypeDef",
    "NetworkAclEntrySetUnionTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "PutAdminAccountRequestRequestTypeDef",
    "RemediationActionTypeDef",
    "InvalidNetworkAclEntriesViolationTypeDef",
    "PolicyOptionOutputTypeDef",
    "NetworkAclCommonPolicyTypeDef",
    "RemediationActionWithOrderTypeDef",
    "SecurityServicePolicyDataOutputTypeDef",
    "NetworkAclCommonPolicyUnionTypeDef",
    "PossibleRemediationActionTypeDef",
    "PolicyOutputTypeDef",
    "PolicyOptionTypeDef",
    "PossibleRemediationActionsTypeDef",
    "GetPolicyResponseTypeDef",
    "PutPolicyResponseTypeDef",
    "PolicyOptionUnionTypeDef",
    "ResourceViolationTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "ViolationDetailTypeDef",
    "SecurityServicePolicyDataUnionTypeDef",
    "GetViolationDetailsResponseTypeDef",
    "PolicyTypeDef",
    "PutPolicyRequestRequestTypeDef",
)

AccountScopeOutputTypeDef = TypedDict(
    "AccountScopeOutputTypeDef",
    {
        "Accounts": NotRequired[List[str]],
        "AllAccountsEnabled": NotRequired[bool],
        "ExcludeSpecifiedAccounts": NotRequired[bool],
    },
)
AccountScopeTypeDef = TypedDict(
    "AccountScopeTypeDef",
    {
        "Accounts": NotRequired[Sequence[str]],
        "AllAccountsEnabled": NotRequired[bool],
        "ExcludeSpecifiedAccounts": NotRequired[bool],
    },
)
ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ResourceId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
AdminAccountSummaryTypeDef = TypedDict(
    "AdminAccountSummaryTypeDef",
    {
        "AdminAccount": NotRequired[str],
        "DefaultAdmin": NotRequired[bool],
        "Status": NotRequired[OrganizationStatusType],
    },
)
OrganizationalUnitScopeOutputTypeDef = TypedDict(
    "OrganizationalUnitScopeOutputTypeDef",
    {
        "OrganizationalUnits": NotRequired[List[str]],
        "AllOrganizationalUnitsEnabled": NotRequired[bool],
        "ExcludeSpecifiedOrganizationalUnits": NotRequired[bool],
    },
)
PolicyTypeScopeOutputTypeDef = TypedDict(
    "PolicyTypeScopeOutputTypeDef",
    {
        "PolicyTypes": NotRequired[List[SecurityServiceTypeType]],
        "AllPolicyTypesEnabled": NotRequired[bool],
    },
)
RegionScopeOutputTypeDef = TypedDict(
    "RegionScopeOutputTypeDef",
    {
        "Regions": NotRequired[List[str]],
        "AllRegionsEnabled": NotRequired[bool],
    },
)
AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppName": str,
        "Protocol": str,
        "Port": int,
    },
)
TimestampTypeDef = Union[datetime, str]
AssociateAdminAccountRequestRequestTypeDef = TypedDict(
    "AssociateAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)
AssociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
        "HostId": NotRequired[str],
    },
)
AwsEc2NetworkInterfaceViolationTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolatingSecurityGroups": NotRequired[List[str]],
    },
)
PartialMatchTypeDef = TypedDict(
    "PartialMatchTypeDef",
    {
        "Reference": NotRequired[str],
        "TargetViolationReasons": NotRequired[List[str]],
    },
)
BatchAssociateResourceRequestRequestTypeDef = TypedDict(
    "BatchAssociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": Sequence[str],
    },
)
FailedItemTypeDef = TypedDict(
    "FailedItemTypeDef",
    {
        "URI": NotRequired[str],
        "Reason": NotRequired[FailedItemReasonType],
    },
)
BatchDisassociateResourceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": Sequence[str],
    },
)
ComplianceViolatorTypeDef = TypedDict(
    "ComplianceViolatorTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ViolationReason": NotRequired[ViolationReasonType],
        "ResourceType": NotRequired[str],
        "Metadata": NotRequired[Dict[str, str]],
    },
)
DeleteAppsListRequestRequestTypeDef = TypedDict(
    "DeleteAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "DeleteAllPolicyResources": NotRequired[bool],
    },
)
DeleteProtocolsListRequestRequestTypeDef = TypedDict(
    "DeleteProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
DeleteResourceSetRequestRequestTypeDef = TypedDict(
    "DeleteResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
DisassociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)
DiscoveredResourceTypeDef = TypedDict(
    "DiscoveredResourceTypeDef",
    {
        "URI": NotRequired[str],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DnsDuplicateRuleGroupViolationTypeDef = TypedDict(
    "DnsDuplicateRuleGroupViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
    },
)
DnsRuleGroupLimitExceededViolationTypeDef = TypedDict(
    "DnsRuleGroupLimitExceededViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "NumberOfRuleGroupsAlreadyAssociated": NotRequired[int],
    },
)
DnsRuleGroupPriorityConflictViolationTypeDef = TypedDict(
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "ConflictingPriority": NotRequired[int],
        "ConflictingPolicyId": NotRequired[str],
        "UnavailablePriorities": NotRequired[List[int]],
    },
)
EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": NotRequired[PolicyComplianceStatusTypeType],
        "ViolatorCount": NotRequired[int],
        "EvaluationLimitExceeded": NotRequired[bool],
    },
)
ExpectedRouteTypeDef = TypedDict(
    "ExpectedRouteTypeDef",
    {
        "IpV4Cidr": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "IpV6Cidr": NotRequired[str],
        "ContributingSubnets": NotRequired[List[str]],
        "AllowedTargets": NotRequired[List[str]],
        "RouteTableId": NotRequired[str],
    },
)
FMSPolicyUpdateFirewallCreationConfigActionTypeDef = TypedDict(
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    {
        "Description": NotRequired[str],
        "FirewallCreationConfig": NotRequired[str],
    },
)
FirewallSubnetIsOutOfScopeViolationTypeDef = TypedDict(
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
    },
)
FirewallSubnetMissingVPCEndpointViolationTypeDef = TypedDict(
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
    },
)
GetAdminScopeRequestRequestTypeDef = TypedDict(
    "GetAdminScopeRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)
GetAppsListRequestRequestTypeDef = TypedDict(
    "GetAppsListRequestRequestTypeDef",
    {
        "ListId": str,
        "DefaultList": NotRequired[bool],
    },
)
GetComplianceDetailRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
    },
)
GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
GetProtocolsListRequestRequestTypeDef = TypedDict(
    "GetProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
        "DefaultList": NotRequired[bool],
    },
)
ProtocolsListDataOutputTypeDef = TypedDict(
    "ProtocolsListDataOutputTypeDef",
    {
        "ListName": str,
        "ProtocolsList": List[str],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "PreviousProtocolsList": NotRequired[Dict[str, List[str]]],
    },
)
GetResourceSetRequestRequestTypeDef = TypedDict(
    "GetResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
ResourceSetOutputTypeDef = TypedDict(
    "ResourceSetOutputTypeDef",
    {
        "Name": str,
        "ResourceTypeList": List[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "UpdateToken": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
        "ResourceSetStatus": NotRequired[ResourceSetStatusType],
    },
)
GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)
GetViolationDetailsRequestRequestTypeDef = TypedDict(
    "GetViolationDetailsRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListAdminAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAdminsManagingAccountRequestRequestTypeDef = TypedDict(
    "ListAdminsManagingAccountRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAppsListsRequestRequestTypeDef = TypedDict(
    "ListAppsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DefaultLists": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
ListComplianceStatusRequestRequestTypeDef = TypedDict(
    "ListComplianceStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestRequestTypeDef",
    {
        "MemberAccountIds": Sequence[str],
        "ResourceType": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "PolicyArn": NotRequired[str],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "ResourceType": NotRequired[str],
        "SecurityServiceType": NotRequired[SecurityServiceTypeType],
        "RemediationEnabled": NotRequired[bool],
        "DeleteUnusedFMManagedResources": NotRequired[bool],
        "PolicyStatus": NotRequired[CustomerPolicyStatusType],
    },
)
ListProtocolsListsRequestRequestTypeDef = TypedDict(
    "ListProtocolsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DefaultLists": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
ProtocolsListDataSummaryTypeDef = TypedDict(
    "ProtocolsListDataSummaryTypeDef",
    {
        "ListArn": NotRequired[str],
        "ListId": NotRequired[str],
        "ListName": NotRequired[str],
        "ProtocolsList": NotRequired[List[str]],
    },
)
ListResourceSetResourcesRequestRequestTypeDef = TypedDict(
    "ListResourceSetResourcesRequestRequestTypeDef",
    {
        "Identifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "URI": str,
        "AccountId": NotRequired[str],
    },
)
ListResourceSetsRequestRequestTypeDef = TypedDict(
    "ListResourceSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ResourceSetSummaryTypeDef = TypedDict(
    "ResourceSetSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
        "ResourceSetStatus": NotRequired[ResourceSetStatusType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
        "MaxResults": int,
        "NextToken": NotRequired[str],
    },
)
ThirdPartyFirewallFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    {
        "FirewallPolicyId": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
    },
)
NetworkAclIcmpTypeCodeTypeDef = TypedDict(
    "NetworkAclIcmpTypeCodeTypeDef",
    {
        "Code": NotRequired[int],
        "Type": NotRequired[int],
    },
)
NetworkAclPortRangeTypeDef = TypedDict(
    "NetworkAclPortRangeTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
    },
)
RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationType": NotRequired[DestinationTypeType],
        "TargetType": NotRequired[TargetTypeType],
        "Destination": NotRequired[str],
        "Target": NotRequired[str],
    },
)
NetworkFirewallMissingExpectedRTViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CurrentRouteTable": NotRequired[str],
        "ExpectedRouteTable": NotRequired[str],
    },
)
NetworkFirewallMissingFirewallViolationTypeDef = TypedDict(
    "NetworkFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
NetworkFirewallMissingSubnetViolationTypeDef = TypedDict(
    "NetworkFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
StatefulEngineOptionsTypeDef = TypedDict(
    "StatefulEngineOptionsTypeDef",
    {
        "RuleOrder": NotRequired[RuleOrderType],
        "StreamExceptionPolicy": NotRequired[StreamExceptionPolicyType],
    },
)
StatelessRuleGroupTypeDef = TypedDict(
    "StatelessRuleGroupTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Priority": NotRequired[int],
    },
)
NetworkFirewallPolicyTypeDef = TypedDict(
    "NetworkFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": NotRequired[FirewallDeploymentModelType],
    },
)
NetworkFirewallStatefulRuleGroupOverrideTypeDef = TypedDict(
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    {
        "Action": NotRequired[Literal["DROP_TO_ALERT"]],
    },
)
OrganizationalUnitScopeTypeDef = TypedDict(
    "OrganizationalUnitScopeTypeDef",
    {
        "OrganizationalUnits": NotRequired[Sequence[str]],
        "AllOrganizationalUnitsEnabled": NotRequired[bool],
        "ExcludeSpecifiedOrganizationalUnits": NotRequired[bool],
    },
)
ThirdPartyFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": NotRequired[FirewallDeploymentModelType],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
PolicyTypeScopeTypeDef = TypedDict(
    "PolicyTypeScopeTypeDef",
    {
        "PolicyTypes": NotRequired[Sequence[SecurityServiceTypeType]],
        "AllPolicyTypesEnabled": NotRequired[bool],
    },
)
PutNotificationChannelRequestRequestTypeDef = TypedDict(
    "PutNotificationChannelRequestRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
    },
)
RegionScopeTypeDef = TypedDict(
    "RegionScopeTypeDef",
    {
        "Regions": NotRequired[Sequence[str]],
        "AllRegionsEnabled": NotRequired[bool],
    },
)
ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CurrentRouteTable": NotRequired[str],
        "ExpectedRouteTable": NotRequired[str],
    },
)
ThirdPartyFirewallMissingFirewallViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
ThirdPartyFirewallMissingSubnetViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
WebACLHasIncompatibleConfigurationViolationTypeDef = TypedDict(
    "WebACLHasIncompatibleConfigurationViolationTypeDef",
    {
        "WebACLArn": NotRequired[str],
        "Description": NotRequired[str],
    },
)
WebACLHasOutOfScopeResourcesViolationTypeDef = TypedDict(
    "WebACLHasOutOfScopeResourcesViolationTypeDef",
    {
        "WebACLArn": NotRequired[str],
        "OutOfScopeResourceList": NotRequired[List[str]],
    },
)
SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "IPV4Range": NotRequired[str],
        "IPV6Range": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "Protocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
AccountScopeUnionTypeDef = Union[AccountScopeTypeDef, AccountScopeOutputTypeDef]
CreateNetworkAclActionTypeDef = TypedDict(
    "CreateNetworkAclActionTypeDef",
    {
        "Description": NotRequired[str],
        "Vpc": NotRequired[ActionTargetTypeDef],
        "FMSCanRemediate": NotRequired[bool],
    },
)
EC2AssociateRouteTableActionTypeDef = TypedDict(
    "EC2AssociateRouteTableActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "SubnetId": NotRequired[ActionTargetTypeDef],
        "GatewayId": NotRequired[ActionTargetTypeDef],
    },
)
EC2CopyRouteTableActionTypeDef = TypedDict(
    "EC2CopyRouteTableActionTypeDef",
    {
        "VpcId": ActionTargetTypeDef,
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
    },
)
EC2CreateRouteActionTypeDef = TypedDict(
    "EC2CreateRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "VpcEndpointId": NotRequired[ActionTargetTypeDef],
        "GatewayId": NotRequired[ActionTargetTypeDef],
    },
)
EC2CreateRouteTableActionTypeDef = TypedDict(
    "EC2CreateRouteTableActionTypeDef",
    {
        "VpcId": ActionTargetTypeDef,
        "Description": NotRequired[str],
    },
)
EC2DeleteRouteActionTypeDef = TypedDict(
    "EC2DeleteRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
    },
)
EC2ReplaceRouteActionTypeDef = TypedDict(
    "EC2ReplaceRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "GatewayId": NotRequired[ActionTargetTypeDef],
    },
)
EC2ReplaceRouteTableAssociationActionTypeDef = TypedDict(
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    {
        "AssociationId": ActionTargetTypeDef,
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
    },
)
ReplaceNetworkAclAssociationActionTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationActionTypeDef",
    {
        "Description": NotRequired[str],
        "AssociationId": NotRequired[ActionTargetTypeDef],
        "NetworkAclId": NotRequired[ActionTargetTypeDef],
        "FMSCanRemediate": NotRequired[bool],
    },
)
AdminScopeOutputTypeDef = TypedDict(
    "AdminScopeOutputTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeOutputTypeDef],
        "OrganizationalUnitScope": NotRequired[OrganizationalUnitScopeOutputTypeDef],
        "RegionScope": NotRequired[RegionScopeOutputTypeDef],
        "PolicyTypeScope": NotRequired[PolicyTypeScopeOutputTypeDef],
    },
)
AppsListDataOutputTypeDef = TypedDict(
    "AppsListDataOutputTypeDef",
    {
        "ListName": str,
        "AppsList": List[AppTypeDef],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "PreviousAppsList": NotRequired[Dict[str, List[AppTypeDef]]],
    },
)
AppsListDataSummaryTypeDef = TypedDict(
    "AppsListDataSummaryTypeDef",
    {
        "ListArn": NotRequired[str],
        "ListId": NotRequired[str],
        "ListName": NotRequired[str],
        "AppsList": NotRequired[List[AppTypeDef]],
    },
)
AppsListDataTypeDef = TypedDict(
    "AppsListDataTypeDef",
    {
        "ListName": str,
        "AppsList": Sequence[AppTypeDef],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[TimestampTypeDef],
        "LastUpdateTime": NotRequired[TimestampTypeDef],
        "PreviousAppsList": NotRequired[Mapping[str, Sequence[AppTypeDef]]],
    },
)
GetProtectionStatusRequestRequestTypeDef = TypedDict(
    "GetProtectionStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccountId": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ProtocolsListDataTypeDef = TypedDict(
    "ProtocolsListDataTypeDef",
    {
        "ListName": str,
        "ProtocolsList": Sequence[str],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[TimestampTypeDef],
        "LastUpdateTime": NotRequired[TimestampTypeDef],
        "PreviousProtocolsList": NotRequired[Mapping[str, Sequence[str]]],
    },
)
ResourceSetTypeDef = TypedDict(
    "ResourceSetTypeDef",
    {
        "Name": str,
        "ResourceTypeList": Sequence[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "UpdateToken": NotRequired[str],
        "LastUpdateTime": NotRequired[TimestampTypeDef],
        "ResourceSetStatus": NotRequired[ResourceSetStatusType],
    },
)
AssociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "AssociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAdminAccountResponseTypeDef = TypedDict(
    "GetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": AccountRoleStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNotificationChannelResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProtectionStatusResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": SecurityServiceTypeType,
        "Data": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetThirdPartyFirewallAssociationStatusResponseTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "MarketplaceOnboardingStatus": MarketplaceSubscriptionOnboardingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAdminAccountsForOrganizationResponseTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationResponseTypeDef",
    {
        "AdminAccounts": List[AdminAccountSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAdminsManagingAccountResponseTypeDef = TypedDict(
    "ListAdminsManagingAccountResponseTypeDef",
    {
        "AdminAccounts": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {
        "MemberAccounts": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AwsEc2InstanceViolationTypeDef = TypedDict(
    "AwsEc2InstanceViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "AwsEc2NetworkInterfaceViolations": NotRequired[
            List[AwsEc2NetworkInterfaceViolationTypeDef]
        ],
    },
)
BatchAssociateResourceResponseTypeDef = TypedDict(
    "BatchAssociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List[FailedItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateResourceResponseTypeDef = TypedDict(
    "BatchDisassociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List[FailedItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyComplianceDetailTypeDef = TypedDict(
    "PolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": NotRequired[str],
        "PolicyId": NotRequired[str],
        "MemberAccount": NotRequired[str],
        "Violators": NotRequired[List[ComplianceViolatorTypeDef]],
        "EvaluationLimitExceeded": NotRequired[bool],
        "ExpiredAt": NotRequired[datetime],
        "IssueInfoMap": NotRequired[Dict[DependentServiceNameType, str]],
    },
)
ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "Items": List[DiscoveredResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PolicyComplianceStatusTypeDef = TypedDict(
    "PolicyComplianceStatusTypeDef",
    {
        "PolicyOwner": NotRequired[str],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "MemberAccount": NotRequired[str],
        "EvaluationResults": NotRequired[List[EvaluationResultTypeDef]],
        "LastUpdated": NotRequired[datetime],
        "IssueInfoMap": NotRequired[Dict[DependentServiceNameType, str]],
    },
)
NetworkFirewallMissingExpectedRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ExpectedRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "VpcId": NotRequired[str],
    },
)
GetProtocolsListResponseTypeDef = TypedDict(
    "GetProtocolsListResponseTypeDef",
    {
        "ProtocolsList": ProtocolsListDataOutputTypeDef,
        "ProtocolsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProtocolsListResponseTypeDef = TypedDict(
    "PutProtocolsListResponseTypeDef",
    {
        "ProtocolsList": ProtocolsListDataOutputTypeDef,
        "ProtocolsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceSetResponseTypeDef = TypedDict(
    "GetResourceSetResponseTypeDef",
    {
        "ResourceSet": ResourceSetOutputTypeDef,
        "ResourceSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourceSetResponseTypeDef = TypedDict(
    "PutResourceSetResponseTypeDef",
    {
        "ResourceSet": ResourceSetOutputTypeDef,
        "ResourceSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef = TypedDict(
    "ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAppsListsRequestListAppsListsPaginateTypeDef = TypedDict(
    "ListAppsListsRequestListAppsListsPaginateTypeDef",
    {
        "DefaultLists": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComplianceStatusRequestListComplianceStatusPaginateTypeDef = TypedDict(
    "ListComplianceStatusRequestListComplianceStatusPaginateTypeDef",
    {
        "PolicyId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMemberAccountsRequestListMemberAccountsPaginateTypeDef = TypedDict(
    "ListMemberAccountsRequestListMemberAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesRequestListPoliciesPaginateTypeDef = TypedDict(
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProtocolsListsRequestListProtocolsListsPaginateTypeDef = TypedDict(
    "ListProtocolsListsRequestListProtocolsListsPaginateTypeDef",
    {
        "DefaultLists": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "PolicyList": List[PolicySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProtocolsListsResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseTypeDef",
    {
        "ProtocolsLists": List[ProtocolsListDataSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourceSetResourcesResponseTypeDef = TypedDict(
    "ListResourceSetResourcesResponseTypeDef",
    {
        "Items": List[ResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourceSetsResponseTypeDef = TypedDict(
    "ListResourceSetsResponseTypeDef",
    {
        "ResourceSets": List[ResourceSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": Sequence[TagTypeDef],
    },
)
ListThirdPartyFirewallFirewallPoliciesResponseTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    {
        "ThirdPartyFirewallFirewallPolicies": List[ThirdPartyFirewallFirewallPolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
NetworkAclEntryTypeDef = TypedDict(
    "NetworkAclEntryTypeDef",
    {
        "Protocol": str,
        "RuleAction": NetworkAclRuleActionType,
        "Egress": bool,
        "IcmpTypeCode": NotRequired[NetworkAclIcmpTypeCodeTypeDef],
        "PortRange": NotRequired[NetworkAclPortRangeTypeDef],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
    },
)
NetworkFirewallBlackHoleRouteDetectedViolationTypeDef = TypedDict(
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "VpcId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
    },
)
NetworkFirewallInternetTrafficNotInspectedViolationTypeDef = TypedDict(
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "IsRouteTableUsedInDifferentAZ": NotRequired[bool],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "ExpectedFirewallEndpoint": NotRequired[str],
        "FirewallSubnetId": NotRequired[str],
        "ExpectedFirewallSubnetRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualFirewallSubnetRoutes": NotRequired[List[RouteTypeDef]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "ExpectedInternetGatewayRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualInternetGatewayRoutes": NotRequired[List[RouteTypeDef]],
        "VpcId": NotRequired[str],
    },
)
NetworkFirewallInvalidRouteConfigurationViolationTypeDef = TypedDict(
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    {
        "AffectedSubnets": NotRequired[List[str]],
        "RouteTableId": NotRequired[str],
        "IsRouteTableUsedInDifferentAZ": NotRequired[bool],
        "ViolatingRoute": NotRequired[RouteTypeDef],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "ExpectedFirewallEndpoint": NotRequired[str],
        "ActualFirewallEndpoint": NotRequired[str],
        "ExpectedFirewallSubnetId": NotRequired[str],
        "ActualFirewallSubnetId": NotRequired[str],
        "ExpectedFirewallSubnetRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualFirewallSubnetRoutes": NotRequired[List[RouteTypeDef]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "ExpectedInternetGatewayRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualInternetGatewayRoutes": NotRequired[List[RouteTypeDef]],
        "VpcId": NotRequired[str],
    },
)
NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "RouteTableId": NotRequired[str],
        "FirewallEndpoint": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    {
        "GatewayId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "RouteTableId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
RouteHasOutOfScopeEndpointViolationTypeDef = TypedDict(
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "FirewallSubnetId": NotRequired[str],
        "FirewallSubnetRoutes": NotRequired[List[RouteTypeDef]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "InternetGatewayRoutes": NotRequired[List[RouteTypeDef]],
    },
)
StatefulRuleGroupTypeDef = TypedDict(
    "StatefulRuleGroupTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Priority": NotRequired[int],
        "Override": NotRequired[NetworkFirewallStatefulRuleGroupOverrideTypeDef],
    },
)
OrganizationalUnitScopeUnionTypeDef = Union[
    OrganizationalUnitScopeTypeDef, OrganizationalUnitScopeOutputTypeDef
]
PolicyTypeScopeUnionTypeDef = Union[PolicyTypeScopeTypeDef, PolicyTypeScopeOutputTypeDef]
RegionScopeUnionTypeDef = Union[RegionScopeTypeDef, RegionScopeOutputTypeDef]
SecurityGroupRemediationActionTypeDef = TypedDict(
    "SecurityGroupRemediationActionTypeDef",
    {
        "RemediationActionType": NotRequired[RemediationActionTypeType],
        "Description": NotRequired[str],
        "RemediationResult": NotRequired[SecurityGroupRuleDescriptionTypeDef],
        "IsDefaultAction": NotRequired[bool],
    },
)
GetAdminScopeResponseTypeDef = TypedDict(
    "GetAdminScopeResponseTypeDef",
    {
        "AdminScope": AdminScopeOutputTypeDef,
        "Status": OrganizationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppsListResponseTypeDef = TypedDict(
    "GetAppsListResponseTypeDef",
    {
        "AppsList": AppsListDataOutputTypeDef,
        "AppsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppsListResponseTypeDef = TypedDict(
    "PutAppsListResponseTypeDef",
    {
        "AppsList": AppsListDataOutputTypeDef,
        "AppsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppsListsResponseTypeDef = TypedDict(
    "ListAppsListsResponseTypeDef",
    {
        "AppsLists": List[AppsListDataSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutAppsListRequestRequestTypeDef = TypedDict(
    "PutAppsListRequestRequestTypeDef",
    {
        "AppsList": AppsListDataTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
PutProtocolsListRequestRequestTypeDef = TypedDict(
    "PutProtocolsListRequestRequestTypeDef",
    {
        "ProtocolsList": ProtocolsListDataTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
PutResourceSetRequestRequestTypeDef = TypedDict(
    "PutResourceSetRequestRequestTypeDef",
    {
        "ResourceSet": ResourceSetTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
GetComplianceDetailResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseTypeDef",
    {
        "PolicyComplianceDetail": PolicyComplianceDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[PolicyComplianceStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EntryDescriptionTypeDef = TypedDict(
    "EntryDescriptionTypeDef",
    {
        "EntryDetail": NotRequired[NetworkAclEntryTypeDef],
        "EntryRuleNumber": NotRequired[int],
        "EntryType": NotRequired[EntryTypeType],
    },
)
NetworkAclEntrySetOutputTypeDef = TypedDict(
    "NetworkAclEntrySetOutputTypeDef",
    {
        "ForceRemediateForFirstEntries": bool,
        "ForceRemediateForLastEntries": bool,
        "FirstEntries": NotRequired[List[NetworkAclEntryTypeDef]],
        "LastEntries": NotRequired[List[NetworkAclEntryTypeDef]],
    },
)
NetworkAclEntrySetTypeDef = TypedDict(
    "NetworkAclEntrySetTypeDef",
    {
        "ForceRemediateForFirstEntries": bool,
        "ForceRemediateForLastEntries": bool,
        "FirstEntries": NotRequired[Sequence[NetworkAclEntryTypeDef]],
        "LastEntries": NotRequired[Sequence[NetworkAclEntryTypeDef]],
    },
)
NetworkFirewallPolicyDescriptionTypeDef = TypedDict(
    "NetworkFirewallPolicyDescriptionTypeDef",
    {
        "StatelessRuleGroups": NotRequired[List[StatelessRuleGroupTypeDef]],
        "StatelessDefaultActions": NotRequired[List[str]],
        "StatelessFragmentDefaultActions": NotRequired[List[str]],
        "StatelessCustomActions": NotRequired[List[str]],
        "StatefulRuleGroups": NotRequired[List[StatefulRuleGroupTypeDef]],
        "StatefulDefaultActions": NotRequired[List[str]],
        "StatefulEngineOptions": NotRequired[StatefulEngineOptionsTypeDef],
    },
)
AdminScopeTypeDef = TypedDict(
    "AdminScopeTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeUnionTypeDef],
        "OrganizationalUnitScope": NotRequired[OrganizationalUnitScopeUnionTypeDef],
        "RegionScope": NotRequired[RegionScopeUnionTypeDef],
        "PolicyTypeScope": NotRequired[PolicyTypeScopeUnionTypeDef],
    },
)
AwsVPCSecurityGroupViolationTypeDef = TypedDict(
    "AwsVPCSecurityGroupViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "PartialMatches": NotRequired[List[PartialMatchTypeDef]],
        "PossibleSecurityGroupRemediationActions": NotRequired[
            List[SecurityGroupRemediationActionTypeDef]
        ],
    },
)
CreateNetworkAclEntriesActionTypeDef = TypedDict(
    "CreateNetworkAclEntriesActionTypeDef",
    {
        "Description": NotRequired[str],
        "NetworkAclId": NotRequired[ActionTargetTypeDef],
        "NetworkAclEntriesToBeCreated": NotRequired[List[EntryDescriptionTypeDef]],
        "FMSCanRemediate": NotRequired[bool],
    },
)
DeleteNetworkAclEntriesActionTypeDef = TypedDict(
    "DeleteNetworkAclEntriesActionTypeDef",
    {
        "Description": NotRequired[str],
        "NetworkAclId": NotRequired[ActionTargetTypeDef],
        "NetworkAclEntriesToBeDeleted": NotRequired[List[EntryDescriptionTypeDef]],
        "FMSCanRemediate": NotRequired[bool],
    },
)
EntryViolationTypeDef = TypedDict(
    "EntryViolationTypeDef",
    {
        "ExpectedEntry": NotRequired[EntryDescriptionTypeDef],
        "ExpectedEvaluationOrder": NotRequired[str],
        "ActualEvaluationOrder": NotRequired[str],
        "EntryAtExpectedEvaluationOrder": NotRequired[EntryDescriptionTypeDef],
        "EntriesWithConflicts": NotRequired[List[EntryDescriptionTypeDef]],
        "EntryViolationReasons": NotRequired[List[EntryViolationReasonType]],
    },
)
NetworkAclCommonPolicyOutputTypeDef = TypedDict(
    "NetworkAclCommonPolicyOutputTypeDef",
    {
        "NetworkAclEntrySet": NetworkAclEntrySetOutputTypeDef,
    },
)
NetworkAclEntrySetUnionTypeDef = Union[NetworkAclEntrySetTypeDef, NetworkAclEntrySetOutputTypeDef]
NetworkFirewallPolicyModifiedViolationTypeDef = TypedDict(
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "CurrentPolicyDescription": NotRequired[NetworkFirewallPolicyDescriptionTypeDef],
        "ExpectedPolicyDescription": NotRequired[NetworkFirewallPolicyDescriptionTypeDef],
    },
)
PutAdminAccountRequestRequestTypeDef = TypedDict(
    "PutAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
        "AdminScope": NotRequired[AdminScopeTypeDef],
    },
)
RemediationActionTypeDef = TypedDict(
    "RemediationActionTypeDef",
    {
        "Description": NotRequired[str],
        "EC2CreateRouteAction": NotRequired[EC2CreateRouteActionTypeDef],
        "EC2ReplaceRouteAction": NotRequired[EC2ReplaceRouteActionTypeDef],
        "EC2DeleteRouteAction": NotRequired[EC2DeleteRouteActionTypeDef],
        "EC2CopyRouteTableAction": NotRequired[EC2CopyRouteTableActionTypeDef],
        "EC2ReplaceRouteTableAssociationAction": NotRequired[
            EC2ReplaceRouteTableAssociationActionTypeDef
        ],
        "EC2AssociateRouteTableAction": NotRequired[EC2AssociateRouteTableActionTypeDef],
        "EC2CreateRouteTableAction": NotRequired[EC2CreateRouteTableActionTypeDef],
        "FMSPolicyUpdateFirewallCreationConfigAction": NotRequired[
            FMSPolicyUpdateFirewallCreationConfigActionTypeDef
        ],
        "CreateNetworkAclAction": NotRequired[CreateNetworkAclActionTypeDef],
        "ReplaceNetworkAclAssociationAction": NotRequired[
            ReplaceNetworkAclAssociationActionTypeDef
        ],
        "CreateNetworkAclEntriesAction": NotRequired[CreateNetworkAclEntriesActionTypeDef],
        "DeleteNetworkAclEntriesAction": NotRequired[DeleteNetworkAclEntriesActionTypeDef],
    },
)
InvalidNetworkAclEntriesViolationTypeDef = TypedDict(
    "InvalidNetworkAclEntriesViolationTypeDef",
    {
        "Vpc": NotRequired[str],
        "Subnet": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "CurrentAssociatedNetworkAcl": NotRequired[str],
        "EntryViolations": NotRequired[List[EntryViolationTypeDef]],
    },
)
PolicyOptionOutputTypeDef = TypedDict(
    "PolicyOptionOutputTypeDef",
    {
        "NetworkFirewallPolicy": NotRequired[NetworkFirewallPolicyTypeDef],
        "ThirdPartyFirewallPolicy": NotRequired[ThirdPartyFirewallPolicyTypeDef],
        "NetworkAclCommonPolicy": NotRequired[NetworkAclCommonPolicyOutputTypeDef],
    },
)
NetworkAclCommonPolicyTypeDef = TypedDict(
    "NetworkAclCommonPolicyTypeDef",
    {
        "NetworkAclEntrySet": NetworkAclEntrySetUnionTypeDef,
    },
)
RemediationActionWithOrderTypeDef = TypedDict(
    "RemediationActionWithOrderTypeDef",
    {
        "RemediationAction": NotRequired[RemediationActionTypeDef],
        "Order": NotRequired[int],
    },
)
SecurityServicePolicyDataOutputTypeDef = TypedDict(
    "SecurityServicePolicyDataOutputTypeDef",
    {
        "Type": SecurityServiceTypeType,
        "ManagedServiceData": NotRequired[str],
        "PolicyOption": NotRequired[PolicyOptionOutputTypeDef],
    },
)
NetworkAclCommonPolicyUnionTypeDef = Union[
    NetworkAclCommonPolicyTypeDef, NetworkAclCommonPolicyOutputTypeDef
]
PossibleRemediationActionTypeDef = TypedDict(
    "PossibleRemediationActionTypeDef",
    {
        "OrderedRemediationActions": List[RemediationActionWithOrderTypeDef],
        "Description": NotRequired[str],
        "IsDefaultAction": NotRequired[bool],
    },
)
PolicyOutputTypeDef = TypedDict(
    "PolicyOutputTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": SecurityServicePolicyDataOutputTypeDef,
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "PolicyId": NotRequired[str],
        "PolicyUpdateToken": NotRequired[str],
        "ResourceTypeList": NotRequired[List[str]],
        "ResourceTags": NotRequired[List[ResourceTagTypeDef]],
        "DeleteUnusedFMManagedResources": NotRequired[bool],
        "IncludeMap": NotRequired[Dict[CustomerPolicyScopeIdTypeType, List[str]]],
        "ExcludeMap": NotRequired[Dict[CustomerPolicyScopeIdTypeType, List[str]]],
        "ResourceSetIds": NotRequired[List[str]],
        "PolicyDescription": NotRequired[str],
        "PolicyStatus": NotRequired[CustomerPolicyStatusType],
    },
)
PolicyOptionTypeDef = TypedDict(
    "PolicyOptionTypeDef",
    {
        "NetworkFirewallPolicy": NotRequired[NetworkFirewallPolicyTypeDef],
        "ThirdPartyFirewallPolicy": NotRequired[ThirdPartyFirewallPolicyTypeDef],
        "NetworkAclCommonPolicy": NotRequired[NetworkAclCommonPolicyUnionTypeDef],
    },
)
PossibleRemediationActionsTypeDef = TypedDict(
    "PossibleRemediationActionsTypeDef",
    {
        "Description": NotRequired[str],
        "Actions": NotRequired[List[PossibleRemediationActionTypeDef]],
    },
)
GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": PolicyOutputTypeDef,
        "PolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPolicyResponseTypeDef = TypedDict(
    "PutPolicyResponseTypeDef",
    {
        "Policy": PolicyOutputTypeDef,
        "PolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyOptionUnionTypeDef = Union[PolicyOptionTypeDef, PolicyOptionOutputTypeDef]
ResourceViolationTypeDef = TypedDict(
    "ResourceViolationTypeDef",
    {
        "AwsVPCSecurityGroupViolation": NotRequired[AwsVPCSecurityGroupViolationTypeDef],
        "AwsEc2NetworkInterfaceViolation": NotRequired[AwsEc2NetworkInterfaceViolationTypeDef],
        "AwsEc2InstanceViolation": NotRequired[AwsEc2InstanceViolationTypeDef],
        "NetworkFirewallMissingFirewallViolation": NotRequired[
            NetworkFirewallMissingFirewallViolationTypeDef
        ],
        "NetworkFirewallMissingSubnetViolation": NotRequired[
            NetworkFirewallMissingSubnetViolationTypeDef
        ],
        "NetworkFirewallMissingExpectedRTViolation": NotRequired[
            NetworkFirewallMissingExpectedRTViolationTypeDef
        ],
        "NetworkFirewallPolicyModifiedViolation": NotRequired[
            NetworkFirewallPolicyModifiedViolationTypeDef
        ],
        "NetworkFirewallInternetTrafficNotInspectedViolation": NotRequired[
            NetworkFirewallInternetTrafficNotInspectedViolationTypeDef
        ],
        "NetworkFirewallInvalidRouteConfigurationViolation": NotRequired[
            NetworkFirewallInvalidRouteConfigurationViolationTypeDef
        ],
        "NetworkFirewallBlackHoleRouteDetectedViolation": NotRequired[
            NetworkFirewallBlackHoleRouteDetectedViolationTypeDef
        ],
        "NetworkFirewallUnexpectedFirewallRoutesViolation": NotRequired[
            NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef
        ],
        "NetworkFirewallUnexpectedGatewayRoutesViolation": NotRequired[
            NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef
        ],
        "NetworkFirewallMissingExpectedRoutesViolation": NotRequired[
            NetworkFirewallMissingExpectedRoutesViolationTypeDef
        ],
        "DnsRuleGroupPriorityConflictViolation": NotRequired[
            DnsRuleGroupPriorityConflictViolationTypeDef
        ],
        "DnsDuplicateRuleGroupViolation": NotRequired[DnsDuplicateRuleGroupViolationTypeDef],
        "DnsRuleGroupLimitExceededViolation": NotRequired[
            DnsRuleGroupLimitExceededViolationTypeDef
        ],
        "FirewallSubnetIsOutOfScopeViolation": NotRequired[
            FirewallSubnetIsOutOfScopeViolationTypeDef
        ],
        "RouteHasOutOfScopeEndpointViolation": NotRequired[
            RouteHasOutOfScopeEndpointViolationTypeDef
        ],
        "ThirdPartyFirewallMissingFirewallViolation": NotRequired[
            ThirdPartyFirewallMissingFirewallViolationTypeDef
        ],
        "ThirdPartyFirewallMissingSubnetViolation": NotRequired[
            ThirdPartyFirewallMissingSubnetViolationTypeDef
        ],
        "ThirdPartyFirewallMissingExpectedRouteTableViolation": NotRequired[
            ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef
        ],
        "FirewallSubnetMissingVPCEndpointViolation": NotRequired[
            FirewallSubnetMissingVPCEndpointViolationTypeDef
        ],
        "InvalidNetworkAclEntriesViolation": NotRequired[InvalidNetworkAclEntriesViolationTypeDef],
        "PossibleRemediationActions": NotRequired[PossibleRemediationActionsTypeDef],
        "WebACLHasIncompatibleConfigurationViolation": NotRequired[
            WebACLHasIncompatibleConfigurationViolationTypeDef
        ],
        "WebACLHasOutOfScopeResourcesViolation": NotRequired[
            WebACLHasOutOfScopeResourcesViolationTypeDef
        ],
    },
)
SecurityServicePolicyDataTypeDef = TypedDict(
    "SecurityServicePolicyDataTypeDef",
    {
        "Type": SecurityServiceTypeType,
        "ManagedServiceData": NotRequired[str],
        "PolicyOption": NotRequired[PolicyOptionUnionTypeDef],
    },
)
ViolationDetailTypeDef = TypedDict(
    "ViolationDetailTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceViolations": List[ResourceViolationTypeDef],
        "ResourceTags": NotRequired[List[TagTypeDef]],
        "ResourceDescription": NotRequired[str],
    },
)
SecurityServicePolicyDataUnionTypeDef = Union[
    SecurityServicePolicyDataTypeDef, SecurityServicePolicyDataOutputTypeDef
]
GetViolationDetailsResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseTypeDef",
    {
        "ViolationDetail": ViolationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": SecurityServicePolicyDataUnionTypeDef,
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "PolicyId": NotRequired[str],
        "PolicyUpdateToken": NotRequired[str],
        "ResourceTypeList": NotRequired[Sequence[str]],
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
        "DeleteUnusedFMManagedResources": NotRequired[bool],
        "IncludeMap": NotRequired[Mapping[CustomerPolicyScopeIdTypeType, Sequence[str]]],
        "ExcludeMap": NotRequired[Mapping[CustomerPolicyScopeIdTypeType, Sequence[str]]],
        "ResourceSetIds": NotRequired[Sequence[str]],
        "PolicyDescription": NotRequired[str],
        "PolicyStatus": NotRequired[CustomerPolicyStatusType],
    },
)
PutPolicyRequestRequestTypeDef = TypedDict(
    "PutPolicyRequestRequestTypeDef",
    {
        "Policy": PolicyTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
