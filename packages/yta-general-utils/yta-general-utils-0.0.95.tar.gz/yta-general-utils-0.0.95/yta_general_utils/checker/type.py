from typing import Union

import inspect


def variable_is_type(variable, type):
    """
    Checks if the type of the provided 'variable' is the also provided
    'type', returning True if yes or False if not.
    """
    # TODO: Maybe let this accept array of types to check if one of 
    # them (?)
    # Check this to validate 'type' is array to treat it like an array:
    # https://stackoverflow.com/a/16807050
    if isinstance(variable, type):
        return True
    
    return False

def variable_is_number(variable: Union[int, float, str]):
    """
    This method checks if the provided 'variable' is a numeric type,
    or tries to cast it as a float number if string provided, and
    returns True in the only case that the 'variable' is actual a
    number by itself or as a string.
    """
    if not isinstance(variable, (int, float, str)):
        return False
    
    if isinstance(variable, str):
        try:
            float(variable)
        except:
            return False
        
    return True

def variable_is_positive_number(variable: Union[int, float, str]):
    """
    This method checks if the provided 'variable' is a numeric type,
    or tries to cast it as a float number if string provided, and
    returns True in the only case that the 'variable' is actual a
    number by itself or as a string and it is 0 or above it.
    """
    if not isinstance(variable, (int, float, str)):
        return False
    
    if isinstance(variable, str):
        try:
            variable = float(variable)
        except:
            return False
        
    return variable >= 0

def code_file_is(parameter, filename):
    """
    Checks if the provided parameter code is contained in the also
    provided 'filename'. This method is useful to check Enum objects
    or classes as we know the name we use for the files.

    This method was created to be able to check if a function that
    was passed as parameter was part of a custom Enum we created
    and so we could validate the was actually that custom Enum.
    Working with classes was not returning the custom Enum class
    created, so we needed this.
    """
    if inspect.getfile(parameter).endswith(filename):
        return True
    
    return False

def is_class(parameter, class_names: Union[str, list[str]]):
    """
    Checks if the provided 'parameter' is of one of the also provided
    'class_names'.
    """
    # TODO: Improve this checking and transforming
    if isinstance(class_names, str):
        class_names = [class_names]

    return type(parameter).__name__ in class_names