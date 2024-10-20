import sys

from plutonkit.config import ARCHITECTURE_DETAILS_FILE
from plutonkit.helper.filesystem import (
    generate_project_folder_cwd, write_file_content,
)


class StarterArchitecture:
    def __init__(self,directory,project_name) -> None:
        self.directory = directory
        self.project_name = project_name
        self.folder_name = ""
    def set_folder_name(self, name):
        self.folder_name = name
    def execute(self):
        try:
            generate_project_folder_cwd(self.folder_name)
            write_file_content(
                            self.directory, self.folder_name, "README.md", "", {"project_name":self.project_name}
                        )
            write_file_content(
                            self.directory, self.folder_name, ARCHITECTURE_DETAILS_FILE, self._get_architecture_content(), {"project_name":self.project_name}
                        )

        except Exception as e:
            print(e)
            print("Invalid details to proceed in creating new project")
            sys.exit(0)


    def _get_architecture_content(self):
        return """
name: {{project_name}}
settings:
  install_type: pip
files:
  default:
    - file: README.md

"""
