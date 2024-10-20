import re

from plutonkit.config.framework import VAR_SHORTCUT_TEMPLATE
from plutonkit.helper.arguments import get_dict_value


class TheShortCutWord:
    def __init__(self, content: str, args=None):
        self.args = args
        self.content = content
        self.data = self.__wragle_data(content)

    def __get_init_action(self, val, actions):
        if actions[0]["name"] in VAR_SHORTCUT_TEMPLATE:
            val = VAR_SHORTCUT_TEMPLATE[actions[0]["name"]](val,actions)

        actions.pop(0)
        if len(actions) > 0:
            return self.__get_init_action(val, actions)
        return val

    def __get_action(self, vals):
        list_template = []
        for val in vals:
            arg_val = re.findall(r"(.*?)(\()(.*?)(\))", val)
            if len(arg_val) == 0:
                list_template.append({"name": val.strip(), "arg": []})
            else:
                list_template.append(
                    {
                        "name": arg_val[0][0].strip(),
                        "arg": arg_val[0][2].strip().split(","),
                    }
                )

        return list_template

    def __take_value(self, val):
        split_value = val.split("|")

        val_retrieve = get_dict_value(split_value[0].split("."), self.args)
        if val_retrieve is not None and len(split_value) > 1:
            arg_pass = self.__get_action(split_value[1:])
            val_retrieve = self.__get_init_action(val_retrieve, arg_pass)
        return val_retrieve

    def __wragle_data(self, contents):
        list_template = []
        find_value = re.findall(r"(\{\{)(.*?)(\}\})", contents)
        for val in find_value:
            if len(val) == 3:
                list_template.append(
                    {
                        "template": "".join(val),
                        "variable": self.__take_value(val[1].strip()),
                    }
                )
        return list_template

    def get_convert(self):

        for val in self.data:
            self.content = self.content.replace(val["template"], str(val["variable"]))

        return self.content
