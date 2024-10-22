import os
from enum import Enum
from typing import Any, Dict, List

from loguru import logger
from pydantic import ConfigDict, Field, create_model, model_validator

from plurally.json_utils import load_from_json_dict, replace_refs
from plurally.models.env_vars import BaseEnvVars, OpenAiApiKey
from plurally.models.fields import NameableHandle, get_nameable_fields
from plurally.models.misc import Table
from plurally.models.node import Node


class InstructModel(str, Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4_TURBO = "gpt-4-turbo"


InstructField = Field(
    title="Instructions",
    description="Instructions for the AI model.",
    examples=[
        "Write a response to the incoming email (given by question_asked, person_asking_name), you should output a body and a subject."
    ],
    help="It is best to mention the inputs and outputs in the instructions, e.g. 'Write a response to the incoming email (given by question_asked, person_asking_name), you should output a body and a subject.'",
    min_length=1,
    json_schema_extra={
        "uiSchema": {
            "ui:widget": "textarea",
            "ui:placeholder": "Write instructions here. Example: Write a response to the incoming email (given by question_asked, person_asking_name), you should output a body and a subject.",
        }
    },
)


class Instruct(Node):
    ICON = "openai"
    PLURALLY_VERSION = 1

    class OutputSchema(Node.OutputSchema):
        key_vals: Dict[str, str]

    class EnvVars(BaseEnvVars):
        OPENAI_API_KEY: str = OpenAiApiKey

    class InputSchema(Node.InputSchema):
        model_config = ConfigDict(json_schema_extra={"can-add-fields": True})

    class InitSchema(Node.InitSchema):

        model: InstructModel = Field(
            InstructModel.GPT_4O_MINI,
            title="Model",
            description="The OpenAI model to use.",
            examples=[InstructModel.GPT_4O_MINI.value],
            json_schema_extra={"advanced": True},
        )
        is_table: bool = Field(
            False,
            title="Table Output",
            description="Whether the output is a table. For instance, if you want ChatGPT to output a list of outputs with the same columns, you should tick this.",
            examples=[True, False],
            json_schema_extra={"advanced": True},
        )

        input_fields: List[NameableHandle] = get_nameable_fields(
            title="Inputs",
            description="The different inputs of the AI model. For instance if you want to write an automatic support email, your inputs might be: like 'Question asked', 'Name of person asking'. Be sure to mention them in your instructions (see examples).",
            examples=["Question asked", "Name of person asking"],
            placeholder="Enter input name, example: Question asked",
            default_factory=list,
            json_schema_extra_extra={"is_input": True},
        )
        instruct: str = InstructField
        output_fields: List[NameableHandle] = get_nameable_fields(
            title="Outputs",
            description="The different output attributes of the AI model. For instance if you want to write a support email, your outputs might be: like 'Email subject' and 'Email body'. Be sure to mention them in your instructions (see examples).",
            min_length=1,
            examples=["Email Subject", "Email Body"],
            placeholder="Enter output name, example: Email Subject",
            json_schema_extra_extra={"is_output": True},
        )

        @model_validator(mode="after")
        def ckeck_model(cls, values):
            if len(set(field._clean for field in values.input_fields)) != len(
                values.input_fields
            ):
                raise ValueError("Input fields must be unique")
            if len(set(field._clean for field in values.output_fields)) != len(
                values.output_fields
            ):
                raise ValueError("Output fields must be unique")
            return values

    InitSchema.__doc__ = """Instruct an AI model to perform a task."""
    DESC = InitSchema.__doc__

    def __init__(
        self,
        init_inputs: InitSchema,
    ) -> None:
        self.is_table = init_inputs.is_table
        self._client = None  # lazy init
        self.model = init_inputs.model
        self.instruct = init_inputs.instruct

        self._input_fields = init_inputs.input_fields
        self._output_fields = init_inputs.output_fields

        super().__init__(init_inputs)

    def build_messages(self, node_input: InputSchema) -> List[Dict[str, str]]:
        prompt = self.instruct + "\n"
        for input_field in self.input_fields:
            prompt += f"""
#### Beginning of {input_field.free} ####
{getattr(node_input, input_field._clean)}
#### End of {input_field.free} ####

"""
        return [
            # {"role": "assistant", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]

    def _set_schemas(self) -> None:
        # create pydantic model from output_fields
        out_fields_map = {}
        for field in self.output_fields:
            out_fields_map[field._clean] = (
                str,
                Field(
                    ...,
                    title=field.free,
                    json_schema_extra={"handle_id": field.handle_id},
                ),
            )
        self.instruct_schema = create_model("OutputSchema", **out_fields_map)

        if self.is_table:
            self.instruct_schema = List[self.instruct_schema]

            class OutputSchema(Node.OutputSchema):
                data: Table = Field(
                    description=f"The ouputs converted to a table, columns are the output fields: {[o._clean for o in self.output_fields]}.",
                )

            self.OutputSchema = OutputSchema

        else:
            self.OutputSchema = self.instruct_schema

        # create pydantic model from input_fields
        in_fields_map = {}
        for field in self.input_fields:
            in_fields_map[field._clean] = (
                str,
                Field(
                    ...,
                    title=field.free,
                    json_schema_extra={"handle_id": field.handle_id},
                ),
            )
        self.InputSchema = create_model(
            "InputSchema",
            **in_fields_map,
            __base__=Instruct.InputSchema,
        )
        assert self.InputSchema.model_json_schema()["can-add-fields"]

    @property
    def output_fields(self):
        return self._output_fields

    @output_fields.setter
    def output_fields(self, value):
        value = [
            v if isinstance(v, NameableHandle) else NameableHandle(**v) for v in value
        ]
        assert len(set(field._clean for field in value)) == len(
            value
        ), f"Output fields must be unique {value}"
        self._output_fields = value
        self._set_schemas()
        self.src_handles = self._get_handles(self.OutputSchema, None)

    @property
    def input_fields(self):
        return self._input_fields

    @input_fields.setter
    def input_fields(self, value):
        value = [
            v if isinstance(v, NameableHandle) else NameableHandle(**v) for v in value
        ]
        assert len(set(field._clean for field in value)) == len(
            value
        ), f"Input fields must be unique {value}"
        self._input_fields = value
        self._set_schemas()
        self.tgt_handles = self._get_handles(self.InputSchema, None)

    @property
    def client(self):
        global instructor
        import instructor

        global OpenAI
        from openai import OpenAI

        if self._client is None:
            self._client = instructor.from_openai(OpenAI())
        return self._client

    def create(self, messages: List[Dict[str, str]]) -> Any:
        model_override = os.environ.get("OPENAI_MODEL")
        model = self.model
        if model_override:
            logger.info(f"Found override for OPENAI_MODEL: {model_override}, using it.")
            model = model_override

        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            response_model=self.instruct_schema,
        )

    def forward(self, node_input) -> Any:
        messages = self.build_messages(node_input)

        output: self.OutputSchema = self.create(messages)

        if self.is_table:
            self.outputs["data"] = Table(data=[o.model_dump() for o in output])
        else:
            self.outputs = output.model_dump()

    def serialize(self) -> dict:
        return {
            **super().serialize(),
            "instruct": self.instruct,
            "output_fields": [o.model_dump() for o in self.output_fields],
            "input_fields": [i.model_dump() for i in self.input_fields],
            "output_schema": replace_refs(self.OutputSchema.model_json_schema()),
            "input_schema": replace_refs(self.InputSchema.model_json_schema()),
            "is_table": self.is_table,
            "model": self.model,
        }

    @classmethod
    def adapt_version(cls, node_ids: List[str], flow_serialization_data: dict):
        assert len(node_ids := set(node_ids)) == len(
            node_ids
        ), "Node ids must be unique"
        for n in flow_serialization_data["nodes"]:
            n = n["id"]
            if n["_node_id"] not in node_ids:
                continue

            version_from = n.get("PLURALLY_VERSION")
            n["PLURALLY_VERSION"] = cls.PLURALLY_VERSION
            if version_from != cls.PLURALLY_VERSION and cls.PLURALLY_VERSION != 0:
                logger.debug(
                    f"Adapting {n['name']} ({n['_node_id'][:5]}) from version {version_from} to {cls.PLURALLY_VERSION}"
                )

                # need to find the number of edges to contexts handle:
                src_handles, tgt_handles = [], []
                src_handles_clean, tgt_handles_clean = [], ["run"]

                src_added = set()
                tgt_added = set()

                for e in flow_serialization_data["links"]:
                    if e["target"] == n["_node_id"] and e["tgt_handle"] == "contexts":
                        tgt_added.add(e["tgt_handle"])
                        new_tgt_handle = NameableHandle(
                            free=f"Input {len(tgt_handles) + 1}"
                        )
                        tgt_handles.append(new_tgt_handle.model_dump())
                        tgt_handles_clean.append(new_tgt_handle._clean)
                        e["tgt_handle"] = new_tgt_handle._clean
                        e["key"] = (
                            e["key"].split("###")[0] + "###" + new_tgt_handle._clean
                        )
                    elif e["source"] == n["_node_id"]:
                        if n["is_table"]:
                            assert e["src_handle"] == "data"
                            src_added.add(e["src_handle"])
                            new_src_handle = NameableHandle(
                                free=e["src_handle"].title(),
                            )
                        else:
                            src_added.add(e["src_handle"])
                            new_src_handle = NameableHandle(
                                free=e["src_handle"] + f" {len(src_handles) + 1}"
                            )
                        src_handles.append(new_src_handle.model_dump())
                        src_handles_clean.append(new_src_handle._clean)
                        e["src_handle"] = new_src_handle._clean
                        e["key"] = (
                            new_src_handle._clean + "###" + e["key"].split("###")[1]
                        )

                # also add handles that are not connected...
                for src_handle in n["output_fields"]:
                    if src_handle not in src_added:
                        new_src_handle = NameableHandle(
                            free=src_handle + f" {len(src_handles) + 1}"
                        )
                        src_handles.append(new_src_handle.model_dump())
                        src_handles_clean.append(new_src_handle._clean)

                for tgt_handle in ["contexts"]:
                    if tgt_handle not in tgt_added:
                        new_tgt_handle = NameableHandle(
                            free=f"Input {len(tgt_handles) + 1}"
                        )
                        tgt_handles.append(new_tgt_handle.model_dump())
                        tgt_handles_clean.append(new_tgt_handle._clean)

                n["input_fields"] = tgt_handles
                n["output_fields"] = src_handles
                n["tgt_handles"] = tgt_handles_clean
                n["src_handles"] = src_handles_clean

    @classmethod
    def _parse(cls, **kwargs):
        kwargs = load_from_json_dict(kwargs)
        kwargs["output_fields"] = [NameableHandle(**o) for o in kwargs["output_fields"]]
        kwargs["input_fields"] = [NameableHandle(**i) for i in kwargs["input_fields"]]
        return cls(cls.InitSchema(**kwargs))

    def add_target_handle(self, src_handle):
        """
        src_handle is the handle that one wants to connect to the node while adding a tgt_handle
        """
        new_tgt_handle = NameableHandle(free=src_handle)
        ix = 1
        while new_tgt_handle._clean in [i._clean for i in self.input_fields]:
            new_tgt_handle = NameableHandle(free=new_tgt_handle.free + f" {ix}")
        self.input_fields = [*self.input_fields, new_tgt_handle]
        return new_tgt_handle._clean
