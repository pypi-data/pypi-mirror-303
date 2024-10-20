from yta_general_utils.programming.error_message import ErrorMessage
from yta_general_utils.file.filename import filename_is_type, FileType
from yta_general_utils.checker.type import variable_is_positive_number
from yta_general_utils.file.checker import file_exists
from yta_general_utils.checker.url import url_is_ok
from enum import Enum
from typing import Union


class ParameterValidator:
    @classmethod
    def validate_mandatory_parameter(cls, name: str, value):
        """
        Validates if the provided 'value' parameter with the also
        provided 'name' has a value, raising an Exception if not.

        This method returns the provided 'value' if everything is
        ok.
        """
        if not value:
            raise Exception(ErrorMessage.parameter_not_provided(name))

        return value
        
    @classmethod
    def validate_string_parameter(cls, name: str, value: str):
        """
        Validates if the provided 'value' parameter with the also
        provided 'name' is a string value, raising an Exception if
        not.

        This method returns the provided 'value' if everything is
        ok.
        """
        if not isinstance(value, str):
            raise Exception(ErrorMessage.parameter_is_not_string(name))

        return value

    @classmethod
    def validate_bool_parameter(cls, name: str, value: bool):
        """
        Validates if the provided 'value' parameter with the also
        provided 'name' is a boolean value, raising and Exception 
        if not.

        This method returns the provided 'value' if everything is
        ok.
        """
        if not isinstance(value, bool):
            raise Exception(ErrorMessage.parameter_is_not_boolean(name))

        return value
        
    @classmethod
    def validate_file_exists(cls, name: str, value: str):
        """
        Validates if the provided 'value' parameter with the also
        provided 'name' is a file that actually exists, raising
        an Exception if not.

        This method returns the provided 'value' if everything is
        ok.
        """
        if not file_exists(value):
            raise Exception(ErrorMessage.parameter_is_file_that_doesnt_exist(name))

        return value
        
    @classmethod
    def validate_filename_is_type(cls, name: str, value: str, file_type: FileType = FileType.IMAGE):
        """
        Validates if the provided 'value' parameter with the also
        provided 'name' is a filename of the given 'file_type',
        raising an Exception if not.

        This method returns the provided 'value' if everything is
        ok.
        """
        if not filename_is_type(value, file_type):
            raise Exception(ErrorMessage.parameter_is_not_file_of_file_type(name, file_type))

        return value
        
    @classmethod
    def validate_url_is_ok(cls, name: str, value: str):
        """
        Validates if the provided 'value' parameter with the also
        provided 'name' is a valid url (the url is accessible),
        raising an Exception if not.

        This method returns the provided 'value' if everything is
        ok.
        """
        if not url_is_ok(value):
            raise Exception(ErrorMessage.parameter_is_not_valid_url(name))

        return value
        
    @classmethod
    def validate_positive_number(cls, name: str, value: Union[int, float]):
        """
        Validates if the provided 'value' parameter with the also
        provided 'name' is a positive number (0 or greater),
        raising an Exception if not.

        This method returns the provided 'value' as it is if 
        everything is ok.
        """
        if not variable_is_positive_number(value):
            raise Exception(ErrorMessage.parameter_is_not_positive_number(name))

        return value

    @classmethod
    def validate_is_class(cls, name: str, value, class_names: Union[list[str], str]):
        """
        Validates if the provided 'value' is one of the provided 'class_names'
        by using the 'type(value).__name__' checking.

        This method returns the 'value' as it is if everything is ok.
        """
        if isinstance(class_names, str):
            class_names = [class_names]

        if not type(value).__name__ in class_names:
            raise Exception(ErrorMessage.parameter_is_not_class(name, class_names))
        
        return value
        
    # Complex ones below
    @classmethod
    def validate_string_mandatory_parameter(cls, name: str, value: str):
        """
        Validates if the provided 'value' is a valid and non
        empty string.
        """
        cls.validate_mandatory_parameter(name, value)
        cls.validate_string_parameter(name, value)

        return value

    @classmethod
    def validate_numeric_positive_mandatory_parameter(cls, name: str, value: str):
        """
        Validates if the provided 'value' is a positive numeric
        value.
        """
        cls.validate_mandatory_parameter(name, value)
        cls.validate_positive_number(name, value)

        return value
    
    @classmethod
    def validate_is_enum_class(cls, enum: Union['YTAEnum', Enum]):
        """
        Validates if the provided 'value' is a valid Enum
        class or subclass.

        This method will raise an Exception if the provided
        'value' is not a valid Enum class or subclass, or
        will return it as it is if yes.
        """
        if not isinstance(enum, Enum) and not issubclass(enum, Enum):
            raise Exception(f'The parameter "{enum}" provided is not an Enum class or subclass.')
        
        return enum

    @classmethod
    def validate_enum(cls, value: Union['YTAEnum', str], enum: 'YTAEnum'):
        """
        Validates if the provided 'value' value is a valid
        Enum or Enum value of the also provided 'enum' class.

        This method will raise an Exception if something is
        wrong or will return the 'value' as an 'enum' Enum.
        instance if everything is ok.
        """
        cls.validate_mandatory_parameter('value', value)
        cls.validate_is_enum_class(enum)
        cls.validate_is_class('value', value, [enum.__class__.__name__, 'str'])

        return enum.to_enum(value)