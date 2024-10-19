from typing import Tuple, Literal, List, Optional, Dict, Union, Any
from pydantic import ConfigDict, Field, BaseModel
from fluss_next.funcs import aexecute, execute
from fluss_next.traits import MockableTrait
from fluss_next.scalars import EventValue, ValidatorFunction
from rath.scalars import ID
from datetime import datetime
from enum import Enum
from fluss_next.rath import FlussRath


class GraphNodeKind(str, Enum):
    REACTIVE = "REACTIVE"
    ARGS = "ARGS"
    RETURNS = "RETURNS"
    REKUEST = "REKUEST"
    REKUEST_FILTER = "REKUEST_FILTER"


class PortScope(str, Enum):
    GLOBAL = "GLOBAL"
    LOCAL = "LOCAL"


class PortKind(str, Enum):
    INT = "INT"
    STRING = "STRING"
    STRUCTURE = "STRUCTURE"
    LIST = "LIST"
    BOOL = "BOOL"
    DICT = "DICT"
    FLOAT = "FLOAT"
    DATE = "DATE"
    UNION = "UNION"
    MODEL = "MODEL"


class LogicalCondition(str, Enum):
    IS = "IS"
    IS_NOT = "IS_NOT"
    IN = "IN"


class EffectKind(str, Enum):
    MESSAGE = "MESSAGE"
    CUSTOM = "CUSTOM"


class AssignWidgetKind(str, Enum):
    SEARCH = "SEARCH"
    CHOICE = "CHOICE"
    SLIDER = "SLIDER"
    CUSTOM = "CUSTOM"
    STRING = "STRING"
    STATE_CHOICE = "STATE_CHOICE"


class ReturnWidgetKind(str, Enum):
    CHOICE = "CHOICE"
    CUSTOM = "CUSTOM"


class NodeKind(str, Enum):
    FUNCTION = "FUNCTION"
    GENERATOR = "GENERATOR"


class GraphEdgeKind(str, Enum):
    VANILLA = "VANILLA"
    LOGGING = "LOGGING"


class ReactiveImplementation(str, Enum):
    ZIP = "ZIP"
    COMBINELATEST = "COMBINELATEST"
    WITHLATEST = "WITHLATEST"
    BUFFER_COMPLETE = "BUFFER_COMPLETE"
    BUFFER_UNTIL = "BUFFER_UNTIL"
    DELAY = "DELAY"
    DELAY_UNTIL = "DELAY_UNTIL"
    CHUNK = "CHUNK"
    SPLIT = "SPLIT"
    OMIT = "OMIT"
    ENSURE = "ENSURE"
    SELECT = "SELECT"
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    MODULO = "MODULO"
    POWER = "POWER"
    JUST = "JUST"
    PREFIX = "PREFIX"
    SUFFIX = "SUFFIX"
    FILTER = "FILTER"
    GATE = "GATE"
    TO_LIST = "TO_LIST"
    FOREACH = "FOREACH"
    IF = "IF"
    AND = "AND"
    ALL = "ALL"


class RunEventKind(str, Enum):
    NEXT = "NEXT"
    ERROR = "ERROR"
    COMPLETE = "COMPLETE"
    UNKNOWN = "UNKNOWN"


class MapStrategy(str, Enum):
    MAP = "MAP"
    MAP_TO = "MAP_TO"
    MAP_FROM = "MAP_FROM"


class OffsetPaginationInput(BaseModel):
    offset: int
    limit: int
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class GraphInput(BaseModel):
    nodes: Tuple["GraphNodeInput", ...]
    edges: Tuple["GraphEdgeInput", ...]
    globals: Tuple["GlobalArgInput", ...]
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class GraphNodeInput(BaseModel):
    hello: Optional[str] = None
    path: Optional[str] = None
    id: str
    kind: GraphNodeKind
    position: "PositionInput"
    parent_node: Optional[str] = Field(alias="parentNode", default=None)
    ins: Tuple[Tuple["PortInput", ...], ...]
    outs: Tuple[Tuple["PortInput", ...], ...]
    constants: Tuple["PortInput", ...]
    voids: Tuple["PortInput", ...]
    constants_map: Dict = Field(alias="constantsMap")
    globals_map: Dict = Field(alias="globalsMap")
    description: Optional[str] = None
    title: Optional[str] = None
    retries: Optional[int] = None
    retry_delay: Optional[int] = Field(alias="retryDelay", default=None)
    node_kind: Optional[NodeKind] = Field(alias="nodeKind", default=None)
    next_timeout: Optional[int] = Field(alias="nextTimeout", default=None)
    hash: Optional[str] = None
    map_strategy: Optional[MapStrategy] = Field(alias="mapStrategy", default=None)
    allow_local_execution: Optional[bool] = Field(
        alias="allowLocalExecution", default=None
    )
    binds: Optional["BindsInput"] = None
    implementation: Optional[ReactiveImplementation] = None
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class PositionInput(BaseModel):
    x: float
    y: float
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class PortInput(BaseModel):
    validators: Optional[Tuple["ValidatorInput", ...]] = None
    key: str
    scope: PortScope
    label: Optional[str] = None
    kind: PortKind
    description: Optional[str] = None
    identifier: Optional[str] = None
    nullable: bool
    effects: Optional[Tuple["EffectInput", ...]] = None
    default: Optional[Any] = None
    children: Optional[Tuple["ChildPortInput", ...]] = None
    assign_widget: Optional["AssignWidgetInput"] = Field(
        alias="assignWidget", default=None
    )
    return_widget: Optional["ReturnWidgetInput"] = Field(
        alias="returnWidget", default=None
    )
    groups: Optional[Tuple[str, ...]] = None
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class ValidatorInput(BaseModel):
    function: ValidatorFunction
    dependencies: Optional[Tuple[str, ...]] = None
    label: Optional[str] = None
    error_message: Optional[str] = Field(alias="errorMessage", default=None)
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class EffectInput(BaseModel):
    label: str
    description: Optional[str] = None
    dependencies: Tuple["EffectDependencyInput", ...]
    kind: EffectKind
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class EffectDependencyInput(BaseModel):
    key: str
    condition: LogicalCondition
    value: Any
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class ChildPortInput(BaseModel):
    default: Optional[Any] = None
    key: str
    label: Optional[str] = None
    kind: PortKind
    scope: PortScope
    description: Optional[str] = None
    identifier: Optional[str] = None
    nullable: bool
    children: Optional[Tuple["ChildPortInput", ...]] = None
    effects: Optional[Tuple[EffectInput, ...]] = None
    assign_widget: Optional["AssignWidgetInput"] = Field(
        alias="assignWidget", default=None
    )
    return_widget: Optional["ReturnWidgetInput"] = Field(
        alias="returnWidget", default=None
    )
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class AssignWidgetInput(BaseModel):
    as_paragraph: Optional[bool] = Field(alias="asParagraph", default=None)
    kind: AssignWidgetKind
    query: Optional[str] = None
    choices: Optional[Tuple["ChoiceInput", ...]] = None
    state_choices: Optional[str] = Field(alias="stateChoices", default=None)
    follow_value: Optional[str] = Field(alias="followValue", default=None)
    min: Optional[int] = None
    max: Optional[int] = None
    step: Optional[int] = None
    placeholder: Optional[str] = None
    hook: Optional[str] = None
    ward: Optional[str] = None
    fallback: Optional["AssignWidgetInput"] = None
    filters: Optional[Tuple[ChildPortInput, ...]] = None
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class ChoiceInput(BaseModel):
    value: Any
    label: str
    description: Optional[str] = None
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class ReturnWidgetInput(BaseModel):
    kind: ReturnWidgetKind
    query: Optional[str] = None
    choices: Optional[Tuple[ChoiceInput, ...]] = None
    min: Optional[int] = None
    max: Optional[int] = None
    step: Optional[int] = None
    placeholder: Optional[str] = None
    hook: Optional[str] = None
    ward: Optional[str] = None
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class BindsInput(BaseModel):
    templates: Optional[Tuple[str, ...]] = None
    clients: Optional[Tuple[str, ...]] = None
    desired_instances: int = Field(alias="desiredInstances")
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class GraphEdgeInput(BaseModel):
    label: Optional[str] = None
    level: Optional[str] = None
    kind: GraphEdgeKind
    id: str
    source: str
    target: str
    source_handle: str = Field(alias="sourceHandle")
    target_handle: str = Field(alias="targetHandle")
    stream: Tuple["StreamItemInput", ...]
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class StreamItemInput(BaseModel):
    kind: PortKind
    label: str
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class GlobalArgInput(BaseModel):
    key: str
    port: PortInput
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class RunFragmentFlow(BaseModel):
    """Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)"""

    typename: Optional[Literal["Flow"]] = Field(
        alias="__typename", default="Flow", exclude=True
    )
    id: ID
    title: str
    model_config = ConfigDict(frozen=True)


class RunFragmentEvents(BaseModel):
    """RunEvent(id, created_at, reference, run, kind, t, caused_by, source, handle, value)"""

    typename: Optional[Literal["RunEvent"]] = Field(
        alias="__typename", default="RunEvent", exclude=True
    )
    kind: RunEventKind
    "The type of event"
    t: int
    caused_by: Tuple[ID, ...] = Field(alias="causedBy")
    created_at: datetime = Field(alias="createdAt")
    value: Optional[EventValue] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class RunFragment(BaseModel):
    typename: Optional[Literal["Run"]] = Field(
        alias="__typename", default="Run", exclude=True
    )
    id: ID
    assignation: ID
    flow: RunFragmentFlow
    events: Tuple[RunFragmentEvents, ...]
    created_at: datetime = Field(alias="createdAt")
    model_config = ConfigDict(frozen=True)


