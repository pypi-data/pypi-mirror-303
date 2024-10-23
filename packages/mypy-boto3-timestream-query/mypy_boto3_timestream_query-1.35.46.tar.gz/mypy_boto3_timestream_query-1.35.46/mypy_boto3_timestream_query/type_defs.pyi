"""
Type annotations for timestream-query service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/type_defs/)

Usage::

    ```python
    from mypy_boto3_timestream_query.type_defs import CancelQueryRequestRequestTypeDef

    data: CancelQueryRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence, Union

from .literals import (
    MeasureValueTypeType,
    QueryInsightsModeType,
    QueryPricingModelType,
    S3EncryptionOptionType,
    ScalarMeasureValueTypeType,
    ScalarTypeType,
    ScheduledQueryInsightsModeType,
    ScheduledQueryRunStatusType,
    ScheduledQueryStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CancelQueryRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TypePaginatorTypeDef",
    "ColumnInfoTypeDef",
    "ScheduleConfigurationTypeDef",
    "TagTypeDef",
    "TimeSeriesDataPointPaginatorTypeDef",
    "TimeSeriesDataPointTypeDef",
    "DeleteScheduledQueryRequestRequestTypeDef",
    "EndpointTypeDef",
    "DescribeScheduledQueryRequestRequestTypeDef",
    "DimensionMappingTypeDef",
    "S3ConfigurationTypeDef",
    "S3ReportLocationTypeDef",
    "ScheduledQueryInsightsTypeDef",
    "TimestampTypeDef",
    "ExecutionStatsTypeDef",
    "PaginatorConfigTypeDef",
    "ListScheduledQueriesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "SnsConfigurationTypeDef",
    "PrepareQueryRequestRequestTypeDef",
    "QueryInsightsTypeDef",
    "QueryStatusTypeDef",
    "QuerySpatialCoverageMaxTypeDef",
    "QueryTemporalRangeMaxTypeDef",
    "TimestreamDestinationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateScheduledQueryRequestRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "CreateScheduledQueryResponseTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "ColumnInfoPaginatorTypeDef",
    "TypeTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DatumPaginatorTypeDef",
    "DatumTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "ErrorReportConfigurationTypeDef",
    "ErrorReportLocationTypeDef",
    "ExecuteScheduledQueryRequestRequestTypeDef",
    "ListScheduledQueriesRequestListScheduledQueriesPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "MixedMeasureMappingOutputTypeDef",
    "MixedMeasureMappingTypeDef",
    "MultiMeasureMappingsOutputTypeDef",
    "MultiMeasureMappingsTypeDef",
    "NotificationConfigurationTypeDef",
    "QueryRequestQueryPaginateTypeDef",
    "QueryRequestRequestTypeDef",
    "QuerySpatialCoverageTypeDef",
    "QueryTemporalRangeTypeDef",
    "TargetDestinationTypeDef",
    "ParameterMappingTypeDef",
    "SelectColumnTypeDef",
    "RowPaginatorTypeDef",
    "RowTypeDef",
    "MixedMeasureMappingUnionTypeDef",
    "TimestreamConfigurationOutputTypeDef",
    "MultiMeasureMappingsUnionTypeDef",
    "QueryInsightsResponseTypeDef",
    "ScheduledQueryInsightsResponseTypeDef",
    "ScheduledQueryTypeDef",
    "PrepareQueryResponseTypeDef",
    "TargetConfigurationOutputTypeDef",
    "TimestreamConfigurationTypeDef",
    "QueryResponsePaginatorTypeDef",
    "QueryResponseTypeDef",
    "ScheduledQueryRunSummaryTypeDef",
    "ListScheduledQueriesResponseTypeDef",
    "TimestreamConfigurationUnionTypeDef",
    "ScheduledQueryDescriptionTypeDef",
    "TargetConfigurationTypeDef",
    "DescribeScheduledQueryResponseTypeDef",
    "CreateScheduledQueryRequestRequestTypeDef",
)

CancelQueryRequestRequestTypeDef = TypedDict(
    "CancelQueryRequestRequestTypeDef",
    {
        "QueryId": str,
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
TypePaginatorTypeDef = TypedDict(
    "TypePaginatorTypeDef",
    {
        "ScalarType": NotRequired[ScalarTypeType],
        "ArrayColumnInfo": NotRequired[Dict[str, Any]],
        "TimeSeriesMeasureValueColumnInfo": NotRequired[Dict[str, Any]],
        "RowColumnInfo": NotRequired[List[Dict[str, Any]]],
    },
)
ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "Type": Dict[str, Any],
        "Name": NotRequired[str],
    },
)
ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "ScheduleExpression": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
TimeSeriesDataPointPaginatorTypeDef = TypedDict(
    "TimeSeriesDataPointPaginatorTypeDef",
    {
        "Time": str,
        "Value": Dict[str, Any],
    },
)
TimeSeriesDataPointTypeDef = TypedDict(
    "TimeSeriesDataPointTypeDef",
    {
        "Time": str,
        "Value": Dict[str, Any],
    },
)
DeleteScheduledQueryRequestRequestTypeDef = TypedDict(
    "DeleteScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)
DescribeScheduledQueryRequestRequestTypeDef = TypedDict(
    "DescribeScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
    },
)
DimensionMappingTypeDef = TypedDict(
    "DimensionMappingTypeDef",
    {
        "Name": str,
        "DimensionValueType": Literal["VARCHAR"],
    },
)
S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketName": str,
        "ObjectKeyPrefix": NotRequired[str],
        "EncryptionOption": NotRequired[S3EncryptionOptionType],
    },
)
S3ReportLocationTypeDef = TypedDict(
    "S3ReportLocationTypeDef",
    {
        "BucketName": NotRequired[str],
        "ObjectKey": NotRequired[str],
    },
)
ScheduledQueryInsightsTypeDef = TypedDict(
    "ScheduledQueryInsightsTypeDef",
    {
        "Mode": ScheduledQueryInsightsModeType,
    },
)
TimestampTypeDef = Union[datetime, str]
ExecutionStatsTypeDef = TypedDict(
    "ExecutionStatsTypeDef",
    {
        "ExecutionTimeInMillis": NotRequired[int],
        "DataWrites": NotRequired[int],
        "BytesMetered": NotRequired[int],
        "CumulativeBytesScanned": NotRequired[int],
        "RecordsIngested": NotRequired[int],
        "QueryResultRows": NotRequired[int],
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
ListScheduledQueriesRequestRequestTypeDef = TypedDict(
    "ListScheduledQueriesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MultiMeasureAttributeMappingTypeDef = TypedDict(
    "MultiMeasureAttributeMappingTypeDef",
    {
        "SourceColumn": str,
        "MeasureValueType": ScalarMeasureValueTypeType,
        "TargetMultiMeasureAttributeName": NotRequired[str],
    },
)
SnsConfigurationTypeDef = TypedDict(
    "SnsConfigurationTypeDef",
    {
        "TopicArn": str,
    },
)
PrepareQueryRequestRequestTypeDef = TypedDict(
    "PrepareQueryRequestRequestTypeDef",
    {
        "QueryString": str,
        "ValidateOnly": NotRequired[bool],
    },
)
QueryInsightsTypeDef = TypedDict(
    "QueryInsightsTypeDef",
    {
        "Mode": QueryInsightsModeType,
    },
)
QueryStatusTypeDef = TypedDict(
    "QueryStatusTypeDef",
    {
        "ProgressPercentage": NotRequired[float],
        "CumulativeBytesScanned": NotRequired[int],
        "CumulativeBytesMetered": NotRequired[int],
    },
)
QuerySpatialCoverageMaxTypeDef = TypedDict(
    "QuerySpatialCoverageMaxTypeDef",
    {
        "Value": NotRequired[float],
        "TableArn": NotRequired[str],
        "PartitionKey": NotRequired[List[str]],
    },
)
QueryTemporalRangeMaxTypeDef = TypedDict(
    "QueryTemporalRangeMaxTypeDef",
    {
        "Value": NotRequired[int],
        "TableArn": NotRequired[str],
    },
)
TimestreamDestinationTypeDef = TypedDict(
    "TimestreamDestinationTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "MaxQueryTCU": NotRequired[int],
        "QueryPricingModel": NotRequired[QueryPricingModelType],
    },
)
UpdateScheduledQueryRequestRequestTypeDef = TypedDict(
    "UpdateScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
        "State": ScheduledQueryStateType,
    },
)
CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "CancellationMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScheduledQueryResponseTypeDef = TypedDict(
    "CreateScheduledQueryResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountSettingsResponseTypeDef = TypedDict(
    "DescribeAccountSettingsResponseTypeDef",
    {
        "MaxQueryTCU": int,
        "QueryPricingModel": QueryPricingModelType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccountSettingsResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseTypeDef",
    {
        "MaxQueryTCU": int,
        "QueryPricingModel": QueryPricingModelType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ColumnInfoPaginatorTypeDef = TypedDict(
    "ColumnInfoPaginatorTypeDef",
    {
        "Type": TypePaginatorTypeDef,
        "Name": NotRequired[str],
    },
)
TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "ScalarType": NotRequired[ScalarTypeType],
        "ArrayColumnInfo": NotRequired[Dict[str, Any]],
        "TimeSeriesMeasureValueColumnInfo": NotRequired[Dict[str, Any]],
        "RowColumnInfo": NotRequired[List[ColumnInfoTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
DatumPaginatorTypeDef = TypedDict(
    "DatumPaginatorTypeDef",
    {
        "ScalarValue": NotRequired[str],
        "TimeSeriesValue": NotRequired[List[TimeSeriesDataPointPaginatorTypeDef]],
        "ArrayValue": NotRequired[List[Dict[str, Any]]],
        "RowValue": NotRequired[Dict[str, Any]],
        "NullValue": NotRequired[bool],
    },
)
DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "ScalarValue": NotRequired[str],
        "TimeSeriesValue": NotRequired[List[TimeSeriesDataPointTypeDef]],
        "ArrayValue": NotRequired[List[Dict[str, Any]]],
        "RowValue": NotRequired[Dict[str, Any]],
        "NullValue": NotRequired[bool],
    },
)
DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ErrorReportConfigurationTypeDef = TypedDict(
    "ErrorReportConfigurationTypeDef",
    {
        "S3Configuration": S3ConfigurationTypeDef,
    },
)
ErrorReportLocationTypeDef = TypedDict(
    "ErrorReportLocationTypeDef",
    {
        "S3ReportLocation": NotRequired[S3ReportLocationTypeDef],
    },
)
ExecuteScheduledQueryRequestRequestTypeDef = TypedDict(
    "ExecuteScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
        "InvocationTime": TimestampTypeDef,
        "ClientToken": NotRequired[str],
        "QueryInsights": NotRequired[ScheduledQueryInsightsTypeDef],
    },
)
ListScheduledQueriesRequestListScheduledQueriesPaginateTypeDef = TypedDict(
    "ListScheduledQueriesRequestListScheduledQueriesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceARN": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
MixedMeasureMappingOutputTypeDef = TypedDict(
    "MixedMeasureMappingOutputTypeDef",
    {
        "MeasureValueType": MeasureValueTypeType,
        "MeasureName": NotRequired[str],
        "SourceColumn": NotRequired[str],
        "TargetMeasureName": NotRequired[str],
        "MultiMeasureAttributeMappings": NotRequired[List[MultiMeasureAttributeMappingTypeDef]],
    },
)
MixedMeasureMappingTypeDef = TypedDict(
    "MixedMeasureMappingTypeDef",
    {
        "MeasureValueType": MeasureValueTypeType,
        "MeasureName": NotRequired[str],
        "SourceColumn": NotRequired[str],
        "TargetMeasureName": NotRequired[str],
        "MultiMeasureAttributeMappings": NotRequired[Sequence[MultiMeasureAttributeMappingTypeDef]],
    },
)
MultiMeasureMappingsOutputTypeDef = TypedDict(
    "MultiMeasureMappingsOutputTypeDef",
    {
        "MultiMeasureAttributeMappings": List[MultiMeasureAttributeMappingTypeDef],
        "TargetMultiMeasureName": NotRequired[str],
    },
)
MultiMeasureMappingsTypeDef = TypedDict(
    "MultiMeasureMappingsTypeDef",
    {
        "MultiMeasureAttributeMappings": Sequence[MultiMeasureAttributeMappingTypeDef],
        "TargetMultiMeasureName": NotRequired[str],
    },
)
NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "SnsConfiguration": SnsConfigurationTypeDef,
    },
)
QueryRequestQueryPaginateTypeDef = TypedDict(
    "QueryRequestQueryPaginateTypeDef",
    {
        "QueryString": str,
        "ClientToken": NotRequired[str],
        "QueryInsights": NotRequired[QueryInsightsTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
QueryRequestRequestTypeDef = TypedDict(
    "QueryRequestRequestTypeDef",
    {
        "QueryString": str,
        "ClientToken": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxRows": NotRequired[int],
        "QueryInsights": NotRequired[QueryInsightsTypeDef],
    },
)
QuerySpatialCoverageTypeDef = TypedDict(
    "QuerySpatialCoverageTypeDef",
    {
        "Max": NotRequired[QuerySpatialCoverageMaxTypeDef],
    },
)
QueryTemporalRangeTypeDef = TypedDict(
    "QueryTemporalRangeTypeDef",
    {
        "Max": NotRequired[QueryTemporalRangeMaxTypeDef],
    },
)
TargetDestinationTypeDef = TypedDict(
    "TargetDestinationTypeDef",
    {
        "TimestreamDestination": NotRequired[TimestreamDestinationTypeDef],
    },
)
ParameterMappingTypeDef = TypedDict(
    "ParameterMappingTypeDef",
    {
        "Name": str,
        "Type": TypeTypeDef,
    },
)
SelectColumnTypeDef = TypedDict(
    "SelectColumnTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[TypeTypeDef],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Aliased": NotRequired[bool],
    },
)
RowPaginatorTypeDef = TypedDict(
    "RowPaginatorTypeDef",
    {
        "Data": List[DatumPaginatorTypeDef],
    },
)
RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": List[DatumTypeDef],
    },
)
MixedMeasureMappingUnionTypeDef = Union[
    MixedMeasureMappingTypeDef, MixedMeasureMappingOutputTypeDef
]
TimestreamConfigurationOutputTypeDef = TypedDict(
    "TimestreamConfigurationOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "TimeColumn": str,
        "DimensionMappings": List[DimensionMappingTypeDef],
        "MultiMeasureMappings": NotRequired[MultiMeasureMappingsOutputTypeDef],
        "MixedMeasureMappings": NotRequired[List[MixedMeasureMappingOutputTypeDef]],
        "MeasureNameColumn": NotRequired[str],
    },
)
MultiMeasureMappingsUnionTypeDef = Union[
    MultiMeasureMappingsTypeDef, MultiMeasureMappingsOutputTypeDef
]
QueryInsightsResponseTypeDef = TypedDict(
    "QueryInsightsResponseTypeDef",
    {
        "QuerySpatialCoverage": NotRequired[QuerySpatialCoverageTypeDef],
        "QueryTemporalRange": NotRequired[QueryTemporalRangeTypeDef],
        "QueryTableCount": NotRequired[int],
        "OutputRows": NotRequired[int],
        "OutputBytes": NotRequired[int],
        "UnloadPartitionCount": NotRequired[int],
        "UnloadWrittenRows": NotRequired[int],
        "UnloadWrittenBytes": NotRequired[int],
    },
)
ScheduledQueryInsightsResponseTypeDef = TypedDict(
    "ScheduledQueryInsightsResponseTypeDef",
    {
        "QuerySpatialCoverage": NotRequired[QuerySpatialCoverageTypeDef],
        "QueryTemporalRange": NotRequired[QueryTemporalRangeTypeDef],
        "QueryTableCount": NotRequired[int],
        "OutputRows": NotRequired[int],
        "OutputBytes": NotRequired[int],
    },
)
ScheduledQueryTypeDef = TypedDict(
    "ScheduledQueryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "State": ScheduledQueryStateType,
        "CreationTime": NotRequired[datetime],
        "PreviousInvocationTime": NotRequired[datetime],
        "NextInvocationTime": NotRequired[datetime],
        "ErrorReportConfiguration": NotRequired[ErrorReportConfigurationTypeDef],
        "TargetDestination": NotRequired[TargetDestinationTypeDef],
        "LastRunStatus": NotRequired[ScheduledQueryRunStatusType],
    },
)
PrepareQueryResponseTypeDef = TypedDict(
    "PrepareQueryResponseTypeDef",
    {
        "QueryString": str,
        "Columns": List[SelectColumnTypeDef],
        "Parameters": List[ParameterMappingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TargetConfigurationOutputTypeDef = TypedDict(
    "TargetConfigurationOutputTypeDef",
    {
        "TimestreamConfiguration": TimestreamConfigurationOutputTypeDef,
    },
)
TimestreamConfigurationTypeDef = TypedDict(
    "TimestreamConfigurationTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "TimeColumn": str,
        "DimensionMappings": Sequence[DimensionMappingTypeDef],
        "MultiMeasureMappings": NotRequired[MultiMeasureMappingsUnionTypeDef],
        "MixedMeasureMappings": NotRequired[Sequence[MixedMeasureMappingUnionTypeDef]],
        "MeasureNameColumn": NotRequired[str],
    },
)
QueryResponsePaginatorTypeDef = TypedDict(
    "QueryResponsePaginatorTypeDef",
    {
        "QueryId": str,
        "Rows": List[RowPaginatorTypeDef],
        "ColumnInfo": List[ColumnInfoPaginatorTypeDef],
        "QueryStatus": QueryStatusTypeDef,
        "QueryInsightsResponse": QueryInsightsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
QueryResponseTypeDef = TypedDict(
    "QueryResponseTypeDef",
    {
        "QueryId": str,
        "Rows": List[RowTypeDef],
        "ColumnInfo": List[ColumnInfoTypeDef],
        "QueryStatus": QueryStatusTypeDef,
        "QueryInsightsResponse": QueryInsightsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ScheduledQueryRunSummaryTypeDef = TypedDict(
    "ScheduledQueryRunSummaryTypeDef",
    {
        "InvocationTime": NotRequired[datetime],
        "TriggerTime": NotRequired[datetime],
        "RunStatus": NotRequired[ScheduledQueryRunStatusType],
        "ExecutionStats": NotRequired[ExecutionStatsTypeDef],
        "QueryInsightsResponse": NotRequired[ScheduledQueryInsightsResponseTypeDef],
        "ErrorReportLocation": NotRequired[ErrorReportLocationTypeDef],
        "FailureReason": NotRequired[str],
    },
)
ListScheduledQueriesResponseTypeDef = TypedDict(
    "ListScheduledQueriesResponseTypeDef",
    {
        "ScheduledQueries": List[ScheduledQueryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TimestreamConfigurationUnionTypeDef = Union[
    TimestreamConfigurationTypeDef, TimestreamConfigurationOutputTypeDef
]
ScheduledQueryDescriptionTypeDef = TypedDict(
    "ScheduledQueryDescriptionTypeDef",
    {
        "Arn": str,
        "Name": str,
        "QueryString": str,
        "State": ScheduledQueryStateType,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
        "CreationTime": NotRequired[datetime],
        "PreviousInvocationTime": NotRequired[datetime],
        "NextInvocationTime": NotRequired[datetime],
        "TargetConfiguration": NotRequired[TargetConfigurationOutputTypeDef],
        "ScheduledQueryExecutionRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "ErrorReportConfiguration": NotRequired[ErrorReportConfigurationTypeDef],
        "LastRunSummary": NotRequired[ScheduledQueryRunSummaryTypeDef],
        "RecentlyFailedRuns": NotRequired[List[ScheduledQueryRunSummaryTypeDef]],
    },
)
TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "TimestreamConfiguration": TimestreamConfigurationUnionTypeDef,
    },
)
DescribeScheduledQueryResponseTypeDef = TypedDict(
    "DescribeScheduledQueryResponseTypeDef",
    {
        "ScheduledQuery": ScheduledQueryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScheduledQueryRequestRequestTypeDef = TypedDict(
    "CreateScheduledQueryRequestRequestTypeDef",
    {
        "Name": str,
        "QueryString": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
        "ScheduledQueryExecutionRoleArn": str,
        "ErrorReportConfiguration": ErrorReportConfigurationTypeDef,
        "TargetConfiguration": NotRequired[TargetConfigurationTypeDef],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "KmsKeyId": NotRequired[str],
    },
)
