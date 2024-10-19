from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class AspectType(Enum):
    ASSET_CONTACTS = "ASSET_CONTACTS"
    ASSET_FOLLOWERS = "ASSET_FOLLOWERS"
    ASSET_GOVERNED_TAGS = "ASSET_GOVERNED_TAGS"
    ASSET_LIKES = "ASSET_LIKES"
    ASSET_STRUCTURE = "ASSET_STRUCTURE"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    COMMON_COLUMN_ATTRIBUTES = "COMMON_COLUMN_ATTRIBUTES"
    CUSTOM_METADATA = "CUSTOM_METADATA"
    DASHBOARD_INFO = "DASHBOARD_INFO"
    DATASET_DATA_QUALITY = "DATASET_DATA_QUALITY"
    DATASET_DOCUMENTATION = "DATASET_DOCUMENTATION"
    DATASET_FIELD_ASSOCIATIONS = "DATASET_FIELD_ASSOCIATIONS"
    DATASET_FIELD_STATISTICS = "DATASET_FIELD_STATISTICS"
    DATASET_INFO = "DATASET_INFO"
    DATASET_LAST_QUERY = "DATASET_LAST_QUERY"
    DATASET_SCHEMA = "DATASET_SCHEMA"
    DATASET_SODA_DATA_QUALITY = "DATASET_SODA_DATA_QUALITY"
    DATASET_STATISTICS = "DATASET_STATISTICS"
    DATASET_USAGE = "DATASET_USAGE"
    DBT_METRIC = "DBT_METRIC"
    DBT_MODEL = "DBT_MODEL"
    ENTITY_UPSTREAM = "ENTITY_UPSTREAM"
    FIVETRAN_PIPELINE = "FIVETRAN_PIPELINE"
    GROUP_INFO = "GROUP_INFO"
    HIERARCHY_INFO = "HIERARCHY_INFO"
    INFORMATICA_MAPPING = "INFORMATICA_MAPPING"
    KNOWLEDGE_CARD_INFO = "KNOWLEDGE_CARD_INFO"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    METRIC_INFO = "METRIC_INFO"
    NAMESPACE_ASSETS = "NAMESPACE_ASSETS"
    NAMESPACE_INFO = "NAMESPACE_INFO"
    OVERALL_DATA_QUALITY = "OVERALL_DATA_QUALITY"
    PARSED_UPSTREAM = "PARSED_UPSTREAM"
    PERSONALIZATION_OPTIONS = "PERSONALIZATION_OPTIONS"
    PERSON_ACTIVITY = "PERSON_ACTIVITY"
    PERSON_ORGANIZATION = "PERSON_ORGANIZATION"
    PERSON_PINS = "PERSON_PINS"
    PERSON_PROPERTIES = "PERSON_PROPERTIES"
    PERSON_SCIM_PROFILE = "PERSON_SCIM_PROFILE"
    PERSON_SLACK_PROFILE = "PERSON_SLACK_PROFILE"
    PERSON_TEAMS_CONVERSION_REFERENCE = "PERSON_TEAMS_CONVERSION_REFERENCE"
    PIPELINE_INFO = "PIPELINE_INFO"
    POWER_BI_DATAFLOW = "POWER_BI_DATAFLOW"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUICK_SIGHT_DATASET = "QUICK_SIGHT_DATASET"
    RELATED_ASSETS = "RELATED_ASSETS"
    SNOWFLAKE_ICEBERG_INFO = "SNOWFLAKE_ICEBERG_INFO"
    SNOWFLAKE_STREAM_INFO = "SNOWFLAKE_STREAM_INFO"
    SOURCE_INFO = "SOURCE_INFO"
    SPARK_JOB = "SPARK_JOB"
    SYSTEM_CONTACTS = "SYSTEM_CONTACTS"
    SYSTEM_DESCRIPTION = "SYSTEM_DESCRIPTION"
    SYSTEM_TAGS = "SYSTEM_TAGS"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    UNITY_CATALOG = "UNITY_CATALOG"
    USER_DEFINED_RESOURCE_INFO = "USER_DEFINED_RESOURCE_INFO"
    VIRTUAL_VIEW_SCHEMA = "VIRTUAL_VIEW_SCHEMA"


class ContactValueType(Enum):
    EMAIL = "EMAIL"
    GROUP = "GROUP"
    PERSON = "PERSON"
    SLACK = "SLACK"
    UNKNOWN = "UNKNOWN"