class ListWorkspaceFragment(BaseModel):
    typename: Optional[Literal["Workspace"]] = Field(
        alias="__typename", default="Workspace", exclude=True
    )
    id: ID
    title: str
    description: Optional[str] = Field(default=None)
    latest_flow: Optional["ListFlowFragment"] = Field(default=None, alias="latestFlow")
    model_config = ConfigDict(frozen=True)


class WorkspaceFragment(BaseModel):
    typename: Optional[Literal["Workspace"]] = Field(
        alias="__typename", default="Workspace", exclude=True
    )
    id: ID
    title: str
    latest_flow: Optional["FlowFragment"] = Field(default=None, alias="latestFlow")
    model_config = ConfigDict(frozen=True)


class FlussStringAssignWidgetFragment(BaseModel):
    typename: Optional[Literal["StringAssignWidget"]] = Field(
        alias="__typename", default="StringAssignWidget", exclude=True
    )
    kind: AssignWidgetKind
    placeholder: str
    as_paragraph: bool = Field(alias="asParagraph")
    model_config = ConfigDict(frozen=True)


class FlussSliderAssignWidgetFragment(BaseModel):
    typename: Optional[Literal["SliderAssignWidget"]] = Field(
        alias="__typename", default="SliderAssignWidget", exclude=True
    )
    kind: AssignWidgetKind
    min: Optional[int] = Field(default=None)
    max: Optional[int] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class FlussSearchAssignWidgetFragment(BaseModel):
    typename: Optional[Literal["SearchAssignWidget"]] = Field(
        alias="__typename", default="SearchAssignWidget", exclude=True
    )
    kind: AssignWidgetKind
    query: str
    ward: str
    model_config = ConfigDict(frozen=True)


class FlussCustomAssignWidgetFragment(BaseModel):
    typename: Optional[Literal["CustomAssignWidget"]] = Field(
        alias="__typename", default="CustomAssignWidget", exclude=True
    )
    ward: str
    hook: str
    model_config = ConfigDict(frozen=True)


class FlussChoiceAssignWidgetFragmentChoices(BaseModel):
    typename: Optional[Literal["Choice"]] = Field(
        alias="__typename", default="Choice", exclude=True
    )
    value: str
    label: str
    description: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class FlussChoiceAssignWidgetFragment(BaseModel):
    typename: Optional[Literal["ChoiceAssignWidget"]] = Field(
        alias="__typename", default="ChoiceAssignWidget", exclude=True
    )
    kind: AssignWidgetKind
    choices: Optional[Tuple[FlussChoiceAssignWidgetFragmentChoices, ...]] = Field(
        default=None
    )
    model_config = ConfigDict(frozen=True)


class FlussChildPortNestedFragmentChildren(BaseModel):
    typename: Optional[Literal["ChildPort"]] = Field(
        alias="__typename", default="ChildPort", exclude=True
    )
    kind: PortKind
    identifier: Optional[str] = Field(default=None)
    scope: PortScope
    assign_widget: Optional["FlussAssignWidgetFragment"] = Field(
        default=None, alias="assignWidget"
    )
    return_widget: Optional["FlussReturnWidgetFragment"] = Field(
        default=None, alias="returnWidget"
    )
    model_config = ConfigDict(frozen=True)


class FlussChildPortNestedFragment(BaseModel):
    typename: Optional[Literal["ChildPort"]] = Field(
        alias="__typename", default="ChildPort", exclude=True
    )
    kind: PortKind
    identifier: Optional[str] = Field(default=None)
    children: Optional[Tuple[FlussChildPortNestedFragmentChildren, ...]] = Field(
        default=None
    )
    scope: PortScope
    assign_widget: Optional["FlussAssignWidgetFragment"] = Field(
        default=None, alias="assignWidget"
    )
    return_widget: Optional["FlussReturnWidgetFragment"] = Field(
        default=None, alias="returnWidget"
    )
    model_config = ConfigDict(frozen=True)


class FlussChildPortFragment(BaseModel):
    typename: Optional[Literal["ChildPort"]] = Field(
        alias="__typename", default="ChildPort", exclude=True
    )
    kind: PortKind
    identifier: Optional[str] = Field(default=None)
    scope: PortScope
    children: Optional[Tuple[FlussChildPortNestedFragment, ...]] = Field(default=None)
    assign_widget: Optional["FlussAssignWidgetFragment"] = Field(
        default=None, alias="assignWidget"
    )
    return_widget: Optional["FlussReturnWidgetFragment"] = Field(
        default=None, alias="returnWidget"
    )
    nullable: bool
    model_config = ConfigDict(frozen=True)


class FlussEffectDependencyFragment(BaseModel):
    typename: Optional[Literal["EffectDependency"]] = Field(
        alias="__typename", default="EffectDependency", exclude=True
    )
    key: str
    condition: LogicalCondition
    value: str
    model_config = ConfigDict(frozen=True)


class FlussCustomEffectFragment(BaseModel):
    typename: Optional[Literal["CustomEffect"]] = Field(
        alias="__typename", default="CustomEffect", exclude=True
    )
    kind: EffectKind
    hook: str
    ward: str
    model_config = ConfigDict(frozen=True)


class FlussMessageEffectFragment(BaseModel):
    typename: Optional[Literal["MessageEffect"]] = Field(
        alias="__typename", default="MessageEffect", exclude=True
    )
    kind: EffectKind
    message: str
    model_config = ConfigDict(frozen=True)


class FlussPortEffectFragmentBase(BaseModel):
    kind: EffectKind
    dependencies: Tuple[FlussEffectDependencyFragment, ...]


class FlussPortEffectFragmentBaseFlussCustomEffect(
    FlussCustomEffectFragment, FlussPortEffectFragmentBase
):
    pass


class FlussPortEffectFragmentBaseFlussMessageEffect(
    FlussMessageEffectFragment, FlussPortEffectFragmentBase
):
    pass


FlussPortEffectFragment = Union[
    FlussPortEffectFragmentBaseFlussCustomEffect,
    FlussPortEffectFragmentBaseFlussMessageEffect,
    FlussPortEffectFragmentBase,
]


class FlussAssignWidgetFragmentBase(BaseModel):
    kind: AssignWidgetKind


class FlussAssignWidgetFragmentBaseFlussStringAssignWidget(
    FlussStringAssignWidgetFragment, FlussAssignWidgetFragmentBase
):
    pass


class FlussAssignWidgetFragmentBaseFlussSearchAssignWidget(
    FlussSearchAssignWidgetFragment, FlussAssignWidgetFragmentBase
):
    pass


class FlussAssignWidgetFragmentBaseFlussSliderAssignWidget(
    FlussSliderAssignWidgetFragment, FlussAssignWidgetFragmentBase
):
    pass


class FlussAssignWidgetFragmentBaseFlussChoiceAssignWidget(
    FlussChoiceAssignWidgetFragment, FlussAssignWidgetFragmentBase
):
    pass


class FlussAssignWidgetFragmentBaseFlussCustomAssignWidget(
    FlussCustomAssignWidgetFragment, FlussAssignWidgetFragmentBase
):
    pass


FlussAssignWidgetFragment = Union[
    FlussAssignWidgetFragmentBaseFlussStringAssignWidget,
    FlussAssignWidgetFragmentBaseFlussSearchAssignWidget,
    FlussAssignWidgetFragmentBaseFlussSliderAssignWidget,
    FlussAssignWidgetFragmentBaseFlussChoiceAssignWidget,
    FlussAssignWidgetFragmentBaseFlussCustomAssignWidget,
    FlussAssignWidgetFragmentBase,
]


class ValidatorFragment(BaseModel):
    typename: Optional[Literal["Validator"]] = Field(
        alias="__typename", default="Validator", exclude=True
    )
    function: ValidatorFunction
    dependencies: Optional[Tuple[str, ...]] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class FlussPortFragment(BaseModel):
    typename: Optional[Literal["Port"]] = Field(
        alias="__typename", default="Port", exclude=True
    )
    key: str
    label: Optional[str] = Field(default=None)
    nullable: bool
    description: Optional[str] = Field(default=None)
    scope: PortScope
    effects: Optional[Tuple[FlussPortEffectFragment, ...]] = Field(default=None)
    assign_widget: Optional[FlussAssignWidgetFragment] = Field(
        default=None, alias="assignWidget"
    )
    return_widget: Optional["FlussReturnWidgetFragment"] = Field(
        default=None, alias="returnWidget"
    )
    kind: PortKind
    identifier: Optional[str] = Field(default=None)
    children: Optional[Tuple[FlussChildPortFragment, ...]] = Field(default=None)
    default: Optional[Any] = Field(default=None)
    nullable: bool
    groups: Optional[Tuple[str, ...]] = Field(default=None)
    validators: Optional[Tuple[ValidatorFragment, ...]] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class FlussCustomReturnWidgetFragment(BaseModel):
    typename: Optional[Literal["CustomReturnWidget"]] = Field(
        alias="__typename", default="CustomReturnWidget", exclude=True
    )
    kind: ReturnWidgetKind
    hook: str
    ward: str
    model_config = ConfigDict(frozen=True)


class FlussChoiceReturnWidgetFragmentChoices(BaseModel):
    typename: Optional[Literal["Choice"]] = Field(
        alias="__typename", default="Choice", exclude=True
    )
    label: str
    value: str
    description: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class FlussChoiceReturnWidgetFragment(BaseModel):
    typename: Optional[Literal["ChoiceReturnWidget"]] = Field(
        alias="__typename", default="ChoiceReturnWidget", exclude=True
    )
    choices: Optional[Tuple[FlussChoiceReturnWidgetFragmentChoices, ...]] = Field(
        default=None
    )
    model_config = ConfigDict(frozen=True)


