"""Module providing a function printing python version."""

import os
import re
import subprocess

from plutonkit.config import REQUIREMENT
from plutonkit.config.search import SEARCH_CHAR_ENCLOSE
from plutonkit.helper.filesystem import default_project_name

from .environment import convertVarToTemplate
from .format import get_enclose_str, replace_index_to_enclose, spilt_char


def pip_install_requirement(reference_value):
    directory = os.getcwd()
    path = os.path.join(
        directory,
        default_project_name(reference_value["details"]["project_name"]),
        REQUIREMENT,
    )
    subprocess.call(["pip", "install", "-r", path])

def pip_run_command(command):
    subprocess.call(command)

def clean_command_split(command: str):
    command = re.sub(r"\s{2,}", " ", command)
    command = spilt_char(command,SEARCH_CHAR_ENCLOSE)

    arg_split = get_enclose_str(convertVarToTemplate(command),[],SEARCH_CHAR_ENCLOSE)
    arg_split_replace_ant  = arg_split["replace_ant"]
    arg_split_content  = arg_split["content"].split(" ")
    for key,val in enumerate(arg_split_content):
        arg_split_content[key] = replace_index_to_enclose({
            "content": val,
            "replace_ant":arg_split_replace_ant
        },SEARCH_CHAR_ENCLOSE)

    return arg_split_content
