from pydantic import BaseModel
from typing import Dict, Type
import ast
from crimson.py_ts_types_beta.convert_typing import convert_py_to_ts
from crimson.ast_dev_tool import collect_nodes
from pydantic.fields import FieldInfo
from typing import _TypedDictMeta


def convert_fieldinfo_to_string_dict(field_info: FieldInfo) -> Dict[str, str]:
    code = repr(field_info)
    call_node = collect_nodes(code, ast.Call)[0]
    output = {}
    for keyword in call_node.keywords:
        output[keyword.arg] = ast.unparse(keyword.value)
    return output


def get_string_fields(model_fields: Dict[str, FieldInfo]) -> Dict[str, Dict[str, str]]:
    string_fields = {}
    for arg, field_info in model_fields.items():
        string_fields[arg] = convert_fieldinfo_to_string_dict(field_info)

    return string_fields


def generate_arg(name: str, string_dict: Dict[str, str]):
    template = f"{name}"
    if string_dict["required"] == "False":
        template = template + "?"
    return template


def generate_annotation(annotation: str):
    annotation = convert_py_to_ts(annotation)
    return f":{annotation}"


def generate_interface_line(name: str, string_dict: Dict[str, str]):
    return generate_arg(name, string_dict) + generate_annotation(
        string_dict["annotation"]
    )


def generate_interface(model_obj: Type[BaseModel], indent: int = 4):
    start = """interface {name}""".format(name=model_obj.__name__) + " {"
    string_fields = get_string_fields(model_obj.model_fields)
    arg_lines = [
        " " * indent + generate_interface_line(name, string_dict)
        for name, string_dict in string_fields.items()
    ]
    end = "}"

    return "\n".join([start] + arg_lines + [end])


def generate_default_line(name: str, string_dict: Dict[str, str]) -> str | None:
    if "default" in string_dict.keys():
        return f"{name} = {string_dict['default']}"
    else:
        None


def generate_default(model_obj: Type[BaseModel], indent: int = 4):
    start = """const default{name}: {name}""".format(name=model_obj.__name__) + " {"
    string_fields = get_string_fields(model_obj.model_fields)
    arg_lines = [
        " " * indent + generate_default_line(name, string_dict)
        for name, string_dict in string_fields.items()
        if generate_default_line(name, string_dict) is not None
    ]
    end = "}"

    return "\n".join([start] + arg_lines + [end])


def is_basemodel(obj: object) -> bool:
    candidates = [BaseModel]
    for candidate in candidates:
        if any([base is candidate for base in obj.__bases__]):
            return True
    return False


def is_typeddict(obj: object) -> bool:
    return type(obj) is _TypedDictMeta
