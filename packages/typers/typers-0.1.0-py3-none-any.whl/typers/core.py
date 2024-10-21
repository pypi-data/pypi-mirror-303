from .Exceptions.validate_error import ValidateError

class Valid:
    """A utility class for performing various validation checks on values.

    The `Valid` class provides static methods to validate data types, ranges, lengths, and custom validations.
    It is useful for ensuring that function arguments or values passed to a program are of the expected type or structure.
    
    The methods raise a `ValueError` if validation fails, and some methods may raise a `ValidateError`
    if there are issues with the parameters (e.g., a missing or invalid 'name' argument).
    
    Validation types include:
    - Non-null checks
    - Strings, integers, floats, and booleans
    - Lists, tuples, sets, and dictionaries
    - Ranges and length validation
    - Custom validations using user-defined functions
    """
    # ------------------ Not None ------------------ #
    @staticmethod
    def _not_none(value, name: str = None):
        """Validate that the given value is not None.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is None.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if value is None:
            raise ValueError(f"The '{name}' argument cannot be None.")

    # ------------------ Strings ------------------- #
    @staticmethod
    def _string(value, name: str = None):
        """Validate that the given value is a string.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a string.
            ValidateError: If the name is None.
        """
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, str):
            raise ValueError(f"The '{name}' argument must be a string.")

    # ------------------ Integers ------------------ #
    @staticmethod
    def _integer(value, name: str = None):
        """Validate that the given value is an integer.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not an integer.
            ValidateError: If the name is None.
        """
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int):
            raise ValueError(f"The '{name}' argument must be an integer.")

    @staticmethod
    def _positive_int_in(value, name: str = None):
        """Validate that the given value is a positive integer (greater than zero).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a positive integer.
            ValidateError: If the name is None.
        """
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"The '{name}' argument must be a positive integer.")

    @staticmethod
    def _positive_int_out(value, name: str = None):
        """Validate that the given value is a non-negative integer (zero or greater).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a non-negative integer.
            ValidateError: If the name is None.
        """
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"The '{name}' argument must be a positive integer excluding 0.")


    @staticmethod
    def _negative_int_in(value, name: str = None):
        """Validate that the given value is a negative integer (less than zero).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a negative integer.
            ValidateError: If the name is None.
        """
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value >= 0:
            raise ValueError(f"The '{name}' argument must be a negative integer.")

    @staticmethod
    def _negative_int_out(value, name: str = None):
        """Validate that the given value is a non-positive integer (zero or less).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a non-positive integer.
            ValidateError: If the name is None.
        """
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value > 0:
            raise ValueError(f"The '{name}' argument must be a negative integer excluding 0.")

    # ------------------ Floats --------------+----- #
    @staticmethod
    def _float(value, name: str = None):
        """Validate that the given value is a float.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a float.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float):
            raise ValueError(f"The '{name}' argument must be a float.")

    @staticmethod
    def _positive_float_in(value, name: str = None):
        """Validate that the given value is a positive float (greater than zero).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a positive float.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value <= 0:
            raise ValueError(f"The '{name}' argument must be a positive float.")

    @staticmethod
    def _positive_float_out(value, name: str = None):
        """Validate that the given value is a non-negative float (zero or greater).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a non-negative float.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"The '{name}' argument must be a positive float excluding 0.")

    @staticmethod
    def _negative_float_in(value, name: str = None):
        """Validate that the given value is a negative float (less than zero).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a negative float.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value >= 0:
            raise ValueError(f"The '{name}' argument must be a negative float.")

    @staticmethod
    def _negative_float_out(value, name: str = None):
        """Validate that the given value is a non-positive float (zero or less).

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a non-positive float.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value > 0:
            raise ValueError(f"The '{name}' argument must be a negative float excluding 0.")

    # ------------------ Booleans ------------------ #
    @staticmethod
    def _boolean(value, name: str = None):
        """Validate that the given value is a boolean.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a boolean.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, bool):
            raise ValueError(f"The '{name}' argument must be a boolean.")

    # ------------------- Lists -------------------- #
    @staticmethod
    def _list(value, name: str = None):
        """Validate that the given value is a list.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a list.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list):
            raise ValueError(f"The '{name}' argument must be a list.")

    @staticmethod
    def _list_of_strings(value, name: str = None):
        """Validate that the given value is a list of strings.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a list of strings.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of strings.")
    
    @staticmethod
    def _list_of_ints(value, name: str = None):
        """Validate that the given value is a list of integers.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a list of integers.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of integers.")

    @staticmethod
    def _list_of_floats(value, name: str = None):
        """Validate that the given value is a list of floats.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a list of floats.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of floats.")

    @staticmethod
    def _list_of_bools(value, name: str = None):
        """Validate that the given value is a list of booleans.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a list of booleans.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of booleans.")
    
    # ------------------ Ranges -------------------- #
    @staticmethod
    def _in_range(value, min_val, max_val, name: str = None):
        """Validate that the value is within a specified range [min_val, max_val].

        Args:
            value: The value to check.
            min_val: The minimum allowed value.
            max_val: The maximum allowed value.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not within the range.
            ValidateError: If the name is None or if min_val is greater than or equal to max_val.
        """
        if min_val >= max_val:
            raise ValidateError("The 'min_val' argument cannot be bigger or equal to the 'max_val' argument.")
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, (int, float)) or not (min_val <= value <= max_val):
            raise ValueError(f"The '{name}' argument must be between {min_val} and {max_val}.")

    # ------------------ Tuples -------------------- #
    @staticmethod
    def _tuple(value, name: str = None):
        """Validate that the given value is a tuple.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a tuple.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple):
            raise ValueError(f"The '{name}' argument must be a tuple.")

    @staticmethod
    def _tuple_of_strings(value, name: str = None):
        """Validate that the given value is a tuple of strings.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a tuple of strings.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of strings.")

    @staticmethod
    def _tuple_of_ints(value, name: str = None):
        """Validate that the given value is a tuple of integers.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a tuple of integers.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of integers.")

    @staticmethod
    def _tuple_of_floats(value, name: str = None):
        """Validate that the given value is a tuple of floats.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a tuple of floats.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of floats.")

    @staticmethod
    def _tuple_of_bools(value, name: str = None):
        """Validate that the given value is a tuple of booleans.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a tuple of booleans.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of booleans.")

    # ------------------ Sets ---------------------- #
    @staticmethod
    def _set(value, name: str = None):
        """Validate that the given value is a set.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a set.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set):
            raise ValueError(f"The '{name}' argument must be a set.")
    
    @staticmethod
    def _set_of_strings(value, name: str = None):
        """Validate that the given value is a set of strings.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a set of strings.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, string) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of strings.")

    @staticmethod
    def _set_of_ints(value, name: str = None):
        """Validate that the given value is a set of integers.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a set of integers.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of integers.")

    @staticmethod
    def _set_of_floats(value, name: str = None):
        """Validate that the given value is a set of floats.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a set of floats.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of floats.")

    @staticmethod
    def _set_of_bools(value, name: str = None):
        """Validate that the given value is a set of booleans.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a set of booleans.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of booleans.")

    # ------------------ Dictionaries -------------- #
    @staticmethod
    def _dict(value, name: str = None):
        """Validate that the given value is a dictionary.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a dictionary.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, dict):
            raise ValueError(f"The '{name}' argument must be a dictionary.")

    @staticmethod
    def _dict_of_strings(value, name: str = None):
        """Validate that the given value is a dictionary with string keys and values.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a dictionary of string keys and values.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in value.items()):
            raise ValueError(f"The '{name}' argument must be a dictionary of string keys and values.")
  
    # ------------------ Length -------------------- #
    @staticmethod
    def _length(value, expected_length, name: str = None):
        """Validate that the value has a specific length.

        Args:
            value: The value to check.
            expected_length: The expected length.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value does not have the expected length.
            ValidateError: If the name is None or expected_length is negative.
        """
        if expected_length < 0:
            raise ValidateError("The 'excepted_length' argument must be a positive integer.")
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not hasattr(value, '__len__') or len(value) != expected_length:
            raise ValueError(f"The '{name}' argument must have a length of {expected_length}.")

    # ------------------ Custom types -------------- #
    @staticmethod
    def _type(value, expected_type, name: str = None):
        """Validate that the value matches the expected type.

        Args:
            value: The value to check.
            expected_type: The expected type.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value does not match the expected type.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, expected_type):
            raise ValueError(f"The '{name}' argument must be of type {expected_type.__name__}.")

    # ------------------ Optionals ----------------- #
    @staticmethod
    def _optional(value, expected_type, name: str = None):
        """Validate that the value is either None or matches the expected type.

        Args:
            value: The value to check.
            expected_type: The expected type if value is not None.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is neither None nor the expected type.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if value is not None and not isinstance(value, expected_type):
            raise ValueError(f"The '{name}' argument must be None or of type {expected_type.__name__}.")

    # ------------------ Enums --------------------- #
    @staticmethod
    def _enum(value, options, name: str = None):
        """Validate that the value is one of the specified options.

        Args:
            value: The value to check.
            options: A list of valid options.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not one of the options.
            ValidateError: If the name is None or options are invalid.
        """
        if not isinstance(options, list) or len(options) == 0:
            raise ValidateError("The 'options' argument must be a list.")
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if value not in options:
            raise ValueError(f"The '{name}' argument must be one of {options}.")

    # ------------------ Non-empty strings --------- #
    @staticmethod
    def _non_empty_string(value, name: str = None):
        """Validate that the value is a non-empty string.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a non-empty string.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"The '{name}' argument must be a non-empty string.")

    # ------------------ Non-empty lists ----------- #
    @staticmethod
    def _non_empty_list(value, name: str = None):
        """Validate that the value is a non-empty list.

        Args:
            value: The value to check.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the value is not a non-empty list.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or len(value) == 0:
            raise ValueError(f"The '{name}' argument must be a non-empty list.")

    # ------------------ Custom -------------------- #
    @staticmethod
    def _custom(value, validation_func, name: str = None):
        """Perform custom validation using a provided function.

        Args:
            value: The value to check.
            validation_func: A function that takes the value and returns True if valid, False otherwise.
            name: The name of the argument (for error messages).

        Raises:
            ValueError: If the custom validation fails.
            ValidateError: If the name is None.
        """
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not validation_func(value):
            raise ValueError(f"The '{name}' argument failed custom validation.")
