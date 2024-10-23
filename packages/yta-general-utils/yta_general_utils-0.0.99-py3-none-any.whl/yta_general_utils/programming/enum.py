from yta_general_utils.programming.parameter_validator import ParameterValidator
from yta_general_utils.programming.error_message import ErrorMessage
from random import choice as rand_choice
from enum import Enum


class YTAEnum(Enum):
    @classmethod
    def is_valid_value(cls, value):
        """
        This method returns True if the provided 'value' is a valid
        value for this YTAEnum class, or False if not.
        """
        return is_valid_value(value, cls)
    
    @classmethod
    def is_valid_name(cls, name, ignore_case: bool = False):
        """
        This method returns True if the provided 'name' is a valid
        name of this YTAEnum class, or False if not.
        """
        return is_valid_name(name, cls, ignore_case)
    
    @classmethod
    def is_valid_name_or_value(cls, name_or_value):
        """
        This method returns True if the provided 'name_or_value' is
        a valid name or a valid value of this YTAEnum class, or 
        False if not.
        """
        return is_valid_name_or_value(name_or_value, cls)
    
    @classmethod
    def is_valid(cls, name_or_value_or_enum):
        """
        This method returns True if the provided 'name_or_value_or_enum'
        is a valid name, a valid value or a valid instance of this
        YTAEnum class, or returns False if not.
        """
        return is_valid(name_or_value_or_enum, cls)
    
    @classmethod
    def name_to_enum(cls, name):
        """
        This method returns this 'enum' YTAEnum item instance if the
        provided 'name' is a valid name of that 'enum' YTAEnum class,
        or raises an Exception if not.
        """
        return from_name(name, cls)
    
    @classmethod
    def value_to_enum(cls, value):
        """
        This method returns the 'enum' YTAEnum item instance if the
        provided 'value' is a valid value of that 'enum' YTAEnum class,
        or raises an Exception if not.
        """
        return from_value(value, cls)
    
    @classmethod
    def name_or_value_to_enum(cls, name_or_value):
        """
        This method returns this 'enum' YTAEnum item instance if the
        provided 'name_or_value' is a valid name or a valid value of
        that 'enum' YTAEnum class, or raises an Exception if not.
        """
        return from_name_or_value(name_or_value, cls)
    
    @classmethod
    def to_enum(cls, name_or_value_or_enum):
        """
        This method returns this 'enum' YTAEnum item instance if the
        provided 'name_or_value_or_enum' is a valid name, a valid
        value or a valid instance of this 'enum' YTAEnum class, or
        raises an Exception if not.
        """
        return from_name_or_value_or_enum(name_or_value_or_enum, cls)

    @classmethod
    def get_all(cls):
        """
        This method returns all the existing items in this 'cls' Enum
        class.
        """
        return get_all(cls)
    
    @classmethod
    def get_all_names(cls):
        """
        This method returns all the names of the existing items in
        this 'cls' Enum class.
        """
        return get_all_names(cls)

    @classmethod
    def get_all_values(cls):
        """
        This method returns all the values of the existing items in 
        this 'cls' Enum class.
        """
        return get_all_values(cls)
    
    @classmethod
    def get_all_values_as_str(cls):
        """
        This method returns all the values of the existing items as
        strings separated by commas. This is useful to show the 
        accepted values of an Enum.
        """
        return get_values_as_str(cls.get_all())
    
    @classmethod
    def get_all_names_as_str(cls):
        return get_names_as_str(cls.get_all())
    
    @classmethod
    def get_valid_name(cls, name: str):
        """
        This method will ignore cases to look for the provided 'name'
        as a valid name of the provided 'enums'. This method is useful
        when user provided us a name and we want to obtain the actual
        Enum name to be able to instantiate it, but maybe user provided
        'name' is quite different, invalid for instantiating but valid
        for our logic.

        This method returns None if the provided 'name' is not a valid
        name for this Enum class.
        """
        names = cls.get_all_names()

        try:
            return names[[enum_name.lower() for enum_name in names].index(name.lower())]
        except Exception:
            return None
        
    @classmethod
    def get_random(cls):
        """
        Returns one of the available Enums randomly chosen.
        """
        return rand_choice(cls.get_all())





