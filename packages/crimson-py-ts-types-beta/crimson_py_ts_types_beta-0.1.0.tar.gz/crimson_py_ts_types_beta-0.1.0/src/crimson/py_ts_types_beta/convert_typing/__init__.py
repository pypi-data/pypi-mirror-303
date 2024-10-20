from crimson.py_ts_types_beta.convert_typing.positive import SubscribeNode
from crimson.py_ts_types_beta.convert_typing.negative import convert_final


def convert_py_to_ts(py_annotation: str) -> str:
    root = SubscribeNode(converted=[py_annotation])
    root.generate_children()
    return root.to_string()


def convert_ts_to_py(ts_annotation: str) -> str:
    return convert_final(ts_annotation)
