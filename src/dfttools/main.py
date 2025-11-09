# from instructions.force import VFORCE,AFORCE
# from instructions.meas import *
# from instructions.force_sweep import *
from dfttools.instructions.I2C import *
from dfttools.glob import g
from dfttools.callbacks.force_callbacks import *
from dfttools.callbacks.measure_callbacks import *
from dfttools.callbacks.force_sweep_callbacks import *
from dfttools.callbacks.i2c_callback import *
_simulated_registers = {}

def i2c_reg_write(device_address: int, register_address: int, value: int) -> bool:
    """
    Simulate writing a value to an I2C register.
    """
    key = (device_address, register_address)
    _simulated_registers[key] = value
    print(f"[i2c_reg_write] Wrote 0x{value:X} to device 0x{device_address:X}, register 0x{register_address:X}")
    return True

def i2c_reg_read(device_address: int, register_address: int, No_bytes: int = 1) -> int:
    """
    Simulate reading a value from an I2C register.
    """
    key = (device_address, register_address)
    value = _simulated_registers.get(key, 0)
    print(f"[i2c_reg_read] Read 0x{value:X} from device 0x{device_address:X}, register 0x{register_address:X}")
    return value

def i2c_bit_write(device_address: int, register_address: int, msb: int, lsb: int, value: int) -> bool:
    """
    Simulate writing bits (msb, lsb, and combined value) to a register.
    For simplicity, store combined value only.
    """
    key = (device_address, register_address)
    _simulated_registers[key] = value
    print(f"[i2c_bit_write] Wrote combined 0x{value:X} (MSB=0x{msb:X}, LSB=0x{lsb:X}) to device 0x{device_address:X}, register 0x{register_address:X}")
    return True

def i2c_bit_read(device_address: int, register_address: int, msb: int, lsb: int, expected_value: int = None):
    """
    Simulate reading bits from a register.
    Returns combined value stored.
    """
    key = (device_address, register_address)
    value = _simulated_registers.get(key, 0)
    print(f"[i2c_bit_read] Read combined 0x{value:X} from device 0x{device_address:X}, register 0x{register_address:X}")
    return value
def i2c_write_custom_callback(*args,**kwargs):
    print(args)
    return True,False
g.hardware_callbacks = {
    'i2c_reg_write': i2c_reg_write,
    'i2c_reg_read': i2c_reg_read,
    'i2c_bit_write': i2c_bit_write,
    'i2c_bit_read': i2c_bit_read,
    'i2c_write': i2c_write_custom_callback
}
g.hardware_callbacks['i2c_write'] = i2c_write_custom_callback
# I2C_WRITE(device_address="0x38", field_info={'fieldname': 'ref_force', 'length': 1, 'registers': [{'REG': '0x1C', 'POS': 4, 'RegisterName': 'FORCE_REGISTERS_5', 'RegisterLength': 8, 'Name': 'ref_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
# I2C_WRITE(device_address="0x38", field_info= {
#     "fieldname": "otp_isense_coeff0",
#     "length": 10,
#     "registers": [
#       {
#         "REG": "0xBA",
#         "POS": 6,
#         "RegisterName": "OTP FIELDS 10",
#         "RegisterLength": 8,
#         "Name": "otp_isense_coeff0[9:8]",
#         "Mask": "0xC0",
#         "Length": 2,
#         "FieldMSB": 9,
#         "FieldLSB": 8,
#         "Attribute": "NNNNNNNN",
#         "Default": "0x00",
#         "User": "00000000",
#         "Clocking": "REF",
#         "Reset": "C",
#         "PageName": "PAG1"
#       },
#       {
#         "REG": "0xBD",
#         "POS": 0,
#         "RegisterName": "OTP FIELDS 13 - TRACEABILITY 1",
#         "RegisterLength": 8,
#         "Name": "otp_isense_coeff0[7:0]",
#         "Mask": "0xFF",
#         "Length": 8,
#         "FieldMSB": 7,
#         "FieldLSB": 0,
#         "Attribute": "NNNNNNNN",
#         "Default": "0x00",
#         "User": "00000000",
#         "Clocking": "REF",
#         "Reset": "C",
#         "PageName": "PAG1"
#       }
#     ]
#   }, write_value=0x0201)

I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x4)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)