def is_enum(cls: Enum):
    """
    This method returns True if the provided 'cls' parameter is
    an enum class or subclass.
    """
    return isinstance(cls, Enum) or issubclass(cls, (Enum, YTAEnum))

def is_valid(name_or_value_or_enum: any, enum: YTAEnum):
    """
    Returns True if the provided 'name_or_value_or_enum' is
    a valid name or a valid value of the also provided 'enum'
    YTAEnum object, or even if it is an YTAEnum instance of
    that 'enum' YTAEnum class, or False if not.

    This method returns True or False.
    """
    ParameterValidator.validate_mandatory_parameter('name_or_value_or_enum', name_or_value_or_enum)
    ParameterValidator.validate_is_enum_class(enum)

    return isinstance(name_or_value_or_enum, enum) or is_valid_name(name_or_value_or_enum, enum) or is_valid_value(name_or_value_or_enum, enum)

def is_valid_name_or_value(name_or_value: any, enum: YTAEnum):
    """
    Returns True if the provided 'name_or_value' is a valid
    name or a valid value of the also provided 'enum' YTAEnum 
    object, or False if not.

    This method returns True or False.
    """
    ParameterValidator.validate_mandatory_parameter('name_or_value', name_or_value)
    ParameterValidator.validate_is_enum_class(enum)

    return is_valid_name(name_or_value) or is_valid_value(name_or_value)

def is_valid_name(name: any, enum: YTAEnum, ignore_case: bool = False):
    """
    Returns True if the provided 'name' is a valid name of
    the also provided 'enum' YTAEnum object, or False if not.

    This method returns True or False.
    """
    ParameterValidator.validate_mandatory_parameter('name', name)
    ParameterValidator.validate_is_enum_class(enum)

    if not ignore_case:
        try:
            enum[name]

            return True
        except Exception:
            return False
    else:
        names = get_all_names()
        try:
            names[[enum_name.lower() for enum_name in names].index(name.lower())]

            return True
        except Exception:
            return False
    
def is_valid_value(value: any, enum: YTAEnum):
    """
    Returns True if the provided 'value' is a valid value of
    the also provided 'enum' YTAEnum object.

    This method returns True or False.
    """
    ParameterValidator.validate_mandatory_parameter('value', value)
    ParameterValidator.validate_is_enum_class(enum)

    try:
        enum(value)

        return True
    except Exception:
        return False
    
def from_name(name: any, enum: YTAEnum, ignore_case: bool = False):
    """
    This method returns the 'enum' YTAEnum item instance if the
    provided 'name' is a valid name of that 'enum' YTAEnum class,
    or raises an Exception if not.
    """
    if is_valid_name(name, enum, ignore_case):
        return enum[name]
    
    raise Exception(ErrorMessage.parameter_is_not_name_of_ytaenum_class(name, enum))

def from_value(value: any, enum: YTAEnum):
    """
    This method returns the 'enum' YTAEnum item instance if the
    provided 'value' is a valid value of that 'enum' YTAEnum class,
    or raises an Exception if not.
    """
    if is_valid_value(value, enum):
        return enum(value)
    
    raise Exception(ErrorMessage.parameter_is_not_value_of_ytaenum_class(value, enum))

def from_name_or_value(name_or_value: any, enum: YTAEnum):
    """
    This method returns the 'enum' YTAEnum item instance if the
    provided 'name_or_value' is a valid name or a valid value of
    that 'enum' YTAEnum class, or raises an Exception if not.
    """
    if is_valid_name(name_or_value, enum):
        return enum[name_or_value]
    elif is_valid_value(name_or_value, enum):
        return enum(name_or_value)
    
    raise Exception(ErrorMessage.parameter_is_not_name_nor_value_of_ytaenum_class(name_or_value, enum))

