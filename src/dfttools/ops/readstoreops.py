from typing import Union
from ..enum import Enum
from . import TestOperation
import json
from . import Instructions

class ReadStoreTestOperation(Enum):
    """
    Base class for read-store test operations, inheriting from Enum.
    """
    READREG_STORE = Instructions.READREG_STORE

    def __init__(self, t: int, field_name: str, variable: str, restore: bool = False, comment: str = None):
        """
        Initializes a ReadStoreTestOperation.

        Args:
            t (int): The type of test operation.
            field_name (str): The name of the field to store.
            variable (str): The variable to associate with the field name.
            restore (bool): Indicates whether to restore the variable. Defaults to False.
            comment (str, optional): A comment for the operation. Defaults to None.

        Raises:
            ValueError: If either field_name or variable is not a string.
        """
        if not isinstance(field_name, str):
            raise ValueError("field_name must be a string.")
        if not isinstance(variable, str):
            raise ValueError("variable must be a string.")

        self._t = t  # Set the operation type
        self._field_name = field_name
        self._variable = variable
        self._restore = restore  # Store the restore flag
        self._comment = comment

        # Initialize Enum with the enum value and name
        super().__init__(t, zip(Instructions.values(), Instructions.keys()))

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': self._t,
            'field_name': self._field_name,
            'variable': self._variable,
            'restore': self._restore,  # Include restore in the dictionary
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())

class ReadStoreOperation(ReadStoreTestOperation):
    """
    Concrete class inheriting from ReadStoreTestOperation.
    """
    def __init__(self, field_name: str, variable: str, restore: bool = False, comment: str = None):
        """
        Initializes a ReadStoreOperation.

        Args:
            field_name (str): The name of the field to store.
            variable (str): The variable to associate with the field name.
            restore (bool): Indicates whether to restore the variable. Defaults to False.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(Instructions.READREG_STORE, field_name, variable, restore, comment)

    def __repr__(self):
        """
        Returns a string representation of the ReadStoreOperation object.

        Returns:
            str: A human-readable string representation.
        """
        if self._restore:
            return f"Variable data {self._variable} restored to register field {self._field_name}, comment={self._comment}"
        else:
            return f"Read field data {self._field_name}, and store in variable {self._variable}, comment={self._comment}"

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values including inherited attributes.
        """
        return {
            **super().to_dict(),  # Call parent method and include its data
            # Add any additional attributes if needed (none in this case)
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values including inherited attributes.
        """
        return json.dumps(self.to_dict())

