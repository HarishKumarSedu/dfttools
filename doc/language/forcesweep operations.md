# Force Sweep Test Operations Module

## Overview

This module provides a structured approach to managing force sweep test operations. It includes a base class (`ForceSweepTestOperation`) and specialized classes for different sweep types (voltage, current, resistance, and clock frequency). The module uses enums and inheritance to define the structure and behavior of these operations.

## Module Contents

### 1. `Instructions` (Mock Class)

This class simulates an instructions set. In a real-world scenario, these instructions would likely be imported from another module to define available test operations.

### 2. `ForceSweepTestOperation` (Enum)

The base class for all force sweep operations, inheriting from `enum.Enum`. It defines common attributes and methods used by all specific sweep types.

#### Key Features:

-   **Initialization (`__init__`)**: Sets up the basic parameters for a sweep operation, including signals, units, values, and timing.
-   **Attributes**:
    -   `_unit`: The unit of measurement for the sweep.
    -   `_signal1`: The primary signal being swept.
    -   `_signal2`: The secondary/reference signal.
    -   `_initialvalue`: The starting value for the sweep.
    -   `_finalvalue`: The ending value for the sweep.
    -   `_stepsize`: The increment/decrement step size.
    -   `_stepunit`: The unit for the step size.
    -   `_timestep`: The time between steps.
    -   `_timestepunit`: The unit for the time step.
-   **Serialization**:
    -   `to_dict()`: Converts the operation's attributes to a dictionary.
    -   `to_json()`: Converts the operation's attributes to a JSON string.

### 3. Specialized Force Sweep Classes (Voltage, Current, Resistance, Clock)

These classes inherit from `ForceSweepTestOperation` and implement specific types of force sweep operations.

#### Common Features:

-   **Inheritance**: Each class inherits attributes and methods from `ForceSweepTestOperation`.
-   **Initialization (`__init__`)**: Calls the superclass's initialization and sets specific parameters for that sweep type (e.g., voltage-related arguments for `VoltageForceSweepOperation`).
-   **String Representation (`__repr__`)**: Provides a human-readable string describing the sweep operation, including signal details, range, and step information.
-   **Serialization**:
    -   `to_dict()`: Updates the base dictionary with the specific sweep type.
    -   `to_json()`: Converts the dictionary to a JSON string.

#### Class-Specifics:

-   **`VoltageForceSweepOperation`**: Manages voltage sweeps.
-   **`CurrentForceSweepOperation`**: Manages current sweeps.
-   **`ResistanceForceSweepOperation`**: Manages resistance sweeps.
-   **`ClockForceSweepOperation`**: Manages clock frequency sweeps.

### 4. Relationship Between Classes

The `ForceSweepTestOperation` acts as a blueprint, offering a consistent way to handle sweep configurations. The specialized classes then extend this blueprint with their unique specifications, all while maintaining the ability to serialize to dictionaries and JSON for easy configuration and data storage.

## Dependencies

-   `enum`
-   `typing`
-   `json`
