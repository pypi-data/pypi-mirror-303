"""Module providing a function printing python version."""

import sys

from plutonkit.command.action.clone_project import CloneProject
from plutonkit.command.action.command import Command
from plutonkit.command.action.create_achitecture import CreateAchitecture
from plutonkit.command.action.create_project import CreateProject
from plutonkit.command.action.validate_blueprint import ValidateBlueprint

argv = sys.argv
ACTIONS = {
    "clone_project": CloneProject(argv),
    "create_achitecture": CreateAchitecture(argv),
    "create_project": CreateProject(argv),
    "cmd": Command(argv),
    "validate_blueprint": ValidateBlueprint(argv),
}