class FlussReturnWidgetFragmentBase(BaseModel):
    kind: ReturnWidgetKind


class FlussReturnWidgetFragmentBaseFlussCustomReturnWidget(
    FlussCustomReturnWidgetFragment, FlussReturnWidgetFragmentBase
):
    pass


class FlussReturnWidgetFragmentBaseFlussChoiceReturnWidget(
    FlussChoiceReturnWidgetFragment, FlussReturnWidgetFragmentBase
):
    pass


FlussReturnWidgetFragment = Union[
    FlussReturnWidgetFragmentBaseFlussCustomReturnWidget,
    FlussReturnWidgetFragmentBaseFlussChoiceReturnWidget,
    FlussReturnWidgetFragmentBase,
]


class ReactiveTemplateFragment(BaseModel):
    typename: Optional[Literal["ReactiveTemplate"]] = Field(
        alias="__typename", default="ReactiveTemplate", exclude=True
    )
    id: ID
    ins: Tuple[Tuple[FlussPortFragment, ...], ...]
    outs: Tuple[Tuple[FlussPortFragment, ...], ...]
    constants: Tuple[FlussPortFragment, ...]
    implementation: ReactiveImplementation
    "Check async Programming Textbook"
    title: str
    description: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class BaseGraphNodeFragmentBase(BaseModel):
    ins: Tuple[Tuple[FlussPortFragment, ...], ...]
    outs: Tuple[Tuple[FlussPortFragment, ...], ...]
    constants: Tuple[FlussPortFragment, ...]
    voids: Tuple[FlussPortFragment, ...]
    globals_map: Dict = Field(alias="globalsMap")
    constants_map: Dict = Field(alias="constantsMap")
    title: str
    description: str
    kind: GraphNodeKind


class FlussBindsFragment(BaseModel):
    typename: Optional[Literal["Binds"]] = Field(
        alias="__typename", default="Binds", exclude=True
    )
    templates: Tuple[ID, ...]
    model_config = ConfigDict(frozen=True)


class RetriableNodeFragmentBase(BaseModel):
    retries: Optional[int] = Field(default=None)
    retry_delay: Optional[int] = Field(default=None, alias="retryDelay")


class AssignableNodeFragmentBase(BaseModel):
    next_timeout: Optional[int] = Field(default=None, alias="nextTimeout")


class RekuestNodeFragmentBase(BaseModel):
    hash: str
    map_strategy: str = Field(alias="mapStrategy")
    allow_local_execution: bool = Field(alias="allowLocalExecution")
    binds: FlussBindsFragment
    node_kind: NodeKind = Field(alias="nodeKind")


class RekuestMapNodeFragment(
    RekuestNodeFragmentBase,
    AssignableNodeFragmentBase,
    RetriableNodeFragmentBase,
    BaseGraphNodeFragmentBase,
    BaseModel,
):
    typename: Optional[Literal["RekuestMapNode"]] = Field(
        alias="__typename", default="RekuestMapNode", exclude=True
    )
    hello: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class RekuestFilterNodeFragment(
    RekuestNodeFragmentBase,
    AssignableNodeFragmentBase,
    RetriableNodeFragmentBase,
    BaseGraphNodeFragmentBase,
    BaseModel,
):
    typename: Optional[Literal["RekuestFilterNode"]] = Field(
        alias="__typename", default="RekuestFilterNode", exclude=True
    )
    path: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class ReactiveNodeFragment(BaseGraphNodeFragmentBase, BaseModel):
    typename: Optional[Literal["ReactiveNode"]] = Field(
        alias="__typename", default="ReactiveNode", exclude=True
    )
    implementation: ReactiveImplementation
    model_config = ConfigDict(frozen=True)


class ArgNodeFragment(BaseGraphNodeFragmentBase, BaseModel):
    typename: Optional[Literal["ArgNode"]] = Field(
        alias="__typename", default="ArgNode", exclude=True
    )
    model_config = ConfigDict(frozen=True)


class ReturnNodeFragment(BaseGraphNodeFragmentBase, BaseModel):
    typename: Optional[Literal["ReturnNode"]] = Field(
        alias="__typename", default="ReturnNode", exclude=True
    )
    model_config = ConfigDict(frozen=True)


class GraphNodeFragmentBasePosition(BaseModel):
    typename: Optional[Literal["Position"]] = Field(
        alias="__typename", default="Position", exclude=True
    )
    x: float
    y: float
    model_config = ConfigDict(frozen=True)


class GraphNodeFragmentBase(BaseModel):
    id: ID
    position: GraphNodeFragmentBasePosition
    parent_node: Optional[str] = Field(default=None, alias="parentNode")


class GraphNodeFragmentBaseRekuestFilterNode(
    RekuestFilterNodeFragment, GraphNodeFragmentBase
):
    pass


class GraphNodeFragmentBaseRekuestMapNode(
    RekuestMapNodeFragment, GraphNodeFragmentBase
):
    pass


class GraphNodeFragmentBaseReactiveNode(ReactiveNodeFragment, GraphNodeFragmentBase):
    pass


class GraphNodeFragmentBaseArgNode(ArgNodeFragment, GraphNodeFragmentBase):
    pass


class GraphNodeFragmentBaseReturnNode(ReturnNodeFragment, GraphNodeFragmentBase):
    pass


GraphNodeFragment = Union[
    GraphNodeFragmentBaseRekuestFilterNode,
    GraphNodeFragmentBaseRekuestMapNode,
    GraphNodeFragmentBaseReactiveNode,
    GraphNodeFragmentBaseArgNode,
    GraphNodeFragmentBaseReturnNode,
    GraphNodeFragmentBase,
]


class StreamItemFragment(MockableTrait, BaseModel):
    typename: Optional[Literal["StreamItem"]] = Field(
        alias="__typename", default="StreamItem", exclude=True
    )
    kind: PortKind
    label: str
    model_config = ConfigDict(frozen=True)


class BaseGraphEdgeFragmentBase(BaseModel):
    id: ID
    source: str
    source_handle: str = Field(alias="sourceHandle")
    target: str
    target_handle: str = Field(alias="targetHandle")
    kind: GraphEdgeKind
    stream: Tuple[StreamItemFragment, ...]


class LoggingEdgeFragment(BaseGraphEdgeFragmentBase, BaseModel):
    typename: Optional[Literal["LoggingEdge"]] = Field(
        alias="__typename", default="LoggingEdge", exclude=True
    )
    level: str
    model_config = ConfigDict(frozen=True)


class VanillaEdgeFragment(BaseGraphEdgeFragmentBase, BaseModel):
    typename: Optional[Literal["VanillaEdge"]] = Field(
        alias="__typename", default="VanillaEdge", exclude=True
    )
    label: Optional[str] = Field(default=None)
    model_config = ConfigDict(frozen=True)


class GraphEdgeFragmentBase(BaseModel):
    id: ID


class GraphEdgeFragmentBaseLoggingEdge(LoggingEdgeFragment, GraphEdgeFragmentBase):
    pass


class GraphEdgeFragmentBaseVanillaEdge(VanillaEdgeFragment, GraphEdgeFragmentBase):
    pass


GraphEdgeFragment = Union[
    GraphEdgeFragmentBaseLoggingEdge,
    GraphEdgeFragmentBaseVanillaEdge,
    GraphEdgeFragmentBase,
]


class GlobalArgFragment(BaseModel):
    typename: Optional[Literal["GlobalArg"]] = Field(
        alias="__typename", default="GlobalArg", exclude=True
    )
    key: str
    port: FlussPortFragment
    model_config = ConfigDict(frozen=True)


class GraphFragment(BaseModel):
    typename: Optional[Literal["Graph"]] = Field(
        alias="__typename", default="Graph", exclude=True
    )
    nodes: Tuple[GraphNodeFragment, ...]
    edges: Tuple[GraphEdgeFragment, ...]
    globals: Tuple[GlobalArgFragment, ...]
    model_config = ConfigDict(frozen=True)


