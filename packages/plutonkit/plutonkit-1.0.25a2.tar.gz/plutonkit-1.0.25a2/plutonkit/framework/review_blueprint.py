import os

from plutonkit.framework.analysis.word_distance import WordDistance
from plutonkit.management.request.ArchitectureRequest import (
    ArchitectureRequest,
)

VALID_MASTER_BLUEPRINT_KEY = ["name", "bootscript","env", "settings", "choices", "dependencies", "script", "files"]


class ReviewBlueprint:
    def __init__(self, blueprint_content, path) -> None:
        self.path = path
        self.directory = os.getcwd()
        self.blueprint_content = blueprint_content

    def verify_blueprint(self):
        validate_data = {
            "error_message": [],
        }
        self.__check_invalid_value(validate_data, self.blueprint_content, VALID_MASTER_BLUEPRINT_KEY)
        arch_req = ArchitectureRequest(self.path, self.directory)
        if arch_req.isValidReq is False:
            validate_data["error_message"].append(arch_req.errorMessage)

        if len(validate_data["error_message"]) == 0:

            if "name" not in self.blueprint_content:
                validate_data["error_message"].append(
                    "`name` is missing in architecture.yaml, please provide"
                )
            if "settings" not in self.blueprint_content:
                validate_data["error_message"].append(
                    "`settings` is missing in architecture.yaml, please provide"
                )
            else:
                if "install_type" not in self.blueprint_content["settings"]:
                    validate_data["error_message"].append(
                        "`settings -> install_type` is missing in architecture.yaml, please provide"
                    )

            self.__verify_files(validate_data,arch_req)
            self.__verify_choices(validate_data)
            self.__verify_dependencies(validate_data)
            self.__verify_script(validate_data)
            self.__verify_bootsript(validate_data)
        return validate_data

    def __verify_files(self,validate_data,arch_req):
        if "files" not in self.blueprint_content:
            validate_data["error_message"].append(
                "`files` is missing in architecture.yaml, please provide"
                )
        else:
            self.__check_invalid_value(validate_data, self.blueprint_content["files"], [
                "mv_file", "default", "optional"], "files -> ")
            if "optional" in self.blueprint_content["files"]:
                for val in self.blueprint_content["files"]["optional"]:
                    self.__check_invalid_value(validate_data,  val, [
                        "condition", "dependent","mv_file", "mv_folder_name"], "files ->optional -> ")

            self._check_files(validate_data, self.blueprint_content["files"], arch_req)
    def __verify_choices(self,validate_data):
        if "choices" in self.blueprint_content:
            for val in self.blueprint_content["choices"]:
                self.__check_invalid_value(validate_data,  val, [
                    "name", "question", "type", "option"], "choices[] -> ")

    def __verify_dependencies(self,validate_data):
        if "dependencies" in self.blueprint_content:
            self.__check_invalid_value(validate_data,  self.blueprint_content["dependencies"], [
                "default", "optional"], "dependencies -> ")

            if "optional" in self.blueprint_content["dependencies"]:
                for val in self.blueprint_content["dependencies"]["optional"]:
                    self.__check_invalid_value(validate_data,  val, [
                        "condition", "dependent"], "dependencies ->optional -> ")

    def __verify_script(self,validate_data):
        if "script" in self.blueprint_content:
            for _, val in self.blueprint_content["script"].items():
                self.__check_invalid_value(validate_data,  val, [
                    "command", "description"], "script[] -> ")
    def __verify_bootsript(self,validate_data):
        if "bootscript" in self.blueprint_content:
            for val in self.blueprint_content["bootscript"]:
                self.__check_invalid_value(validate_data, val, [
                    "command", "exec_position", "condition"], "bootscript[] -> ")
                if "exec_position" in val:
                    if val["exec_position"] != "start" and val["exec_position"] != "end":
                        validate_data["error_message"].append(
                            "the `bootscript[] -> exec_position` is invalid, choose either start or end"
                        )

    def __check_invalid_value(self, validate_data, values, trained, main_key=""):
        words_distance = WordDistance(trained)
        for key,_ in values.items():
            distances = words_distance.get_ave_distance(key)
            max_distance = max(distances)
            if max_distance != 1.0:
                validate_data["error_message"].append(
                    f"the `{main_key}{key}` is invalid,  I assume you are using this command `{main_key}{trained[distances.index(max_distance)]}`"
                )

    def _check_files(self, validate_data, value_files, arch_req):
        default_item = value_files.get("default", [])

        #
        for val in value_files.get("optional", []):
            for val2 in val["dependent"]:
                default_item.append(val2)

        for value in default_item:
            data = arch_req.getFiles(value["file"])
            if data["is_valid"] is False:
                validate_data["error_message"].append(
                    f'error in downloading the file `{value["file"]}`'
                )
