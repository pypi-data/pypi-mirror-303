import abc
import uuid
from typing import List, Union, get_args

import networkx as nx
from loguru import logger
from pydantic import BaseModel, EmailStr, Field
from pydantic_core import ValidationError

from plurally.json_utils import load_from_json_dict
from plurally.models.env_vars import BaseEnvVars

TYPE_ADAPTER = {
    EmailStr: str,
}


class Edge(BaseModel):
    src_node_id: str
    tgt_node_id: str
    src_handle: str
    tgt_handle: str


def get_inner_type(field_type):
    # If output_type is a Union, extract all possible types
    # check if field_type is a List
    if hasattr(field_type, "__origin__") and field_type.__origin__ is Union:
        return [get_inner_type(allowed_type) for allowed_type in get_args(field_type)]

    try:
        # Otherwise, simply check if input_type is a subclass of output_type
        if hasattr(field_type, "__origin__") and field_type.__origin__ is list:
            return field_type.__args__[0]
        else:
            return field_type
    except Exception as e:
        raise ValueError(
            f"Could not get inner type: {field_type=}, {field_type.__args__=}"
        ) from e


def is_type_compatible(input_field, output_field):
    # If output_type is a Union, extract all possible types
    input_type = TYPE_ADAPTER.get(input_field.annotation, input_field.annotation)
    output_type = get_inner_type(
        TYPE_ADAPTER.get(output_field.annotation, output_field.annotation)
    )
    # check if output_type is a List
    if isinstance(output_type, list):
        return any(issubclass(input_type, allowed_type) for allowed_type in output_type)

    try:
        return issubclass(input_type, output_type)
    except Exception as e:
        raise ValueError(
            f"Error checking type compatibility: {input_type=}, {output_type=}"
        ) from e


class SchemaWithPrivate(BaseModel):

    @classmethod
    def model_json_schema(cls, **kwargs):
        schema = super().model_json_schema(**kwargs)
        # Filter out fields ending with "_"
        properties = schema.get("properties", {})
        schema["properties"] = {
            key: value for key, value in properties.items() if not key.endswith("_")
        }
        return schema


