"""Module providing a function printing python version."""

from plutonkit.config.func.shortcut import (
    shortcut_if, shortcut_join_space, shortcut_lower, shortcut_replace,
    shortcut_ucfirst, shortcut_upper,
)
from plutonkit.config.func.template import (
    template_content, template_load, template_python,
)
from plutonkit.management.format import format_argument_input

FRAMEWORK_WEB = [
    format_argument_input("framework", "django", "Do you need docker", "django", []),
    format_argument_input("framework", "bottle", "Do you need docker", "bottle", []),
    format_argument_input("framework", "fastapi", "Do you need docker", "fastapi", []),
    format_argument_input("framework", "flask", "Do you need docker", "flask", []),
]

FRAMEWORK_GRAPHQL = [
    format_argument_input(
        "framework", "graphene", "Do you need docker", "graphene", []
    ),
    format_argument_input("framework", "ariadne", "Do you need docker", "ariadne", []),
    format_argument_input(
        "framework", "tartiflette", "Do you need docker", "tartiflette", []
    ),
]

DEFAULT_GRPC = [
    format_argument_input(
        "framework", "default_grpc", "Do you need docker", "default", []
    ),
]

DEFAULT_WEB3 = [
    format_argument_input(
        "framework", "default_web3", "Do you need docker", "default", []
    ),
]

DEFAULT_PACKAGE = [
    format_argument_input(
        "framework", "default_starter_python", "Start creating your new python apps", "Python starter", []
    ),
    format_argument_input(
        "framework", "default_starter_golang", "Start creating your new go apps", "Golang starter", []
    ),
    format_argument_input(
        "framework", "default_starter_ruby", "Start creating your new ruby apps", "Ruby starter", []
    ),
]

DEFAULT_WEB_SOCKET = [
    format_argument_input(
        "framework", "default_websocket", "Do you need docker", "default", []
    ),
]

STANDARD_LIBRARY = ["pylint==3.0.2", "pytest==7.4.3", "python-decouple==3.8"]

VAR_SHORTCUT_TEMPLATE = {
    "ucfirst": shortcut_ucfirst,
    "lower": shortcut_lower,
    "upper": shortcut_upper,
    "join_space": shortcut_join_space,
    "replace": shortcut_replace,
    "if": shortcut_if,
}

VAR_TEMPLATE_EXEC = {
    "content": template_content,
    "load": template_load,
    "script": template_python
}


VAR_DEFAULT_BLUEPRINT = [
    "django",
    "bottle",
    "fastapi",
    "flask",
    "graphene",
    "ariadne",
    "tartiflette",
    "default_grpc",
    "default_web3",
    "default_starter_python",
    "default_starter_golang",
    "default_starter_ruby",
    "default_websocket"
]
