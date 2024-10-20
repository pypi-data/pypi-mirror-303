import ast
from typing import List
from crimson.ast_dev_tool import collect_nodes
from crimson.py_ts_types_beta.convert_typing.schema import SchemaHolder
from crimson.anytree_extension.patch.nodemixin import NodeMixinTyped


def separate_list(data: List, separator: str):
    output = []
    for unit in data:
        output.append(unit)
        output.append(separator)
    del output[-1]
    return output


def convert_with_elts(
    node: ast.Subscript, name: str, open: str, close: str, separator: str
) -> List[str]:
    start = name + open
    elements = [ast.unparse(elt) for elt in node.slice.elts]
    elements = separate_list(elements, separator)
    return [start] + elements + [close]


def convert_with_slice(
    node: ast.Subscript, name: str, open: str, close: str
) -> List[str]:
    start = name + open
    return [start] + [ast.unparse(node.slice)] + [close]


def convert_unit(code: str) -> List[str] | None:
    nodes = collect_nodes(code, ast.Subscript)

    if len(nodes) != 0:
        node = nodes[0]

        for key, with_elts in SchemaHolder.with_elts_schemas.items():
            if node.value.id == key.__name__:
                return convert_with_elts(node, **with_elts.model_dump())

        for key, with_slice in SchemaHolder.with_slice_schemas.items():
            if node.value.id == key.__name__:
                return convert_with_slice(node, **with_slice.model_dump())

    return None


class SubscribeNode(NodeMixinTyped["SubscribeNode"]):
    def __init__(
        self,
        parent=None,
        children=None,
        converted=List[str],
        index: int | None = None,
    ):
        self.parent = parent
        self.converted = converted
        self.index = index
        if children:
            self.children = children

    def generate_children(self):
        for index, unit in enumerate(self.converted):
            try:
                converted = convert_unit(unit)
                if converted is not None:
                    child = SubscribeNode(parent=self, converted=converted, index=index)
                    child.generate_children()
            except:
                pass

    def to_string(self):
        output = self.converted.copy()
        for child in self.children:
            output[child.index] = child.to_string()
        return "".join(output)
