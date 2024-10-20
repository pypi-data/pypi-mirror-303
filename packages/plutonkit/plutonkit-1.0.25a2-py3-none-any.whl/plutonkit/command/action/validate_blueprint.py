import os
import sys

from yaml import Loader, load

from plutonkit.config import ARCHITECTURE_DETAILS_FILE
from plutonkit.framework.review_blueprint import ReviewBlueprint
from plutonkit.management.request.ArchitectureRequest import (
    ArchitectureRequest,
)


class ValidateBlueprint:
    def __init__(self, argv) -> None:
        self.argv = argv

    def comment(self):
        return "Check your blueprint before issue before deploying"

    def execute(self):
        command_list = self.argv[2::]
        if len(command_list) > 0:
            path = command_list[0]
            directory = os.getcwd()
            arch_req = ArchitectureRequest(path, directory)
            if arch_req.isValidReq:
                try:
                    content = load(str(arch_req.getValidReq), Loader=Loader)
                    cls = ReviewBlueprint(content, path)
                    verify_blueprint = cls.verify_blueprint()
                    if len(verify_blueprint["error_message"]) == 0:
                        print("No error found")
                    else:
                        for val in verify_blueprint["error_message"]:
                            print(val)
                except Exception as e:
                    print(e, f"Invalid {ARCHITECTURE_DETAILS_FILE}, please use proper yaml format")
                    sys.exit(0)
            else:
                print(arch_req.errorMessage)
        else:
            print("Please specify director , url or git location")
        sys.exit(0)
