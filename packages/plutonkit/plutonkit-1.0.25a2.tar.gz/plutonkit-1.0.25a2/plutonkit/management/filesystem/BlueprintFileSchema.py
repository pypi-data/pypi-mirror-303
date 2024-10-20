import re

from plutonkit.helper.template import convert_shortcode


class BlueprintFileSchema:
    def __init__(self, value, args) -> None:
        self.value = value
        self.args = args

    def isObjFile(self):
        return "file" in self.value

    def get_save_files(self):
        value_mv_file = self.__clean_file_name(convert_shortcode(self.value.get("mv_file",""), self.args))
        value_file = self.__clean_file_name(convert_shortcode(self.value.get("file",""), self.args))
        list_mv_files = [value_mv_file]
        list_files = [value_file]
        if "mv_file" in self.value:
            return list_mv_files
        return list_files

    def __clean_file_name(self, name):
        name = re.sub(r"^(/)", "", name)
        return name
