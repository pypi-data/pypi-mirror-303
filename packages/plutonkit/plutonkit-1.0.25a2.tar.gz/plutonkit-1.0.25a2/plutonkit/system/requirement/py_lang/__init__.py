import os

from plutonkit.config import REQUIREMENT
from plutonkit.config.framework import STANDARD_LIBRARY
from plutonkit.management.logic.ConditionSplit import ConditionSplit

from ....helper.filesystem import default_project_name


def pip_generate_requirement(directory,project_name, values,args):
    default_item = values.get("default", [])
    library = []
    for value in default_item:
        library.append(value)

    optional_item = values.get("optional", [])
    for value in optional_item:
        cond_valid = ConditionSplit(value.get("condition"), args)
        if "dependent" in value and cond_valid.validCond():
            library += value.get("dependent", [])
    with open(
        os.path.join(directory, default_project_name(project_name), REQUIREMENT),
        "w",
        encoding="utf-8",
    ) as fw:
        fw.write("\n".join(STANDARD_LIBRARY + library + [""]))
        fw.close()
