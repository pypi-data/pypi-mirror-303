"""
Type annotations for dms service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/type_defs/)

Usage::

    ```python
    from mypy_boto3_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AssessmentReportTypeType,
    AuthMechanismValueType,
    AuthTypeValueType,
    CannedAclForObjectsValueType,
    CharLengthSemanticsType,
    CollectorStatusType,
    CompressionTypeValueType,
    DatabaseModeType,
    DataFormatValueType,
    DatePartitionDelimiterValueType,
    DatePartitionSequenceValueType,
    DmsSslModeValueType,
    EncodingTypeValueType,
    EncryptionModeValueType,
    EndpointSettingTypeValueType,
    KafkaSaslMechanismType,
    KafkaSecurityProtocolType,
    KafkaSslEndpointIdentificationAlgorithmType,
    LongVarcharMappingTypeType,
    MessageFormatValueType,
    MigrationTypeValueType,
    NestingLevelValueType,
    OriginTypeValueType,
    ParquetVersionValueType,
    PluginNameValueType,
    RedisAuthTypeValueType,
    RefreshSchemasStatusTypeValueType,
    ReleaseStatusValuesType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    SafeguardPolicyType,
    SslSecurityProtocolValueType,
    StartReplicationMigrationTypeValueType,
    StartReplicationTaskTypeValueType,
    TargetDbTypeType,
    TlogAccessModeType,
    VersionStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountQuotaTypeDef",
    "TagTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchStartRecommendationsErrorEntryTypeDef",
    "BlobTypeDef",
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    "CertificateTypeDef",
    "CollectorHealthCheckTypeDef",
    "InventoryDataTypeDef",
    "CollectorShortInfoResponseTypeDef",
    "ComputeConfigOutputTypeDef",
    "ComputeConfigTypeDef",
    "ConnectionTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "GcpMySQLSettingsTypeDef",
    "IBMDb2SettingsTypeDef",
    "KafkaSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "MongoDbSettingsTypeDef",
    "MySQLSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleSettingsTypeDef",
    "PostgreSQLSettingsTypeDef",
    "RedisSettingsTypeDef",
    "RedshiftSettingsTypeDef",
    "S3SettingsTypeDef",
    "SybaseSettingsTypeDef",
    "TimestreamSettingsTypeDef",
    "EventSubscriptionTypeDef",
    "CreateFleetAdvisorCollectorRequestRequestTypeDef",
    "InstanceProfileTypeDef",
    "DataProviderDescriptorDefinitionTypeDef",
    "SCApplicationAttributesTypeDef",
    "TimestampTypeDef",
    "DataMigrationSettingsTypeDef",
    "DataMigrationStatisticsTypeDef",
    "SourceDataSettingOutputTypeDef",
    "DataProviderDescriptorTypeDef",
    "DocDbDataProviderSettingsTypeDef",
    "MariaDbDataProviderSettingsTypeDef",
    "MicrosoftSqlServerDataProviderSettingsTypeDef",
    "MongoDbDataProviderSettingsTypeDef",
    "MySqlDataProviderSettingsTypeDef",
    "OracleDataProviderSettingsTypeDef",
    "PostgreSqlDataProviderSettingsTypeDef",
    "RedshiftDataProviderSettingsTypeDef",
    "DatabaseInstanceSoftwareDetailsResponseTypeDef",
    "ServerShortInfoResponseTypeDef",
    "DatabaseShortInfoResponseTypeDef",
    "DefaultErrorDetailsTypeDef",
    "DeleteCertificateMessageRequestTypeDef",
    "DeleteCollectorRequestRequestTypeDef",
    "DeleteConnectionMessageRequestTypeDef",
    "DeleteDataMigrationMessageRequestTypeDef",
    "DeleteDataProviderMessageRequestTypeDef",
    "DeleteEndpointMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteFleetAdvisorDatabasesRequestRequestTypeDef",
    "DeleteInstanceProfileMessageRequestTypeDef",
    "DeleteMigrationProjectMessageRequestTypeDef",
    "DeleteReplicationConfigMessageRequestTypeDef",
    "DeleteReplicationInstanceMessageRequestTypeDef",
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    "DeleteReplicationTaskMessageRequestTypeDef",
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
    "DescribeConversionConfigurationMessageRequestTypeDef",
    "DescribeEndpointSettingsMessageRequestTypeDef",
    "EndpointSettingTypeDef",
    "SupportedEndpointTypeTypeDef",
    "DescribeEngineVersionsMessageRequestTypeDef",
    "EngineVersionTypeDef",
    "EventCategoryGroupTypeDef",
    "EventTypeDef",
    "DescribeFleetAdvisorLsaAnalysisRequestRequestTypeDef",
    "FleetAdvisorLsaAnalysisResponseTypeDef",
    "FleetAdvisorSchemaObjectResponseTypeDef",
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "LimitationTypeDef",
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    "RefreshSchemasStatusTypeDef",
    "DescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "TableStatisticsTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskIndividualAssessmentTypeDef",
    "DescribeSchemasMessageRequestTypeDef",
    "OracleSettingsOutputTypeDef",
    "ExportMetadataModelAssessmentMessageRequestTypeDef",
    "ExportMetadataModelAssessmentResultEntryTypeDef",
    "ExportSqlDetailsTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ModifyConversionConfigurationMessageRequestTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyInstanceProfileMessageRequestTypeDef",
    "ModifyReplicationInstanceMessageRequestTypeDef",
    "ModifyReplicationSubnetGroupMessageRequestTypeDef",
    "MoveReplicationTaskMessageRequestTypeDef",
    "PendingMaintenanceActionTypeDef",
    "ProvisionDataTypeDef",
    "RdsConfigurationTypeDef",
    "RdsRequirementsTypeDef",
    "RebootReplicationInstanceMessageRequestTypeDef",
    "RecommendationSettingsTypeDef",
    "RefreshSchemasMessageRequestTypeDef",
    "TableToReloadTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "ReplicationStatsTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
    "ReplicationTaskAssessmentRunResultStatisticTypeDef",
    "ReplicationTaskStatsTypeDef",
    "SchemaShortInfoResponseTypeDef",
    "StartDataMigrationMessageRequestTypeDef",
    "StartExtensionPackAssociationMessageRequestTypeDef",
    "StartMetadataModelAssessmentMessageRequestTypeDef",
    "StartMetadataModelConversionMessageRequestTypeDef",
    "StartMetadataModelExportAsScriptMessageRequestTypeDef",
    "StartMetadataModelExportToTargetMessageRequestTypeDef",
    "StartMetadataModelImportMessageRequestTypeDef",
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    "StopDataMigrationMessageRequestTypeDef",
    "StopReplicationMessageRequestTypeDef",
    "StopReplicationTaskMessageRequestTypeDef",
    "TestConnectionMessageRequestTypeDef",
    "UpdateSubscriptionsToEventBridgeMessageRequestTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateInstanceProfileMessageRequestTypeDef",
    "CreateReplicationInstanceMessageRequestTypeDef",
    "CreateReplicationSubnetGroupMessageRequestTypeDef",
    "StartReplicationTaskAssessmentRunMessageRequestTypeDef",
    "CreateFleetAdvisorCollectorResponseTypeDef",
    "DeleteFleetAdvisorDatabasesResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    "DescribeConversionConfigurationResponseTypeDef",
    "DescribeSchemasResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyConversionConfigurationResponseTypeDef",
    "ReloadReplicationTablesResponseTypeDef",
    "ReloadTablesResponseTypeDef",
    "RunFleetAdvisorLsaAnalysisResponseTypeDef",
    "StartExtensionPackAssociationResponseTypeDef",
    "StartMetadataModelAssessmentResponseTypeDef",
    "StartMetadataModelConversionResponseTypeDef",
    "StartMetadataModelExportAsScriptResponseTypeDef",
    "StartMetadataModelExportToTargetResponseTypeDef",
    "StartMetadataModelImportResponseTypeDef",
    "UpdateSubscriptionsToEventBridgeResponseTypeDef",
    "SubnetTypeDef",
    "BatchStartRecommendationsResponseTypeDef",
    "ImportCertificateMessageRequestTypeDef",
    "DeleteCertificateResponseTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "ImportCertificateResponseTypeDef",
    "CollectorResponseTypeDef",
    "ReplicationConfigTypeDef",
    "CreateReplicationConfigMessageRequestTypeDef",
    "ModifyReplicationConfigMessageRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "TestConnectionResponseTypeDef",
    "CreateEndpointMessageRequestTypeDef",
    "ModifyEndpointMessageRequestTypeDef",
    "CreateEventSubscriptionResponseTypeDef",
    "DeleteEventSubscriptionResponseTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "ModifyEventSubscriptionResponseTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "DeleteInstanceProfileResponseTypeDef",
    "DescribeInstanceProfilesResponseTypeDef",
    "ModifyInstanceProfileResponseTypeDef",
    "CreateMigrationProjectMessageRequestTypeDef",
    "ModifyMigrationProjectMessageRequestTypeDef",
    "CreateReplicationTaskMessageRequestTypeDef",
    "ModifyReplicationTaskMessageRequestTypeDef",
    "SourceDataSettingTypeDef",
    "StartReplicationMessageRequestTypeDef",
    "StartReplicationTaskMessageRequestTypeDef",
    "DataMigrationTypeDef",
    "MigrationProjectTypeDef",
    "DataProviderSettingsTypeDef",
    "DatabaseResponseTypeDef",
    "ErrorDetailsTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeConnectionsMessageRequestTypeDef",
    "DescribeDataMigrationsMessageRequestTypeDef",
    "DescribeDataProvidersMessageRequestTypeDef",
    "DescribeEndpointTypesMessageRequestTypeDef",
    "DescribeEndpointsMessageRequestTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeExtensionPackAssociationsMessageRequestTypeDef",
    "DescribeFleetAdvisorCollectorsRequestRequestTypeDef",
    "DescribeFleetAdvisorDatabasesRequestRequestTypeDef",
    "DescribeFleetAdvisorSchemaObjectSummaryRequestRequestTypeDef",
    "DescribeFleetAdvisorSchemasRequestRequestTypeDef",
    "DescribeInstanceProfilesMessageRequestTypeDef",
    "DescribeMetadataModelAssessmentsMessageRequestTypeDef",
    "DescribeMetadataModelConversionsMessageRequestTypeDef",
    "DescribeMetadataModelExportsAsScriptMessageRequestTypeDef",
    "DescribeMetadataModelExportsToTargetMessageRequestTypeDef",
    "DescribeMetadataModelImportsMessageRequestTypeDef",
    "DescribeMigrationProjectsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribeRecommendationLimitationsRequestRequestTypeDef",
    "DescribeRecommendationsRequestRequestTypeDef",
    "DescribeReplicationConfigsMessageRequestTypeDef",
    "DescribeReplicationInstancesMessageRequestTypeDef",
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    "DescribeReplicationTableStatisticsMessageRequestTypeDef",
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    "DescribeReplicationTasksMessageRequestTypeDef",
    "DescribeReplicationsMessageRequestTypeDef",
    "DescribeTableStatisticsMessageRequestTypeDef",
    "DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef",
    "DescribeConnectionsMessageDescribeConnectionsPaginateTypeDef",
    "DescribeDataMigrationsMessageDescribeDataMigrationsPaginateTypeDef",
    "DescribeEndpointTypesMessageDescribeEndpointTypesPaginateTypeDef",
    "DescribeEndpointsMessageDescribeEndpointsPaginateTypeDef",
    "DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef",
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    "DescribeOrderableReplicationInstancesMessageDescribeOrderableReplicationInstancesPaginateTypeDef",
    "DescribeReplicationInstancesMessageDescribeReplicationInstancesPaginateTypeDef",
    "DescribeReplicationSubnetGroupsMessageDescribeReplicationSubnetGroupsPaginateTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessageDescribeReplicationTaskAssessmentResultsPaginateTypeDef",
    "DescribeReplicationTasksMessageDescribeReplicationTasksPaginateTypeDef",
    "DescribeSchemasMessageDescribeSchemasPaginateTypeDef",
    "DescribeTableStatisticsMessageDescribeTableStatisticsPaginateTypeDef",
    "DescribeConnectionsMessageTestConnectionSucceedsWaitTypeDef",
    "DescribeEndpointsMessageEndpointDeletedWaitTypeDef",
    "DescribeReplicationInstancesMessageReplicationInstanceAvailableWaitTypeDef",
    "DescribeReplicationInstancesMessageReplicationInstanceDeletedWaitTypeDef",
    "DescribeReplicationTasksMessageReplicationTaskDeletedWaitTypeDef",
    "DescribeReplicationTasksMessageReplicationTaskReadyWaitTypeDef",
    "DescribeReplicationTasksMessageReplicationTaskRunningWaitTypeDef",
    "DescribeReplicationTasksMessageReplicationTaskStoppedWaitTypeDef",
    "DescribeEndpointSettingsResponseTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DescribeEngineVersionsResponseTypeDef",
    "DescribeEventCategoriesResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeFleetAdvisorLsaAnalysisResponseTypeDef",
    "DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "DescribeRecommendationLimitationsResponseTypeDef",
    "DescribeRefreshSchemasStatusResponseTypeDef",
    "RefreshSchemasResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    "DescribeReplicationTableStatisticsResponseTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    "EndpointTypeDef",
    "ExportMetadataModelAssessmentResponseTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "RdsRecommendationTypeDef",
    "StartRecommendationsRequestEntryTypeDef",
    "StartRecommendationsRequestRequestTypeDef",
    "ReloadReplicationTablesMessageRequestTypeDef",
    "ReloadTablesMessageRequestTypeDef",
    "ReplicationTypeDef",
    "ReplicationTaskAssessmentRunTypeDef",
    "ReplicationTaskTypeDef",
    "SchemaResponseTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "DescribeFleetAdvisorCollectorsResponseTypeDef",
    "CreateReplicationConfigResponseTypeDef",
    "DeleteReplicationConfigResponseTypeDef",
    "DescribeReplicationConfigsResponseTypeDef",
    "ModifyReplicationConfigResponseTypeDef",
    "ModifyDataMigrationMessageRequestTypeDef",
    "SourceDataSettingUnionTypeDef",
    "CreateDataMigrationResponseTypeDef",
    "DeleteDataMigrationResponseTypeDef",
    "DescribeDataMigrationsResponseTypeDef",
    "ModifyDataMigrationResponseTypeDef",
    "StartDataMigrationResponseTypeDef",
    "StopDataMigrationResponseTypeDef",
    "CreateMigrationProjectResponseTypeDef",
    "DeleteMigrationProjectResponseTypeDef",
    "DescribeMigrationProjectsResponseTypeDef",
    "ModifyMigrationProjectResponseTypeDef",
    "CreateDataProviderMessageRequestTypeDef",
    "DataProviderTypeDef",
    "ModifyDataProviderMessageRequestTypeDef",
    "DescribeFleetAdvisorDatabasesResponseTypeDef",
    "SchemaConversionRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "ModifyEndpointResponseTypeDef",
    "ApplyPendingMaintenanceActionResponseTypeDef",
    "DescribePendingMaintenanceActionsResponseTypeDef",
    "RecommendationDataTypeDef",
    "BatchStartRecommendationsRequestRequestTypeDef",
    "DescribeReplicationsResponseTypeDef",
    "StartReplicationResponseTypeDef",
    "StopReplicationResponseTypeDef",
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    "CreateReplicationTaskResponseTypeDef",
    "DeleteReplicationTaskResponseTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "ModifyReplicationTaskResponseTypeDef",
    "MoveReplicationTaskResponseTypeDef",
    "StartReplicationTaskAssessmentResponseTypeDef",
    "StartReplicationTaskResponseTypeDef",
    "StopReplicationTaskResponseTypeDef",
    "DescribeFleetAdvisorSchemasResponseTypeDef",
    "CreateReplicationSubnetGroupResponseTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "ModifyReplicationSubnetGroupResponseTypeDef",
    "ReplicationInstanceTypeDef",
    "CreateDataMigrationMessageRequestTypeDef",
    "CreateDataProviderResponseTypeDef",
    "DeleteDataProviderResponseTypeDef",
    "DescribeDataProvidersResponseTypeDef",
    "ModifyDataProviderResponseTypeDef",
    "DescribeExtensionPackAssociationsResponseTypeDef",
    "DescribeMetadataModelAssessmentsResponseTypeDef",
    "DescribeMetadataModelConversionsResponseTypeDef",
    "DescribeMetadataModelExportsAsScriptResponseTypeDef",
    "DescribeMetadataModelExportsToTargetResponseTypeDef",
    "DescribeMetadataModelImportsResponseTypeDef",
    "RecommendationTypeDef",
    "CreateReplicationInstanceResponseTypeDef",
    "DeleteReplicationInstanceResponseTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "ModifyReplicationInstanceResponseTypeDef",
    "RebootReplicationInstanceResponseTypeDef",
    "DescribeRecommendationsResponseTypeDef",
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": NotRequired[str],
        "Used": NotRequired[int],
        "Max": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)
ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ApplyAction": str,
        "OptInType": str,
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
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
BatchStartRecommendationsErrorEntryTypeDef = TypedDict(
    "BatchStartRecommendationsErrorEntryTypeDef",
    {
        "DatabaseId": NotRequired[str],
        "Message": NotRequired[str],
        "Code": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "CertificateCreationDate": NotRequired[datetime],
        "CertificatePem": NotRequired[str],
        "CertificateWallet": NotRequired[bytes],
        "CertificateArn": NotRequired[str],
        "CertificateOwner": NotRequired[str],
        "ValidFromDate": NotRequired[datetime],
        "ValidToDate": NotRequired[datetime],
        "SigningAlgorithm": NotRequired[str],
        "KeyLength": NotRequired[int],
    },
)
CollectorHealthCheckTypeDef = TypedDict(
    "CollectorHealthCheckTypeDef",
    {
        "CollectorStatus": NotRequired[CollectorStatusType],
        "LocalCollectorS3Access": NotRequired[bool],
        "WebCollectorS3Access": NotRequired[bool],
        "WebCollectorGrantedRoleBasedAccess": NotRequired[bool],
    },
)
InventoryDataTypeDef = TypedDict(
    "InventoryDataTypeDef",
    {
        "NumberOfDatabases": NotRequired[int],
        "NumberOfSchemas": NotRequired[int],
    },
)
CollectorShortInfoResponseTypeDef = TypedDict(
    "CollectorShortInfoResponseTypeDef",
    {
        "CollectorReferencedId": NotRequired[str],
        "CollectorName": NotRequired[str],
    },
)
ComputeConfigOutputTypeDef = TypedDict(
    "ComputeConfigOutputTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "DnsNameServers": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "MaxCapacityUnits": NotRequired[int],
        "MinCapacityUnits": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReplicationSubnetGroupId": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[List[str]],
    },
)
ComputeConfigTypeDef = TypedDict(
    "ComputeConfigTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "DnsNameServers": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "MaxCapacityUnits": NotRequired[int],
        "MinCapacityUnits": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReplicationSubnetGroupId": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ReplicationInstanceArn": NotRequired[str],
        "EndpointArn": NotRequired[str],
        "Status": NotRequired[str],
        "LastFailureMessage": NotRequired[str],
        "EndpointIdentifier": NotRequired[str],
        "ReplicationInstanceIdentifier": NotRequired[str],
    },
)
DmsTransferSettingsTypeDef = TypedDict(
    "DmsTransferSettingsTypeDef",
    {
        "ServiceAccessRoleArn": NotRequired[str],
        "BucketName": NotRequired[str],
    },
)
DocDbSettingsTypeDef = TypedDict(
    "DocDbSettingsTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "NestingLevel": NotRequired[NestingLevelValueType],
        "ExtractDocId": NotRequired[bool],
        "DocsToInvestigate": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "UseUpdateLookUp": NotRequired[bool],
        "ReplicateShardCollections": NotRequired[bool],
    },
)
DynamoDbSettingsTypeDef = TypedDict(
    "DynamoDbSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
    },
)
ElasticsearchSettingsTypeDef = TypedDict(
    "ElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": NotRequired[int],
        "ErrorRetryDuration": NotRequired[int],
        "UseNewMappingType": NotRequired[bool],
    },
)
GcpMySQLSettingsTypeDef = TypedDict(
    "GcpMySQLSettingsTypeDef",
    {
        "AfterConnectScript": NotRequired[str],
        "CleanSourceMetadataOnMismatch": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "EventsPollInterval": NotRequired[int],
        "TargetDbType": NotRequired[TargetDbTypeType],
        "MaxFileSize": NotRequired[int],
        "ParallelLoadThreads": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "ServerTimezone": NotRequired[str],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)
IBMDb2SettingsTypeDef = TypedDict(
    "IBMDb2SettingsTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "SetDataCaptureChanges": NotRequired[bool],
        "CurrentLsn": NotRequired[str],
        "MaxKBytesPerRead": NotRequired[int],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "LoadTimeout": NotRequired[int],
        "WriteBufferSize": NotRequired[int],
        "MaxFileSize": NotRequired[int],
        "KeepCsvFiles": NotRequired[bool],
    },
)
KafkaSettingsTypeDef = TypedDict(
    "KafkaSettingsTypeDef",
    {
        "Broker": NotRequired[str],
        "Topic": NotRequired[str],
        "MessageFormat": NotRequired[MessageFormatValueType],
        "IncludeTransactionDetails": NotRequired[bool],
        "IncludePartitionValue": NotRequired[bool],
        "PartitionIncludeSchemaTable": NotRequired[bool],
        "IncludeTableAlterOperations": NotRequired[bool],
        "IncludeControlDetails": NotRequired[bool],
        "MessageMaxBytes": NotRequired[int],
        "IncludeNullAndEmpty": NotRequired[bool],
        "SecurityProtocol": NotRequired[KafkaSecurityProtocolType],
        "SslClientCertificateArn": NotRequired[str],
        "SslClientKeyArn": NotRequired[str],
        "SslClientKeyPassword": NotRequired[str],
        "SslCaCertificateArn": NotRequired[str],
        "SaslUsername": NotRequired[str],
        "SaslPassword": NotRequired[str],
        "NoHexPrefix": NotRequired[bool],
        "SaslMechanism": NotRequired[KafkaSaslMechanismType],
        "SslEndpointIdentificationAlgorithm": NotRequired[
            KafkaSslEndpointIdentificationAlgorithmType
        ],
    },
)
KinesisSettingsTypeDef = TypedDict(
    "KinesisSettingsTypeDef",
    {
        "StreamArn": NotRequired[str],
        "MessageFormat": NotRequired[MessageFormatValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "IncludeTransactionDetails": NotRequired[bool],
        "IncludePartitionValue": NotRequired[bool],
        "PartitionIncludeSchemaTable": NotRequired[bool],
        "IncludeTableAlterOperations": NotRequired[bool],
        "IncludeControlDetails": NotRequired[bool],
        "IncludeNullAndEmpty": NotRequired[bool],
        "NoHexPrefix": NotRequired[bool],
    },
)
MicrosoftSQLServerSettingsTypeDef = TypedDict(
    "MicrosoftSQLServerSettingsTypeDef",
    {
        "Port": NotRequired[int],
        "BcpPacketSize": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ControlTablesFileGroup": NotRequired[str],
        "Password": NotRequired[str],
        "QuerySingleAlwaysOnNode": NotRequired[bool],
        "ReadBackupOnly": NotRequired[bool],
        "SafeguardPolicy": NotRequired[SafeguardPolicyType],
        "ServerName": NotRequired[str],
        "Username": NotRequired[str],
        "UseBcpFullLoad": NotRequired[bool],
        "UseThirdPartyBackupDevice": NotRequired[bool],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "TrimSpaceInChar": NotRequired[bool],
        "TlogAccessMode": NotRequired[TlogAccessModeType],
        "ForceLobLookup": NotRequired[bool],
    },
)
MongoDbSettingsTypeDef = TypedDict(
    "MongoDbSettingsTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "AuthType": NotRequired[AuthTypeValueType],
        "AuthMechanism": NotRequired[AuthMechanismValueType],
        "NestingLevel": NotRequired[NestingLevelValueType],
        "ExtractDocId": NotRequired[str],
        "DocsToInvestigate": NotRequired[str],
        "AuthSource": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "UseUpdateLookUp": NotRequired[bool],
        "ReplicateShardCollections": NotRequired[bool],
    },
)
MySQLSettingsTypeDef = TypedDict(
    "MySQLSettingsTypeDef",
    {
        "AfterConnectScript": NotRequired[str],
        "CleanSourceMetadataOnMismatch": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "EventsPollInterval": NotRequired[int],
        "TargetDbType": NotRequired[TargetDbTypeType],
        "MaxFileSize": NotRequired[int],
        "ParallelLoadThreads": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "ServerTimezone": NotRequired[str],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "ExecuteTimeout": NotRequired[int],
    },
)
NeptuneSettingsTypeDef = TypedDict(
    "NeptuneSettingsTypeDef",
    {
        "S3BucketName": str,
        "S3BucketFolder": str,
        "ServiceAccessRoleArn": NotRequired[str],
        "ErrorRetryDuration": NotRequired[int],
        "MaxFileSize": NotRequired[int],
        "MaxRetryCount": NotRequired[int],
        "IamAuthEnabled": NotRequired[bool],
    },
)
OracleSettingsTypeDef = TypedDict(
    "OracleSettingsTypeDef",
    {
        "AddSupplementalLogging": NotRequired[bool],
        "ArchivedLogDestId": NotRequired[int],
        "AdditionalArchivedLogDestId": NotRequired[int],
        "ExtraArchivedLogDestIds": NotRequired[Sequence[int]],
        "AllowSelectNestedTables": NotRequired[bool],
        "ParallelAsmReadThreads": NotRequired[int],
        "ReadAheadBlocks": NotRequired[int],
        "AccessAlternateDirectly": NotRequired[bool],
        "UseAlternateFolderForOnline": NotRequired[bool],
        "OraclePathPrefix": NotRequired[str],
        "UsePathPrefix": NotRequired[str],
        "ReplacePathPrefix": NotRequired[bool],
        "EnableHomogenousTablespace": NotRequired[bool],
        "DirectPathNoLog": NotRequired[bool],
        "ArchivedLogsOnly": NotRequired[bool],
        "AsmPassword": NotRequired[str],
        "AsmServer": NotRequired[str],
        "AsmUser": NotRequired[str],
        "CharLengthSemantics": NotRequired[CharLengthSemanticsType],
        "DatabaseName": NotRequired[str],
        "DirectPathParallelLoad": NotRequired[bool],
        "FailTasksOnLobTruncation": NotRequired[bool],
        "NumberDatatypeScale": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ReadTableSpaceName": NotRequired[bool],
        "RetryInterval": NotRequired[int],
        "SecurityDbEncryption": NotRequired[str],
        "SecurityDbEncryptionName": NotRequired[str],
        "ServerName": NotRequired[str],
        "SpatialDataOptionToGeoJsonFunctionName": NotRequired[str],
        "StandbyDelayTime": NotRequired[int],
        "Username": NotRequired[str],
        "UseBFile": NotRequired[bool],
        "UseDirectPathFullLoad": NotRequired[bool],
        "UseLogminerReader": NotRequired[bool],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "SecretsManagerOracleAsmAccessRoleArn": NotRequired[str],
        "SecretsManagerOracleAsmSecretId": NotRequired[str],
        "TrimSpaceInChar": NotRequired[bool],
        "ConvertTimestampWithZoneToUTC": NotRequired[bool],
        "OpenTransactionWindow": NotRequired[int],
    },
)
PostgreSQLSettingsTypeDef = TypedDict(
    "PostgreSQLSettingsTypeDef",
    {
        "AfterConnectScript": NotRequired[str],
        "CaptureDdls": NotRequired[bool],
        "MaxFileSize": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "DdlArtifactsSchema": NotRequired[str],
        "ExecuteTimeout": NotRequired[int],
        "FailTasksOnLobTruncation": NotRequired[bool],
        "HeartbeatEnable": NotRequired[bool],
        "HeartbeatSchema": NotRequired[str],
        "HeartbeatFrequency": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "Username": NotRequired[str],
        "SlotName": NotRequired[str],
        "PluginName": NotRequired[PluginNameValueType],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "TrimSpaceInChar": NotRequired[bool],
        "MapBooleanAsBoolean": NotRequired[bool],
        "MapJsonbAsClob": NotRequired[bool],
        "MapLongVarcharAs": NotRequired[LongVarcharMappingTypeType],
        "DatabaseMode": NotRequired[DatabaseModeType],
        "BabelfishDatabaseName": NotRequired[str],
    },
)
RedisSettingsTypeDef = TypedDict(
    "RedisSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "SslSecurityProtocol": NotRequired[SslSecurityProtocolValueType],
        "AuthType": NotRequired[RedisAuthTypeValueType],
        "AuthUserName": NotRequired[str],
        "AuthPassword": NotRequired[str],
        "SslCaCertificateArn": NotRequired[str],
    },
)
RedshiftSettingsTypeDef = TypedDict(
    "RedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": NotRequired[bool],
        "AfterConnectScript": NotRequired[str],
        "BucketFolder": NotRequired[str],
        "BucketName": NotRequired[str],
        "CaseSensitiveNames": NotRequired[bool],
        "CompUpdate": NotRequired[bool],
        "ConnectionTimeout": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "DateFormat": NotRequired[str],
        "EmptyAsNull": NotRequired[bool],
        "EncryptionMode": NotRequired[EncryptionModeValueType],
        "ExplicitIds": NotRequired[bool],
        "FileTransferUploadStreams": NotRequired[int],
        "LoadTimeout": NotRequired[int],
        "MaxFileSize": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "RemoveQuotes": NotRequired[bool],
        "ReplaceInvalidChars": NotRequired[str],
        "ReplaceChars": NotRequired[str],
        "ServerName": NotRequired[str],
        "ServiceAccessRoleArn": NotRequired[str],
        "ServerSideEncryptionKmsKeyId": NotRequired[str],
        "TimeFormat": NotRequired[str],
        "TrimBlanks": NotRequired[bool],
        "TruncateColumns": NotRequired[bool],
        "Username": NotRequired[str],
        "WriteBufferSize": NotRequired[int],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "MapBooleanAsBoolean": NotRequired[bool],
    },
)
S3SettingsTypeDef = TypedDict(
    "S3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "CsvRowDelimiter": NotRequired[str],
        "CsvDelimiter": NotRequired[str],
        "BucketFolder": NotRequired[str],
        "BucketName": NotRequired[str],
        "CompressionType": NotRequired[CompressionTypeValueType],
        "EncryptionMode": NotRequired[EncryptionModeValueType],
        "ServerSideEncryptionKmsKeyId": NotRequired[str],
        "DataFormat": NotRequired[DataFormatValueType],
        "EncodingType": NotRequired[EncodingTypeValueType],
        "DictPageSizeLimit": NotRequired[int],
        "RowGroupLength": NotRequired[int],
        "DataPageSize": NotRequired[int],
        "ParquetVersion": NotRequired[ParquetVersionValueType],
        "EnableStatistics": NotRequired[bool],
        "IncludeOpForFullLoad": NotRequired[bool],
        "CdcInsertsOnly": NotRequired[bool],
        "TimestampColumnName": NotRequired[str],
        "ParquetTimestampInMillisecond": NotRequired[bool],
        "CdcInsertsAndUpdates": NotRequired[bool],
        "DatePartitionEnabled": NotRequired[bool],
        "DatePartitionSequence": NotRequired[DatePartitionSequenceValueType],
        "DatePartitionDelimiter": NotRequired[DatePartitionDelimiterValueType],
        "UseCsvNoSupValue": NotRequired[bool],
        "CsvNoSupValue": NotRequired[str],
        "PreserveTransactions": NotRequired[bool],
        "CdcPath": NotRequired[str],
        "UseTaskStartTimeForFullLoadTimestamp": NotRequired[bool],
        "CannedAclForObjects": NotRequired[CannedAclForObjectsValueType],
        "AddColumnName": NotRequired[bool],
        "CdcMaxBatchInterval": NotRequired[int],
        "CdcMinFileSize": NotRequired[int],
        "CsvNullValue": NotRequired[str],
        "IgnoreHeaderRows": NotRequired[int],
        "MaxFileSize": NotRequired[int],
        "Rfc4180": NotRequired[bool],
        "DatePartitionTimezone": NotRequired[str],
        "AddTrailingPaddingCharacter": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
        "GlueCatalogGeneration": NotRequired[bool],
    },
)
SybaseSettingsTypeDef = TypedDict(
    "SybaseSettingsTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)
TimestreamSettingsTypeDef = TypedDict(
    "TimestreamSettingsTypeDef",
    {
        "DatabaseName": str,
        "MemoryDuration": int,
        "MagneticDuration": int,
        "CdcInsertsAndUpdates": NotRequired[bool],
        "EnableMagneticStoreWrites": NotRequired[bool],
    },
)
EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": NotRequired[str],
        "CustSubscriptionId": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
        "SourceType": NotRequired[str],
        "SourceIdsList": NotRequired[List[str]],
        "EventCategoriesList": NotRequired[List[str]],
        "Enabled": NotRequired[bool],
    },
)
CreateFleetAdvisorCollectorRequestRequestTypeDef = TypedDict(
    "CreateFleetAdvisorCollectorRequestRequestTypeDef",
    {
        "CollectorName": str,
        "ServiceAccessRoleArn": str,
        "S3BucketName": str,
        "Description": NotRequired[str],
    },
)
InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "InstanceProfileArn": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "NetworkType": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Description": NotRequired[str],
        "InstanceProfileCreationTime": NotRequired[datetime],
        "SubnetGroupIdentifier": NotRequired[str],
        "VpcSecurityGroups": NotRequired[List[str]],
    },
)
DataProviderDescriptorDefinitionTypeDef = TypedDict(
    "DataProviderDescriptorDefinitionTypeDef",
    {
        "DataProviderIdentifier": str,
        "SecretsManagerSecretId": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
    },
)
SCApplicationAttributesTypeDef = TypedDict(
    "SCApplicationAttributesTypeDef",
    {
        "S3BucketPath": NotRequired[str],
        "S3BucketRoleArn": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
DataMigrationSettingsTypeDef = TypedDict(
    "DataMigrationSettingsTypeDef",
    {
        "NumberOfJobs": NotRequired[int],
        "CloudwatchLogsEnabled": NotRequired[bool],
        "SelectionRules": NotRequired[str],
    },
)
DataMigrationStatisticsTypeDef = TypedDict(
    "DataMigrationStatisticsTypeDef",
    {
        "TablesLoaded": NotRequired[int],
        "ElapsedTimeMillis": NotRequired[int],
        "TablesLoading": NotRequired[int],
        "FullLoadPercentage": NotRequired[int],
        "CDCLatency": NotRequired[int],
        "TablesQueued": NotRequired[int],
        "TablesErrored": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "StopTime": NotRequired[datetime],
    },
)
SourceDataSettingOutputTypeDef = TypedDict(
    "SourceDataSettingOutputTypeDef",
    {
        "CDCStartPosition": NotRequired[str],
        "CDCStartTime": NotRequired[datetime],
        "CDCStopTime": NotRequired[datetime],
        "SlotName": NotRequired[str],
    },
)
DataProviderDescriptorTypeDef = TypedDict(
    "DataProviderDescriptorTypeDef",
    {
        "SecretsManagerSecretId": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "DataProviderName": NotRequired[str],
        "DataProviderArn": NotRequired[str],
    },
)
DocDbDataProviderSettingsTypeDef = TypedDict(
    "DocDbDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "CertificateArn": NotRequired[str],
    },
)
MariaDbDataProviderSettingsTypeDef = TypedDict(
    "MariaDbDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "SslMode": NotRequired[DmsSslModeValueType],
        "CertificateArn": NotRequired[str],
    },
)
MicrosoftSqlServerDataProviderSettingsTypeDef = TypedDict(
    "MicrosoftSqlServerDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "CertificateArn": NotRequired[str],
    },
)
MongoDbDataProviderSettingsTypeDef = TypedDict(
    "MongoDbDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "CertificateArn": NotRequired[str],
        "AuthType": NotRequired[AuthTypeValueType],
        "AuthSource": NotRequired[str],
        "AuthMechanism": NotRequired[AuthMechanismValueType],
    },
)
MySqlDataProviderSettingsTypeDef = TypedDict(
    "MySqlDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "SslMode": NotRequired[DmsSslModeValueType],
        "CertificateArn": NotRequired[str],
    },
)
OracleDataProviderSettingsTypeDef = TypedDict(
    "OracleDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "CertificateArn": NotRequired[str],
        "AsmServer": NotRequired[str],
        "SecretsManagerOracleAsmSecretId": NotRequired[str],
        "SecretsManagerOracleAsmAccessRoleArn": NotRequired[str],
        "SecretsManagerSecurityDbEncryptionSecretId": NotRequired[str],
        "SecretsManagerSecurityDbEncryptionAccessRoleArn": NotRequired[str],
    },
)
PostgreSqlDataProviderSettingsTypeDef = TypedDict(
    "PostgreSqlDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "CertificateArn": NotRequired[str],
    },
)
RedshiftDataProviderSettingsTypeDef = TypedDict(
    "RedshiftDataProviderSettingsTypeDef",
    {
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
    },
)
DatabaseInstanceSoftwareDetailsResponseTypeDef = TypedDict(
    "DatabaseInstanceSoftwareDetailsResponseTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EngineEdition": NotRequired[str],
        "ServicePack": NotRequired[str],
        "SupportLevel": NotRequired[str],
        "OsArchitecture": NotRequired[int],
        "Tooltip": NotRequired[str],
    },
)
ServerShortInfoResponseTypeDef = TypedDict(
    "ServerShortInfoResponseTypeDef",
    {
        "ServerId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "ServerName": NotRequired[str],
    },
)
DatabaseShortInfoResponseTypeDef = TypedDict(
    "DatabaseShortInfoResponseTypeDef",
    {
        "DatabaseId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DatabaseIpAddress": NotRequired[str],
        "DatabaseEngine": NotRequired[str],
    },
)
DefaultErrorDetailsTypeDef = TypedDict(
    "DefaultErrorDetailsTypeDef",
    {
        "Message": NotRequired[str],
    },
)
DeleteCertificateMessageRequestTypeDef = TypedDict(
    "DeleteCertificateMessageRequestTypeDef",
    {
        "CertificateArn": str,
    },
)
DeleteCollectorRequestRequestTypeDef = TypedDict(
    "DeleteCollectorRequestRequestTypeDef",
    {
        "CollectorReferencedId": str,
    },
)
DeleteConnectionMessageRequestTypeDef = TypedDict(
    "DeleteConnectionMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)
DeleteDataMigrationMessageRequestTypeDef = TypedDict(
    "DeleteDataMigrationMessageRequestTypeDef",
    {
        "DataMigrationIdentifier": str,
    },
)
DeleteDataProviderMessageRequestTypeDef = TypedDict(
    "DeleteDataProviderMessageRequestTypeDef",
    {
        "DataProviderIdentifier": str,
    },
)
DeleteEndpointMessageRequestTypeDef = TypedDict(
    "DeleteEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)
DeleteFleetAdvisorDatabasesRequestRequestTypeDef = TypedDict(
    "DeleteFleetAdvisorDatabasesRequestRequestTypeDef",
    {
        "DatabaseIds": Sequence[str],
    },
)
DeleteInstanceProfileMessageRequestTypeDef = TypedDict(
    "DeleteInstanceProfileMessageRequestTypeDef",
    {
        "InstanceProfileIdentifier": str,
    },
)
DeleteMigrationProjectMessageRequestTypeDef = TypedDict(
    "DeleteMigrationProjectMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
DeleteReplicationConfigMessageRequestTypeDef = TypedDict(
    "DeleteReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
    },
)
DeleteReplicationInstanceMessageRequestTypeDef = TypedDict(
    "DeleteReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
DeleteReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
    },
)
DeleteReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)
DeleteReplicationTaskMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
DescribeApplicableIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "SourceEngineName": NotRequired[str],
        "TargetEngineName": NotRequired[str],
        "MigrationType": NotRequired[MigrationTypeValueType],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
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
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeConversionConfigurationMessageRequestTypeDef = TypedDict(
    "DescribeConversionConfigurationMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
DescribeEndpointSettingsMessageRequestTypeDef = TypedDict(
    "DescribeEndpointSettingsMessageRequestTypeDef",
    {
        "EngineName": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
EndpointSettingTypeDef = TypedDict(
    "EndpointSettingTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[EndpointSettingTypeValueType],
        "EnumValues": NotRequired[List[str]],
        "Sensitive": NotRequired[bool],
        "Units": NotRequired[str],
        "Applicability": NotRequired[str],
        "IntValueMin": NotRequired[int],
        "IntValueMax": NotRequired[int],
        "DefaultValue": NotRequired[str],
    },
)
SupportedEndpointTypeTypeDef = TypedDict(
    "SupportedEndpointTypeTypeDef",
    {
        "EngineName": NotRequired[str],
        "SupportsCDC": NotRequired[bool],
        "EndpointType": NotRequired[ReplicationEndpointTypeValueType],
        "ReplicationInstanceEngineMinimumVersion": NotRequired[str],
        "EngineDisplayName": NotRequired[str],
    },
)
DescribeEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeEngineVersionsMessageRequestTypeDef",
    {
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "Version": NotRequired[str],
        "Lifecycle": NotRequired[str],
        "ReleaseStatus": NotRequired[ReleaseStatusValuesType],
        "LaunchDate": NotRequired[datetime],
        "AutoUpgradeDate": NotRequired[datetime],
        "DeprecationDate": NotRequired[datetime],
        "ForceUpgradeDate": NotRequired[datetime],
        "AvailableUpgrades": NotRequired[List[str]],
    },
)
EventCategoryGroupTypeDef = TypedDict(
    "EventCategoryGroupTypeDef",
    {
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[Literal["replication-instance"]],
        "Message": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
        "Date": NotRequired[datetime],
    },
)
DescribeFleetAdvisorLsaAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorLsaAnalysisRequestRequestTypeDef",
    {
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
FleetAdvisorLsaAnalysisResponseTypeDef = TypedDict(
    "FleetAdvisorLsaAnalysisResponseTypeDef",
    {
        "LsaAnalysisId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
FleetAdvisorSchemaObjectResponseTypeDef = TypedDict(
    "FleetAdvisorSchemaObjectResponseTypeDef",
    {
        "SchemaId": NotRequired[str],
        "ObjectType": NotRequired[str],
        "NumberOfObjects": NotRequired[int],
        "CodeLineCount": NotRequired[int],
        "CodeSize": NotRequired[int],
    },
)
DescribeOrderableReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    {
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
OrderableReplicationInstanceTypeDef = TypedDict(
    "OrderableReplicationInstanceTypeDef",
    {
        "EngineVersion": NotRequired[str],
        "ReplicationInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "MinAllocatedStorage": NotRequired[int],
        "MaxAllocatedStorage": NotRequired[int],
        "DefaultAllocatedStorage": NotRequired[int],
        "IncludedAllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[List[str]],
        "ReleaseStatus": NotRequired[ReleaseStatusValuesType],
    },
)
LimitationTypeDef = TypedDict(
    "LimitationTypeDef",
    {
        "DatabaseId": NotRequired[str],
        "EngineName": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Impact": NotRequired[str],
        "Type": NotRequired[str],
    },
)
DescribeRefreshSchemasStatusMessageRequestTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
RefreshSchemasStatusTypeDef = TypedDict(
    "RefreshSchemasStatusTypeDef",
    {
        "EndpointArn": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "Status": NotRequired[RefreshSchemasStatusTypeValueType],
        "LastRefreshDate": NotRequired[datetime],
        "LastFailureMessage": NotRequired[str],
    },
)
DescribeReplicationInstanceTaskLogsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ReplicationInstanceTaskLogTypeDef = TypedDict(
    "ReplicationInstanceTaskLogTypeDef",
    {
        "ReplicationTaskName": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationInstanceTaskLogSize": NotRequired[int],
    },
)
TableStatisticsTypeDef = TypedDict(
    "TableStatisticsTypeDef",
    {
        "SchemaName": NotRequired[str],
        "TableName": NotRequired[str],
        "Inserts": NotRequired[int],
        "Deletes": NotRequired[int],
        "Updates": NotRequired[int],
        "Ddls": NotRequired[int],
        "AppliedInserts": NotRequired[int],
        "AppliedDeletes": NotRequired[int],
        "AppliedUpdates": NotRequired[int],
        "AppliedDdls": NotRequired[int],
        "FullLoadRows": NotRequired[int],
        "FullLoadCondtnlChkFailedRows": NotRequired[int],
        "FullLoadErrorRows": NotRequired[int],
        "FullLoadStartTime": NotRequired[datetime],
        "FullLoadEndTime": NotRequired[datetime],
        "FullLoadReloaded": NotRequired[bool],
        "LastUpdateTime": NotRequired[datetime],
        "TableState": NotRequired[str],
        "ValidationPendingRecords": NotRequired[int],
        "ValidationFailedRecords": NotRequired[int],
        "ValidationSuspendedRecords": NotRequired[int],
        "ValidationState": NotRequired[str],
        "ValidationStateDetails": NotRequired[str],
    },
)
DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ReplicationTaskAssessmentResultTypeDef = TypedDict(
    "ReplicationTaskAssessmentResultTypeDef",
    {
        "ReplicationTaskIdentifier": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationTaskLastAssessmentDate": NotRequired[datetime],
        "AssessmentStatus": NotRequired[str],
        "AssessmentResultsFile": NotRequired[str],
        "AssessmentResults": NotRequired[str],
        "S3ObjectUrl": NotRequired[str],
    },
)
ReplicationTaskIndividualAssessmentTypeDef = TypedDict(
    "ReplicationTaskIndividualAssessmentTypeDef",
    {
        "ReplicationTaskIndividualAssessmentArn": NotRequired[str],
        "ReplicationTaskAssessmentRunArn": NotRequired[str],
        "IndividualAssessmentName": NotRequired[str],
        "Status": NotRequired[str],
        "ReplicationTaskIndividualAssessmentStartDate": NotRequired[datetime],
    },
)
DescribeSchemasMessageRequestTypeDef = TypedDict(
    "DescribeSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
OracleSettingsOutputTypeDef = TypedDict(
    "OracleSettingsOutputTypeDef",
    {
        "AddSupplementalLogging": NotRequired[bool],
        "ArchivedLogDestId": NotRequired[int],
        "AdditionalArchivedLogDestId": NotRequired[int],
        "ExtraArchivedLogDestIds": NotRequired[List[int]],
        "AllowSelectNestedTables": NotRequired[bool],
        "ParallelAsmReadThreads": NotRequired[int],
        "ReadAheadBlocks": NotRequired[int],
        "AccessAlternateDirectly": NotRequired[bool],
        "UseAlternateFolderForOnline": NotRequired[bool],
        "OraclePathPrefix": NotRequired[str],
        "UsePathPrefix": NotRequired[str],
        "ReplacePathPrefix": NotRequired[bool],
        "EnableHomogenousTablespace": NotRequired[bool],
        "DirectPathNoLog": NotRequired[bool],
        "ArchivedLogsOnly": NotRequired[bool],
        "AsmPassword": NotRequired[str],
        "AsmServer": NotRequired[str],
        "AsmUser": NotRequired[str],
        "CharLengthSemantics": NotRequired[CharLengthSemanticsType],
        "DatabaseName": NotRequired[str],
        "DirectPathParallelLoad": NotRequired[bool],
        "FailTasksOnLobTruncation": NotRequired[bool],
        "NumberDatatypeScale": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ReadTableSpaceName": NotRequired[bool],
        "RetryInterval": NotRequired[int],
        "SecurityDbEncryption": NotRequired[str],
        "SecurityDbEncryptionName": NotRequired[str],
        "ServerName": NotRequired[str],
        "SpatialDataOptionToGeoJsonFunctionName": NotRequired[str],
        "StandbyDelayTime": NotRequired[int],
        "Username": NotRequired[str],
        "UseBFile": NotRequired[bool],
        "UseDirectPathFullLoad": NotRequired[bool],
        "UseLogminerReader": NotRequired[bool],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "SecretsManagerOracleAsmAccessRoleArn": NotRequired[str],
        "SecretsManagerOracleAsmSecretId": NotRequired[str],
        "TrimSpaceInChar": NotRequired[bool],
        "ConvertTimestampWithZoneToUTC": NotRequired[bool],
        "OpenTransactionWindow": NotRequired[int],
    },
)
ExportMetadataModelAssessmentMessageRequestTypeDef = TypedDict(
    "ExportMetadataModelAssessmentMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
        "FileName": NotRequired[str],
        "AssessmentReportTypes": NotRequired[Sequence[AssessmentReportTypeType]],
    },
)
ExportMetadataModelAssessmentResultEntryTypeDef = TypedDict(
    "ExportMetadataModelAssessmentResultEntryTypeDef",
    {
        "S3ObjectKey": NotRequired[str],
        "ObjectURL": NotRequired[str],
    },
)
ExportSqlDetailsTypeDef = TypedDict(
    "ExportSqlDetailsTypeDef",
    {
        "S3ObjectKey": NotRequired[str],
        "ObjectURL": NotRequired[str],
    },
)
ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceArnList": NotRequired[Sequence[str]],
    },
)
ModifyConversionConfigurationMessageRequestTypeDef = TypedDict(
    "ModifyConversionConfigurationMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "ConversionConfiguration": str,
    },
)
ModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "ModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": NotRequired[str],
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)
ModifyInstanceProfileMessageRequestTypeDef = TypedDict(
    "ModifyInstanceProfileMessageRequestTypeDef",
    {
        "InstanceProfileIdentifier": str,
        "AvailabilityZone": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "NetworkType": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Description": NotRequired[str],
        "SubnetGroupIdentifier": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence[str]],
    },
)
ModifyReplicationInstanceMessageRequestTypeDef = TypedDict(
    "ModifyReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "AllocatedStorage": NotRequired[int],
        "ApplyImmediately": NotRequired[bool],
        "ReplicationInstanceClass": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReplicationInstanceIdentifier": NotRequired[str],
        "NetworkType": NotRequired[str],
    },
)
ModifyReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "SubnetIds": Sequence[str],
        "ReplicationSubnetGroupDescription": NotRequired[str],
    },
)
MoveReplicationTaskMessageRequestTypeDef = TypedDict(
    "MoveReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TargetReplicationInstanceArn": str,
    },
)
PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": NotRequired[str],
        "AutoAppliedAfterDate": NotRequired[datetime],
        "ForcedApplyDate": NotRequired[datetime],
        "OptInStatus": NotRequired[str],
        "CurrentApplyDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)
ProvisionDataTypeDef = TypedDict(
    "ProvisionDataTypeDef",
    {
        "ProvisionState": NotRequired[str],
        "ProvisionedCapacityUnits": NotRequired[int],
        "DateProvisioned": NotRequired[datetime],
        "IsNewProvisioningAvailable": NotRequired[bool],
        "DateNewProvisioningDataAvailable": NotRequired[datetime],
        "ReasonForNewProvisioningData": NotRequired[str],
    },
)
RdsConfigurationTypeDef = TypedDict(
    "RdsConfigurationTypeDef",
    {
        "EngineEdition": NotRequired[str],
        "InstanceType": NotRequired[str],
        "InstanceVcpu": NotRequired[float],
        "InstanceMemory": NotRequired[float],
        "StorageType": NotRequired[str],
        "StorageSize": NotRequired[int],
        "StorageIops": NotRequired[int],
        "DeploymentOption": NotRequired[str],
        "EngineVersion": NotRequired[str],
    },
)
RdsRequirementsTypeDef = TypedDict(
    "RdsRequirementsTypeDef",
    {
        "EngineEdition": NotRequired[str],
        "InstanceVcpu": NotRequired[float],
        "InstanceMemory": NotRequired[float],
        "StorageSize": NotRequired[int],
        "StorageIops": NotRequired[int],
        "DeploymentOption": NotRequired[str],
        "EngineVersion": NotRequired[str],
    },
)
RebootReplicationInstanceMessageRequestTypeDef = TypedDict(
    "RebootReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ForceFailover": NotRequired[bool],
        "ForcePlannedFailover": NotRequired[bool],
    },
)
RecommendationSettingsTypeDef = TypedDict(
    "RecommendationSettingsTypeDef",
    {
        "InstanceSizingType": str,
        "WorkloadType": str,
    },
)
RefreshSchemasMessageRequestTypeDef = TypedDict(
    "RefreshSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)
TableToReloadTypeDef = TypedDict(
    "TableToReloadTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
    },
)
RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
ReplicationPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "NetworkType": NotRequired[str],
    },
)
VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
ReplicationStatsTypeDef = TypedDict(
    "ReplicationStatsTypeDef",
    {
        "FullLoadProgressPercent": NotRequired[int],
        "ElapsedTimeMillis": NotRequired[int],
        "TablesLoaded": NotRequired[int],
        "TablesLoading": NotRequired[int],
        "TablesQueued": NotRequired[int],
        "TablesErrored": NotRequired[int],
        "FreshStartDate": NotRequired[datetime],
        "StartDate": NotRequired[datetime],
        "StopDate": NotRequired[datetime],
        "FullLoadStartDate": NotRequired[datetime],
        "FullLoadFinishDate": NotRequired[datetime],
    },
)
ReplicationTaskAssessmentRunProgressTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunProgressTypeDef",
    {
        "IndividualAssessmentCount": NotRequired[int],
        "IndividualAssessmentCompletedCount": NotRequired[int],
    },
)
ReplicationTaskAssessmentRunResultStatisticTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunResultStatisticTypeDef",
    {
        "Passed": NotRequired[int],
        "Failed": NotRequired[int],
        "Error": NotRequired[int],
        "Warning": NotRequired[int],
        "Cancelled": NotRequired[int],
    },
)
ReplicationTaskStatsTypeDef = TypedDict(
    "ReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": NotRequired[int],
        "ElapsedTimeMillis": NotRequired[int],
        "TablesLoaded": NotRequired[int],
        "TablesLoading": NotRequired[int],
        "TablesQueued": NotRequired[int],
        "TablesErrored": NotRequired[int],
        "FreshStartDate": NotRequired[datetime],
        "StartDate": NotRequired[datetime],
        "StopDate": NotRequired[datetime],
        "FullLoadStartDate": NotRequired[datetime],
        "FullLoadFinishDate": NotRequired[datetime],
    },
)
SchemaShortInfoResponseTypeDef = TypedDict(
    "SchemaShortInfoResponseTypeDef",
    {
        "SchemaId": NotRequired[str],
        "SchemaName": NotRequired[str],
        "DatabaseId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DatabaseIpAddress": NotRequired[str],
    },
)
StartDataMigrationMessageRequestTypeDef = TypedDict(
    "StartDataMigrationMessageRequestTypeDef",
    {
        "DataMigrationIdentifier": str,
        "StartType": StartReplicationMigrationTypeValueType,
    },
)
StartExtensionPackAssociationMessageRequestTypeDef = TypedDict(
    "StartExtensionPackAssociationMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
StartMetadataModelAssessmentMessageRequestTypeDef = TypedDict(
    "StartMetadataModelAssessmentMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
    },
)
StartMetadataModelConversionMessageRequestTypeDef = TypedDict(
    "StartMetadataModelConversionMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
    },
)
StartMetadataModelExportAsScriptMessageRequestTypeDef = TypedDict(
    "StartMetadataModelExportAsScriptMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
        "Origin": OriginTypeValueType,
        "FileName": NotRequired[str],
    },
)
StartMetadataModelExportToTargetMessageRequestTypeDef = TypedDict(
    "StartMetadataModelExportToTargetMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
        "OverwriteExtensionPack": NotRequired[bool],
    },
)
StartMetadataModelImportMessageRequestTypeDef = TypedDict(
    "StartMetadataModelImportMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
        "Origin": OriginTypeValueType,
        "Refresh": NotRequired[bool],
    },
)
StartReplicationTaskAssessmentMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
StopDataMigrationMessageRequestTypeDef = TypedDict(
    "StopDataMigrationMessageRequestTypeDef",
    {
        "DataMigrationIdentifier": str,
    },
)
StopReplicationMessageRequestTypeDef = TypedDict(
    "StopReplicationMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
    },
)
StopReplicationTaskMessageRequestTypeDef = TypedDict(
    "StopReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
TestConnectionMessageRequestTypeDef = TypedDict(
    "TestConnectionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
    },
)
UpdateSubscriptionsToEventBridgeMessageRequestTypeDef = TypedDict(
    "UpdateSubscriptionsToEventBridgeMessageRequestTypeDef",
    {
        "ForceMove": NotRequired[bool],
    },
)
AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "CreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "SourceIds": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateInstanceProfileMessageRequestTypeDef = TypedDict(
    "CreateInstanceProfileMessageRequestTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "NetworkType": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Description": NotRequired[str],
        "SubnetGroupIdentifier": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence[str]],
    },
)
CreateReplicationInstanceMessageRequestTypeDef = TypedDict(
    "CreateReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "AllocatedStorage": NotRequired[int],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "AvailabilityZone": NotRequired[str],
        "ReplicationSubnetGroupIdentifier": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "KmsKeyId": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "DnsNameServers": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
        "NetworkType": NotRequired[str],
    },
)
CreateReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "AssessmentRunName": str,
        "ResultLocationFolder": NotRequired[str],
        "ResultEncryptionMode": NotRequired[str],
        "ResultKmsKeyArn": NotRequired[str],
        "IncludeOnly": NotRequired[Sequence[str]],
        "Exclude": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateFleetAdvisorCollectorResponseTypeDef = TypedDict(
    "CreateFleetAdvisorCollectorResponseTypeDef",
    {
        "CollectorReferencedId": str,
        "CollectorName": str,
        "Description": str,
        "ServiceAccessRoleArn": str,
        "S3BucketName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFleetAdvisorDatabasesResponseTypeDef = TypedDict(
    "DeleteFleetAdvisorDatabasesResponseTypeDef",
    {
        "DatabaseIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List[AccountQuotaTypeDef],
        "UniqueAccountIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeApplicableIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    {
        "IndividualAssessmentNames": List[str],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConversionConfigurationResponseTypeDef = TypedDict(
    "DescribeConversionConfigurationResponseTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "ConversionConfiguration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSchemasResponseTypeDef = TypedDict(
    "DescribeSchemasResponseTypeDef",
    {
        "Marker": str,
        "Schemas": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyConversionConfigurationResponseTypeDef = TypedDict(
    "ModifyConversionConfigurationResponseTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReloadReplicationTablesResponseTypeDef = TypedDict(
    "ReloadReplicationTablesResponseTypeDef",
    {
        "ReplicationConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReloadTablesResponseTypeDef = TypedDict(
    "ReloadTablesResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunFleetAdvisorLsaAnalysisResponseTypeDef = TypedDict(
    "RunFleetAdvisorLsaAnalysisResponseTypeDef",
    {
        "LsaAnalysisId": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExtensionPackAssociationResponseTypeDef = TypedDict(
    "StartExtensionPackAssociationResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMetadataModelAssessmentResponseTypeDef = TypedDict(
    "StartMetadataModelAssessmentResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMetadataModelConversionResponseTypeDef = TypedDict(
    "StartMetadataModelConversionResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMetadataModelExportAsScriptResponseTypeDef = TypedDict(
    "StartMetadataModelExportAsScriptResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMetadataModelExportToTargetResponseTypeDef = TypedDict(
    "StartMetadataModelExportToTargetResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMetadataModelImportResponseTypeDef = TypedDict(
    "StartMetadataModelImportResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSubscriptionsToEventBridgeResponseTypeDef = TypedDict(
    "UpdateSubscriptionsToEventBridgeResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[AvailabilityZoneTypeDef],
        "SubnetStatus": NotRequired[str],
    },
)
BatchStartRecommendationsResponseTypeDef = TypedDict(
    "BatchStartRecommendationsResponseTypeDef",
    {
        "ErrorEntries": List[BatchStartRecommendationsErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportCertificateMessageRequestTypeDef = TypedDict(
    "ImportCertificateMessageRequestTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificatePem": NotRequired[str],
        "CertificateWallet": NotRequired[BlobTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DeleteCertificateResponseTypeDef = TypedDict(
    "DeleteCertificateResponseTypeDef",
    {
        "Certificate": CertificateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCertificatesResponseTypeDef = TypedDict(
    "DescribeCertificatesResponseTypeDef",
    {
        "Marker": str,
        "Certificates": List[CertificateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "Certificate": CertificateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CollectorResponseTypeDef = TypedDict(
    "CollectorResponseTypeDef",
    {
        "CollectorReferencedId": NotRequired[str],
        "CollectorName": NotRequired[str],
        "CollectorVersion": NotRequired[str],
        "VersionStatus": NotRequired[VersionStatusType],
        "Description": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "ServiceAccessRoleArn": NotRequired[str],
        "CollectorHealthCheck": NotRequired[CollectorHealthCheckTypeDef],
        "LastDataReceived": NotRequired[str],
        "RegisteredDate": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "ModifiedDate": NotRequired[str],
        "InventoryData": NotRequired[InventoryDataTypeDef],
    },
)
ReplicationConfigTypeDef = TypedDict(
    "ReplicationConfigTypeDef",
    {
        "ReplicationConfigIdentifier": NotRequired[str],
        "ReplicationConfigArn": NotRequired[str],
        "SourceEndpointArn": NotRequired[str],
        "TargetEndpointArn": NotRequired[str],
        "ReplicationType": NotRequired[MigrationTypeValueType],
        "ComputeConfig": NotRequired[ComputeConfigOutputTypeDef],
        "ReplicationSettings": NotRequired[str],
        "SupplementalSettings": NotRequired[str],
        "TableMappings": NotRequired[str],
        "ReplicationConfigCreateTime": NotRequired[datetime],
        "ReplicationConfigUpdateTime": NotRequired[datetime],
    },
)
CreateReplicationConfigMessageRequestTypeDef = TypedDict(
    "CreateReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationConfigIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ComputeConfig": ComputeConfigTypeDef,
        "ReplicationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationSettings": NotRequired[str],
        "SupplementalSettings": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ModifyReplicationConfigMessageRequestTypeDef = TypedDict(
    "ModifyReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
        "ReplicationConfigIdentifier": NotRequired[str],
        "ReplicationType": NotRequired[MigrationTypeValueType],
        "TableMappings": NotRequired[str],
        "ReplicationSettings": NotRequired[str],
        "SupplementalSettings": NotRequired[str],
        "ComputeConfig": NotRequired[ComputeConfigTypeDef],
        "SourceEndpointArn": NotRequired[str],
        "TargetEndpointArn": NotRequired[str],
    },
)
DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConnectionsResponseTypeDef = TypedDict(
    "DescribeConnectionsResponseTypeDef",
    {
        "Marker": str,
        "Connections": List[ConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestConnectionResponseTypeDef = TypedDict(
    "TestConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEndpointMessageRequestTypeDef = TypedDict(
    "CreateEndpointMessageRequestTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "CertificateArn": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "DynamoDbSettings": NotRequired[DynamoDbSettingsTypeDef],
        "S3Settings": NotRequired[S3SettingsTypeDef],
        "DmsTransferSettings": NotRequired[DmsTransferSettingsTypeDef],
        "MongoDbSettings": NotRequired[MongoDbSettingsTypeDef],
        "KinesisSettings": NotRequired[KinesisSettingsTypeDef],
        "KafkaSettings": NotRequired[KafkaSettingsTypeDef],
        "ElasticsearchSettings": NotRequired[ElasticsearchSettingsTypeDef],
        "NeptuneSettings": NotRequired[NeptuneSettingsTypeDef],
        "RedshiftSettings": NotRequired[RedshiftSettingsTypeDef],
        "PostgreSQLSettings": NotRequired[PostgreSQLSettingsTypeDef],
        "MySQLSettings": NotRequired[MySQLSettingsTypeDef],
        "OracleSettings": NotRequired[OracleSettingsTypeDef],
        "SybaseSettings": NotRequired[SybaseSettingsTypeDef],
        "MicrosoftSQLServerSettings": NotRequired[MicrosoftSQLServerSettingsTypeDef],
        "IBMDb2Settings": NotRequired[IBMDb2SettingsTypeDef],
        "ResourceIdentifier": NotRequired[str],
        "DocDbSettings": NotRequired[DocDbSettingsTypeDef],
        "RedisSettings": NotRequired[RedisSettingsTypeDef],
        "GcpMySQLSettings": NotRequired[GcpMySQLSettingsTypeDef],
        "TimestreamSettings": NotRequired[TimestreamSettingsTypeDef],
    },
)
ModifyEndpointMessageRequestTypeDef = TypedDict(
    "ModifyEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "EndpointIdentifier": NotRequired[str],
        "EndpointType": NotRequired[ReplicationEndpointTypeValueType],
        "EngineName": NotRequired[str],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "DynamoDbSettings": NotRequired[DynamoDbSettingsTypeDef],
        "S3Settings": NotRequired[S3SettingsTypeDef],
        "DmsTransferSettings": NotRequired[DmsTransferSettingsTypeDef],
        "MongoDbSettings": NotRequired[MongoDbSettingsTypeDef],
        "KinesisSettings": NotRequired[KinesisSettingsTypeDef],
        "KafkaSettings": NotRequired[KafkaSettingsTypeDef],
        "ElasticsearchSettings": NotRequired[ElasticsearchSettingsTypeDef],
        "NeptuneSettings": NotRequired[NeptuneSettingsTypeDef],
        "RedshiftSettings": NotRequired[RedshiftSettingsTypeDef],
        "PostgreSQLSettings": NotRequired[PostgreSQLSettingsTypeDef],
        "MySQLSettings": NotRequired[MySQLSettingsTypeDef],
        "OracleSettings": NotRequired[OracleSettingsTypeDef],
        "SybaseSettings": NotRequired[SybaseSettingsTypeDef],
        "MicrosoftSQLServerSettings": NotRequired[MicrosoftSQLServerSettingsTypeDef],
        "IBMDb2Settings": NotRequired[IBMDb2SettingsTypeDef],
        "DocDbSettings": NotRequired[DocDbSettingsTypeDef],
        "RedisSettings": NotRequired[RedisSettingsTypeDef],
        "ExactSettings": NotRequired[bool],
        "GcpMySQLSettings": NotRequired[GcpMySQLSettingsTypeDef],
        "TimestreamSettings": NotRequired[TimestreamSettingsTypeDef],
    },
)
CreateEventSubscriptionResponseTypeDef = TypedDict(
    "CreateEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEventSubscriptionResponseTypeDef = TypedDict(
    "DeleteEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[EventSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ModifyEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceProfileResponseTypeDef = TypedDict(
    "CreateInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInstanceProfileResponseTypeDef = TypedDict(
    "DeleteInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceProfilesResponseTypeDef = TypedDict(
    "DescribeInstanceProfilesResponseTypeDef",
    {
        "Marker": str,
        "InstanceProfiles": List[InstanceProfileTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceProfileResponseTypeDef = TypedDict(
    "ModifyInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMigrationProjectMessageRequestTypeDef = TypedDict(
    "CreateMigrationProjectMessageRequestTypeDef",
    {
        "SourceDataProviderDescriptors": Sequence[DataProviderDescriptorDefinitionTypeDef],
        "TargetDataProviderDescriptors": Sequence[DataProviderDescriptorDefinitionTypeDef],
        "InstanceProfileIdentifier": str,
        "MigrationProjectName": NotRequired[str],
        "TransformationRules": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SchemaConversionApplicationAttributes": NotRequired[SCApplicationAttributesTypeDef],
    },
)
ModifyMigrationProjectMessageRequestTypeDef = TypedDict(
    "ModifyMigrationProjectMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "MigrationProjectName": NotRequired[str],
        "SourceDataProviderDescriptors": NotRequired[
            Sequence[DataProviderDescriptorDefinitionTypeDef]
        ],
        "TargetDataProviderDescriptors": NotRequired[
            Sequence[DataProviderDescriptorDefinitionTypeDef]
        ],
        "InstanceProfileIdentifier": NotRequired[str],
        "TransformationRules": NotRequired[str],
        "Description": NotRequired[str],
        "SchemaConversionApplicationAttributes": NotRequired[SCApplicationAttributesTypeDef],
    },
)
CreateReplicationTaskMessageRequestTypeDef = TypedDict(
    "CreateReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": NotRequired[str],
        "CdcStartTime": NotRequired[TimestampTypeDef],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TaskData": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
    },
)
ModifyReplicationTaskMessageRequestTypeDef = TypedDict(
    "ModifyReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ReplicationTaskIdentifier": NotRequired[str],
        "MigrationType": NotRequired[MigrationTypeValueType],
        "TableMappings": NotRequired[str],
        "ReplicationTaskSettings": NotRequired[str],
        "CdcStartTime": NotRequired[TimestampTypeDef],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "TaskData": NotRequired[str],
    },
)
SourceDataSettingTypeDef = TypedDict(
    "SourceDataSettingTypeDef",
    {
        "CDCStartPosition": NotRequired[str],
        "CDCStartTime": NotRequired[TimestampTypeDef],
        "CDCStopTime": NotRequired[TimestampTypeDef],
        "SlotName": NotRequired[str],
    },
)
StartReplicationMessageRequestTypeDef = TypedDict(
    "StartReplicationMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
        "StartReplicationType": str,
        "CdcStartTime": NotRequired[TimestampTypeDef],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
    },
)
StartReplicationTaskMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "StartReplicationTaskType": StartReplicationTaskTypeValueType,
        "CdcStartTime": NotRequired[TimestampTypeDef],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
    },
)
DataMigrationTypeDef = TypedDict(
    "DataMigrationTypeDef",
    {
        "DataMigrationName": NotRequired[str],
        "DataMigrationArn": NotRequired[str],
        "DataMigrationCreateTime": NotRequired[datetime],
        "DataMigrationStartTime": NotRequired[datetime],
        "DataMigrationEndTime": NotRequired[datetime],
        "ServiceAccessRoleArn": NotRequired[str],
        "MigrationProjectArn": NotRequired[str],
        "DataMigrationType": NotRequired[MigrationTypeValueType],
        "DataMigrationSettings": NotRequired[DataMigrationSettingsTypeDef],
        "SourceDataSettings": NotRequired[List[SourceDataSettingOutputTypeDef]],
        "DataMigrationStatistics": NotRequired[DataMigrationStatisticsTypeDef],
        "DataMigrationStatus": NotRequired[str],
        "PublicIpAddresses": NotRequired[List[str]],
        "DataMigrationCidrBlocks": NotRequired[List[str]],
        "LastFailureMessage": NotRequired[str],
        "StopReason": NotRequired[str],
    },
)
MigrationProjectTypeDef = TypedDict(
    "MigrationProjectTypeDef",
    {
        "MigrationProjectName": NotRequired[str],
        "MigrationProjectArn": NotRequired[str],
        "MigrationProjectCreationTime": NotRequired[datetime],
        "SourceDataProviderDescriptors": NotRequired[List[DataProviderDescriptorTypeDef]],
        "TargetDataProviderDescriptors": NotRequired[List[DataProviderDescriptorTypeDef]],
        "InstanceProfileArn": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "TransformationRules": NotRequired[str],
        "Description": NotRequired[str],
        "SchemaConversionApplicationAttributes": NotRequired[SCApplicationAttributesTypeDef],
    },
)
DataProviderSettingsTypeDef = TypedDict(
    "DataProviderSettingsTypeDef",
    {
        "RedshiftSettings": NotRequired[RedshiftDataProviderSettingsTypeDef],
        "PostgreSqlSettings": NotRequired[PostgreSqlDataProviderSettingsTypeDef],
        "MySqlSettings": NotRequired[MySqlDataProviderSettingsTypeDef],
        "OracleSettings": NotRequired[OracleDataProviderSettingsTypeDef],
        "MicrosoftSqlServerSettings": NotRequired[MicrosoftSqlServerDataProviderSettingsTypeDef],
        "DocDbSettings": NotRequired[DocDbDataProviderSettingsTypeDef],
        "MariaDbSettings": NotRequired[MariaDbDataProviderSettingsTypeDef],
        "MongoDbSettings": NotRequired[MongoDbDataProviderSettingsTypeDef],
    },
)
DatabaseResponseTypeDef = TypedDict(
    "DatabaseResponseTypeDef",
    {
        "DatabaseId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "IpAddress": NotRequired[str],
        "NumberOfSchemas": NotRequired[int],
        "Server": NotRequired[ServerShortInfoResponseTypeDef],
        "SoftwareDetails": NotRequired[DatabaseInstanceSoftwareDetailsResponseTypeDef],
        "Collectors": NotRequired[List[CollectorShortInfoResponseTypeDef]],
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "defaultErrorDetails": NotRequired[DefaultErrorDetailsTypeDef],
    },
)
DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeConnectionsMessageRequestTypeDef = TypedDict(
    "DescribeConnectionsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDataMigrationsMessageRequestTypeDef = TypedDict(
    "DescribeDataMigrationsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WithoutSettings": NotRequired[bool],
        "WithoutStatistics": NotRequired[bool],
    },
)
DescribeDataProvidersMessageRequestTypeDef = TypedDict(
    "DescribeDataProvidersMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEndpointTypesMessageRequestTypeDef = TypedDict(
    "DescribeEndpointTypesMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeEndpointsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[Literal["replication-instance"]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeExtensionPackAssociationsMessageRequestTypeDef = TypedDict(
    "DescribeExtensionPackAssociationsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeFleetAdvisorCollectorsRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorCollectorsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFleetAdvisorDatabasesRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorDatabasesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFleetAdvisorSchemaObjectSummaryRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemaObjectSummaryRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFleetAdvisorSchemasRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemasRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstanceProfilesMessageRequestTypeDef = TypedDict(
    "DescribeInstanceProfilesMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeMetadataModelAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeMetadataModelAssessmentsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeMetadataModelConversionsMessageRequestTypeDef = TypedDict(
    "DescribeMetadataModelConversionsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeMetadataModelExportsAsScriptMessageRequestTypeDef = TypedDict(
    "DescribeMetadataModelExportsAsScriptMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeMetadataModelExportsToTargetMessageRequestTypeDef = TypedDict(
    "DescribeMetadataModelExportsToTargetMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeMetadataModelImportsMessageRequestTypeDef = TypedDict(
    "DescribeMetadataModelImportsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeMigrationProjectsMessageRequestTypeDef = TypedDict(
    "DescribeMigrationProjectsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeRecommendationLimitationsRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationLimitationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeRecommendationsRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeReplicationConfigsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationConfigsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReplicationSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReplicationTableStatisticsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTableStatisticsMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReplicationTasksMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTasksMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WithoutSettings": NotRequired[bool],
    },
)
DescribeReplicationsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeTableStatisticsMessageRequestTypeDef = TypedDict(
    "DescribeTableStatisticsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef = TypedDict(
    "DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConnectionsMessageDescribeConnectionsPaginateTypeDef = TypedDict(
    "DescribeConnectionsMessageDescribeConnectionsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDataMigrationsMessageDescribeDataMigrationsPaginateTypeDef = TypedDict(
    "DescribeDataMigrationsMessageDescribeDataMigrationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "WithoutSettings": NotRequired[bool],
        "WithoutStatistics": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEndpointTypesMessageDescribeEndpointTypesPaginateTypeDef = TypedDict(
    "DescribeEndpointTypesMessageDescribeEndpointTypesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEndpointsMessageDescribeEndpointsPaginateTypeDef = TypedDict(
    "DescribeEndpointsMessageDescribeEndpointsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsMessageDescribeEventsPaginateTypeDef = TypedDict(
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[Literal["replication-instance"]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrderableReplicationInstancesMessageDescribeOrderableReplicationInstancesPaginateTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesMessageDescribeOrderableReplicationInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReplicationInstancesMessageDescribeReplicationInstancesPaginateTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageDescribeReplicationInstancesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReplicationSubnetGroupsMessageDescribeReplicationSubnetGroupsPaginateTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsMessageDescribeReplicationSubnetGroupsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReplicationTaskAssessmentResultsMessageDescribeReplicationTaskAssessmentResultsPaginateTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsMessageDescribeReplicationTaskAssessmentResultsPaginateTypeDef",
    {
        "ReplicationTaskArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReplicationTasksMessageDescribeReplicationTasksPaginateTypeDef = TypedDict(
    "DescribeReplicationTasksMessageDescribeReplicationTasksPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "WithoutSettings": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSchemasMessageDescribeSchemasPaginateTypeDef = TypedDict(
    "DescribeSchemasMessageDescribeSchemasPaginateTypeDef",
    {
        "EndpointArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTableStatisticsMessageDescribeTableStatisticsPaginateTypeDef = TypedDict(
    "DescribeTableStatisticsMessageDescribeTableStatisticsPaginateTypeDef",
    {
        "ReplicationTaskArn": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConnectionsMessageTestConnectionSucceedsWaitTypeDef = TypedDict(
    "DescribeConnectionsMessageTestConnectionSucceedsWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEndpointsMessageEndpointDeletedWaitTypeDef = TypedDict(
    "DescribeEndpointsMessageEndpointDeletedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationInstancesMessageReplicationInstanceAvailableWaitTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageReplicationInstanceAvailableWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationInstancesMessageReplicationInstanceDeletedWaitTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageReplicationInstanceDeletedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationTasksMessageReplicationTaskDeletedWaitTypeDef = TypedDict(
    "DescribeReplicationTasksMessageReplicationTaskDeletedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WithoutSettings": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationTasksMessageReplicationTaskReadyWaitTypeDef = TypedDict(
    "DescribeReplicationTasksMessageReplicationTaskReadyWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WithoutSettings": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationTasksMessageReplicationTaskRunningWaitTypeDef = TypedDict(
    "DescribeReplicationTasksMessageReplicationTaskRunningWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WithoutSettings": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationTasksMessageReplicationTaskStoppedWaitTypeDef = TypedDict(
    "DescribeReplicationTasksMessageReplicationTaskStoppedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WithoutSettings": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEndpointSettingsResponseTypeDef = TypedDict(
    "DescribeEndpointSettingsResponseTypeDef",
    {
        "Marker": str,
        "EndpointSettings": List[EndpointSettingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEndpointTypesResponseTypeDef = TypedDict(
    "DescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List[SupportedEndpointTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEngineVersionsResponseTypeDef = TypedDict(
    "DescribeEngineVersionsResponseTypeDef",
    {
        "EngineVersions": List[EngineVersionTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventCategoriesResponseTypeDef = TypedDict(
    "DescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List[EventCategoryGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "Marker": str,
        "Events": List[EventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetAdvisorLsaAnalysisResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorLsaAnalysisResponseTypeDef",
    {
        "Analysis": List[FleetAdvisorLsaAnalysisResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef",
    {
        "FleetAdvisorSchemaObjects": List[FleetAdvisorSchemaObjectResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List[OrderableReplicationInstanceTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRecommendationLimitationsResponseTypeDef = TypedDict(
    "DescribeRecommendationLimitationsResponseTypeDef",
    {
        "Limitations": List[LimitationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusResponseTypeDef",
    {
        "RefreshSchemasStatus": RefreshSchemasStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RefreshSchemasResponseTypeDef = TypedDict(
    "RefreshSchemasResponseTypeDef",
    {
        "RefreshSchemasStatus": RefreshSchemasStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List[ReplicationInstanceTaskLogTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationTableStatisticsResponseTypeDef = TypedDict(
    "DescribeReplicationTableStatisticsResponseTypeDef",
    {
        "ReplicationConfigArn": str,
        "Marker": str,
        "ReplicationTableStatistics": List[TableStatisticsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTableStatisticsResponseTypeDef = TypedDict(
    "DescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[TableStatisticsTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[ReplicationTaskAssessmentResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationTaskIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskIndividualAssessments": List[ReplicationTaskIndividualAssessmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointIdentifier": NotRequired[str],
        "EndpointType": NotRequired[ReplicationEndpointTypeValueType],
        "EngineName": NotRequired[str],
        "EngineDisplayName": NotRequired[str],
        "Username": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "Status": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "EndpointArn": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "ExternalId": NotRequired[str],
        "DynamoDbSettings": NotRequired[DynamoDbSettingsTypeDef],
        "S3Settings": NotRequired[S3SettingsTypeDef],
        "DmsTransferSettings": NotRequired[DmsTransferSettingsTypeDef],
        "MongoDbSettings": NotRequired[MongoDbSettingsTypeDef],
        "KinesisSettings": NotRequired[KinesisSettingsTypeDef],
        "KafkaSettings": NotRequired[KafkaSettingsTypeDef],
        "ElasticsearchSettings": NotRequired[ElasticsearchSettingsTypeDef],
        "NeptuneSettings": NotRequired[NeptuneSettingsTypeDef],
        "RedshiftSettings": NotRequired[RedshiftSettingsTypeDef],
        "PostgreSQLSettings": NotRequired[PostgreSQLSettingsTypeDef],
        "MySQLSettings": NotRequired[MySQLSettingsTypeDef],
        "OracleSettings": NotRequired[OracleSettingsOutputTypeDef],
        "SybaseSettings": NotRequired[SybaseSettingsTypeDef],
        "MicrosoftSQLServerSettings": NotRequired[MicrosoftSQLServerSettingsTypeDef],
        "IBMDb2Settings": NotRequired[IBMDb2SettingsTypeDef],
        "DocDbSettings": NotRequired[DocDbSettingsTypeDef],
        "RedisSettings": NotRequired[RedisSettingsTypeDef],
        "GcpMySQLSettings": NotRequired[GcpMySQLSettingsTypeDef],
        "TimestreamSettings": NotRequired[TimestreamSettingsTypeDef],
    },
)
ExportMetadataModelAssessmentResponseTypeDef = TypedDict(
    "ExportMetadataModelAssessmentResponseTypeDef",
    {
        "PdfReport": ExportMetadataModelAssessmentResultEntryTypeDef,
        "CsvReport": ExportMetadataModelAssessmentResultEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "PendingMaintenanceActionDetails": NotRequired[List[PendingMaintenanceActionTypeDef]],
    },
)
RdsRecommendationTypeDef = TypedDict(
    "RdsRecommendationTypeDef",
    {
        "RequirementsToTarget": NotRequired[RdsRequirementsTypeDef],
        "TargetConfiguration": NotRequired[RdsConfigurationTypeDef],
    },
)
StartRecommendationsRequestEntryTypeDef = TypedDict(
    "StartRecommendationsRequestEntryTypeDef",
    {
        "DatabaseId": str,
        "Settings": RecommendationSettingsTypeDef,
    },
)
StartRecommendationsRequestRequestTypeDef = TypedDict(
    "StartRecommendationsRequestRequestTypeDef",
    {
        "DatabaseId": str,
        "Settings": RecommendationSettingsTypeDef,
    },
)
ReloadReplicationTablesMessageRequestTypeDef = TypedDict(
    "ReloadReplicationTablesMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
        "TablesToReload": Sequence[TableToReloadTypeDef],
        "ReloadOption": NotRequired[ReloadOptionValueType],
    },
)
ReloadTablesMessageRequestTypeDef = TypedDict(
    "ReloadTablesMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TablesToReload": Sequence[TableToReloadTypeDef],
        "ReloadOption": NotRequired[ReloadOptionValueType],
    },
)
ReplicationTypeDef = TypedDict(
    "ReplicationTypeDef",
    {
        "ReplicationConfigIdentifier": NotRequired[str],
        "ReplicationConfigArn": NotRequired[str],
        "SourceEndpointArn": NotRequired[str],
        "TargetEndpointArn": NotRequired[str],
        "ReplicationType": NotRequired[MigrationTypeValueType],
        "Status": NotRequired[str],
        "ProvisionData": NotRequired[ProvisionDataTypeDef],
        "StopReason": NotRequired[str],
        "FailureMessages": NotRequired[List[str]],
        "ReplicationStats": NotRequired[ReplicationStatsTypeDef],
        "StartReplicationType": NotRequired[str],
        "CdcStartTime": NotRequired[datetime],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "RecoveryCheckpoint": NotRequired[str],
        "ReplicationCreateTime": NotRequired[datetime],
        "ReplicationUpdateTime": NotRequired[datetime],
        "ReplicationLastStopTime": NotRequired[datetime],
        "ReplicationDeprovisionTime": NotRequired[datetime],
    },
)
ReplicationTaskAssessmentRunTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "Status": NotRequired[str],
        "ReplicationTaskAssessmentRunCreationDate": NotRequired[datetime],
        "AssessmentProgress": NotRequired[ReplicationTaskAssessmentRunProgressTypeDef],
        "LastFailureMessage": NotRequired[str],
        "ServiceAccessRoleArn": NotRequired[str],
        "ResultLocationBucket": NotRequired[str],
        "ResultLocationFolder": NotRequired[str],
        "ResultEncryptionMode": NotRequired[str],
        "ResultKmsKeyArn": NotRequired[str],
        "AssessmentRunName": NotRequired[str],
        "IsLatestTaskAssessmentRun": NotRequired[bool],
        "ResultStatistic": NotRequired[ReplicationTaskAssessmentRunResultStatisticTypeDef],
    },
)
ReplicationTaskTypeDef = TypedDict(
    "ReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": NotRequired[str],
        "SourceEndpointArn": NotRequired[str],
        "TargetEndpointArn": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "MigrationType": NotRequired[MigrationTypeValueType],
        "TableMappings": NotRequired[str],
        "ReplicationTaskSettings": NotRequired[str],
        "Status": NotRequired[str],
        "LastFailureMessage": NotRequired[str],
        "StopReason": NotRequired[str],
        "ReplicationTaskCreationDate": NotRequired[datetime],
        "ReplicationTaskStartDate": NotRequired[datetime],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "RecoveryCheckpoint": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationTaskStats": NotRequired[ReplicationTaskStatsTypeDef],
        "TaskData": NotRequired[str],
        "TargetReplicationInstanceArn": NotRequired[str],
    },
)
SchemaResponseTypeDef = TypedDict(
    "SchemaResponseTypeDef",
    {
        "CodeLineCount": NotRequired[int],
        "CodeSize": NotRequired[int],
        "Complexity": NotRequired[str],
        "Server": NotRequired[ServerShortInfoResponseTypeDef],
        "DatabaseInstance": NotRequired[DatabaseShortInfoResponseTypeDef],
        "SchemaId": NotRequired[str],
        "SchemaName": NotRequired[str],
        "OriginalSchema": NotRequired[SchemaShortInfoResponseTypeDef],
        "Similarity": NotRequired[float],
    },
)
ReplicationSubnetGroupTypeDef = TypedDict(
    "ReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": NotRequired[str],
        "ReplicationSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List[SubnetTypeDef]],
        "SupportedNetworkTypes": NotRequired[List[str]],
    },
)
DescribeFleetAdvisorCollectorsResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorCollectorsResponseTypeDef",
    {
        "Collectors": List[CollectorResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateReplicationConfigResponseTypeDef = TypedDict(
    "CreateReplicationConfigResponseTypeDef",
    {
        "ReplicationConfig": ReplicationConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteReplicationConfigResponseTypeDef = TypedDict(
    "DeleteReplicationConfigResponseTypeDef",
    {
        "ReplicationConfig": ReplicationConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationConfigsResponseTypeDef = TypedDict(
    "DescribeReplicationConfigsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationConfigs": List[ReplicationConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyReplicationConfigResponseTypeDef = TypedDict(
    "ModifyReplicationConfigResponseTypeDef",
    {
        "ReplicationConfig": ReplicationConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDataMigrationMessageRequestTypeDef = TypedDict(
    "ModifyDataMigrationMessageRequestTypeDef",
    {
        "DataMigrationIdentifier": str,
        "DataMigrationName": NotRequired[str],
        "EnableCloudwatchLogs": NotRequired[bool],
        "ServiceAccessRoleArn": NotRequired[str],
        "DataMigrationType": NotRequired[MigrationTypeValueType],
        "SourceDataSettings": NotRequired[Sequence[SourceDataSettingTypeDef]],
        "NumberOfJobs": NotRequired[int],
        "SelectionRules": NotRequired[str],
    },
)
SourceDataSettingUnionTypeDef = Union[SourceDataSettingTypeDef, SourceDataSettingOutputTypeDef]
CreateDataMigrationResponseTypeDef = TypedDict(
    "CreateDataMigrationResponseTypeDef",
    {
        "DataMigration": DataMigrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataMigrationResponseTypeDef = TypedDict(
    "DeleteDataMigrationResponseTypeDef",
    {
        "DataMigration": DataMigrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDataMigrationsResponseTypeDef = TypedDict(
    "DescribeDataMigrationsResponseTypeDef",
    {
        "DataMigrations": List[DataMigrationTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDataMigrationResponseTypeDef = TypedDict(
    "ModifyDataMigrationResponseTypeDef",
    {
        "DataMigration": DataMigrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataMigrationResponseTypeDef = TypedDict(
    "StartDataMigrationResponseTypeDef",
    {
        "DataMigration": DataMigrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDataMigrationResponseTypeDef = TypedDict(
    "StopDataMigrationResponseTypeDef",
    {
        "DataMigration": DataMigrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMigrationProjectResponseTypeDef = TypedDict(
    "CreateMigrationProjectResponseTypeDef",
    {
        "MigrationProject": MigrationProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMigrationProjectResponseTypeDef = TypedDict(
    "DeleteMigrationProjectResponseTypeDef",
    {
        "MigrationProject": MigrationProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMigrationProjectsResponseTypeDef = TypedDict(
    "DescribeMigrationProjectsResponseTypeDef",
    {
        "Marker": str,
        "MigrationProjects": List[MigrationProjectTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyMigrationProjectResponseTypeDef = TypedDict(
    "ModifyMigrationProjectResponseTypeDef",
    {
        "MigrationProject": MigrationProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataProviderMessageRequestTypeDef = TypedDict(
    "CreateDataProviderMessageRequestTypeDef",
    {
        "Engine": str,
        "Settings": DataProviderSettingsTypeDef,
        "DataProviderName": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DataProviderTypeDef = TypedDict(
    "DataProviderTypeDef",
    {
        "DataProviderName": NotRequired[str],
        "DataProviderArn": NotRequired[str],
        "DataProviderCreationTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "Engine": NotRequired[str],
        "Settings": NotRequired[DataProviderSettingsTypeDef],
    },
)
ModifyDataProviderMessageRequestTypeDef = TypedDict(
    "ModifyDataProviderMessageRequestTypeDef",
    {
        "DataProviderIdentifier": str,
        "DataProviderName": NotRequired[str],
        "Description": NotRequired[str],
        "Engine": NotRequired[str],
        "ExactSettings": NotRequired[bool],
        "Settings": NotRequired[DataProviderSettingsTypeDef],
    },
)
DescribeFleetAdvisorDatabasesResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorDatabasesResponseTypeDef",
    {
        "Databases": List[DatabaseResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SchemaConversionRequestTypeDef = TypedDict(
    "SchemaConversionRequestTypeDef",
    {
        "Status": NotRequired[str],
        "RequestIdentifier": NotRequired[str],
        "MigrationProjectArn": NotRequired[str],
        "Error": NotRequired[ErrorDetailsTypeDef],
        "ExportSqlDetails": NotRequired[ExportSqlDetailsTypeDef],
    },
)
CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "Endpoint": EndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef",
    {
        "Endpoint": EndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Marker": str,
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyEndpointResponseTypeDef = TypedDict(
    "ModifyEndpointResponseTypeDef",
    {
        "Endpoint": EndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ResourcePendingMaintenanceActionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[ResourcePendingMaintenanceActionsTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "RdsEngine": NotRequired[RdsRecommendationTypeDef],
    },
)
BatchStartRecommendationsRequestRequestTypeDef = TypedDict(
    "BatchStartRecommendationsRequestRequestTypeDef",
    {
        "Data": NotRequired[Sequence[StartRecommendationsRequestEntryTypeDef]],
    },
)
DescribeReplicationsResponseTypeDef = TypedDict(
    "DescribeReplicationsResponseTypeDef",
    {
        "Marker": str,
        "Replications": List[ReplicationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReplicationResponseTypeDef = TypedDict(
    "StartReplicationResponseTypeDef",
    {
        "Replication": ReplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopReplicationResponseTypeDef = TypedDict(
    "StopReplicationResponseTypeDef",
    {
        "Replication": ReplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": ReplicationTaskAssessmentRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": ReplicationTaskAssessmentRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationTaskAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskAssessmentRuns": List[ReplicationTaskAssessmentRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": ReplicationTaskAssessmentRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReplicationTaskResponseTypeDef = TypedDict(
    "CreateReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": ReplicationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteReplicationTaskResponseTypeDef = TypedDict(
    "DeleteReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": ReplicationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationTasksResponseTypeDef = TypedDict(
    "DescribeReplicationTasksResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List[ReplicationTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyReplicationTaskResponseTypeDef = TypedDict(
    "ModifyReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": ReplicationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MoveReplicationTaskResponseTypeDef = TypedDict(
    "MoveReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": ReplicationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentResponseTypeDef",
    {
        "ReplicationTask": ReplicationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReplicationTaskResponseTypeDef = TypedDict(
    "StartReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": ReplicationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopReplicationTaskResponseTypeDef = TypedDict(
    "StopReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": ReplicationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetAdvisorSchemasResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemasResponseTypeDef",
    {
        "FleetAdvisorSchemas": List[SchemaResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "CreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ReplicationSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List[ReplicationSubnetGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ReplicationSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicationInstanceTypeDef = TypedDict(
    "ReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": NotRequired[str],
        "ReplicationInstanceClass": NotRequired[str],
        "ReplicationInstanceStatus": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "InstanceCreateTime": NotRequired[datetime],
        "VpcSecurityGroups": NotRequired[List[VpcSecurityGroupMembershipTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "ReplicationSubnetGroup": NotRequired[ReplicationSubnetGroupTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[ReplicationPendingModifiedValuesTypeDef],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "ReplicationInstancePublicIpAddress": NotRequired[str],
        "ReplicationInstancePrivateIpAddress": NotRequired[str],
        "ReplicationInstancePublicIpAddresses": NotRequired[List[str]],
        "ReplicationInstancePrivateIpAddresses": NotRequired[List[str]],
        "ReplicationInstanceIpv6Addresses": NotRequired[List[str]],
        "PubliclyAccessible": NotRequired[bool],
        "SecondaryAvailabilityZone": NotRequired[str],
        "FreeUntil": NotRequired[datetime],
        "DnsNameServers": NotRequired[str],
        "NetworkType": NotRequired[str],
    },
)
CreateDataMigrationMessageRequestTypeDef = TypedDict(
    "CreateDataMigrationMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "DataMigrationType": MigrationTypeValueType,
        "ServiceAccessRoleArn": str,
        "DataMigrationName": NotRequired[str],
        "EnableCloudwatchLogs": NotRequired[bool],
        "SourceDataSettings": NotRequired[Sequence[SourceDataSettingUnionTypeDef]],
        "NumberOfJobs": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SelectionRules": NotRequired[str],
    },
)
CreateDataProviderResponseTypeDef = TypedDict(
    "CreateDataProviderResponseTypeDef",
    {
        "DataProvider": DataProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataProviderResponseTypeDef = TypedDict(
    "DeleteDataProviderResponseTypeDef",
    {
        "DataProvider": DataProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDataProvidersResponseTypeDef = TypedDict(
    "DescribeDataProvidersResponseTypeDef",
    {
        "Marker": str,
        "DataProviders": List[DataProviderTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDataProviderResponseTypeDef = TypedDict(
    "ModifyDataProviderResponseTypeDef",
    {
        "DataProvider": DataProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExtensionPackAssociationsResponseTypeDef = TypedDict(
    "DescribeExtensionPackAssociationsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List[SchemaConversionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMetadataModelAssessmentsResponseTypeDef = TypedDict(
    "DescribeMetadataModelAssessmentsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List[SchemaConversionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMetadataModelConversionsResponseTypeDef = TypedDict(
    "DescribeMetadataModelConversionsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List[SchemaConversionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMetadataModelExportsAsScriptResponseTypeDef = TypedDict(
    "DescribeMetadataModelExportsAsScriptResponseTypeDef",
    {
        "Marker": str,
        "Requests": List[SchemaConversionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMetadataModelExportsToTargetResponseTypeDef = TypedDict(
    "DescribeMetadataModelExportsToTargetResponseTypeDef",
    {
        "Marker": str,
        "Requests": List[SchemaConversionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMetadataModelImportsResponseTypeDef = TypedDict(
    "DescribeMetadataModelImportsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List[SchemaConversionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "DatabaseId": NotRequired[str],
        "EngineName": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Status": NotRequired[str],
        "Preferred": NotRequired[bool],
        "Settings": NotRequired[RecommendationSettingsTypeDef],
        "Data": NotRequired[RecommendationDataTypeDef],
    },
)
CreateReplicationInstanceResponseTypeDef = TypedDict(
    "CreateReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ReplicationInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteReplicationInstanceResponseTypeDef = TypedDict(
    "DeleteReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ReplicationInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List[ReplicationInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyReplicationInstanceResponseTypeDef = TypedDict(
    "ModifyReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ReplicationInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootReplicationInstanceResponseTypeDef = TypedDict(
    "RebootReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": ReplicationInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRecommendationsResponseTypeDef = TypedDict(
    "DescribeRecommendationsResponseTypeDef",
    {
        "Recommendations": List[RecommendationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
