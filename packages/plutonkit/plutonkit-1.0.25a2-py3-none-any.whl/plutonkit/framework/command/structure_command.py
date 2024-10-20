import platform
import re
from copy import copy
from os import path
from typing import List

from .schema_command import SchemaCommand


class StructureCommand:
    def __init__(self, reference_value, directory: str) -> None:

        self.reference_value = reference_value
        self.directory = directory

    def get_error(self) -> List[str]:

        schema_command = SchemaCommand(self.reference_value)
        command_list: List[str] = schema_command.get_error()
        return command_list

    def get_list_commands(self):
        scripts = self.reference_value.get("script", {})
        if platform.system() == "Windows":
            if "win_script" in self.reference_value:
                scripts = self.reference_value.get("win_script", {})
        obj_commands = {}
        for key, value in scripts.items():
            sub_list = [key]
            self.__add_sub_command(value)
            self.__get_sub_command(obj_commands, sub_list, value)
        return obj_commands

    def __add_sub_command(self, values):
        if "chdir" not in values:
            values["chdir"] = self.directory
        else:
            values["chdir"] = path.join(
                self.directory, self.__get_format_str(values["chdir"])
            )

    def __get_sub_command(self, obj_commands, list_commands, values):
        glob = {}
        for key, value in values.items():
            if key == "group":
                list_commands_copy = copy(list_commands)
                for key1, value1 in value.items():
                    list_commands_copy.append(key1)
                    self.__add_sub_command(value1)
                    self.__get_sub_command(obj_commands, list_commands_copy, value1)
                    list_commands_copy.pop()
            else:
                glob[key] = self.__get_format_str(value)
                obj_commands[":.:".join(list_commands)] = glob

    def __get_format_str(self, value):

        if isinstance(value, str):
            value = self.__set_replace_str(value)
        if isinstance(value, (List)):
            for kk, vv in enumerate(value):
                value[kk] = self.__set_replace_str(vv)

        return value

    def __set_replace_str(self, value):

        environment = self.reference_value.get("environment", {})

        find_value = re.findall(r"(\{\$)([a-zA-Z0-0_]{1,})(\})", value)
        if len(find_value) > 0:
            for val in find_value:
                value = value.replace("".join(val), environment.get(val[1], ""))

        return value
