import re
from copy import deepcopy

from .ContentExtraction import ContentExtraction


class TemplateStruct:
    def __init__(self, contents: str, args=None):
        self.args = args
        self.contents: list[str] = contents.split("\n")
        self.join_contents = ""
        self.template: list[str] = self.__find_template(self.contents)

        self.get_component_template: list[str] = self.__component_template(
            self.template
        )
        self.convert_template: list[str] = self.__convert_template(
            self.get_component_template
        )

    def __find_template(self, contents: list[str]):
        templates = []
        rows = []
        for content in contents:
            if len(rows) > 0:
                if re.match(r"\}\)", content):

                    rows.append(content)
                    templates.append(deepcopy(rows))
                    rows = []
                else:
                    rows.append(content)

            if re.match(r"\(\{", content):

                rows.append(content)

        return templates

    def __component_template(self, contents: list[str]):
        templates = []
        for content in contents:
            raw_content = content[1:]
            raw_content = raw_content[0: len(raw_content) - 1]
            row_name = ""
            rows_capture_data = []
            rows_input = []
            rows_count = 0
            is_name = True
            for row in raw_content:
                start_value = re.findall(r"@([a-zA-Z0-9_]{1,})[\n\t\s]{0,}\{", row)

                if len(start_value) > 0:
                    row_name = start_value[0]
                    is_name = False

                if row_name != "":
                    findall_open = len(re.findall(r"{", row))
                    findall_close = len(re.findall(r"}", row))
                    if findall_open > 0:
                        rows_count += findall_open
                    if findall_close > 0:
                        rows_count -= findall_close

                if row_name != "":
                    if rows_count == 0:
                        rows_capture_data.append(
                            {"name": row_name, "input": deepcopy(rows_input)}
                        )

                        rows_input = []
                        row_name = ""

                    else:
                        if is_name:
                            rows_input.append(row)
                        is_name = True
            templates.append({"template": content, "component": rows_capture_data})

        return templates

    def __convert_template(self, templates=None):

        self.join_contents = "\n".join(self.contents)
        data = []

        for template in templates:
            list_template = template.get("template", [])
            str_template = "\n".join(list_template)
            list_component = template.get("component", [])
            template_instruction = ContentExtraction(list_component, self.args)
            data.append(
                {
                    "template": str_template,
                    "component": template_instruction.get_component,
                }
            )

        return data

    def get_content(self) -> str:
        return self.join_contents
