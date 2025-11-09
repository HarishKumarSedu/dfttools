from dfttools import *
from dfttools.glob import db,detect_and_handle_main_db

detect_and_handle_main_db()
_simulated_registers = {}
def i2c_reg_write(device_address: int, register_address: int, value: int,page_No:int) -> bool:
    """
    Simulate writing a value to an I2C register.
    """
    key = (device_address, register_address)
    _simulated_registers[key] = value
    print(f"[i2c_reg_write] Wrote 0x{value:X} to device 0x{device_address:X}, register 0x{register_address:X}")
    db.create({'Instruction':'I2C','Unit':'W','data':{'DevADDR':device_address,'Reg':register_address,'value':value,'Page':page_No}})
    return False
def i2c_reg_read(device_address: int, register_address: int, page_No:int, No_bytes: int = 1) -> int:
    """
    Simulate reading a value from an I2C register.
    """
    key = (device_address, register_address)
    value = _simulated_registers.get(key, 0)
    print(f"[i2c_reg_read] Read 0x{value:X} from device 0x{device_address:X}, register 0x{register_address:X}")
    db.create({'Instruction':'I2C','Unit':'R','data':{'DevADDR':device_address,'Reg':register_address,'page_No':page_No}})
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
    # 'i2c_bit_write': i2c_bit_write,
    # 'i2c_bit_read': i2c_bit_read,
    # 'i2c_write': i2c_write_custom_callback
}
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x4)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x4)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_REG_WRITE(0x38,0x0f,0x01,0)
I2C_REG_READ(0x38,0x0f,0x01,0)
from main import test1
test1()
globals()['__cache__']= db.dump()
print(globals().get('__cache__'))