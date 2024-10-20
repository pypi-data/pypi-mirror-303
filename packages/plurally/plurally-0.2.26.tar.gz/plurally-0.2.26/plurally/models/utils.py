from typing import Dict, List, get_origin

from pydantic import BaseModel, create_model


def is_list_type(schema):
    return hasattr(schema, "annotation") and get_origin(schema.annotation) is list


def get_required_fields(schema):
    required_fields = set()
    for field_name, field in schema.model_fields.items():
        if field.is_required():
            required_fields.add(field_name)
    return required_fields


def create_dynamic_model(
    model_name: str,
    fields: List[str],
    defaults: dict = None,
    types: dict = None,
    base=None,
):
    fields_map = {}
    defaults = defaults or {}
    types = types or {}
    for field_name in fields:
        field_type = types.get(field_name, str)
        if (
            field_name in defaults
        ):  # do not replace by defaults.get(field_name), as None is not the same as ...
            fields_map[field_name] = (field_type, defaults[field_name])
        else:
            fields_map[field_name] = (field_type, ...)
    return create_model(model_name, **fields_map, __base__=base)


class Link(BaseModel):
    key: str
    label: str
    source: str
    src_handle: str
    target: str
    tgt_handle: str


def serialize_link(link: Dict, input_schemas, output_schemas) -> Dict:
    source = link["source"]
    target = link["target"]

    src_handle_title = output_schemas[source.node_id]["properties"][
        link["src_handle"]
    ].get("title")
    tgt_handle_title = input_schemas[target.node_id]["properties"][
        link["tgt_handle"]
    ].get("title")

    label = f"{src_handle_title} -> {tgt_handle_title}"
    return Link(
        **{
            **link,
            "label": label,
            "source": source.node_id,
            "target": target.node_id,
        }
    ).model_dump()


def get_input_schemas(nodes, to_json=True) -> Dict[str, Dict]:
    input_schemas = {}
    for node in nodes:
        input_schemas[node.node_id] = (
            node.InputSchema.model_json_schema() if to_json else node.InputSchema
        )
    return input_schemas


def get_output_schemas(nodes, to_json=True) -> Dict[str, Dict]:
    output_schemas = {}
    for node in nodes:
        output_schemas[node.node_id] = (
            node.OutputSchema.model_json_schema() if to_json else node.OutputSchema
        )
    return output_schemas
