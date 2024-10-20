from yta_general_utils.file.checker import file_exists

import json


def read_json_from_file(filename: str):
    """
    Reads the provided 'filename' and turns the information 
    into a json format (if possible). This method returns
    None if it was not possible.

    @param
        **filename**
        File path from which we want to read the information.
    """
    if not filename:
        return None
    
    if not file_exists(filename):
        return None
    
    with open(filename, encoding = 'utf-8') as json_file:
        return json.load(json_file)