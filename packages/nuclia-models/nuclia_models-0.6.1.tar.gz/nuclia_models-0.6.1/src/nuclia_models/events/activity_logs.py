import re
from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from pydantic.main import create_model

from nuclia_models.common.client import ClientType
from nuclia_models.common.pagination import Pagination
from nuclia_models.common.user import UserType
from nuclia_models.common.utils import CaseInsensitiveEnum

T = TypeVar("T")


class EventType(CaseInsensitiveEnum):
    # Nucliadb
    VISITED = "visited"
    MODIFIED = "modified"
    DELETED = "deleted"
    NEW = "new"
    SEARCH = "search"
    SUGGEST = "suggest"
    INDEXED = "indexed"
    CHAT = "chat"
    # Tasks
    STARTED = "started"
    STOPPED = "stopped"
    # Processor
    PROCESSED = "processed"


class BaseConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class GenericFilter(BaseConfigModel, Generic[T]):
    eq: Optional[T] = None
    gt: Optional[T] = None
    ge: Optional[T] = None
    lt: Optional[T] = None
    le: Optional[T] = None
    ne: Optional[T] = None
    isnull: Optional[bool] = None


class StringFilter(GenericFilter[str]):
    like: Optional[str] = None
    ilike: Optional[str] = None


class AuditMetadata(StringFilter):
    key: str


class QueryFiltersCommon(BaseConfigModel):
    id: Optional[BaseConfigModel] = Field(None)
    date: Optional[BaseConfigModel] = Field(None, serialization_alias="event_date")
    user_id: Optional[GenericFilter[str]] = None
    user_type: Optional[GenericFilter[UserType]] = None
    client_type: Optional[GenericFilter[ClientType]] = None
    total_duration: Optional[GenericFilter[float]] = None
    audit_metadata: Optional[list[AuditMetadata]] = Field(
        None, serialization_alias="data.user_request.audit_metadata"
    )


class QueryFiltersSearch(QueryFiltersCommon):
    question: Optional[StringFilter] = Field(None, serialization_alias="data.user_request.query")
    resources_count: Optional[StringFilter] = Field(
        None,
        serialization_alias="data.resources_count",
    )
    filter: Optional[BaseConfigModel] = Field(None, serialization_alias="data.request.filter")
    learning_id: Optional[BaseConfigModel] = Field(None, serialization_alias="data.request.learning_id")


class QueryFiltersChat(QueryFiltersSearch):
    rephrased_question: Optional[StringFilter] = Field(
        None, serialization_alias="data.request.rephrased_question"
    )
    answer: Optional[StringFilter] = Field(None, serialization_alias="data.request.answer")
    retrieved_context: Optional[BaseConfigModel] = Field(None, serialization_alias="data.request.context")
    chat_history: Optional[BaseConfigModel] = Field(None, serialization_alias="data.request.chat_context")
    feedback_good: Optional[GenericFilter[bool]] = Field(
        None, serialization_alias="data.feedback.good", cast_to=bool
    )
    feedback_comment: Optional[StringFilter] = Field(None, serialization_alias="data.feedback.feedback")
    model: Optional[StringFilter] = Field(None, serialization_alias="data.request.model")
    rag_strategies_names: Optional[BaseConfigModel] = Field(None, serialization_alias="data.rag_strategies")
    rag_strategies: Optional[BaseConfigModel] = Field(
        None, serialization_alias="data.user_request.rag_strategies"
    )
    status: Optional[GenericFilter[int]] = Field(
        None, serialization_alias="data.request.status_code", cast_to=int
    )
    time_to_first_char: Optional[BaseConfigModel] = Field(
        None, serialization_alias="data.generative_answer_first_chunk_time"
    )


def create_dynamic_model(name: str, base_model: QueryFiltersChat):
    field_definitions = {}
    field_type_map = {
        "id": int,
        "user_type": Optional[UserType],
        "client_type": Optional[ClientType],
        "total_duration": Optional[float],
        "time_to_first_char": Optional[float],
    }
    for field_name in base_model.model_fields.keys():
        field_type = field_type_map.get(field_name, Optional[str])

        field_definitions[field_name] = (field_type, Field(default=None))

    return create_model(name, **field_definitions)


ActivityLogsQueryResponse = create_dynamic_model(
    name="ActivityLogsQueryResponse", base_model=QueryFiltersChat
)


class ActivityLogsQueryCommon(BaseConfigModel):
    year_month: str

    @field_validator("year_month")
    def validate_year_month(cls, value):
        if not re.match(r"^\d{4}-(0[1-9]|1[0-2])$", value):
            raise ValueError("year_month must be in the format YYYY-MM")
        return value

    @staticmethod
    def _validate_show(show: set[str], model: type[QueryFiltersCommon]):
        allowed_fields = list(model.model_fields.keys())
        for field in show:
            if field.startswith("audit_metadata."):
                continue
            if field not in allowed_fields:
                raise ValueError(f"{field} is not a field. List of fields: {allowed_fields}")
        return show


class ActivityLogs(ActivityLogsQueryCommon):
    show: set[str] = set()
    filters: QueryFiltersCommon

    @field_validator("show")
    def validate_show(cls, show: set[str]):
        return cls._validate_show(show=show, model=QueryFiltersCommon)


class ActivityLogsChat(ActivityLogsQueryCommon):
    show: set[str] = set()
    filters: QueryFiltersChat

    @field_validator("show")
    def validate_show(cls, show: set[str]):
        return cls._validate_show(show=show, model=QueryFiltersChat)


class ActivityLogsSearch(ActivityLogsQueryCommon):
    show: set[str] = set()
    filters: QueryFiltersSearch

    @field_validator("show")
    def validate_show(cls, show: set[str]):
        return cls._validate_show(show=show, model=QueryFiltersSearch)


class ActivityLogsSearchQuery(ActivityLogsSearch):
    pagination: Pagination = Pagination()


class ActivityLogsChatQuery(ActivityLogsChat):
    pagination: Pagination = Pagination()


class ActivityLogsQuery(ActivityLogs):
    pagination: Pagination = Pagination()


class DownloadRequestType(str, Enum):
    QUERY = "query"


class DownloadFormat(str, Enum):
    NDJSON = "ndjson"
    CSV = "csv"


class DownloadRequest(BaseModel):
    id: Annotated[int, Field(exclude=True)]
    request_id: str
    download_type: DownloadRequestType
    download_format: DownloadFormat
    event_type: EventType
    requested_at: datetime
    user_id: Annotated[str, Field(exclude=True)]
    kb_id: str
    query: Annotated[dict[Any, Any], Field(exclude=True)]
    download_url: Optional[str]

    # Configuration for Pydantic v2 to handle ORM mapping
    class Config:
        from_attributes = True


class DownloadActivityLogsQueryMixin(BaseModel):
    email_address: Optional[EmailStr] = Field(default=None)
    notify_via_email: bool = Field(default=False)

    @field_validator("notify_via_email")
    def check_email_if_notify(cls, value, values):
        if values.data.get("email_address") is None and value is True:
            raise ValueError("An email_address must be provided if notify_via_email is set to True.")
        return value


class DownloadActivityLogsSearchQuery(DownloadActivityLogsQueryMixin, ActivityLogsSearch):
    pass


class DownloadActivityLogsChatQuery(DownloadActivityLogsQueryMixin, ActivityLogsChat):
    pass


class DownloadActivityLogsQuery(DownloadActivityLogsQueryMixin, ActivityLogs):
    pass
