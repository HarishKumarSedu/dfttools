from dfttools import *
from dfttools.glob import g

# Set up callbacks
g.hardware_callbacks['voltage_force'] = voltage_force_callback
g.hardware_callbacks['current_force'] = current_force_callback

# Test force functions
print("Testing Voltage Force:")
result_voltage = VFORCE(signal='VCC', value=1.1)
print(f"Voltage Force Result: {result_voltage}")

print("\nTesting Current Force:")
result_current = AFORCE(signal='VCC', reference='GND', value=1.0)
print(f"Current Force Result: {result_current}")

# Test measurement functions
print("\nTesting Voltage Measurement:")
result_measurement = VMEASURE(signal='VCC', reference='GND', expected_value=3.3)
print(f"Voltage Measurement Result: {result_measurement}")

# List all available keywords
import dfttools
print("\nAvailable keywords in dfttools:")
print([name for name in dir(dfttools) if not name.startswith("_")])