class FlowFragmentWorkspace(BaseModel):
    """Graph is a Template for a Template"""

    typename: Optional[Literal["Workspace"]] = Field(
        alias="__typename", default="Workspace", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class FlowFragment(BaseModel):
    typename: Optional[Literal["Flow"]] = Field(
        alias="__typename", default="Flow", exclude=True
    )
    id: ID
    graph: GraphFragment
    title: str
    description: Optional[str] = Field(default=None)
    created_at: datetime = Field(alias="createdAt")
    workspace: FlowFragmentWorkspace
    model_config = ConfigDict(frozen=True)


class ListFlowFragmentWorkspace(BaseModel):
    """Graph is a Template for a Template"""

    typename: Optional[Literal["Workspace"]] = Field(
        alias="__typename", default="Workspace", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class ListFlowFragment(BaseModel):
    typename: Optional[Literal["Flow"]] = Field(
        alias="__typename", default="Flow", exclude=True
    )
    id: ID
    title: str
    created_at: datetime = Field(alias="createdAt")
    workspace: ListFlowFragmentWorkspace
    model_config = ConfigDict(frozen=True)


class CreateRunMutationCreaterun(BaseModel):
    """Run(id, created_at, flow, assignation, status, snapshot_interval)"""

    typename: Optional[Literal["Run"]] = Field(
        alias="__typename", default="Run", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class CreateRunMutation(BaseModel):
    """Start a run on fluss"""

    create_run: CreateRunMutationCreaterun = Field(alias="createRun")

    class Arguments(BaseModel):
        assignation: ID
        flow: ID
        snapshot_interval: int

    class Meta:
        document = "mutation CreateRun($assignation: ID!, $flow: ID!, $snapshot_interval: Int!) {\n  createRun(\n    input: {assignation: $assignation, flow: $flow, snapshotInterval: $snapshot_interval}\n  ) {\n    id\n  }\n}"


class CloseRunMutationCloserun(BaseModel):
    """Run(id, created_at, flow, assignation, status, snapshot_interval)"""

    typename: Optional[Literal["Run"]] = Field(
        alias="__typename", default="Run", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class CloseRunMutation(BaseModel):
    """Start a run on fluss"""

    close_run: CloseRunMutationCloserun = Field(alias="closeRun")

    class Arguments(BaseModel):
        run: ID

    class Meta:
        document = "mutation CloseRun($run: ID!) {\n  closeRun(input: {run: $run}) {\n    id\n  }\n}"


class SnapshotMutationSnapshot(BaseModel):
    """Snapshot(id, created_at, run, t, status)"""

    typename: Optional[Literal["Snapshot"]] = Field(
        alias="__typename", default="Snapshot", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class SnapshotMutation(BaseModel):
    """Snapshot the current state on the fluss platform"""

    snapshot: SnapshotMutationSnapshot

    class Arguments(BaseModel):
        run: ID
        events: List[ID]
        t: int

    class Meta:
        document = "mutation Snapshot($run: ID!, $events: [ID!]!, $t: Int!) {\n  snapshot(input: {run: $run, events: $events, t: $t}) {\n    id\n  }\n}"


class TrackMutationTrack(BaseModel):
    """RunEvent(id, created_at, reference, run, kind, t, caused_by, source, handle, value)"""

    typename: Optional[Literal["RunEvent"]] = Field(
        alias="__typename", default="RunEvent", exclude=True
    )
    id: ID
    kind: RunEventKind
    "The type of event"
    value: Optional[EventValue] = Field(default=None)
    caused_by: Tuple[ID, ...] = Field(alias="causedBy")
    model_config = ConfigDict(frozen=True)


class TrackMutation(BaseModel):
    """Track a new event on the fluss platform"""

    track: TrackMutationTrack

    class Arguments(BaseModel):
        reference: str
        run: ID
        t: int
        caused_by: List[ID]
        kind: RunEventKind
        value: Optional[EventValue] = Field(default=None)
        exception: Optional[str] = Field(default=None)
        message: Optional[str] = Field(default=None)
        source: str
        handle: str

    class Meta:
        document = "mutation Track($reference: String!, $run: ID!, $t: Int!, $caused_by: [ID!]!, $kind: RunEventKind!, $value: EventValue, $exception: String, $message: String, $source: String!, $handle: String!) {\n  track(\n    input: {run: $run, kind: $kind, value: $value, exception: $exception, causedBy: $caused_by, t: $t, reference: $reference, message: $message, source: $source, handle: $handle}\n  ) {\n    id\n    kind\n    value\n    causedBy\n  }\n}"


class UpdateWorkspaceMutation(BaseModel):
    update_workspace: WorkspaceFragment = Field(alias="updateWorkspace")

    class Arguments(BaseModel):
        id: ID
        graph: GraphInput

    class Meta:
        document = "fragment StreamItem on StreamItem {\n  kind\n  label\n}\n\nfragment FlussChildPortNested on ChildPort {\n  __typename\n  kind\n  identifier\n  children {\n    kind\n    identifier\n    scope\n    assignWidget {\n      ...FlussAssignWidget\n    }\n    returnWidget {\n      ...FlussReturnWidget\n    }\n  }\n  scope\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n}\n\nfragment FlussSliderAssignWidget on SliderAssignWidget {\n  __typename\n  kind\n  min\n  max\n}\n\nfragment FlussChoiceReturnWidget on ChoiceReturnWidget {\n  __typename\n  choices {\n    label\n    value\n    description\n  }\n}\n\nfragment FlussMessageEffect on MessageEffect {\n  __typename\n  kind\n  message\n}\n\nfragment FlussSearchAssignWidget on SearchAssignWidget {\n  __typename\n  kind\n  query\n  ward\n}\n\nfragment FlussEffectDependency on EffectDependency {\n  key\n  condition\n  value\n}\n\nfragment FlussChoiceAssignWidget on ChoiceAssignWidget {\n  __typename\n  kind\n  choices {\n    value\n    label\n    description\n  }\n}\n\nfragment FlussCustomEffect on CustomEffect {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomReturnWidget on CustomReturnWidget {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomAssignWidget on CustomAssignWidget {\n  __typename\n  ward\n  hook\n}\n\nfragment FlussStringAssignWidget on StringAssignWidget {\n  __typename\n  kind\n  placeholder\n  asParagraph\n}\n\nfragment FlussBinds on Binds {\n  templates\n}\n\nfragment RekuestNode on RekuestNode {\n  hash\n  mapStrategy\n  allowLocalExecution\n  binds {\n    ...FlussBinds\n  }\n  nodeKind\n}\n\nfragment FlussChildPort on ChildPort {\n  __typename\n  kind\n  identifier\n  scope\n  children {\n    ...FlussChildPortNested\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  nullable\n}\n\nfragment FlussPortEffect on Effect {\n  __typename\n  kind\n  dependencies {\n    ...FlussEffectDependency\n  }\n  ...FlussCustomEffect\n  ...FlussMessageEffect\n}\n\nfragment FlussAssignWidget on AssignWidget {\n  __typename\n  kind\n  ...FlussStringAssignWidget\n  ...FlussSearchAssignWidget\n  ...FlussSliderAssignWidget\n  ...FlussChoiceAssignWidget\n  ...FlussCustomAssignWidget\n}\n\nfragment Validator on Validator {\n  function\n  dependencies\n}\n\nfragment RetriableNode on RetriableNode {\n  retries\n  retryDelay\n}\n\nfragment AssignableNode on AssignableNode {\n  nextTimeout\n}\n\nfragment BaseGraphNode on GraphNode {\n  __typename\n  ins {\n    ...FlussPort\n  }\n  outs {\n    ...FlussPort\n  }\n  constants {\n    ...FlussPort\n  }\n  voids {\n    ...FlussPort\n  }\n  globalsMap\n  constantsMap\n  title\n  description\n  kind\n}\n\nfragment BaseGraphEdge on GraphEdge {\n  __typename\n  id\n  source\n  sourceHandle\n  target\n  targetHandle\n  kind\n  stream {\n    ...StreamItem\n  }\n}\n\nfragment FlussReturnWidget on ReturnWidget {\n  __typename\n  kind\n  ...FlussCustomReturnWidget\n  ...FlussChoiceReturnWidget\n}\n\nfragment RekuestMapNode on RekuestMapNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  hello\n}\n\nfragment ReactiveNode on ReactiveNode {\n  ...BaseGraphNode\n  __typename\n  implementation\n}\n\nfragment VanillaEdge on VanillaEdge {\n  ...BaseGraphEdge\n  label\n}\n\nfragment LoggingEdge on LoggingEdge {\n  ...BaseGraphEdge\n  level\n}\n\nfragment FlussPort on Port {\n  __typename\n  key\n  label\n  nullable\n  description\n  scope\n  effects {\n    ...FlussPortEffect\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  kind\n  identifier\n  children {\n    ...FlussChildPort\n  }\n  default\n  nullable\n  groups\n  validators {\n    ...Validator\n  }\n}\n\nfragment ArgNode on ArgNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment ReturnNode on ReturnNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment RekuestFilterNode on RekuestFilterNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  path\n}\n\nfragment GlobalArg on GlobalArg {\n  key\n  port {\n    ...FlussPort\n  }\n}\n\nfragment GraphEdge on GraphEdge {\n  __typename\n  id\n  ...LoggingEdge\n  ...VanillaEdge\n}\n\nfragment GraphNode on GraphNode {\n  __typename\n  id\n  position {\n    x\n    y\n  }\n  parentNode\n  ...RekuestFilterNode\n  ...RekuestMapNode\n  ...ReactiveNode\n  ...ArgNode\n  ...ReturnNode\n}\n\nfragment Graph on Graph {\n  nodes {\n    ...GraphNode\n  }\n  edges {\n    ...GraphEdge\n  }\n  globals {\n    ...GlobalArg\n  }\n}\n\nfragment Flow on Flow {\n  __typename\n  id\n  graph {\n    ...Graph\n  }\n  title\n  description\n  createdAt\n  workspace {\n    id\n  }\n}\n\nfragment Workspace on Workspace {\n  id\n  title\n  latestFlow {\n    ...Flow\n  }\n}\n\nmutation UpdateWorkspace($id: ID!, $graph: GraphInput!) {\n  updateWorkspace(input: {workspace: $id, graph: $graph}) {\n    ...Workspace\n  }\n}"


class CreateWorkspaceMutation(BaseModel):
    create_workspace: WorkspaceFragment = Field(alias="createWorkspace")

    class Arguments(BaseModel):
        name: Optional[str] = Field(default=None)

    class Meta:
        document = "fragment StreamItem on StreamItem {\n  kind\n  label\n}\n\nfragment FlussChildPortNested on ChildPort {\n  __typename\n  kind\n  identifier\n  children {\n    kind\n    identifier\n    scope\n    assignWidget {\n      ...FlussAssignWidget\n    }\n    returnWidget {\n      ...FlussReturnWidget\n    }\n  }\n  scope\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n}\n\nfragment FlussSliderAssignWidget on SliderAssignWidget {\n  __typename\n  kind\n  min\n  max\n}\n\nfragment FlussChoiceReturnWidget on ChoiceReturnWidget {\n  __typename\n  choices {\n    label\n    value\n    description\n  }\n}\n\nfragment FlussMessageEffect on MessageEffect {\n  __typename\n  kind\n  message\n}\n\nfragment FlussSearchAssignWidget on SearchAssignWidget {\n  __typename\n  kind\n  query\n  ward\n}\n\nfragment FlussEffectDependency on EffectDependency {\n  key\n  condition\n  value\n}\n\nfragment FlussChoiceAssignWidget on ChoiceAssignWidget {\n  __typename\n  kind\n  choices {\n    value\n    label\n    description\n  }\n}\n\nfragment FlussCustomEffect on CustomEffect {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomReturnWidget on CustomReturnWidget {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomAssignWidget on CustomAssignWidget {\n  __typename\n  ward\n  hook\n}\n\nfragment FlussStringAssignWidget on StringAssignWidget {\n  __typename\n  kind\n  placeholder\n  asParagraph\n}\n\nfragment FlussBinds on Binds {\n  templates\n}\n\nfragment RekuestNode on RekuestNode {\n  hash\n  mapStrategy\n  allowLocalExecution\n  binds {\n    ...FlussBinds\n  }\n  nodeKind\n}\n\nfragment FlussChildPort on ChildPort {\n  __typename\n  kind\n  identifier\n  scope\n  children {\n    ...FlussChildPortNested\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  nullable\n}\n\nfragment FlussPortEffect on Effect {\n  __typename\n  kind\n  dependencies {\n    ...FlussEffectDependency\n  }\n  ...FlussCustomEffect\n  ...FlussMessageEffect\n}\n\nfragment FlussAssignWidget on AssignWidget {\n  __typename\n  kind\n  ...FlussStringAssignWidget\n  ...FlussSearchAssignWidget\n  ...FlussSliderAssignWidget\n  ...FlussChoiceAssignWidget\n  ...FlussCustomAssignWidget\n}\n\nfragment Validator on Validator {\n  function\n  dependencies\n}\n\nfragment RetriableNode on RetriableNode {\n  retries\n  retryDelay\n}\n\nfragment AssignableNode on AssignableNode {\n  nextTimeout\n}\n\nfragment BaseGraphNode on GraphNode {\n  __typename\n  ins {\n    ...FlussPort\n  }\n  outs {\n    ...FlussPort\n  }\n  constants {\n    ...FlussPort\n  }\n  voids {\n    ...FlussPort\n  }\n  globalsMap\n  constantsMap\n  title\n  description\n  kind\n}\n\nfragment BaseGraphEdge on GraphEdge {\n  __typename\n  id\n  source\n  sourceHandle\n  target\n  targetHandle\n  kind\n  stream {\n    ...StreamItem\n  }\n}\n\nfragment FlussReturnWidget on ReturnWidget {\n  __typename\n  kind\n  ...FlussCustomReturnWidget\n  ...FlussChoiceReturnWidget\n}\n\nfragment RekuestMapNode on RekuestMapNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  hello\n}\n\nfragment ReactiveNode on ReactiveNode {\n  ...BaseGraphNode\n  __typename\n  implementation\n}\n\nfragment VanillaEdge on VanillaEdge {\n  ...BaseGraphEdge\n  label\n}\n\nfragment LoggingEdge on LoggingEdge {\n  ...BaseGraphEdge\n  level\n}\n\nfragment FlussPort on Port {\n  __typename\n  key\n  label\n  nullable\n  description\n  scope\n  effects {\n    ...FlussPortEffect\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  kind\n  identifier\n  children {\n    ...FlussChildPort\n  }\n  default\n  nullable\n  groups\n  validators {\n    ...Validator\n  }\n}\n\nfragment ArgNode on ArgNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment ReturnNode on ReturnNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment RekuestFilterNode on RekuestFilterNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  path\n}\n\nfragment GlobalArg on GlobalArg {\n  key\n  port {\n    ...FlussPort\n  }\n}\n\nfragment GraphEdge on GraphEdge {\n  __typename\n  id\n  ...LoggingEdge\n  ...VanillaEdge\n}\n\nfragment GraphNode on GraphNode {\n  __typename\n  id\n  position {\n    x\n    y\n  }\n  parentNode\n  ...RekuestFilterNode\n  ...RekuestMapNode\n  ...ReactiveNode\n  ...ArgNode\n  ...ReturnNode\n}\n\nfragment Graph on Graph {\n  nodes {\n    ...GraphNode\n  }\n  edges {\n    ...GraphEdge\n  }\n  globals {\n    ...GlobalArg\n  }\n}\n\nfragment Flow on Flow {\n  __typename\n  id\n  graph {\n    ...Graph\n  }\n  title\n  description\n  createdAt\n  workspace {\n    id\n  }\n}\n\nfragment Workspace on Workspace {\n  id\n  title\n  latestFlow {\n    ...Flow\n  }\n}\n\nmutation CreateWorkspace($name: String) {\n  createWorkspace(input: {title: $name}) {\n    ...Workspace\n  }\n}"


class RunQuery(BaseModel):
    run: RunFragment

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Run on Run {\n  id\n  assignation\n  flow {\n    id\n    title\n  }\n  events {\n    kind\n    t\n    causedBy\n    createdAt\n    value\n  }\n  createdAt\n}\n\nquery Run($id: ID!) {\n  run(id: $id) {\n    ...Run\n  }\n}"


class SearchRunsQueryOptions(BaseModel):
    """Run(id, created_at, flow, assignation, status, snapshot_interval)"""

    typename: Optional[Literal["Run"]] = Field(
        alias="__typename", default="Run", exclude=True
    )
    value: ID
    label: ID
    model_config = ConfigDict(frozen=True)


class SearchRunsQuery(BaseModel):
    options: Tuple[SearchRunsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchRuns($search: String, $values: [ID!]) {\n  options: runs(filters: {search: $search, ids: $values}) {\n    value: id\n    label: assignation\n  }\n}"


class WorkspaceQuery(BaseModel):
    workspace: WorkspaceFragment

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment StreamItem on StreamItem {\n  kind\n  label\n}\n\nfragment FlussChildPortNested on ChildPort {\n  __typename\n  kind\n  identifier\n  children {\n    kind\n    identifier\n    scope\n    assignWidget {\n      ...FlussAssignWidget\n    }\n    returnWidget {\n      ...FlussReturnWidget\n    }\n  }\n  scope\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n}\n\nfragment FlussSliderAssignWidget on SliderAssignWidget {\n  __typename\n  kind\n  min\n  max\n}\n\nfragment FlussChoiceReturnWidget on ChoiceReturnWidget {\n  __typename\n  choices {\n    label\n    value\n    description\n  }\n}\n\nfragment FlussMessageEffect on MessageEffect {\n  __typename\n  kind\n  message\n}\n\nfragment FlussSearchAssignWidget on SearchAssignWidget {\n  __typename\n  kind\n  query\n  ward\n}\n\nfragment FlussEffectDependency on EffectDependency {\n  key\n  condition\n  value\n}\n\nfragment FlussChoiceAssignWidget on ChoiceAssignWidget {\n  __typename\n  kind\n  choices {\n    value\n    label\n    description\n  }\n}\n\nfragment FlussCustomEffect on CustomEffect {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomReturnWidget on CustomReturnWidget {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomAssignWidget on CustomAssignWidget {\n  __typename\n  ward\n  hook\n}\n\nfragment FlussStringAssignWidget on StringAssignWidget {\n  __typename\n  kind\n  placeholder\n  asParagraph\n}\n\nfragment FlussBinds on Binds {\n  templates\n}\n\nfragment RekuestNode on RekuestNode {\n  hash\n  mapStrategy\n  allowLocalExecution\n  binds {\n    ...FlussBinds\n  }\n  nodeKind\n}\n\nfragment FlussChildPort on ChildPort {\n  __typename\n  kind\n  identifier\n  scope\n  children {\n    ...FlussChildPortNested\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  nullable\n}\n\nfragment FlussPortEffect on Effect {\n  __typename\n  kind\n  dependencies {\n    ...FlussEffectDependency\n  }\n  ...FlussCustomEffect\n  ...FlussMessageEffect\n}\n\nfragment FlussAssignWidget on AssignWidget {\n  __typename\n  kind\n  ...FlussStringAssignWidget\n  ...FlussSearchAssignWidget\n  ...FlussSliderAssignWidget\n  ...FlussChoiceAssignWidget\n  ...FlussCustomAssignWidget\n}\n\nfragment Validator on Validator {\n  function\n  dependencies\n}\n\nfragment RetriableNode on RetriableNode {\n  retries\n  retryDelay\n}\n\nfragment AssignableNode on AssignableNode {\n  nextTimeout\n}\n\nfragment BaseGraphNode on GraphNode {\n  __typename\n  ins {\n    ...FlussPort\n  }\n  outs {\n    ...FlussPort\n  }\n  constants {\n    ...FlussPort\n  }\n  voids {\n    ...FlussPort\n  }\n  globalsMap\n  constantsMap\n  title\n  description\n  kind\n}\n\nfragment BaseGraphEdge on GraphEdge {\n  __typename\n  id\n  source\n  sourceHandle\n  target\n  targetHandle\n  kind\n  stream {\n    ...StreamItem\n  }\n}\n\nfragment FlussReturnWidget on ReturnWidget {\n  __typename\n  kind\n  ...FlussCustomReturnWidget\n  ...FlussChoiceReturnWidget\n}\n\nfragment RekuestMapNode on RekuestMapNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  hello\n}\n\nfragment ReactiveNode on ReactiveNode {\n  ...BaseGraphNode\n  __typename\n  implementation\n}\n\nfragment VanillaEdge on VanillaEdge {\n  ...BaseGraphEdge\n  label\n}\n\nfragment LoggingEdge on LoggingEdge {\n  ...BaseGraphEdge\n  level\n}\n\nfragment FlussPort on Port {\n  __typename\n  key\n  label\n  nullable\n  description\n  scope\n  effects {\n    ...FlussPortEffect\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  kind\n  identifier\n  children {\n    ...FlussChildPort\n  }\n  default\n  nullable\n  groups\n  validators {\n    ...Validator\n  }\n}\n\nfragment ArgNode on ArgNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment ReturnNode on ReturnNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment RekuestFilterNode on RekuestFilterNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  path\n}\n\nfragment GlobalArg on GlobalArg {\n  key\n  port {\n    ...FlussPort\n  }\n}\n\nfragment GraphEdge on GraphEdge {\n  __typename\n  id\n  ...LoggingEdge\n  ...VanillaEdge\n}\n\nfragment GraphNode on GraphNode {\n  __typename\n  id\n  position {\n    x\n    y\n  }\n  parentNode\n  ...RekuestFilterNode\n  ...RekuestMapNode\n  ...ReactiveNode\n  ...ArgNode\n  ...ReturnNode\n}\n\nfragment Graph on Graph {\n  nodes {\n    ...GraphNode\n  }\n  edges {\n    ...GraphEdge\n  }\n  globals {\n    ...GlobalArg\n  }\n}\n\nfragment Flow on Flow {\n  __typename\n  id\n  graph {\n    ...Graph\n  }\n  title\n  description\n  createdAt\n  workspace {\n    id\n  }\n}\n\nfragment Workspace on Workspace {\n  id\n  title\n  latestFlow {\n    ...Flow\n  }\n}\n\nquery Workspace($id: ID!) {\n  workspace(id: $id) {\n    ...Workspace\n  }\n}"


class WorkspacesQuery(BaseModel):
    workspaces: Tuple[ListWorkspaceFragment, ...]

    class Arguments(BaseModel):
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "fragment ListFlow on Flow {\n  id\n  title\n  createdAt\n  workspace {\n    id\n  }\n}\n\nfragment ListWorkspace on Workspace {\n  id\n  title\n  description\n  latestFlow {\n    ...ListFlow\n  }\n}\n\nquery Workspaces($pagination: OffsetPaginationInput) {\n  workspaces(pagination: $pagination) {\n    ...ListWorkspace\n  }\n}"


class ReactiveTemplatesQuery(BaseModel):
    reactive_templates: Tuple[ReactiveTemplateFragment, ...] = Field(
        alias="reactiveTemplates"
    )

    class Arguments(BaseModel):
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "fragment FlussChoiceReturnWidget on ChoiceReturnWidget {\n  __typename\n  choices {\n    label\n    value\n    description\n  }\n}\n\nfragment FlussCustomReturnWidget on CustomReturnWidget {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussMessageEffect on MessageEffect {\n  __typename\n  kind\n  message\n}\n\nfragment FlussChoiceAssignWidget on ChoiceAssignWidget {\n  __typename\n  kind\n  choices {\n    value\n    label\n    description\n  }\n}\n\nfragment FlussCustomAssignWidget on CustomAssignWidget {\n  __typename\n  ward\n  hook\n}\n\nfragment FlussSearchAssignWidget on SearchAssignWidget {\n  __typename\n  kind\n  query\n  ward\n}\n\nfragment FlussChildPortNested on ChildPort {\n  __typename\n  kind\n  identifier\n  children {\n    kind\n    identifier\n    scope\n    assignWidget {\n      ...FlussAssignWidget\n    }\n    returnWidget {\n      ...FlussReturnWidget\n    }\n  }\n  scope\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n}\n\nfragment FlussSliderAssignWidget on SliderAssignWidget {\n  __typename\n  kind\n  min\n  max\n}\n\nfragment FlussStringAssignWidget on StringAssignWidget {\n  __typename\n  kind\n  placeholder\n  asParagraph\n}\n\nfragment FlussEffectDependency on EffectDependency {\n  key\n  condition\n  value\n}\n\nfragment FlussCustomEffect on CustomEffect {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment Validator on Validator {\n  function\n  dependencies\n}\n\nfragment FlussChildPort on ChildPort {\n  __typename\n  kind\n  identifier\n  scope\n  children {\n    ...FlussChildPortNested\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  nullable\n}\n\nfragment FlussPortEffect on Effect {\n  __typename\n  kind\n  dependencies {\n    ...FlussEffectDependency\n  }\n  ...FlussCustomEffect\n  ...FlussMessageEffect\n}\n\nfragment FlussReturnWidget on ReturnWidget {\n  __typename\n  kind\n  ...FlussCustomReturnWidget\n  ...FlussChoiceReturnWidget\n}\n\nfragment FlussAssignWidget on AssignWidget {\n  __typename\n  kind\n  ...FlussStringAssignWidget\n  ...FlussSearchAssignWidget\n  ...FlussSliderAssignWidget\n  ...FlussChoiceAssignWidget\n  ...FlussCustomAssignWidget\n}\n\nfragment FlussPort on Port {\n  __typename\n  key\n  label\n  nullable\n  description\n  scope\n  effects {\n    ...FlussPortEffect\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  kind\n  identifier\n  children {\n    ...FlussChildPort\n  }\n  default\n  nullable\n  groups\n  validators {\n    ...Validator\n  }\n}\n\nfragment ReactiveTemplate on ReactiveTemplate {\n  id\n  ins {\n    ...FlussPort\n  }\n  outs {\n    ...FlussPort\n  }\n  constants {\n    ...FlussPort\n  }\n  implementation\n  title\n  description\n}\n\nquery ReactiveTemplates($pagination: OffsetPaginationInput) {\n  reactiveTemplates(pagination: $pagination) {\n    ...ReactiveTemplate\n  }\n}"


class ReactiveTemplateQuery(BaseModel):
    reactive_template: ReactiveTemplateFragment = Field(alias="reactiveTemplate")

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment FlussChoiceReturnWidget on ChoiceReturnWidget {\n  __typename\n  choices {\n    label\n    value\n    description\n  }\n}\n\nfragment FlussCustomReturnWidget on CustomReturnWidget {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussMessageEffect on MessageEffect {\n  __typename\n  kind\n  message\n}\n\nfragment FlussChoiceAssignWidget on ChoiceAssignWidget {\n  __typename\n  kind\n  choices {\n    value\n    label\n    description\n  }\n}\n\nfragment FlussCustomAssignWidget on CustomAssignWidget {\n  __typename\n  ward\n  hook\n}\n\nfragment FlussSearchAssignWidget on SearchAssignWidget {\n  __typename\n  kind\n  query\n  ward\n}\n\nfragment FlussChildPortNested on ChildPort {\n  __typename\n  kind\n  identifier\n  children {\n    kind\n    identifier\n    scope\n    assignWidget {\n      ...FlussAssignWidget\n    }\n    returnWidget {\n      ...FlussReturnWidget\n    }\n  }\n  scope\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n}\n\nfragment FlussSliderAssignWidget on SliderAssignWidget {\n  __typename\n  kind\n  min\n  max\n}\n\nfragment FlussStringAssignWidget on StringAssignWidget {\n  __typename\n  kind\n  placeholder\n  asParagraph\n}\n\nfragment FlussEffectDependency on EffectDependency {\n  key\n  condition\n  value\n}\n\nfragment FlussCustomEffect on CustomEffect {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment Validator on Validator {\n  function\n  dependencies\n}\n\nfragment FlussChildPort on ChildPort {\n  __typename\n  kind\n  identifier\n  scope\n  children {\n    ...FlussChildPortNested\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  nullable\n}\n\nfragment FlussPortEffect on Effect {\n  __typename\n  kind\n  dependencies {\n    ...FlussEffectDependency\n  }\n  ...FlussCustomEffect\n  ...FlussMessageEffect\n}\n\nfragment FlussReturnWidget on ReturnWidget {\n  __typename\n  kind\n  ...FlussCustomReturnWidget\n  ...FlussChoiceReturnWidget\n}\n\nfragment FlussAssignWidget on AssignWidget {\n  __typename\n  kind\n  ...FlussStringAssignWidget\n  ...FlussSearchAssignWidget\n  ...FlussSliderAssignWidget\n  ...FlussChoiceAssignWidget\n  ...FlussCustomAssignWidget\n}\n\nfragment FlussPort on Port {\n  __typename\n  key\n  label\n  nullable\n  description\n  scope\n  effects {\n    ...FlussPortEffect\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  kind\n  identifier\n  children {\n    ...FlussChildPort\n  }\n  default\n  nullable\n  groups\n  validators {\n    ...Validator\n  }\n}\n\nfragment ReactiveTemplate on ReactiveTemplate {\n  id\n  ins {\n    ...FlussPort\n  }\n  outs {\n    ...FlussPort\n  }\n  constants {\n    ...FlussPort\n  }\n  implementation\n  title\n  description\n}\n\nquery ReactiveTemplate($id: ID!) {\n  reactiveTemplate(id: $id) {\n    ...ReactiveTemplate\n  }\n}"


class GetFlowQuery(BaseModel):
    flow: FlowFragment

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment StreamItem on StreamItem {\n  kind\n  label\n}\n\nfragment FlussChildPortNested on ChildPort {\n  __typename\n  kind\n  identifier\n  children {\n    kind\n    identifier\n    scope\n    assignWidget {\n      ...FlussAssignWidget\n    }\n    returnWidget {\n      ...FlussReturnWidget\n    }\n  }\n  scope\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n}\n\nfragment FlussSliderAssignWidget on SliderAssignWidget {\n  __typename\n  kind\n  min\n  max\n}\n\nfragment FlussChoiceReturnWidget on ChoiceReturnWidget {\n  __typename\n  choices {\n    label\n    value\n    description\n  }\n}\n\nfragment FlussMessageEffect on MessageEffect {\n  __typename\n  kind\n  message\n}\n\nfragment FlussSearchAssignWidget on SearchAssignWidget {\n  __typename\n  kind\n  query\n  ward\n}\n\nfragment FlussEffectDependency on EffectDependency {\n  key\n  condition\n  value\n}\n\nfragment FlussChoiceAssignWidget on ChoiceAssignWidget {\n  __typename\n  kind\n  choices {\n    value\n    label\n    description\n  }\n}\n\nfragment FlussCustomEffect on CustomEffect {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomReturnWidget on CustomReturnWidget {\n  __typename\n  kind\n  hook\n  ward\n}\n\nfragment FlussCustomAssignWidget on CustomAssignWidget {\n  __typename\n  ward\n  hook\n}\n\nfragment FlussStringAssignWidget on StringAssignWidget {\n  __typename\n  kind\n  placeholder\n  asParagraph\n}\n\nfragment FlussBinds on Binds {\n  templates\n}\n\nfragment RekuestNode on RekuestNode {\n  hash\n  mapStrategy\n  allowLocalExecution\n  binds {\n    ...FlussBinds\n  }\n  nodeKind\n}\n\nfragment FlussChildPort on ChildPort {\n  __typename\n  kind\n  identifier\n  scope\n  children {\n    ...FlussChildPortNested\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  nullable\n}\n\nfragment FlussPortEffect on Effect {\n  __typename\n  kind\n  dependencies {\n    ...FlussEffectDependency\n  }\n  ...FlussCustomEffect\n  ...FlussMessageEffect\n}\n\nfragment FlussAssignWidget on AssignWidget {\n  __typename\n  kind\n  ...FlussStringAssignWidget\n  ...FlussSearchAssignWidget\n  ...FlussSliderAssignWidget\n  ...FlussChoiceAssignWidget\n  ...FlussCustomAssignWidget\n}\n\nfragment Validator on Validator {\n  function\n  dependencies\n}\n\nfragment RetriableNode on RetriableNode {\n  retries\n  retryDelay\n}\n\nfragment AssignableNode on AssignableNode {\n  nextTimeout\n}\n\nfragment BaseGraphNode on GraphNode {\n  __typename\n  ins {\n    ...FlussPort\n  }\n  outs {\n    ...FlussPort\n  }\n  constants {\n    ...FlussPort\n  }\n  voids {\n    ...FlussPort\n  }\n  globalsMap\n  constantsMap\n  title\n  description\n  kind\n}\n\nfragment BaseGraphEdge on GraphEdge {\n  __typename\n  id\n  source\n  sourceHandle\n  target\n  targetHandle\n  kind\n  stream {\n    ...StreamItem\n  }\n}\n\nfragment FlussReturnWidget on ReturnWidget {\n  __typename\n  kind\n  ...FlussCustomReturnWidget\n  ...FlussChoiceReturnWidget\n}\n\nfragment RekuestMapNode on RekuestMapNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  hello\n}\n\nfragment ReactiveNode on ReactiveNode {\n  ...BaseGraphNode\n  __typename\n  implementation\n}\n\nfragment VanillaEdge on VanillaEdge {\n  ...BaseGraphEdge\n  label\n}\n\nfragment LoggingEdge on LoggingEdge {\n  ...BaseGraphEdge\n  level\n}\n\nfragment FlussPort on Port {\n  __typename\n  key\n  label\n  nullable\n  description\n  scope\n  effects {\n    ...FlussPortEffect\n  }\n  assignWidget {\n    ...FlussAssignWidget\n  }\n  returnWidget {\n    ...FlussReturnWidget\n  }\n  kind\n  identifier\n  children {\n    ...FlussChildPort\n  }\n  default\n  nullable\n  groups\n  validators {\n    ...Validator\n  }\n}\n\nfragment ArgNode on ArgNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment ReturnNode on ReturnNode {\n  ...BaseGraphNode\n  __typename\n}\n\nfragment RekuestFilterNode on RekuestFilterNode {\n  ...BaseGraphNode\n  ...RetriableNode\n  ...AssignableNode\n  ...RekuestNode\n  __typename\n  path\n}\n\nfragment GlobalArg on GlobalArg {\n  key\n  port {\n    ...FlussPort\n  }\n}\n\nfragment GraphEdge on GraphEdge {\n  __typename\n  id\n  ...LoggingEdge\n  ...VanillaEdge\n}\n\nfragment GraphNode on GraphNode {\n  __typename\n  id\n  position {\n    x\n    y\n  }\n  parentNode\n  ...RekuestFilterNode\n  ...RekuestMapNode\n  ...ReactiveNode\n  ...ArgNode\n  ...ReturnNode\n}\n\nfragment Graph on Graph {\n  nodes {\n    ...GraphNode\n  }\n  edges {\n    ...GraphEdge\n  }\n  globals {\n    ...GlobalArg\n  }\n}\n\nfragment Flow on Flow {\n  __typename\n  id\n  graph {\n    ...Graph\n  }\n  title\n  description\n  createdAt\n  workspace {\n    id\n  }\n}\n\nquery GetFlow($id: ID!) {\n  flow(id: $id) {\n    ...Flow\n  }\n}"


class FlowsQuery(BaseModel):
    flows: Tuple[ListFlowFragment, ...]

    class Arguments(BaseModel):
        limit: Optional[int] = Field(default=None)

    class Meta:
        document = "fragment ListFlow on Flow {\n  id\n  title\n  createdAt\n  workspace {\n    id\n  }\n}\n\nquery Flows($limit: Int) {\n  flows(pagination: {limit: $limit}) {\n    ...ListFlow\n  }\n}"


class SearchFlowsQueryOptions(BaseModel):
    """Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)"""

    typename: Optional[Literal["Flow"]] = Field(
        alias="__typename", default="Flow", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchFlowsQuery(BaseModel):
    options: Tuple[SearchFlowsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchFlows($search: String, $values: [ID!]) {\n  options: flows(filters: {search: $search, ids: $values}) {\n    value: id\n    label: title\n  }\n}"


async def acreate_run(
    assignation: ID, flow: ID, snapshot_interval: int, rath: Optional[FlussRath] = None
) -> CreateRunMutationCreaterun:
    """CreateRun

     Start a run on fluss

    Arguments:
        assignation (ID): assignation
        flow (ID): flow
        snapshot_interval (int): snapshot_interval
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        CreateRunMutationCreaterun"""
    return (
        await aexecute(
            CreateRunMutation,
            {
                "assignation": assignation,
                "flow": flow,
                "snapshot_interval": snapshot_interval,
            },
            rath=rath,
        )
    ).create_run


def create_run(
    assignation: ID, flow: ID, snapshot_interval: int, rath: Optional[FlussRath] = None
) -> CreateRunMutationCreaterun:
    """CreateRun

     Start a run on fluss

    Arguments:
        assignation (ID): assignation
        flow (ID): flow
        snapshot_interval (int): snapshot_interval
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        CreateRunMutationCreaterun"""
    return execute(
        CreateRunMutation,
        {
            "assignation": assignation,
            "flow": flow,
            "snapshot_interval": snapshot_interval,
        },
        rath=rath,
    ).create_run


async def aclose_run(
    run: ID, rath: Optional[FlussRath] = None
) -> CloseRunMutationCloserun:
    """CloseRun

     Start a run on fluss

    Arguments:
        run (ID): run
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        CloseRunMutationCloserun"""
    return (await aexecute(CloseRunMutation, {"run": run}, rath=rath)).close_run


def close_run(run: ID, rath: Optional[FlussRath] = None) -> CloseRunMutationCloserun:
    """CloseRun

     Start a run on fluss

    Arguments:
        run (ID): run
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        CloseRunMutationCloserun"""
    return execute(CloseRunMutation, {"run": run}, rath=rath).close_run


async def asnapshot(
    run: ID, events: List[ID], t: int, rath: Optional[FlussRath] = None
) -> SnapshotMutationSnapshot:
    """Snapshot

     Snapshot the current state on the fluss platform

    Arguments:
        run (ID): run
        events (List[ID]): events
        t (int): t
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        SnapshotMutationSnapshot"""
    return (
        await aexecute(
            SnapshotMutation, {"run": run, "events": events, "t": t}, rath=rath
        )
    ).snapshot


def snapshot(
    run: ID, events: List[ID], t: int, rath: Optional[FlussRath] = None
) -> SnapshotMutationSnapshot:
    """Snapshot

     Snapshot the current state on the fluss platform

    Arguments:
        run (ID): run
        events (List[ID]): events
        t (int): t
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        SnapshotMutationSnapshot"""
    return execute(
        SnapshotMutation, {"run": run, "events": events, "t": t}, rath=rath
    ).snapshot


async def atrack(
    reference: str,
    run: ID,
    t: int,
    caused_by: List[ID],
    kind: RunEventKind,
    source: str,
    handle: str,
    value: Optional[EventValue] = None,
    exception: Optional[str] = None,
    message: Optional[str] = None,
    rath: Optional[FlussRath] = None,
) -> TrackMutationTrack:
    """Track

     Track a new event on the fluss platform

    Arguments:
        reference (str): reference
        run (ID): run
        t (int): t
        caused_by (List[ID]): caused_by
        kind (RunEventKind): kind
        source (str): source
        handle (str): handle
        value (Optional[EventValue], optional): value.
        exception (Optional[str], optional): exception.
        message (Optional[str], optional): message.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        TrackMutationTrack"""
    return (
        await aexecute(
            TrackMutation,
            {
                "reference": reference,
                "run": run,
                "t": t,
                "caused_by": caused_by,
                "kind": kind,
                "value": value,
                "exception": exception,
                "message": message,
                "source": source,
                "handle": handle,
            },
            rath=rath,
        )
    ).track


def track(
    reference: str,
    run: ID,
    t: int,
    caused_by: List[ID],
    kind: RunEventKind,
    source: str,
    handle: str,
    value: Optional[EventValue] = None,
    exception: Optional[str] = None,
    message: Optional[str] = None,
    rath: Optional[FlussRath] = None,
) -> TrackMutationTrack:
    """Track

     Track a new event on the fluss platform

    Arguments:
        reference (str): reference
        run (ID): run
        t (int): t
        caused_by (List[ID]): caused_by
        kind (RunEventKind): kind
        source (str): source
        handle (str): handle
        value (Optional[EventValue], optional): value.
        exception (Optional[str], optional): exception.
        message (Optional[str], optional): message.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        TrackMutationTrack"""
    return execute(
        TrackMutation,
        {
            "reference": reference,
            "run": run,
            "t": t,
            "caused_by": caused_by,
            "kind": kind,
            "value": value,
            "exception": exception,
            "message": message,
            "source": source,
            "handle": handle,
        },
        rath=rath,
    ).track


async def aupdate_workspace(
    id: ID, graph: GraphInput, rath: Optional[FlussRath] = None
) -> WorkspaceFragment:
    """UpdateWorkspace


     updateWorkspace: Graph is a Template for a Template


    Arguments:
        id (ID): id
        graph (GraphInput): graph
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        WorkspaceFragment"""
    return (
        await aexecute(UpdateWorkspaceMutation, {"id": id, "graph": graph}, rath=rath)
    ).update_workspace


def update_workspace(
    id: ID, graph: GraphInput, rath: Optional[FlussRath] = None
) -> WorkspaceFragment:
    """UpdateWorkspace


     updateWorkspace: Graph is a Template for a Template


    Arguments:
        id (ID): id
        graph (GraphInput): graph
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        WorkspaceFragment"""
    return execute(
        UpdateWorkspaceMutation, {"id": id, "graph": graph}, rath=rath
    ).update_workspace


async def acreate_workspace(
    name: Optional[str] = None, rath: Optional[FlussRath] = None
) -> WorkspaceFragment:
    """CreateWorkspace


     createWorkspace: Graph is a Template for a Template


    Arguments:
        name (Optional[str], optional): name.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        WorkspaceFragment"""
    return (
        await aexecute(CreateWorkspaceMutation, {"name": name}, rath=rath)
    ).create_workspace


def create_workspace(
    name: Optional[str] = None, rath: Optional[FlussRath] = None
) -> WorkspaceFragment:
    """CreateWorkspace


     createWorkspace: Graph is a Template for a Template


    Arguments:
        name (Optional[str], optional): name.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        WorkspaceFragment"""
    return execute(CreateWorkspaceMutation, {"name": name}, rath=rath).create_workspace


async def arun(id: ID, rath: Optional[FlussRath] = None) -> RunFragment:
    """Run


     run: Run(id, created_at, flow, assignation, status, snapshot_interval)


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        RunFragment"""
    return (await aexecute(RunQuery, {"id": id}, rath=rath)).run


def run(id: ID, rath: Optional[FlussRath] = None) -> RunFragment:
    """Run


     run: Run(id, created_at, flow, assignation, status, snapshot_interval)


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        RunFragment"""
    return execute(RunQuery, {"id": id}, rath=rath).run


async def asearch_runs(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[FlussRath] = None,
) -> List[SearchRunsQueryOptions]:
    """SearchRuns


     options: Run(id, created_at, flow, assignation, status, snapshot_interval)


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchRunsQueryRuns]"""
    return (
        await aexecute(SearchRunsQuery, {"search": search, "values": values}, rath=rath)
    ).options


def search_runs(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[FlussRath] = None,
) -> List[SearchRunsQueryOptions]:
    """SearchRuns


     options: Run(id, created_at, flow, assignation, status, snapshot_interval)


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchRunsQueryRuns]"""
    return execute(
        SearchRunsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aworkspace(id: ID, rath: Optional[FlussRath] = None) -> WorkspaceFragment:
    """Workspace


     workspace: Graph is a Template for a Template


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        WorkspaceFragment"""
    return (await aexecute(WorkspaceQuery, {"id": id}, rath=rath)).workspace


def workspace(id: ID, rath: Optional[FlussRath] = None) -> WorkspaceFragment:
    """Workspace


     workspace: Graph is a Template for a Template


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        WorkspaceFragment"""
    return execute(WorkspaceQuery, {"id": id}, rath=rath).workspace


async def aworkspaces(
    pagination: Optional[OffsetPaginationInput] = None, rath: Optional[FlussRath] = None
) -> List[ListWorkspaceFragment]:
    """Workspaces


     workspaces: Graph is a Template for a Template


    Arguments:
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListWorkspaceFragment]"""
    return (
        await aexecute(WorkspacesQuery, {"pagination": pagination}, rath=rath)
    ).workspaces


def workspaces(
    pagination: Optional[OffsetPaginationInput] = None, rath: Optional[FlussRath] = None
) -> List[ListWorkspaceFragment]:
    """Workspaces


     workspaces: Graph is a Template for a Template


    Arguments:
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListWorkspaceFragment]"""
    return execute(WorkspacesQuery, {"pagination": pagination}, rath=rath).workspaces


async def areactive_templates(
    pagination: Optional[OffsetPaginationInput] = None, rath: Optional[FlussRath] = None
) -> List[ReactiveTemplateFragment]:
    """ReactiveTemplates


     reactiveTemplates: ReactiveTemplate(id, title, description, implementation, ins, outs, voids, constants)


    Arguments:
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ReactiveTemplateFragment]"""
    return (
        await aexecute(ReactiveTemplatesQuery, {"pagination": pagination}, rath=rath)
    ).reactive_templates


def reactive_templates(
    pagination: Optional[OffsetPaginationInput] = None, rath: Optional[FlussRath] = None
) -> List[ReactiveTemplateFragment]:
    """ReactiveTemplates


     reactiveTemplates: ReactiveTemplate(id, title, description, implementation, ins, outs, voids, constants)


    Arguments:
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ReactiveTemplateFragment]"""
    return execute(
        ReactiveTemplatesQuery, {"pagination": pagination}, rath=rath
    ).reactive_templates


async def areactive_template(
    id: ID, rath: Optional[FlussRath] = None
) -> ReactiveTemplateFragment:
    """ReactiveTemplate


     reactiveTemplate: ReactiveTemplate(id, title, description, implementation, ins, outs, voids, constants)


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        ReactiveTemplateFragment"""
    return (
        await aexecute(ReactiveTemplateQuery, {"id": id}, rath=rath)
    ).reactive_template


def reactive_template(
    id: ID, rath: Optional[FlussRath] = None
) -> ReactiveTemplateFragment:
    """ReactiveTemplate


     reactiveTemplate: ReactiveTemplate(id, title, description, implementation, ins, outs, voids, constants)


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        ReactiveTemplateFragment"""
    return execute(ReactiveTemplateQuery, {"id": id}, rath=rath).reactive_template


async def aget_flow(id: ID, rath: Optional[FlussRath] = None) -> FlowFragment:
    """GetFlow


     flow: Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        FlowFragment"""
    return (await aexecute(GetFlowQuery, {"id": id}, rath=rath)).flow


def get_flow(id: ID, rath: Optional[FlussRath] = None) -> FlowFragment:
    """GetFlow


     flow: Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)


    Arguments:
        id (ID): id
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        FlowFragment"""
    return execute(GetFlowQuery, {"id": id}, rath=rath).flow


async def aflows(
    limit: Optional[int] = None, rath: Optional[FlussRath] = None
) -> List[ListFlowFragment]:
    """Flows


     flows: Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)


    Arguments:
        limit (Optional[int], optional): limit.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListFlowFragment]"""
    return (await aexecute(FlowsQuery, {"limit": limit}, rath=rath)).flows


def flows(
    limit: Optional[int] = None, rath: Optional[FlussRath] = None
) -> List[ListFlowFragment]:
    """Flows


     flows: Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)


    Arguments:
        limit (Optional[int], optional): limit.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListFlowFragment]"""
    return execute(FlowsQuery, {"limit": limit}, rath=rath).flows


async def asearch_flows(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[FlussRath] = None,
) -> List[SearchFlowsQueryOptions]:
    """SearchFlows


     options: Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchFlowsQueryFlows]"""
    return (
        await aexecute(
            SearchFlowsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_flows(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[FlussRath] = None,
) -> List[SearchFlowsQueryOptions]:
    """SearchFlows


     options: Flow(id, created_at, workspace, creator, restrict, version, title, nodes, edges, graph, hash, description, brittle)


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (fluss_next.rath.FlussRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchFlowsQueryFlows]"""
    return execute(
        SearchFlowsQuery, {"search": search, "values": values}, rath=rath
    ).options


AssignWidgetInput.model_rebuild()
ChildPortInput.model_rebuild()
EffectInput.model_rebuild()
FlussChildPortFragment.model_rebuild()
FlussChildPortNestedFragment.model_rebuild()
FlussChildPortNestedFragmentChildren.model_rebuild()
FlussPortFragment.model_rebuild()
GraphEdgeInput.model_rebuild()
GraphInput.model_rebuild()
GraphNodeInput.model_rebuild()
ListWorkspaceFragment.model_rebuild()
PortInput.model_rebuild()
WorkspaceFragment.model_rebuild()
