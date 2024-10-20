from typing import List, Tuple

from crimson.py_ts_types_beta.convert_typing.schema import SchemaHolder


def validate(annotation_string: str):
    bracket_pairs = [("[", "]"), ("<", ">")]
    for open, close in bracket_pairs:
        if annotation_string.count(open) != annotation_string.count(close):
            raise Exception("Check bracket counts.")


def generate_mapping(node_name: str) -> List[Tuple[str, str]]:
    schema = SchemaHolder.converted_schemas[node_name]
    mapping = [("|", ",")]
    mapping.append((schema.open, "["))
    mapping.append((schema.close, "]"))
    return mapping


def tokenize_and_extract_strings(
    input_string: str, quotes: List[str] = ["'", '"'], string_token="text"
) -> Tuple[str, List[str], List[str]]:
    result = []
    extracted_strings = []
    i = 0
    in_string = False
    current_quote = ""
    current_string = ""
    token_count = 0
    used_quotes = []

    while i < len(input_string):
        if not in_string:
            if input_string[i] in quotes:
                in_string = True
                current_quote = input_string[i]
                current_string = current_quote
                used_quotes.append(current_quote)
            else:
                result.append(input_string[i])
        else:
            if input_string[i] == current_quote:
                current_string += current_quote
                extracted_strings.append(current_string[1:-1])  # Remove quotes
                result.append(string_token + str(token_count))
                in_string = False
                current_string = ""
                token_count += 1
            else:
                current_string += input_string[i]
        i += 1

    return "".join(result), extracted_strings, used_quotes


def get_first_unit_node_indexes(
    input_string: str, separators=["<", "[", ",", "|"]
) -> Tuple[int, int, int]:
    first_close_index = input_string.find(">")
    front = input_string[:first_close_index]
    pair_open_index = front.rfind("<")
    previous_separator_index = max(
        [input_string[:pair_open_index].rfind(separator) for separator in separators]
    )

    return previous_separator_index, pair_open_index, first_close_index


def split_annotation(input_string: str) -> Tuple[str, str, str, str]:
    previous_separator_index, pair_open_index, first_close_index = (
        get_first_unit_node_indexes(input_string)
    )
    node_name = input_string[previous_separator_index + 1 : pair_open_index]
    before_node = input_string[: previous_separator_index + 1]
    first_unitnode = input_string[previous_separator_index + 1 : first_close_index + 1]
    after_node = input_string[first_close_index + 1 :]
    return node_name, before_node, first_unitnode, after_node


def convert_unit_node(node_name: str, unit_node: str) -> str:
    mapping = generate_mapping(node_name)
    converted = unit_node
    for target, new in mapping:
        converted = converted.replace(target, new)
    return converted


def convert_first_unitnode(input_string: str) -> str:
    validate(input_string)
    node_name, before_node, first_unitnode, after_node = split_annotation(input_string)

    unitnode = convert_unit_node(node_name, first_unitnode)
    new_text = before_node + unitnode + after_node
    validate(new_text)
    return new_text


def convert(tokenized_annotation_string: str) -> str:
    num_nodes = tokenized_annotation_string.count("<")
    for _ in range(num_nodes):
        tokenized_annotation_string = convert_first_unitnode(
            tokenized_annotation_string
        )
    return tokenized_annotation_string


def convert_final(annotation_string: str) -> str:

    string_free_string, extracted_strings, used_quotes = tokenize_and_extract_strings(
        input_string=annotation_string,
        quotes=["'", "'''", '"', '"""'],
        string_token="text",
    )

    string_free_string = string_free_string.replace(" ", "")

    converted = convert(tokenized_annotation_string=string_free_string)

    for i, extracted_string in enumerate(extracted_strings):
        token = f"text{i}"
        quote = used_quotes[i]
        converted = converted.replace(token, f"{quote}{extracted_string}{quote}")

    return converted
