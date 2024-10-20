import os
import re

import yaml

from .template import convert_shortcode, convert_template


def default_project_name(name):
    return f"{name}"


def generate_project_folder_cwd(project_name):
    directory = os.getcwd()
    os.makedirs(os.path.join(directory, default_project_name(project_name)))


def create_yaml_file(project_name, filename, library=None):
    directory = os.getcwd()
    with open(
        os.path.join(directory, default_project_name(project_name), filename),
        "w",
        encoding="utf-8",
    ) as fw:
        fw.write(yaml.dump(library, default_flow_style=False))
        fw.close()


def write_file_content(
    directory: str, folder_name: str, file: str, content: str, args=None
):
    file_path = os.path.dirname(file)
    if file_path != "":
        new_folder = os.path.join(
            directory, default_project_name(folder_name), file_path
        )

        if os.path.exists(new_folder) is False:
            os.makedirs(new_folder)

    name = os.path.join(directory, default_project_name(folder_name), file)
    base_name = os.path.splitext(name)

    content = convert_shortcode(content, args)
    if len(base_name) > 1:
        if re.match(r"^(.tpl)", base_name[1]):
            raw_filename = base_name[0]
            raw_fileext = re.sub(r"(.tpl)", ".", base_name[1]).strip()
            if raw_fileext == ".":
                raw_fileext = ""
            name = os.path.join(
                directory, default_project_name(folder_name), f"{raw_filename}{raw_fileext}"
            )
            content = convert_template(content, args)
    with open(name, "w", encoding="utf-8") as f_write:
        f_write.write(content)
        f_write.close()
