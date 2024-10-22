from typing import Dict, List

from pydantic import ConfigDict, Field, conlist, constr

from plurally.json_utils import replace_refs
from plurally.models.node import Node
from plurally.models.utils import create_dynamic_model


class Switch(Node):
    ICON = "switch"

    class InitSchema(Node.InitSchema):
        """Creates a conditional branching. The output corresponding to the input's value will be activated, the others won't."""

        model_config = ConfigDict(json_schema_extra={"hide-run": True})
        possible_values: conlist(
            constr(pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
            min_length=1,
        ) = Field(
            title="Possible Values",
            description="The possible values that the input can take.",
            example=["yes", "no"],
            min_length=1,
            help="For instance, if your input can be 'yes' or 'no', then you should have \"yes\" and \"no\" as possible values. These outputs will then be used to condition the flow.",
            json_schema_extra={
                "is_output": True,
                "uniqueItems": True,
                "uiSchema": {
                    "items": {
                        "ui:label": False,
                        "errorMessages": {
                            "pattern": "Outputs can only contain letters, numbers, and underscores, and must start with a letter."
                        },
                    }
                },
            },
        )

    class InputSchema(Node.InputSchema):
        value: str = Field(
            title="Input",
            description="The input to condition on.",
        )

    class OutputSchema(Node.OutputSchema):
        key_vals: Dict[str, str]

    DESC = InitSchema.__doc__

    def __init__(self, init_inputs: InitSchema) -> None:
        self._possible_values = init_inputs.possible_values
        super().__init__(init_inputs)

    @property
    def possible_values(self):
        return self._possible_values

    @possible_values.setter
    def possible_values(self, value):
        self._possible_values = value
        self._set_schemas()
        self.src_handles = self._get_handles(self.OutputSchema, None)

    def _set_schemas(self) -> None:
        # create pydantic model from fields
        self.OutputSchema = create_dynamic_model(
            "OutputSchema",
            self.possible_values,
            defaults={val: None for val in self.possible_values},
            types={val: bool for val in self.possible_values},
        )

    def forward(self, node_input: InputSchema):
        for val in self.possible_values:
            self.outputs[val] = False
        self.outputs[node_input.value] = True

    def serialize(self):
        return {
            **super().serialize(),
            "possible_values": self.possible_values,
            "output_schema": replace_refs(self.OutputSchema.model_json_schema()),
        }


class LogicalInputSchema(Node.InputSchema):
    inputs: List[bool] = Field(
        description="The inputs.",
        min_length=1,
        examples=[True, False],
    )


class And(Node):
    ICON = "switch"

    InputSchema = LogicalInputSchema

    class InitSchema(Node.InitSchema):
        __doc__ = "Will return True if all of the inputs are True, else False."
        model_config = ConfigDict(json_schema_extra={"hide-run": True})

    class OutputSchema(Node.OutputSchema):
        output: bool = Field(
            description="The output, will be True if all of the inputs are True, else False.",
            examples=[True, False],
        )

    def forward(self, node_input: InputSchema):
        self.outputs["output"] = all(node_input.inputs)


class Or(Node):
    ICON = "switch"

    InputSchema = LogicalInputSchema

    class InitSchema(Node.InitSchema):
        __doc__ = "Will return True if any of the inputs is True, else False."
        model_config = ConfigDict(json_schema_extra={"hide-run": True})

    class OutputSchema(Node.OutputSchema):
        output: bool = Field(
            description="The output, will be True if any of the inputs is True, else False.",
            examples=[True, False],
        )

    def forward(self, node_input: InputSchema):
        self.outputs["output"] = any(node_input.inputs)


__all__ = ["Switch", "And", "Or"]
