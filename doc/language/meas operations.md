# MEAS and WAIT Operations Module

## Overview

This module provides a structured and extensible foundation for defining and managing test operations within a testing framework. It includes a base enumeration (`TestOperation`) and specialized classes for different types of operations, like wait operations, voltage measurements, current measurements, resistance measurements, and frequency measurements. The module facilitates configuration, data representation, and serialization of operation data for storage or transmission.

## Module Contents

### 1. `Instructions` (Simulated Class)

The `Instructions` class is a placeholder that simulates an actual set of instructions that a testing environment might use. In a real-world scenario, this would likely be imported from another module.

### 2. `TestOperation` (Enum)

The `TestOperation` class is an enumeration (inheriting from `enum.Enum`) that serves as the foundation for all specific test operation types. It encapsulates the core attributes and methods shared by various test operations.

#### Key Features:

-   **Initialization (`__init__`)**: 
    -   Sets up the basic parameters for each test operation.
    -   Accepts parameters such as the operation type (`t`), primary signal (`signal1`), secondary signal (`signal2`), a comment, and additional keyword arguments.
  
-   **Attributes**:
    -   `_t`: The type of test operation (integer).
    -   `_signal1`: The primary signal associated with the operation (string, optional).
    -   `_signal2`: The secondary signal or reference (string, optional).
    -   `_unit`: The unit of measurement for the operation (Enum, optional).
    -   `_comment`: An optional comment describing the operation (string).
    -   `_variable`: An optional variable associated with the operation (string).

-   **Serialization**:
    -   `to_dict()`: Converts the operation's attributes into a dictionary format, facilitating data representation and manipulation.
    -   `to_json()`: Converts the operation's attributes into a JSON string format, enabling data storage and transmission.

### 3. Specialized Test Operation Classes

These classes inherit from `TestOperation` and represent specific types of test operations, extending the base class with operation-specific functionality.

#### Common Features:

-   **Inheritance**: Each class inherits attributes and methods from `TestOperation`.
-   **String Representation (`__repr__`)**:  Returns a human-readable string describing the test operation, including signal details, unit, and comment. This method is implemented to output relevant data .
-   **Initialization (`__init__`)**: Calls the superclass's initialization to set common parameters while defining specific ones for each test type.
-   **Serialization**: Methods to serialize the object's data into dictionaries and JSON strings.

#### Class-Specifics:

1.  **`WaitOperation`**:

    -   Represents a wait operation that introduces a delay in the test sequence. It inherits from `TestOperation`.

    -   **Initialization (`__init__`)**:
        -   Sets up a wait operation with a specified `unit` (for the time duration) and `delay` (the amount of time to wait).

    -   **Attributes**:

        -   `delay`: The duration of the wait (Union[int, float]).

    -   **String Representation (`__repr__`)**:

        -   Provides a human-readable representation of the wait operation, showing the delay and its unit. For example: `"time delay, 5Second"`.

    -   **Serialization**:

        -   Overrides `to_dict()` to include the `delay` attribute in the dictionary representation.

2.  **Measurement Operations (VoltageMeasOperation, CurrentMeasOperation, ResistanceMeasOperation, FrequencyMeasOperation)**:

    -   Represent measurement operations, inheriting from `TestOperation` and extending it for voltage, current, resistance, and frequency measurements.

    -   **Initialization (`__init__`)**:

        -   Sets up a measurement operation with a specific `unit`, `signal`, `reference` (defaulting to 'GND'), `variable` (where to store the measurement), and an optional `comment`.

    -   **Attributes**:

        -   These operations inherit attributes from `TestOperation`, utilizing `signal1` for the signal being measured and `signal2` for the reference.

    -   **String Representation (`__repr__`)**:

        -   Provides a descriptive string representation of the measurement operation, including the signal, reference, unit, and the variable where the result will be stored (if specified).
        -   For example, a voltage measurement might look like: `"voltage measurement: VOUT wrt GND, unit: Volt savemeas to : voltage_value ( Measure voltage )"`.

    -   **Serialization**:

        -   Overrides `to_dict()` to include relevant attributes like the signal, reference, unit, variable, and comment in the dictionary representation.

#### Summary of Measurement Operations
The measurement classes follow a similar design pattern, and each class is similar to the `VoltageMeasOperation` and all of the Classes listed below can easily be made to match the VoltageMeasOperation class.
*   `VoltageMeasOperation` is used to represent measurement of the voltage signal.
*   `CurrentMeasOperation` is used to represent measurement of the current signal.
*   `ResistanceMeasOperation` is used to represent measurement of the resistance signal.
*   `FrequencyMeasOperation` is used to represent measurement of the clock signal.

### 4. Module Dependencies

-   `json`: For JSON serialization and deserialization.
-   `typing`: For type hinting and specifying variable types.
-   `enum`: For creating enumerations, allowing the module to define a set of named values.

### 5. Best Practices
*   Utilize the to\_dict and to\_json to log information about the code and test various senarios.


