"""Module providing a function printing python version."""


def format_argument_input(type_format, name, question, option_name, config):
    return {
        "field_type": "input",
        "type": type_format,
        "name": name,
        "option_name": option_name,
        "question": question,
        "config": config,
    }
