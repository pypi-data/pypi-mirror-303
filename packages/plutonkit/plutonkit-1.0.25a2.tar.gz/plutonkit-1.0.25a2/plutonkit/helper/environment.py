import copy
import os

from .template import convert_shortcode


def setEnvironmentVariable(values):
    for key,value in values.items():
        os.environ[key] = value

def convertVarToTemplate(template):
    return convert_shortcode(template,copy.deepcopy(os.environ))
