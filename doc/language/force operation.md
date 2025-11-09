# FORCE Operations Module

## Overview

This module provides a structured and extensible foundation for defining and managing test operations within a testing framework. It includes a base enumeration (`TestOperation`) and a mechanism for associating instruction codes with operation types. The module emphasizes configurability and facilitates serialization of operation data for storage or transmission.

## Module Contents

### 1. Instruction Mapping

The module begins by defining a set of instructions and their corresponding integer codes. These codes represent different types of test operations.

#### Key Components:

-   **`instructions_dict`**: This dictionary maps instruction names (strings) to their corresponding integer codes. These instruction names represent different types of test operations, such as:
    -   `'WAIT'`: Represents a wait operation.
    -   `'MEAS'`: Represents a measurement operation.
    -   `'FORCE'`: Represents a force operation.
    -   `'REGOP'`: Represents a register operation.
    -   `'FORCESWEEP'`: Represents a force sweep operation.
    -   `'READREG_STORE'`: Represents an operation to read from a register and store the value.
    -   `'COPYREG_TO_REG'`: Represents an operation to copy data from one register to another.
    -   `'RESTOREREG_FRO_MVAR'`: Represents an operation to restore a register value from a variable.
    -   `'MEAS_MATCH'`: Represents a measurement match operation.

    ```
    instructions_dict = {'WAIT':0,
                         'MEAS':1,
                         'FORCE':2,
                         'REGOP':3,
                         'FORCESWEEP':4,
                         'READREG_STORE':5,
                         'COPYREG_TO_REG':6,
                         'RESTOREREG_FRO_MVAR':7,
                         'MEAS_MATCH':8
                         }
    ```

-   **`Instructions`**: A `Box` object is created from the `instructions_dict`. The `Box` object provides attribute-style access to the dictionary values, making it more convenient to retrieve the instruction codes. For example, instead of writing `instructions_dict['WAIT']`, you can use `Instructions.WAIT`. This enhances code readability.

    ```
    Instructions = Box(instructions_dict)
    ```

### 2. `TestOperation` (Enum)

The `TestOperation` class is an enumeration (inheriting from `enum.Enum`) that serves as the foundation for all specific test operation types. It encapsulates the core attributes and methods shared by various test operations.

#### Key Features:

-   **Enumeration Members**:
    -   `MEAS`: Assigned the integer code from `Instructions.MEAS` to represent a measurement operation.
    -   `WAIT`: Assigned the integer code from `Instructions.WAIT` to represent a wait operation.
    -   `FORCE`: Assigned the integer code from `Instructions.FORCE` to represent a force operation.
    -   `REGOP`: Assigned the integer code from `Instructions.REGOP` to represent a register operation.

    ```
    class TestOperation(Enum):
        MEAS  = Instructions.MEAS
        WAIT  = Instructions.WAIT
        FORCE = Instructions.FORCE
        REGOP = Instructions.REGOP
    ```

-   **Initialization (`__init__`)**: The constructor for the `TestOperation` class. It's used to set up the basic parameters for each specific test operation.

    -   **Purpose**:
        -   Initializes a `TestOperation` instance.
        -   Sets the operation type, signals, comment, unit, and variable based on the provided arguments.

    -   **Parameters**:
        -   `t` (int): The type of test operation, typically an instruction code from the `Instructions` object.
        -   `signal1` (str, optional): The primary signal associated with the operation. Defaults to `None`.
        -   `signal2` (str, optional): The secondary signal or reference. Defaults to `None`.
        -   `comment` (str, optional): An optional comment describing the operation. Defaults to an empty string.
        -   `**kwargs`: Additional keyword arguments. This allows passing extra parameters like `'unit'` and `'variable'` which are used in more specialized operations.

    -   **Implementation Details**:
        -   The constructor assigns the provided arguments to instance variables (e.g., `self._t`, `self._signal1`, `self._comment`).
        -   It retrieves the `'unit'` and `'variable'` values from the `kwargs` dictionary using the `get()` method, which allows for optional parameters without raising an error if they are not provided.
        -   `super().__init__(t, zip(Instructions.values(),Instructions.keys()))` :This initializes enum with a list of pairs and a type, allowing for the enum to function.

    ```
    def __init__(self, t: int, signal1: str = None, signal2: str = None,
                 comment: str = "", **kwargs):
        """
        Initializes a TestOperation.

        Args:
            t (int): The type of test operation.
            signal1 (str, optional): The primary signal. Defaults to None.
            signal2 (str, optional): The secondary signal. Defaults to None.
            comment (str, optional): A comment for the operation. Defaults to "".
            **kwargs: Additional keyword arguments, including 'unit' and 'variable'.
        """
        self._t = t
        self._unit = kwargs.get('unit', None)
        self._comment = comment
        self._signal1 = signal1
        self._signal2 = signal2
        self._variable = kwargs.get('variable', None)
        super().__init__(t, zip(Instructions.values(),Instructions.keys()))
    ```

-   **Serialization Methods**:

    -   `to_dict()`: This method converts the `TestOperation` instance into a dictionary, making it easier to work with the data programmatically or to serialize it into other formats.
        -   **Purpose**:
            -   Creates a dictionary representation of the `TestOperation`.
            -   This is useful for debugging, logging, or converting to other formats like JSON.

        -   **Returns**:
            -   `dict`: A dictionary containing the key attributes of the `TestOperation`.

        ```
        def to_dict(self) -> dict:
            """
            Returns the initialized values as a dictionary.

            Returns:
                dict: A dictionary representation of the initialized values.
            """
            return {
                'type': self._t,
                'signal1': self._signal1,
                'signal2': self._signal2,
                'unit': str(self._unit),
                'variable': self._variable,
                'comment': self._comment
            }
        ```

    -   `to_json()`: This method converts the `TestOperation` instance into a JSON string.
        -   **Purpose**:
            -   Serializes the `TestOperation` into a JSON string.
            -   JSON is a common format for data interchange, so this method is useful for transmitting `TestOperation` data over a network or storing it in a file.

        -   **Returns**:
            -   `str`: A JSON string representing the `TestOperation`.

        ```
        def to_json(self) -> str:
            """
            Returns the initialized values as a JSON string.

            Returns:
                str: A JSON string representation of the initialized values.
            """
            return json.dumps(self.to_dict())
        ```

### 3. Key Dependencies

The module relies on the following dependencies:

-   `json`: For JSON serialization.
-   `typing`: For type hinting (specifying variable types).
-   `enum`: For creating enumerations.
-   `collections`: This library is required because it facilitates looping through instruction values .
-   `box`:  A library that allows you to easily use dot notation on dictionaries (e.g., `my_box.key` instead of `my_dict['key']`).