class Node(abc.ABC):
    class InputSchema(SchemaWithPrivate):
        run: bool = Field(
            True,
            title="Run",
            description="Whether to run the block.",
            examples=[True, False],
        )

    class OutputSchema(SchemaWithPrivate): ...

    IS_DEPRECATED = False
    EnvVars: BaseEnvVars = None
    SensitiveFields = tuple()
    DESC = ""
    SCOPES: List[str] = None
    IS_TRIGGER = False
    STATES = tuple()
    ICON: str = ""
    PLURALLY_VERSION: int = 0

    class InitSchema(BaseModel):
        name: str = Field(
            title="Block Name",
            description="Name of the block.",
            examples=["Block 1"],
            min_length=1,
            max_length=35,
        )
        pos_x: float = 0
        pos_y: float = 0
        src_handles: List[str] | None = Field(None)
        tgt_handles: List[str] | None = Field(None)

        @classmethod
        def get_overrideable_fields(cls):
            return []

    def _get_handles(self, schema, in_handles):
        out_handles = set(
            handle for handle in schema.model_fields if not handle.endswith("_")
        )

        if self.is_trigger:
            out_handles = out_handles - {"run"}
        if in_handles is not None:
            out_handles &= set(in_handles)
        return list(out_handles)

    def __init__(self, init_inputs: InitSchema, outputs=None):
        self._node_id = f"nd-{str(uuid.uuid4())}"
        self.name = init_inputs.name
        self.outputs = outputs or {}
        self._set_schemas()
        self._check_schemas()

        self._pos_x = init_inputs.pos_x
        self._pos_y = init_inputs.pos_y

        self.tgt_handles = self._get_handles(self.InputSchema, init_inputs.tgt_handles)
        self.src_handles = self._get_handles(self.OutputSchema, init_inputs.src_handles)

        self.has_run_successfully = False

    def early_stop_if_needed(self, graph: nx.MultiDiGraph):
        return False

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x = value

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = value

    @property
    def is_trigger(self):
        return self.IS_TRIGGER

    def callback(self):
        self.has_run_successfully = False

    def _check_schemas(self):
        if self.InputSchema is None or not issubclass(self.InputSchema, BaseModel):
            raise ValueError(f"{type(self).__name__} must have an InputSchema")
        if self.OutputSchema is None or not issubclass(self.OutputSchema, BaseModel):
            raise ValueError(f"{type(self).__name__} must have an OutputSchema")

    def _set_schemas(self): ...

    @property
    def node_id(self):
        return self._node_id

    def validate_connection(
        self, src_node: "Node", output_node_id: str, input_node_id: str
    ):
        output_node_schema = src_node.OutputSchema.model_fields.get(output_node_id)
        input_node_schema = self.InputSchema.model_fields.get(input_node_id)

        if output_node_schema is None or input_node_schema is None:
            return True
        return is_type_compatible(output_node_schema, input_node_schema)

    def validate_inputs(self, **kwargs):
        try:
            return self.InputSchema(**kwargs)
        except ValidationError as e:
            raise ValueError(f"Invalid inputs for {self}, got={kwargs}") from e

    def __call__(self, **kwargs):
        """Override this method in child classes to define logic."""
        node_input = self.validate_inputs(**kwargs)
        self.forward(node_input)
        self.has_run_successfully = True

    def get_necessary_env_vars(self) -> List[str]:
        if self.EnvVars:
            return list(self.EnvVars.model_fields.keys())
        return []

    def forward(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Node) and other.node_id == self.node_id

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, node_id={self.node_id[:7]})"

    def __hash__(self) -> int:
        return hash(self.node_id)

    def _state(self):
        return {}

    def state(self):
        state = self._state()
        assert set(state) == set(self.STATES), f"{state=} not in {self.STATES=}"
        return state

    def update_state(self, state_update):
        if state_update:
            for key, value in state_update.items():
                assert hasattr(self, key), f"Node {self} does not have attribute {key}"
                assert key in self.STATES
                setattr(self, key, value)

    def serialize(self):
        # outputs_to_serialize = None
        # if self.outputs is not None:
        #     outputs_to_serialize = {**self.outputs}
        #     for k, v in outputs_to_serialize.items():
        #         if isinstance(v, datetime):
        #             outputs_to_serialize[k] = v.isoformat()

        return {
            "PLURALLY_VERSION": self.PLURALLY_VERSION,
            "kls": type(self).__name__,
            "name": self.name,
            "_node_id": self._node_id,
            "pos_x": self.pos_x,
            "pos_y": self.pos_y,
            "is_trigger": self.is_trigger,
            # "outputs": outputs_to_serialize,
            "src_handles": self.src_handles,
            "tgt_handles": self.tgt_handles,
        }

    @classmethod
    def _parse(cls, **kwargs):
        kwargs = load_from_json_dict(kwargs)
        return cls(cls.InitSchema(**kwargs))

    def get_issues(self, graph):
        return []

    @classmethod
    def adapt_version(cls, node_ids: List[str], flow_serialization_data: dict):
        raise NotImplementedError(f"Subclasses must implement this method {cls}")

    @classmethod
    def parse(cls, **kwargs):
        _node_id = kwargs.pop("_node_id")
        # outputs = kwargs.pop("outputs")
        try:
            obj = cls._parse(**kwargs)
        except Exception as e:
            logger.error(f"Error parsing {cls.__name__} with {kwargs=}")
            raise e
        obj._node_id = _node_id
        obj.pos_x = kwargs.get("pos_x", 0)
        obj.pos_y = kwargs.get("pos_y", 0)

        # if outputs is not None:
        #     for k, v in outputs.items():
        #         if isinstance(v, datetime):
        #             outputs[k] = v.fromisoformat(v)

        # obj.outputs = outputs
        return obj

    def get_scopes_and_meta_data(self):
        return [(self.SCOPES, {})]

    def add_target_handle(self, src_handle: str) -> str:
        raise NotImplementedError(f"Subclasses must implement this method {self}")
