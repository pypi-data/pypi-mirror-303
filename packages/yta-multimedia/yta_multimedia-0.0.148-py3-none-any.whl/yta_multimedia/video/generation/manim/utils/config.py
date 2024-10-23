from yta_general_utils.file.writer import write_file
from yta_general_utils.programming.path import get_project_abspath

import json


CONFIG_MANIM_ABSPATH = get_project_abspath() + 'manim_parameters.json'

def write_manim_config_file(json_data):
    """
    Writes in the configuration file that we use to share
    parameters with manim software. This is the way to 
    share parameters to the process.
    
    TODO: I would like to be able to handle manim through 
    python code directly and not an external process I run,
    but for now this is working.
    """
    # We serialize json to str
    json_object_str = json.dumps(json_data, indent = 4)
    
    write_file(json_object_str, CONFIG_MANIM_ABSPATH)

def read_manim_config_file():
    """
    Reads the configuration file and returns it as a json
    object.
    """
    json_object = None

    # TODO: Create a general method to read files (?)
    with open(CONFIG_MANIM_ABSPATH, 'r') as config_file:
        json_object = json.load(config_file)
        config_file.close()

    return json_object