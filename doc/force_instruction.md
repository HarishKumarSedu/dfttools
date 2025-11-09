# dfttools Force Instruction

---

## Overview

The **dfttools** library provides a modular and extensible framework to control hardware forces such as voltage, current, resistance, and frequency. Similar to measurement instructions, **force instructions** apply specified values to hardware signals and rely on customizable callback functions to interface with the actual hardware.

All force instructions and configurations can be accessed via:

```python
from dfttools import *
```

Callback functions receive hardware meta data (signal, reference, value) and **must return a tuple** indicating hardware availability and the actual value applied or measured. This design allows users to tailor the library to their specific hardware setup.

---

## Key Features

- **Unified Global Context (`g`)** manages hardware state, output logs, and callback registrations.
- **Force Instructions (`VFORCE`, `AFORCE`, `RESFORCE`, `FREQFORCE`)** to apply voltage, current, resistance, and frequency forces.
- **Meta-driven Callback System**: Callbacks receive meta data and return `(hardware_available, value)`.
- **Output Logging**: All force operations are logged for traceability.
- **Extensible and Customizable**: Users implement hardware-specific callbacks.

---

## Code Structure and Analysis

### 1. Global Context (`glob/__init__.py`)

```python
class GlobalContext:
    """Global context for managing hardware availability and callback functions."""
    def __init__(self):
        self.output = []
        self.instructions = {}
        self.dut_description = None

        # Hardware availability flags
        self.voltage_force_hardware_available = False
        self.current_force_hardware_available = False
        self.resistance_force_hardware_available = False
        self.frequency_force_hardware_available = False

        # Callback functions for force and measurement
        self.hardware_callbacks = {
            'voltage_force': None,
            'current_force': None,
            'resistance_force': None,
            'frequency_force': None,
            'voltage_measure': None,
            'current_measure': None,
            'resistance_measure': None,
            'frequency_measure': None,
            'voltage_force_sweep': None,
            'current_force_sweep': None,
            'resistance_force_sweep': None,
            'frequency_force_sweep': None,
            'i2c_read': None,
            'i2c_write': None,
        }

    @property
    def callback_keys(self):
        return self.hardware_callbacks.keys()

g = GlobalContext()
```

**Analysis:**
This global context object (`g`) holds the callback registry and tracks hardware availability flags for force and measurement operations. It also stores output logs of all instructions executed.

---

### 2. Callback Functions for Force (`callbacks/force_callbacks.py`)

Example callback implementations simulating hardware interaction:

```python
def voltage_force_callback(g, signal, reference, value):
    force_hardware_available = True  # Hardware presence flag
    measured_value = 3.295  # Example applied voltage value
    return force_hardware_available, measured_value

def current_force_callback(g, signal, reference, value):
    force_hardware_available = True
    measured_value = 3.295  # Example applied current value
    return force_hardware_available, measured_value

def resistance_force_callback(g, signal, reference, value):
    force_hardware_available = True
    measured_value = 1000  # Example applied resistance value
    return force_hardware_available, measured_value

def frequency_force_callback(g, signal, reference, value):
    force_hardware_available = True
    measured_value = 100  # Example applied frequency value
    return force_hardware_available, measured_value
```

**Analysis:**
These callbacks must be customized to communicate with your hardware. They receive the global context, signal, reference, and the force value to apply. They return whether the hardware is available and the actual value applied.

---

### 3. Hardware Meta Function (`hardware/force.py`)

```python
def apply_force_and_measure(g, signal, reference, value, force_type):
    # Check if callback is registered for the force_type
    if g.hardware_callbacks[force_type]:
        hardware_available, measured_value = g.hardware_callbacks[force_type](g, signal, reference, value)
        if hardware_available:
            return hardware_available, measured_value
        return False, 0
    return False, 0
```

**Analysis:**
This function abstracts the interaction between instructions and hardware callbacks. It dispatches the force command to the appropriate callback and returns the hardware availability and measured/applied value.

---

### 4. Force Instructions (`instructions/force.py`)

```python
from dfttools.glob import g
from dfttools.hardware.force import apply_force_and_measure

def VFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'voltage_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value

def AFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'current_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value

def RESFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'resistance_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value

def FREQFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'frequency_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value
```

**Analysis:**
Each force instruction applies a force of a given type (voltage/current/resistance/frequency) to a hardware signal and reference. If hardware is unavailable, it returns the requested value as-is. All successful operations are logged.

---

### 5. Example Usage

```python
from dfttools import *

# Register force callbacks
g.hardware_callbacks = {
    'voltage_force': voltage_force_callback,
    'current_force': current_force_callback,
    'resistance_force': resistance_force_callback,
    'frequency_force': frequency_force_callback,
}

print("Testing Voltage Force:")
result_voltage = VFORCE(signal='VCC', value=1.1)
print(f"Voltage Force Result: {result_voltage}")

print("\nTesting Current Force:")
result_current = AFORCE(signal='VCC', reference='GND', value=1.0)
print(f"Current Force Result: {result_current}")
```

**Analysis:**
This snippet shows how to register your hardware callbacks and apply voltage and current forces. The printed results demonstrate the applied values or fallback behavior if hardware is unavailable.

---
# Customizable Power Supply Force Callbacks and Usage Examples for dfttools

---

