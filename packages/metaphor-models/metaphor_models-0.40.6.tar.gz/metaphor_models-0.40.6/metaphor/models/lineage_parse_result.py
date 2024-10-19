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


class Target(Enum):
    CLL = "CLL"
    OTHERS = "OTHERS"
    TLL = "TLL"


@dataclass
class ParseWarning:
    message: Optional[str] = None
    target: Optional[Target] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ParseWarning':
        assert isinstance(obj, dict)
        message = from_union([from_str, from_none], obj.get("message"))
        target = from_union([Target, from_none], obj.get("target"))
        return ParseWarning(message, target)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.message is not None:
            result["message"] = from_union([from_str, from_none], self.message)
        if self.target is not None:
            result["target"] = from_union([lambda x: to_enum(Target, x), from_none], self.target)
        return result


@dataclass
class LineageParseResult:
    id: Optional[str] = None
    """The ID for this lineage parse result. Value should be the MD5 hash of the SQL query and
    the processed entity's ID.
    """
    processed_at: Optional[datetime] = None
    """The date when the lineage parser result is generated."""

    sql: Optional[str] = None
    """The SQL query."""

    target_entity_id: Optional[str] = None
    """This is the EntityId of the lineage parser run's target entity."""

    warnings: Optional[List[ParseWarning]] = None
    """Warnings generated during lineage parsing. If there is no warning, we don't store the
    parsed result into MongoDB.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'LineageParseResult':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("_id"))
        processed_at = from_union([from_datetime, from_none], obj.get("processedAt"))
        sql = from_union([from_str, from_none], obj.get("sql"))
        target_entity_id = from_union([from_str, from_none], obj.get("targetEntityId"))
        warnings = from_union([lambda x: from_list(ParseWarning.from_dict, x), from_none], obj.get("warnings"))
        return LineageParseResult(id, processed_at, sql, target_entity_id, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.processed_at is not None:
            result["processedAt"] = from_union([lambda x: x.isoformat(), from_none], self.processed_at)
        if self.sql is not None:
            result["sql"] = from_union([from_str, from_none], self.sql)
        if self.target_entity_id is not None:
            result["targetEntityId"] = from_union([from_str, from_none], self.target_entity_id)
        if self.warnings is not None:
            result["warnings"] = from_union([lambda x: from_list(lambda x: to_class(ParseWarning, x), x), from_none], self.warnings)
        return result


def lineage_parse_result_from_dict(s: Any) -> LineageParseResult:
    return LineageParseResult.from_dict(s)


def lineage_parse_result_to_dict(x: LineageParseResult) -> Any:
    return to_class(LineageParseResult, x)
