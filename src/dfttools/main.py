# from dfttools.instructions.force import VFORCE,AFORCE
# from dfttools.instructions.meas import *
# from dfttools.instructions.force_sweep import *
# from dfttools.instructions.I2C import *
# from dfttools.glob import g
# from dfttools.callbacks.force_callbacks import *
# from dfttools.callbacks.measure_callbacks import *
# from dfttools.callbacks.force_sweep_callbacks import *
# from dfttools.callbacks.i2c_callback import *
from dfttools import *

# g.hardware_callbacks = {
#     'voltage_force': voltage_force_callback, # must return hardware availablity and value
#     'current_force': current_force_callback,
#     'resistance_force': resistance_force_callback,
#     'frequency_force': frequency_force_callback,
# }
# print("Testing Voltage Force:")
# result_current = VFORCE(signal='VCC',value=1.1)
# print(f"voltage Force Result: {result_current}")

# print("\nTesting Current Force:")
# result_current = AFORCE(signal='VCC', reference='GND', value=1.0)
# print(f"Current Force Result: {result_current}")

# # Register callbacks in global context
# g.hardware_callbacks['voltage_measure'] = voltage_measure_callback
# g.hardware_callbacks['current_measure'] = current_measure_callback
# g.hardware_callbacks['resistance_measure'] = resistance_measure_callback
# g.hardware_callbacks['frequency_measure'] = frequency_measure_callback

<<<<<<< HEAD
# print("Voltage Measurement:", VMEASURE(signal='VCC', reference='GND', expected_value=3.5))
# print("Current Measurement:", AMEASURE(signal='VCC', reference='GND', expected_value=1.5))
# print("Resistance Measurement:", RESMEASURE(signal='R1', reference='GND', expected_value=1200))
# print("Frequency Measurement:", FREQMEASURE(signal='CLK', reference='GND', expected_value=60))
# # Register callbacks in global context
# g.hardware_callbacks = {
#     'voltage_force_sweep': voltage_force_sweep_callback,
#     'current_force_sweep': current_force_sweep_callback,
#     'resistance_force_sweep': resistance_force_sweep_callback,
#     'frequency_force_sweep': frequency_force_sweep_callback,
# }
=======
print("Voltage Measurement:", VMEASURE(signal='VCC', reference='GND', expected_value=3.5,error_spread=0.35))
print("Current Measurement:", AMEASURE(signal='VCC', reference='GND', expected_value=1.5))
print("Resistance Measurement:", RESMEASURE(signal='R1', reference='GND', expected_value=1200))
print("Frequency Measurement:", FREQMEASURE(signal='CLK', reference='GND', expected_value=60))
# Register callbacks in global context
g.hardware_callbacks = {
    'voltage_force_sweep': voltage_force_sweep_callback,
    'current_force_sweep': current_force_sweep_callback,
    'resistance_force_sweep': resistance_force_sweep_callback,
    'frequency_force_sweep': frequency_force_sweep_callback,
}
>>>>>>> 1dda9e84e076c0279f20e874e92afa8e7b82ab5e

# print("Voltage Sweep Results:", VFORCESWEEP(signal='VCC', reference='GND', initial_value=0.0, end_value=5.0, step=1, step_time=0.01))
# print("Current Sweep Results:", AFORCESWEEP(signal='VCC', reference='GND', initial_value=0.0, end_value=5.0, step=1, step_time=0.01))
# print("Resistance Sweep Results:", RESFORCESWEEP(signal='R1', reference='GND', initial_value=0.0, end_value=1000.0, step=100.0, step_time=0.01))
# print("Frequency Sweep Results:", FREQFORCESWEEP(signal='CLK', reference='GND', initial_value=0.0, end_value=100.0, step=100.0, step_time=0.01))
# # Register callbacks in global context
# # Register callbacks in global context
field_info1 = {
    "fieldname": "tdm_bclk_osr",
    "length": 2,
    "registers": [
      {
        "REG": "0x00",
        "POS": 6,
        "RegisterName": "Config REG1",
        "RegisterLength": 8,
        "Name": "tdm_bclk_osr[1:0]",
        "Mask": "0xC0",
        "Length": 2,
        "FieldMSB": 1,
        "FieldLSB": 0,
        "Attribute": "NNNNNNNN",
        "Default": "00",
        "User": "000YYYYY",
        "Clocking": "FRO",
        "Reset": "C",
        "PageName": "PAG0"
      }
    ]
  }   
field_info2 = {
    "fieldname": "vbat_meas",
    "length": 10,
    "registers": [
      {
        "REG": "0x31",
        "POS": 0,
        "RegisterName": "VBAT measurement reg 1",
        "RegisterLength": 8,
        "Name": "vbat_meas[9:8]",
        "Mask": "0x3",
        "Length": 2,
        "FieldMSB": 9,
        "FieldLSB": 8,
        "Attribute": "000000RR",
        "Default": "00",
        "User": "00YYYYYY",
        "Clocking": "REF",
        "Reset": "C",
        "PageName": "PAG0"
      },
      {
        "REG": "0x32",
        "POS": 0,
        "RegisterName": "VBAT measurement reg 2",
        "RegisterLength": 8,
        "Name": "vbat_meas[7:0]",
        "Mask": "0xFF",
        "Length": 8,
        "FieldMSB": 7,
        "FieldLSB": 0,
        "Attribute": "RRRRRRRR",
        "Default": "00",
        "User": "YYYYYYYY",
        "Clocking": "REF",
        "Reset": "C",
        "PageName": "PAG0"
      }
    ]
  }
def i2c_read_1_callback(device_address: int, register_address: int):
    # Simulated read logic (replace with actual I2C logic)
    print(f"Reading I2C device at address {device_address} register {register_address} ")
    return 0xFF
g.hardware_callbacks = {
    'i2c_read': i2c_read_1_callback,
    'i2c_write': i2c_write_callback
}

# Test I2C operations
print("I2C Read Results:", I2C_READ( device_address=0x12, field_info=field_info1, expected_value=0x3))
print("I2C Write Results:", I2C_WRITE( device_address=0x12, field_info=field_info1, write_value=0x3))
# Test I2C operations
print("I2C Read Results:", I2C_READ( device_address=0x12, field_info=field_info2, expected_value=0x3))
print("I2C Write Results:", I2C_WRITE( device_address=0x12, field_info=field_info2, write_value=0x3))