## Overview

This section provides **elaborated, real-world examples** of how to implement and use customizable callback functions for power supply operations (voltage force, current force, electronic loads, etc.) in the `dfttools` framework. These callbacks should interface with your actual hardware APIs or communication protocols (e.g., SCPI, serial, socket, REST API) and **must return a tuple**:
`(hardware_exists, force_value)`
where `hardware_exists` is a boolean indicating whether the hardware is accessible, and `force_value` is the value applied or measured.

---

## Example: Power Supply Control Callbacks

Below are example callback implementations for voltage force, current force, and electronic load. Replace the simulated logic with your actual hardware communication code.

### 1. Voltage Force Callback

```python
def voltage_force_callback(g, signal, reference, value):
    """
    Set the power supply voltage for a given channel (signal).
    Returns (hardware_exists, actual_voltage_set).
    """
    try:
        # Example: Replace with your hardware API call
        # Example SCPI: psu.write(f"VOLT {value}, (@{signal})")
        print(f"[PowerSupply] Setting voltage {value}V on channel {signal}")
        actual_voltage = value  # In real code, query the hardware for the set value
        hardware_exists = True  # Set to False if hardware is not found or communication fails
    except Exception as e:
        print(f"Error setting voltage: {e}")
        hardware_exists = False
        actual_voltage = 0.0
    return hardware_exists, actual_voltage
```


### 2. Current Force Callback

```python
def current_force_callback(g, signal, reference, value):
    """
    Set the power supply current limit for a given channel (signal).
    Returns (hardware_exists, actual_current_set).
    """
    try:
        # Example: Replace with your hardware API call
        # Example SCPI: psu.write(f"CURR {value}, (@{signal})")
        print(f"[PowerSupply] Setting current {value}A on channel {signal}")
        actual_current = value  # In real code, query the hardware for the set value
        hardware_exists = True
    except Exception as e:
        print(f"Error setting current: {e}")
        hardware_exists = False
        actual_current = 0.0
    return hardware_exists, actual_current
```


### 3. Electronic Load (Current Sink) Callback

```python
def load_force_callback(g, signal, reference, value):
    """
    Set the electronic load to sink a specific current on a given channel.
    Returns (hardware_exists, actual_load_set).
    """
    try:
        # Example: Replace with your hardware API call
        # Example SCPI: eload.write(f"CURR {value}, (@{signal})")
        print(f"[E-Load] Setting load current {value}A on channel {signal}")
        actual_load = value  # In real code, query the hardware for the set value
        hardware_exists = True
    except Exception as e:
        print(f"Error setting load: {e}")
        hardware_exists = False
        actual_load = 0.0
    return hardware_exists, actual_load
```

---

## Registering Callbacks

Register your callbacks for use in force instructions:

```python
from dfttools.glob import g

g.hardware_callbacks['voltage_force'] = voltage_force_callback
g.hardware_callbacks['current_force'] = current_force_callback
g.hardware_callbacks['load_force'] = load_force_callback
```

---

## Using Force Instructions

You can now use the force instructions as follows:

```python
from dfttools import *

# Voltage force example
result = VFORCE(signal='CH1', value=5.0)
print(f"Voltage Force Result: {result}")

# Current force example
result = AFORCE(signal='CH1', reference='GND', value=1.0)
print(f"Current Force Result: {result}")

# Load force example (assuming you have added a LOADFORCE instruction)
result = LOADFORCE(signal='CH1', reference='GND', value=2.0)
print(f"Load Force Result: {result}")
```

---

## Example: Adding a Custom Force Instruction

If you want to add a new force instruction (e.g., for a programmable load):

```python
def LOADFORCE(signal: str = 'CH1', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'load_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value
```

---

## Notes on Customization

- **Meta Data**: You can expand the callback signature to include more meta data (e.g., ranges, modes, protection settings) as needed.
- **Error Handling**: Always catch exceptions and return `hardware_exists = False` if the hardware is not accessible.
- **Hardware Abstraction**: For real hardware, use the vendor’s Python API, SCPI commands via VISA/pyvisa, serial communication, or network sockets as appropriate.
- **Testing**: For simulation or testing, callbacks can simply print actions and return the requested value.

---

## Summary Table

| Callback Name | Purpose | Must Return |
| :-- | :-- | :-- |
| voltage_force_callback | Set power supply voltage | (hardware_exists, voltage) |
| current_force_callback | Set power supply current | (hardware_exists, current) |
| load_force_callback | Set electronic load current | (hardware_exists, load) |

---

## Example Output

```
[PowerSupply] Setting voltage 5.0V on channel CH1
Voltage Force Result: 5.0

[PowerSupply] Setting current 1.0A on channel CH1
Current Force Result: 1.0

[E-Load] Setting load current 2.0A on channel CH1
Load Force Result: 2.0
```

---
## Summary

- **Force instructions** in dfttools allow applying voltage, current, resistance, and frequency to hardware signals.
- **Callbacks** receive meta data (`g`, `signal`, `reference`, `value`) and must return `(hardware_available, applied_value)`.
- The **global context `g`** manages callbacks, hardware availability flags, and logs all operations.
- Users must **customize callbacks** to interface with their specific hardware.
- The system is **modular, extensible, and traceable**, suitable for automated hardware testing and control.