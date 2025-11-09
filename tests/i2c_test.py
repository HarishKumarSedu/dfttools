from dfttools import *
# Simulated hardware registers storage
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
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'ref_force', 'length': 1, 'registers': [{'REG': '0x1C', 'POS': 4, 'RegisterName': 'FORCE_REGISTERS_5', 'RegisterLength': 8, 'Name': 'ref_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
# # Test I2C_REG_WRITE
# device_addr = '0x50'
# register_addr = '0x01'
# write_val = '0xAB'

# print("\n--- Testing I2C_REG_WRITE ---")
# success = I2C_REG_WRITE( device_addr, register_addr, write_val)
# print(f"Write success: {success}")

# # Test I2C_REG_READ
# print("\n--- Testing I2C_REG_READ ---")
# read_val = I2C_REG_READ( device_addr, register_addr, expected_value=write_val)
# print(f"Read value: 0x{read_val:X}")

# # Test I2C_BIT_WRITE
# msb_val = 2
# lsb_val = 1
# combined_val = (msb_val << 8) | lsb_val

# print("\n--- Testing I2C_BIT_WRITE ---")
# bit_write_success = I2C_BIT_WRITE( device_addr, register_addr, msb_val, lsb_val, combined_val)
# print(f"Bit write success: {bit_write_success}")

# # Test I2C_BIT_READ
# print("\n--- Testing I2C_BIT_READ ---")
# bit_read_val = I2C_BIT_READ( device_addr, register_addr, msb=msb_val, lsb=lsb_val, expected_value=combined_val)
# print(f"Bit read value: {read_val}")

# field_info1 = {
#     "fieldname": "tdm_bclk_osr",
#     "length": 2,
#     "registers": [
#       {
#         "REG": "0x00",
#         "POS": 6,
#         "RegisterName": "Config REG1",
#         "RegisterLength": 8,
#         "Name": "tdm_bclk_osr[1:0]",
#         "Mask": "0xC0",
#         "Length": 2,
#         "FieldMSB": 1,
#         "FieldLSB": 0,
#         "Attribute": "NNNNNNNN",
#         "Default": "00",
#         "User": "000YYYYY",
#         "Clocking": "FRO",
#         "Reset": "C",
#         "PageName": "PAG0"
#       }
#     ]
#   }   
# field_info2 = {
#     "fieldname": "vbat_meas",
#     "length": 10,
#     "registers": [
#       {
#         "REG": "0x31",
#         "POS": 0,
#         "RegisterName": "VBAT measurement reg 1",
#         "RegisterLength": 8,
#         "Name": "vbat_meas[9:8]",
#         "Mask": "0x3",
#         "Length": 2,
#         "FieldMSB": 9,
#         "FieldLSB": 8,
#         "Attribute": "000000RR",
#         "Default": "00",
#         "User": "00YYYYYY",
#         "Clocking": "REF",
#         "Reset": "C",
#         "PageName": "PAG0"
#       },
#       {
#         "REG": "0x32",
#         "POS": 0,
#         "RegisterName": "VBAT measurement reg 2",
#         "RegisterLength": 8,
#         "Name": "vbat_meas[7:0]",
#         "Mask": "0xFF",
#         "Length": 8,
#         "FieldMSB": 7,
#         "FieldLSB": 0,
#         "Attribute": "RRRRRRRR",
#         "Default": "00",
#         "User": "YYYYYYYY",
#         "Clocking": "REF",
#         "Reset": "C",
#         "PageName": "PAG0"
#       }
#     ]
#   }
# def i2c_read_1_callback(device_address: int, register_address: int,reg):
#     # Simulated read logic (replace with actual I2C logic)
#     print(reg)
#     print(f"Reading I2C device at address {device_address} register {register_address} ")
#     return 0xFF
# g.hardware_callbacks = {
#     'i2c_read': i2c_read_1_callback,
#     'i2c_write': i2c_write_callback
# }

# # Test I2C operations
# print("I2C Read Results:", I2C_READ( device_address=0x12, field_info=field_info1, expected_value=0x3))