@dataclass
class DesignatedContact:
    designation: Optional[str] = None
    value: Optional[str] = None
    value_type: Optional[ContactValueType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DesignatedContact':
        assert isinstance(obj, dict)
        designation = from_union([from_str, from_none], obj.get("designation"))
        value = from_union([from_str, from_none], obj.get("value"))
        value_type = from_union([ContactValueType, from_none], obj.get("valueType"))
        return DesignatedContact(designation, value, value_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.designation is not None:
            result["designation"] = from_union([from_str, from_none], self.designation)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        if self.value_type is not None:
            result["valueType"] = from_union([lambda x: to_enum(ContactValueType, x), from_none], self.value_type)
        return result


@dataclass
class AuditStamp:
    """An AuditStamp containing creator and creation time attributes for the Aspect instance
    
    An AuditStamp containing modification and modifier attributes for the Aspect instance
    """
    actor: Optional[str] = None
    time: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuditStamp':
        assert isinstance(obj, dict)
        actor = from_union([from_str, from_none], obj.get("actor"))
        time = from_union([from_datetime, from_none], obj.get("time"))
        return AuditStamp(actor, time)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.actor is not None:
            result["actor"] = from_union([from_str, from_none], self.actor)
        if self.time is not None:
            result["time"] = from_union([lambda x: x.isoformat(), from_none], self.time)
        return result


@dataclass
class AssetContacts:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    contacts: Optional[List[DesignatedContact]] = None
    """Resolved on AssetContactResolver"""

    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    asset_contacts_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    @staticmethod
    def from_dict(obj: Any) -> 'AssetContacts':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        contacts = from_union([lambda x: from_list(DesignatedContact.from_dict, x), from_none], obj.get("contacts"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        asset_contacts_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        return AssetContacts(created_at, aspect_type, contacts, created, asset_contacts_created_at, entity_id, id, last_modified)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.contacts is not None:
            result["contacts"] = from_union([lambda x: from_list(lambda x: to_class(DesignatedContact, x), x), from_none], self.contacts)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.asset_contacts_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.asset_contacts_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        return result


@dataclass
class AssetFollowers:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    asset_followers_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    followed_by: Optional[List[str]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    muted: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AssetFollowers':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        asset_followers_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        followed_by = from_union([lambda x: from_list(from_str, x), from_none], obj.get("followedBy"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        muted = from_union([lambda x: from_list(from_str, x), from_none], obj.get("muted"))
        return AssetFollowers(created_at, aspect_type, created, asset_followers_created_at, entity_id, followed_by, id, last_modified, muted)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.asset_followers_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.asset_followers_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.followed_by is not None:
            result["followedBy"] = from_union([lambda x: from_list(from_str, x), from_none], self.followed_by)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        if self.muted is not None:
            result["muted"] = from_union([lambda x: from_list(from_str, x), from_none], self.muted)
        return result


@dataclass
class AssetGovernedTags:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    asset_governed_tags_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    governed_tag_ids: Optional[List[str]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    @staticmethod
    def from_dict(obj: Any) -> 'AssetGovernedTags':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        asset_governed_tags_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        governed_tag_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("governedTagIds"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        return AssetGovernedTags(created_at, aspect_type, created, asset_governed_tags_created_at, entity_id, governed_tag_ids, id, last_modified)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.asset_governed_tags_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.asset_governed_tags_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.governed_tag_ids is not None:
            result["governedTagIds"] = from_union([lambda x: from_list(from_str, x), from_none], self.governed_tag_ids)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        return result


@dataclass
class AssetLikes:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    asset_likes_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    like_count: Optional[float] = None
    """This is stored as an additional separate field on the document, as opposed to resolved,
    to enable sorting at the database layer
    Mongo does not support sorting on properties of an array such as length
    Note: Although this is a getter, the wrapper withEnumerableGettersTrait will allow the
    field to be enumerable when the instance is iterated
    for example, when assigning / copying
    """
    liked_by: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AssetLikes':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        asset_likes_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        like_count = from_union([from_float, from_none], obj.get("likeCount"))
        liked_by = from_union([lambda x: from_list(from_str, x), from_none], obj.get("likedBy"))
        return AssetLikes(created_at, aspect_type, created, asset_likes_created_at, entity_id, id, last_modified, like_count, liked_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.asset_likes_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.asset_likes_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        if self.like_count is not None:
            result["likeCount"] = from_union([to_float, from_none], self.like_count)
        if self.liked_by is not None:
            result["likedBy"] = from_union([lambda x: from_list(from_str, x), from_none], self.liked_by)
        return result


class DependencyCondition(Enum):
    COMPLETED = "Completed"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    SUCCEEDED = "Succeeded"


@dataclass
class ActivityDependency:
    dependency_conditions: Optional[List[DependencyCondition]] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActivityDependency':
        assert isinstance(obj, dict)
        dependency_conditions = from_union([lambda x: from_list(DependencyCondition, x), from_none], obj.get("dependencyConditions"))
        name = from_union([from_str, from_none], obj.get("name"))
        return ActivityDependency(dependency_conditions, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.dependency_conditions is not None:
            result["dependencyConditions"] = from_union([lambda x: from_list(lambda x: to_enum(DependencyCondition, x), x), from_none], self.dependency_conditions)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class AzureDataFactoryActivity:
    depends_on: Optional[List[ActivityDependency]] = None
    name: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AzureDataFactoryActivity':
        assert isinstance(obj, dict)
        depends_on = from_union([lambda x: from_list(ActivityDependency.from_dict, x), from_none], obj.get("dependsOn"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        return AzureDataFactoryActivity(depends_on, name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.depends_on is not None:
            result["dependsOn"] = from_union([lambda x: from_list(lambda x: to_class(ActivityDependency, x), x), from_none], self.depends_on)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class AzureDataFactoryPipeline:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    activities: Optional[List[AzureDataFactoryActivity]] = None
    aspect_type: Optional[AspectType] = None
    azure_data_factory_pipeline_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    factory: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_duration_in_ms: Optional[float] = None
    last_invoke_type: Optional[str] = None
    last_publish_time: Optional[datetime] = None
    last_run_end: Optional[datetime] = None
    last_run_message: Optional[str] = None
    last_run_start: Optional[datetime] = None
    last_run_status: Optional[str] = None
    pipeline_name: Optional[str] = None
    pipeline_url: Optional[str] = None
    sinks: Optional[List[str]] = None
    sources: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AzureDataFactoryPipeline':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        activities = from_union([lambda x: from_list(AzureDataFactoryActivity.from_dict, x), from_none], obj.get("activities"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        azure_data_factory_pipeline_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        factory = from_union([from_str, from_none], obj.get("factory"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_duration_in_ms = from_union([from_float, from_none], obj.get("lastDurationInMs"))
        last_invoke_type = from_union([from_str, from_none], obj.get("lastInvokeType"))
        last_publish_time = from_union([from_datetime, from_none], obj.get("lastPublishTime"))
        last_run_end = from_union([from_datetime, from_none], obj.get("lastRunEnd"))
        last_run_message = from_union([from_str, from_none], obj.get("lastRunMessage"))
        last_run_start = from_union([from_datetime, from_none], obj.get("lastRunStart"))
        last_run_status = from_union([from_str, from_none], obj.get("lastRunStatus"))
        pipeline_name = from_union([from_str, from_none], obj.get("pipelineName"))
        pipeline_url = from_union([from_str, from_none], obj.get("pipelineUrl"))
        sinks = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sinks"))
        sources = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sources"))
        return AzureDataFactoryPipeline(created_at, activities, aspect_type, azure_data_factory_pipeline_created_at, entity_id, factory, id, last_duration_in_ms, last_invoke_type, last_publish_time, last_run_end, last_run_message, last_run_start, last_run_status, pipeline_name, pipeline_url, sinks, sources)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.activities is not None:
            result["activities"] = from_union([lambda x: from_list(lambda x: to_class(AzureDataFactoryActivity, x), x), from_none], self.activities)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.azure_data_factory_pipeline_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.azure_data_factory_pipeline_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.factory is not None:
            result["factory"] = from_union([from_str, from_none], self.factory)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_duration_in_ms is not None:
            result["lastDurationInMs"] = from_union([to_float, from_none], self.last_duration_in_ms)
        if self.last_invoke_type is not None:
            result["lastInvokeType"] = from_union([from_str, from_none], self.last_invoke_type)
        if self.last_publish_time is not None:
            result["lastPublishTime"] = from_union([lambda x: x.isoformat(), from_none], self.last_publish_time)
        if self.last_run_end is not None:
            result["lastRunEnd"] = from_union([lambda x: x.isoformat(), from_none], self.last_run_end)
        if self.last_run_message is not None:
            result["lastRunMessage"] = from_union([from_str, from_none], self.last_run_message)
        if self.last_run_start is not None:
            result["lastRunStart"] = from_union([lambda x: x.isoformat(), from_none], self.last_run_start)
        if self.last_run_status is not None:
            result["lastRunStatus"] = from_union([from_str, from_none], self.last_run_status)
        if self.pipeline_name is not None:
            result["pipelineName"] = from_union([from_str, from_none], self.pipeline_name)
        if self.pipeline_url is not None:
            result["pipelineUrl"] = from_union([from_str, from_none], self.pipeline_url)
        if self.sinks is not None:
            result["sinks"] = from_union([lambda x: from_list(from_str, x), from_none], self.sinks)
        if self.sources is not None:
            result["sources"] = from_union([lambda x: from_list(from_str, x), from_none], self.sources)
        return result


class Index(Enum):
    """Predefined MongoDB Atlas search index names"""

    ASSETS = "assets"
    DASHBOARDS = "dashboards"
    DATASETS = "datasets"
    DATASET_COLUMNS = "dataset_columns"
    GROUPS = "groups"
    HIERARCHIES = "hierarchies"
    KNOWLEDGE_CARDS = "knowledge_cards"
    METRICS = "metrics"
    NAMESPACES = "namespaces"
    PERSONS = "persons"
    PIPELINES = "pipelines"
    USER_DEFINED_RESOURCE = "user_defined_resource"
    VIRTUAL_VIEWS = "virtual_views"


class NativeType(Enum):
    AIRFLOW = "AIRFLOW"
    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGEYE = "BIGEYE"
    BIGQUERY = "BIGQUERY"
    CONFLUENCE = "CONFLUENCE"
    CUSTOM = "CUSTOM"
    CUSTOM_DASHBOARD = "CUSTOM_DASHBOARD"
    DASH = "DASH"
    DATAHUB = "DATAHUB"
    DBT = "DBT"
    DBT_METRIC = "DBT_METRIC"
    DBT_MODEL = "DBT_MODEL"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    FIVETRAN = "FIVETRAN"
    GCS = "GCS"
    GLUE = "GLUE"
    HIVE = "HIVE"
    HTTP = "HTTP"
    INFORMATICA = "INFORMATICA"
    INFORMATICA_MAPPING = "INFORMATICA_MAPPING"
    KAFKA = "KAFKA"
    LIGHTUP = "LIGHTUP"
    LOOKER = "LOOKER"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    METABASE = "METABASE"
    MONDAY = "MONDAY"
    MONGODB = "MONGODB"
    MONTE_CARLO = "MONTE_CARLO"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    NOTION = "NOTION"
    OPEN_API = "OPEN_API"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    POWER_BI = "POWER_BI"
    POWER_BI_DATAFLOW = "POWER_BI_DATAFLOW"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUICK_SIGHT = "QUICK_SIGHT"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SHAREPOINT = "SHAREPOINT"
    SNOWFLAKE = "SNOWFLAKE"
    SODA = "SODA"
    SPARK = "SPARK"
    STATICWEB = "STATICWEB"
    SYNAPSE = "SYNAPSE"
    TABLEAU = "TABLEAU"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


class BrowsePathSegmentType(Enum):
    COLLECTION = "COLLECTION"
    DASHBOARD = "DASHBOARD"
    DATABASE = "DATABASE"
    DATASET = "DATASET"
    DIRECTORY = "DIRECTORY"
    EXPLORE = "EXPLORE"
    METRIC = "METRIC"
    MODEL = "MODEL"
    NAMESPACE = "NAMESPACE"
    PIPELINE = "PIPELINE"
    PLATFORM = "PLATFORM"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    PROJECT = "PROJECT"
    QUICK_SIGHT_DATASET = "QUICK_SIGHT_DATASET"
    SCHEMA = "SCHEMA"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_DASHBOARD = "THOUGHT_SPOT_DASHBOARD"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    TYPE = "TYPE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"
    WORKSPACE = "WORKSPACE"


@dataclass
class BrowsePathSegment:
    count: Optional[float] = None
    display_name: Optional[str] = None
    native_type: Optional[NativeType] = None
    segment_id: Optional[str] = None
    text: Optional[str] = None
    type: Optional[BrowsePathSegmentType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BrowsePathSegment':
        assert isinstance(obj, dict)
        count = from_union([from_float, from_none], obj.get("count"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        native_type = from_union([NativeType, from_none], obj.get("nativeType"))
        segment_id = from_union([from_str, from_none], obj.get("segmentId"))
        text = from_union([from_str, from_none], obj.get("text"))
        type = from_union([BrowsePathSegmentType, from_none], obj.get("type"))
        return BrowsePathSegment(count, display_name, native_type, segment_id, text, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.count is not None:
            result["count"] = from_union([to_float, from_none], self.count)
        if self.display_name is not None:
            result["displayName"] = from_union([from_str, from_none], self.display_name)
        if self.native_type is not None:
            result["nativeType"] = from_union([lambda x: to_enum(NativeType, x), from_none], self.native_type)
        if self.segment_id is not None:
            result["segmentId"] = from_union([from_str, from_none], self.segment_id)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(BrowsePathSegmentType, x), from_none], self.type)
        return result


@dataclass
class BrowsePath:
    index: Optional[Index] = None
    """Predefined MongoDB Atlas search index names"""

    segments: Optional[List[BrowsePathSegment]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BrowsePath':
        assert isinstance(obj, dict)
        index = from_union([Index, from_none], obj.get("index"))
        segments = from_union([lambda x: from_list(BrowsePathSegment.from_dict, x), from_none], obj.get("segments"))
        return BrowsePath(index, segments)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.index is not None:
            result["index"] = from_union([lambda x: to_enum(Index, x), from_none], self.index)
        if self.segments is not None:
            result["segments"] = from_union([lambda x: from_list(lambda x: to_class(BrowsePathSegment, x), x), from_none], self.segments)
        return result


@dataclass
class CustomMetadataItem:
    """A single key-value pair entry for the custom metadata"""

    key: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CustomMetadataItem':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([from_str, from_none], obj.get("value"))
        return CustomMetadataItem(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class CustomMetadata:
    """Captures custom metadata for an asset"""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    custom_metadata_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    metadata: Optional[List[CustomMetadataItem]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CustomMetadata':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        custom_metadata_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        metadata = from_union([lambda x: from_list(CustomMetadataItem.from_dict, x), from_none], obj.get("metadata"))
        return CustomMetadata(created_at, aspect_type, created, custom_metadata_created_at, entity_id, id, last_modified, metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.custom_metadata_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.custom_metadata_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        if self.metadata is not None:
            result["metadata"] = from_union([lambda x: from_list(lambda x: to_class(CustomMetadataItem, x), x), from_none], self.metadata)
        return result


class ChartType(Enum):
    AREA = "AREA"
    BAR = "BAR"
    BOX_PLOT = "BOX_PLOT"
    COLUMN = "COLUMN"
    DONUT = "DONUT"
    FUNNEL = "FUNNEL"
    LINE = "LINE"
    MAP = "MAP"
    OTHER = "OTHER"
    PIE = "PIE"
    SCATTER = "SCATTER"
    TABLE = "TABLE"
    TEXT = "TEXT"
    TIMELINE = "TIMELINE"
    UNKNOWN = "UNKNOWN"
    WATERFALL = "WATERFALL"


class DataPlatform(Enum):
    """The data platform of the upstream dataset"""

    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGQUERY = "BIGQUERY"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    GCS = "GCS"
    GLUE = "GLUE"
    HIVE = "HIVE"
    HTTP = "HTTP"
    KAFKA = "KAFKA"
    MONGODB = "MONGODB"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SNOWFLAKE = "SNOWFLAKE"
    SYNAPSE = "SYNAPSE"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


@dataclass
class ChartQuery:
    account: Optional[str] = None
    default_database: Optional[str] = None
    default_schema: Optional[str] = None
    platform: Optional[DataPlatform] = None
    query: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChartQuery':
        assert isinstance(obj, dict)
        account = from_union([from_str, from_none], obj.get("account"))
        default_database = from_union([from_str, from_none], obj.get("defaultDatabase"))
        default_schema = from_union([from_str, from_none], obj.get("defaultSchema"))
        platform = from_union([DataPlatform, from_none], obj.get("platform"))
        query = from_union([from_str, from_none], obj.get("query"))
        return ChartQuery(account, default_database, default_schema, platform, query)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account is not None:
            result["account"] = from_union([from_str, from_none], self.account)
        if self.default_database is not None:
            result["defaultDatabase"] = from_union([from_str, from_none], self.default_database)
        if self.default_schema is not None:
            result["defaultSchema"] = from_union([from_str, from_none], self.default_schema)
        if self.platform is not None:
            result["platform"] = from_union([lambda x: to_enum(DataPlatform, x), from_none], self.platform)
        if self.query is not None:
            result["query"] = from_union([from_str, from_none], self.query)
        return result


@dataclass
class Chart:
    chart_type: Optional[ChartType] = None
    description: Optional[str] = None
    id: Optional[str] = None
    preview: Optional[str] = None
    query: Optional[ChartQuery] = None
    title: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Chart':
        assert isinstance(obj, dict)
        chart_type = from_union([ChartType, from_none], obj.get("chartType"))
        description = from_union([from_str, from_none], obj.get("description"))
        id = from_union([from_str, from_none], obj.get("id"))
        preview = from_union([from_str, from_none], obj.get("preview"))
        query = from_union([ChartQuery.from_dict, from_none], obj.get("query"))
        title = from_union([from_str, from_none], obj.get("title"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Chart(chart_type, description, id, preview, query, title, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.chart_type is not None:
            result["chartType"] = from_union([lambda x: to_enum(ChartType, x), from_none], self.chart_type)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.preview is not None:
            result["preview"] = from_union([from_str, from_none], self.preview)
        if self.query is not None:
            result["query"] = from_union([lambda x: to_class(ChartQuery, x), from_none], self.query)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class DashboardType(Enum):
    POWER_BI_DASHBOARD = "POWER_BI_DASHBOARD"
    POWER_BI_REPORT = "POWER_BI_REPORT"
    THOUGHT_SPOT_ANSWER = "THOUGHT_SPOT_ANSWER"
    THOUGHT_SPOT_LIVEBOARD = "THOUGHT_SPOT_LIVEBOARD"
    UNKNOWN = "UNKNOWN"


@dataclass
class PowerBIApp:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIApp':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return PowerBIApp(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


class PowerBIEndorsementType(Enum):
    CERTIFIED = "Certified"
    NONE = "None"
    PROMOTED = "Promoted"


@dataclass
class PowerBIEndorsement:
    certified_by: Optional[str] = None
    endorsement: Optional[PowerBIEndorsementType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIEndorsement':
        assert isinstance(obj, dict)
        certified_by = from_union([from_str, from_none], obj.get("certifiedBy"))
        endorsement = from_union([PowerBIEndorsementType, from_none], obj.get("endorsement"))
        return PowerBIEndorsement(certified_by, endorsement)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.certified_by is not None:
            result["certifiedBy"] = from_union([from_str, from_none], self.certified_by)
        if self.endorsement is not None:
            result["endorsement"] = from_union([lambda x: to_enum(PowerBIEndorsementType, x), from_none], self.endorsement)
        return result


class PowerBIDashboardType(Enum):
    DASHBOARD = "DASHBOARD"
    REPORT = "REPORT"


@dataclass
class PowerBISensitivityLabel:
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBISensitivityLabel':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return PowerBISensitivityLabel(description, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class PowerBISubscriptionUser:
    display_name: Optional[str] = None
    email_address: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBISubscriptionUser':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        email_address = from_union([from_str, from_none], obj.get("emailAddress"))
        return PowerBISubscriptionUser(display_name, email_address)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_name is not None:
            result["displayName"] = from_union([from_str, from_none], self.display_name)
        if self.email_address is not None:
            result["emailAddress"] = from_union([from_str, from_none], self.email_address)
        return result


@dataclass
class PowerBISubscription:
    artifact_display_name: Optional[str] = None
    end_date: Optional[datetime] = None
    frequency: Optional[str] = None
    id: Optional[str] = None
    start_date: Optional[datetime] = None
    sub_artifact_display_name: Optional[str] = None
    title: Optional[str] = None
    users: Optional[List[PowerBISubscriptionUser]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBISubscription':
        assert isinstance(obj, dict)
        artifact_display_name = from_union([from_str, from_none], obj.get("artifactDisplayName"))
        end_date = from_union([from_datetime, from_none], obj.get("endDate"))
        frequency = from_union([from_str, from_none], obj.get("frequency"))
        id = from_union([from_str, from_none], obj.get("id"))
        start_date = from_union([from_datetime, from_none], obj.get("startDate"))
        sub_artifact_display_name = from_union([from_str, from_none], obj.get("subArtifactDisplayName"))
        title = from_union([from_str, from_none], obj.get("title"))
        users = from_union([lambda x: from_list(PowerBISubscriptionUser.from_dict, x), from_none], obj.get("users"))
        return PowerBISubscription(artifact_display_name, end_date, frequency, id, start_date, sub_artifact_display_name, title, users)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.artifact_display_name is not None:
            result["artifactDisplayName"] = from_union([from_str, from_none], self.artifact_display_name)
        if self.end_date is not None:
            result["endDate"] = from_union([lambda x: x.isoformat(), from_none], self.end_date)
        if self.frequency is not None:
            result["frequency"] = from_union([from_str, from_none], self.frequency)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.start_date is not None:
            result["startDate"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        if self.sub_artifact_display_name is not None:
            result["subArtifactDisplayName"] = from_union([from_str, from_none], self.sub_artifact_display_name)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.users is not None:
            result["users"] = from_union([lambda x: from_list(lambda x: to_class(PowerBISubscriptionUser, x), x), from_none], self.users)
        return result


@dataclass
class PowerBIInfo:
    app: Optional[PowerBIApp] = None
    created_by: Optional[str] = None
    created_date_time: Optional[datetime] = None
    endorsement: Optional[PowerBIEndorsement] = None
    modified_by: Optional[str] = None
    modified_date_time: Optional[datetime] = None
    power_bi_dashboard_type: Optional[PowerBIDashboardType] = None
    sensitivity_label: Optional[PowerBISensitivityLabel] = None
    subscriptions: Optional[List[PowerBISubscription]] = None
    workspace_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIInfo':
        assert isinstance(obj, dict)
        app = from_union([PowerBIApp.from_dict, from_none], obj.get("app"))
        created_by = from_union([from_str, from_none], obj.get("createdBy"))
        created_date_time = from_union([from_datetime, from_none], obj.get("createdDateTime"))
        endorsement = from_union([PowerBIEndorsement.from_dict, from_none], obj.get("endorsement"))
        modified_by = from_union([from_str, from_none], obj.get("modifiedBy"))
        modified_date_time = from_union([from_datetime, from_none], obj.get("modifiedDateTime"))
        power_bi_dashboard_type = from_union([PowerBIDashboardType, from_none], obj.get("powerBiDashboardType"))
        sensitivity_label = from_union([PowerBISensitivityLabel.from_dict, from_none], obj.get("sensitivityLabel"))
        subscriptions = from_union([lambda x: from_list(PowerBISubscription.from_dict, x), from_none], obj.get("subscriptions"))
        workspace_id = from_union([from_str, from_none], obj.get("workspaceId"))
        return PowerBIInfo(app, created_by, created_date_time, endorsement, modified_by, modified_date_time, power_bi_dashboard_type, sensitivity_label, subscriptions, workspace_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.app is not None:
            result["app"] = from_union([lambda x: to_class(PowerBIApp, x), from_none], self.app)
        if self.created_by is not None:
            result["createdBy"] = from_union([from_str, from_none], self.created_by)
        if self.created_date_time is not None:
            result["createdDateTime"] = from_union([lambda x: x.isoformat(), from_none], self.created_date_time)
        if self.endorsement is not None:
            result["endorsement"] = from_union([lambda x: to_class(PowerBIEndorsement, x), from_none], self.endorsement)
        if self.modified_by is not None:
            result["modifiedBy"] = from_union([from_str, from_none], self.modified_by)
        if self.modified_date_time is not None:
            result["modifiedDateTime"] = from_union([lambda x: x.isoformat(), from_none], self.modified_date_time)
        if self.power_bi_dashboard_type is not None:
            result["powerBiDashboardType"] = from_union([lambda x: to_enum(PowerBIDashboardType, x), from_none], self.power_bi_dashboard_type)
        if self.sensitivity_label is not None:
            result["sensitivityLabel"] = from_union([lambda x: to_class(PowerBISensitivityLabel, x), from_none], self.sensitivity_label)
        if self.subscriptions is not None:
            result["subscriptions"] = from_union([lambda x: from_list(lambda x: to_class(PowerBISubscription, x), x), from_none], self.subscriptions)
        if self.workspace_id is not None:
            result["workspaceId"] = from_union([from_str, from_none], self.workspace_id)
        return result


class ThoughtSpotDashboardType(Enum):
    """Deprecated this subtype"""

    ANSWER = "ANSWER"
    LIVEBOARD = "LIVEBOARD"
    UNKNOWN = "UNKNOWN"


@dataclass
class ThoughtSpotInfo:
    embed_url: Optional[str] = None
    type: Optional[ThoughtSpotDashboardType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThoughtSpotInfo':
        assert isinstance(obj, dict)
        embed_url = from_union([from_str, from_none], obj.get("embedUrl"))
        type = from_union([ThoughtSpotDashboardType, from_none], obj.get("type"))
        return ThoughtSpotInfo(embed_url, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.embed_url is not None:
            result["embedUrl"] = from_union([from_str, from_none], self.embed_url)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(ThoughtSpotDashboardType, x), from_none], self.type)
        return result


@dataclass
class DashboardInfo:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    charts: Optional[List[Chart]] = None
    dashboard_info_created_at: Optional[datetime] = None
    dashboard_type: Optional[DashboardType] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    power_bi: Optional[PowerBIInfo] = None
    thought_spot: Optional[ThoughtSpotInfo] = None
    title: Optional[str] = None
    view_count: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DashboardInfo':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        charts = from_union([lambda x: from_list(Chart.from_dict, x), from_none], obj.get("charts"))
        dashboard_info_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        dashboard_type = from_union([DashboardType, from_none], obj.get("dashboardType"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        power_bi = from_union([PowerBIInfo.from_dict, from_none], obj.get("powerBi"))
        thought_spot = from_union([ThoughtSpotInfo.from_dict, from_none], obj.get("thoughtSpot"))
        title = from_union([from_str, from_none], obj.get("title"))
        view_count = from_union([from_float, from_none], obj.get("viewCount"))
        return DashboardInfo(created_at, aspect_type, charts, dashboard_info_created_at, dashboard_type, description, entity_id, id, power_bi, thought_spot, title, view_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.charts is not None:
            result["charts"] = from_union([lambda x: from_list(lambda x: to_class(Chart, x), x), from_none], self.charts)
        if self.dashboard_info_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dashboard_info_created_at)
        if self.dashboard_type is not None:
            result["dashboardType"] = from_union([lambda x: to_enum(DashboardType, x), from_none], self.dashboard_type)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.power_bi is not None:
            result["powerBi"] = from_union([lambda x: to_class(PowerBIInfo, x), from_none], self.power_bi)
        if self.thought_spot is not None:
            result["thoughtSpot"] = from_union([lambda x: to_class(ThoughtSpotInfo, x), from_none], self.thought_spot)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.view_count is not None:
            result["viewCount"] = from_union([to_float, from_none], self.view_count)
        return result


class DataMonitorSeverity(Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"


class DataMonitorStatus(Enum):
    ERROR = "ERROR"
    PASSED = "PASSED"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"


@dataclass
class DataMonitorTarget:
    column: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    dataset: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataMonitorTarget':
        assert isinstance(obj, dict)
        column = from_union([from_str, from_none], obj.get("column"))
        dataset = from_union([from_str, from_none], obj.get("dataset"))
        return DataMonitorTarget(column, dataset)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.column is not None:
            result["column"] = from_union([from_str, from_none], self.column)
        if self.dataset is not None:
            result["dataset"] = from_union([from_str, from_none], self.dataset)
        return result


@dataclass
class DataMonitor:
    description: Optional[str] = None
    exceptions: Optional[List[str]] = None
    last_run: Optional[datetime] = None
    owner: Optional[str] = None
    severity: Optional[DataMonitorSeverity] = None
    status: Optional[DataMonitorStatus] = None
    targets: Optional[List[DataMonitorTarget]] = None
    title: Optional[str] = None
    url: Optional[str] = None
    value: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataMonitor':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        exceptions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("exceptions"))
        last_run = from_union([from_datetime, from_none], obj.get("lastRun"))
        owner = from_union([from_str, from_none], obj.get("owner"))
        severity = from_union([DataMonitorSeverity, from_none], obj.get("severity"))
        status = from_union([DataMonitorStatus, from_none], obj.get("status"))
        targets = from_union([lambda x: from_list(DataMonitorTarget.from_dict, x), from_none], obj.get("targets"))
        title = from_union([from_str, from_none], obj.get("title"))
        url = from_union([from_str, from_none], obj.get("url"))
        value = from_union([from_float, from_none], obj.get("value"))
        return DataMonitor(description, exceptions, last_run, owner, severity, status, targets, title, url, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.exceptions is not None:
            result["exceptions"] = from_union([lambda x: from_list(from_str, x), from_none], self.exceptions)
        if self.last_run is not None:
            result["lastRun"] = from_union([lambda x: x.isoformat(), from_none], self.last_run)
        if self.owner is not None:
            result["owner"] = from_union([from_str, from_none], self.owner)
        if self.severity is not None:
            result["severity"] = from_union([lambda x: to_enum(DataMonitorSeverity, x), from_none], self.severity)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(DataMonitorStatus, x), from_none], self.status)
        if self.targets is not None:
            result["targets"] = from_union([lambda x: from_list(lambda x: to_class(DataMonitorTarget, x), x), from_none], self.targets)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.value is not None:
            result["value"] = from_union([to_float, from_none], self.value)
        return result


class DataQualityProvider(Enum):
    BIGEYE = "BIGEYE"
    DBT = "DBT"
    LIGHTUP = "LIGHTUP"
    MONTE_CARLO = "MONTE_CARLO"
    SODA = "SODA"
    UNKNOWN = "UNKNOWN"


@dataclass
class DatasetDataQuality:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dataset_data_quality_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    monitors: Optional[List[DataMonitor]] = None
    provider: Optional[DataQualityProvider] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetDataQuality':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dataset_data_quality_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        monitors = from_union([lambda x: from_list(DataMonitor.from_dict, x), from_none], obj.get("monitors"))
        provider = from_union([DataQualityProvider, from_none], obj.get("provider"))
        url = from_union([from_str, from_none], obj.get("url"))
        return DatasetDataQuality(created_at, aspect_type, dataset_data_quality_created_at, entity_id, id, monitors, provider, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dataset_data_quality_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_data_quality_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.monitors is not None:
            result["monitors"] = from_union([lambda x: from_list(lambda x: to_class(DataMonitor, x), x), from_none], self.monitors)
        if self.provider is not None:
            result["provider"] = from_union([lambda x: to_enum(DataQualityProvider, x), from_none], self.provider)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class MetricFilter:
    field: Optional[str] = None
    operator: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MetricFilter':
        assert isinstance(obj, dict)
        field = from_union([from_str, from_none], obj.get("field"))
        operator = from_union([from_str, from_none], obj.get("operator"))
        value = from_union([from_str, from_none], obj.get("value"))
        return MetricFilter(field, operator, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        if self.operator is not None:
            result["operator"] = from_union([from_str, from_none], self.operator)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class DbtMetric:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dbt_metric_created_at: Optional[datetime] = None
    description: Optional[str] = None
    dimensions: Optional[List[str]] = None
    entity_id: Optional[str] = None
    filters: Optional[List[MetricFilter]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    label: Optional[str] = None
    package_name: Optional[str] = None
    source_datasets: Optional[List[str]] = None
    source_models: Optional[List[str]] = None
    sql: Optional[str] = None
    time_grains: Optional[List[str]] = None
    timestamp: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DbtMetric':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dbt_metric_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        dimensions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("dimensions"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        filters = from_union([lambda x: from_list(MetricFilter.from_dict, x), from_none], obj.get("filters"))
        id = from_union([from_str, from_none], obj.get("id"))
        label = from_union([from_str, from_none], obj.get("label"))
        package_name = from_union([from_str, from_none], obj.get("packageName"))
        source_datasets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceDatasets"))
        source_models = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceModels"))
        sql = from_union([from_str, from_none], obj.get("sql"))
        time_grains = from_union([lambda x: from_list(from_str, x), from_none], obj.get("timeGrains"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        type = from_union([from_str, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        return DbtMetric(created_at, aspect_type, dbt_metric_created_at, description, dimensions, entity_id, filters, id, label, package_name, source_datasets, source_models, sql, time_grains, timestamp, type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dbt_metric_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dbt_metric_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.dimensions is not None:
            result["dimensions"] = from_union([lambda x: from_list(from_str, x), from_none], self.dimensions)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.filters is not None:
            result["filters"] = from_union([lambda x: from_list(lambda x: to_class(MetricFilter, x), x), from_none], self.filters)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.label is not None:
            result["label"] = from_union([from_str, from_none], self.label)
        if self.package_name is not None:
            result["packageName"] = from_union([from_str, from_none], self.package_name)
        if self.source_datasets is not None:
            result["sourceDatasets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_datasets)
        if self.source_models is not None:
            result["sourceModels"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_models)
        if self.sql is not None:
            result["sql"] = from_union([from_str, from_none], self.sql)
        if self.time_grains is not None:
            result["timeGrains"] = from_union([lambda x: from_list(from_str, x), from_none], self.time_grains)
        if self.timestamp is not None:
            result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class SchemaField:
    description: Optional[str] = None
    field_name: Optional[str] = None
    field_path: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    is_unique: Optional[bool] = None
    max_length: Optional[float] = None
    native_type: Optional[str] = None
    nullable: Optional[bool] = None
    precision: Optional[float] = None
    subfields: Optional[List['SchemaField']] = None
    tags: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SchemaField':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        field_name = from_union([from_str, from_none], obj.get("fieldName"))
        field_path = from_union([from_str, from_none], obj.get("fieldPath"))
        is_unique = from_union([from_bool, from_none], obj.get("isUnique"))
        max_length = from_union([from_float, from_none], obj.get("maxLength"))
        native_type = from_union([from_str, from_none], obj.get("nativeType"))
        nullable = from_union([from_bool, from_none], obj.get("nullable"))
        precision = from_union([from_float, from_none], obj.get("precision"))
        subfields = from_union([lambda x: from_list(SchemaField.from_dict, x), from_none], obj.get("subfields"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tags"))
        return SchemaField(description, field_name, field_path, is_unique, max_length, native_type, nullable, precision, subfields, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.field_name is not None:
            result["fieldName"] = from_union([from_str, from_none], self.field_name)
        if self.field_path is not None:
            result["fieldPath"] = from_union([from_str, from_none], self.field_path)
        if self.is_unique is not None:
            result["isUnique"] = from_union([from_bool, from_none], self.is_unique)
        if self.max_length is not None:
            result["maxLength"] = from_union([to_float, from_none], self.max_length)
        if self.native_type is not None:
            result["nativeType"] = from_union([from_str, from_none], self.native_type)
        if self.nullable is not None:
            result["nullable"] = from_union([from_bool, from_none], self.nullable)
        if self.precision is not None:
            result["precision"] = from_union([to_float, from_none], self.precision)
        if self.subfields is not None:
            result["subfields"] = from_union([lambda x: from_list(lambda x: to_class(SchemaField, x), x), from_none], self.subfields)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        return result


@dataclass
class DbtMacroArgument:
    description: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DbtMacroArgument':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        return DbtMacroArgument(description, name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class DbtMacro:
    arguments: Optional[List[DbtMacroArgument]] = None
    depends_on_macros: Optional[List[str]] = None
    description: Optional[str] = None
    name: Optional[str] = None
    package_name: Optional[str] = None
    sql: Optional[str] = None
    unique_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DbtMacro':
        assert isinstance(obj, dict)
        arguments = from_union([lambda x: from_list(DbtMacroArgument.from_dict, x), from_none], obj.get("arguments"))
        depends_on_macros = from_union([lambda x: from_list(from_str, x), from_none], obj.get("dependsOnMacros"))
        description = from_union([from_str, from_none], obj.get("description"))
        name = from_union([from_str, from_none], obj.get("name"))
        package_name = from_union([from_str, from_none], obj.get("packageName"))
        sql = from_union([from_str, from_none], obj.get("sql"))
        unique_id = from_union([from_str, from_none], obj.get("uniqueId"))
        return DbtMacro(arguments, depends_on_macros, description, name, package_name, sql, unique_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.arguments is not None:
            result["arguments"] = from_union([lambda x: from_list(lambda x: to_class(DbtMacroArgument, x), x), from_none], self.arguments)
        if self.depends_on_macros is not None:
            result["dependsOnMacros"] = from_union([lambda x: from_list(from_str, x), from_none], self.depends_on_macros)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.package_name is not None:
            result["packageName"] = from_union([from_str, from_none], self.package_name)
        if self.sql is not None:
            result["sql"] = from_union([from_str, from_none], self.sql)
        if self.unique_id is not None:
            result["uniqueId"] = from_union([from_str, from_none], self.unique_id)
        return result


class DbtMaterializationType(Enum):
    EPHEMERAL = "EPHEMERAL"
    INCREMENTAL = "INCREMENTAL"
    OTHER = "OTHER"
    SNAPSHOT = "SNAPSHOT"
    TABLE = "TABLE"
    VIEW = "VIEW"


@dataclass
class DbtMaterialization:
    target_dataset: Optional[str] = None
    type: Optional[DbtMaterializationType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DbtMaterialization':
        assert isinstance(obj, dict)
        target_dataset = from_union([from_str, from_none], obj.get("targetDataset"))
        type = from_union([DbtMaterializationType, from_none], obj.get("type"))
        return DbtMaterialization(target_dataset, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.target_dataset is not None:
            result["targetDataset"] = from_union([from_str, from_none], self.target_dataset)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(DbtMaterializationType, x), from_none], self.type)
        return result


@dataclass
class DbtMetadataItem:
    """A single key-value pair entry for dbt metadata
    See https://docs.getdbt.com/reference/resource-configs/meta
    """
    key: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DbtMetadataItem':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([from_str, from_none], obj.get("value"))
        return DbtMetadataItem(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class DbtTest:
    columns: Optional[List[str]] = None
    depends_on_macros: Optional[List[str]] = None
    name: Optional[str] = None
    sql: Optional[str] = None
    unique_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DbtTest':
        assert isinstance(obj, dict)
        columns = from_union([lambda x: from_list(from_str, x), from_none], obj.get("columns"))
        depends_on_macros = from_union([lambda x: from_list(from_str, x), from_none], obj.get("dependsOnMacros"))
        name = from_union([from_str, from_none], obj.get("name"))
        sql = from_union([from_str, from_none], obj.get("sql"))
        unique_id = from_union([from_str, from_none], obj.get("uniqueId"))
        return DbtTest(columns, depends_on_macros, name, sql, unique_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.columns is not None:
            result["columns"] = from_union([lambda x: from_list(from_str, x), from_none], self.columns)
        if self.depends_on_macros is not None:
            result["dependsOnMacros"] = from_union([lambda x: from_list(from_str, x), from_none], self.depends_on_macros)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.sql is not None:
            result["sql"] = from_union([from_str, from_none], self.sql)
        if self.unique_id is not None:
            result["uniqueId"] = from_union([from_str, from_none], self.unique_id)
        return result


@dataclass
class DbtModel:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    compiled_sql: Optional[str] = None
    dbt_model_created_at: Optional[datetime] = None
    description: Optional[str] = None
    docs_url: Optional[str] = None
    entity_id: Optional[str] = None
    fields: Optional[List[SchemaField]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    macros: Optional[List[DbtMacro]] = None
    materialization: Optional[DbtMaterialization] = None
    meta: Optional[List[DbtMetadataItem]] = None
    owners: Optional[List[str]] = None
    package_name: Optional[str] = None
    raw_sql: Optional[str] = None
    source_datasets: Optional[List[str]] = None
    source_models: Optional[List[str]] = None
    tests: Optional[List[DbtTest]] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DbtModel':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        compiled_sql = from_union([from_str, from_none], obj.get("compiledSql"))
        dbt_model_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        docs_url = from_union([from_str, from_none], obj.get("docsUrl"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        fields = from_union([lambda x: from_list(SchemaField.from_dict, x), from_none], obj.get("fields"))
        id = from_union([from_str, from_none], obj.get("id"))
        macros = from_union([lambda x: from_list(DbtMacro.from_dict, x), from_none], obj.get("macros"))
        materialization = from_union([DbtMaterialization.from_dict, from_none], obj.get("materialization"))
        meta = from_union([lambda x: from_list(DbtMetadataItem.from_dict, x), from_none], obj.get("meta"))
        owners = from_union([lambda x: from_list(from_str, x), from_none], obj.get("owners"))
        package_name = from_union([from_str, from_none], obj.get("packageName"))
        raw_sql = from_union([from_str, from_none], obj.get("rawSql"))
        source_datasets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceDatasets"))
        source_models = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceModels"))
        tests = from_union([lambda x: from_list(DbtTest.from_dict, x), from_none], obj.get("tests"))
        url = from_union([from_str, from_none], obj.get("url"))
        return DbtModel(created_at, aspect_type, compiled_sql, dbt_model_created_at, description, docs_url, entity_id, fields, id, macros, materialization, meta, owners, package_name, raw_sql, source_datasets, source_models, tests, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.compiled_sql is not None:
            result["compiledSql"] = from_union([from_str, from_none], self.compiled_sql)
        if self.dbt_model_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dbt_model_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.docs_url is not None:
            result["docsUrl"] = from_union([from_str, from_none], self.docs_url)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.fields is not None:
            result["fields"] = from_union([lambda x: from_list(lambda x: to_class(SchemaField, x), x), from_none], self.fields)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.macros is not None:
            result["macros"] = from_union([lambda x: from_list(lambda x: to_class(DbtMacro, x), x), from_none], self.macros)
        if self.materialization is not None:
            result["materialization"] = from_union([lambda x: to_class(DbtMaterialization, x), from_none], self.materialization)
        if self.meta is not None:
            result["meta"] = from_union([lambda x: from_list(lambda x: to_class(DbtMetadataItem, x), x), from_none], self.meta)
        if self.owners is not None:
            result["owners"] = from_union([lambda x: from_list(from_str, x), from_none], self.owners)
        if self.package_name is not None:
            result["packageName"] = from_union([from_str, from_none], self.package_name)
        if self.raw_sql is not None:
            result["rawSql"] = from_union([from_str, from_none], self.raw_sql)
        if self.source_datasets is not None:
            result["sourceDatasets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_datasets)
        if self.source_models is not None:
            result["sourceModels"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_models)
        if self.tests is not None:
            result["tests"] = from_union([lambda x: from_list(lambda x: to_class(DbtTest, x), x), from_none], self.tests)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class AssetDescription:
    author: Optional[str] = None
    description: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AssetDescription':
        assert isinstance(obj, dict)
        author = from_union([from_str, from_none], obj.get("author"))
        description = from_union([from_str, from_none], obj.get("description"))
        return AssetDescription(author, description)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.author is not None:
            result["author"] = from_union([from_str, from_none], self.author)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        return result


@dataclass
class ColumnDescriptionAssignment:
    asset_descriptions: Optional[List[AssetDescription]] = None
    column_name: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    @staticmethod
    def from_dict(obj: Any) -> 'ColumnDescriptionAssignment':
        assert isinstance(obj, dict)
        asset_descriptions = from_union([lambda x: from_list(AssetDescription.from_dict, x), from_none], obj.get("assetDescriptions"))
        column_name = from_union([from_str, from_none], obj.get("columnName"))
        return ColumnDescriptionAssignment(asset_descriptions, column_name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.asset_descriptions is not None:
            result["assetDescriptions"] = from_union([lambda x: from_list(lambda x: to_class(AssetDescription, x), x), from_none], self.asset_descriptions)
        if self.column_name is not None:
            result["columnName"] = from_union([from_str, from_none], self.column_name)
        return result


@dataclass
class DescriptionAssignment:
    asset_descriptions: Optional[List[AssetDescription]] = None
    column_description_assignments: Optional[List[ColumnDescriptionAssignment]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DescriptionAssignment':
        assert isinstance(obj, dict)
        asset_descriptions = from_union([lambda x: from_list(AssetDescription.from_dict, x), from_none], obj.get("assetDescriptions"))
        column_description_assignments = from_union([lambda x: from_list(ColumnDescriptionAssignment.from_dict, x), from_none], obj.get("columnDescriptionAssignments"))
        return DescriptionAssignment(asset_descriptions, column_description_assignments)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.asset_descriptions is not None:
            result["assetDescriptions"] = from_union([lambda x: from_list(lambda x: to_class(AssetDescription, x), x), from_none], self.asset_descriptions)
        if self.column_description_assignments is not None:
            result["columnDescriptionAssignments"] = from_union([lambda x: from_list(lambda x: to_class(ColumnDescriptionAssignment, x), x), from_none], self.column_description_assignments)
        return result


@dataclass
class FieldDocumentation:
    documentation: Optional[str] = None
    field_path: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    tests: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FieldDocumentation':
        assert isinstance(obj, dict)
        documentation = from_union([from_str, from_none], obj.get("documentation"))
        field_path = from_union([from_str, from_none], obj.get("fieldPath"))
        tests = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tests"))
        return FieldDocumentation(documentation, field_path, tests)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.documentation is not None:
            result["documentation"] = from_union([from_str, from_none], self.documentation)
        if self.field_path is not None:
            result["fieldPath"] = from_union([from_str, from_none], self.field_path)
        if self.tests is not None:
            result["tests"] = from_union([lambda x: from_list(from_str, x), from_none], self.tests)
        return result


@dataclass
class DatasetDocumentation:
    """Captures dataset documentations from other tools outside the data source, e.g. dbt
    documentation on source datasets
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dataset_documentation_created_at: Optional[datetime] = None
    dataset_documentations: Optional[List[str]] = None
    entity_id: Optional[str] = None
    field_documentations: Optional[List[FieldDocumentation]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetDocumentation':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dataset_documentation_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        dataset_documentations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("datasetDocumentations"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        field_documentations = from_union([lambda x: from_list(FieldDocumentation.from_dict, x), from_none], obj.get("fieldDocumentations"))
        id = from_union([from_str, from_none], obj.get("id"))
        return DatasetDocumentation(created_at, aspect_type, dataset_documentation_created_at, dataset_documentations, entity_id, field_documentations, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dataset_documentation_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_documentation_created_at)
        if self.dataset_documentations is not None:
            result["datasetDocumentations"] = from_union([lambda x: from_list(from_str, x), from_none], self.dataset_documentations)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.field_documentations is not None:
            result["fieldDocumentations"] = from_union([lambda x: from_list(lambda x: to_class(FieldDocumentation, x), x), from_none], self.field_documentations)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


class EntityType(Enum):
    API = "API"
    DASHBOARD = "DASHBOARD"
    DATASET = "DATASET"
    GROUP = "GROUP"
    HIERARCHY = "HIERARCHY"
    KNOWLEDGE_CARD = "KNOWLEDGE_CARD"
    METRIC = "METRIC"
    NAMESPACE = "NAMESPACE"
    PERSON = "PERSON"
    PIPELINE = "PIPELINE"
    USER_DEFINED_RESOURCE = "USER_DEFINED_RESOURCE"
    VIRTUAL_VIEW = "VIRTUAL_VIEW"


@dataclass
class DatasetLogicalID:
    """Identify an entity "logically".
    Each entity must have a logicalId to be ingested.
    A compelling use-case is that this allows a producer to create an
    instance of the Entity without requiring an entity ID to be
    obtained prior to instantiation, potentially resulting in two round-trips
    """
    account: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[DataPlatform] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetLogicalID':
        assert isinstance(obj, dict)
        account = from_union([from_str, from_none], obj.get("account"))
        name = from_union([from_str, from_none], obj.get("name"))
        platform = from_union([DataPlatform, from_none], obj.get("platform"))
        return DatasetLogicalID(account, name, platform)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account is not None:
            result["account"] = from_union([from_str, from_none], self.account)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.platform is not None:
            result["platform"] = from_union([lambda x: to_enum(DataPlatform, x), from_none], self.platform)
        return result


@dataclass
class SourceField:
    dataset: Optional[DatasetLogicalID] = None
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    source_entity_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SourceField':
        assert isinstance(obj, dict)
        dataset = from_union([DatasetLogicalID.from_dict, from_none], obj.get("dataset"))
        field = from_union([from_str, from_none], obj.get("field"))
        source_entity_id = from_union([from_str, from_none], obj.get("sourceEntityId"))
        return SourceField(dataset, field, source_entity_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.dataset is not None:
            result["dataset"] = from_union([lambda x: to_class(DatasetLogicalID, x), from_none], self.dataset)
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        if self.source_entity_id is not None:
            result["sourceEntityId"] = from_union([from_str, from_none], self.source_entity_id)
        return result


@dataclass
class FieldMapping:
    destination: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    sources: Optional[List[SourceField]] = None
    transformation: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FieldMapping':
        assert isinstance(obj, dict)
        destination = from_union([from_str, from_none], obj.get("destination"))
        sources = from_union([lambda x: from_list(SourceField.from_dict, x), from_none], obj.get("sources"))
        transformation = from_union([from_str, from_none], obj.get("transformation"))
        return FieldMapping(destination, sources, transformation)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.destination is not None:
            result["destination"] = from_union([from_str, from_none], self.destination)
        if self.sources is not None:
            result["sources"] = from_union([lambda x: from_list(lambda x: to_class(SourceField, x), x), from_none], self.sources)
        if self.transformation is not None:
            result["transformation"] = from_union([from_str, from_none], self.transformation)
        return result


@dataclass
class EntityUpstream:
    """EntityUpstream captures upstream lineages from data sources to this entity"""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    entity_upstream_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    executor_url: Optional[str] = None
    field_mappings: Optional[List[FieldMapping]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    source_code_url: Optional[str] = None
    source_entities: Optional[List[str]] = None
    transformation: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EntityUpstream':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        entity_upstream_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        executor_url = from_union([from_str, from_none], obj.get("executorUrl"))
        field_mappings = from_union([lambda x: from_list(FieldMapping.from_dict, x), from_none], obj.get("fieldMappings"))
        id = from_union([from_str, from_none], obj.get("id"))
        source_code_url = from_union([from_str, from_none], obj.get("sourceCodeUrl"))
        source_entities = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceEntities"))
        transformation = from_union([from_str, from_none], obj.get("transformation"))
        return EntityUpstream(created_at, aspect_type, entity_upstream_created_at, entity_id, executor_url, field_mappings, id, source_code_url, source_entities, transformation)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.entity_upstream_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.entity_upstream_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.executor_url is not None:
            result["executorUrl"] = from_union([from_str, from_none], self.executor_url)
        if self.field_mappings is not None:
            result["fieldMappings"] = from_union([lambda x: from_list(lambda x: to_class(FieldMapping, x), x), from_none], self.field_mappings)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.source_code_url is not None:
            result["sourceCodeUrl"] = from_union([from_str, from_none], self.source_code_url)
        if self.source_entities is not None:
            result["sourceEntities"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_entities)
        if self.transformation is not None:
            result["transformation"] = from_union([from_str, from_none], self.transformation)
        return result


@dataclass
class FieldTagAssociations:
    field_path: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    governed_tag_ids: Optional[List[str]] = None
    """Stores Entity IDs for the Governed Tags that are associated with this schema field"""

    @staticmethod
    def from_dict(obj: Any) -> 'FieldTagAssociations':
        assert isinstance(obj, dict)
        field_path = from_union([from_str, from_none], obj.get("fieldPath"))
        governed_tag_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("governedTagIds"))
        return FieldTagAssociations(field_path, governed_tag_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field_path is not None:
            result["fieldPath"] = from_union([from_str, from_none], self.field_path)
        if self.governed_tag_ids is not None:
            result["governedTagIds"] = from_union([lambda x: from_list(from_str, x), from_none], self.governed_tag_ids)
        return result


@dataclass
class DatasetFieldAssociations:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    dataset_field_associations_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    governed_tag_fields: Optional[List[FieldTagAssociations]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetFieldAssociations':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        dataset_field_associations_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        governed_tag_fields = from_union([lambda x: from_list(FieldTagAssociations.from_dict, x), from_none], obj.get("governedTagFields"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        return DatasetFieldAssociations(created_at, aspect_type, created, dataset_field_associations_created_at, entity_id, governed_tag_fields, id, last_modified)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.dataset_field_associations_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_field_associations_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.governed_tag_fields is not None:
            result["governedTagFields"] = from_union([lambda x: from_list(lambda x: to_class(FieldTagAssociations, x), x), from_none], self.governed_tag_fields)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        return result


@dataclass
class FieldStatistics:
    """The statistics of a field/column, e.g. values count, min/max/avg, etc',"""

    average: Optional[float] = None
    distinct_value_count: Optional[float] = None
    field_path: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    max_value: Optional[float] = None
    min_value: Optional[float] = None
    nonnull_value_count: Optional[float] = None
    null_value_count: Optional[float] = None
    std_dev: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FieldStatistics':
        assert isinstance(obj, dict)
        average = from_union([from_float, from_none], obj.get("average"))
        distinct_value_count = from_union([from_float, from_none], obj.get("distinctValueCount"))
        field_path = from_union([from_str, from_none], obj.get("fieldPath"))
        max_value = from_union([from_float, from_none], obj.get("maxValue"))
        min_value = from_union([from_float, from_none], obj.get("minValue"))
        nonnull_value_count = from_union([from_float, from_none], obj.get("nonnullValueCount"))
        null_value_count = from_union([from_float, from_none], obj.get("nullValueCount"))
        std_dev = from_union([from_float, from_none], obj.get("stdDev"))
        return FieldStatistics(average, distinct_value_count, field_path, max_value, min_value, nonnull_value_count, null_value_count, std_dev)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.average is not None:
            result["average"] = from_union([to_float, from_none], self.average)
        if self.distinct_value_count is not None:
            result["distinctValueCount"] = from_union([to_float, from_none], self.distinct_value_count)
        if self.field_path is not None:
            result["fieldPath"] = from_union([from_str, from_none], self.field_path)
        if self.max_value is not None:
            result["maxValue"] = from_union([to_float, from_none], self.max_value)
        if self.min_value is not None:
            result["minValue"] = from_union([to_float, from_none], self.min_value)
        if self.nonnull_value_count is not None:
            result["nonnullValueCount"] = from_union([to_float, from_none], self.nonnull_value_count)
        if self.null_value_count is not None:
            result["nullValueCount"] = from_union([to_float, from_none], self.null_value_count)
        if self.std_dev is not None:
            result["stdDev"] = from_union([to_float, from_none], self.std_dev)
        return result


@dataclass
class DatasetFieldStatistics:
    """DatasetStatistics captures operational information about the dataset, e.g. the number of
    records or the last refresh time.
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dataset_field_statistics_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    field_statistics: Optional[List[FieldStatistics]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetFieldStatistics':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dataset_field_statistics_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        field_statistics = from_union([lambda x: from_list(FieldStatistics.from_dict, x), from_none], obj.get("fieldStatistics"))
        id = from_union([from_str, from_none], obj.get("id"))
        return DatasetFieldStatistics(created_at, aspect_type, dataset_field_statistics_created_at, entity_id, field_statistics, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dataset_field_statistics_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_field_statistics_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.field_statistics is not None:
            result["fieldStatistics"] = from_union([lambda x: from_list(lambda x: to_class(FieldStatistics, x), x), from_none], self.field_statistics)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class FiveTranConnectorStatus:
    setup_state: Optional[str] = None
    sync_state: Optional[str] = None
    update_state: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FiveTranConnectorStatus':
        assert isinstance(obj, dict)
        setup_state = from_union([from_str, from_none], obj.get("setupState"))
        sync_state = from_union([from_str, from_none], obj.get("syncState"))
        update_state = from_union([from_str, from_none], obj.get("updateState"))
        return FiveTranConnectorStatus(setup_state, sync_state, update_state)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.setup_state is not None:
            result["setupState"] = from_union([from_str, from_none], self.setup_state)
        if self.sync_state is not None:
            result["syncState"] = from_union([from_str, from_none], self.sync_state)
        if self.update_state is not None:
            result["updateState"] = from_union([from_str, from_none], self.update_state)
        return result


@dataclass
class FivetranPipeline:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    config: Optional[str] = None
    connector_logs_url: Optional[str] = None
    connector_name: Optional[str] = None
    connector_type_id: Optional[str] = None
    connector_type_name: Optional[str] = None
    connector_url: Optional[str] = None
    created: Optional[datetime] = None
    fivetran_pipeline_created_at: Optional[datetime] = None
    creator_email: Optional[str] = None
    entity_id: Optional[str] = None
    icon_url: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_succeeded: Optional[datetime] = None
    paused: Optional[bool] = None
    schema_metadata: Optional[str] = None
    sources: Optional[List[str]] = None
    status: Optional[FiveTranConnectorStatus] = None
    sync_interval_in_minute: Optional[float] = None
    targets: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FivetranPipeline':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        config = from_union([from_str, from_none], obj.get("config"))
        connector_logs_url = from_union([from_str, from_none], obj.get("connectorLogsUrl"))
        connector_name = from_union([from_str, from_none], obj.get("connectorName"))
        connector_type_id = from_union([from_str, from_none], obj.get("connectorTypeId"))
        connector_type_name = from_union([from_str, from_none], obj.get("connectorTypeName"))
        connector_url = from_union([from_str, from_none], obj.get("connectorUrl"))
        created = from_union([from_datetime, from_none], obj.get("created"))
        fivetran_pipeline_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        creator_email = from_union([from_str, from_none], obj.get("creatorEmail"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        icon_url = from_union([from_str, from_none], obj.get("iconUrl"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_succeeded = from_union([from_datetime, from_none], obj.get("lastSucceeded"))
        paused = from_union([from_bool, from_none], obj.get("paused"))
        schema_metadata = from_union([from_str, from_none], obj.get("schemaMetadata"))
        sources = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sources"))
        status = from_union([FiveTranConnectorStatus.from_dict, from_none], obj.get("status"))
        sync_interval_in_minute = from_union([from_float, from_none], obj.get("syncIntervalInMinute"))
        targets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("targets"))
        return FivetranPipeline(created_at, aspect_type, config, connector_logs_url, connector_name, connector_type_id, connector_type_name, connector_url, created, fivetran_pipeline_created_at, creator_email, entity_id, icon_url, id, last_succeeded, paused, schema_metadata, sources, status, sync_interval_in_minute, targets)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.config is not None:
            result["config"] = from_union([from_str, from_none], self.config)
        if self.connector_logs_url is not None:
            result["connectorLogsUrl"] = from_union([from_str, from_none], self.connector_logs_url)
        if self.connector_name is not None:
            result["connectorName"] = from_union([from_str, from_none], self.connector_name)
        if self.connector_type_id is not None:
            result["connectorTypeId"] = from_union([from_str, from_none], self.connector_type_id)
        if self.connector_type_name is not None:
            result["connectorTypeName"] = from_union([from_str, from_none], self.connector_type_name)
        if self.connector_url is not None:
            result["connectorUrl"] = from_union([from_str, from_none], self.connector_url)
        if self.created is not None:
            result["created"] = from_union([lambda x: x.isoformat(), from_none], self.created)
        if self.fivetran_pipeline_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.fivetran_pipeline_created_at)
        if self.creator_email is not None:
            result["creatorEmail"] = from_union([from_str, from_none], self.creator_email)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.icon_url is not None:
            result["iconUrl"] = from_union([from_str, from_none], self.icon_url)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_succeeded is not None:
            result["lastSucceeded"] = from_union([lambda x: x.isoformat(), from_none], self.last_succeeded)
        if self.paused is not None:
            result["paused"] = from_union([from_bool, from_none], self.paused)
        if self.schema_metadata is not None:
            result["schemaMetadata"] = from_union([from_str, from_none], self.schema_metadata)
        if self.sources is not None:
            result["sources"] = from_union([lambda x: from_list(from_str, x), from_none], self.sources)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_class(FiveTranConnectorStatus, x), from_none], self.status)
        if self.sync_interval_in_minute is not None:
            result["syncIntervalInMinute"] = from_union([to_float, from_none], self.sync_interval_in_minute)
        if self.targets is not None:
            result["targets"] = from_union([lambda x: from_list(from_str, x), from_none], self.targets)
        return result


@dataclass
class MetabaseCollection:
    name: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MetabaseCollection':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        return MetabaseCollection(name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class GroupUserAccessRight(Enum):
    ADMIN = "Admin"
    MEMBER = "Member"
    VIEWER = "Viewer"


@dataclass
class PowerBIWorkspaceUser:
    display_name: Optional[str] = None
    email_address: Optional[str] = None
    group_user_access_right: Optional[GroupUserAccessRight] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIWorkspaceUser':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        email_address = from_union([from_str, from_none], obj.get("emailAddress"))
        group_user_access_right = from_union([GroupUserAccessRight, from_none], obj.get("groupUserAccessRight"))
        return PowerBIWorkspaceUser(display_name, email_address, group_user_access_right)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_name is not None:
            result["displayName"] = from_union([from_str, from_none], self.display_name)
        if self.email_address is not None:
            result["emailAddress"] = from_union([from_str, from_none], self.email_address)
        if self.group_user_access_right is not None:
            result["groupUserAccessRight"] = from_union([lambda x: to_enum(GroupUserAccessRight, x), from_none], self.group_user_access_right)
        return result


@dataclass
class PowerBIWorkspace:
    name: Optional[str] = None
    url: Optional[str] = None
    users: Optional[List[PowerBIWorkspaceUser]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIWorkspace':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        users = from_union([lambda x: from_list(PowerBIWorkspaceUser.from_dict, x), from_none], obj.get("users"))
        return PowerBIWorkspace(name, url, users)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.users is not None:
            result["users"] = from_union([lambda x: from_list(lambda x: to_class(PowerBIWorkspaceUser, x), x), from_none], self.users)
        return result


class HierarchyType(Enum):
    LOOKER_FOLDER = "LOOKER_FOLDER"
    METABASE_COLLECTION = "METABASE_COLLECTION"
    POWER_BI_WORKSPACE = "POWER_BI_WORKSPACE"
    THOUGHT_SPOT_VIRTUAL_HIERARCHY = "THOUGHT_SPOT_VIRTUAL_HIERARCHY"
    UNKNOWN = "UNKNOWN"
    VIRTUAL_HIERARCHY = "VIRTUAL_HIERARCHY"


@dataclass
class HierarchyInfo:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    hierarchy_info_created_at: Optional[datetime] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    metabase_collection: Optional[MetabaseCollection] = None
    name: Optional[str] = None
    power_bi_workspace: Optional[PowerBIWorkspace] = None
    type: Optional[HierarchyType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HierarchyInfo':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        hierarchy_info_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        metabase_collection = from_union([MetabaseCollection.from_dict, from_none], obj.get("metabaseCollection"))
        name = from_union([from_str, from_none], obj.get("name"))
        power_bi_workspace = from_union([PowerBIWorkspace.from_dict, from_none], obj.get("powerBiWorkspace"))
        type = from_union([HierarchyType, from_none], obj.get("type"))
        return HierarchyInfo(created_at, aspect_type, hierarchy_info_created_at, description, entity_id, id, metabase_collection, name, power_bi_workspace, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.hierarchy_info_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.hierarchy_info_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.metabase_collection is not None:
            result["metabaseCollection"] = from_union([lambda x: to_class(MetabaseCollection, x), from_none], self.metabase_collection)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.power_bi_workspace is not None:
            result["powerBiWorkspace"] = from_union([lambda x: to_class(PowerBIWorkspace, x), from_none], self.power_bi_workspace)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(HierarchyType, x), from_none], self.type)
        return result


class Bsontype(Enum):
    OBJECT_ID = "ObjectId"


class Species18106___ToStringTag8530(Enum):
    SHARED_ARRAY_BUFFER = "SharedArrayBuffer"


@dataclass
class SharedArrayBuffer:
    species_18106: Optional['SharedArrayBuffer'] = None
    to_string_tag_8530: Optional[Species18106___ToStringTag8530] = None
    byte_length: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SharedArrayBuffer':
        assert isinstance(obj, dict)
        species_18106 = from_union([SharedArrayBuffer.from_dict, from_none], obj.get("__@species@18106"))
        to_string_tag_8530 = from_union([Species18106___ToStringTag8530, from_none], obj.get("__@toStringTag@8530"))
        byte_length = from_union([from_float, from_none], obj.get("byteLength"))
        return SharedArrayBuffer(species_18106, to_string_tag_8530, byte_length)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.species_18106 is not None:
            result["__@species@18106"] = from_union([lambda x: to_class(SharedArrayBuffer, x), from_none], self.species_18106)
        if self.to_string_tag_8530 is not None:
            result["__@toStringTag@8530"] = from_union([lambda x: to_enum(Species18106___ToStringTag8530, x), from_none], self.to_string_tag_8530)
        if self.byte_length is not None:
            result["byteLength"] = from_union([to_float, from_none], self.byte_length)
        return result


@dataclass
class ArrayBufferLike:
    to_string_tag_8530: Optional[str] = None
    byte_length: Optional[float] = None
    species_18106: Optional[SharedArrayBuffer] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ArrayBufferLike':
        assert isinstance(obj, dict)
        to_string_tag_8530 = from_union([from_str, from_none], obj.get("__@toStringTag@8530"))
        byte_length = from_union([from_float, from_none], obj.get("byteLength"))
        species_18106 = from_union([SharedArrayBuffer.from_dict, from_none], obj.get("__@species@18106"))
        return ArrayBufferLike(to_string_tag_8530, byte_length, species_18106)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.to_string_tag_8530 is not None:
            result["__@toStringTag@8530"] = from_union([from_str, from_none], self.to_string_tag_8530)
        if self.byte_length is not None:
            result["byteLength"] = from_union([to_float, from_none], self.byte_length)
        if self.species_18106 is not None:
            result["__@species@18106"] = from_union([lambda x: to_class(SharedArrayBuffer, x), from_none], self.species_18106)
        return result


class IDToStringTag8530(Enum):
    UINT8_ARRAY = "Uint8Array"


@dataclass
class ID:
    """The ObjectId bytes"""

    to_string_tag_8530: Optional[IDToStringTag8530] = None
    buffer: Optional[ArrayBufferLike] = None
    byte_length: Optional[float] = None
    byte_offset: Optional[float] = None
    bytes_per_element: Optional[float] = None
    length: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ID':
        assert isinstance(obj, dict)
        to_string_tag_8530 = from_union([IDToStringTag8530, from_none], obj.get("__@toStringTag@8530"))
        buffer = from_union([ArrayBufferLike.from_dict, from_none], obj.get("buffer"))
        byte_length = from_union([from_float, from_none], obj.get("byteLength"))
        byte_offset = from_union([from_float, from_none], obj.get("byteOffset"))
        bytes_per_element = from_union([from_float, from_none], obj.get("BYTES_PER_ELEMENT"))
        length = from_union([from_float, from_none], obj.get("length"))
        return ID(to_string_tag_8530, buffer, byte_length, byte_offset, bytes_per_element, length)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.to_string_tag_8530 is not None:
            result["__@toStringTag@8530"] = from_union([lambda x: to_enum(IDToStringTag8530, x), from_none], self.to_string_tag_8530)
        if self.buffer is not None:
            result["buffer"] = from_union([lambda x: to_class(ArrayBufferLike, x), from_none], self.buffer)
        if self.byte_length is not None:
            result["byteLength"] = from_union([to_float, from_none], self.byte_length)
        if self.byte_offset is not None:
            result["byteOffset"] = from_union([to_float, from_none], self.byte_offset)
        if self.bytes_per_element is not None:
            result["BYTES_PER_ELEMENT"] = from_union([to_float, from_none], self.bytes_per_element)
        if self.length is not None:
            result["length"] = from_union([to_float, from_none], self.length)
        return result


@dataclass
class ObjectID:
    """Native Mongo db BSON id instance
    
    A class representation of the BSON ObjectId type.
    """
    bsontype: Optional[Bsontype] = None
    id: Optional[ID] = None
    """The ObjectId bytes"""

    @staticmethod
    def from_dict(obj: Any) -> 'ObjectID':
        assert isinstance(obj, dict)
        bsontype = from_union([Bsontype, from_none], obj.get("_bsontype"))
        id = from_union([ID.from_dict, from_none], obj.get("id"))
        return ObjectID(bsontype, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bsontype is not None:
            result["_bsontype"] = from_union([lambda x: to_enum(Bsontype, x), from_none], self.bsontype)
        if self.id is not None:
            result["id"] = from_union([lambda x: to_class(ID, x), from_none], self.id)
        return result


@dataclass
class InformaticaMapping:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    informatica_mapping_created_at: Optional[datetime] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InformaticaMapping':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        informatica_mapping_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return InformaticaMapping(created_at, aspect_type, informatica_mapping_created_at, description, entity_id, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.informatica_mapping_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.informatica_mapping_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class DatasetLastQuery:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dataset_last_query_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_queried_at: Optional[datetime] = None
    last_queried_by: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetLastQuery':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dataset_last_query_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_queried_at = from_union([from_datetime, from_none], obj.get("lastQueriedAt"))
        last_queried_by = from_union([from_str, from_none], obj.get("lastQueriedBy"))
        return DatasetLastQuery(created_at, aspect_type, dataset_last_query_created_at, entity_id, id, last_queried_at, last_queried_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dataset_last_query_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_last_query_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_queried_at is not None:
            result["lastQueriedAt"] = from_union([lambda x: x.isoformat(), from_none], self.last_queried_at)
        if self.last_queried_by is not None:
            result["lastQueriedBy"] = from_union([from_str, from_none], self.last_queried_by)
        return result


class Platform(Enum):
    """The data platform of the upstream dataset"""

    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGQUERY = "BIGQUERY"
    CUSTOM_DASHBOARD = "CUSTOM_DASHBOARD"
    DASH = "DASH"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    GCS = "GCS"
    GLUE = "GLUE"
    HIVE = "HIVE"
    HTTP = "HTTP"
    KAFKA = "KAFKA"
    LOOKER = "LOOKER"
    METABASE = "METABASE"
    MONGODB = "MONGODB"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    OPEN_API = "OPEN_API"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    POWER_BI = "POWER_BI"
    QUICK_SIGHT = "QUICK_SIGHT"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SNOWFLAKE = "SNOWFLAKE"
    SYNAPSE = "SYNAPSE"
    TABLEAU = "TABLEAU"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


class TypeEnum(Enum):
    AIRFLOW = "AIRFLOW"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    DBT_METRIC = "DBT_METRIC"
    DBT_MODEL = "DBT_MODEL"
    FIVETRAN = "FIVETRAN"
    INFORMATICA_MAPPING = "INFORMATICA_MAPPING"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    POWER_BI_DATAFLOW = "POWER_BI_DATAFLOW"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUICK_SIGHT = "QUICK_SIGHT"
    SPARK = "SPARK"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    UNKNOWN = "UNKNOWN"


@dataclass
class APILogicalID:
    """Identify an entity "logically".
    Each entity must have a logicalId to be ingested.
    A compelling use-case is that this allows a producer to create an
    instance of the Entity without requiring an entity ID to be
    obtained prior to instantiation, potentially resulting in two round-trips
    
    Implemented in {@link KnowledgeCard} output type
    Definite assignment assertion is safe since it is defined in output subtype.
    This is due to unresolved TypeScript bug preventing this class from being defined as an
    abstract class, and
    then being used in a mixin {@see https://github.com/microsoft/TypeScript/issues/37142}
    
    Implemented in {@link UserDefinedResource} output type
    Definite assignment operator is used because field is implemented on output type but not
    expected on input type
    """
    platform: Optional[Platform] = None
    url: Optional[str] = None
    dashboard_id: Optional[str] = None
    account: Optional[str] = None
    name: Optional[str] = None
    type: Optional[TypeEnum] = None
    path: Optional[List[str]] = None
    id: Optional[str] = None
    email: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'APILogicalID':
        assert isinstance(obj, dict)
        platform = from_union([Platform, from_none], obj.get("platform"))
        url = from_union([from_str, from_none], obj.get("url"))
        dashboard_id = from_union([from_str, from_none], obj.get("dashboardId"))
        account = from_union([from_str, from_none], obj.get("account"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        path = from_union([lambda x: from_list(from_str, x), from_none], obj.get("path"))
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        return APILogicalID(platform, url, dashboard_id, account, name, type, path, id, email)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.platform is not None:
            result["platform"] = from_union([lambda x: to_enum(Platform, x), from_none], self.platform)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.dashboard_id is not None:
            result["dashboardId"] = from_union([from_str, from_none], self.dashboard_id)
        if self.account is not None:
            result["account"] = from_union([from_str, from_none], self.account)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        if self.path is not None:
            result["path"] = from_union([lambda x: from_list(from_str, x), from_none], self.path)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        return result


@dataclass
class LookerExploreFilter:
    allowed_values: Optional[str] = None
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    @staticmethod
    def from_dict(obj: Any) -> 'LookerExploreFilter':
        assert isinstance(obj, dict)
        allowed_values = from_union([from_str, from_none], obj.get("allowedValues"))
        field = from_union([from_str, from_none], obj.get("field"))
        return LookerExploreFilter(allowed_values, field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.allowed_values is not None:
            result["allowedValues"] = from_union([from_str, from_none], self.allowed_values)
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        return result


@dataclass
class LookerExploreJoin:
    fields: Optional[List[str]] = None
    on_clause: Optional[str] = None
    relationship: Optional[str] = None
    type: Optional[str] = None
    view: Optional[str] = None
    """The Looker View that is joined in the Explore"""

    where_clause: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LookerExploreJoin':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_list(from_str, x), from_none], obj.get("fields"))
        on_clause = from_union([from_str, from_none], obj.get("onClause"))
        relationship = from_union([from_str, from_none], obj.get("relationship"))
        type = from_union([from_str, from_none], obj.get("type"))
        view = from_union([from_str, from_none], obj.get("view"))
        where_clause = from_union([from_str, from_none], obj.get("whereClause"))
        return LookerExploreJoin(fields, on_clause, relationship, type, view, where_clause)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.fields is not None:
            result["fields"] = from_union([lambda x: from_list(from_str, x), from_none], self.fields)
        if self.on_clause is not None:
            result["onClause"] = from_union([from_str, from_none], self.on_clause)
        if self.relationship is not None:
            result["relationship"] = from_union([from_str, from_none], self.relationship)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.view is not None:
            result["view"] = from_union([from_str, from_none], self.view)
        if self.where_clause is not None:
            result["whereClause"] = from_union([from_str, from_none], self.where_clause)
        return result


@dataclass
class LookerExplore:
    """Captures information of a Looker Explore,
    https://docs.looker.com/reference/explore-reference
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    base_view: Optional[str] = None
    """The Looker View which the Explore is based on"""

    looker_explore_created_at: Optional[datetime] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    extends: Optional[List[str]] = None
    fields: Optional[List[str]] = None
    filters: Optional[List[LookerExploreFilter]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    joins: Optional[List[LookerExploreJoin]] = None
    label: Optional[str] = None
    model_name: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LookerExplore':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        base_view = from_union([from_str, from_none], obj.get("baseView"))
        looker_explore_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        extends = from_union([lambda x: from_list(from_str, x), from_none], obj.get("extends"))
        fields = from_union([lambda x: from_list(from_str, x), from_none], obj.get("fields"))
        filters = from_union([lambda x: from_list(LookerExploreFilter.from_dict, x), from_none], obj.get("filters"))
        id = from_union([from_str, from_none], obj.get("id"))
        joins = from_union([lambda x: from_list(LookerExploreJoin.from_dict, x), from_none], obj.get("joins"))
        label = from_union([from_str, from_none], obj.get("label"))
        model_name = from_union([from_str, from_none], obj.get("modelName"))
        url = from_union([from_str, from_none], obj.get("url"))
        return LookerExplore(created_at, aspect_type, base_view, looker_explore_created_at, description, entity_id, extends, fields, filters, id, joins, label, model_name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.base_view is not None:
            result["baseView"] = from_union([from_str, from_none], self.base_view)
        if self.looker_explore_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.looker_explore_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.extends is not None:
            result["extends"] = from_union([lambda x: from_list(from_str, x), from_none], self.extends)
        if self.fields is not None:
            result["fields"] = from_union([lambda x: from_list(from_str, x), from_none], self.fields)
        if self.filters is not None:
            result["filters"] = from_union([lambda x: from_list(lambda x: to_class(LookerExploreFilter, x), x), from_none], self.filters)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.joins is not None:
            result["joins"] = from_union([lambda x: from_list(lambda x: to_class(LookerExploreJoin, x), x), from_none], self.joins)
        if self.label is not None:
            result["label"] = from_union([from_str, from_none], self.label)
        if self.model_name is not None:
            result["modelName"] = from_union([from_str, from_none], self.model_name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class LookerViewDimension:
    data_type: Optional[str] = None
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    @staticmethod
    def from_dict(obj: Any) -> 'LookerViewDimension':
        assert isinstance(obj, dict)
        data_type = from_union([from_str, from_none], obj.get("dataType"))
        field = from_union([from_str, from_none], obj.get("field"))
        return LookerViewDimension(data_type, field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.data_type is not None:
            result["dataType"] = from_union([from_str, from_none], self.data_type)
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        return result


@dataclass
class LookerViewFilter:
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LookerViewFilter':
        assert isinstance(obj, dict)
        field = from_union([from_str, from_none], obj.get("field"))
        type = from_union([from_str, from_none], obj.get("type"))
        return LookerViewFilter(field, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class LookerViewMeasure:
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LookerViewMeasure':
        assert isinstance(obj, dict)
        field = from_union([from_str, from_none], obj.get("field"))
        type = from_union([from_str, from_none], obj.get("type"))
        return LookerViewMeasure(field, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class VirtualViewQuery:
    default_database: Optional[str] = None
    default_schema: Optional[str] = None
    query: Optional[str] = None
    source_dataset_account: Optional[str] = None
    source_platform: Optional[DataPlatform] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VirtualViewQuery':
        assert isinstance(obj, dict)
        default_database = from_union([from_str, from_none], obj.get("defaultDatabase"))
        default_schema = from_union([from_str, from_none], obj.get("defaultSchema"))
        query = from_union([from_str, from_none], obj.get("query"))
        source_dataset_account = from_union([from_str, from_none], obj.get("sourceDatasetAccount"))
        source_platform = from_union([DataPlatform, from_none], obj.get("sourcePlatform"))
        return VirtualViewQuery(default_database, default_schema, query, source_dataset_account, source_platform)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.default_database is not None:
            result["defaultDatabase"] = from_union([from_str, from_none], self.default_database)
        if self.default_schema is not None:
            result["defaultSchema"] = from_union([from_str, from_none], self.default_schema)
        if self.query is not None:
            result["query"] = from_union([from_str, from_none], self.query)
        if self.source_dataset_account is not None:
            result["sourceDatasetAccount"] = from_union([from_str, from_none], self.source_dataset_account)
        if self.source_platform is not None:
            result["sourcePlatform"] = from_union([lambda x: to_enum(DataPlatform, x), from_none], self.source_platform)
        return result


@dataclass
class LookerView:
    """Captures information of a Looker View, https://docs.looker.com/reference/view-reference"""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    looker_view_created_at: Optional[datetime] = None
    dimensions: Optional[List[LookerViewDimension]] = None
    entity_id: Optional[str] = None
    extends: Optional[List[str]] = None
    filters: Optional[List[LookerViewFilter]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    label: Optional[str] = None
    measures: Optional[List[LookerViewMeasure]] = None
    query: Optional[VirtualViewQuery] = None
    source_datasets: Optional[List[str]] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LookerView':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        looker_view_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        dimensions = from_union([lambda x: from_list(LookerViewDimension.from_dict, x), from_none], obj.get("dimensions"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        extends = from_union([lambda x: from_list(from_str, x), from_none], obj.get("extends"))
        filters = from_union([lambda x: from_list(LookerViewFilter.from_dict, x), from_none], obj.get("filters"))
        id = from_union([from_str, from_none], obj.get("id"))
        label = from_union([from_str, from_none], obj.get("label"))
        measures = from_union([lambda x: from_list(LookerViewMeasure.from_dict, x), from_none], obj.get("measures"))
        query = from_union([VirtualViewQuery.from_dict, from_none], obj.get("query"))
        source_datasets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceDatasets"))
        url = from_union([from_str, from_none], obj.get("url"))
        return LookerView(created_at, aspect_type, looker_view_created_at, dimensions, entity_id, extends, filters, id, label, measures, query, source_datasets, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.looker_view_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.looker_view_created_at)
        if self.dimensions is not None:
            result["dimensions"] = from_union([lambda x: from_list(lambda x: to_class(LookerViewDimension, x), x), from_none], self.dimensions)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.extends is not None:
            result["extends"] = from_union([lambda x: from_list(from_str, x), from_none], self.extends)
        if self.filters is not None:
            result["filters"] = from_union([lambda x: from_list(lambda x: to_class(LookerViewFilter, x), x), from_none], self.filters)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.label is not None:
            result["label"] = from_union([from_str, from_none], self.label)
        if self.measures is not None:
            result["measures"] = from_union([lambda x: from_list(lambda x: to_class(LookerViewMeasure, x), x), from_none], self.measures)
        if self.query is not None:
            result["query"] = from_union([lambda x: to_class(VirtualViewQuery, x), from_none], self.query)
        if self.source_datasets is not None:
            result["sourceDatasets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_datasets)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class PersonOrganization:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    person_organization_created_at: Optional[datetime] = None
    department: Optional[str] = None
    division: Optional[str] = None
    employee_number: Optional[str] = None
    entity_id: Optional[str] = None
    groups: Optional[List[str]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    manager: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PersonOrganization':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        person_organization_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        department = from_union([from_str, from_none], obj.get("department"))
        division = from_union([from_str, from_none], obj.get("division"))
        employee_number = from_union([from_str, from_none], obj.get("employeeNumber"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        groups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("groups"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        manager = from_union([from_str, from_none], obj.get("manager"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        return PersonOrganization(created_at, aspect_type, created, person_organization_created_at, department, division, employee_number, entity_id, groups, id, last_modified, manager, name, title)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.person_organization_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.person_organization_created_at)
        if self.department is not None:
            result["department"] = from_union([from_str, from_none], self.department)
        if self.division is not None:
            result["division"] = from_union([from_str, from_none], self.division)
        if self.employee_number is not None:
            result["employeeNumber"] = from_union([from_str, from_none], self.employee_number)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.groups is not None:
            result["groups"] = from_union([lambda x: from_list(from_str, x), from_none], self.groups)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        if self.manager is not None:
            result["manager"] = from_union([from_str, from_none], self.manager)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        return result


@dataclass
class DataQualityStatusSource:
    source_entity: Optional[str] = None
    status: Optional[DataMonitorStatus] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataQualityStatusSource':
        assert isinstance(obj, dict)
        source_entity = from_union([from_str, from_none], obj.get("sourceEntity"))
        status = from_union([DataMonitorStatus, from_none], obj.get("status"))
        return DataQualityStatusSource(source_entity, status)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.source_entity is not None:
            result["sourceEntity"] = from_union([from_str, from_none], self.source_entity)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(DataMonitorStatus, x), from_none], self.status)
        return result


@dataclass
class OverallDataQuality:
    """Overall data quality of entity, it is calculated by it's upstream node.
    Any FAILED, or WARNING status of upstreams will cause the overall data quality WARN
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    computed_at: Optional[datetime] = None
    overall_data_quality_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    status: Optional[DataMonitorStatus] = None
    status_sources: Optional[List[DataQualityStatusSource]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OverallDataQuality':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        computed_at = from_union([from_datetime, from_none], obj.get("computedAt"))
        overall_data_quality_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        status = from_union([DataMonitorStatus, from_none], obj.get("status"))
        status_sources = from_union([lambda x: from_list(DataQualityStatusSource.from_dict, x), from_none], obj.get("statusSources"))
        return OverallDataQuality(created_at, aspect_type, computed_at, overall_data_quality_created_at, entity_id, id, status, status_sources)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.computed_at is not None:
            result["computedAt"] = from_union([lambda x: x.isoformat(), from_none], self.computed_at)
        if self.overall_data_quality_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.overall_data_quality_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(DataMonitorStatus, x), from_none], self.status)
        if self.status_sources is not None:
            result["statusSources"] = from_union([lambda x: from_list(lambda x: to_class(DataQualityStatusSource, x), x), from_none], self.status_sources)
        return result


@dataclass
class Ownership:
    contact_designation_name: Optional[str] = None
    person: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Ownership':
        assert isinstance(obj, dict)
        contact_designation_name = from_union([from_str, from_none], obj.get("contactDesignationName"))
        person = from_union([from_str, from_none], obj.get("person"))
        return Ownership(contact_designation_name, person)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.contact_designation_name is not None:
            result["contactDesignationName"] = from_union([from_str, from_none], self.contact_designation_name)
        if self.person is not None:
            result["person"] = from_union([from_str, from_none], self.person)
        return result


@dataclass
class OwnershipAssignment:
    ownerships: Optional[List[Ownership]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OwnershipAssignment':
        assert isinstance(obj, dict)
        ownerships = from_union([lambda x: from_list(Ownership.from_dict, x), from_none], obj.get("ownerships"))
        return OwnershipAssignment(ownerships)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.ownerships is not None:
            result["ownerships"] = from_union([lambda x: from_list(lambda x: to_class(Ownership, x), x), from_none], self.ownerships)
        return result


class SourceType(Enum):
    LINEAGE_DEFINITION = "LINEAGE_DEFINITION"
    PIPELINE = "PIPELINE"
    QUERY_LOG = "QUERY_LOG"


@dataclass
class ParsedSource:
    field_mappings: Optional[List[FieldMapping]] = None
    last_parsed: Optional[datetime] = None
    query_id: Optional[str] = None
    source_entities: Optional[List[str]] = None
    source_type: Optional[SourceType] = None
    source_unique_id: Optional[str] = None
    transformation: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ParsedSource':
        assert isinstance(obj, dict)
        field_mappings = from_union([lambda x: from_list(FieldMapping.from_dict, x), from_none], obj.get("fieldMappings"))
        last_parsed = from_union([from_datetime, from_none], obj.get("lastParsed"))
        query_id = from_union([from_str, from_none], obj.get("queryId"))
        source_entities = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceEntities"))
        source_type = from_union([SourceType, from_none], obj.get("sourceType"))
        source_unique_id = from_union([from_str, from_none], obj.get("sourceUniqueId"))
        transformation = from_union([from_str, from_none], obj.get("transformation"))
        return ParsedSource(field_mappings, last_parsed, query_id, source_entities, source_type, source_unique_id, transformation)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field_mappings is not None:
            result["fieldMappings"] = from_union([lambda x: from_list(lambda x: to_class(FieldMapping, x), x), from_none], self.field_mappings)
        if self.last_parsed is not None:
            result["lastParsed"] = from_union([lambda x: x.isoformat(), from_none], self.last_parsed)
        if self.query_id is not None:
            result["queryId"] = from_union([from_str, from_none], self.query_id)
        if self.source_entities is not None:
            result["sourceEntities"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_entities)
        if self.source_type is not None:
            result["sourceType"] = from_union([lambda x: to_enum(SourceType, x), from_none], self.source_type)
        if self.source_unique_id is not None:
            result["sourceUniqueId"] = from_union([from_str, from_none], self.source_unique_id)
        if self.transformation is not None:
            result["transformation"] = from_union([from_str, from_none], self.transformation)
        return result


@dataclass
class ParsedUpstream:
    """Stores the lineage information generated by parser"""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    parsed_upstream_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    sources: Optional[List[ParsedSource]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ParsedUpstream':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        parsed_upstream_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        sources = from_union([lambda x: from_list(ParsedSource.from_dict, x), from_none], obj.get("sources"))
        return ParsedUpstream(created_at, aspect_type, parsed_upstream_created_at, entity_id, id, sources)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.parsed_upstream_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.parsed_upstream_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.sources is not None:
            result["sources"] = from_union([lambda x: from_list(lambda x: to_class(ParsedSource, x), x), from_none], self.sources)
        return result


@dataclass
class PipelineMapping:
    is_virtual: Optional[bool] = None
    pipeline_entity_id: Optional[str] = None
    source_entity_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PipelineMapping':
        assert isinstance(obj, dict)
        is_virtual = from_union([from_bool, from_none], obj.get("isVirtual"))
        pipeline_entity_id = from_union([from_str, from_none], obj.get("pipelineEntityId"))
        source_entity_id = from_union([from_str, from_none], obj.get("sourceEntityId"))
        return PipelineMapping(is_virtual, pipeline_entity_id, source_entity_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.is_virtual is not None:
            result["isVirtual"] = from_union([from_bool, from_none], self.is_virtual)
        if self.pipeline_entity_id is not None:
            result["pipelineEntityId"] = from_union([from_str, from_none], self.pipeline_entity_id)
        if self.source_entity_id is not None:
            result["sourceEntityId"] = from_union([from_str, from_none], self.source_entity_id)
        return result


@dataclass
class PipelineInfo:
    """PipelineInfo captures related pipeline from data sources to this entity"""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    pipeline_info_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    pipeline_mapping: Optional[List[PipelineMapping]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PipelineInfo':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        pipeline_info_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        pipeline_mapping = from_union([lambda x: from_list(PipelineMapping.from_dict, x), from_none], obj.get("pipelineMapping"))
        return PipelineInfo(created_at, aspect_type, pipeline_info_created_at, entity_id, id, pipeline_mapping)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.pipeline_info_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.pipeline_info_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.pipeline_mapping is not None:
            result["pipelineMapping"] = from_union([lambda x: from_list(lambda x: to_class(PipelineMapping, x), x), from_none], self.pipeline_mapping)
        return result


@dataclass
class PowerBIRefreshSchedule:
    days: Optional[List[str]] = None
    enabled: Optional[bool] = None
    frequency_in_minutes: Optional[float] = None
    local_time_zone_id: Optional[str] = None
    notify_option: Optional[str] = None
    times: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIRefreshSchedule':
        assert isinstance(obj, dict)
        days = from_union([lambda x: from_list(from_str, x), from_none], obj.get("days"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        frequency_in_minutes = from_union([from_float, from_none], obj.get("frequencyInMinutes"))
        local_time_zone_id = from_union([from_str, from_none], obj.get("localTimeZoneId"))
        notify_option = from_union([from_str, from_none], obj.get("notifyOption"))
        times = from_union([lambda x: from_list(from_str, x), from_none], obj.get("times"))
        return PowerBIRefreshSchedule(days, enabled, frequency_in_minutes, local_time_zone_id, notify_option, times)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.days is not None:
            result["days"] = from_union([lambda x: from_list(from_str, x), from_none], self.days)
        if self.enabled is not None:
            result["enabled"] = from_union([from_bool, from_none], self.enabled)
        if self.frequency_in_minutes is not None:
            result["frequencyInMinutes"] = from_union([to_float, from_none], self.frequency_in_minutes)
        if self.local_time_zone_id is not None:
            result["localTimeZoneId"] = from_union([from_str, from_none], self.local_time_zone_id)
        if self.notify_option is not None:
            result["notifyOption"] = from_union([from_str, from_none], self.notify_option)
        if self.times is not None:
            result["times"] = from_union([lambda x: from_list(from_str, x), from_none], self.times)
        return result


@dataclass
class PowerBIDataflow:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    configured_by: Optional[str] = None
    content: Optional[str] = None
    power_bi_dataflow_created_at: Optional[datetime] = None
    dataflow_url: Optional[str] = None
    description: Optional[str] = None
    document: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_refreshed: Optional[datetime] = None
    modified_by: Optional[str] = None
    modified_date_time: Optional[datetime] = None
    name: Optional[str] = None
    refresh_schedule: Optional[PowerBIRefreshSchedule] = None
    workspace_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIDataflow':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        configured_by = from_union([from_str, from_none], obj.get("configuredBy"))
        content = from_union([from_str, from_none], obj.get("content"))
        power_bi_dataflow_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        dataflow_url = from_union([from_str, from_none], obj.get("dataflowUrl"))
        description = from_union([from_str, from_none], obj.get("description"))
        document = from_union([from_str, from_none], obj.get("document"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_refreshed = from_union([from_datetime, from_none], obj.get("lastRefreshed"))
        modified_by = from_union([from_str, from_none], obj.get("modifiedBy"))
        modified_date_time = from_union([from_datetime, from_none], obj.get("modifiedDateTime"))
        name = from_union([from_str, from_none], obj.get("name"))
        refresh_schedule = from_union([PowerBIRefreshSchedule.from_dict, from_none], obj.get("refreshSchedule"))
        workspace_id = from_union([from_str, from_none], obj.get("workspaceId"))
        return PowerBIDataflow(created_at, aspect_type, configured_by, content, power_bi_dataflow_created_at, dataflow_url, description, document, entity_id, id, last_refreshed, modified_by, modified_date_time, name, refresh_schedule, workspace_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.configured_by is not None:
            result["configuredBy"] = from_union([from_str, from_none], self.configured_by)
        if self.content is not None:
            result["content"] = from_union([from_str, from_none], self.content)
        if self.power_bi_dataflow_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.power_bi_dataflow_created_at)
        if self.dataflow_url is not None:
            result["dataflowUrl"] = from_union([from_str, from_none], self.dataflow_url)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.document is not None:
            result["document"] = from_union([from_str, from_none], self.document)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_refreshed is not None:
            result["lastRefreshed"] = from_union([lambda x: x.isoformat(), from_none], self.last_refreshed)
        if self.modified_by is not None:
            result["modifiedBy"] = from_union([from_str, from_none], self.modified_by)
        if self.modified_date_time is not None:
            result["modifiedDateTime"] = from_union([lambda x: x.isoformat(), from_none], self.modified_date_time)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.refresh_schedule is not None:
            result["refreshSchedule"] = from_union([lambda x: to_class(PowerBIRefreshSchedule, x), from_none], self.refresh_schedule)
        if self.workspace_id is not None:
            result["workspaceId"] = from_union([from_str, from_none], self.workspace_id)
        return result


@dataclass
class PowerBIDatasource:
    account: Optional[str] = None
    database: Optional[str] = None
    datasource_id: Optional[str] = None
    domain: Optional[str] = None
    gateway_id: Optional[str] = None
    kind: Optional[str] = None
    path: Optional[str] = None
    server: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIDatasource':
        assert isinstance(obj, dict)
        account = from_union([from_str, from_none], obj.get("account"))
        database = from_union([from_str, from_none], obj.get("database"))
        datasource_id = from_union([from_str, from_none], obj.get("datasourceId"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        gateway_id = from_union([from_str, from_none], obj.get("gatewayId"))
        kind = from_union([from_str, from_none], obj.get("kind"))
        path = from_union([from_str, from_none], obj.get("path"))
        server = from_union([from_str, from_none], obj.get("server"))
        type = from_union([from_str, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        return PowerBIDatasource(account, database, datasource_id, domain, gateway_id, kind, path, server, type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account is not None:
            result["account"] = from_union([from_str, from_none], self.account)
        if self.database is not None:
            result["database"] = from_union([from_str, from_none], self.database)
        if self.datasource_id is not None:
            result["datasourceId"] = from_union([from_str, from_none], self.datasource_id)
        if self.domain is not None:
            result["domain"] = from_union([from_str, from_none], self.domain)
        if self.gateway_id is not None:
            result["gatewayId"] = from_union([from_str, from_none], self.gateway_id)
        if self.kind is not None:
            result["kind"] = from_union([from_str, from_none], self.kind)
        if self.path is not None:
            result["path"] = from_union([from_str, from_none], self.path)
        if self.server is not None:
            result["server"] = from_union([from_str, from_none], self.server)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class PowerBIDatasetParameter:
    """Captures the parameters associated with the PowerBI dataset,
    https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-parameters-in-group#mashupparameter
    """
    is_required: Optional[bool] = None
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIDatasetParameter':
        assert isinstance(obj, dict)
        is_required = from_union([from_bool, from_none], obj.get("isRequired"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        return PowerBIDatasetParameter(is_required, name, type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.is_required is not None:
            result["isRequired"] = from_union([from_bool, from_none], self.is_required)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class PowerBIColumn:
    """Captures column name of a dataset table,
    https://docs.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result#column
    """
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIColumn':
        assert isinstance(obj, dict)
        field = from_union([from_str, from_none], obj.get("field"))
        type = from_union([from_str, from_none], obj.get("type"))
        return PowerBIColumn(field, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class PowerBIMeasure:
    """Captures Power BI measure of a dataset table,
    https://docs.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result#measure
    """
    description: Optional[str] = None
    expression: Optional[str] = None
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIMeasure':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        expression = from_union([from_str, from_none], obj.get("expression"))
        field = from_union([from_str, from_none], obj.get("field"))
        return PowerBIMeasure(description, expression, field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.expression is not None:
            result["expression"] = from_union([from_str, from_none], self.expression)
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        return result


@dataclass
class PowerBIDatasetTable:
    """Captures dataset table information of a Power BI Dataset,
    https://docs.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result#table
    """
    columns: Optional[List[PowerBIColumn]] = None
    expression: Optional[str] = None
    measures: Optional[List[PowerBIMeasure]] = None
    name: Optional[str] = None
    sources: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIDatasetTable':
        assert isinstance(obj, dict)
        columns = from_union([lambda x: from_list(PowerBIColumn.from_dict, x), from_none], obj.get("columns"))
        expression = from_union([from_str, from_none], obj.get("expression"))
        measures = from_union([lambda x: from_list(PowerBIMeasure.from_dict, x), from_none], obj.get("measures"))
        name = from_union([from_str, from_none], obj.get("name"))
        sources = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sources"))
        return PowerBIDatasetTable(columns, expression, measures, name, sources)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.columns is not None:
            result["columns"] = from_union([lambda x: from_list(lambda x: to_class(PowerBIColumn, x), x), from_none], self.columns)
        if self.expression is not None:
            result["expression"] = from_union([from_str, from_none], self.expression)
        if self.measures is not None:
            result["measures"] = from_union([lambda x: from_list(lambda x: to_class(PowerBIMeasure, x), x), from_none], self.measures)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.sources is not None:
            result["sources"] = from_union([lambda x: from_list(from_str, x), from_none], self.sources)
        return result


@dataclass
class PowerBIDataset:
    """Captures information of a Power BI Dataset using admin API,
    https://docs.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result#workspaceinfodataset
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    configured_by: Optional[str] = None
    power_bi_dataset_created_at: Optional[datetime] = None
    created_date: Optional[datetime] = None
    data_sources: Optional[List[PowerBIDatasource]] = None
    description: Optional[str] = None
    endorsement: Optional[PowerBIEndorsement] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_refreshed: Optional[datetime] = None
    name: Optional[str] = None
    parameters: Optional[List[PowerBIDatasetParameter]] = None
    refresh_schedule: Optional[PowerBIRefreshSchedule] = None
    sensitivity_label: Optional[PowerBISensitivityLabel] = None
    source_datasets: Optional[List[str]] = None
    tables: Optional[List[PowerBIDatasetTable]] = None
    url: Optional[str] = None
    workspace_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIDataset':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        configured_by = from_union([from_str, from_none], obj.get("configuredBy"))
        power_bi_dataset_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        created_date = from_union([from_datetime, from_none], obj.get("createdDate"))
        data_sources = from_union([lambda x: from_list(PowerBIDatasource.from_dict, x), from_none], obj.get("dataSources"))
        description = from_union([from_str, from_none], obj.get("description"))
        endorsement = from_union([PowerBIEndorsement.from_dict, from_none], obj.get("endorsement"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_refreshed = from_union([from_datetime, from_none], obj.get("lastRefreshed"))
        name = from_union([from_str, from_none], obj.get("name"))
        parameters = from_union([lambda x: from_list(PowerBIDatasetParameter.from_dict, x), from_none], obj.get("parameters"))
        refresh_schedule = from_union([PowerBIRefreshSchedule.from_dict, from_none], obj.get("refreshSchedule"))
        sensitivity_label = from_union([PowerBISensitivityLabel.from_dict, from_none], obj.get("sensitivityLabel"))
        source_datasets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceDatasets"))
        tables = from_union([lambda x: from_list(PowerBIDatasetTable.from_dict, x), from_none], obj.get("tables"))
        url = from_union([from_str, from_none], obj.get("url"))
        workspace_id = from_union([from_str, from_none], obj.get("workspaceId"))
        return PowerBIDataset(created_at, aspect_type, configured_by, power_bi_dataset_created_at, created_date, data_sources, description, endorsement, entity_id, id, last_refreshed, name, parameters, refresh_schedule, sensitivity_label, source_datasets, tables, url, workspace_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.configured_by is not None:
            result["configuredBy"] = from_union([from_str, from_none], self.configured_by)
        if self.power_bi_dataset_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.power_bi_dataset_created_at)
        if self.created_date is not None:
            result["createdDate"] = from_union([lambda x: x.isoformat(), from_none], self.created_date)
        if self.data_sources is not None:
            result["dataSources"] = from_union([lambda x: from_list(lambda x: to_class(PowerBIDatasource, x), x), from_none], self.data_sources)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.endorsement is not None:
            result["endorsement"] = from_union([lambda x: to_class(PowerBIEndorsement, x), from_none], self.endorsement)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_refreshed is not None:
            result["lastRefreshed"] = from_union([lambda x: x.isoformat(), from_none], self.last_refreshed)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.parameters is not None:
            result["parameters"] = from_union([lambda x: from_list(lambda x: to_class(PowerBIDatasetParameter, x), x), from_none], self.parameters)
        if self.refresh_schedule is not None:
            result["refreshSchedule"] = from_union([lambda x: to_class(PowerBIRefreshSchedule, x), from_none], self.refresh_schedule)
        if self.sensitivity_label is not None:
            result["sensitivityLabel"] = from_union([lambda x: to_class(PowerBISensitivityLabel, x), from_none], self.sensitivity_label)
        if self.source_datasets is not None:
            result["sourceDatasets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_datasets)
        if self.tables is not None:
            result["tables"] = from_union([lambda x: from_list(lambda x: to_class(PowerBIDatasetTable, x), x), from_none], self.tables)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.workspace_id is not None:
            result["workspaceId"] = from_union([from_str, from_none], self.workspace_id)
        return result


@dataclass
class QuickSightTable:
    table_content: Optional[str] = None
    table_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuickSightTable':
        assert isinstance(obj, dict)
        table_content = from_union([from_str, from_none], obj.get("tableContent"))
        table_id = from_union([from_str, from_none], obj.get("tableId"))
        return QuickSightTable(table_content, table_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.table_content is not None:
            result["tableContent"] = from_union([from_str, from_none], self.table_content)
        if self.table_id is not None:
            result["tableId"] = from_union([from_str, from_none], self.table_id)
        return result


@dataclass
class QuickSightPhysicalTable:
    account: Optional[str] = None
    database: Optional[str] = None
    platform: Optional[DataPlatform] = None
    schema: Optional[str] = None
    table_content: Optional[str] = None
    table_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuickSightPhysicalTable':
        assert isinstance(obj, dict)
        account = from_union([from_str, from_none], obj.get("account"))
        database = from_union([from_str, from_none], obj.get("database"))
        platform = from_union([DataPlatform, from_none], obj.get("platform"))
        schema = from_union([from_str, from_none], obj.get("schema"))
        table_content = from_union([from_str, from_none], obj.get("tableContent"))
        table_id = from_union([from_str, from_none], obj.get("tableId"))
        return QuickSightPhysicalTable(account, database, platform, schema, table_content, table_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account is not None:
            result["account"] = from_union([from_str, from_none], self.account)
        if self.database is not None:
            result["database"] = from_union([from_str, from_none], self.database)
        if self.platform is not None:
            result["platform"] = from_union([lambda x: to_enum(DataPlatform, x), from_none], self.platform)
        if self.schema is not None:
            result["schema"] = from_union([from_str, from_none], self.schema)
        if self.table_content is not None:
            result["tableContent"] = from_union([from_str, from_none], self.table_content)
        if self.table_id is not None:
            result["tableId"] = from_union([from_str, from_none], self.table_id)
        return result


@dataclass
class QuickSightDataset:
    """QuickSight Dataset information"""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    quick_sight_dataset_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    logical_tables: Optional[List[QuickSightTable]] = None
    physical_tables: Optional[List[QuickSightPhysicalTable]] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuickSightDataset':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        quick_sight_dataset_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        logical_tables = from_union([lambda x: from_list(QuickSightTable.from_dict, x), from_none], obj.get("logicalTables"))
        physical_tables = from_union([lambda x: from_list(QuickSightPhysicalTable.from_dict, x), from_none], obj.get("physicalTables"))
        type = from_union([from_str, from_none], obj.get("type"))
        return QuickSightDataset(created_at, aspect_type, quick_sight_dataset_created_at, entity_id, id, logical_tables, physical_tables, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.quick_sight_dataset_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.quick_sight_dataset_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.logical_tables is not None:
            result["logicalTables"] = from_union([lambda x: from_list(lambda x: to_class(QuickSightTable, x), x), from_none], self.logical_tables)
        if self.physical_tables is not None:
            result["physicalTables"] = from_union([lambda x: from_list(lambda x: to_class(QuickSightPhysicalTable, x), x), from_none], self.physical_tables)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class RelatedAssets:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    created: Optional[AuditStamp] = None
    """An AuditStamp containing creator and creation time attributes for the Aspect instance"""

    related_assets_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    """An AuditStamp containing modification and modifier attributes for the Aspect instance"""

    related_entity_ids: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelatedAssets':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        created = from_union([AuditStamp.from_dict, from_none], obj.get("created"))
        related_assets_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        related_entity_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("relatedEntityIds"))
        return RelatedAssets(created_at, aspect_type, created, related_assets_created_at, entity_id, id, last_modified, related_entity_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.created is not None:
            result["created"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.created)
        if self.related_assets_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.related_assets_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        if self.related_entity_ids is not None:
            result["relatedEntityIds"] = from_union([lambda x: from_list(from_str, x), from_none], self.related_entity_ids)
        return result


@dataclass
class SchemaFieldClass:
    description: Optional[str] = None
    field_name: Optional[str] = None
    field_path: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    is_unique: Optional[bool] = None
    max_length: Optional[float] = None
    native_type: Optional[str] = None
    nullable: Optional[bool] = None
    precision: Optional[float] = None
    subfields: Optional[List[SchemaField]] = None
    tags: Optional[List[str]] = None
    formula: Optional[str] = None
    optional_type: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SchemaFieldClass':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        field_name = from_union([from_str, from_none], obj.get("fieldName"))
        field_path = from_union([from_str, from_none], obj.get("fieldPath"))
        is_unique = from_union([from_bool, from_none], obj.get("isUnique"))
        max_length = from_union([from_float, from_none], obj.get("maxLength"))
        native_type = from_union([from_str, from_none], obj.get("nativeType"))
        nullable = from_union([from_bool, from_none], obj.get("nullable"))
        precision = from_union([from_float, from_none], obj.get("precision"))
        subfields = from_union([lambda x: from_list(SchemaField.from_dict, x), from_none], obj.get("subfields"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tags"))
        formula = from_union([from_str, from_none], obj.get("formula"))
        optional_type = from_union([from_str, from_none], obj.get("optionalType"))
        type = from_union([from_str, from_none], obj.get("type"))
        return SchemaFieldClass(description, field_name, field_path, is_unique, max_length, native_type, nullable, precision, subfields, tags, formula, optional_type, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.field_name is not None:
            result["fieldName"] = from_union([from_str, from_none], self.field_name)
        if self.field_path is not None:
            result["fieldPath"] = from_union([from_str, from_none], self.field_path)
        if self.is_unique is not None:
            result["isUnique"] = from_union([from_bool, from_none], self.is_unique)
        if self.max_length is not None:
            result["maxLength"] = from_union([to_float, from_none], self.max_length)
        if self.native_type is not None:
            result["nativeType"] = from_union([from_str, from_none], self.native_type)
        if self.nullable is not None:
            result["nullable"] = from_union([from_bool, from_none], self.nullable)
        if self.precision is not None:
            result["precision"] = from_union([to_float, from_none], self.precision)
        if self.subfields is not None:
            result["subfields"] = from_union([lambda x: from_list(lambda x: to_class(SchemaField, x), x), from_none], self.subfields)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        if self.formula is not None:
            result["formula"] = from_union([from_str, from_none], self.formula)
        if self.optional_type is not None:
            result["optionalType"] = from_union([from_str, from_none], self.optional_type)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


class SchemaType(Enum):
    AVRO = "AVRO"
    BSON = "BSON"
    DYNAMODB = "DYNAMODB"
    JSON = "JSON"
    ORC = "ORC"
    PARQUET = "PARQUET"
    PROTOBUF = "PROTOBUF"
    SCHEMALESS = "SCHEMALESS"
    SQL = "SQL"


@dataclass
class ForeignKey:
    field_path: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    parent: Optional[DatasetLogicalID] = None
    parent_field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    @staticmethod
    def from_dict(obj: Any) -> 'ForeignKey':
        assert isinstance(obj, dict)
        field_path = from_union([from_str, from_none], obj.get("fieldPath"))
        parent = from_union([DatasetLogicalID.from_dict, from_none], obj.get("parent"))
        parent_field = from_union([from_str, from_none], obj.get("parentField"))
        return ForeignKey(field_path, parent, parent_field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field_path is not None:
            result["fieldPath"] = from_union([from_str, from_none], self.field_path)
        if self.parent is not None:
            result["parent"] = from_union([lambda x: to_class(DatasetLogicalID, x), from_none], self.parent)
        if self.parent_field is not None:
            result["parentField"] = from_union([from_str, from_none], self.parent_field)
        return result


class MaterializationType(Enum):
    EXTERNAL = "EXTERNAL"
    MATERIALIZED_VIEW = "MATERIALIZED_VIEW"
    SNAPSHOT = "SNAPSHOT"
    STREAM = "STREAM"
    TABLE = "TABLE"
    VIEW = "VIEW"


@dataclass
class SQLSchema:
    foreign_key: Optional[List[ForeignKey]] = None
    materialization: Optional[MaterializationType] = None
    primary_key: Optional[List[str]] = None
    snapshot_time: Optional[datetime] = None
    table_schema: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SQLSchema':
        assert isinstance(obj, dict)
        foreign_key = from_union([lambda x: from_list(ForeignKey.from_dict, x), from_none], obj.get("foreignKey"))
        materialization = from_union([MaterializationType, from_none], obj.get("materialization"))
        primary_key = from_union([lambda x: from_list(from_str, x), from_none], obj.get("primaryKey"))
        snapshot_time = from_union([from_datetime, from_none], obj.get("snapshotTime"))
        table_schema = from_union([from_str, from_none], obj.get("tableSchema"))
        return SQLSchema(foreign_key, materialization, primary_key, snapshot_time, table_schema)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.foreign_key is not None:
            result["foreignKey"] = from_union([lambda x: from_list(lambda x: to_class(ForeignKey, x), x), from_none], self.foreign_key)
        if self.materialization is not None:
            result["materialization"] = from_union([lambda x: to_enum(MaterializationType, x), from_none], self.materialization)
        if self.primary_key is not None:
            result["primaryKey"] = from_union([lambda x: from_list(from_str, x), from_none], self.primary_key)
        if self.snapshot_time is not None:
            result["snapshotTime"] = from_union([lambda x: x.isoformat(), from_none], self.snapshot_time)
        if self.table_schema is not None:
            result["tableSchema"] = from_union([from_str, from_none], self.table_schema)
        return result


@dataclass
class Schema:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    schema_created_at: Optional[datetime] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    fields: Optional[List[SchemaFieldClass]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_modified: Optional[AuditStamp] = None
    raw_schema: Optional[str] = None
    schema_type: Optional[SchemaType] = None
    sql_schema: Optional[SQLSchema] = None
    query: Optional[VirtualViewQuery] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Schema':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        schema_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        fields = from_union([lambda x: from_list(SchemaFieldClass.from_dict, x), from_none], obj.get("fields"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_modified = from_union([AuditStamp.from_dict, from_none], obj.get("lastModified"))
        raw_schema = from_union([from_str, from_none], obj.get("rawSchema"))
        schema_type = from_union([SchemaType, from_none], obj.get("schemaType"))
        sql_schema = from_union([SQLSchema.from_dict, from_none], obj.get("sqlSchema"))
        query = from_union([VirtualViewQuery.from_dict, from_none], obj.get("query"))
        return Schema(created_at, aspect_type, schema_created_at, description, entity_id, fields, id, last_modified, raw_schema, schema_type, sql_schema, query)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.schema_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.schema_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.fields is not None:
            result["fields"] = from_union([lambda x: from_list(lambda x: to_class(SchemaFieldClass, x), x), from_none], self.fields)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_modified is not None:
            result["lastModified"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.last_modified)
        if self.raw_schema is not None:
            result["rawSchema"] = from_union([from_str, from_none], self.raw_schema)
        if self.schema_type is not None:
            result["schemaType"] = from_union([lambda x: to_enum(SchemaType, x), from_none], self.schema_type)
        if self.sql_schema is not None:
            result["sqlSchema"] = from_union([lambda x: to_class(SQLSchema, x), from_none], self.sql_schema)
        if self.query is not None:
            result["query"] = from_union([lambda x: to_class(VirtualViewQuery, x), from_none], self.query)
        return result


@dataclass
class HierarchySegment:
    index: Optional[float] = None
    text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HierarchySegment':
        assert isinstance(obj, dict)
        index = from_union([from_float, from_none], obj.get("index"))
        text = from_union([from_str, from_none], obj.get("text"))
        return HierarchySegment(index, text)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.index is not None:
            result["index"] = from_union([to_float, from_none], self.index)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        return result


class SnowflakeIcebergTableType(Enum):
    MANAGED = "MANAGED"
    NOT_ICEBERG = "NOT ICEBERG"
    UNKNOWN = "UNKNOWN"
    UNMANAGED = "UNMANAGED"


@dataclass
class SnowflakeIcebergInfo:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    snowflake_iceberg_info_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    external_volume_name: Optional[str] = None
    iceberg_table_type: Optional[SnowflakeIcebergTableType] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    @staticmethod
    def from_dict(obj: Any) -> 'SnowflakeIcebergInfo':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        snowflake_iceberg_info_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        external_volume_name = from_union([from_str, from_none], obj.get("externalVolumeName"))
        iceberg_table_type = from_union([SnowflakeIcebergTableType, from_none], obj.get("icebergTableType"))
        id = from_union([from_str, from_none], obj.get("id"))
        return SnowflakeIcebergInfo(created_at, aspect_type, snowflake_iceberg_info_created_at, entity_id, external_volume_name, iceberg_table_type, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.snowflake_iceberg_info_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.snowflake_iceberg_info_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.external_volume_name is not None:
            result["externalVolumeName"] = from_union([from_str, from_none], self.external_volume_name)
        if self.iceberg_table_type is not None:
            result["icebergTableType"] = from_union([lambda x: to_enum(SnowflakeIcebergTableType, x), from_none], self.iceberg_table_type)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


class SnowflakeStreamSourceType(Enum):
    TABLE = "TABLE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"


class SnowflakeStreamType(Enum):
    APPEND_ONLY = "APPEND_ONLY"
    INSERT_ONLY = "INSERT_ONLY"
    STANDARD = "STANDARD"
    UNKNOWN = "UNKNOWN"


@dataclass
class SnowflakeStreamInfo:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    snowflake_stream_info_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    source_type: Optional[SnowflakeStreamSourceType] = None
    stale: Optional[bool] = None
    stale_after: Optional[datetime] = None
    stream_type: Optional[SnowflakeStreamType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SnowflakeStreamInfo':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        snowflake_stream_info_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        source_type = from_union([SnowflakeStreamSourceType, from_none], obj.get("sourceType"))
        stale = from_union([from_bool, from_none], obj.get("stale"))
        stale_after = from_union([from_datetime, from_none], obj.get("staleAfter"))
        stream_type = from_union([SnowflakeStreamType, from_none], obj.get("streamType"))
        return SnowflakeStreamInfo(created_at, aspect_type, snowflake_stream_info_created_at, entity_id, id, source_type, stale, stale_after, stream_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.snowflake_stream_info_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.snowflake_stream_info_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.source_type is not None:
            result["sourceType"] = from_union([lambda x: to_enum(SnowflakeStreamSourceType, x), from_none], self.source_type)
        if self.stale is not None:
            result["stale"] = from_union([from_bool, from_none], self.stale)
        if self.stale_after is not None:
            result["staleAfter"] = from_union([lambda x: x.isoformat(), from_none], self.stale_after)
        if self.stream_type is not None:
            result["streamType"] = from_union([lambda x: to_enum(SnowflakeStreamType, x), from_none], self.stream_type)
        return result


@dataclass
class SodaDataMonitorTarget:
    column: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    dataset: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SodaDataMonitorTarget':
        assert isinstance(obj, dict)
        column = from_union([from_str, from_none], obj.get("column"))
        dataset = from_union([from_str, from_none], obj.get("dataset"))
        return SodaDataMonitorTarget(column, dataset)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.column is not None:
            result["column"] = from_union([from_str, from_none], self.column)
        if self.dataset is not None:
            result["dataset"] = from_union([from_str, from_none], self.dataset)
        return result


@dataclass
class SodaDataMonitor:
    last_run: Optional[datetime] = None
    owner: Optional[str] = None
    status: Optional[DataMonitorStatus] = None
    targets: Optional[List[SodaDataMonitorTarget]] = None
    title: Optional[str] = None
    value: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SodaDataMonitor':
        assert isinstance(obj, dict)
        last_run = from_union([from_datetime, from_none], obj.get("lastRun"))
        owner = from_union([from_str, from_none], obj.get("owner"))
        status = from_union([DataMonitorStatus, from_none], obj.get("status"))
        targets = from_union([lambda x: from_list(SodaDataMonitorTarget.from_dict, x), from_none], obj.get("targets"))
        title = from_union([from_str, from_none], obj.get("title"))
        value = from_union([from_float, from_none], obj.get("value"))
        return SodaDataMonitor(last_run, owner, status, targets, title, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.last_run is not None:
            result["lastRun"] = from_union([lambda x: x.isoformat(), from_none], self.last_run)
        if self.owner is not None:
            result["owner"] = from_union([from_str, from_none], self.owner)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(DataMonitorStatus, x), from_none], self.status)
        if self.targets is not None:
            result["targets"] = from_union([lambda x: from_list(lambda x: to_class(SodaDataMonitorTarget, x), x), from_none], self.targets)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.value is not None:
            result["value"] = from_union([to_float, from_none], self.value)
        return result


@dataclass
class SodaDataProfileMetrics:
    distinct: Optional[float] = None
    invalid: Optional[float] = None
    maximum: Optional[float] = None
    mean: Optional[float] = None
    minimum: Optional[float] = None
    missing: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SodaDataProfileMetrics':
        assert isinstance(obj, dict)
        distinct = from_union([from_float, from_none], obj.get("distinct"))
        invalid = from_union([from_float, from_none], obj.get("invalid"))
        maximum = from_union([from_float, from_none], obj.get("maximum"))
        mean = from_union([from_float, from_none], obj.get("mean"))
        minimum = from_union([from_float, from_none], obj.get("minimum"))
        missing = from_union([from_float, from_none], obj.get("missing"))
        return SodaDataProfileMetrics(distinct, invalid, maximum, mean, minimum, missing)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.distinct is not None:
            result["distinct"] = from_union([to_float, from_none], self.distinct)
        if self.invalid is not None:
            result["invalid"] = from_union([to_float, from_none], self.invalid)
        if self.maximum is not None:
            result["maximum"] = from_union([to_float, from_none], self.maximum)
        if self.mean is not None:
            result["mean"] = from_union([to_float, from_none], self.mean)
        if self.minimum is not None:
            result["minimum"] = from_union([to_float, from_none], self.minimum)
        if self.missing is not None:
            result["missing"] = from_union([to_float, from_none], self.missing)
        return result


@dataclass
class SodaDataProfile:
    column: Optional[str] = None
    last_run: Optional[datetime] = None
    metrics: Optional[SodaDataProfileMetrics] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SodaDataProfile':
        assert isinstance(obj, dict)
        column = from_union([from_str, from_none], obj.get("column"))
        last_run = from_union([from_datetime, from_none], obj.get("lastRun"))
        metrics = from_union([SodaDataProfileMetrics.from_dict, from_none], obj.get("metrics"))
        return SodaDataProfile(column, last_run, metrics)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.column is not None:
            result["column"] = from_union([from_str, from_none], self.column)
        if self.last_run is not None:
            result["lastRun"] = from_union([lambda x: x.isoformat(), from_none], self.last_run)
        if self.metrics is not None:
            result["metrics"] = from_union([lambda x: to_class(SodaDataProfileMetrics, x), from_none], self.metrics)
        return result


@dataclass
class DatasetSodaDataQuality:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dataset_soda_data_quality_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    monitors: Optional[List[SodaDataMonitor]] = None
    profiles: Optional[List[SodaDataProfile]] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetSodaDataQuality':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dataset_soda_data_quality_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        monitors = from_union([lambda x: from_list(SodaDataMonitor.from_dict, x), from_none], obj.get("monitors"))
        profiles = from_union([lambda x: from_list(SodaDataProfile.from_dict, x), from_none], obj.get("profiles"))
        url = from_union([from_str, from_none], obj.get("url"))
        return DatasetSodaDataQuality(created_at, aspect_type, dataset_soda_data_quality_created_at, entity_id, id, monitors, profiles, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dataset_soda_data_quality_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_soda_data_quality_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.monitors is not None:
            result["monitors"] = from_union([lambda x: from_list(lambda x: to_class(SodaDataMonitor, x), x), from_none], self.monitors)
        if self.profiles is not None:
            result["profiles"] = from_union([lambda x: from_list(lambda x: to_class(SodaDataProfile, x), x), from_none], self.profiles)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class SourceInfo:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    source_info_created_at: Optional[datetime] = None
    created_at_source: Optional[datetime] = None
    created_by: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    last_updated: Optional[datetime] = None
    main_url: Optional[str] = None
    updated_by: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SourceInfo':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        source_info_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        created_at_source = from_union([from_datetime, from_none], obj.get("createdAtSource"))
        created_by = from_union([from_str, from_none], obj.get("createdBy"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_updated = from_union([from_datetime, from_none], obj.get("lastUpdated"))
        main_url = from_union([from_str, from_none], obj.get("mainUrl"))
        updated_by = from_union([from_str, from_none], obj.get("updatedBy"))
        return SourceInfo(created_at, aspect_type, source_info_created_at, created_at_source, created_by, entity_id, id, last_updated, main_url, updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.source_info_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.source_info_created_at)
        if self.created_at_source is not None:
            result["createdAtSource"] = from_union([lambda x: x.isoformat(), from_none], self.created_at_source)
        if self.created_by is not None:
            result["createdBy"] = from_union([from_str, from_none], self.created_by)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_updated is not None:
            result["lastUpdated"] = from_union([lambda x: x.isoformat(), from_none], self.last_updated)
        if self.main_url is not None:
            result["mainUrl"] = from_union([from_str, from_none], self.main_url)
        if self.updated_by is not None:
            result["updatedBy"] = from_union([from_str, from_none], self.updated_by)
        return result


@dataclass
class SparkJob:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    spark_job_created_at: Optional[datetime] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    source_code_url: Optional[str] = None
    sql: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SparkJob':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        spark_job_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        source_code_url = from_union([from_str, from_none], obj.get("sourceCodeUrl"))
        sql = from_union([from_str, from_none], obj.get("sql"))
        return SparkJob(created_at, aspect_type, spark_job_created_at, description, entity_id, id, source_code_url, sql)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.spark_job_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.spark_job_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.source_code_url is not None:
            result["sourceCodeUrl"] = from_union([from_str, from_none], self.source_code_url)
        if self.sql is not None:
            result["sql"] = from_union([from_str, from_none], self.sql)
        return result


@dataclass
class DatasetStatistics:
    """DatasetStatistics captures operational information about the dataset, e.g. the number of
    records or the last refresh time.
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dataset_statistics_created_at: Optional[datetime] = None
    data_size_bytes: Optional[float] = None
    entity_id: Optional[str] = None
    field_statistics: Optional[List[FieldStatistics]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    record_count: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetStatistics':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dataset_statistics_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        data_size_bytes = from_union([from_float, from_none], obj.get("dataSizeBytes"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        field_statistics = from_union([lambda x: from_list(FieldStatistics.from_dict, x), from_none], obj.get("fieldStatistics"))
        id = from_union([from_str, from_none], obj.get("id"))
        record_count = from_union([from_float, from_none], obj.get("recordCount"))
        return DatasetStatistics(created_at, aspect_type, dataset_statistics_created_at, data_size_bytes, entity_id, field_statistics, id, record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dataset_statistics_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_statistics_created_at)
        if self.data_size_bytes is not None:
            result["dataSizeBytes"] = from_union([to_float, from_none], self.data_size_bytes)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.field_statistics is not None:
            result["fieldStatistics"] = from_union([lambda x: from_list(lambda x: to_class(FieldStatistics, x), x), from_none], self.field_statistics)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.record_count is not None:
            result["recordCount"] = from_union([to_float, from_none], self.record_count)
        return result


@dataclass
class SetStructure:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    set_structure_created_at: Optional[datetime] = None
    directories: Optional[List[str]] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    name: Optional[str] = None
    database: Optional[str] = None
    schema: Optional[str] = None
    table: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SetStructure':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        set_structure_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        directories = from_union([lambda x: from_list(from_str, x), from_none], obj.get("directories"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        database = from_union([from_str, from_none], obj.get("database"))
        schema = from_union([from_str, from_none], obj.get("schema"))
        table = from_union([from_str, from_none], obj.get("table"))
        return SetStructure(created_at, aspect_type, set_structure_created_at, directories, entity_id, id, name, database, schema, table)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.set_structure_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.set_structure_created_at)
        if self.directories is not None:
            result["directories"] = from_union([lambda x: from_list(from_str, x), from_none], self.directories)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.database is not None:
            result["database"] = from_union([from_str, from_none], self.database)
        if self.schema is not None:
            result["schema"] = from_union([from_str, from_none], self.schema)
        if self.table is not None:
            result["table"] = from_union([from_str, from_none], self.table)
        return result


class AssetPlatform(Enum):
    """Platform across all entity specific platform"""

    AIRFLOW = "AIRFLOW"
    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGQUERY = "BIGQUERY"
    CUSTOM = "CUSTOM"
    DASH = "DASH"
    DBT = "DBT"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    FIVETRAN = "FIVETRAN"
    GCS = "GCS"
    GLUE = "GLUE"
    HIVE = "HIVE"
    HTTP = "HTTP"
    INFORMATICA = "INFORMATICA"
    KAFKA = "KAFKA"
    LOOKER = "LOOKER"
    METABASE = "METABASE"
    MONGODB = "MONGODB"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    OPEN_API = "OPEN_API"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    POWER_BI = "POWER_BI"
    QUICK_SIGHT = "QUICK_SIGHT"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SNOWFLAKE = "SNOWFLAKE"
    SPARK = "SPARK"
    SYNAPSE = "SYNAPSE"
    TABLEAU = "TABLEAU"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


@dataclass
class SystemContact:
    email: Optional[str] = None
    system_contact_source: Optional[AssetPlatform] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SystemContact':
        assert isinstance(obj, dict)
        email = from_union([from_str, from_none], obj.get("email"))
        system_contact_source = from_union([AssetPlatform, from_none], obj.get("systemContactSource"))
        return SystemContact(email, system_contact_source)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.system_contact_source is not None:
            result["systemContactSource"] = from_union([lambda x: to_enum(AssetPlatform, x), from_none], self.system_contact_source)
        return result


@dataclass
class SystemContacts:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    contacts: Optional[List[SystemContact]] = None
    system_contacts_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    @staticmethod
    def from_dict(obj: Any) -> 'SystemContacts':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        contacts = from_union([lambda x: from_list(SystemContact.from_dict, x), from_none], obj.get("contacts"))
        system_contacts_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        return SystemContacts(created_at, aspect_type, contacts, system_contacts_created_at, entity_id, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.contacts is not None:
            result["contacts"] = from_union([lambda x: from_list(lambda x: to_class(SystemContact, x), x), from_none], self.contacts)
        if self.system_contacts_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.system_contacts_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class SystemDescription:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    system_description_created_at: Optional[datetime] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    platform: Optional[AssetPlatform] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SystemDescription':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        system_description_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        platform = from_union([AssetPlatform, from_none], obj.get("platform"))
        return SystemDescription(created_at, aspect_type, system_description_created_at, description, entity_id, id, platform)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.system_description_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.system_description_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.platform is not None:
            result["platform"] = from_union([lambda x: to_enum(AssetPlatform, x), from_none], self.platform)
        return result


class SystemTagSource(Enum):
    DATAHUB = "DATAHUB"
    DBT = "DBT"
    LOOKER = "LOOKER"
    SNOWFLAKE = "SNOWFLAKE"
    TABLEAU = "TABLEAU"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNKNOWN = "UNKNOWN"


@dataclass
class SystemTag:
    key: Optional[str] = None
    system_tag_source: Optional[SystemTagSource] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SystemTag':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        system_tag_source = from_union([SystemTagSource, from_none], obj.get("systemTagSource"))
        value = from_union([from_str, from_none], obj.get("value"))
        return SystemTag(key, system_tag_source, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.system_tag_source is not None:
            result["systemTagSource"] = from_union([lambda x: to_enum(SystemTagSource, x), from_none], self.system_tag_source)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class SystemTags:
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    system_tags_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    tags: Optional[List[SystemTag]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SystemTags':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        system_tags_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        tags = from_union([lambda x: from_list(SystemTag.from_dict, x), from_none], obj.get("tags"))
        return SystemTags(created_at, aspect_type, system_tags_created_at, entity_id, id, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.system_tags_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.system_tags_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(lambda x: to_class(SystemTag, x), x), from_none], self.tags)
        return result


@dataclass
class TableauField:
    description: Optional[str] = None
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    @staticmethod
    def from_dict(obj: Any) -> 'TableauField':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        field = from_union([from_str, from_none], obj.get("field"))
        return TableauField(description, field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        return result


@dataclass
class TableauDatasource:
    """Modeling Tableau Datasource as a virtual view.
    https://help.tableau.com/current/server/en-us/datasource.htm
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    tableau_datasource_created_at: Optional[datetime] = None
    description: Optional[str] = None
    embedded: Optional[bool] = None
    entity_id: Optional[str] = None
    fields: Optional[List[TableauField]] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    name: Optional[str] = None
    query: Optional[str] = None
    source_dataset_account: Optional[str] = None
    source_platform: Optional[DataPlatform] = None
    source_datasets: Optional[List[str]] = None
    source_virtual_views: Optional[List[str]] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TableauDatasource':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        tableau_datasource_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        embedded = from_union([from_bool, from_none], obj.get("embedded"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        fields = from_union([lambda x: from_list(TableauField.from_dict, x), from_none], obj.get("fields"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        query = from_union([from_str, from_none], obj.get("query"))
        source_dataset_account = from_union([from_str, from_none], obj.get("source_dataset_account"))
        source_platform = from_union([DataPlatform, from_none], obj.get("source_platform"))
        source_datasets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceDatasets"))
        source_virtual_views = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceVirtualViews"))
        url = from_union([from_str, from_none], obj.get("url"))
        return TableauDatasource(created_at, aspect_type, tableau_datasource_created_at, description, embedded, entity_id, fields, id, name, query, source_dataset_account, source_platform, source_datasets, source_virtual_views, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.tableau_datasource_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.tableau_datasource_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.embedded is not None:
            result["embedded"] = from_union([from_bool, from_none], self.embedded)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.fields is not None:
            result["fields"] = from_union([lambda x: from_list(lambda x: to_class(TableauField, x), x), from_none], self.fields)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.query is not None:
            result["query"] = from_union([from_str, from_none], self.query)
        if self.source_dataset_account is not None:
            result["source_dataset_account"] = from_union([from_str, from_none], self.source_dataset_account)
        if self.source_platform is not None:
            result["source_platform"] = from_union([lambda x: to_enum(DataPlatform, x), from_none], self.source_platform)
        if self.source_datasets is not None:
            result["sourceDatasets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_datasets)
        if self.source_virtual_views is not None:
            result["sourceVirtualViews"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_virtual_views)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class ColumnTagAssignment:
    column_name: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    tag_names: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ColumnTagAssignment':
        assert isinstance(obj, dict)
        column_name = from_union([from_str, from_none], obj.get("columnName"))
        tag_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tagNames"))
        return ColumnTagAssignment(column_name, tag_names)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.column_name is not None:
            result["columnName"] = from_union([from_str, from_none], self.column_name)
        if self.tag_names is not None:
            result["tagNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.tag_names)
        return result


@dataclass
class TagAssignment:
    column_tag_assignments: Optional[List[ColumnTagAssignment]] = None
    tag_names: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TagAssignment':
        assert isinstance(obj, dict)
        column_tag_assignments = from_union([lambda x: from_list(ColumnTagAssignment.from_dict, x), from_none], obj.get("columnTagAssignments"))
        tag_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tagNames"))
        return TagAssignment(column_tag_assignments, tag_names)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.column_tag_assignments is not None:
            result["columnTagAssignments"] = from_union([lambda x: from_list(lambda x: to_class(ColumnTagAssignment, x), x), from_none], self.column_tag_assignments)
        if self.tag_names is not None:
            result["tagNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.tag_names)
        return result


@dataclass
class ThoughtSpotColumn:
    description: Optional[str] = None
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    formula: Optional[str] = None
    name: Optional[str] = None
    optional_type: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThoughtSpotColumn':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        field = from_union([from_str, from_none], obj.get("field"))
        formula = from_union([from_str, from_none], obj.get("formula"))
        name = from_union([from_str, from_none], obj.get("name"))
        optional_type = from_union([from_str, from_none], obj.get("optionalType"))
        type = from_union([from_str, from_none], obj.get("type"))
        return ThoughtSpotColumn(description, field, formula, name, optional_type, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        if self.formula is not None:
            result["formula"] = from_union([from_str, from_none], self.formula)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.optional_type is not None:
            result["optionalType"] = from_union([from_str, from_none], self.optional_type)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


class ThoughtSpotDataObjectType(Enum):
    TABLE = "TABLE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"
    WORKSHEET = "WORKSHEET"


@dataclass
class ThoughtSpotDataObject:
    """Modeling ThoughtSpot DataSource or DataObject in the API into a virtual view.
    DataSource: https://docs.thoughtspot.com/software/latest/data-sources
    """
    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    columns: Optional[List[ThoughtSpotColumn]] = None
    thought_spot_data_object_created_at: Optional[datetime] = None
    description: Optional[str] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    name: Optional[str] = None
    source_datasets: Optional[List[str]] = None
    source_virtual_views: Optional[List[str]] = None
    type: Optional[ThoughtSpotDataObjectType] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThoughtSpotDataObject':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        columns = from_union([lambda x: from_list(ThoughtSpotColumn.from_dict, x), from_none], obj.get("columns"))
        thought_spot_data_object_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        source_datasets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceDatasets"))
        source_virtual_views = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sourceVirtualViews"))
        type = from_union([ThoughtSpotDataObjectType, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        return ThoughtSpotDataObject(created_at, aspect_type, columns, thought_spot_data_object_created_at, description, entity_id, id, name, source_datasets, source_virtual_views, type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.columns is not None:
            result["columns"] = from_union([lambda x: from_list(lambda x: to_class(ThoughtSpotColumn, x), x), from_none], self.columns)
        if self.thought_spot_data_object_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.thought_spot_data_object_created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.source_datasets is not None:
            result["sourceDatasets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_datasets)
        if self.source_virtual_views is not None:
            result["sourceVirtualViews"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_virtual_views)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(ThoughtSpotDataObjectType, x), from_none], self.type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class UnityCatalogDatasetType(Enum):
    UNITY_CATALOG_EXTERNAL_LOCATION = "UNITY_CATALOG_EXTERNAL_LOCATION"
    UNITY_CATALOG_TABLE = "UNITY_CATALOG_TABLE"
    UNITY_CATALOG_VOLUME = "UNITY_CATALOG_VOLUME"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


@dataclass
class KeyValuePair:
    """A generic key-value pair"""

    key: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'KeyValuePair':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([from_str, from_none], obj.get("value"))
        return KeyValuePair(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


class UnityCatalogTableType(Enum):
    EXTERNAL = "EXTERNAL"
    EXTERNAL_SHALLOW_CLONE = "EXTERNAL_SHALLOW_CLONE"
    FOREIGN = "FOREIGN"
    MANAGED = "MANAGED"
    MANAGED_SHALLOW_CLONE = "MANAGED_SHALLOW_CLONE"
    MATERIALIZED_VIEW = "MATERIALIZED_VIEW"
    STREAMING_TABLE = "STREAMING_TABLE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"


@dataclass
class UnityCatalogTableInfo:
    """File under a Unity Catalog Volume"""

    data_source_format: Optional[str] = None
    owner: Optional[str] = None
    properties: Optional[List[KeyValuePair]] = None
    storage_location: Optional[str] = None
    type: Optional[UnityCatalogTableType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UnityCatalogTableInfo':
        assert isinstance(obj, dict)
        data_source_format = from_union([from_str, from_none], obj.get("dataSourceFormat"))
        owner = from_union([from_str, from_none], obj.get("owner"))
        properties = from_union([lambda x: from_list(KeyValuePair.from_dict, x), from_none], obj.get("properties"))
        storage_location = from_union([from_str, from_none], obj.get("storageLocation"))
        type = from_union([UnityCatalogTableType, from_none], obj.get("type"))
        return UnityCatalogTableInfo(data_source_format, owner, properties, storage_location, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.data_source_format is not None:
            result["dataSourceFormat"] = from_union([from_str, from_none], self.data_source_format)
        if self.owner is not None:
            result["owner"] = from_union([from_str, from_none], self.owner)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: from_list(lambda x: to_class(KeyValuePair, x), x), from_none], self.properties)
        if self.storage_location is not None:
            result["storageLocation"] = from_union([from_str, from_none], self.storage_location)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(UnityCatalogTableType, x), from_none], self.type)
        return result


class UnityCatalogVolumeType(Enum):
    EXTERNAL = "EXTERNAL"
    MANAGED = "MANAGED"
    UNKNOWN = "UNKNOWN"


@dataclass
class VolumeFile:
    """File under a Unity Catalog Volume"""

    entity_id: Optional[str] = None
    modification_time: Optional[datetime] = None
    name: Optional[str] = None
    path: Optional[str] = None
    size: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VolumeFile':
        assert isinstance(obj, dict)
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        modification_time = from_union([from_datetime, from_none], obj.get("modification_time"))
        name = from_union([from_str, from_none], obj.get("name"))
        path = from_union([from_str, from_none], obj.get("path"))
        size = from_union([from_float, from_none], obj.get("size"))
        return VolumeFile(entity_id, modification_time, name, path, size)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.modification_time is not None:
            result["modification_time"] = from_union([lambda x: x.isoformat(), from_none], self.modification_time)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.path is not None:
            result["path"] = from_union([from_str, from_none], self.path)
        if self.size is not None:
            result["size"] = from_union([to_float, from_none], self.size)
        return result


@dataclass
class UnityCatalogVolumeInfo:
    """File under a Unity Catalog Volume"""

    storage_location: Optional[str] = None
    type: Optional[UnityCatalogVolumeType] = None
    volume_files: Optional[List[VolumeFile]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UnityCatalogVolumeInfo':
        assert isinstance(obj, dict)
        storage_location = from_union([from_str, from_none], obj.get("storageLocation"))
        type = from_union([UnityCatalogVolumeType, from_none], obj.get("type"))
        volume_files = from_union([lambda x: from_list(VolumeFile.from_dict, x), from_none], obj.get("volumeFiles"))
        return UnityCatalogVolumeInfo(storage_location, type, volume_files)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.storage_location is not None:
            result["storageLocation"] = from_union([from_str, from_none], self.storage_location)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(UnityCatalogVolumeType, x), from_none], self.type)
        if self.volume_files is not None:
            result["volumeFiles"] = from_union([lambda x: from_list(lambda x: to_class(VolumeFile, x), x), from_none], self.volume_files)
        return result


@dataclass
class UnityCatalog:
    """Metadata specific to Unity Catalog datasets"""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    unity_catalog_created_at: Optional[datetime] = None
    dataset_type: Optional[UnityCatalogDatasetType] = None
    entity_id: Optional[str] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    table_info: Optional[UnityCatalogTableInfo] = None
    """File under a Unity Catalog Volume"""

    volume_entity_id: Optional[str] = None
    volume_info: Optional[UnityCatalogVolumeInfo] = None
    """File under a Unity Catalog Volume"""

    @staticmethod
    def from_dict(obj: Any) -> 'UnityCatalog':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        unity_catalog_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        dataset_type = from_union([UnityCatalogDatasetType, from_none], obj.get("datasetType"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        id = from_union([from_str, from_none], obj.get("id"))
        table_info = from_union([UnityCatalogTableInfo.from_dict, from_none], obj.get("tableInfo"))
        volume_entity_id = from_union([from_str, from_none], obj.get("volumeEntityId"))
        volume_info = from_union([UnityCatalogVolumeInfo.from_dict, from_none], obj.get("volumeInfo"))
        return UnityCatalog(created_at, aspect_type, unity_catalog_created_at, dataset_type, entity_id, id, table_info, volume_entity_id, volume_info)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.unity_catalog_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.unity_catalog_created_at)
        if self.dataset_type is not None:
            result["datasetType"] = from_union([lambda x: to_enum(UnityCatalogDatasetType, x), from_none], self.dataset_type)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.table_info is not None:
            result["tableInfo"] = from_union([lambda x: to_class(UnityCatalogTableInfo, x), from_none], self.table_info)
        if self.volume_entity_id is not None:
            result["volumeEntityId"] = from_union([from_str, from_none], self.volume_entity_id)
        if self.volume_info is not None:
            result["volumeInfo"] = from_union([lambda x: to_class(UnityCatalogVolumeInfo, x), from_none], self.volume_info)
        return result


@dataclass
class FieldQueryCount:
    """Query count number and statistics of a dataset field"""

    count: Optional[float] = None
    field: Optional[str] = None
    """Alias for the path of a field on an Entity"""

    percentile: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FieldQueryCount':
        assert isinstance(obj, dict)
        count = from_union([from_float, from_none], obj.get("count"))
        field = from_union([from_str, from_none], obj.get("field"))
        percentile = from_union([from_float, from_none], obj.get("percentile"))
        return FieldQueryCount(count, field, percentile)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.count is not None:
            result["count"] = from_union([to_float, from_none], self.count)
        if self.field is not None:
            result["field"] = from_union([from_str, from_none], self.field)
        if self.percentile is not None:
            result["percentile"] = from_union([to_float, from_none], self.percentile)
        return result


@dataclass
class FieldQueryCounts:
    """Captures field/column query counts in last day/week/month/year."""

    last24_hours: Optional[List[FieldQueryCount]] = None
    last30_days: Optional[List[FieldQueryCount]] = None
    last365_days: Optional[List[FieldQueryCount]] = None
    last7_days: Optional[List[FieldQueryCount]] = None
    last90_days: Optional[List[FieldQueryCount]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FieldQueryCounts':
        assert isinstance(obj, dict)
        last24_hours = from_union([lambda x: from_list(FieldQueryCount.from_dict, x), from_none], obj.get("last24Hours"))
        last30_days = from_union([lambda x: from_list(FieldQueryCount.from_dict, x), from_none], obj.get("last30Days"))
        last365_days = from_union([lambda x: from_list(FieldQueryCount.from_dict, x), from_none], obj.get("last365Days"))
        last7_days = from_union([lambda x: from_list(FieldQueryCount.from_dict, x), from_none], obj.get("last7Days"))
        last90_days = from_union([lambda x: from_list(FieldQueryCount.from_dict, x), from_none], obj.get("last90Days"))
        return FieldQueryCounts(last24_hours, last30_days, last365_days, last7_days, last90_days)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.last24_hours is not None:
            result["last24Hours"] = from_union([lambda x: from_list(lambda x: to_class(FieldQueryCount, x), x), from_none], self.last24_hours)
        if self.last30_days is not None:
            result["last30Days"] = from_union([lambda x: from_list(lambda x: to_class(FieldQueryCount, x), x), from_none], self.last30_days)
        if self.last365_days is not None:
            result["last365Days"] = from_union([lambda x: from_list(lambda x: to_class(FieldQueryCount, x), x), from_none], self.last365_days)
        if self.last7_days is not None:
            result["last7Days"] = from_union([lambda x: from_list(lambda x: to_class(FieldQueryCount, x), x), from_none], self.last7_days)
        if self.last90_days is not None:
            result["last90Days"] = from_union([lambda x: from_list(lambda x: to_class(FieldQueryCount, x), x), from_none], self.last90_days)
        return result


@dataclass
class QueryCount:
    """Query count number and statistics"""

    count: Optional[float] = None
    percentile: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QueryCount':
        assert isinstance(obj, dict)
        count = from_union([from_float, from_none], obj.get("count"))
        percentile = from_union([from_float, from_none], obj.get("percentile"))
        return QueryCount(count, percentile)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.count is not None:
            result["count"] = from_union([to_float, from_none], self.count)
        if self.percentile is not None:
            result["percentile"] = from_union([to_float, from_none], self.percentile)
        return result


@dataclass
class QueryCounts:
    """Captures query counts in last day/week/month/year."""

    last24_hours: Optional[QueryCount] = None
    """Query count number and statistics"""

    last30_days: Optional[QueryCount] = None
    """Query count number and statistics"""

    last365_days: Optional[QueryCount] = None
    """Query count number and statistics"""

    last7_days: Optional[QueryCount] = None
    """Query count number and statistics"""

    last90_days: Optional[QueryCount] = None
    """Query count number and statistics"""

    @staticmethod
    def from_dict(obj: Any) -> 'QueryCounts':
        assert isinstance(obj, dict)
        last24_hours = from_union([QueryCount.from_dict, from_none], obj.get("last24Hours"))
        last30_days = from_union([QueryCount.from_dict, from_none], obj.get("last30Days"))
        last365_days = from_union([QueryCount.from_dict, from_none], obj.get("last365Days"))
        last7_days = from_union([QueryCount.from_dict, from_none], obj.get("last7Days"))
        last90_days = from_union([QueryCount.from_dict, from_none], obj.get("last90Days"))
        return QueryCounts(last24_hours, last30_days, last365_days, last7_days, last90_days)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.last24_hours is not None:
            result["last24Hours"] = from_union([lambda x: to_class(QueryCount, x), from_none], self.last24_hours)
        if self.last30_days is not None:
            result["last30Days"] = from_union([lambda x: to_class(QueryCount, x), from_none], self.last30_days)
        if self.last365_days is not None:
            result["last365Days"] = from_union([lambda x: to_class(QueryCount, x), from_none], self.last365_days)
        if self.last7_days is not None:
            result["last7Days"] = from_union([lambda x: to_class(QueryCount, x), from_none], self.last7_days)
        if self.last90_days is not None:
            result["last90Days"] = from_union([lambda x: to_class(QueryCount, x), from_none], self.last90_days)
        return result


@dataclass
class JoinedDataset:
    """A dataset that has been joined with the current dataset"""

    count: Optional[float] = None
    emails: Optional[List[str]] = None
    id: Optional[str] = None
    user_ids: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'JoinedDataset':
        assert isinstance(obj, dict)
        count = from_union([from_float, from_none], obj.get("count"))
        emails = from_union([lambda x: from_list(from_str, x), from_none], obj.get("emails"))
        id = from_union([from_str, from_none], obj.get("id"))
        user_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("userIds"))
        return JoinedDataset(count, emails, id, user_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.count is not None:
            result["count"] = from_union([to_float, from_none], self.count)
        if self.emails is not None:
            result["emails"] = from_union([lambda x: from_list(from_str, x), from_none], self.emails)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.user_ids is not None:
            result["userIds"] = from_union([lambda x: from_list(from_str, x), from_none], self.user_ids)
        return result


@dataclass
class TableJoin:
    """Table join usage statistics"""

    joined_assets: Optional[List[JoinedDataset]] = None
    total_join_count: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TableJoin':
        assert isinstance(obj, dict)
        joined_assets = from_union([lambda x: from_list(JoinedDataset.from_dict, x), from_none], obj.get("joinedAssets"))
        total_join_count = from_union([from_float, from_none], obj.get("totalJoinCount"))
        return TableJoin(joined_assets, total_join_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.joined_assets is not None:
            result["joinedAssets"] = from_union([lambda x: from_list(lambda x: to_class(JoinedDataset, x), x), from_none], self.joined_assets)
        if self.total_join_count is not None:
            result["totalJoinCount"] = from_union([to_float, from_none], self.total_join_count)
        return result


@dataclass
class TableJoins:
    """Captures table join usage info in last day/week/month/year."""

    last24_hours: Optional[TableJoin] = None
    """Table join usage statistics"""

    last30_days: Optional[TableJoin] = None
    """Table join usage statistics"""

    last365_days: Optional[TableJoin] = None
    """Table join usage statistics"""

    last7_days: Optional[TableJoin] = None
    """Table join usage statistics"""

    last90_days: Optional[TableJoin] = None
    """Table join usage statistics"""

    @staticmethod
    def from_dict(obj: Any) -> 'TableJoins':
        assert isinstance(obj, dict)
        last24_hours = from_union([TableJoin.from_dict, from_none], obj.get("last24Hours"))
        last30_days = from_union([TableJoin.from_dict, from_none], obj.get("last30Days"))
        last365_days = from_union([TableJoin.from_dict, from_none], obj.get("last365Days"))
        last7_days = from_union([TableJoin.from_dict, from_none], obj.get("last7Days"))
        last90_days = from_union([TableJoin.from_dict, from_none], obj.get("last90Days"))
        return TableJoins(last24_hours, last30_days, last365_days, last7_days, last90_days)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.last24_hours is not None:
            result["last24Hours"] = from_union([lambda x: to_class(TableJoin, x), from_none], self.last24_hours)
        if self.last30_days is not None:
            result["last30Days"] = from_union([lambda x: to_class(TableJoin, x), from_none], self.last30_days)
        if self.last365_days is not None:
            result["last365Days"] = from_union([lambda x: to_class(TableJoin, x), from_none], self.last365_days)
        if self.last7_days is not None:
            result["last7Days"] = from_union([lambda x: to_class(TableJoin, x), from_none], self.last7_days)
        if self.last90_days is not None:
            result["last90Days"] = from_union([lambda x: to_class(TableJoin, x), from_none], self.last90_days)
        return result


@dataclass
class UserQueryCount:
    """Query count number and statistics from a user/account"""

    count: Optional[float] = None
    user: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserQueryCount':
        assert isinstance(obj, dict)
        count = from_union([from_float, from_none], obj.get("count"))
        user = from_union([from_str, from_none], obj.get("user"))
        return UserQueryCount(count, user)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.count is not None:
            result["count"] = from_union([to_float, from_none], self.count)
        if self.user is not None:
            result["user"] = from_union([from_str, from_none], self.user)
        return result


@dataclass
class UserQueryCounts:
    """Captures user query counts in last day/week/month/year."""

    last24_hours: Optional[List[UserQueryCount]] = None
    last24_hours_queried_by_count: Optional[float] = None
    last30_days: Optional[List[UserQueryCount]] = None
    last30_days_queried_by_count: Optional[float] = None
    last365_days: Optional[List[UserQueryCount]] = None
    last365_days_queried_by_count: Optional[float] = None
    last7_days: Optional[List[UserQueryCount]] = None
    last7_days_queried_by_count: Optional[float] = None
    last90_days: Optional[List[UserQueryCount]] = None
    last90_days_queried_by_count: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserQueryCounts':
        assert isinstance(obj, dict)
        last24_hours = from_union([lambda x: from_list(UserQueryCount.from_dict, x), from_none], obj.get("last24Hours"))
        last24_hours_queried_by_count = from_union([from_float, from_none], obj.get("last24HoursQueriedByCount"))
        last30_days = from_union([lambda x: from_list(UserQueryCount.from_dict, x), from_none], obj.get("last30Days"))
        last30_days_queried_by_count = from_union([from_float, from_none], obj.get("last30DaysQueriedByCount"))
        last365_days = from_union([lambda x: from_list(UserQueryCount.from_dict, x), from_none], obj.get("last365Days"))
        last365_days_queried_by_count = from_union([from_float, from_none], obj.get("last365DaysQueriedByCount"))
        last7_days = from_union([lambda x: from_list(UserQueryCount.from_dict, x), from_none], obj.get("last7Days"))
        last7_days_queried_by_count = from_union([from_float, from_none], obj.get("last7DaysQueriedByCount"))
        last90_days = from_union([lambda x: from_list(UserQueryCount.from_dict, x), from_none], obj.get("last90Days"))
        last90_days_queried_by_count = from_union([from_float, from_none], obj.get("last90DaysQueriedByCount"))
        return UserQueryCounts(last24_hours, last24_hours_queried_by_count, last30_days, last30_days_queried_by_count, last365_days, last365_days_queried_by_count, last7_days, last7_days_queried_by_count, last90_days, last90_days_queried_by_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.last24_hours is not None:
            result["last24Hours"] = from_union([lambda x: from_list(lambda x: to_class(UserQueryCount, x), x), from_none], self.last24_hours)
        if self.last24_hours_queried_by_count is not None:
            result["last24HoursQueriedByCount"] = from_union([to_float, from_none], self.last24_hours_queried_by_count)
        if self.last30_days is not None:
            result["last30Days"] = from_union([lambda x: from_list(lambda x: to_class(UserQueryCount, x), x), from_none], self.last30_days)
        if self.last30_days_queried_by_count is not None:
            result["last30DaysQueriedByCount"] = from_union([to_float, from_none], self.last30_days_queried_by_count)
        if self.last365_days is not None:
            result["last365Days"] = from_union([lambda x: from_list(lambda x: to_class(UserQueryCount, x), x), from_none], self.last365_days)
        if self.last365_days_queried_by_count is not None:
            result["last365DaysQueriedByCount"] = from_union([to_float, from_none], self.last365_days_queried_by_count)
        if self.last7_days is not None:
            result["last7Days"] = from_union([lambda x: from_list(lambda x: to_class(UserQueryCount, x), x), from_none], self.last7_days)
        if self.last7_days_queried_by_count is not None:
            result["last7DaysQueriedByCount"] = from_union([to_float, from_none], self.last7_days_queried_by_count)
        if self.last90_days is not None:
            result["last90Days"] = from_union([lambda x: from_list(lambda x: to_class(UserQueryCount, x), x), from_none], self.last90_days)
        if self.last90_days_queried_by_count is not None:
            result["last90DaysQueriedByCount"] = from_union([to_float, from_none], self.last90_days_queried_by_count)
        return result


@dataclass
class DatasetUsage:
    """Captures dataset usage statistic, e.g. the query counts."""

    created_at: Optional[datetime] = None
    """Backing store for the aspect creation date"""

    aspect_type: Optional[AspectType] = None
    dataset_usage_created_at: Optional[datetime] = None
    entity_id: Optional[str] = None
    field_query_counts: Optional[FieldQueryCounts] = None
    id: Optional[str] = None
    """The id field is deprecated and will be removed at a later time post migration"""

    query_counts: Optional[QueryCounts] = None
    table_joins: Optional[TableJoins] = None
    user_query_counts: Optional[UserQueryCounts] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DatasetUsage':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        aspect_type = from_union([AspectType, from_none], obj.get("aspectType"))
        dataset_usage_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        entity_id = from_union([from_str, from_none], obj.get("entityId"))
        field_query_counts = from_union([FieldQueryCounts.from_dict, from_none], obj.get("fieldQueryCounts"))
        id = from_union([from_str, from_none], obj.get("id"))
        query_counts = from_union([QueryCounts.from_dict, from_none], obj.get("queryCounts"))
        table_joins = from_union([TableJoins.from_dict, from_none], obj.get("tableJoins"))
        user_query_counts = from_union([UserQueryCounts.from_dict, from_none], obj.get("userQueryCounts"))
        return DatasetUsage(created_at, aspect_type, dataset_usage_created_at, entity_id, field_query_counts, id, query_counts, table_joins, user_query_counts)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.aspect_type is not None:
            result["aspectType"] = from_union([lambda x: to_enum(AspectType, x), from_none], self.aspect_type)
        if self.dataset_usage_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.dataset_usage_created_at)
        if self.entity_id is not None:
            result["entityId"] = from_union([from_str, from_none], self.entity_id)
        if self.field_query_counts is not None:
            result["fieldQueryCounts"] = from_union([lambda x: to_class(FieldQueryCounts, x), from_none], self.field_query_counts)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.query_counts is not None:
            result["queryCounts"] = from_union([lambda x: to_class(QueryCounts, x), from_none], self.query_counts)
        if self.table_joins is not None:
            result["tableJoins"] = from_union([lambda x: to_class(TableJoins, x), from_none], self.table_joins)
        if self.user_query_counts is not None:
            result["userQueryCounts"] = from_union([lambda x: to_class(UserQueryCounts, x), from_none], self.user_query_counts)
        return result


@dataclass
class Entity:
    """The original entity for the parser to process
    
    Defines the attributes shared across input and output types for a Person entity
    """
    created_at: Optional[datetime] = None
    """Backing store for an optionally provided creation date"""

    id: Optional[ObjectID] = None
    """Native Mongo db BSON id instance"""

    versioned_id: Optional[str] = None
    """Optional protected internal field to store a versionId of the entity, if the instance is
    versioned
    """
    asset_contacts: Optional[AssetContacts] = None
    asset_followers: Optional[AssetFollowers] = None
    asset_governed_tags: Optional[AssetGovernedTags] = None
    entity_created_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    display_name: Optional[str] = None
    """Implement a dummy accessor here, the children class will implement the correct one."""

    entity_type: Optional[EntityType] = None
    entity_upstream: Optional[EntityUpstream] = None
    """EntityUpstream captures upstream lineages from data sources to this entity"""

    force_shown: Optional[AuditStamp] = None
    entity_id: Optional[str] = None
    """A getter for the id property that's directly generated from the
    entity type & logical ID.
    """
    is_complete: Optional[bool] = None
    is_deleted: Optional[bool] = None
    is_non_prod: Optional[bool] = None
    is_production: Optional[bool] = None
    last_ingested_at: Optional[datetime] = None
    last_modified_at: Optional[datetime] = None
    logical_id: Optional[APILogicalID] = None
    """Identify an entity "logically".
    Each entity must have a logicalId to be ingested.
    A compelling use-case is that this allows a producer to create an
    instance of the Entity without requiring an entity ID to be
    obtained prior to instantiation, potentially resulting in two round-trips
    
    Implemented in {@link KnowledgeCard} output type
    Definite assignment assertion is safe since it is defined in output subtype.
    This is due to unresolved TypeScript bug preventing this class from being defined as an
    abstract class, and
    then being used in a mixin {@see https://github.com/microsoft/TypeScript/issues/37142}
    
    Implemented in {@link UserDefinedResource} output type
    Definite assignment operator is used because field is implemented on output type but not
    expected on input type
    """
    parsed_upstream: Optional[ParsedUpstream] = None
    """Stores the lineage information generated by parser"""

    related_assets: Optional[RelatedAssets] = None
    source_info: Optional[SourceInfo] = None
    structure: Optional[SetStructure] = None
    system_contacts: Optional[SystemContacts] = None
    system_description: Optional[SystemDescription] = None
    system_tags: Optional[SystemTags] = None
    system_tag_values: Optional[List[str]] = None
    entity_versioned_id: Optional[str] = None
    """Write-only api to set a versionId of the entity, if the instance is versioned
    This allows the versionedId to be maintained on the entity e.g. when an instance is
    created by the factory
    """
    dashboard_info: Optional[DashboardInfo] = None
    overall_data_quality: Optional[OverallDataQuality] = None
    """Overall data quality of entity, it is calculated by it's upstream node.
    Any FAILED, or WARNING status of upstreams will cause the overall data quality WARN
    """
    custom_metadata: Optional[CustomMetadata] = None
    """Captures custom metadata for an asset"""

    data_quality: Optional[DatasetDataQuality] = None
    description_assignment: Optional[DescriptionAssignment] = None
    documentation: Optional[DatasetDocumentation] = None
    """Captures dataset documentations from other tools outside the data source, e.g. dbt
    documentation on source datasets
    """
    field_associations: Optional[DatasetFieldAssociations] = None
    field_statistics: Optional[DatasetFieldStatistics] = None
    """DatasetStatistics captures operational information about the dataset, e.g. the number of
    records or the last refresh time.
    """
    last_query: Optional[DatasetLastQuery] = None
    ownership_assignment: Optional[OwnershipAssignment] = None
    pipeline_info: Optional[PipelineInfo] = None
    """PipelineInfo captures related pipeline from data sources to this entity"""

    schema: Optional[Schema] = None
    snowflake_iceberg_info: Optional[SnowflakeIcebergInfo] = None
    snowflake_stream_info: Optional[SnowflakeStreamInfo] = None
    soda_data_quality: Optional[DatasetSodaDataQuality] = None
    statistics: Optional[DatasetStatistics] = None
    """DatasetStatistics captures operational information about the dataset, e.g. the number of
    records or the last refresh time.
    """
    tag_assignment: Optional[TagAssignment] = None
    unity_catalog: Optional[UnityCatalog] = None
    """Metadata specific to Unity Catalog datasets"""

    usage: Optional[DatasetUsage] = None
    """Captures dataset usage statistic, e.g. the query counts."""

    dbt_metric: Optional[DbtMetric] = None
    azure_data_factory_pipeline: Optional[AzureDataFactoryPipeline] = None
    fivetran: Optional[FivetranPipeline] = None
    informatica_mapping: Optional[InformaticaMapping] = None
    power_bi_dataflow: Optional[PowerBIDataflow] = None
    spark: Optional[SparkJob] = None
    dbt_model: Optional[DbtModel] = None
    full_name: Optional[str] = None
    looker_explore: Optional[LookerExplore] = None
    """Captures information of a Looker Explore,
    https://docs.looker.com/reference/explore-reference
    """
    looker_view: Optional[LookerView] = None
    """Captures information of a Looker View, https://docs.looker.com/reference/view-reference"""

    power_bi_dataset: Optional[PowerBIDataset] = None
    """Captures information of a Power BI Dataset using admin API,
    https://docs.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result#workspaceinfodataset
    """
    quick_sight: Optional[QuickSightDataset] = None
    """QuickSight Dataset information"""

    tableau_datasource: Optional[TableauDatasource] = None
    """Modeling Tableau Datasource as a virtual view.
    https://help.tableau.com/current/server/en-us/datasource.htm
    """
    thought_spot: Optional[ThoughtSpotDataObject] = None
    """Modeling ThoughtSpot DataSource or DataObject in the API into a virtual view.
    DataSource: https://docs.thoughtspot.com/software/latest/data-sources
    """
    level: Optional[float] = None
    segments: Optional[List[HierarchySegment]] = None
    browse_paths: Optional[List[BrowsePath]] = None
    display_name_without_fallback: Optional[str] = None
    hierarchy_info: Optional[HierarchyInfo] = None
    asset_likes: Optional[AssetLikes] = None
    organization: Optional[PersonOrganization] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entity':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("_createdAt"))
        id = from_union([ObjectID.from_dict, from_none], obj.get("_id"))
        versioned_id = from_union([from_str, from_none], obj.get("_versionedId"))
        asset_contacts = from_union([AssetContacts.from_dict, from_none], obj.get("assetContacts"))
        asset_followers = from_union([AssetFollowers.from_dict, from_none], obj.get("assetFollowers"))
        asset_governed_tags = from_union([AssetGovernedTags.from_dict, from_none], obj.get("assetGovernedTags"))
        entity_created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        deleted_at = from_union([from_datetime, from_none], obj.get("deletedAt"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        entity_type = from_union([EntityType, from_none], obj.get("entityType"))
        entity_upstream = from_union([EntityUpstream.from_dict, from_none], obj.get("entityUpstream"))
        force_shown = from_union([AuditStamp.from_dict, from_none], obj.get("forceShown"))
        entity_id = from_union([from_str, from_none], obj.get("id"))
        is_complete = from_union([from_bool, from_none], obj.get("isComplete"))
        is_deleted = from_union([from_bool, from_none], obj.get("isDeleted"))
        is_non_prod = from_union([from_bool, from_none], obj.get("isNonProd"))
        is_production = from_union([from_bool, from_none], obj.get("isProduction"))
        last_ingested_at = from_union([from_datetime, from_none], obj.get("lastIngestedAt"))
        last_modified_at = from_union([from_datetime, from_none], obj.get("lastModifiedAt"))
        logical_id = from_union([APILogicalID.from_dict, from_none], obj.get("logicalId"))
        parsed_upstream = from_union([ParsedUpstream.from_dict, from_none], obj.get("parsedUpstream"))
        related_assets = from_union([RelatedAssets.from_dict, from_none], obj.get("relatedAssets"))
        source_info = from_union([SourceInfo.from_dict, from_none], obj.get("sourceInfo"))
        structure = from_union([SetStructure.from_dict, from_none], obj.get("structure"))
        system_contacts = from_union([SystemContacts.from_dict, from_none], obj.get("systemContacts"))
        system_description = from_union([SystemDescription.from_dict, from_none], obj.get("systemDescription"))
        system_tags = from_union([SystemTags.from_dict, from_none], obj.get("systemTags"))
        system_tag_values = from_union([lambda x: from_list(from_str, x), from_none], obj.get("systemTagValues"))
        entity_versioned_id = from_union([from_str, from_none], obj.get("versionedId"))
        dashboard_info = from_union([DashboardInfo.from_dict, from_none], obj.get("dashboardInfo"))
        overall_data_quality = from_union([OverallDataQuality.from_dict, from_none], obj.get("overallDataQuality"))
        custom_metadata = from_union([CustomMetadata.from_dict, from_none], obj.get("customMetadata"))
        data_quality = from_union([DatasetDataQuality.from_dict, from_none], obj.get("dataQuality"))
        description_assignment = from_union([DescriptionAssignment.from_dict, from_none], obj.get("descriptionAssignment"))
        documentation = from_union([DatasetDocumentation.from_dict, from_none], obj.get("documentation"))
        field_associations = from_union([DatasetFieldAssociations.from_dict, from_none], obj.get("fieldAssociations"))
        field_statistics = from_union([DatasetFieldStatistics.from_dict, from_none], obj.get("fieldStatistics"))
        last_query = from_union([DatasetLastQuery.from_dict, from_none], obj.get("lastQuery"))
        ownership_assignment = from_union([OwnershipAssignment.from_dict, from_none], obj.get("ownershipAssignment"))
        pipeline_info = from_union([PipelineInfo.from_dict, from_none], obj.get("pipelineInfo"))
        schema = from_union([Schema.from_dict, from_none], obj.get("schema"))
        snowflake_iceberg_info = from_union([SnowflakeIcebergInfo.from_dict, from_none], obj.get("snowflakeIcebergInfo"))
        snowflake_stream_info = from_union([SnowflakeStreamInfo.from_dict, from_none], obj.get("snowflakeStreamInfo"))
        soda_data_quality = from_union([DatasetSodaDataQuality.from_dict, from_none], obj.get("sodaDataQuality"))
        statistics = from_union([DatasetStatistics.from_dict, from_none], obj.get("statistics"))
        tag_assignment = from_union([TagAssignment.from_dict, from_none], obj.get("tagAssignment"))
        unity_catalog = from_union([UnityCatalog.from_dict, from_none], obj.get("unityCatalog"))
        usage = from_union([DatasetUsage.from_dict, from_none], obj.get("usage"))
        dbt_metric = from_union([DbtMetric.from_dict, from_none], obj.get("dbtMetric"))
        azure_data_factory_pipeline = from_union([AzureDataFactoryPipeline.from_dict, from_none], obj.get("azureDataFactoryPipeline"))
        fivetran = from_union([FivetranPipeline.from_dict, from_none], obj.get("fivetran"))
        informatica_mapping = from_union([InformaticaMapping.from_dict, from_none], obj.get("informaticaMapping"))
        power_bi_dataflow = from_union([PowerBIDataflow.from_dict, from_none], obj.get("powerBiDataflow"))
        spark = from_union([SparkJob.from_dict, from_none], obj.get("spark"))
        dbt_model = from_union([DbtModel.from_dict, from_none], obj.get("dbtModel"))
        full_name = from_union([from_str, from_none], obj.get("fullName"))
        looker_explore = from_union([LookerExplore.from_dict, from_none], obj.get("lookerExplore"))
        looker_view = from_union([LookerView.from_dict, from_none], obj.get("lookerView"))
        power_bi_dataset = from_union([PowerBIDataset.from_dict, from_none], obj.get("powerBIDataset"))
        quick_sight = from_union([QuickSightDataset.from_dict, from_none], obj.get("quickSight"))
        tableau_datasource = from_union([TableauDatasource.from_dict, from_none], obj.get("tableauDatasource"))
        thought_spot = from_union([ThoughtSpotDataObject.from_dict, from_none], obj.get("thoughtSpot"))
        level = from_union([from_float, from_none], obj.get("_level"))
        segments = from_union([lambda x: from_list(HierarchySegment.from_dict, x), from_none], obj.get("_segments"))
        browse_paths = from_union([lambda x: from_list(BrowsePath.from_dict, x), from_none], obj.get("browsePaths"))
        display_name_without_fallback = from_union([from_str, from_none], obj.get("displayNameWithoutFallback"))
        hierarchy_info = from_union([HierarchyInfo.from_dict, from_none], obj.get("hierarchyInfo"))
        asset_likes = from_union([AssetLikes.from_dict, from_none], obj.get("assetLikes"))
        organization = from_union([PersonOrganization.from_dict, from_none], obj.get("organization"))
        return Entity(created_at, id, versioned_id, asset_contacts, asset_followers, asset_governed_tags, entity_created_at, deleted_at, display_name, entity_type, entity_upstream, force_shown, entity_id, is_complete, is_deleted, is_non_prod, is_production, last_ingested_at, last_modified_at, logical_id, parsed_upstream, related_assets, source_info, structure, system_contacts, system_description, system_tags, system_tag_values, entity_versioned_id, dashboard_info, overall_data_quality, custom_metadata, data_quality, description_assignment, documentation, field_associations, field_statistics, last_query, ownership_assignment, pipeline_info, schema, snowflake_iceberg_info, snowflake_stream_info, soda_data_quality, statistics, tag_assignment, unity_catalog, usage, dbt_metric, azure_data_factory_pipeline, fivetran, informatica_mapping, power_bi_dataflow, spark, dbt_model, full_name, looker_explore, looker_view, power_bi_dataset, quick_sight, tableau_datasource, thought_spot, level, segments, browse_paths, display_name_without_fallback, hierarchy_info, asset_likes, organization)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["_createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["_id"] = from_union([lambda x: to_class(ObjectID, x), from_none], self.id)
        if self.versioned_id is not None:
            result["_versionedId"] = from_union([from_str, from_none], self.versioned_id)
        if self.asset_contacts is not None:
            result["assetContacts"] = from_union([lambda x: to_class(AssetContacts, x), from_none], self.asset_contacts)
        if self.asset_followers is not None:
            result["assetFollowers"] = from_union([lambda x: to_class(AssetFollowers, x), from_none], self.asset_followers)
        if self.asset_governed_tags is not None:
            result["assetGovernedTags"] = from_union([lambda x: to_class(AssetGovernedTags, x), from_none], self.asset_governed_tags)
        if self.entity_created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.entity_created_at)
        if self.deleted_at is not None:
            result["deletedAt"] = from_union([lambda x: x.isoformat(), from_none], self.deleted_at)
        if self.display_name is not None:
            result["displayName"] = from_union([from_str, from_none], self.display_name)
        if self.entity_type is not None:
            result["entityType"] = from_union([lambda x: to_enum(EntityType, x), from_none], self.entity_type)
        if self.entity_upstream is not None:
            result["entityUpstream"] = from_union([lambda x: to_class(EntityUpstream, x), from_none], self.entity_upstream)
        if self.force_shown is not None:
            result["forceShown"] = from_union([lambda x: to_class(AuditStamp, x), from_none], self.force_shown)
        if self.entity_id is not None:
            result["id"] = from_union([from_str, from_none], self.entity_id)
        if self.is_complete is not None:
            result["isComplete"] = from_union([from_bool, from_none], self.is_complete)
        if self.is_deleted is not None:
            result["isDeleted"] = from_union([from_bool, from_none], self.is_deleted)
        if self.is_non_prod is not None:
            result["isNonProd"] = from_union([from_bool, from_none], self.is_non_prod)
        if self.is_production is not None:
            result["isProduction"] = from_union([from_bool, from_none], self.is_production)
        if self.last_ingested_at is not None:
            result["lastIngestedAt"] = from_union([lambda x: x.isoformat(), from_none], self.last_ingested_at)
        if self.last_modified_at is not None:
            result["lastModifiedAt"] = from_union([lambda x: x.isoformat(), from_none], self.last_modified_at)
        if self.logical_id is not None:
            result["logicalId"] = from_union([lambda x: to_class(APILogicalID, x), from_none], self.logical_id)
        if self.parsed_upstream is not None:
            result["parsedUpstream"] = from_union([lambda x: to_class(ParsedUpstream, x), from_none], self.parsed_upstream)
        if self.related_assets is not None:
            result["relatedAssets"] = from_union([lambda x: to_class(RelatedAssets, x), from_none], self.related_assets)
        if self.source_info is not None:
            result["sourceInfo"] = from_union([lambda x: to_class(SourceInfo, x), from_none], self.source_info)
        if self.structure is not None:
            result["structure"] = from_union([lambda x: to_class(SetStructure, x), from_none], self.structure)
        if self.system_contacts is not None:
            result["systemContacts"] = from_union([lambda x: to_class(SystemContacts, x), from_none], self.system_contacts)
        if self.system_description is not None:
            result["systemDescription"] = from_union([lambda x: to_class(SystemDescription, x), from_none], self.system_description)
        if self.system_tags is not None:
            result["systemTags"] = from_union([lambda x: to_class(SystemTags, x), from_none], self.system_tags)
        if self.system_tag_values is not None:
            result["systemTagValues"] = from_union([lambda x: from_list(from_str, x), from_none], self.system_tag_values)
        if self.entity_versioned_id is not None:
            result["versionedId"] = from_union([from_str, from_none], self.entity_versioned_id)
        if self.dashboard_info is not None:
            result["dashboardInfo"] = from_union([lambda x: to_class(DashboardInfo, x), from_none], self.dashboard_info)
        if self.overall_data_quality is not None:
            result["overallDataQuality"] = from_union([lambda x: to_class(OverallDataQuality, x), from_none], self.overall_data_quality)
        if self.custom_metadata is not None:
            result["customMetadata"] = from_union([lambda x: to_class(CustomMetadata, x), from_none], self.custom_metadata)
        if self.data_quality is not None:
            result["dataQuality"] = from_union([lambda x: to_class(DatasetDataQuality, x), from_none], self.data_quality)
        if self.description_assignment is not None:
            result["descriptionAssignment"] = from_union([lambda x: to_class(DescriptionAssignment, x), from_none], self.description_assignment)
        if self.documentation is not None:
            result["documentation"] = from_union([lambda x: to_class(DatasetDocumentation, x), from_none], self.documentation)
        if self.field_associations is not None:
            result["fieldAssociations"] = from_union([lambda x: to_class(DatasetFieldAssociations, x), from_none], self.field_associations)
        if self.field_statistics is not None:
            result["fieldStatistics"] = from_union([lambda x: to_class(DatasetFieldStatistics, x), from_none], self.field_statistics)
        if self.last_query is not None:
            result["lastQuery"] = from_union([lambda x: to_class(DatasetLastQuery, x), from_none], self.last_query)
        if self.ownership_assignment is not None:
            result["ownershipAssignment"] = from_union([lambda x: to_class(OwnershipAssignment, x), from_none], self.ownership_assignment)
        if self.pipeline_info is not None:
            result["pipelineInfo"] = from_union([lambda x: to_class(PipelineInfo, x), from_none], self.pipeline_info)
        if self.schema is not None:
            result["schema"] = from_union([lambda x: to_class(Schema, x), from_none], self.schema)
        if self.snowflake_iceberg_info is not None:
            result["snowflakeIcebergInfo"] = from_union([lambda x: to_class(SnowflakeIcebergInfo, x), from_none], self.snowflake_iceberg_info)
        if self.snowflake_stream_info is not None:
            result["snowflakeStreamInfo"] = from_union([lambda x: to_class(SnowflakeStreamInfo, x), from_none], self.snowflake_stream_info)
        if self.soda_data_quality is not None:
            result["sodaDataQuality"] = from_union([lambda x: to_class(DatasetSodaDataQuality, x), from_none], self.soda_data_quality)
        if self.statistics is not None:
            result["statistics"] = from_union([lambda x: to_class(DatasetStatistics, x), from_none], self.statistics)
        if self.tag_assignment is not None:
            result["tagAssignment"] = from_union([lambda x: to_class(TagAssignment, x), from_none], self.tag_assignment)
        if self.unity_catalog is not None:
            result["unityCatalog"] = from_union([lambda x: to_class(UnityCatalog, x), from_none], self.unity_catalog)
        if self.usage is not None:
            result["usage"] = from_union([lambda x: to_class(DatasetUsage, x), from_none], self.usage)
        if self.dbt_metric is not None:
            result["dbtMetric"] = from_union([lambda x: to_class(DbtMetric, x), from_none], self.dbt_metric)
        if self.azure_data_factory_pipeline is not None:
            result["azureDataFactoryPipeline"] = from_union([lambda x: to_class(AzureDataFactoryPipeline, x), from_none], self.azure_data_factory_pipeline)
        if self.fivetran is not None:
            result["fivetran"] = from_union([lambda x: to_class(FivetranPipeline, x), from_none], self.fivetran)
        if self.informatica_mapping is not None:
            result["informaticaMapping"] = from_union([lambda x: to_class(InformaticaMapping, x), from_none], self.informatica_mapping)
        if self.power_bi_dataflow is not None:
            result["powerBiDataflow"] = from_union([lambda x: to_class(PowerBIDataflow, x), from_none], self.power_bi_dataflow)
        if self.spark is not None:
            result["spark"] = from_union([lambda x: to_class(SparkJob, x), from_none], self.spark)
        if self.dbt_model is not None:
            result["dbtModel"] = from_union([lambda x: to_class(DbtModel, x), from_none], self.dbt_model)
        if self.full_name is not None:
            result["fullName"] = from_union([from_str, from_none], self.full_name)
        if self.looker_explore is not None:
            result["lookerExplore"] = from_union([lambda x: to_class(LookerExplore, x), from_none], self.looker_explore)
        if self.looker_view is not None:
            result["lookerView"] = from_union([lambda x: to_class(LookerView, x), from_none], self.looker_view)
        if self.power_bi_dataset is not None:
            result["powerBIDataset"] = from_union([lambda x: to_class(PowerBIDataset, x), from_none], self.power_bi_dataset)
        if self.quick_sight is not None:
            result["quickSight"] = from_union([lambda x: to_class(QuickSightDataset, x), from_none], self.quick_sight)
        if self.tableau_datasource is not None:
            result["tableauDatasource"] = from_union([lambda x: to_class(TableauDatasource, x), from_none], self.tableau_datasource)
        if self.thought_spot is not None:
            result["thoughtSpot"] = from_union([lambda x: to_class(ThoughtSpotDataObject, x), from_none], self.thought_spot)
        if self.level is not None:
            result["_level"] = from_union([to_float, from_none], self.level)
        if self.segments is not None:
            result["_segments"] = from_union([lambda x: from_list(lambda x: to_class(HierarchySegment, x), x), from_none], self.segments)
        if self.browse_paths is not None:
            result["browsePaths"] = from_union([lambda x: from_list(lambda x: to_class(BrowsePath, x), x), from_none], self.browse_paths)
        if self.display_name_without_fallback is not None:
            result["displayNameWithoutFallback"] = from_union([from_str, from_none], self.display_name_without_fallback)
        if self.hierarchy_info is not None:
            result["hierarchyInfo"] = from_union([lambda x: to_class(HierarchyInfo, x), from_none], self.hierarchy_info)
        if self.asset_likes is not None:
            result["assetLikes"] = from_union([lambda x: to_class(AssetLikes, x), from_none], self.asset_likes)
        if self.organization is not None:
            result["organization"] = from_union([lambda x: to_class(PersonOrganization, x), from_none], self.organization)
        return result


@dataclass
class MapStringString:
    """Field transformation/mapping to apply after SQL query"""

    to_string_tag_8530: Optional[str] = None
    size: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MapStringString':
        assert isinstance(obj, dict)
        to_string_tag_8530 = from_union([from_str, from_none], obj.get("__@toStringTag@8530"))
        size = from_union([from_float, from_none], obj.get("size"))
        return MapStringString(to_string_tag_8530, size)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.to_string_tag_8530 is not None:
            result["__@toStringTag@8530"] = from_union([from_str, from_none], self.to_string_tag_8530)
        if self.size is not None:
            result["size"] = from_union([to_float, from_none], self.size)
        return result


@dataclass
class PowerBIDatasetTableParserContext:
    field_transformation: Optional[MapStringString] = None
    """Field transformation/mapping to apply after SQL query"""

    name: Optional[str] = None
    """The PowerBI table name within the PowerBI dataset"""

    query: Optional[str] = None
    """The SQL query to parse"""

    source_account: Optional[str] = None
    """The account of the upstream dataset"""

    source_database: Optional[str] = None
    """The database name of the upstream dataset"""

    source_platform: Optional[DataPlatform] = None
    """The data platform of the upstream dataset"""

    unique_id: Optional[str] = None
    """The unique ID associated with this parser context"""

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIDatasetTableParserContext':
        assert isinstance(obj, dict)
        field_transformation = from_union([MapStringString.from_dict, from_none], obj.get("fieldTransformation"))
        name = from_union([from_str, from_none], obj.get("name"))
        query = from_union([from_str, from_none], obj.get("query"))
        source_account = from_union([from_str, from_none], obj.get("sourceAccount"))
        source_database = from_union([from_str, from_none], obj.get("sourceDatabase"))
        source_platform = from_union([DataPlatform, from_none], obj.get("sourcePlatform"))
        unique_id = from_union([from_str, from_none], obj.get("uniqueId"))
        return PowerBIDatasetTableParserContext(field_transformation, name, query, source_account, source_database, source_platform, unique_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.field_transformation is not None:
            result["fieldTransformation"] = from_union([lambda x: to_class(MapStringString, x), from_none], self.field_transformation)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.query is not None:
            result["query"] = from_union([from_str, from_none], self.query)
        if self.source_account is not None:
            result["sourceAccount"] = from_union([from_str, from_none], self.source_account)
        if self.source_database is not None:
            result["sourceDatabase"] = from_union([from_str, from_none], self.source_database)
        if self.source_platform is not None:
            result["sourcePlatform"] = from_union([lambda x: to_enum(DataPlatform, x), from_none], self.source_platform)
        if self.unique_id is not None:
            result["uniqueId"] = from_union([from_str, from_none], self.unique_id)
        return result


@dataclass
class PowerBIDatasetParserContext:
    """The PowerBI dataset native queries to parse"""

    parsed_field_mappings: Optional[List[FieldMapping]] = None
    """CLL field mappings that have already been parsed and will be merged with parsed table
    queries
    """
    tables: Optional[List[PowerBIDatasetTableParserContext]] = None
    """The PowerBI table name within the PowerBI dataset"""

    @staticmethod
    def from_dict(obj: Any) -> 'PowerBIDatasetParserContext':
        assert isinstance(obj, dict)
        parsed_field_mappings = from_union([lambda x: from_list(FieldMapping.from_dict, x), from_none], obj.get("parsedFieldMappings"))
        tables = from_union([lambda x: from_list(PowerBIDatasetTableParserContext.from_dict, x), from_none], obj.get("tables"))
        return PowerBIDatasetParserContext(parsed_field_mappings, tables)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.parsed_field_mappings is not None:
            result["parsedFieldMappings"] = from_union([lambda x: from_list(lambda x: to_class(FieldMapping, x), x), from_none], self.parsed_field_mappings)
        if self.tables is not None:
            result["tables"] = from_union([lambda x: from_list(lambda x: to_class(PowerBIDatasetTableParserContext, x), x), from_none], self.tables)
        return result


@dataclass
class ParserCacheItem:
    entity: Optional[Entity] = None
    """The original entity for the parser to process"""

    power_bi_dataset: Optional[PowerBIDatasetParserContext] = None
    """The PowerBI dataset native queries to parse"""

    @staticmethod
    def from_dict(obj: Any) -> 'ParserCacheItem':
        assert isinstance(obj, dict)
        entity = from_union([Entity.from_dict, from_none], obj.get("entity"))
        power_bi_dataset = from_union([PowerBIDatasetParserContext.from_dict, from_none], obj.get("powerBiDataset"))
        return ParserCacheItem(entity, power_bi_dataset)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.entity is not None:
            result["entity"] = from_union([lambda x: to_class(Entity, x), from_none], self.entity)
        if self.power_bi_dataset is not None:
            result["powerBiDataset"] = from_union([lambda x: to_class(PowerBIDatasetParserContext, x), from_none], self.power_bi_dataset)
        return result


def parser_cache_item_from_dict(s: Any) -> ParserCacheItem:
    return ParserCacheItem.from_dict(s)


def parser_cache_item_to_dict(x: ParserCacheItem) -> Any:
    return to_class(ParserCacheItem, x)
