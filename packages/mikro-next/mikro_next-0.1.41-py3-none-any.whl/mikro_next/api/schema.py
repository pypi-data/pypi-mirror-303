from typing import Optional, Tuple, Union, AsyncIterator, Any, Iterator, List, Literal
from mikro_next.scalars import (
    Upload,
    Milliseconds,
    Micrograms,
    ParquetLike,
    Micrometers,
    ArrayLike,
    FiveDVector,
    FourByFourMatrix,
    Microliters,
    FileLike,
)
from rath.scalars import ID
from mikro_next.traits import (
    HasDownloadAccessor,
    ExpressionTrait,
    HasPresignedDownloadAccessor,
    HasZarrStoreTrait,
    GraphTrait,
    HasParquestStoreTrait,
    HasParquetStoreAccesor,
    OntologyTrait,
    HasZarrStoreAccessor,
    EntityTrait,
    EntityRelationTrait,
    LinkedExpressionTrait,
    IsVectorizableTrait,
)
from pydantic import ConfigDict, BaseModel, Field
from mikro_next.funcs import subscribe, execute, aexecute, asubscribe
from mikro_next.rath import MikroNextRath
from datetime import datetime
from enum import Enum


class RoiKind(str, Enum):
    ELLIPSIS = "ELLIPSIS"
    POLYGON = "POLYGON"
    LINE = "LINE"
    RECTANGLE = "RECTANGLE"
    SPECTRAL_RECTANGLE = "SPECTRAL_RECTANGLE"
    TEMPORAL_RECTANGLE = "TEMPORAL_RECTANGLE"
    CUBE = "CUBE"
    SPECTRAL_CUBE = "SPECTRAL_CUBE"
    TEMPORAL_CUBE = "TEMPORAL_CUBE"
    HYPERCUBE = "HYPERCUBE"
    SPECTRAL_HYPERCUBE = "SPECTRAL_HYPERCUBE"
    PATH = "PATH"
    FRAME = "FRAME"
    SLICE = "SLICE"
    POINT = "POINT"


class ExpressionKind(str, Enum):
    RELATION = "RELATION"
    ENTITY = "ENTITY"
    METRIC = "METRIC"
    RELATION_METRIC = "RELATION_METRIC"
    CONCEPT = "CONCEPT"