def from_name_or_value_or_enum(name_or_value_or_enum: any, enum: YTAEnum):
    """
    This method returns the 'enum' YTAEnum item instance if the
    provided 'name_or_value_or_enum' is a valid name, a valid
    value or a valid instance of that 'enum' YTAEnum class, or
    raises an Exception if not.
    """
    if isinstance(name_or_value_or_enum, enum):
        return name_or_value_or_enum
    elif is_valid_name(name_or_value_or_enum, enum):
        return enum[name_or_value_or_enum]
    elif is_valid_value(name_or_value_or_enum, enum):
        return enum(name_or_value_or_enum)
    
    raise Exception(ErrorMessage.parameter_is_not_name_nor_value_nor_enum_of_ytaenum_class(name_or_value_or_enum, enum))
    
def is_name_or_value(name_or_value: any, enum: YTAEnum):
    """
    This method validates if the provided 'value' is a name
    or a value of the also provided 'enum' YTAEnum, raising
    an Exception if not.

    This method returns the enum item (containing .name and
    .value) if it is valid.
    """
    ParameterValidator.validate_mandatory_parameter('name_or_value', name_or_value)
    ParameterValidator.validate_is_enum_class(enum)

    if name_or_value in enum.get_all_names():
        return enum[name_or_value]
    elif name_or_value in enum.get_all_values():
        return enum(name_or_value)
    
    raise Exception(ErrorMessage.parameter_is_not_name_nor_value_of_ytaenum_class(name_or_value, enum))
    
def get_all(enum: Enum):
    """
    This method returns all the items defined in a Enum subtype that
    is provided as the 'enum' parameter.
    """
    if not enum:
        raise Exception('No "enum" provided.')
    
    if not isinstance(enum, Enum) and not issubclass(enum, Enum):
        raise Exception('The "enum" parameter provided is not an Enum.')
    
    return [item for item in enum]

def get_all_names(cls):
    """
    Returns a list containing all the registered enum names.
    """
    return [item.name for item in get_all(cls)]

def get_all_names_as_str(cls):
    """
    Returns a string containing all the enums of the provided
    YTAEnum 'cls' class names separated by commas.
    """
    return get_names_as_str(get_all(cls))

def get_all_values(cls):
    """
    Returns a list containing all the registered enum values.
    """
    return [item.value for item in get_all(cls)]

def get_all_values_as_str(cls):
    """
    Returns a string containing all the enums of the provided
    YTAEnum 'cls' class values separated by commas.
    """
    return get_values_as_str(get_all(cls))

def get_names(enums: list[Enum]):
    """
    Returns a list containing all the names of the provided
    'enums' Enum elements.
    """
    if any(not is_enum(enum) for enum in enums):
        raise TypeError('At least one of the given "enums" is not an Enum class or subclass.')    
    
    return [item.name for item in enums]

def get_names_as_str(enums: list[YTAEnum]):
    """
    Returns a string containing the provided 'enums' names separated
    by commas.
    """
    if any(not is_enum(enum) for enum in enums):
        raise TypeError('At least one of the given "enums" is not an Enum class or subclass.')    
    
    return ', '.join(get_names(enums))

def get_values(enums: list[Enum]):
    """
    Returns a list containing all the values of the provided
    'enums' Enum elements.
    """
    if any(not is_enum(enum) for enum in enums):
        raise TypeError('At least one of the given "enums" is not an Enum class or subclass.')    
     
    return [item.value for item in enums]

def get_values_as_str(enums: Enum):
    """
    Returns a string containing the provided 'enums' values separated
    by commas.
    """
    if any(not is_enum(enum) for enum in enums):
        raise TypeError('At least one of the given "enums" is not an Enum class or subclass.')    
     
    return ', '.join(get_values(enums))