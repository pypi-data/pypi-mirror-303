import os
import sys

from plutonkit.framework.starter_architecture import StarterArchitecture


class CreateAchitecture:
    def __init__(self, argv) -> None:
        self.argv = argv

    def comment(self):
        return "Create your first architecture"

    def execute(self):

        project_name = input("Name of folder project?")
        folder_name = f"Project name: {project_name}"
        answer = input(f"\n{folder_name}\nDo you want to proceed creating your starterkit?(y/n) > ")
        if answer == "y":
            framework_blueprint = StarterArchitecture(os.getcwd(),project_name)
            framework_blueprint.set_folder_name(project_name)
            framework_blueprint.execute()
        sys.exit(0)