class MetricDataType(str, Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    DATETIME = "DATETIME"
    STRING = "STRING"
    CATEGORY = "CATEGORY"
    BOOLEAN = "BOOLEAN"
    THREE_D_VECTOR = "THREE_D_VECTOR"
    TWO_D_VECTOR = "TWO_D_VECTOR"
    ONE_D_VECTOR = "ONE_D_VECTOR"
    FOUR_D_VECTOR = "FOUR_D_VECTOR"
    N_VECTOR = "N_VECTOR"


class ProtocolStepKind(str, Enum):
    PREPERATION = "PREPERATION"
    ADD_REAGENT = "ADD_REAGENT"
    MEASUREMENT = "MEASUREMENT"
    ANALYSIS = "ANALYSIS"
    STORAGE = "STORAGE"
    CUSTOM = "CUSTOM"
    UNKNOWN = "UNKNOWN"


class ColorMap(str, Enum):
    VIRIDIS = "VIRIDIS"
    PLASMA = "PLASMA"
    INFERNO = "INFERNO"
    MAGMA = "MAGMA"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    INTENSITY = "INTENSITY"


class Blending(str, Enum):
    ADDITIVE = "ADDITIVE"
    MULTIPLICATIVE = "MULTIPLICATIVE"


class RenderNodeKind(str, Enum):
    CONTEXT = "CONTEXT"
    OVERLAY = "OVERLAY"
    GRID = "GRID"
    SPIT = "SPIT"


class ProvenanceFilter(BaseModel):
    during: Optional[str] = None
    and_: Optional["ProvenanceFilter"] = Field(alias="AND", default=None)
    or_: Optional["ProvenanceFilter"] = Field(alias="OR", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class StrFilterLookup(BaseModel):
    exact: Optional[str] = None
    i_exact: Optional[str] = Field(alias="iExact", default=None)
    contains: Optional[str] = None
    i_contains: Optional[str] = Field(alias="iContains", default=None)
    in_list: Optional[Tuple[str, ...]] = Field(alias="inList", default=None)
    gt: Optional[str] = None
    gte: Optional[str] = None
    lt: Optional[str] = None
    lte: Optional[str] = None
    starts_with: Optional[str] = Field(alias="startsWith", default=None)
    i_starts_with: Optional[str] = Field(alias="iStartsWith", default=None)
    ends_with: Optional[str] = Field(alias="endsWith", default=None)
    i_ends_with: Optional[str] = Field(alias="iEndsWith", default=None)
    range: Optional[Tuple[str, ...]] = None
    is_null: Optional[bool] = Field(alias="isNull", default=None)
    regex: Optional[str] = None
    i_regex: Optional[str] = Field(alias="iRegex", default=None)
    n_exact: Optional[str] = Field(alias="nExact", default=None)
    n_i_exact: Optional[str] = Field(alias="nIExact", default=None)
    n_contains: Optional[str] = Field(alias="nContains", default=None)
    n_i_contains: Optional[str] = Field(alias="nIContains", default=None)
    n_in_list: Optional[Tuple[str, ...]] = Field(alias="nInList", default=None)
    n_gt: Optional[str] = Field(alias="nGt", default=None)
    n_gte: Optional[str] = Field(alias="nGte", default=None)
    n_lt: Optional[str] = Field(alias="nLt", default=None)
    n_lte: Optional[str] = Field(alias="nLte", default=None)
    n_starts_with: Optional[str] = Field(alias="nStartsWith", default=None)
    n_i_starts_with: Optional[str] = Field(alias="nIStartsWith", default=None)
    n_ends_with: Optional[str] = Field(alias="nEndsWith", default=None)
    n_i_ends_with: Optional[str] = Field(alias="nIEndsWith", default=None)
    n_range: Optional[Tuple[str, ...]] = Field(alias="nRange", default=None)
    n_is_null: Optional[bool] = Field(alias="nIsNull", default=None)
    n_regex: Optional[str] = Field(alias="nRegex", default=None)
    n_i_regex: Optional[str] = Field(alias="nIRegex", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class OffsetPaginationInput(BaseModel):
    offset: int
    limit: int
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class ImageFilter(BaseModel):
    name: Optional[StrFilterLookup] = None
    ids: Optional[Tuple[ID, ...]] = None
    store: Optional["ZarrStoreFilter"] = None
    dataset: Optional["DatasetFilter"] = None
    transformation_views: Optional["AffineTransformationViewFilter"] = Field(
        alias="transformationViews", default=None
    )
    timepoint_views: Optional["TimepointViewFilter"] = Field(
        alias="timepointViews", default=None
    )
    not_derived: Optional[bool] = Field(alias="notDerived", default=None)
    provenance: Optional[ProvenanceFilter] = None
    and_: Optional["ImageFilter"] = Field(alias="AND", default=None)
    or_: Optional["ImageFilter"] = Field(alias="OR", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class ZarrStoreFilter(BaseModel):
    shape: Optional["IntFilterLookup"] = None
    and_: Optional["ZarrStoreFilter"] = Field(alias="AND", default=None)
    or_: Optional["ZarrStoreFilter"] = Field(alias="OR", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class IntFilterLookup(BaseModel):
    exact: Optional[int] = None
    i_exact: Optional[int] = Field(alias="iExact", default=None)
    contains: Optional[int] = None
    i_contains: Optional[int] = Field(alias="iContains", default=None)
    in_list: Optional[Tuple[int, ...]] = Field(alias="inList", default=None)
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    starts_with: Optional[int] = Field(alias="startsWith", default=None)
    i_starts_with: Optional[int] = Field(alias="iStartsWith", default=None)
    ends_with: Optional[int] = Field(alias="endsWith", default=None)
    i_ends_with: Optional[int] = Field(alias="iEndsWith", default=None)
    range: Optional[Tuple[int, ...]] = None
    is_null: Optional[bool] = Field(alias="isNull", default=None)
    regex: Optional[str] = None
    i_regex: Optional[str] = Field(alias="iRegex", default=None)
    n_exact: Optional[int] = Field(alias="nExact", default=None)
    n_i_exact: Optional[int] = Field(alias="nIExact", default=None)
    n_contains: Optional[int] = Field(alias="nContains", default=None)
    n_i_contains: Optional[int] = Field(alias="nIContains", default=None)
    n_in_list: Optional[Tuple[int, ...]] = Field(alias="nInList", default=None)
    n_gt: Optional[int] = Field(alias="nGt", default=None)
    n_gte: Optional[int] = Field(alias="nGte", default=None)
    n_lt: Optional[int] = Field(alias="nLt", default=None)
    n_lte: Optional[int] = Field(alias="nLte", default=None)
    n_starts_with: Optional[int] = Field(alias="nStartsWith", default=None)
    n_i_starts_with: Optional[int] = Field(alias="nIStartsWith", default=None)
    n_ends_with: Optional[int] = Field(alias="nEndsWith", default=None)
    n_i_ends_with: Optional[int] = Field(alias="nIEndsWith", default=None)
    n_range: Optional[Tuple[int, ...]] = Field(alias="nRange", default=None)
    n_is_null: Optional[bool] = Field(alias="nIsNull", default=None)
    n_regex: Optional[str] = Field(alias="nRegex", default=None)
    n_i_regex: Optional[str] = Field(alias="nIRegex", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class DatasetFilter(BaseModel):
    id: Optional[ID] = None
    name: Optional[StrFilterLookup] = None
    provenance: Optional[ProvenanceFilter] = None
    and_: Optional["DatasetFilter"] = Field(alias="AND", default=None)
    or_: Optional["DatasetFilter"] = Field(alias="OR", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class AffineTransformationViewFilter(BaseModel):
    is_global: Optional[bool] = Field(alias="isGlobal", default=None)
    provenance: Optional[ProvenanceFilter] = None
    and_: Optional["AffineTransformationViewFilter"] = Field(alias="AND", default=None)
    or_: Optional["AffineTransformationViewFilter"] = Field(alias="OR", default=None)
    stage: Optional["StageFilter"] = None
    pixel_size: Optional["FloatFilterLookup"] = Field(alias="pixelSize", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class StageFilter(BaseModel):
    ids: Optional[Tuple[ID, ...]] = None
    search: Optional[str] = None
    id: Optional[ID] = None
    kind: Optional[str] = None
    name: Optional[StrFilterLookup] = None
    provenance: Optional[ProvenanceFilter] = None
    and_: Optional["StageFilter"] = Field(alias="AND", default=None)
    or_: Optional["StageFilter"] = Field(alias="OR", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class FloatFilterLookup(BaseModel):
    exact: Optional[float] = None
    i_exact: Optional[float] = Field(alias="iExact", default=None)
    contains: Optional[float] = None
    i_contains: Optional[float] = Field(alias="iContains", default=None)
    in_list: Optional[Tuple[float, ...]] = Field(alias="inList", default=None)
    gt: Optional[float] = None
    gte: Optional[float] = None
    lt: Optional[float] = None
    lte: Optional[float] = None
    starts_with: Optional[float] = Field(alias="startsWith", default=None)
    i_starts_with: Optional[float] = Field(alias="iStartsWith", default=None)
    ends_with: Optional[float] = Field(alias="endsWith", default=None)
    i_ends_with: Optional[float] = Field(alias="iEndsWith", default=None)
    range: Optional[Tuple[float, ...]] = None
    is_null: Optional[bool] = Field(alias="isNull", default=None)
    regex: Optional[str] = None
    i_regex: Optional[str] = Field(alias="iRegex", default=None)
    n_exact: Optional[float] = Field(alias="nExact", default=None)
    n_i_exact: Optional[float] = Field(alias="nIExact", default=None)
    n_contains: Optional[float] = Field(alias="nContains", default=None)
    n_i_contains: Optional[float] = Field(alias="nIContains", default=None)
    n_in_list: Optional[Tuple[float, ...]] = Field(alias="nInList", default=None)
    n_gt: Optional[float] = Field(alias="nGt", default=None)
    n_gte: Optional[float] = Field(alias="nGte", default=None)
    n_lt: Optional[float] = Field(alias="nLt", default=None)
    n_lte: Optional[float] = Field(alias="nLte", default=None)
    n_starts_with: Optional[float] = Field(alias="nStartsWith", default=None)
    n_i_starts_with: Optional[float] = Field(alias="nIStartsWith", default=None)
    n_ends_with: Optional[float] = Field(alias="nEndsWith", default=None)
    n_i_ends_with: Optional[float] = Field(alias="nIEndsWith", default=None)
    n_range: Optional[Tuple[float, ...]] = Field(alias="nRange", default=None)
    n_is_null: Optional[bool] = Field(alias="nIsNull", default=None)
    n_regex: Optional[str] = Field(alias="nRegex", default=None)
    n_i_regex: Optional[str] = Field(alias="nIRegex", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class TimepointViewFilter(BaseModel):
    is_global: Optional[bool] = Field(alias="isGlobal", default=None)
    provenance: Optional[ProvenanceFilter] = None
    and_: Optional["TimepointViewFilter"] = Field(alias="AND", default=None)
    or_: Optional["TimepointViewFilter"] = Field(alias="OR", default=None)
    era: Optional["EraFilter"] = None
    ms_since_start: Optional[float] = Field(alias="msSinceStart", default=None)
    index_since_start: Optional[int] = Field(alias="indexSinceStart", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class EraFilter(BaseModel):
    id: Optional[ID] = None
    begin: Optional[datetime] = None
    provenance: Optional[ProvenanceFilter] = None
    and_: Optional["EraFilter"] = Field(alias="AND", default=None)
    or_: Optional["EraFilter"] = Field(alias="OR", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class LinkedExpressionFilter(BaseModel):
    graph: Optional[ID] = None
    search: Optional[str] = None
    pinned: Optional[bool] = None
    kind: Optional[ExpressionKind] = None
    ids: Optional[Tuple[ID, ...]] = None
    and_: Optional["LinkedExpressionFilter"] = Field(alias="AND", default=None)
    or_: Optional["LinkedExpressionFilter"] = Field(alias="OR", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class EntityFilter(BaseModel):
    graph: Optional[ID] = None
    kind: Optional[ID] = None
    ids: Optional[Tuple[ID, ...]] = None
    linked_expression: Optional[ID] = Field(alias="linkedExpression", default=None)
    search: Optional[str] = None
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class GraphPaginationInput(BaseModel):
    limit: Optional[int] = None
    offset: Optional[int] = None
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialChannelViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    channel: ID
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialAffineTransformationViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    stage: Optional[ID] = None
    affine_matrix: FourByFourMatrix = Field(alias="affineMatrix")
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialAcquisitionViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    description: Optional[str] = None
    acquired_at: Optional[datetime] = Field(alias="acquiredAt", default=None)
    operator: Optional[ID] = None
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialPixelViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    linked_view: Optional[ID] = Field(alias="linkedView", default=None)
    range_labels: Optional[Tuple["RangePixelLabel", ...]] = Field(
        alias="rangeLabels", default=None
    )
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class RangePixelLabel(BaseModel):
    group: Optional[ID] = None
    entity_kind: ID = Field(alias="entityKind")
    min: int
    max: int
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialSpecimenViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    entity: ID
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialRGBViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    context: Optional[ID] = None
    gamma: Optional[float] = None
    contrast_limit_min: Optional[float] = Field(alias="contrastLimitMin", default=None)
    contrast_limit_max: Optional[float] = Field(alias="contrastLimitMax", default=None)
    rescale: Optional[bool] = None
    scale: Optional[float] = None
    active: Optional[bool] = None
    color_map: Optional[ColorMap] = Field(alias="colorMap", default=None)
    base_color: Optional[Tuple[float, ...]] = Field(alias="baseColor", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialTimepointViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    era: Optional[ID] = None
    ms_since_start: Optional[Milliseconds] = Field(alias="msSinceStart", default=None)
    index_since_start: Optional[int] = Field(alias="indexSinceStart", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialOpticsViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    instrument: Optional[ID] = None
    objective: Optional[ID] = None
    camera: Optional[ID] = None
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class PartialScaleViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    parent: Optional[ID] = None
    scale_x: Optional[float] = Field(alias="scaleX", default=None)
    scale_y: Optional[float] = Field(alias="scaleY", default=None)
    scale_z: Optional[float] = Field(alias="scaleZ", default=None)
    scale_t: Optional[float] = Field(alias="scaleT", default=None)
    scale_c: Optional[float] = Field(alias="scaleC", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class TreeInput(BaseModel):
    id: Optional[str] = None
    children: Tuple["TreeNodeInput", ...]
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class TreeNodeInput(BaseModel):
    kind: RenderNodeKind
    label: Optional[str] = None
    context: Optional[str] = None
    gap: Optional[int] = None
    children: Optional[Tuple["TreeNodeInput", ...]] = None
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class OverlayInput(BaseModel):
    object: str
    identifier: str
    color: str
    x: int
    y: int
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class ProtocolStepInput(BaseModel):
    name: str
    kind: ProtocolStepKind
    expression: ID
    entity: Optional[ID] = None
    reagent: Optional[ID] = None
    description: Optional[str] = None
    performed_at: Optional[datetime] = Field(alias="performedAt", default=None)
    performed_by: Optional[ID] = Field(alias="performedBy", default=None)
    used_reagent: Optional[ID] = Field(alias="usedReagent", default=None)
    used_reagent_volume: Optional[Microliters] = Field(
        alias="usedReagentVolume", default=None
    )
    used_reagent_mass: Optional[Micrograms] = Field(
        alias="usedReagentMass", default=None
    )
    used_entity: Optional[ID] = Field(alias="usedEntity", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class CreateRGBContextInput(BaseModel):
    name: Optional[str] = None
    thumbnail: Optional[ID] = None
    image: ID
    views: Optional[Tuple[PartialRGBViewInput, ...]] = None
    z: Optional[int] = None
    t: Optional[int] = None
    c: Optional[int] = None
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class UpdateRGBContextInput(BaseModel):
    id: ID
    name: Optional[str] = None
    thumbnail: Optional[ID] = None
    views: Optional[Tuple[PartialRGBViewInput, ...]] = None
    z: Optional[int] = None
    t: Optional[int] = None
    c: Optional[int] = None
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class ProtocolStepViewInput(BaseModel):
    collection: Optional[ID] = None
    z_min: Optional[int] = Field(alias="zMin", default=None)
    z_max: Optional[int] = Field(alias="zMax", default=None)
    x_min: Optional[int] = Field(alias="xMin", default=None)
    x_max: Optional[int] = Field(alias="xMax", default=None)
    y_min: Optional[int] = Field(alias="yMin", default=None)
    y_max: Optional[int] = Field(alias="yMax", default=None)
    t_min: Optional[int] = Field(alias="tMin", default=None)
    t_max: Optional[int] = Field(alias="tMax", default=None)
    c_min: Optional[int] = Field(alias="cMin", default=None)
    c_max: Optional[int] = Field(alias="cMax", default=None)
    step: ID
    image: ID
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class UpdateRoiInput(BaseModel):
    roi: ID
    vectors: Optional[Tuple[FiveDVector, ...]] = None
    kind: Optional[RoiKind] = None
    entity: Optional[ID] = None
    entity_kind: Optional[ID] = Field(alias="entityKind", default=None)
    entity_group: Optional[ID] = Field(alias="entityGroup", default=None)
    entity_parent: Optional[ID] = Field(alias="entityParent", default=None)
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class RoiEntityRelationInput(BaseModel):
    left_roi: ID = Field(alias="leftRoi")
    right_roi: ID = Field(alias="rightRoi")
    kind: ID
    model_config = ConfigDict(
        frozen=True, extra="forbid", populate_by_name=True, use_enum_values=True
    )


class ViewBase(BaseModel):
    z_min: Optional[int] = Field(default=None, alias="zMin")
    z_max: Optional[int] = Field(default=None, alias="zMax")


class ChannelView(ViewBase, BaseModel):
    typename: Optional[Literal["ChannelView"]] = Field(
        alias="__typename", default="ChannelView", exclude=True
    )
    id: ID
    channel: "Channel"
    model_config = ConfigDict(frozen=True)


class SpecimenViewEntity(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class SpecimenView(ViewBase, BaseModel):
    typename: Optional[Literal["SpecimenView"]] = Field(
        alias="__typename", default="SpecimenView", exclude=True
    )
    entity: Optional[SpecimenViewEntity] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class ProtocolStepViewStep(BaseModel):
    typename: Optional[Literal["ProtocolStep"]] = Field(
        alias="__typename", default="ProtocolStep", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ProtocolStepView(ViewBase, BaseModel):
    typename: Optional[Literal["ProtocolStepView"]] = Field(
        alias="__typename", default="ProtocolStepView", exclude=True
    )
    id: ID
    step: ProtocolStepViewStep
    model_config = ConfigDict(frozen=True)


class AffineTransformationViewStage(BaseModel):
    typename: Optional[Literal["Stage"]] = Field(
        alias="__typename", default="Stage", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class AffineTransformationView(ViewBase, BaseModel):
    typename: Optional[Literal["AffineTransformationView"]] = Field(
        alias="__typename", default="AffineTransformationView", exclude=True
    )
    id: ID
    affine_matrix: FourByFourMatrix = Field(alias="affineMatrix")
    stage: AffineTransformationViewStage
    model_config = ConfigDict(frozen=True)


class TimepointView(ViewBase, BaseModel):
    typename: Optional[Literal["TimepointView"]] = Field(
        alias="__typename", default="TimepointView", exclude=True
    )
    id: ID
    ms_since_start: Optional[Milliseconds] = Field(default=None, alias="msSinceStart")
    index_since_start: Optional[int] = Field(default=None, alias="indexSinceStart")
    era: "Era"
    model_config = ConfigDict(frozen=True)


class OpticsViewObjective(BaseModel):
    typename: Optional[Literal["Objective"]] = Field(
        alias="__typename", default="Objective", exclude=True
    )
    id: ID
    name: str
    serial_number: str = Field(alias="serialNumber")
    model_config = ConfigDict(frozen=True)


class OpticsViewCamera(BaseModel):
    typename: Optional[Literal["Camera"]] = Field(
        alias="__typename", default="Camera", exclude=True
    )
    id: ID
    name: str
    serial_number: str = Field(alias="serialNumber")
    model_config = ConfigDict(frozen=True)


class OpticsViewInstrument(BaseModel):
    typename: Optional[Literal["Instrument"]] = Field(
        alias="__typename", default="Instrument", exclude=True
    )
    id: ID
    name: str
    serial_number: str = Field(alias="serialNumber")
    model_config = ConfigDict(frozen=True)


class OpticsView(ViewBase, BaseModel):
    typename: Optional[Literal["OpticsView"]] = Field(
        alias="__typename", default="OpticsView", exclude=True
    )
    objective: Optional[OpticsViewObjective] = Field(default=None)
    camera: Optional[OpticsViewCamera] = Field(default=None)
    instrument: Optional[OpticsViewInstrument] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class LabelView(ViewBase, BaseModel):
    typename: Optional[Literal["LabelView"]] = Field(
        alias="__typename", default="LabelView", exclude=True
    )
    id: ID
    label: str
    model_config = ConfigDict(frozen=True)


class ScaleView(ViewBase, BaseModel):
    typename: Optional[Literal["ScaleView"]] = Field(
        alias="__typename", default="ScaleView", exclude=True
    )
    id: ID
    scale_x: float = Field(alias="scaleX")
    scale_y: float = Field(alias="scaleY")
    scale_z: float = Field(alias="scaleZ")
    scale_t: float = Field(alias="scaleT")
    scale_c: float = Field(alias="scaleC")
    model_config = ConfigDict(frozen=True)


class RGBView(ViewBase, BaseModel):
    typename: Optional[Literal["RGBView"]] = Field(
        alias="__typename", default="RGBView", exclude=True
    )
    id: ID
    color_map: ColorMap = Field(alias="colorMap")
    contrast_limit_min: Optional[float] = Field(default=None, alias="contrastLimitMin")
    contrast_limit_max: Optional[float] = Field(default=None, alias="contrastLimitMax")
    gamma: Optional[float] = Field(default=None)
    rescale: bool
    active: bool
    c_min: Optional[int] = Field(default=None, alias="cMin")
    c_max: Optional[int] = Field(default=None, alias="cMax")
    full_colour: str = Field(alias="fullColour")
    base_color: Optional[Tuple[int, ...]] = Field(default=None, alias="baseColor")
    model_config = ConfigDict(frozen=True)


class LinkedExpressionGraph(GraphTrait, BaseModel):
    typename: Optional[Literal["Graph"]] = Field(
        alias="__typename", default="Graph", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class LinkedExpressionExpressionOntology(OntologyTrait, BaseModel):
    typename: Optional[Literal["Ontology"]] = Field(
        alias="__typename", default="Ontology", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class LinkedExpressionExpression(ExpressionTrait, BaseModel):
    typename: Optional[Literal["Expression"]] = Field(
        alias="__typename", default="Expression", exclude=True
    )
    id: ID
    label: str
    ontology: LinkedExpressionExpressionOntology
    model_config = ConfigDict(frozen=True)


class LinkedExpression(LinkedExpressionTrait, BaseModel):
    typename: Optional[Literal["LinkedExpression"]] = Field(
        alias="__typename", default="LinkedExpression", exclude=True
    )
    id: ID
    graph: LinkedExpressionGraph
    kind: ExpressionKind
    expression: LinkedExpressionExpression
    model_config = ConfigDict(frozen=True)


class ListLinkedExpressionGraph(GraphTrait, BaseModel):
    typename: Optional[Literal["Graph"]] = Field(
        alias="__typename", default="Graph", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ListLinkedExpressionExpressionOntology(OntologyTrait, BaseModel):
    typename: Optional[Literal["Ontology"]] = Field(
        alias="__typename", default="Ontology", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class ListLinkedExpressionExpression(ExpressionTrait, BaseModel):
    typename: Optional[Literal["Expression"]] = Field(
        alias="__typename", default="Expression", exclude=True
    )
    id: ID
    label: str
    ontology: ListLinkedExpressionExpressionOntology
    model_config = ConfigDict(frozen=True)


class ListLinkedExpression(LinkedExpressionTrait, BaseModel):
    typename: Optional[Literal["LinkedExpression"]] = Field(
        alias="__typename", default="LinkedExpression", exclude=True
    )
    id: ID
    graph: ListLinkedExpressionGraph
    kind: ExpressionKind
    expression: ListLinkedExpressionExpression
    model_config = ConfigDict(frozen=True)


class Camera(BaseModel):
    typename: Optional[Literal["Camera"]] = Field(
        alias="__typename", default="Camera", exclude=True
    )
    sensor_size_x: Optional[int] = Field(default=None, alias="sensorSizeX")
    sensor_size_y: Optional[int] = Field(default=None, alias="sensorSizeY")
    pixel_size_x: Optional[Micrometers] = Field(default=None, alias="pixelSizeX")
    pixel_size_y: Optional[Micrometers] = Field(default=None, alias="pixelSizeY")
    name: str
    serial_number: str = Field(alias="serialNumber")
    model_config = ConfigDict(frozen=True)


class TableOrigins(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class Table(HasParquestStoreTrait, BaseModel):
    typename: Optional[Literal["Table"]] = Field(
        alias="__typename", default="Table", exclude=True
    )
    origins: Tuple[TableOrigins, ...]
    id: ID
    name: str
    store: "ParquetStore"
    model_config = ConfigDict(frozen=True)


class RenderedPlotStore(HasPresignedDownloadAccessor, BaseModel):
    typename: Optional[Literal["MediaStore"]] = Field(
        alias="__typename", default="MediaStore", exclude=True
    )
    id: ID
    key: str
    model_config = ConfigDict(frozen=True)


class RenderedPlot(BaseModel):
    typename: Optional[Literal["RenderedPlot"]] = Field(
        alias="__typename", default="RenderedPlot", exclude=True
    )
    id: ID
    store: RenderedPlotStore
    model_config = ConfigDict(frozen=True)


class ListRenderedPlotStore(HasPresignedDownloadAccessor, BaseModel):
    typename: Optional[Literal["MediaStore"]] = Field(
        alias="__typename", default="MediaStore", exclude=True
    )
    id: ID
    key: str
    model_config = ConfigDict(frozen=True)


class ListRenderedPlot(BaseModel):
    typename: Optional[Literal["RenderedPlot"]] = Field(
        alias="__typename", default="RenderedPlot", exclude=True
    )
    id: ID
    store: ListRenderedPlotStore
    model_config = ConfigDict(frozen=True)


class Credentials(BaseModel):
    typename: Optional[Literal["Credentials"]] = Field(
        alias="__typename", default="Credentials", exclude=True
    )
    access_key: str = Field(alias="accessKey")
    status: str
    secret_key: str = Field(alias="secretKey")
    bucket: str
    key: str
    session_token: str = Field(alias="sessionToken")
    store: str
    model_config = ConfigDict(frozen=True)


class AccessCredentials(BaseModel):
    typename: Optional[Literal["AccessCredentials"]] = Field(
        alias="__typename", default="AccessCredentials", exclude=True
    )
    access_key: str = Field(alias="accessKey")
    secret_key: str = Field(alias="secretKey")
    bucket: str
    key: str
    session_token: str = Field(alias="sessionToken")
    path: str
    model_config = ConfigDict(frozen=True)


class FileOrigins(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class File(BaseModel):
    typename: Optional[Literal["File"]] = Field(
        alias="__typename", default="File", exclude=True
    )
    origins: Tuple[FileOrigins, ...]
    id: ID
    name: str
    store: "BigFileStore"
    model_config = ConfigDict(frozen=True)


class Stage(BaseModel):
    typename: Optional[Literal["Stage"]] = Field(
        alias="__typename", default="Stage", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class ROIImage(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ROI(IsVectorizableTrait, BaseModel):
    typename: Optional[Literal["ROI"]] = Field(
        alias="__typename", default="ROI", exclude=True
    )
    id: ID
    image: ROIImage
    vectors: Tuple[FiveDVector, ...]
    kind: RoiKind
    model_config = ConfigDict(frozen=True)


class Graph(GraphTrait, BaseModel):
    typename: Optional[Literal["Graph"]] = Field(
        alias="__typename", default="Graph", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class Objective(BaseModel):
    typename: Optional[Literal["Objective"]] = Field(
        alias="__typename", default="Objective", exclude=True
    )
    id: ID
    na: Optional[float] = Field(default=None)
    name: str
    serial_number: str = Field(alias="serialNumber")
    model_config = ConfigDict(frozen=True)


class RGBContextImage(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    id: ID
    store: "ZarrStore"
    "The store where the image data is stored."
    model_config = ConfigDict(frozen=True)


class RGBContext(BaseModel):
    typename: Optional[Literal["RGBContext"]] = Field(
        alias="__typename", default="RGBContext", exclude=True
    )
    id: ID
    views: Tuple[RGBView, ...]
    image: RGBContextImage
    pinned: bool
    name: str
    z: int
    t: int
    c: int
    blending: Blending
    model_config = ConfigDict(frozen=True)


class ProtocolStepExpression(ExpressionTrait, BaseModel):
    typename: Optional[Literal["Expression"]] = Field(
        alias="__typename", default="Expression", exclude=True
    )
    label: str
    model_config = ConfigDict(frozen=True)


class ProtocolStepForreagent(BaseModel):
    typename: Optional[Literal["Reagent"]] = Field(
        alias="__typename", default="Reagent", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ProtocolStepForentity(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ProtocolStepUsedentity(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ProtocolStepUsedreagent(BaseModel):
    typename: Optional[Literal["Reagent"]] = Field(
        alias="__typename", default="Reagent", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ProtocolStep(BaseModel):
    typename: Optional[Literal["ProtocolStep"]] = Field(
        alias="__typename", default="ProtocolStep", exclude=True
    )
    id: ID
    name: str
    kind: ProtocolStepKind
    expression: Optional[ProtocolStepExpression] = Field(default=None)
    description: Optional[str] = Field(default=None)
    for_reagent: Optional[ProtocolStepForreagent] = Field(
        default=None, alias="forReagent"
    )
    for_entity: Optional[ProtocolStepForentity] = Field(default=None, alias="forEntity")
    used_entity: Optional[ProtocolStepUsedentity] = Field(
        default=None, alias="usedEntity"
    )
    used_reagent: Optional[ProtocolStepUsedreagent] = Field(
        default=None, alias="usedReagent"
    )
    model_config = ConfigDict(frozen=True)


class HistoryStuffApp(BaseModel):
    """An app."""

    typename: Optional[Literal["App"]] = Field(
        alias="__typename", default="App", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class HistoryStuff(BaseModel):
    typename: Optional[Literal["History"]] = Field(
        alias="__typename", default="History", exclude=True
    )
    id: ID
    app: Optional[HistoryStuffApp] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class Dataset(BaseModel):
    typename: Optional[Literal["Dataset"]] = Field(
        alias="__typename", default="Dataset", exclude=True
    )
    name: str
    description: Optional[str] = Field(default=None)
    history: Tuple[HistoryStuff, ...]
    model_config = ConfigDict(frozen=True)


class Instrument(BaseModel):
    typename: Optional[Literal["Instrument"]] = Field(
        alias="__typename", default="Instrument", exclude=True
    )
    id: ID
    model: Optional[str] = Field(default=None)
    name: str
    serial_number: str = Field(alias="serialNumber")
    model_config = ConfigDict(frozen=True)


class ExpressionOntology(OntologyTrait, BaseModel):
    typename: Optional[Literal["Ontology"]] = Field(
        alias="__typename", default="Ontology", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class Expression(ExpressionTrait, BaseModel):
    typename: Optional[Literal["Expression"]] = Field(
        alias="__typename", default="Expression", exclude=True
    )
    id: ID
    label: str
    ontology: ExpressionOntology
    model_config = ConfigDict(frozen=True)


class EntityRelationLeft(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class EntityRelationRight(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class EntityRelationLinkedexpression(LinkedExpressionTrait, BaseModel):
    typename: Optional[Literal["LinkedExpression"]] = Field(
        alias="__typename", default="LinkedExpression", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class EntityRelation(EntityRelationTrait, BaseModel):
    typename: Optional[Literal["EntityRelation"]] = Field(
        alias="__typename", default="EntityRelation", exclude=True
    )
    id: ID
    left: EntityRelationLeft
    right: EntityRelationRight
    linked_expression: EntityRelationLinkedexpression = Field(alias="linkedExpression")
    model_config = ConfigDict(frozen=True)


class ReagentExpression(ExpressionTrait, BaseModel):
    typename: Optional[Literal["Expression"]] = Field(
        alias="__typename", default="Expression", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class Reagent(BaseModel):
    typename: Optional[Literal["Reagent"]] = Field(
        alias="__typename", default="Reagent", exclude=True
    )
    id: ID
    expression: Optional[ReagentExpression] = Field(default=None)
    lot_id: str = Field(alias="lotId")
    model_config = ConfigDict(frozen=True)


class ImageOrigins(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ImageViewsBase(BaseModel):
    pass
    model_config = ConfigDict(frozen=True)


class ImageViewsChannelView(ImageViewsBase, ChannelView):
    pass
    model_config = ConfigDict(frozen=True)


class ImageViewsAffineTransformationView(ImageViewsBase, AffineTransformationView):
    pass
    model_config = ConfigDict(frozen=True)


class ImageViewsLabelView(ImageViewsBase, LabelView):
    pass
    model_config = ConfigDict(frozen=True)


class ImageViewsTimepointView(ImageViewsBase, TimepointView):
    pass
    model_config = ConfigDict(frozen=True)


class ImageViewsOpticsView(ImageViewsBase, OpticsView):
    pass
    model_config = ConfigDict(frozen=True)


class ImageViewsScaleView(ImageViewsBase, ScaleView):
    pass
    model_config = ConfigDict(frozen=True)


class ImageViewsSpecimenView(ImageViewsBase, SpecimenView):
    pass
    model_config = ConfigDict(frozen=True)


class ImageSpecimenviewsEntity(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ImageSpecimenviews(BaseModel):
    typename: Optional[Literal["SpecimenView"]] = Field(
        alias="__typename", default="SpecimenView", exclude=True
    )
    id: ID
    entity: Optional[ImageSpecimenviewsEntity] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class ImageDerivedscaleviewsImage(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    name: str
    store: "ZarrStore"
    "The store where the image data is stored."
    model_config = ConfigDict(frozen=True)


class ImageDerivedscaleviews(ScaleView, BaseModel):
    typename: Optional[Literal["ScaleView"]] = Field(
        alias="__typename", default="ScaleView", exclude=True
    )
    image: ImageDerivedscaleviewsImage
    model_config = ConfigDict(frozen=True)


class ImageRgbcontexts(BaseModel):
    typename: Optional[Literal["RGBContext"]] = Field(
        alias="__typename", default="RGBContext", exclude=True
    )
    id: ID
    name: str
    views: Tuple[RGBView, ...]
    model_config = ConfigDict(frozen=True)


class Image(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    origins: Tuple[ImageOrigins, ...]
    id: ID
    name: str
    store: "ZarrStore"
    "The store where the image data is stored."
    views: Tuple[
        Union[
            ImageViewsChannelView,
            ImageViewsAffineTransformationView,
            ImageViewsLabelView,
            ImageViewsTimepointView,
            ImageViewsOpticsView,
            ImageViewsScaleView,
            ImageViewsSpecimenView,
        ],
        ...,
    ]
    specimen_views: Tuple[ImageSpecimenviews, ...] = Field(alias="specimenViews")
    derived_scale_views: Tuple[ImageDerivedscaleviews, ...] = Field(
        alias="derivedScaleViews"
    )
    rgb_contexts: Tuple[ImageRgbcontexts, ...] = Field(alias="rgbContexts")
    model_config = ConfigDict(frozen=True)


class EntityLinkedexpression(LinkedExpressionTrait, BaseModel):
    typename: Optional[Literal["LinkedExpression"]] = Field(
        alias="__typename", default="LinkedExpression", exclude=True
    )
    id: ID
    label: str
    model_config = ConfigDict(frozen=True)


class Entity(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    id: ID
    label: str
    linked_expression: EntityLinkedexpression = Field(alias="linkedExpression")
    model_config = ConfigDict(frozen=True)


class Era(BaseModel):
    typename: Optional[Literal["Era"]] = Field(
        alias="__typename", default="Era", exclude=True
    )
    id: ID
    begin: Optional[datetime] = Field(default=None)
    name: str
    model_config = ConfigDict(frozen=True)


class ProtocolExperiment(BaseModel):
    typename: Optional[Literal["Experiment"]] = Field(
        alias="__typename", default="Experiment", exclude=True
    )
    id: ID
    name: str
    description: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class Protocol(BaseModel):
    typename: Optional[Literal["Protocol"]] = Field(
        alias="__typename", default="Protocol", exclude=True
    )
    id: ID
    name: str
    experiment: ProtocolExperiment
    model_config = ConfigDict(frozen=True)


class SnapshotStore(HasPresignedDownloadAccessor, BaseModel):
    typename: Optional[Literal["MediaStore"]] = Field(
        alias="__typename", default="MediaStore", exclude=True
    )
    key: str
    presigned_url: str = Field(alias="presignedUrl")
    model_config = ConfigDict(frozen=True)


class Snapshot(BaseModel):
    typename: Optional[Literal["Snapshot"]] = Field(
        alias="__typename", default="Snapshot", exclude=True
    )
    id: ID
    store: SnapshotStore
    name: str
    model_config = ConfigDict(frozen=True)


class Ontology(OntologyTrait, BaseModel):
    typename: Optional[Literal["Ontology"]] = Field(
        alias="__typename", default="Ontology", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class ZarrStore(HasZarrStoreAccessor, BaseModel):
    typename: Optional[Literal["ZarrStore"]] = Field(
        alias="__typename", default="ZarrStore", exclude=True
    )
    id: ID
    key: str
    "The key where the data is stored."
    bucket: str
    "The bucket where the data is stored."
    path: Optional[str] = Field(default=None)
    "The path to the data. Relative to the bucket."
    model_config = ConfigDict(frozen=True)


class ParquetStore(HasParquetStoreAccesor, BaseModel):
    typename: Optional[Literal["ParquetStore"]] = Field(
        alias="__typename", default="ParquetStore", exclude=True
    )
    id: ID
    key: str
    bucket: str
    path: str
    model_config = ConfigDict(frozen=True)


class BigFileStore(HasDownloadAccessor, BaseModel):
    typename: Optional[Literal["BigFileStore"]] = Field(
        alias="__typename", default="BigFileStore", exclude=True
    )
    id: ID
    key: str
    bucket: str
    path: str
    presigned_url: str = Field(alias="presignedUrl")
    model_config = ConfigDict(frozen=True)


class Channel(BaseModel):
    typename: Optional[Literal["Channel"]] = Field(
        alias="__typename", default="Channel", exclude=True
    )
    id: ID
    name: str
    excitation_wavelength: Optional[float] = Field(
        default=None, alias="excitationWavelength"
    )
    model_config = ConfigDict(frozen=True)


class Experiment(BaseModel):
    typename: Optional[Literal["Experiment"]] = Field(
        alias="__typename", default="Experiment", exclude=True
    )
    id: ID
    name: str
    description: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class LinkExpressionMutation(BaseModel):
    link_expression: LinkedExpression = Field(alias="linkExpression")

    class Arguments(BaseModel):
        expression: ID
        graph: ID

    class Meta:
        document = "fragment LinkedExpression on LinkedExpression {\n  id\n  graph {\n    id\n  }\n  kind\n  expression {\n    id\n    label\n    ontology {\n      id\n      name\n    }\n  }\n}\n\nmutation LinkExpression($expression: ID!, $graph: ID!) {\n  linkExpression(input: {expression: $expression, graph: $graph}) {\n    ...LinkedExpression\n  }\n}"


class CreateCameraMutationCreatecamera(BaseModel):
    typename: Optional[Literal["Camera"]] = Field(
        alias="__typename", default="Camera", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class CreateCameraMutation(BaseModel):
    create_camera: CreateCameraMutationCreatecamera = Field(alias="createCamera")

    class Arguments(BaseModel):
        serial_number: str = Field(alias="serialNumber")
        name: Optional[str] = Field(default=None)
        pixel_size_x: Optional[Micrometers] = Field(alias="pixelSizeX", default=None)
        pixel_size_y: Optional[Micrometers] = Field(alias="pixelSizeY", default=None)
        sensor_size_x: Optional[int] = Field(alias="sensorSizeX", default=None)
        sensor_size_y: Optional[int] = Field(alias="sensorSizeY", default=None)

    class Meta:
        document = "mutation CreateCamera($serialNumber: String!, $name: String, $pixelSizeX: Micrometers, $pixelSizeY: Micrometers, $sensorSizeX: Int, $sensorSizeY: Int) {\n  createCamera(\n    input: {name: $name, pixelSizeX: $pixelSizeX, serialNumber: $serialNumber, pixelSizeY: $pixelSizeY, sensorSizeX: $sensorSizeX, sensorSizeY: $sensorSizeY}\n  ) {\n    id\n    name\n  }\n}"


class EnsureCameraMutationEnsurecamera(BaseModel):
    typename: Optional[Literal["Camera"]] = Field(
        alias="__typename", default="Camera", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class EnsureCameraMutation(BaseModel):
    ensure_camera: EnsureCameraMutationEnsurecamera = Field(alias="ensureCamera")

    class Arguments(BaseModel):
        serial_number: str = Field(alias="serialNumber")
        name: Optional[str] = Field(default=None)
        pixel_size_x: Optional[Micrometers] = Field(alias="pixelSizeX", default=None)
        pixel_size_y: Optional[Micrometers] = Field(alias="pixelSizeY", default=None)
        sensor_size_x: Optional[int] = Field(alias="sensorSizeX", default=None)
        sensor_size_y: Optional[int] = Field(alias="sensorSizeY", default=None)

    class Meta:
        document = "mutation EnsureCamera($serialNumber: String!, $name: String, $pixelSizeX: Micrometers, $pixelSizeY: Micrometers, $sensorSizeX: Int, $sensorSizeY: Int) {\n  ensureCamera(\n    input: {name: $name, pixelSizeX: $pixelSizeX, serialNumber: $serialNumber, pixelSizeY: $pixelSizeY, sensorSizeX: $sensorSizeX, sensorSizeY: $sensorSizeY}\n  ) {\n    id\n    name\n  }\n}"


class CreateRenderTreeMutationCreaterendertree(BaseModel):
    typename: Optional[Literal["RenderTree"]] = Field(
        alias="__typename", default="RenderTree", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class CreateRenderTreeMutation(BaseModel):
    create_render_tree: CreateRenderTreeMutationCreaterendertree = Field(
        alias="createRenderTree"
    )

    class Arguments(BaseModel):
        name: str
        tree: TreeInput

    class Meta:
        document = "mutation CreateRenderTree($name: String!, $tree: TreeInput!) {\n  createRenderTree(input: {name: $name, tree: $tree}) {\n    id\n  }\n}"


class From_parquet_likeMutation(BaseModel):
    from_parquet_like: Table = Field(alias="fromParquetLike")

    class Arguments(BaseModel):
        dataframe: ParquetLike
        name: str
        origins: Optional[List[ID]] = Field(default=None)
        dataset: Optional[ID] = Field(default=None)

    class Meta:
        document = "fragment ParquetStore on ParquetStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment Table on Table {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...ParquetStore\n  }\n}\n\nmutation from_parquet_like($dataframe: ParquetLike!, $name: String!, $origins: [ID!], $dataset: ID) {\n  fromParquetLike(\n    input: {dataframe: $dataframe, name: $name, origins: $origins, dataset: $dataset}\n  ) {\n    ...Table\n  }\n}"


class RequestTableUploadMutation(BaseModel):
    request_table_upload: Credentials = Field(alias="requestTableUpload")

    class Arguments(BaseModel):
        key: str
        datalayer: str

    class Meta:
        document = "fragment Credentials on Credentials {\n  accessKey\n  status\n  secretKey\n  bucket\n  key\n  sessionToken\n  store\n}\n\nmutation RequestTableUpload($key: String!, $datalayer: String!) {\n  requestTableUpload(input: {key: $key, datalayer: $datalayer}) {\n    ...Credentials\n  }\n}"


class RequestTableAccessMutation(BaseModel):
    request_table_access: AccessCredentials = Field(alias="requestTableAccess")

    class Arguments(BaseModel):
        store: ID
        duration: Optional[int] = Field(default=None)

    class Meta:
        document = "fragment AccessCredentials on AccessCredentials {\n  accessKey\n  secretKey\n  bucket\n  key\n  sessionToken\n  path\n}\n\nmutation RequestTableAccess($store: ID!, $duration: Int) {\n  requestTableAccess(input: {store: $store, duration: $duration}) {\n    ...AccessCredentials\n  }\n}"


class CreateRenderedPlotMutation(BaseModel):
    create_rendered_plot: RenderedPlot = Field(alias="createRenderedPlot")

    class Arguments(BaseModel):
        plot: Upload
        name: str
        overlays: Optional[List[OverlayInput]] = Field(default=None)

    class Meta:
        document = "fragment RenderedPlot on RenderedPlot {\n  id\n  store {\n    id\n    key\n  }\n}\n\nmutation CreateRenderedPlot($plot: Upload!, $name: String!, $overlays: [OverlayInput!]) {\n  createRenderedPlot(input: {plot: $plot, overlays: $overlays, name: $name}) {\n    ...RenderedPlot\n  }\n}"


class From_file_likeMutation(BaseModel):
    from_file_like: File = Field(alias="fromFileLike")

    class Arguments(BaseModel):
        file: FileLike
        name: str
        origins: Optional[List[ID]] = Field(default=None)
        dataset: Optional[ID] = Field(default=None)

    class Meta:
        document = "fragment BigFileStore on BigFileStore {\n  id\n  key\n  bucket\n  path\n  presignedUrl\n}\n\nfragment File on File {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...BigFileStore\n  }\n}\n\nmutation from_file_like($file: FileLike!, $name: String!, $origins: [ID!], $dataset: ID) {\n  fromFileLike(\n    input: {file: $file, name: $name, origins: $origins, dataset: $dataset}\n  ) {\n    ...File\n  }\n}"


class RequestFileUploadMutation(BaseModel):
    request_file_upload: Credentials = Field(alias="requestFileUpload")

    class Arguments(BaseModel):
        key: str
        datalayer: str

    class Meta:
        document = "fragment Credentials on Credentials {\n  accessKey\n  status\n  secretKey\n  bucket\n  key\n  sessionToken\n  store\n}\n\nmutation RequestFileUpload($key: String!, $datalayer: String!) {\n  requestFileUpload(input: {key: $key, datalayer: $datalayer}) {\n    ...Credentials\n  }\n}"


class RequestFileAccessMutation(BaseModel):
    request_file_access: AccessCredentials = Field(alias="requestFileAccess")

    class Arguments(BaseModel):
        store: ID
        duration: Optional[int] = Field(default=None)

    class Meta:
        document = "fragment AccessCredentials on AccessCredentials {\n  accessKey\n  secretKey\n  bucket\n  key\n  sessionToken\n  path\n}\n\nmutation RequestFileAccess($store: ID!, $duration: Int) {\n  requestFileAccess(input: {store: $store, duration: $duration}) {\n    ...AccessCredentials\n  }\n}"


class CreateStageMutation(BaseModel):
    create_stage: Stage = Field(alias="createStage")

    class Arguments(BaseModel):
        name: str

    class Meta:
        document = "fragment Stage on Stage {\n  id\n  name\n}\n\nmutation CreateStage($name: String!) {\n  createStage(input: {name: $name}) {\n    ...Stage\n  }\n}"


class CreateRoiMutation(BaseModel):
    create_roi: ROI = Field(alias="createRoi")

    class Arguments(BaseModel):
        image: ID
        vectors: List[FiveDVector]
        kind: RoiKind
        entity: Optional[ID] = Field(default=None)
        entity_kind: Optional[ID] = Field(alias="entityKind", default=None)
        entity_parent: Optional[ID] = Field(alias="entityParent", default=None)

    class Meta:
        document = "fragment ROI on ROI {\n  id\n  image {\n    id\n  }\n  vectors\n  kind\n}\n\nmutation CreateRoi($image: ID!, $vectors: [FiveDVector!]!, $kind: RoiKind!, $entity: ID, $entityKind: ID, $entityParent: ID) {\n  createRoi(\n    input: {image: $image, vectors: $vectors, kind: $kind, entity: $entity, entityKind: $entityKind, entityParent: $entityParent}\n  ) {\n    ...ROI\n  }\n}"


class DeleteRoiMutation(BaseModel):
    delete_roi: ID = Field(alias="deleteRoi")

    class Arguments(BaseModel):
        roi: ID

    class Meta:
        document = "mutation DeleteRoi($roi: ID!) {\n  deleteRoi(input: {id: $roi})\n}"


class UpdateRoiMutation(BaseModel):
    update_roi: ROI = Field(alias="updateRoi")

    class Arguments(BaseModel):
        input: UpdateRoiInput

    class Meta:
        document = "fragment ROI on ROI {\n  id\n  image {\n    id\n  }\n  vectors\n  kind\n}\n\nmutation UpdateRoi($input: UpdateRoiInput!) {\n  updateRoi(input: $input) {\n    ...ROI\n  }\n}"


class CreateGraphMutation(BaseModel):
    create_graph: Graph = Field(alias="createGraph")

    class Arguments(BaseModel):
        name: str

    class Meta:
        document = "fragment Graph on Graph {\n  id\n  name\n}\n\nmutation CreateGraph($name: String!) {\n  createGraph(input: {name: $name}) {\n    ...Graph\n  }\n}"


class CreateObjectiveMutationCreateobjective(BaseModel):
    typename: Optional[Literal["Objective"]] = Field(
        alias="__typename", default="Objective", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class CreateObjectiveMutation(BaseModel):
    create_objective: CreateObjectiveMutationCreateobjective = Field(
        alias="createObjective"
    )

    class Arguments(BaseModel):
        serial_number: str = Field(alias="serialNumber")
        name: Optional[str] = Field(default=None)
        na: Optional[float] = Field(default=None)
        magnification: Optional[float] = Field(default=None)

    class Meta:
        document = "mutation CreateObjective($serialNumber: String!, $name: String, $na: Float, $magnification: Float) {\n  createObjective(\n    input: {name: $name, na: $na, serialNumber: $serialNumber, magnification: $magnification}\n  ) {\n    id\n    name\n  }\n}"


class EnsureObjectiveMutationEnsureobjective(BaseModel):
    typename: Optional[Literal["Objective"]] = Field(
        alias="__typename", default="Objective", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class EnsureObjectiveMutation(BaseModel):
    ensure_objective: EnsureObjectiveMutationEnsureobjective = Field(
        alias="ensureObjective"
    )

    class Arguments(BaseModel):
        serial_number: str = Field(alias="serialNumber")
        name: Optional[str] = Field(default=None)
        na: Optional[float] = Field(default=None)
        magnification: Optional[float] = Field(default=None)

    class Meta:
        document = "mutation EnsureObjective($serialNumber: String!, $name: String, $na: Float, $magnification: Float) {\n  ensureObjective(\n    input: {name: $name, na: $na, serialNumber: $serialNumber, magnification: $magnification}\n  ) {\n    id\n    name\n  }\n}"


class CreateProtocolStepMutation(BaseModel):
    create_protocol_step: ProtocolStep = Field(alias="createProtocolStep")

    class Arguments(BaseModel):
        input: ProtocolStepInput

    class Meta:
        document = "fragment ProtocolStep on ProtocolStep {\n  id\n  name\n  kind\n  expression {\n    label\n  }\n  description\n  forReagent {\n    id\n  }\n  forEntity {\n    id\n  }\n  usedEntity {\n    id\n  }\n  usedReagent {\n    id\n  }\n}\n\nmutation CreateProtocolStep($input: ProtocolStepInput!) {\n  createProtocolStep(input: $input) {\n    ...ProtocolStep\n  }\n}"


class CreateDatasetMutationCreatedataset(BaseModel):
    typename: Optional[Literal["Dataset"]] = Field(
        alias="__typename", default="Dataset", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class CreateDatasetMutation(BaseModel):
    create_dataset: CreateDatasetMutationCreatedataset = Field(alias="createDataset")

    class Arguments(BaseModel):
        name: str

    class Meta:
        document = "mutation CreateDataset($name: String!) {\n  createDataset(input: {name: $name}) {\n    id\n    name\n  }\n}"


class UpdateDatasetMutationUpdatedataset(BaseModel):
    typename: Optional[Literal["Dataset"]] = Field(
        alias="__typename", default="Dataset", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class UpdateDatasetMutation(BaseModel):
    update_dataset: UpdateDatasetMutationUpdatedataset = Field(alias="updateDataset")

    class Arguments(BaseModel):
        id: ID
        name: str

    class Meta:
        document = "mutation UpdateDataset($id: ID!, $name: String!) {\n  updateDataset(input: {id: $id, name: $name}) {\n    id\n    name\n  }\n}"


class RevertDatasetMutationRevertdataset(BaseModel):
    typename: Optional[Literal["Dataset"]] = Field(
        alias="__typename", default="Dataset", exclude=True
    )
    id: ID
    name: str
    description: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class RevertDatasetMutation(BaseModel):
    revert_dataset: RevertDatasetMutationRevertdataset = Field(alias="revertDataset")

    class Arguments(BaseModel):
        dataset: ID
        history: ID

    class Meta:
        document = "mutation RevertDataset($dataset: ID!, $history: ID!) {\n  revertDataset(input: {id: $dataset, historyId: $history}) {\n    id\n    name\n    description\n  }\n}"


class CreateInstrumentMutationCreateinstrument(BaseModel):
    typename: Optional[Literal["Instrument"]] = Field(
        alias="__typename", default="Instrument", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class CreateInstrumentMutation(BaseModel):
    create_instrument: CreateInstrumentMutationCreateinstrument = Field(
        alias="createInstrument"
    )

    class Arguments(BaseModel):
        serial_number: str = Field(alias="serialNumber")
        name: Optional[str] = Field(default=None)
        model: Optional[str] = Field(default=None)

    class Meta:
        document = "mutation CreateInstrument($serialNumber: String!, $name: String, $model: String) {\n  createInstrument(\n    input: {name: $name, model: $model, serialNumber: $serialNumber}\n  ) {\n    id\n    name\n  }\n}"


class EnsureInstrumentMutationEnsureinstrument(BaseModel):
    typename: Optional[Literal["Instrument"]] = Field(
        alias="__typename", default="Instrument", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class EnsureInstrumentMutation(BaseModel):
    ensure_instrument: EnsureInstrumentMutationEnsureinstrument = Field(
        alias="ensureInstrument"
    )

    class Arguments(BaseModel):
        serial_number: str = Field(alias="serialNumber")
        name: Optional[str] = Field(default=None)
        model: Optional[str] = Field(default=None)

    class Meta:
        document = "mutation EnsureInstrument($serialNumber: String!, $name: String, $model: String) {\n  ensureInstrument(\n    input: {name: $name, model: $model, serialNumber: $serialNumber}\n  ) {\n    id\n    name\n  }\n}"


class CreateExpressionMutation(BaseModel):
    create_expression: Expression = Field(alias="createExpression")

    class Arguments(BaseModel):
        label: str
        ontology: Optional[ID] = Field(default=None)
        purl: Optional[str] = Field(default=None)
        description: Optional[str] = Field(default=None)
        color: Optional[List[int]] = Field(default=None)
        metric_kind: Optional[MetricDataType] = Field(alias="metricKind", default=None)
        kind: ExpressionKind

    class Meta:
        document = "fragment Expression on Expression {\n  id\n  label\n  ontology {\n    id\n    name\n  }\n}\n\nmutation CreateExpression($label: String!, $ontology: ID, $purl: String, $description: String, $color: [Int!], $metricKind: MetricDataType, $kind: ExpressionKind!) {\n  createExpression(\n    input: {label: $label, ontology: $ontology, description: $description, purl: $purl, color: $color, kind: $kind, metricKind: $metricKind}\n  ) {\n    ...Expression\n  }\n}"


class CreateEntityRelationMutation(BaseModel):
    create_entity_relation: EntityRelation = Field(alias="createEntityRelation")

    class Arguments(BaseModel):
        left: ID
        right: ID
        kind: ID

    class Meta:
        document = "fragment EntityRelation on EntityRelation {\n  id\n  left {\n    id\n  }\n  right {\n    id\n  }\n  linkedExpression {\n    id\n  }\n}\n\nmutation CreateEntityRelation($left: ID!, $right: ID!, $kind: ID!) {\n  createEntityRelation(input: {left: $left, right: $right, kind: $kind}) {\n    ...EntityRelation\n  }\n}"


class CreateRoiEntityRelationMutation(BaseModel):
    create_roi_entity_relation: EntityRelation = Field(alias="createRoiEntityRelation")

    class Arguments(BaseModel):
        input: RoiEntityRelationInput

    class Meta:
        document = "fragment EntityRelation on EntityRelation {\n  id\n  left {\n    id\n  }\n  right {\n    id\n  }\n  linkedExpression {\n    id\n  }\n}\n\nmutation CreateRoiEntityRelation($input: RoiEntityRelationInput!) {\n  createRoiEntityRelation(input: $input) {\n    ...EntityRelation\n  }\n}"


class CreateReagentMutation(BaseModel):
    create_reagent: Reagent = Field(alias="createReagent")

    class Arguments(BaseModel):
        expression: ID
        lot_id: str = Field(alias="lotId")

    class Meta:
        document = "fragment Reagent on Reagent {\n  id\n  expression {\n    id\n  }\n  lotId\n}\n\nmutation CreateReagent($expression: ID!, $lotId: String!) {\n  createReagent(input: {expression: $expression, lotId: $lotId}) {\n    ...Reagent\n  }\n}"


class CreateEntityMetricMutation(BaseModel):
    create_entity_metric: Entity = Field(alias="createEntityMetric")

    class Arguments(BaseModel):
        entity: ID
        metric: ID
        value: Any
        timepoint: Optional[datetime] = Field(default=None)

    class Meta:
        document = "fragment Entity on Entity {\n  id\n  label\n  linkedExpression {\n    id\n    label\n  }\n}\n\nmutation CreateEntityMetric($entity: ID!, $metric: ID!, $value: Metric!, $timepoint: DateTime) {\n  createEntityMetric(\n    input: {entity: $entity, metric: $metric, value: $value, timepoint: $timepoint}\n  ) {\n    ...Entity\n  }\n}"


class CreateRelationMetricMutation(BaseModel):
    create_relation_metric: EntityRelation = Field(alias="createRelationMetric")

    class Arguments(BaseModel):
        relation: ID
        metric: ID
        value: Any
        timepoint: Optional[datetime] = Field(default=None)

    class Meta:
        document = "fragment EntityRelation on EntityRelation {\n  id\n  left {\n    id\n  }\n  right {\n    id\n  }\n  linkedExpression {\n    id\n  }\n}\n\nmutation CreateRelationMetric($relation: ID!, $metric: ID!, $value: Metric!, $timepoint: DateTime) {\n  createRelationMetric(\n    input: {relation: $relation, metric: $metric, value: $value, timepoint: $timepoint}\n  ) {\n    ...EntityRelation\n  }\n}"


class From_array_likeMutation(BaseModel):
    from_array_like: Image = Field(alias="fromArrayLike")

    class Arguments(BaseModel):
        array: ArrayLike
        name: str
        origins: Optional[List[ID]] = Field(default=None)
        channel_views: Optional[List[PartialChannelViewInput]] = Field(
            alias="channelViews", default=None
        )
        transformation_views: Optional[List[PartialAffineTransformationViewInput]] = (
            Field(alias="transformationViews", default=None)
        )
        pixel_views: Optional[List[PartialPixelViewInput]] = Field(
            alias="pixelViews", default=None
        )
        rgb_views: Optional[List[PartialRGBViewInput]] = Field(
            alias="rgbViews", default=None
        )
        acquisition_views: Optional[List[PartialAcquisitionViewInput]] = Field(
            alias="acquisitionViews", default=None
        )
        timepoint_views: Optional[List[PartialTimepointViewInput]] = Field(
            alias="timepointViews", default=None
        )
        optics_views: Optional[List[PartialOpticsViewInput]] = Field(
            alias="opticsViews", default=None
        )
        specimen_views: Optional[List[PartialSpecimenViewInput]] = Field(
            alias="specimenViews", default=None
        )
        scale_views: Optional[List[PartialScaleViewInput]] = Field(
            alias="scaleViews", default=None
        )
        tags: Optional[List[str]] = Field(default=None)
        file_origins: Optional[List[ID]] = Field(alias="fileOrigins", default=None)
        roi_origins: Optional[List[ID]] = Field(alias="roiOrigins", default=None)

    class Meta:
        document = "fragment Channel on Channel {\n  id\n  name\n  excitationWavelength\n}\n\nfragment View on View {\n  zMin\n  zMax\n}\n\nfragment Era on Era {\n  id\n  begin\n  name\n}\n\nfragment TimepointView on TimepointView {\n  ...View\n  id\n  msSinceStart\n  indexSinceStart\n  era {\n    ...Era\n  }\n}\n\nfragment ScaleView on ScaleView {\n  ...View\n  id\n  scaleX\n  scaleY\n  scaleZ\n  scaleT\n  scaleC\n}\n\nfragment SpecimenView on SpecimenView {\n  ...View\n  entity {\n    id\n  }\n}\n\nfragment AffineTransformationView on AffineTransformationView {\n  ...View\n  id\n  affineMatrix\n  stage {\n    id\n  }\n}\n\nfragment OpticsView on OpticsView {\n  ...View\n  objective {\n    id\n    name\n    serialNumber\n  }\n  camera {\n    id\n    name\n    serialNumber\n  }\n  instrument {\n    id\n    name\n    serialNumber\n  }\n}\n\nfragment LabelView on LabelView {\n  ...View\n  id\n  label\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment ChannelView on ChannelView {\n  ...View\n  id\n  channel {\n    ...Channel\n  }\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment Image on Image {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...ZarrStore\n  }\n  views {\n    ...ChannelView\n    ...AffineTransformationView\n    ...LabelView\n    ...TimepointView\n    ...OpticsView\n    ...ScaleView\n    ...SpecimenView\n  }\n  specimenViews {\n    id\n    entity {\n      id\n    }\n  }\n  derivedScaleViews {\n    ...ScaleView\n    image {\n      name\n      store {\n        ...ZarrStore\n      }\n    }\n  }\n  rgbContexts {\n    id\n    name\n    views {\n      ...RGBView\n    }\n  }\n}\n\nmutation from_array_like($array: ArrayLike!, $name: String!, $origins: [ID!], $channelViews: [PartialChannelViewInput!], $transformationViews: [PartialAffineTransformationViewInput!], $pixelViews: [PartialPixelViewInput!], $rgbViews: [PartialRGBViewInput!], $acquisitionViews: [PartialAcquisitionViewInput!], $timepointViews: [PartialTimepointViewInput!], $opticsViews: [PartialOpticsViewInput!], $specimenViews: [PartialSpecimenViewInput!], $scaleViews: [PartialScaleViewInput!], $tags: [String!], $fileOrigins: [ID!], $roiOrigins: [ID!]) {\n  fromArrayLike(\n    input: {array: $array, name: $name, origins: $origins, channelViews: $channelViews, transformationViews: $transformationViews, acquisitionViews: $acquisitionViews, pixelViews: $pixelViews, timepointViews: $timepointViews, opticsViews: $opticsViews, rgbViews: $rgbViews, scaleViews: $scaleViews, tags: $tags, fileOrigins: $fileOrigins, roiOrigins: $roiOrigins, specimenViews: $specimenViews}\n  ) {\n    ...Image\n  }\n}"


class RequestUploadMutation(BaseModel):
    request_upload: Credentials = Field(alias="requestUpload")

    class Arguments(BaseModel):
        key: str
        datalayer: str

    class Meta:
        document = "fragment Credentials on Credentials {\n  accessKey\n  status\n  secretKey\n  bucket\n  key\n  sessionToken\n  store\n}\n\nmutation RequestUpload($key: String!, $datalayer: String!) {\n  requestUpload(input: {key: $key, datalayer: $datalayer}) {\n    ...Credentials\n  }\n}"


class RequestAccessMutation(BaseModel):
    request_access: AccessCredentials = Field(alias="requestAccess")
    "Request upload credentials for a given key"

    class Arguments(BaseModel):
        store: ID
        duration: Optional[int] = Field(default=None)

    class Meta:
        document = "fragment AccessCredentials on AccessCredentials {\n  accessKey\n  secretKey\n  bucket\n  key\n  sessionToken\n  path\n}\n\nmutation RequestAccess($store: ID!, $duration: Int) {\n  requestAccess(input: {store: $store, duration: $duration}) {\n    ...AccessCredentials\n  }\n}"


class CreateEntityMutation(BaseModel):
    create_entity: Entity = Field(alias="createEntity")

    class Arguments(BaseModel):
        kind: ID
        group: Optional[ID] = Field(default=None)
        name: Optional[str] = Field(default=None)
        parent: Optional[ID] = Field(default=None)
        instance_kind: Optional[str] = Field(default=None)

    class Meta:
        document = "fragment Entity on Entity {\n  id\n  label\n  linkedExpression {\n    id\n    label\n  }\n}\n\nmutation CreateEntity($kind: ID!, $group: ID, $name: String, $parent: ID, $instance_kind: String) {\n  createEntity(\n    input: {group: $group, kind: $kind, name: $name, parent: $parent, instanceKind: $instance_kind}\n  ) {\n    ...Entity\n  }\n}"


class CreateEraMutationCreateera(BaseModel):
    typename: Optional[Literal["Era"]] = Field(
        alias="__typename", default="Era", exclude=True
    )
    id: ID
    begin: Optional[datetime] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class CreateEraMutation(BaseModel):
    create_era: CreateEraMutationCreateera = Field(alias="createEra")

    class Arguments(BaseModel):
        name: str
        begin: Optional[datetime] = Field(default=None)

    class Meta:
        document = "mutation CreateEra($name: String!, $begin: DateTime) {\n  createEra(input: {name: $name, begin: $begin}) {\n    id\n    begin\n  }\n}"


class CreateProtocolMutation(BaseModel):
    create_protocol: Protocol = Field(alias="createProtocol")

    class Arguments(BaseModel):
        name: str
        experiment: ID
        description: Optional[str] = Field(default=None)

    class Meta:
        document = "fragment Protocol on Protocol {\n  id\n  name\n  experiment {\n    id\n    name\n    description\n  }\n}\n\nmutation CreateProtocol($name: String!, $experiment: ID!, $description: String) {\n  createProtocol(\n    input: {name: $name, experiment: $experiment, description: $description}\n  ) {\n    ...Protocol\n  }\n}"


class CreateSnapshotMutation(BaseModel):
    create_snapshot: Snapshot = Field(alias="createSnapshot")

    class Arguments(BaseModel):
        image: ID
        file: Upload

    class Meta:
        document = "fragment Snapshot on Snapshot {\n  id\n  store {\n    key\n    presignedUrl\n  }\n  name\n}\n\nmutation CreateSnapshot($image: ID!, $file: Upload!) {\n  createSnapshot(input: {file: $file, image: $image}) {\n    ...Snapshot\n  }\n}"


class CreateRgbViewMutationCreatergbview(BaseModel):
    typename: Optional[Literal["RGBView"]] = Field(
        alias="__typename", default="RGBView", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class CreateRgbViewMutation(BaseModel):
    create_rgb_view: CreateRgbViewMutationCreatergbview = Field(alias="createRgbView")

    class Arguments(BaseModel):
        image: ID
        context: ID
        gamma: Optional[float] = Field(default=None)
        contrast_limit_max: Optional[float] = Field(
            alias="contrastLimitMax", default=None
        )
        contrast_limit_min: Optional[float] = Field(
            alias="contrastLimitMin", default=None
        )
        rescale: Optional[bool] = Field(default=None)
        active: Optional[bool] = Field(default=None)
        color_map: Optional[ColorMap] = Field(alias="colorMap", default=None)
        base_color: Optional[List[float]] = Field(alias="baseColor", default=None)

    class Meta:
        document = "mutation CreateRgbView($image: ID!, $context: ID!, $gamma: Float, $contrastLimitMax: Float, $contrastLimitMin: Float, $rescale: Boolean, $active: Boolean, $colorMap: ColorMap, $baseColor: [Float!]) {\n  createRgbView(\n    input: {image: $image, context: $context, gamma: $gamma, contrastLimitMax: $contrastLimitMax, contrastLimitMin: $contrastLimitMin, rescale: $rescale, active: $active, colorMap: $colorMap, baseColor: $baseColor}\n  ) {\n    id\n  }\n}"


class CreateLabelViewMutation(BaseModel):
    create_label_view: LabelView = Field(alias="createLabelView")

    class Arguments(BaseModel):
        image: ID
        label: str

    class Meta:
        document = "fragment View on View {\n  zMin\n  zMax\n}\n\nfragment LabelView on LabelView {\n  ...View\n  id\n  label\n}\n\nmutation CreateLabelView($image: ID!, $label: String!) {\n  createLabelView(input: {image: $image, label: $label}) {\n    ...LabelView\n  }\n}"


class CreateProtocolStepViewMutation(BaseModel):
    create_protocol_step_view: ProtocolStepView = Field(alias="createProtocolStepView")

    class Arguments(BaseModel):
        input: ProtocolStepViewInput

    class Meta:
        document = "fragment View on View {\n  zMin\n  zMax\n}\n\nfragment ProtocolStepView on ProtocolStepView {\n  ...View\n  id\n  step {\n    id\n  }\n}\n\nmutation CreateProtocolStepView($input: ProtocolStepViewInput!) {\n  createProtocolStepView(input: $input) {\n    ...ProtocolStepView\n  }\n}"


class CreateOntologyMutation(BaseModel):
    create_ontology: Ontology = Field(alias="createOntology")

    class Arguments(BaseModel):
        name: str
        purl: Optional[str] = Field(default=None)
        description: Optional[str] = Field(default=None)

    class Meta:
        document = "fragment Ontology on Ontology {\n  id\n  name\n}\n\nmutation CreateOntology($name: String!, $purl: String, $description: String) {\n  createOntology(input: {name: $name, purl: $purl, description: $description}) {\n    ...Ontology\n  }\n}"


class CreateRGBContextMutation(BaseModel):
    create_rgb_context: RGBContext = Field(alias="createRgbContext")

    class Arguments(BaseModel):
        input: CreateRGBContextInput

    class Meta:
        document = "fragment View on View {\n  zMin\n  zMax\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment RGBContext on RGBContext {\n  id\n  views {\n    ...RGBView\n  }\n  image {\n    id\n    store {\n      ...ZarrStore\n    }\n  }\n  pinned\n  name\n  z\n  t\n  c\n  blending\n}\n\nmutation CreateRGBContext($input: CreateRGBContextInput!) {\n  createRgbContext(input: $input) {\n    ...RGBContext\n  }\n}"


class UpdateRGBContextMutation(BaseModel):
    update_rgb_context: RGBContext = Field(alias="updateRgbContext")
    "Update RGB Context"

    class Arguments(BaseModel):
        input: UpdateRGBContextInput

    class Meta:
        document = "fragment View on View {\n  zMin\n  zMax\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment RGBContext on RGBContext {\n  id\n  views {\n    ...RGBView\n  }\n  image {\n    id\n    store {\n      ...ZarrStore\n    }\n  }\n  pinned\n  name\n  z\n  t\n  c\n  blending\n}\n\nmutation UpdateRGBContext($input: UpdateRGBContextInput!) {\n  updateRgbContext(input: $input) {\n    ...RGBContext\n  }\n}"


class CreateViewCollectionMutationCreateviewcollection(BaseModel):
    typename: Optional[Literal["ViewCollection"]] = Field(
        alias="__typename", default="ViewCollection", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class CreateViewCollectionMutation(BaseModel):
    create_view_collection: CreateViewCollectionMutationCreateviewcollection = Field(
        alias="createViewCollection"
    )

    class Arguments(BaseModel):
        name: str

    class Meta:
        document = "mutation CreateViewCollection($name: String!) {\n  createViewCollection(input: {name: $name}) {\n    id\n    name\n  }\n}"


class CreateChannelMutationCreatechannel(BaseModel):
    typename: Optional[Literal["Channel"]] = Field(
        alias="__typename", default="Channel", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class CreateChannelMutation(BaseModel):
    create_channel: CreateChannelMutationCreatechannel = Field(alias="createChannel")

    class Arguments(BaseModel):
        name: str

    class Meta:
        document = "mutation CreateChannel($name: String!) {\n  createChannel(input: {name: $name}) {\n    id\n    name\n  }\n}"


class EnsureChannelMutationEnsurechannel(BaseModel):
    typename: Optional[Literal["Channel"]] = Field(
        alias="__typename", default="Channel", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class EnsureChannelMutation(BaseModel):
    ensure_channel: EnsureChannelMutationEnsurechannel = Field(alias="ensureChannel")

    class Arguments(BaseModel):
        name: str

    class Meta:
        document = "mutation EnsureChannel($name: String!) {\n  ensureChannel(input: {name: $name}) {\n    id\n    name\n  }\n}"


class CreateExperimentMutation(BaseModel):
    create_experiment: Experiment = Field(alias="createExperiment")

    class Arguments(BaseModel):
        name: str
        description: Optional[str] = Field(default=None)

    class Meta:
        document = "fragment Experiment on Experiment {\n  id\n  name\n  description\n}\n\nmutation CreateExperiment($name: String!, $description: String) {\n  createExperiment(input: {name: $name, description: $description}) {\n    ...Experiment\n  }\n}"


class GetLinkedExpressionQuery(BaseModel):
    linked_expression: LinkedExpression = Field(alias="linkedExpression")

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment LinkedExpression on LinkedExpression {\n  id\n  graph {\n    id\n  }\n  kind\n  expression {\n    id\n    label\n    ontology {\n      id\n      name\n    }\n  }\n}\n\nquery GetLinkedExpression($id: ID!) {\n  linkedExpression(id: $id) {\n    ...LinkedExpression\n  }\n}"


class SearchLinkedExpressionsQueryOptions(LinkedExpressionTrait, BaseModel):
    typename: Optional[Literal["LinkedExpression"]] = Field(
        alias="__typename", default="LinkedExpression", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchLinkedExpressionsQuery(BaseModel):
    options: Tuple[SearchLinkedExpressionsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchLinkedExpressions($search: String, $values: [ID!]) {\n  options: linkedExpressions(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: label\n  }\n}"


class ListLinkedExpressionsQuery(BaseModel):
    linked_expressions: Tuple[ListLinkedExpression, ...] = Field(
        alias="linkedExpressions"
    )

    class Arguments(BaseModel):
        filters: Optional[LinkedExpressionFilter] = Field(default=None)
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "fragment ListLinkedExpression on LinkedExpression {\n  id\n  graph {\n    id\n  }\n  kind\n  expression {\n    id\n    label\n    ontology {\n      id\n      name\n    }\n  }\n}\n\nquery ListLinkedExpressions($filters: LinkedExpressionFilter, $pagination: OffsetPaginationInput) {\n  linkedExpressions(filters: $filters, pagination: $pagination) {\n    ...ListLinkedExpression\n  }\n}"


class GetCameraQuery(BaseModel):
    camera: Camera

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Camera on Camera {\n  sensorSizeX\n  sensorSizeY\n  pixelSizeX\n  pixelSizeY\n  name\n  serialNumber\n}\n\nquery GetCamera($id: ID!) {\n  camera(id: $id) {\n    ...Camera\n  }\n}"


class GetTableQuery(BaseModel):
    table: Table

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment ParquetStore on ParquetStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment Table on Table {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...ParquetStore\n  }\n}\n\nquery GetTable($id: ID!) {\n  table(id: $id) {\n    ...Table\n  }\n}"


class GetRenderedPlotQuery(BaseModel):
    rendered_plot: RenderedPlot = Field(alias="renderedPlot")

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment RenderedPlot on RenderedPlot {\n  id\n  store {\n    id\n    key\n  }\n}\n\nquery GetRenderedPlot($id: ID!) {\n  renderedPlot(id: $id) {\n    ...RenderedPlot\n  }\n}"


class ListRenderedPlotsQuery(BaseModel):
    rendered_plots: Tuple[ListRenderedPlot, ...] = Field(alias="renderedPlots")

    class Arguments(BaseModel):
        pass

    class Meta:
        document = "fragment ListRenderedPlot on RenderedPlot {\n  id\n  store {\n    id\n    key\n  }\n}\n\nquery ListRenderedPlots {\n  renderedPlots {\n    ...ListRenderedPlot\n  }\n}"


class SearchRenderedPlotsQueryOptions(BaseModel):
    typename: Optional[Literal["RenderedPlot"]] = Field(
        alias="__typename", default="RenderedPlot", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchRenderedPlotsQuery(BaseModel):
    options: Tuple[SearchRenderedPlotsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchRenderedPlots($search: String, $values: [ID!]) {\n  options: renderedPlots(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetFileQuery(BaseModel):
    file: File

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment BigFileStore on BigFileStore {\n  id\n  key\n  bucket\n  path\n  presignedUrl\n}\n\nfragment File on File {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...BigFileStore\n  }\n}\n\nquery GetFile($id: ID!) {\n  file(id: $id) {\n    ...File\n  }\n}"


class SearchFilesQueryOptions(BaseModel):
    typename: Optional[Literal["File"]] = Field(
        alias="__typename", default="File", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchFilesQuery(BaseModel):
    options: Tuple[SearchFilesQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "query SearchFiles($search: String, $values: [ID!], $pagination: OffsetPaginationInput) {\n  options: files(\n    filters: {search: $search, ids: $values}\n    pagination: $pagination\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetStageQuery(BaseModel):
    stage: Stage

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Stage on Stage {\n  id\n  name\n}\n\nquery GetStage($id: ID!) {\n  stage(id: $id) {\n    ...Stage\n  }\n}"


class SearchStagesQueryOptions(BaseModel):
    typename: Optional[Literal["Stage"]] = Field(
        alias="__typename", default="Stage", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchStagesQuery(BaseModel):
    options: Tuple[SearchStagesQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "query SearchStages($search: String, $values: [ID!], $pagination: OffsetPaginationInput) {\n  options: stages(\n    filters: {search: $search, ids: $values}\n    pagination: $pagination\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetRoisQuery(BaseModel):
    rois: Tuple[ROI, ...]

    class Arguments(BaseModel):
        image: ID

    class Meta:
        document = "fragment ROI on ROI {\n  id\n  image {\n    id\n  }\n  vectors\n  kind\n}\n\nquery GetRois($image: ID!) {\n  rois(filters: {image: $image}) {\n    ...ROI\n  }\n}"


class GetRoiQuery(BaseModel):
    roi: ROI

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment ROI on ROI {\n  id\n  image {\n    id\n  }\n  vectors\n  kind\n}\n\nquery GetRoi($id: ID!) {\n  roi(id: $id) {\n    ...ROI\n  }\n}"


class SearchRoisQueryOptions(IsVectorizableTrait, BaseModel):
    typename: Optional[Literal["ROI"]] = Field(
        alias="__typename", default="ROI", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchRoisQuery(BaseModel):
    options: Tuple[SearchRoisQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchRois($search: String, $values: [ID!]) {\n  options: rois(filters: {search: $search, ids: $values}, pagination: {limit: 10}) {\n    value: id\n    label: name\n  }\n}"


class GetObjectiveQuery(BaseModel):
    objective: Objective

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Objective on Objective {\n  id\n  na\n  name\n  serialNumber\n}\n\nquery GetObjective($id: ID!) {\n  objective(id: $id) {\n    ...Objective\n  }\n}"


class GetProtocolStepQuery(BaseModel):
    protocol_step: ProtocolStep = Field(alias="protocolStep")

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment ProtocolStep on ProtocolStep {\n  id\n  name\n  kind\n  expression {\n    label\n  }\n  description\n  forReagent {\n    id\n  }\n  forEntity {\n    id\n  }\n  usedEntity {\n    id\n  }\n  usedReagent {\n    id\n  }\n}\n\nquery GetProtocolStep($id: ID!) {\n  protocolStep(id: $id) {\n    ...ProtocolStep\n  }\n}"


class SearchProtocolStepsQueryOptions(BaseModel):
    typename: Optional[Literal["ProtocolStep"]] = Field(
        alias="__typename", default="ProtocolStep", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchProtocolStepsQuery(BaseModel):
    options: Tuple[SearchProtocolStepsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchProtocolSteps($search: String, $values: [ID!]) {\n  options: protocolSteps(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetDatasetQuery(BaseModel):
    dataset: Dataset

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment HistoryStuff on History {\n  id\n  app {\n    id\n  }\n}\n\nfragment Dataset on Dataset {\n  name\n  description\n  history {\n    ...HistoryStuff\n  }\n}\n\nquery GetDataset($id: ID!) {\n  dataset(id: $id) {\n    ...Dataset\n  }\n}"


class GetInstrumentQuery(BaseModel):
    instrument: Instrument

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Instrument on Instrument {\n  id\n  model\n  name\n  serialNumber\n}\n\nquery GetInstrument($id: ID!) {\n  instrument(id: $id) {\n    ...Instrument\n  }\n}"


class GetEntityRelationQuery(BaseModel):
    entity_relation: EntityRelation = Field(alias="entityRelation")

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment EntityRelation on EntityRelation {\n  id\n  left {\n    id\n  }\n  right {\n    id\n  }\n  linkedExpression {\n    id\n  }\n}\n\nquery GetEntityRelation($id: ID!) {\n  entityRelation(id: $id) {\n    ...EntityRelation\n  }\n}"


class SearchEntityRelationsQueryOptions(EntityRelationTrait, BaseModel):
    typename: Optional[Literal["EntityRelation"]] = Field(
        alias="__typename", default="EntityRelation", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchEntityRelationsQuery(BaseModel):
    options: Tuple[SearchEntityRelationsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchEntityRelations($search: String, $values: [ID!]) {\n  options: entityRelations(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: label\n  }\n}"


class GetReagentQuery(BaseModel):
    reagent: Reagent

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Reagent on Reagent {\n  id\n  expression {\n    id\n  }\n  lotId\n}\n\nquery GetReagent($id: ID!) {\n  reagent(id: $id) {\n    ...Reagent\n  }\n}"


class SearchReagentsQueryOptions(BaseModel):
    typename: Optional[Literal["Reagent"]] = Field(
        alias="__typename", default="Reagent", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchReagentsQuery(BaseModel):
    options: Tuple[SearchReagentsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchReagents($search: String, $values: [ID!]) {\n  options: reagents(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: label\n  }\n}"


class GetImageQuery(BaseModel):
    image: Image

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Channel on Channel {\n  id\n  name\n  excitationWavelength\n}\n\nfragment View on View {\n  zMin\n  zMax\n}\n\nfragment Era on Era {\n  id\n  begin\n  name\n}\n\nfragment TimepointView on TimepointView {\n  ...View\n  id\n  msSinceStart\n  indexSinceStart\n  era {\n    ...Era\n  }\n}\n\nfragment ScaleView on ScaleView {\n  ...View\n  id\n  scaleX\n  scaleY\n  scaleZ\n  scaleT\n  scaleC\n}\n\nfragment SpecimenView on SpecimenView {\n  ...View\n  entity {\n    id\n  }\n}\n\nfragment AffineTransformationView on AffineTransformationView {\n  ...View\n  id\n  affineMatrix\n  stage {\n    id\n  }\n}\n\nfragment OpticsView on OpticsView {\n  ...View\n  objective {\n    id\n    name\n    serialNumber\n  }\n  camera {\n    id\n    name\n    serialNumber\n  }\n  instrument {\n    id\n    name\n    serialNumber\n  }\n}\n\nfragment LabelView on LabelView {\n  ...View\n  id\n  label\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment ChannelView on ChannelView {\n  ...View\n  id\n  channel {\n    ...Channel\n  }\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment Image on Image {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...ZarrStore\n  }\n  views {\n    ...ChannelView\n    ...AffineTransformationView\n    ...LabelView\n    ...TimepointView\n    ...OpticsView\n    ...ScaleView\n    ...SpecimenView\n  }\n  specimenViews {\n    id\n    entity {\n      id\n    }\n  }\n  derivedScaleViews {\n    ...ScaleView\n    image {\n      name\n      store {\n        ...ZarrStore\n      }\n    }\n  }\n  rgbContexts {\n    id\n    name\n    views {\n      ...RGBView\n    }\n  }\n}\n\nquery GetImage($id: ID!) {\n  image(id: $id) {\n    ...Image\n  }\n}"


class GetRandomImageQuery(BaseModel):
    random_image: Image = Field(alias="randomImage")

    class Arguments(BaseModel):
        pass

    class Meta:
        document = "fragment Channel on Channel {\n  id\n  name\n  excitationWavelength\n}\n\nfragment View on View {\n  zMin\n  zMax\n}\n\nfragment Era on Era {\n  id\n  begin\n  name\n}\n\nfragment TimepointView on TimepointView {\n  ...View\n  id\n  msSinceStart\n  indexSinceStart\n  era {\n    ...Era\n  }\n}\n\nfragment ScaleView on ScaleView {\n  ...View\n  id\n  scaleX\n  scaleY\n  scaleZ\n  scaleT\n  scaleC\n}\n\nfragment SpecimenView on SpecimenView {\n  ...View\n  entity {\n    id\n  }\n}\n\nfragment AffineTransformationView on AffineTransformationView {\n  ...View\n  id\n  affineMatrix\n  stage {\n    id\n  }\n}\n\nfragment OpticsView on OpticsView {\n  ...View\n  objective {\n    id\n    name\n    serialNumber\n  }\n  camera {\n    id\n    name\n    serialNumber\n  }\n  instrument {\n    id\n    name\n    serialNumber\n  }\n}\n\nfragment LabelView on LabelView {\n  ...View\n  id\n  label\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment ChannelView on ChannelView {\n  ...View\n  id\n  channel {\n    ...Channel\n  }\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment Image on Image {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...ZarrStore\n  }\n  views {\n    ...ChannelView\n    ...AffineTransformationView\n    ...LabelView\n    ...TimepointView\n    ...OpticsView\n    ...ScaleView\n    ...SpecimenView\n  }\n  specimenViews {\n    id\n    entity {\n      id\n    }\n  }\n  derivedScaleViews {\n    ...ScaleView\n    image {\n      name\n      store {\n        ...ZarrStore\n      }\n    }\n  }\n  rgbContexts {\n    id\n    name\n    views {\n      ...RGBView\n    }\n  }\n}\n\nquery GetRandomImage {\n  randomImage {\n    ...Image\n  }\n}"


class SearchImagesQueryOptions(HasZarrStoreTrait, BaseModel):
    typename: Optional[Literal["Image"]] = Field(
        alias="__typename", default="Image", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchImagesQuery(BaseModel):
    options: Tuple[SearchImagesQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchImages($search: String, $values: [ID!]) {\n  options: images(\n    filters: {name: {contains: $search}, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class ImagesQuery(BaseModel):
    images: Tuple[Image, ...]

    class Arguments(BaseModel):
        filter: Optional[ImageFilter] = Field(default=None)
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "fragment Channel on Channel {\n  id\n  name\n  excitationWavelength\n}\n\nfragment View on View {\n  zMin\n  zMax\n}\n\nfragment Era on Era {\n  id\n  begin\n  name\n}\n\nfragment TimepointView on TimepointView {\n  ...View\n  id\n  msSinceStart\n  indexSinceStart\n  era {\n    ...Era\n  }\n}\n\nfragment ScaleView on ScaleView {\n  ...View\n  id\n  scaleX\n  scaleY\n  scaleZ\n  scaleT\n  scaleC\n}\n\nfragment SpecimenView on SpecimenView {\n  ...View\n  entity {\n    id\n  }\n}\n\nfragment AffineTransformationView on AffineTransformationView {\n  ...View\n  id\n  affineMatrix\n  stage {\n    id\n  }\n}\n\nfragment OpticsView on OpticsView {\n  ...View\n  objective {\n    id\n    name\n    serialNumber\n  }\n  camera {\n    id\n    name\n    serialNumber\n  }\n  instrument {\n    id\n    name\n    serialNumber\n  }\n}\n\nfragment LabelView on LabelView {\n  ...View\n  id\n  label\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment ChannelView on ChannelView {\n  ...View\n  id\n  channel {\n    ...Channel\n  }\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment Image on Image {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...ZarrStore\n  }\n  views {\n    ...ChannelView\n    ...AffineTransformationView\n    ...LabelView\n    ...TimepointView\n    ...OpticsView\n    ...ScaleView\n    ...SpecimenView\n  }\n  specimenViews {\n    id\n    entity {\n      id\n    }\n  }\n  derivedScaleViews {\n    ...ScaleView\n    image {\n      name\n      store {\n        ...ZarrStore\n      }\n    }\n  }\n  rgbContexts {\n    id\n    name\n    views {\n      ...RGBView\n    }\n  }\n}\n\nquery Images($filter: ImageFilter, $pagination: OffsetPaginationInput) {\n  images(filters: $filter, pagination: $pagination) {\n    ...Image\n  }\n}"


class GetEntityQuery(BaseModel):
    entity: Entity

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Entity on Entity {\n  id\n  label\n  linkedExpression {\n    id\n    label\n  }\n}\n\nquery GetEntity($id: ID!) {\n  entity(id: $id) {\n    ...Entity\n  }\n}"


class SearchEntitiesQueryOptions(EntityTrait, BaseModel):
    typename: Optional[Literal["Entity"]] = Field(
        alias="__typename", default="Entity", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchEntitiesQuery(BaseModel):
    options: Tuple[SearchEntitiesQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchEntities($search: String, $values: [ID!]) {\n  options: entities(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: label\n  }\n}"


class EntitiesQuery(BaseModel):
    entities: Tuple[Entity, ...]

    class Arguments(BaseModel):
        filters: Optional[EntityFilter] = Field(default=None)
        pagination: Optional[GraphPaginationInput] = Field(default=None)

    class Meta:
        document = "fragment Entity on Entity {\n  id\n  label\n  linkedExpression {\n    id\n    label\n  }\n}\n\nquery Entities($filters: EntityFilter, $pagination: GraphPaginationInput) {\n  entities(filters: $filters, pagination: $pagination) {\n    ...Entity\n  }\n}"


class GetProtocolQuery(BaseModel):
    protocol: Protocol

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Protocol on Protocol {\n  id\n  name\n  experiment {\n    id\n    name\n    description\n  }\n}\n\nquery GetProtocol($id: ID!) {\n  protocol(id: $id) {\n    ...Protocol\n  }\n}"


class SearchProtocolsQueryOptions(BaseModel):
    typename: Optional[Literal["Protocol"]] = Field(
        alias="__typename", default="Protocol", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchProtocolsQuery(BaseModel):
    options: Tuple[SearchProtocolsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchProtocols($search: String, $values: [ID!]) {\n  options: protocols(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetSnapshotQuery(BaseModel):
    snapshot: Snapshot

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Snapshot on Snapshot {\n  id\n  store {\n    key\n    presignedUrl\n  }\n  name\n}\n\nquery GetSnapshot($id: ID!) {\n  snapshot(id: $id) {\n    ...Snapshot\n  }\n}"


class SearchSnapshotsQueryOptions(BaseModel):
    typename: Optional[Literal["Snapshot"]] = Field(
        alias="__typename", default="Snapshot", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchSnapshotsQuery(BaseModel):
    options: Tuple[SearchSnapshotsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchSnapshots($search: String, $values: [ID!]) {\n  options: snapshots(\n    filters: {name: {contains: $search}, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetOntologyQuery(BaseModel):
    ontology: Ontology

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Ontology on Ontology {\n  id\n  name\n}\n\nquery GetOntology($id: ID!) {\n  ontology(id: $id) {\n    ...Ontology\n  }\n}"


class SearchOntologiesQueryOptions(OntologyTrait, BaseModel):
    typename: Optional[Literal["Ontology"]] = Field(
        alias="__typename", default="Ontology", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchOntologiesQuery(BaseModel):
    options: Tuple[SearchOntologiesQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchOntologies($search: String, $values: [ID!]) {\n  options: ontologies(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetRGBContextQuery(BaseModel):
    rgbcontext: RGBContext

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment View on View {\n  zMin\n  zMax\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment RGBContext on RGBContext {\n  id\n  views {\n    ...RGBView\n  }\n  image {\n    id\n    store {\n      ...ZarrStore\n    }\n  }\n  pinned\n  name\n  z\n  t\n  c\n  blending\n}\n\nquery GetRGBContext($id: ID!) {\n  rgbcontext(id: $id) {\n    ...RGBContext\n  }\n}"


class WatchFilesSubscriptionFiles(BaseModel):
    typename: Optional[Literal["FileEvent"]] = Field(
        alias="__typename", default="FileEvent", exclude=True
    )
    create: Optional[File] = Field(default=None)
    delete: Optional[ID] = Field(default=None)
    update: Optional[File] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class WatchFilesSubscription(BaseModel):
    files: WatchFilesSubscriptionFiles

    class Arguments(BaseModel):
        dataset: Optional[ID] = Field(default=None)

    class Meta:
        document = "fragment BigFileStore on BigFileStore {\n  id\n  key\n  bucket\n  path\n  presignedUrl\n}\n\nfragment File on File {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...BigFileStore\n  }\n}\n\nsubscription WatchFiles($dataset: ID) {\n  files(dataset: $dataset) {\n    create {\n      ...File\n    }\n    delete\n    update {\n      ...File\n    }\n  }\n}"


class WatchImagesSubscriptionImages(BaseModel):
    typename: Optional[Literal["ImageEvent"]] = Field(
        alias="__typename", default="ImageEvent", exclude=True
    )
    create: Optional[Image] = Field(default=None)
    delete: Optional[ID] = Field(default=None)
    update: Optional[Image] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class WatchImagesSubscription(BaseModel):
    images: WatchImagesSubscriptionImages

    class Arguments(BaseModel):
        dataset: Optional[ID] = Field(default=None)

    class Meta:
        document = "fragment Channel on Channel {\n  id\n  name\n  excitationWavelength\n}\n\nfragment View on View {\n  zMin\n  zMax\n}\n\nfragment Era on Era {\n  id\n  begin\n  name\n}\n\nfragment TimepointView on TimepointView {\n  ...View\n  id\n  msSinceStart\n  indexSinceStart\n  era {\n    ...Era\n  }\n}\n\nfragment ScaleView on ScaleView {\n  ...View\n  id\n  scaleX\n  scaleY\n  scaleZ\n  scaleT\n  scaleC\n}\n\nfragment SpecimenView on SpecimenView {\n  ...View\n  entity {\n    id\n  }\n}\n\nfragment AffineTransformationView on AffineTransformationView {\n  ...View\n  id\n  affineMatrix\n  stage {\n    id\n  }\n}\n\nfragment OpticsView on OpticsView {\n  ...View\n  objective {\n    id\n    name\n    serialNumber\n  }\n  camera {\n    id\n    name\n    serialNumber\n  }\n  instrument {\n    id\n    name\n    serialNumber\n  }\n}\n\nfragment LabelView on LabelView {\n  ...View\n  id\n  label\n}\n\nfragment ZarrStore on ZarrStore {\n  id\n  key\n  bucket\n  path\n}\n\nfragment ChannelView on ChannelView {\n  ...View\n  id\n  channel {\n    ...Channel\n  }\n}\n\nfragment RGBView on RGBView {\n  ...View\n  id\n  colorMap\n  contrastLimitMin\n  contrastLimitMax\n  gamma\n  rescale\n  active\n  cMin\n  cMax\n  fullColour\n  baseColor\n}\n\nfragment Image on Image {\n  origins {\n    id\n  }\n  id\n  name\n  store {\n    ...ZarrStore\n  }\n  views {\n    ...ChannelView\n    ...AffineTransformationView\n    ...LabelView\n    ...TimepointView\n    ...OpticsView\n    ...ScaleView\n    ...SpecimenView\n  }\n  specimenViews {\n    id\n    entity {\n      id\n    }\n  }\n  derivedScaleViews {\n    ...ScaleView\n    image {\n      name\n      store {\n        ...ZarrStore\n      }\n    }\n  }\n  rgbContexts {\n    id\n    name\n    views {\n      ...RGBView\n    }\n  }\n}\n\nsubscription WatchImages($dataset: ID) {\n  images(dataset: $dataset) {\n    create {\n      ...Image\n    }\n    delete\n    update {\n      ...Image\n    }\n  }\n}"


class WatchRoisSubscriptionRois(BaseModel):
    typename: Optional[Literal["RoiEvent"]] = Field(
        alias="__typename", default="RoiEvent", exclude=True
    )
    create: Optional[ROI] = Field(default=None)
    delete: Optional[ID] = Field(default=None)
    update: Optional[ROI] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class WatchRoisSubscription(BaseModel):
    rois: WatchRoisSubscriptionRois

    class Arguments(BaseModel):
        image: ID

    class Meta:
        document = "fragment ROI on ROI {\n  id\n  image {\n    id\n  }\n  vectors\n  kind\n}\n\nsubscription WatchRois($image: ID!) {\n  rois(image: $image) {\n    create {\n      ...ROI\n    }\n    delete\n    update {\n      ...ROI\n    }\n  }\n}"


async def alink_expression(
    expression: ID, graph: ID, rath: Optional[MikroNextRath] = None
) -> LinkedExpression:
    """LinkExpression



    Arguments:
        expression (ID): expression
        graph (ID): graph
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        LinkedExpression"""
    return (
        await aexecute(
            LinkExpressionMutation,
            {"expression": expression, "graph": graph},
            rath=rath,
        )
    ).link_expression


def link_expression(
    expression: ID, graph: ID, rath: Optional[MikroNextRath] = None
) -> LinkedExpression:
    """LinkExpression



    Arguments:
        expression (ID): expression
        graph (ID): graph
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        LinkedExpression"""
    return execute(
        LinkExpressionMutation, {"expression": expression, "graph": graph}, rath=rath
    ).link_expression


async def acreate_camera(
    serial_number: str,
    name: Optional[str] = None,
    pixel_size_x: Optional[Micrometers] = None,
    pixel_size_y: Optional[Micrometers] = None,
    sensor_size_x: Optional[int] = None,
    sensor_size_y: Optional[int] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateCameraMutationCreatecamera:
    """CreateCamera



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        pixel_size_x (Optional[Micrometers], optional): pixelSizeX.
        pixel_size_y (Optional[Micrometers], optional): pixelSizeY.
        sensor_size_x (Optional[int], optional): sensorSizeX.
        sensor_size_y (Optional[int], optional): sensorSizeY.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateCameraMutationCreatecamera"""
    return (
        await aexecute(
            CreateCameraMutation,
            {
                "serialNumber": serial_number,
                "name": name,
                "pixelSizeX": pixel_size_x,
                "pixelSizeY": pixel_size_y,
                "sensorSizeX": sensor_size_x,
                "sensorSizeY": sensor_size_y,
            },
            rath=rath,
        )
    ).create_camera


def create_camera(
    serial_number: str,
    name: Optional[str] = None,
    pixel_size_x: Optional[Micrometers] = None,
    pixel_size_y: Optional[Micrometers] = None,
    sensor_size_x: Optional[int] = None,
    sensor_size_y: Optional[int] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateCameraMutationCreatecamera:
    """CreateCamera



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        pixel_size_x (Optional[Micrometers], optional): pixelSizeX.
        pixel_size_y (Optional[Micrometers], optional): pixelSizeY.
        sensor_size_x (Optional[int], optional): sensorSizeX.
        sensor_size_y (Optional[int], optional): sensorSizeY.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateCameraMutationCreatecamera"""
    return execute(
        CreateCameraMutation,
        {
            "serialNumber": serial_number,
            "name": name,
            "pixelSizeX": pixel_size_x,
            "pixelSizeY": pixel_size_y,
            "sensorSizeX": sensor_size_x,
            "sensorSizeY": sensor_size_y,
        },
        rath=rath,
    ).create_camera


async def aensure_camera(
    serial_number: str,
    name: Optional[str] = None,
    pixel_size_x: Optional[Micrometers] = None,
    pixel_size_y: Optional[Micrometers] = None,
    sensor_size_x: Optional[int] = None,
    sensor_size_y: Optional[int] = None,
    rath: Optional[MikroNextRath] = None,
) -> EnsureCameraMutationEnsurecamera:
    """EnsureCamera



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        pixel_size_x (Optional[Micrometers], optional): pixelSizeX.
        pixel_size_y (Optional[Micrometers], optional): pixelSizeY.
        sensor_size_x (Optional[int], optional): sensorSizeX.
        sensor_size_y (Optional[int], optional): sensorSizeY.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureCameraMutationEnsurecamera"""
    return (
        await aexecute(
            EnsureCameraMutation,
            {
                "serialNumber": serial_number,
                "name": name,
                "pixelSizeX": pixel_size_x,
                "pixelSizeY": pixel_size_y,
                "sensorSizeX": sensor_size_x,
                "sensorSizeY": sensor_size_y,
            },
            rath=rath,
        )
    ).ensure_camera


def ensure_camera(
    serial_number: str,
    name: Optional[str] = None,
    pixel_size_x: Optional[Micrometers] = None,
    pixel_size_y: Optional[Micrometers] = None,
    sensor_size_x: Optional[int] = None,
    sensor_size_y: Optional[int] = None,
    rath: Optional[MikroNextRath] = None,
) -> EnsureCameraMutationEnsurecamera:
    """EnsureCamera



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        pixel_size_x (Optional[Micrometers], optional): pixelSizeX.
        pixel_size_y (Optional[Micrometers], optional): pixelSizeY.
        sensor_size_x (Optional[int], optional): sensorSizeX.
        sensor_size_y (Optional[int], optional): sensorSizeY.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureCameraMutationEnsurecamera"""
    return execute(
        EnsureCameraMutation,
        {
            "serialNumber": serial_number,
            "name": name,
            "pixelSizeX": pixel_size_x,
            "pixelSizeY": pixel_size_y,
            "sensorSizeX": sensor_size_x,
            "sensorSizeY": sensor_size_y,
        },
        rath=rath,
    ).ensure_camera


async def acreate_render_tree(
    name: str, tree: TreeInput, rath: Optional[MikroNextRath] = None
) -> CreateRenderTreeMutationCreaterendertree:
    """CreateRenderTree



    Arguments:
        name (str): name
        tree (TreeInput): tree
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateRenderTreeMutationCreaterendertree"""
    return (
        await aexecute(
            CreateRenderTreeMutation, {"name": name, "tree": tree}, rath=rath
        )
    ).create_render_tree


def create_render_tree(
    name: str, tree: TreeInput, rath: Optional[MikroNextRath] = None
) -> CreateRenderTreeMutationCreaterendertree:
    """CreateRenderTree



    Arguments:
        name (str): name
        tree (TreeInput): tree
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateRenderTreeMutationCreaterendertree"""
    return execute(
        CreateRenderTreeMutation, {"name": name, "tree": tree}, rath=rath
    ).create_render_tree


async def afrom_parquet_like(
    dataframe: ParquetLike,
    name: str,
    origins: Optional[List[ID]] = None,
    dataset: Optional[ID] = None,
    rath: Optional[MikroNextRath] = None,
) -> Table:
    """from_parquet_like



    Arguments:
        dataframe (ParquetLike): dataframe
        name (str): name
        origins (Optional[List[ID]], optional): origins.
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Table"""
    return (
        await aexecute(
            From_parquet_likeMutation,
            {
                "dataframe": dataframe,
                "name": name,
                "origins": origins,
                "dataset": dataset,
            },
            rath=rath,
        )
    ).from_parquet_like


def from_parquet_like(
    dataframe: ParquetLike,
    name: str,
    origins: Optional[List[ID]] = None,
    dataset: Optional[ID] = None,
    rath: Optional[MikroNextRath] = None,
) -> Table:
    """from_parquet_like



    Arguments:
        dataframe (ParquetLike): dataframe
        name (str): name
        origins (Optional[List[ID]], optional): origins.
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Table"""
    return execute(
        From_parquet_likeMutation,
        {"dataframe": dataframe, "name": name, "origins": origins, "dataset": dataset},
        rath=rath,
    ).from_parquet_like


async def arequest_table_upload(
    key: str, datalayer: str, rath: Optional[MikroNextRath] = None
) -> Credentials:
    """RequestTableUpload


     requestTableUpload: Temporary Credentials for a file upload that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        key (str): key
        datalayer (str): datalayer
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Credentials"""
    return (
        await aexecute(
            RequestTableUploadMutation, {"key": key, "datalayer": datalayer}, rath=rath
        )
    ).request_table_upload


def request_table_upload(
    key: str, datalayer: str, rath: Optional[MikroNextRath] = None
) -> Credentials:
    """RequestTableUpload


     requestTableUpload: Temporary Credentials for a file upload that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        key (str): key
        datalayer (str): datalayer
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Credentials"""
    return execute(
        RequestTableUploadMutation, {"key": key, "datalayer": datalayer}, rath=rath
    ).request_table_upload


async def arequest_table_access(
    store: ID, duration: Optional[int] = None, rath: Optional[MikroNextRath] = None
) -> AccessCredentials:
    """RequestTableAccess


     requestTableAccess: Temporary Credentials for a file download that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        store (ID): store
        duration (Optional[int], optional): duration.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        AccessCredentials"""
    return (
        await aexecute(
            RequestTableAccessMutation,
            {"store": store, "duration": duration},
            rath=rath,
        )
    ).request_table_access


def request_table_access(
    store: ID, duration: Optional[int] = None, rath: Optional[MikroNextRath] = None
) -> AccessCredentials:
    """RequestTableAccess


     requestTableAccess: Temporary Credentials for a file download that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        store (ID): store
        duration (Optional[int], optional): duration.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        AccessCredentials"""
    return execute(
        RequestTableAccessMutation, {"store": store, "duration": duration}, rath=rath
    ).request_table_access


async def acreate_rendered_plot(
    plot: Upload,
    name: str,
    overlays: Optional[List[OverlayInput]] = None,
    rath: Optional[MikroNextRath] = None,
) -> RenderedPlot:
    """CreateRenderedPlot



    Arguments:
        plot (Upload): plot
        name (str): name
        overlays (Optional[List[OverlayInput]], optional): overlays.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RenderedPlot"""
    return (
        await aexecute(
            CreateRenderedPlotMutation,
            {"plot": plot, "name": name, "overlays": overlays},
            rath=rath,
        )
    ).create_rendered_plot


def create_rendered_plot(
    plot: Upload,
    name: str,
    overlays: Optional[List[OverlayInput]] = None,
    rath: Optional[MikroNextRath] = None,
) -> RenderedPlot:
    """CreateRenderedPlot



    Arguments:
        plot (Upload): plot
        name (str): name
        overlays (Optional[List[OverlayInput]], optional): overlays.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RenderedPlot"""
    return execute(
        CreateRenderedPlotMutation,
        {"plot": plot, "name": name, "overlays": overlays},
        rath=rath,
    ).create_rendered_plot


async def afrom_file_like(
    file: FileLike,
    name: str,
    origins: Optional[List[ID]] = None,
    dataset: Optional[ID] = None,
    rath: Optional[MikroNextRath] = None,
) -> File:
    """from_file_like



    Arguments:
        file (FileLike): file
        name (str): name
        origins (Optional[List[ID]], optional): origins.
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        File"""
    return (
        await aexecute(
            From_file_likeMutation,
            {"file": file, "name": name, "origins": origins, "dataset": dataset},
            rath=rath,
        )
    ).from_file_like


def from_file_like(
    file: FileLike,
    name: str,
    origins: Optional[List[ID]] = None,
    dataset: Optional[ID] = None,
    rath: Optional[MikroNextRath] = None,
) -> File:
    """from_file_like



    Arguments:
        file (FileLike): file
        name (str): name
        origins (Optional[List[ID]], optional): origins.
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        File"""
    return execute(
        From_file_likeMutation,
        {"file": file, "name": name, "origins": origins, "dataset": dataset},
        rath=rath,
    ).from_file_like


async def arequest_file_upload(
    key: str, datalayer: str, rath: Optional[MikroNextRath] = None
) -> Credentials:
    """RequestFileUpload


     requestFileUpload: Temporary Credentials for a file upload that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        key (str): key
        datalayer (str): datalayer
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Credentials"""
    return (
        await aexecute(
            RequestFileUploadMutation, {"key": key, "datalayer": datalayer}, rath=rath
        )
    ).request_file_upload


def request_file_upload(
    key: str, datalayer: str, rath: Optional[MikroNextRath] = None
) -> Credentials:
    """RequestFileUpload


     requestFileUpload: Temporary Credentials for a file upload that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        key (str): key
        datalayer (str): datalayer
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Credentials"""
    return execute(
        RequestFileUploadMutation, {"key": key, "datalayer": datalayer}, rath=rath
    ).request_file_upload


async def arequest_file_access(
    store: ID, duration: Optional[int] = None, rath: Optional[MikroNextRath] = None
) -> AccessCredentials:
    """RequestFileAccess


     requestFileAccess: Temporary Credentials for a file download that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        store (ID): store
        duration (Optional[int], optional): duration.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        AccessCredentials"""
    return (
        await aexecute(
            RequestFileAccessMutation, {"store": store, "duration": duration}, rath=rath
        )
    ).request_file_access


def request_file_access(
    store: ID, duration: Optional[int] = None, rath: Optional[MikroNextRath] = None
) -> AccessCredentials:
    """RequestFileAccess


     requestFileAccess: Temporary Credentials for a file download that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        store (ID): store
        duration (Optional[int], optional): duration.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        AccessCredentials"""
    return execute(
        RequestFileAccessMutation, {"store": store, "duration": duration}, rath=rath
    ).request_file_access


async def acreate_stage(name: str, rath: Optional[MikroNextRath] = None) -> Stage:
    """CreateStage



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Stage"""
    return (await aexecute(CreateStageMutation, {"name": name}, rath=rath)).create_stage


def create_stage(name: str, rath: Optional[MikroNextRath] = None) -> Stage:
    """CreateStage



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Stage"""
    return execute(CreateStageMutation, {"name": name}, rath=rath).create_stage


async def acreate_roi(
    image: ID,
    vectors: List[FiveDVector],
    kind: RoiKind,
    entity: Optional[ID] = None,
    entity_kind: Optional[ID] = None,
    entity_parent: Optional[ID] = None,
    rath: Optional[MikroNextRath] = None,
) -> ROI:
    """CreateRoi



    Arguments:
        image (ID): image
        vectors (List[FiveDVector]): vectors
        kind (RoiKind): kind
        entity (Optional[ID], optional): entity.
        entity_kind (Optional[ID], optional): entityKind.
        entity_parent (Optional[ID], optional): entityParent.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ROI"""
    return (
        await aexecute(
            CreateRoiMutation,
            {
                "image": image,
                "vectors": vectors,
                "kind": kind,
                "entity": entity,
                "entityKind": entity_kind,
                "entityParent": entity_parent,
            },
            rath=rath,
        )
    ).create_roi


def create_roi(
    image: ID,
    vectors: List[FiveDVector],
    kind: RoiKind,
    entity: Optional[ID] = None,
    entity_kind: Optional[ID] = None,
    entity_parent: Optional[ID] = None,
    rath: Optional[MikroNextRath] = None,
) -> ROI:
    """CreateRoi



    Arguments:
        image (ID): image
        vectors (List[FiveDVector]): vectors
        kind (RoiKind): kind
        entity (Optional[ID], optional): entity.
        entity_kind (Optional[ID], optional): entityKind.
        entity_parent (Optional[ID], optional): entityParent.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ROI"""
    return execute(
        CreateRoiMutation,
        {
            "image": image,
            "vectors": vectors,
            "kind": kind,
            "entity": entity,
            "entityKind": entity_kind,
            "entityParent": entity_parent,
        },
        rath=rath,
    ).create_roi


async def adelete_roi(roi: ID, rath: Optional[MikroNextRath] = None) -> ID:
    """DeleteRoi


     deleteRoi: The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.


    Arguments:
        roi (ID): roi
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ID"""
    return (await aexecute(DeleteRoiMutation, {"roi": roi}, rath=rath)).delete_roi


def delete_roi(roi: ID, rath: Optional[MikroNextRath] = None) -> ID:
    """DeleteRoi


     deleteRoi: The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.


    Arguments:
        roi (ID): roi
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ID"""
    return execute(DeleteRoiMutation, {"roi": roi}, rath=rath).delete_roi


async def aupdate_roi(
    input: UpdateRoiInput, rath: Optional[MikroNextRath] = None
) -> ROI:
    """UpdateRoi



    Arguments:
        input (UpdateRoiInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ROI"""
    return (await aexecute(UpdateRoiMutation, {"input": input}, rath=rath)).update_roi


def update_roi(input: UpdateRoiInput, rath: Optional[MikroNextRath] = None) -> ROI:
    """UpdateRoi



    Arguments:
        input (UpdateRoiInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ROI"""
    return execute(UpdateRoiMutation, {"input": input}, rath=rath).update_roi


async def acreate_graph(name: str, rath: Optional[MikroNextRath] = None) -> Graph:
    """CreateGraph



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Graph"""
    return (await aexecute(CreateGraphMutation, {"name": name}, rath=rath)).create_graph


def create_graph(name: str, rath: Optional[MikroNextRath] = None) -> Graph:
    """CreateGraph



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Graph"""
    return execute(CreateGraphMutation, {"name": name}, rath=rath).create_graph


async def acreate_objective(
    serial_number: str,
    name: Optional[str] = None,
    na: Optional[float] = None,
    magnification: Optional[float] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateObjectiveMutationCreateobjective:
    """CreateObjective



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        na (Optional[float], optional): na.
        magnification (Optional[float], optional): magnification.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateObjectiveMutationCreateobjective"""
    return (
        await aexecute(
            CreateObjectiveMutation,
            {
                "serialNumber": serial_number,
                "name": name,
                "na": na,
                "magnification": magnification,
            },
            rath=rath,
        )
    ).create_objective


def create_objective(
    serial_number: str,
    name: Optional[str] = None,
    na: Optional[float] = None,
    magnification: Optional[float] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateObjectiveMutationCreateobjective:
    """CreateObjective



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        na (Optional[float], optional): na.
        magnification (Optional[float], optional): magnification.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateObjectiveMutationCreateobjective"""
    return execute(
        CreateObjectiveMutation,
        {
            "serialNumber": serial_number,
            "name": name,
            "na": na,
            "magnification": magnification,
        },
        rath=rath,
    ).create_objective


async def aensure_objective(
    serial_number: str,
    name: Optional[str] = None,
    na: Optional[float] = None,
    magnification: Optional[float] = None,
    rath: Optional[MikroNextRath] = None,
) -> EnsureObjectiveMutationEnsureobjective:
    """EnsureObjective



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        na (Optional[float], optional): na.
        magnification (Optional[float], optional): magnification.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureObjectiveMutationEnsureobjective"""
    return (
        await aexecute(
            EnsureObjectiveMutation,
            {
                "serialNumber": serial_number,
                "name": name,
                "na": na,
                "magnification": magnification,
            },
            rath=rath,
        )
    ).ensure_objective


def ensure_objective(
    serial_number: str,
    name: Optional[str] = None,
    na: Optional[float] = None,
    magnification: Optional[float] = None,
    rath: Optional[MikroNextRath] = None,
) -> EnsureObjectiveMutationEnsureobjective:
    """EnsureObjective



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        na (Optional[float], optional): na.
        magnification (Optional[float], optional): magnification.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureObjectiveMutationEnsureobjective"""
    return execute(
        EnsureObjectiveMutation,
        {
            "serialNumber": serial_number,
            "name": name,
            "na": na,
            "magnification": magnification,
        },
        rath=rath,
    ).ensure_objective


async def acreate_protocol_step(
    input: ProtocolStepInput, rath: Optional[MikroNextRath] = None
) -> ProtocolStep:
    """CreateProtocolStep



    Arguments:
        input (ProtocolStepInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ProtocolStep"""
    return (
        await aexecute(CreateProtocolStepMutation, {"input": input}, rath=rath)
    ).create_protocol_step


def create_protocol_step(
    input: ProtocolStepInput, rath: Optional[MikroNextRath] = None
) -> ProtocolStep:
    """CreateProtocolStep



    Arguments:
        input (ProtocolStepInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ProtocolStep"""
    return execute(
        CreateProtocolStepMutation, {"input": input}, rath=rath
    ).create_protocol_step


async def acreate_dataset(
    name: str, rath: Optional[MikroNextRath] = None
) -> CreateDatasetMutationCreatedataset:
    """CreateDataset



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateDatasetMutationCreatedataset"""
    return (
        await aexecute(CreateDatasetMutation, {"name": name}, rath=rath)
    ).create_dataset


def create_dataset(
    name: str, rath: Optional[MikroNextRath] = None
) -> CreateDatasetMutationCreatedataset:
    """CreateDataset



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateDatasetMutationCreatedataset"""
    return execute(CreateDatasetMutation, {"name": name}, rath=rath).create_dataset


async def aupdate_dataset(
    id: ID, name: str, rath: Optional[MikroNextRath] = None
) -> UpdateDatasetMutationUpdatedataset:
    """UpdateDataset



    Arguments:
        id (ID): id
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        UpdateDatasetMutationUpdatedataset"""
    return (
        await aexecute(UpdateDatasetMutation, {"id": id, "name": name}, rath=rath)
    ).update_dataset


def update_dataset(
    id: ID, name: str, rath: Optional[MikroNextRath] = None
) -> UpdateDatasetMutationUpdatedataset:
    """UpdateDataset



    Arguments:
        id (ID): id
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        UpdateDatasetMutationUpdatedataset"""
    return execute(
        UpdateDatasetMutation, {"id": id, "name": name}, rath=rath
    ).update_dataset


async def arevert_dataset(
    dataset: ID, history: ID, rath: Optional[MikroNextRath] = None
) -> RevertDatasetMutationRevertdataset:
    """RevertDataset



    Arguments:
        dataset (ID): dataset
        history (ID): history
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RevertDatasetMutationRevertdataset"""
    return (
        await aexecute(
            RevertDatasetMutation, {"dataset": dataset, "history": history}, rath=rath
        )
    ).revert_dataset


def revert_dataset(
    dataset: ID, history: ID, rath: Optional[MikroNextRath] = None
) -> RevertDatasetMutationRevertdataset:
    """RevertDataset



    Arguments:
        dataset (ID): dataset
        history (ID): history
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RevertDatasetMutationRevertdataset"""
    return execute(
        RevertDatasetMutation, {"dataset": dataset, "history": history}, rath=rath
    ).revert_dataset


async def acreate_instrument(
    serial_number: str,
    name: Optional[str] = None,
    model: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateInstrumentMutationCreateinstrument:
    """CreateInstrument



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        model (Optional[str], optional): model.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateInstrumentMutationCreateinstrument"""
    return (
        await aexecute(
            CreateInstrumentMutation,
            {"serialNumber": serial_number, "name": name, "model": model},
            rath=rath,
        )
    ).create_instrument


def create_instrument(
    serial_number: str,
    name: Optional[str] = None,
    model: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateInstrumentMutationCreateinstrument:
    """CreateInstrument



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        model (Optional[str], optional): model.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateInstrumentMutationCreateinstrument"""
    return execute(
        CreateInstrumentMutation,
        {"serialNumber": serial_number, "name": name, "model": model},
        rath=rath,
    ).create_instrument


async def aensure_instrument(
    serial_number: str,
    name: Optional[str] = None,
    model: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> EnsureInstrumentMutationEnsureinstrument:
    """EnsureInstrument



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        model (Optional[str], optional): model.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureInstrumentMutationEnsureinstrument"""
    return (
        await aexecute(
            EnsureInstrumentMutation,
            {"serialNumber": serial_number, "name": name, "model": model},
            rath=rath,
        )
    ).ensure_instrument


def ensure_instrument(
    serial_number: str,
    name: Optional[str] = None,
    model: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> EnsureInstrumentMutationEnsureinstrument:
    """EnsureInstrument



    Arguments:
        serial_number (str): serialNumber
        name (Optional[str], optional): name.
        model (Optional[str], optional): model.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureInstrumentMutationEnsureinstrument"""
    return execute(
        EnsureInstrumentMutation,
        {"serialNumber": serial_number, "name": name, "model": model},
        rath=rath,
    ).ensure_instrument


async def acreate_expression(
    label: str,
    kind: ExpressionKind,
    ontology: Optional[ID] = None,
    purl: Optional[str] = None,
    description: Optional[str] = None,
    color: Optional[List[int]] = None,
    metric_kind: Optional[MetricDataType] = None,
    rath: Optional[MikroNextRath] = None,
) -> Expression:
    """CreateExpression



    Arguments:
        label (str): label
        kind (ExpressionKind): kind
        ontology (Optional[ID], optional): ontology.
        purl (Optional[str], optional): purl.
        description (Optional[str], optional): description.
        color (Optional[List[int]], optional): color.
        metric_kind (Optional[MetricDataType], optional): metricKind.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Expression"""
    return (
        await aexecute(
            CreateExpressionMutation,
            {
                "label": label,
                "ontology": ontology,
                "purl": purl,
                "description": description,
                "color": color,
                "metricKind": metric_kind,
                "kind": kind,
            },
            rath=rath,
        )
    ).create_expression


def create_expression(
    label: str,
    kind: ExpressionKind,
    ontology: Optional[ID] = None,
    purl: Optional[str] = None,
    description: Optional[str] = None,
    color: Optional[List[int]] = None,
    metric_kind: Optional[MetricDataType] = None,
    rath: Optional[MikroNextRath] = None,
) -> Expression:
    """CreateExpression



    Arguments:
        label (str): label
        kind (ExpressionKind): kind
        ontology (Optional[ID], optional): ontology.
        purl (Optional[str], optional): purl.
        description (Optional[str], optional): description.
        color (Optional[List[int]], optional): color.
        metric_kind (Optional[MetricDataType], optional): metricKind.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Expression"""
    return execute(
        CreateExpressionMutation,
        {
            "label": label,
            "ontology": ontology,
            "purl": purl,
            "description": description,
            "color": color,
            "metricKind": metric_kind,
            "kind": kind,
        },
        rath=rath,
    ).create_expression


async def acreate_entity_relation(
    left: ID, right: ID, kind: ID, rath: Optional[MikroNextRath] = None
) -> EntityRelation:
    """CreateEntityRelation



    Arguments:
        left (ID): left
        right (ID): right
        kind (ID): kind
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return (
        await aexecute(
            CreateEntityRelationMutation,
            {"left": left, "right": right, "kind": kind},
            rath=rath,
        )
    ).create_entity_relation


def create_entity_relation(
    left: ID, right: ID, kind: ID, rath: Optional[MikroNextRath] = None
) -> EntityRelation:
    """CreateEntityRelation



    Arguments:
        left (ID): left
        right (ID): right
        kind (ID): kind
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return execute(
        CreateEntityRelationMutation,
        {"left": left, "right": right, "kind": kind},
        rath=rath,
    ).create_entity_relation


async def acreate_roi_entity_relation(
    input: RoiEntityRelationInput, rath: Optional[MikroNextRath] = None
) -> EntityRelation:
    """CreateRoiEntityRelation



    Arguments:
        input (RoiEntityRelationInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return (
        await aexecute(CreateRoiEntityRelationMutation, {"input": input}, rath=rath)
    ).create_roi_entity_relation


def create_roi_entity_relation(
    input: RoiEntityRelationInput, rath: Optional[MikroNextRath] = None
) -> EntityRelation:
    """CreateRoiEntityRelation



    Arguments:
        input (RoiEntityRelationInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return execute(
        CreateRoiEntityRelationMutation, {"input": input}, rath=rath
    ).create_roi_entity_relation


async def acreate_reagent(
    expression: ID, lot_id: str, rath: Optional[MikroNextRath] = None
) -> Reagent:
    """CreateReagent



    Arguments:
        expression (ID): expression
        lot_id (str): lotId
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Reagent"""
    return (
        await aexecute(
            CreateReagentMutation,
            {"expression": expression, "lotId": lot_id},
            rath=rath,
        )
    ).create_reagent


def create_reagent(
    expression: ID, lot_id: str, rath: Optional[MikroNextRath] = None
) -> Reagent:
    """CreateReagent



    Arguments:
        expression (ID): expression
        lot_id (str): lotId
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Reagent"""
    return execute(
        CreateReagentMutation, {"expression": expression, "lotId": lot_id}, rath=rath
    ).create_reagent


async def acreate_entity_metric(
    entity: ID,
    metric: ID,
    value: Any,
    timepoint: Optional[datetime] = None,
    rath: Optional[MikroNextRath] = None,
) -> Entity:
    """CreateEntityMetric



    Arguments:
        entity (ID): entity
        metric (ID): metric
        value (Any): value
        timepoint (Optional[datetime], optional): timepoint.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Entity"""
    return (
        await aexecute(
            CreateEntityMetricMutation,
            {
                "entity": entity,
                "metric": metric,
                "value": value,
                "timepoint": timepoint,
            },
            rath=rath,
        )
    ).create_entity_metric


def create_entity_metric(
    entity: ID,
    metric: ID,
    value: Any,
    timepoint: Optional[datetime] = None,
    rath: Optional[MikroNextRath] = None,
) -> Entity:
    """CreateEntityMetric



    Arguments:
        entity (ID): entity
        metric (ID): metric
        value (Any): value
        timepoint (Optional[datetime], optional): timepoint.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Entity"""
    return execute(
        CreateEntityMetricMutation,
        {"entity": entity, "metric": metric, "value": value, "timepoint": timepoint},
        rath=rath,
    ).create_entity_metric


async def acreate_relation_metric(
    relation: ID,
    metric: ID,
    value: Any,
    timepoint: Optional[datetime] = None,
    rath: Optional[MikroNextRath] = None,
) -> EntityRelation:
    """CreateRelationMetric



    Arguments:
        relation (ID): relation
        metric (ID): metric
        value (Any): value
        timepoint (Optional[datetime], optional): timepoint.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return (
        await aexecute(
            CreateRelationMetricMutation,
            {
                "relation": relation,
                "metric": metric,
                "value": value,
                "timepoint": timepoint,
            },
            rath=rath,
        )
    ).create_relation_metric


def create_relation_metric(
    relation: ID,
    metric: ID,
    value: Any,
    timepoint: Optional[datetime] = None,
    rath: Optional[MikroNextRath] = None,
) -> EntityRelation:
    """CreateRelationMetric



    Arguments:
        relation (ID): relation
        metric (ID): metric
        value (Any): value
        timepoint (Optional[datetime], optional): timepoint.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return execute(
        CreateRelationMetricMutation,
        {
            "relation": relation,
            "metric": metric,
            "value": value,
            "timepoint": timepoint,
        },
        rath=rath,
    ).create_relation_metric


async def afrom_array_like(
    array: ArrayLike,
    name: str,
    origins: Optional[List[ID]] = None,
    channel_views: Optional[List[PartialChannelViewInput]] = None,
    transformation_views: Optional[List[PartialAffineTransformationViewInput]] = None,
    pixel_views: Optional[List[PartialPixelViewInput]] = None,
    rgb_views: Optional[List[PartialRGBViewInput]] = None,
    acquisition_views: Optional[List[PartialAcquisitionViewInput]] = None,
    timepoint_views: Optional[List[PartialTimepointViewInput]] = None,
    optics_views: Optional[List[PartialOpticsViewInput]] = None,
    specimen_views: Optional[List[PartialSpecimenViewInput]] = None,
    scale_views: Optional[List[PartialScaleViewInput]] = None,
    tags: Optional[List[str]] = None,
    file_origins: Optional[List[ID]] = None,
    roi_origins: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> Image:
    """from_array_like



    Arguments:
        array (ArrayLike): array
        name (str): name
        origins (Optional[List[ID]], optional): origins.
        channel_views (Optional[List[PartialChannelViewInput]], optional): channelViews.
        transformation_views (Optional[List[PartialAffineTransformationViewInput]], optional): transformationViews.
        pixel_views (Optional[List[PartialPixelViewInput]], optional): pixelViews.
        rgb_views (Optional[List[PartialRGBViewInput]], optional): rgbViews.
        acquisition_views (Optional[List[PartialAcquisitionViewInput]], optional): acquisitionViews.
        timepoint_views (Optional[List[PartialTimepointViewInput]], optional): timepointViews.
        optics_views (Optional[List[PartialOpticsViewInput]], optional): opticsViews.
        specimen_views (Optional[List[PartialSpecimenViewInput]], optional): specimenViews.
        scale_views (Optional[List[PartialScaleViewInput]], optional): scaleViews.
        tags (Optional[List[str]], optional): tags.
        file_origins (Optional[List[ID]], optional): fileOrigins.
        roi_origins (Optional[List[ID]], optional): roiOrigins.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Image"""
    return (
        await aexecute(
            From_array_likeMutation,
            {
                "array": array,
                "name": name,
                "origins": origins,
                "channelViews": channel_views,
                "transformationViews": transformation_views,
                "pixelViews": pixel_views,
                "rgbViews": rgb_views,
                "acquisitionViews": acquisition_views,
                "timepointViews": timepoint_views,
                "opticsViews": optics_views,
                "specimenViews": specimen_views,
                "scaleViews": scale_views,
                "tags": tags,
                "fileOrigins": file_origins,
                "roiOrigins": roi_origins,
            },
            rath=rath,
        )
    ).from_array_like


def from_array_like(
    array: ArrayLike,
    name: str,
    origins: Optional[List[ID]] = None,
    channel_views: Optional[List[PartialChannelViewInput]] = None,
    transformation_views: Optional[List[PartialAffineTransformationViewInput]] = None,
    pixel_views: Optional[List[PartialPixelViewInput]] = None,
    rgb_views: Optional[List[PartialRGBViewInput]] = None,
    acquisition_views: Optional[List[PartialAcquisitionViewInput]] = None,
    timepoint_views: Optional[List[PartialTimepointViewInput]] = None,
    optics_views: Optional[List[PartialOpticsViewInput]] = None,
    specimen_views: Optional[List[PartialSpecimenViewInput]] = None,
    scale_views: Optional[List[PartialScaleViewInput]] = None,
    tags: Optional[List[str]] = None,
    file_origins: Optional[List[ID]] = None,
    roi_origins: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> Image:
    """from_array_like



    Arguments:
        array (ArrayLike): array
        name (str): name
        origins (Optional[List[ID]], optional): origins.
        channel_views (Optional[List[PartialChannelViewInput]], optional): channelViews.
        transformation_views (Optional[List[PartialAffineTransformationViewInput]], optional): transformationViews.
        pixel_views (Optional[List[PartialPixelViewInput]], optional): pixelViews.
        rgb_views (Optional[List[PartialRGBViewInput]], optional): rgbViews.
        acquisition_views (Optional[List[PartialAcquisitionViewInput]], optional): acquisitionViews.
        timepoint_views (Optional[List[PartialTimepointViewInput]], optional): timepointViews.
        optics_views (Optional[List[PartialOpticsViewInput]], optional): opticsViews.
        specimen_views (Optional[List[PartialSpecimenViewInput]], optional): specimenViews.
        scale_views (Optional[List[PartialScaleViewInput]], optional): scaleViews.
        tags (Optional[List[str]], optional): tags.
        file_origins (Optional[List[ID]], optional): fileOrigins.
        roi_origins (Optional[List[ID]], optional): roiOrigins.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Image"""
    return execute(
        From_array_likeMutation,
        {
            "array": array,
            "name": name,
            "origins": origins,
            "channelViews": channel_views,
            "transformationViews": transformation_views,
            "pixelViews": pixel_views,
            "rgbViews": rgb_views,
            "acquisitionViews": acquisition_views,
            "timepointViews": timepoint_views,
            "opticsViews": optics_views,
            "specimenViews": specimen_views,
            "scaleViews": scale_views,
            "tags": tags,
            "fileOrigins": file_origins,
            "roiOrigins": roi_origins,
        },
        rath=rath,
    ).from_array_like


async def arequest_upload(
    key: str, datalayer: str, rath: Optional[MikroNextRath] = None
) -> Credentials:
    """RequestUpload


     requestUpload: Temporary Credentials for a file upload that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        key (str): key
        datalayer (str): datalayer
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Credentials"""
    return (
        await aexecute(
            RequestUploadMutation, {"key": key, "datalayer": datalayer}, rath=rath
        )
    ).request_upload


def request_upload(
    key: str, datalayer: str, rath: Optional[MikroNextRath] = None
) -> Credentials:
    """RequestUpload


     requestUpload: Temporary Credentials for a file upload that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        key (str): key
        datalayer (str): datalayer
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Credentials"""
    return execute(
        RequestUploadMutation, {"key": key, "datalayer": datalayer}, rath=rath
    ).request_upload


async def arequest_access(
    store: ID, duration: Optional[int] = None, rath: Optional[MikroNextRath] = None
) -> AccessCredentials:
    """RequestAccess


     requestAccess: Temporary Credentials for a file download that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        store (ID): store
        duration (Optional[int], optional): duration.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        AccessCredentials"""
    return (
        await aexecute(
            RequestAccessMutation, {"store": store, "duration": duration}, rath=rath
        )
    ).request_access


def request_access(
    store: ID, duration: Optional[int] = None, rath: Optional[MikroNextRath] = None
) -> AccessCredentials:
    """RequestAccess


     requestAccess: Temporary Credentials for a file download that can be used by a Client (e.g. in a python datalayer)


    Arguments:
        store (ID): store
        duration (Optional[int], optional): duration.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        AccessCredentials"""
    return execute(
        RequestAccessMutation, {"store": store, "duration": duration}, rath=rath
    ).request_access


async def acreate_entity(
    kind: ID,
    group: Optional[ID] = None,
    name: Optional[str] = None,
    parent: Optional[ID] = None,
    instance_kind: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> Entity:
    """CreateEntity



    Arguments:
        kind (ID): kind
        group (Optional[ID], optional): group.
        name (Optional[str], optional): name.
        parent (Optional[ID], optional): parent.
        instance_kind (Optional[str], optional): instance_kind.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Entity"""
    return (
        await aexecute(
            CreateEntityMutation,
            {
                "kind": kind,
                "group": group,
                "name": name,
                "parent": parent,
                "instance_kind": instance_kind,
            },
            rath=rath,
        )
    ).create_entity


def create_entity(
    kind: ID,
    group: Optional[ID] = None,
    name: Optional[str] = None,
    parent: Optional[ID] = None,
    instance_kind: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> Entity:
    """CreateEntity



    Arguments:
        kind (ID): kind
        group (Optional[ID], optional): group.
        name (Optional[str], optional): name.
        parent (Optional[ID], optional): parent.
        instance_kind (Optional[str], optional): instance_kind.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Entity"""
    return execute(
        CreateEntityMutation,
        {
            "kind": kind,
            "group": group,
            "name": name,
            "parent": parent,
            "instance_kind": instance_kind,
        },
        rath=rath,
    ).create_entity


async def acreate_era(
    name: str, begin: Optional[datetime] = None, rath: Optional[MikroNextRath] = None
) -> CreateEraMutationCreateera:
    """CreateEra



    Arguments:
        name (str): name
        begin (Optional[datetime], optional): begin.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateEraMutationCreateera"""
    return (
        await aexecute(CreateEraMutation, {"name": name, "begin": begin}, rath=rath)
    ).create_era


def create_era(
    name: str, begin: Optional[datetime] = None, rath: Optional[MikroNextRath] = None
) -> CreateEraMutationCreateera:
    """CreateEra



    Arguments:
        name (str): name
        begin (Optional[datetime], optional): begin.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateEraMutationCreateera"""
    return execute(
        CreateEraMutation, {"name": name, "begin": begin}, rath=rath
    ).create_era


async def acreate_protocol(
    name: str,
    experiment: ID,
    description: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> Protocol:
    """CreateProtocol



    Arguments:
        name (str): name
        experiment (ID): experiment
        description (Optional[str], optional): description.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Protocol"""
    return (
        await aexecute(
            CreateProtocolMutation,
            {"name": name, "experiment": experiment, "description": description},
            rath=rath,
        )
    ).create_protocol


def create_protocol(
    name: str,
    experiment: ID,
    description: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> Protocol:
    """CreateProtocol



    Arguments:
        name (str): name
        experiment (ID): experiment
        description (Optional[str], optional): description.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Protocol"""
    return execute(
        CreateProtocolMutation,
        {"name": name, "experiment": experiment, "description": description},
        rath=rath,
    ).create_protocol


async def acreate_snapshot(
    image: ID, file: Upload, rath: Optional[MikroNextRath] = None
) -> Snapshot:
    """CreateSnapshot



    Arguments:
        image (ID): image
        file (Upload): file
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Snapshot"""
    return (
        await aexecute(
            CreateSnapshotMutation, {"image": image, "file": file}, rath=rath
        )
    ).create_snapshot


def create_snapshot(
    image: ID, file: Upload, rath: Optional[MikroNextRath] = None
) -> Snapshot:
    """CreateSnapshot



    Arguments:
        image (ID): image
        file (Upload): file
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Snapshot"""
    return execute(
        CreateSnapshotMutation, {"image": image, "file": file}, rath=rath
    ).create_snapshot


async def acreate_rgb_view(
    image: ID,
    context: ID,
    gamma: Optional[float] = None,
    contrast_limit_max: Optional[float] = None,
    contrast_limit_min: Optional[float] = None,
    rescale: Optional[bool] = None,
    active: Optional[bool] = None,
    color_map: Optional[ColorMap] = None,
    base_color: Optional[List[float]] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateRgbViewMutationCreatergbview:
    """CreateRgbView



    Arguments:
        image (ID): image
        context (ID): context
        gamma (Optional[float], optional): gamma.
        contrast_limit_max (Optional[float], optional): contrastLimitMax.
        contrast_limit_min (Optional[float], optional): contrastLimitMin.
        rescale (Optional[bool], optional): rescale.
        active (Optional[bool], optional): active.
        color_map (Optional[ColorMap], optional): colorMap.
        base_color (Optional[List[float]], optional): baseColor.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateRgbViewMutationCreatergbview"""
    return (
        await aexecute(
            CreateRgbViewMutation,
            {
                "image": image,
                "context": context,
                "gamma": gamma,
                "contrastLimitMax": contrast_limit_max,
                "contrastLimitMin": contrast_limit_min,
                "rescale": rescale,
                "active": active,
                "colorMap": color_map,
                "baseColor": base_color,
            },
            rath=rath,
        )
    ).create_rgb_view


def create_rgb_view(
    image: ID,
    context: ID,
    gamma: Optional[float] = None,
    contrast_limit_max: Optional[float] = None,
    contrast_limit_min: Optional[float] = None,
    rescale: Optional[bool] = None,
    active: Optional[bool] = None,
    color_map: Optional[ColorMap] = None,
    base_color: Optional[List[float]] = None,
    rath: Optional[MikroNextRath] = None,
) -> CreateRgbViewMutationCreatergbview:
    """CreateRgbView



    Arguments:
        image (ID): image
        context (ID): context
        gamma (Optional[float], optional): gamma.
        contrast_limit_max (Optional[float], optional): contrastLimitMax.
        contrast_limit_min (Optional[float], optional): contrastLimitMin.
        rescale (Optional[bool], optional): rescale.
        active (Optional[bool], optional): active.
        color_map (Optional[ColorMap], optional): colorMap.
        base_color (Optional[List[float]], optional): baseColor.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateRgbViewMutationCreatergbview"""
    return execute(
        CreateRgbViewMutation,
        {
            "image": image,
            "context": context,
            "gamma": gamma,
            "contrastLimitMax": contrast_limit_max,
            "contrastLimitMin": contrast_limit_min,
            "rescale": rescale,
            "active": active,
            "colorMap": color_map,
            "baseColor": base_color,
        },
        rath=rath,
    ).create_rgb_view


async def acreate_label_view(
    image: ID, label: str, rath: Optional[MikroNextRath] = None
) -> LabelView:
    """CreateLabelView



    Arguments:
        image (ID): image
        label (str): label
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        LabelView"""
    return (
        await aexecute(
            CreateLabelViewMutation, {"image": image, "label": label}, rath=rath
        )
    ).create_label_view


def create_label_view(
    image: ID, label: str, rath: Optional[MikroNextRath] = None
) -> LabelView:
    """CreateLabelView



    Arguments:
        image (ID): image
        label (str): label
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        LabelView"""
    return execute(
        CreateLabelViewMutation, {"image": image, "label": label}, rath=rath
    ).create_label_view


async def acreate_protocol_step_view(
    input: ProtocolStepViewInput, rath: Optional[MikroNextRath] = None
) -> ProtocolStepView:
    """CreateProtocolStepView



    Arguments:
        input (ProtocolStepViewInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ProtocolStepView"""
    return (
        await aexecute(CreateProtocolStepViewMutation, {"input": input}, rath=rath)
    ).create_protocol_step_view


def create_protocol_step_view(
    input: ProtocolStepViewInput, rath: Optional[MikroNextRath] = None
) -> ProtocolStepView:
    """CreateProtocolStepView



    Arguments:
        input (ProtocolStepViewInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ProtocolStepView"""
    return execute(
        CreateProtocolStepViewMutation, {"input": input}, rath=rath
    ).create_protocol_step_view


async def acreate_ontology(
    name: str,
    purl: Optional[str] = None,
    description: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> Ontology:
    """CreateOntology



    Arguments:
        name (str): name
        purl (Optional[str], optional): purl.
        description (Optional[str], optional): description.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Ontology"""
    return (
        await aexecute(
            CreateOntologyMutation,
            {"name": name, "purl": purl, "description": description},
            rath=rath,
        )
    ).create_ontology


def create_ontology(
    name: str,
    purl: Optional[str] = None,
    description: Optional[str] = None,
    rath: Optional[MikroNextRath] = None,
) -> Ontology:
    """CreateOntology



    Arguments:
        name (str): name
        purl (Optional[str], optional): purl.
        description (Optional[str], optional): description.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Ontology"""
    return execute(
        CreateOntologyMutation,
        {"name": name, "purl": purl, "description": description},
        rath=rath,
    ).create_ontology


async def acreate_rgb_context(
    input: CreateRGBContextInput, rath: Optional[MikroNextRath] = None
) -> RGBContext:
    """CreateRGBContext



    Arguments:
        input (CreateRGBContextInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RGBContext"""
    return (
        await aexecute(CreateRGBContextMutation, {"input": input}, rath=rath)
    ).create_rgb_context


def create_rgb_context(
    input: CreateRGBContextInput, rath: Optional[MikroNextRath] = None
) -> RGBContext:
    """CreateRGBContext



    Arguments:
        input (CreateRGBContextInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RGBContext"""
    return execute(
        CreateRGBContextMutation, {"input": input}, rath=rath
    ).create_rgb_context


async def aupdate_rgb_context(
    input: UpdateRGBContextInput, rath: Optional[MikroNextRath] = None
) -> RGBContext:
    """UpdateRGBContext



    Arguments:
        input (UpdateRGBContextInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RGBContext"""
    return (
        await aexecute(UpdateRGBContextMutation, {"input": input}, rath=rath)
    ).update_rgb_context


def update_rgb_context(
    input: UpdateRGBContextInput, rath: Optional[MikroNextRath] = None
) -> RGBContext:
    """UpdateRGBContext



    Arguments:
        input (UpdateRGBContextInput): input
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RGBContext"""
    return execute(
        UpdateRGBContextMutation, {"input": input}, rath=rath
    ).update_rgb_context


async def acreate_view_collection(
    name: str, rath: Optional[MikroNextRath] = None
) -> CreateViewCollectionMutationCreateviewcollection:
    """CreateViewCollection



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateViewCollectionMutationCreateviewcollection"""
    return (
        await aexecute(CreateViewCollectionMutation, {"name": name}, rath=rath)
    ).create_view_collection


def create_view_collection(
    name: str, rath: Optional[MikroNextRath] = None
) -> CreateViewCollectionMutationCreateviewcollection:
    """CreateViewCollection



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateViewCollectionMutationCreateviewcollection"""
    return execute(
        CreateViewCollectionMutation, {"name": name}, rath=rath
    ).create_view_collection


async def acreate_channel(
    name: str, rath: Optional[MikroNextRath] = None
) -> CreateChannelMutationCreatechannel:
    """CreateChannel



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateChannelMutationCreatechannel"""
    return (
        await aexecute(CreateChannelMutation, {"name": name}, rath=rath)
    ).create_channel


def create_channel(
    name: str, rath: Optional[MikroNextRath] = None
) -> CreateChannelMutationCreatechannel:
    """CreateChannel



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        CreateChannelMutationCreatechannel"""
    return execute(CreateChannelMutation, {"name": name}, rath=rath).create_channel


async def aensure_channel(
    name: str, rath: Optional[MikroNextRath] = None
) -> EnsureChannelMutationEnsurechannel:
    """EnsureChannel



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureChannelMutationEnsurechannel"""
    return (
        await aexecute(EnsureChannelMutation, {"name": name}, rath=rath)
    ).ensure_channel


def ensure_channel(
    name: str, rath: Optional[MikroNextRath] = None
) -> EnsureChannelMutationEnsurechannel:
    """EnsureChannel



    Arguments:
        name (str): name
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EnsureChannelMutationEnsurechannel"""
    return execute(EnsureChannelMutation, {"name": name}, rath=rath).ensure_channel


async def acreate_experiment(
    name: str, description: Optional[str] = None, rath: Optional[MikroNextRath] = None
) -> Experiment:
    """CreateExperiment



    Arguments:
        name (str): name
        description (Optional[str], optional): description.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Experiment"""
    return (
        await aexecute(
            CreateExperimentMutation,
            {"name": name, "description": description},
            rath=rath,
        )
    ).create_experiment


def create_experiment(
    name: str, description: Optional[str] = None, rath: Optional[MikroNextRath] = None
) -> Experiment:
    """CreateExperiment



    Arguments:
        name (str): name
        description (Optional[str], optional): description.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Experiment"""
    return execute(
        CreateExperimentMutation, {"name": name, "description": description}, rath=rath
    ).create_experiment


async def aget_linked_expression(
    id: ID, rath: Optional[MikroNextRath] = None
) -> LinkedExpression:
    """GetLinkedExpression



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        LinkedExpression"""
    return (
        await aexecute(GetLinkedExpressionQuery, {"id": id}, rath=rath)
    ).linked_expression


def get_linked_expression(
    id: ID, rath: Optional[MikroNextRath] = None
) -> LinkedExpression:
    """GetLinkedExpression



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        LinkedExpression"""
    return execute(GetLinkedExpressionQuery, {"id": id}, rath=rath).linked_expression


async def asearch_linked_expressions(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchLinkedExpressionsQueryOptions]:
    """SearchLinkedExpressions



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchLinkedExpressionsQueryLinkedexpressions]"""
    return (
        await aexecute(
            SearchLinkedExpressionsQuery,
            {"search": search, "values": values},
            rath=rath,
        )
    ).options


def search_linked_expressions(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchLinkedExpressionsQueryOptions]:
    """SearchLinkedExpressions



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchLinkedExpressionsQueryLinkedexpressions]"""
    return execute(
        SearchLinkedExpressionsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def alist_linked_expressions(
    filters: Optional[LinkedExpressionFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[ListLinkedExpression]:
    """ListLinkedExpressions



    Arguments:
        filters (Optional[LinkedExpressionFilter], optional): filters.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[ListLinkedExpression]"""
    return (
        await aexecute(
            ListLinkedExpressionsQuery,
            {"filters": filters, "pagination": pagination},
            rath=rath,
        )
    ).linked_expressions


def list_linked_expressions(
    filters: Optional[LinkedExpressionFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[ListLinkedExpression]:
    """ListLinkedExpressions



    Arguments:
        filters (Optional[LinkedExpressionFilter], optional): filters.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[ListLinkedExpression]"""
    return execute(
        ListLinkedExpressionsQuery,
        {"filters": filters, "pagination": pagination},
        rath=rath,
    ).linked_expressions


async def aget_camera(id: ID, rath: Optional[MikroNextRath] = None) -> Camera:
    """GetCamera



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Camera"""
    return (await aexecute(GetCameraQuery, {"id": id}, rath=rath)).camera


def get_camera(id: ID, rath: Optional[MikroNextRath] = None) -> Camera:
    """GetCamera



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Camera"""
    return execute(GetCameraQuery, {"id": id}, rath=rath).camera


async def aget_table(id: ID, rath: Optional[MikroNextRath] = None) -> Table:
    """GetTable



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Table"""
    return (await aexecute(GetTableQuery, {"id": id}, rath=rath)).table


def get_table(id: ID, rath: Optional[MikroNextRath] = None) -> Table:
    """GetTable



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Table"""
    return execute(GetTableQuery, {"id": id}, rath=rath).table


async def aget_rendered_plot(
    id: ID, rath: Optional[MikroNextRath] = None
) -> RenderedPlot:
    """GetRenderedPlot



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RenderedPlot"""
    return (await aexecute(GetRenderedPlotQuery, {"id": id}, rath=rath)).rendered_plot


def get_rendered_plot(id: ID, rath: Optional[MikroNextRath] = None) -> RenderedPlot:
    """GetRenderedPlot



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RenderedPlot"""
    return execute(GetRenderedPlotQuery, {"id": id}, rath=rath).rendered_plot


async def alist_rendered_plots(
    rath: Optional[MikroNextRath] = None,
) -> List[ListRenderedPlot]:
    """ListRenderedPlots



    Arguments:
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[ListRenderedPlot]"""
    return (await aexecute(ListRenderedPlotsQuery, {}, rath=rath)).rendered_plots


def list_rendered_plots(rath: Optional[MikroNextRath] = None) -> List[ListRenderedPlot]:
    """ListRenderedPlots



    Arguments:
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[ListRenderedPlot]"""
    return execute(ListRenderedPlotsQuery, {}, rath=rath).rendered_plots


async def asearch_rendered_plots(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchRenderedPlotsQueryOptions]:
    """SearchRenderedPlots



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchRenderedPlotsQueryRenderedplots]"""
    return (
        await aexecute(
            SearchRenderedPlotsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_rendered_plots(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchRenderedPlotsQueryOptions]:
    """SearchRenderedPlots



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchRenderedPlotsQueryRenderedplots]"""
    return execute(
        SearchRenderedPlotsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_file(id: ID, rath: Optional[MikroNextRath] = None) -> File:
    """GetFile



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        File"""
    return (await aexecute(GetFileQuery, {"id": id}, rath=rath)).file


def get_file(id: ID, rath: Optional[MikroNextRath] = None) -> File:
    """GetFile



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        File"""
    return execute(GetFileQuery, {"id": id}, rath=rath).file


async def asearch_files(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchFilesQueryOptions]:
    """SearchFiles



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchFilesQueryFiles]"""
    return (
        await aexecute(
            SearchFilesQuery,
            {"search": search, "values": values, "pagination": pagination},
            rath=rath,
        )
    ).options


def search_files(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchFilesQueryOptions]:
    """SearchFiles



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchFilesQueryFiles]"""
    return execute(
        SearchFilesQuery,
        {"search": search, "values": values, "pagination": pagination},
        rath=rath,
    ).options


async def aget_stage(id: ID, rath: Optional[MikroNextRath] = None) -> Stage:
    """GetStage



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Stage"""
    return (await aexecute(GetStageQuery, {"id": id}, rath=rath)).stage


def get_stage(id: ID, rath: Optional[MikroNextRath] = None) -> Stage:
    """GetStage



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Stage"""
    return execute(GetStageQuery, {"id": id}, rath=rath).stage


async def asearch_stages(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchStagesQueryOptions]:
    """SearchStages



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchStagesQueryStages]"""
    return (
        await aexecute(
            SearchStagesQuery,
            {"search": search, "values": values, "pagination": pagination},
            rath=rath,
        )
    ).options


def search_stages(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchStagesQueryOptions]:
    """SearchStages



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchStagesQueryStages]"""
    return execute(
        SearchStagesQuery,
        {"search": search, "values": values, "pagination": pagination},
        rath=rath,
    ).options


async def aget_rois(image: ID, rath: Optional[MikroNextRath] = None) -> List[ROI]:
    """GetRois



    Arguments:
        image (ID): image
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[ROI]"""
    return (await aexecute(GetRoisQuery, {"image": image}, rath=rath)).rois


def get_rois(image: ID, rath: Optional[MikroNextRath] = None) -> List[ROI]:
    """GetRois



    Arguments:
        image (ID): image
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[ROI]"""
    return execute(GetRoisQuery, {"image": image}, rath=rath).rois


async def aget_roi(id: ID, rath: Optional[MikroNextRath] = None) -> ROI:
    """GetRoi



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ROI"""
    return (await aexecute(GetRoiQuery, {"id": id}, rath=rath)).roi


def get_roi(id: ID, rath: Optional[MikroNextRath] = None) -> ROI:
    """GetRoi



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ROI"""
    return execute(GetRoiQuery, {"id": id}, rath=rath).roi


async def asearch_rois(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchRoisQueryOptions]:
    """SearchRois



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchRoisQueryRois]"""
    return (
        await aexecute(SearchRoisQuery, {"search": search, "values": values}, rath=rath)
    ).options


def search_rois(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchRoisQueryOptions]:
    """SearchRois



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchRoisQueryRois]"""
    return execute(
        SearchRoisQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_objective(id: ID, rath: Optional[MikroNextRath] = None) -> Objective:
    """GetObjective



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Objective"""
    return (await aexecute(GetObjectiveQuery, {"id": id}, rath=rath)).objective


def get_objective(id: ID, rath: Optional[MikroNextRath] = None) -> Objective:
    """GetObjective



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Objective"""
    return execute(GetObjectiveQuery, {"id": id}, rath=rath).objective


async def aget_protocol_step(
    id: ID, rath: Optional[MikroNextRath] = None
) -> ProtocolStep:
    """GetProtocolStep



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ProtocolStep"""
    return (await aexecute(GetProtocolStepQuery, {"id": id}, rath=rath)).protocol_step


def get_protocol_step(id: ID, rath: Optional[MikroNextRath] = None) -> ProtocolStep:
    """GetProtocolStep



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        ProtocolStep"""
    return execute(GetProtocolStepQuery, {"id": id}, rath=rath).protocol_step


async def asearch_protocol_steps(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchProtocolStepsQueryOptions]:
    """SearchProtocolSteps



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchProtocolStepsQueryProtocolsteps]"""
    return (
        await aexecute(
            SearchProtocolStepsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_protocol_steps(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchProtocolStepsQueryOptions]:
    """SearchProtocolSteps



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchProtocolStepsQueryProtocolsteps]"""
    return execute(
        SearchProtocolStepsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_dataset(id: ID, rath: Optional[MikroNextRath] = None) -> Dataset:
    """GetDataset



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Dataset"""
    return (await aexecute(GetDatasetQuery, {"id": id}, rath=rath)).dataset


def get_dataset(id: ID, rath: Optional[MikroNextRath] = None) -> Dataset:
    """GetDataset



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Dataset"""
    return execute(GetDatasetQuery, {"id": id}, rath=rath).dataset


async def aget_instrument(id: ID, rath: Optional[MikroNextRath] = None) -> Instrument:
    """GetInstrument



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Instrument"""
    return (await aexecute(GetInstrumentQuery, {"id": id}, rath=rath)).instrument


def get_instrument(id: ID, rath: Optional[MikroNextRath] = None) -> Instrument:
    """GetInstrument



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Instrument"""
    return execute(GetInstrumentQuery, {"id": id}, rath=rath).instrument


async def aget_entity_relation(
    id: ID, rath: Optional[MikroNextRath] = None
) -> EntityRelation:
    """GetEntityRelation



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return (
        await aexecute(GetEntityRelationQuery, {"id": id}, rath=rath)
    ).entity_relation


def get_entity_relation(id: ID, rath: Optional[MikroNextRath] = None) -> EntityRelation:
    """GetEntityRelation



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        EntityRelation"""
    return execute(GetEntityRelationQuery, {"id": id}, rath=rath).entity_relation


async def asearch_entity_relations(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchEntityRelationsQueryOptions]:
    """SearchEntityRelations



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchEntityRelationsQueryEntityrelations]"""
    return (
        await aexecute(
            SearchEntityRelationsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_entity_relations(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchEntityRelationsQueryOptions]:
    """SearchEntityRelations



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchEntityRelationsQueryEntityrelations]"""
    return execute(
        SearchEntityRelationsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_reagent(id: ID, rath: Optional[MikroNextRath] = None) -> Reagent:
    """GetReagent



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Reagent"""
    return (await aexecute(GetReagentQuery, {"id": id}, rath=rath)).reagent


def get_reagent(id: ID, rath: Optional[MikroNextRath] = None) -> Reagent:
    """GetReagent



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Reagent"""
    return execute(GetReagentQuery, {"id": id}, rath=rath).reagent


async def asearch_reagents(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchReagentsQueryOptions]:
    """SearchReagents



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchReagentsQueryReagents]"""
    return (
        await aexecute(
            SearchReagentsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_reagents(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchReagentsQueryOptions]:
    """SearchReagents



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchReagentsQueryReagents]"""
    return execute(
        SearchReagentsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_image(id: ID, rath: Optional[MikroNextRath] = None) -> Image:
    """GetImage



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Image"""
    return (await aexecute(GetImageQuery, {"id": id}, rath=rath)).image


def get_image(id: ID, rath: Optional[MikroNextRath] = None) -> Image:
    """GetImage



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Image"""
    return execute(GetImageQuery, {"id": id}, rath=rath).image


async def aget_random_image(rath: Optional[MikroNextRath] = None) -> Image:
    """GetRandomImage



    Arguments:
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Image"""
    return (await aexecute(GetRandomImageQuery, {}, rath=rath)).random_image


def get_random_image(rath: Optional[MikroNextRath] = None) -> Image:
    """GetRandomImage



    Arguments:
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Image"""
    return execute(GetRandomImageQuery, {}, rath=rath).random_image


async def asearch_images(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchImagesQueryOptions]:
    """SearchImages



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchImagesQueryImages]"""
    return (
        await aexecute(
            SearchImagesQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_images(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchImagesQueryOptions]:
    """SearchImages



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchImagesQueryImages]"""
    return execute(
        SearchImagesQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aimages(
    filter: Optional[ImageFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[Image]:
    """Images



    Arguments:
        filter (Optional[ImageFilter], optional): filter.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[Image]"""
    return (
        await aexecute(
            ImagesQuery, {"filter": filter, "pagination": pagination}, rath=rath
        )
    ).images


def images(
    filter: Optional[ImageFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[Image]:
    """Images



    Arguments:
        filter (Optional[ImageFilter], optional): filter.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[Image]"""
    return execute(
        ImagesQuery, {"filter": filter, "pagination": pagination}, rath=rath
    ).images


async def aget_entity(id: ID, rath: Optional[MikroNextRath] = None) -> Entity:
    """GetEntity



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Entity"""
    return (await aexecute(GetEntityQuery, {"id": id}, rath=rath)).entity


def get_entity(id: ID, rath: Optional[MikroNextRath] = None) -> Entity:
    """GetEntity



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Entity"""
    return execute(GetEntityQuery, {"id": id}, rath=rath).entity


async def asearch_entities(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchEntitiesQueryOptions]:
    """SearchEntities



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchEntitiesQueryEntities]"""
    return (
        await aexecute(
            SearchEntitiesQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_entities(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchEntitiesQueryOptions]:
    """SearchEntities



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchEntitiesQueryEntities]"""
    return execute(
        SearchEntitiesQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aentities(
    filters: Optional[EntityFilter] = None,
    pagination: Optional[GraphPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[Entity]:
    """Entities



    Arguments:
        filters (Optional[EntityFilter], optional): filters.
        pagination (Optional[GraphPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[Entity]"""
    return (
        await aexecute(
            EntitiesQuery, {"filters": filters, "pagination": pagination}, rath=rath
        )
    ).entities


def entities(
    filters: Optional[EntityFilter] = None,
    pagination: Optional[GraphPaginationInput] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[Entity]:
    """Entities



    Arguments:
        filters (Optional[EntityFilter], optional): filters.
        pagination (Optional[GraphPaginationInput], optional): pagination.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[Entity]"""
    return execute(
        EntitiesQuery, {"filters": filters, "pagination": pagination}, rath=rath
    ).entities


async def aget_protocol(id: ID, rath: Optional[MikroNextRath] = None) -> Protocol:
    """GetProtocol



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Protocol"""
    return (await aexecute(GetProtocolQuery, {"id": id}, rath=rath)).protocol


def get_protocol(id: ID, rath: Optional[MikroNextRath] = None) -> Protocol:
    """GetProtocol



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Protocol"""
    return execute(GetProtocolQuery, {"id": id}, rath=rath).protocol


async def asearch_protocols(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchProtocolsQueryOptions]:
    """SearchProtocols



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchProtocolsQueryProtocols]"""
    return (
        await aexecute(
            SearchProtocolsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_protocols(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchProtocolsQueryOptions]:
    """SearchProtocols



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchProtocolsQueryProtocols]"""
    return execute(
        SearchProtocolsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_snapshot(id: ID, rath: Optional[MikroNextRath] = None) -> Snapshot:
    """GetSnapshot



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Snapshot"""
    return (await aexecute(GetSnapshotQuery, {"id": id}, rath=rath)).snapshot


def get_snapshot(id: ID, rath: Optional[MikroNextRath] = None) -> Snapshot:
    """GetSnapshot



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Snapshot"""
    return execute(GetSnapshotQuery, {"id": id}, rath=rath).snapshot


async def asearch_snapshots(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchSnapshotsQueryOptions]:
    """SearchSnapshots



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchSnapshotsQuerySnapshots]"""
    return (
        await aexecute(
            SearchSnapshotsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_snapshots(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchSnapshotsQueryOptions]:
    """SearchSnapshots



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchSnapshotsQuerySnapshots]"""
    return execute(
        SearchSnapshotsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_ontology(id: ID, rath: Optional[MikroNextRath] = None) -> Ontology:
    """GetOntology



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Ontology"""
    return (await aexecute(GetOntologyQuery, {"id": id}, rath=rath)).ontology


def get_ontology(id: ID, rath: Optional[MikroNextRath] = None) -> Ontology:
    """GetOntology



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        Ontology"""
    return execute(GetOntologyQuery, {"id": id}, rath=rath).ontology


async def asearch_ontologies(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchOntologiesQueryOptions]:
    """SearchOntologies



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchOntologiesQueryOntologies]"""
    return (
        await aexecute(
            SearchOntologiesQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_ontologies(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[MikroNextRath] = None,
) -> List[SearchOntologiesQueryOptions]:
    """SearchOntologies



    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        List[SearchOntologiesQueryOntologies]"""
    return execute(
        SearchOntologiesQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_rgb_context(id: ID, rath: Optional[MikroNextRath] = None) -> RGBContext:
    """GetRGBContext



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RGBContext"""
    return (await aexecute(GetRGBContextQuery, {"id": id}, rath=rath)).rgbcontext


def get_rgb_context(id: ID, rath: Optional[MikroNextRath] = None) -> RGBContext:
    """GetRGBContext



    Arguments:
        id (ID): id
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        RGBContext"""
    return execute(GetRGBContextQuery, {"id": id}, rath=rath).rgbcontext


async def awatch_files(
    dataset: Optional[ID] = None, rath: Optional[MikroNextRath] = None
) -> AsyncIterator[WatchFilesSubscriptionFiles]:
    """WatchFiles



    Arguments:
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        WatchFilesSubscriptionFiles"""
    async for event in asubscribe(
        WatchFilesSubscription, {"dataset": dataset}, rath=rath
    ):
        yield event.files


def watch_files(
    dataset: Optional[ID] = None, rath: Optional[MikroNextRath] = None
) -> Iterator[WatchFilesSubscriptionFiles]:
    """WatchFiles



    Arguments:
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        WatchFilesSubscriptionFiles"""
    for event in subscribe(WatchFilesSubscription, {"dataset": dataset}, rath=rath):
        yield event.files


async def awatch_images(
    dataset: Optional[ID] = None, rath: Optional[MikroNextRath] = None
) -> AsyncIterator[WatchImagesSubscriptionImages]:
    """WatchImages



    Arguments:
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        WatchImagesSubscriptionImages"""
    async for event in asubscribe(
        WatchImagesSubscription, {"dataset": dataset}, rath=rath
    ):
        yield event.images


def watch_images(
    dataset: Optional[ID] = None, rath: Optional[MikroNextRath] = None
) -> Iterator[WatchImagesSubscriptionImages]:
    """WatchImages



    Arguments:
        dataset (Optional[ID], optional): dataset.
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        WatchImagesSubscriptionImages"""
    for event in subscribe(WatchImagesSubscription, {"dataset": dataset}, rath=rath):
        yield event.images


async def awatch_rois(
    image: ID, rath: Optional[MikroNextRath] = None
) -> AsyncIterator[WatchRoisSubscriptionRois]:
    """WatchRois



    Arguments:
        image (ID): image
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        WatchRoisSubscriptionRois"""
    async for event in asubscribe(WatchRoisSubscription, {"image": image}, rath=rath):
        yield event.rois


def watch_rois(
    image: ID, rath: Optional[MikroNextRath] = None
) -> Iterator[WatchRoisSubscriptionRois]:
    """WatchRois



    Arguments:
        image (ID): image
        rath (mikro_next.rath.MikroNextRath, optional): The mikro rath client

    Returns:
        WatchRoisSubscriptionRois"""
    for event in subscribe(WatchRoisSubscription, {"image": image}, rath=rath):
        yield event.rois


AffineTransformationViewFilter.model_rebuild()
ChannelView.model_rebuild()
DatasetFilter.model_rebuild()
EraFilter.model_rebuild()
File.model_rebuild()
Image.model_rebuild()
ImageDerivedscaleviewsImage.model_rebuild()
ImageFilter.model_rebuild()
LinkedExpressionFilter.model_rebuild()
PartialPixelViewInput.model_rebuild()
ProvenanceFilter.model_rebuild()
RGBContextImage.model_rebuild()
StageFilter.model_rebuild()
Table.model_rebuild()
TimepointView.model_rebuild()
TimepointViewFilter.model_rebuild()
TreeInput.model_rebuild()
TreeNodeInput.model_rebuild()
ZarrStoreFilter.model_rebuild()
