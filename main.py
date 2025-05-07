
from dfttools import *
def trail():
    example_field = {'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}
    # import Trim_BG
    # # Register callbacks in global context
    def i2c_read_1_callback(devaddr,register):
        print(f"Reading I2C device at address {devaddr} register {register} ")

    g.hardware_callbacks = {
        'i2c_read': i2c_read_1_callback,
    }
    # # Test I2C operations
    print("I2C Read Results:", I2C_READ( device_address=0x12, field_info=example_field, expected_value=0x3))
    # print("I2C Write Results:", I2C_WRITE( device_address=0x12, field_info=field_info1, write_value=0x3))
    # # Test I2C operations
    # print("I2C Read Results:", I2C_READ( device_address=0x12, field_info=field_info2, expected_value=0x3))
    # print("I2C Write Results:", I2C_WRITE( device_address=0x12, field_info=field_info2, write_value=0x3))
    
if __name__ == "__main__":
    trail()

{'voltage_force': None, 'current_force': None, 'resistance_force': None, 'frequency_force': None, 'voltage_measure': None, 'current_measure': None, 'resistance_measure': None, 'frequency_measure': None, 'voltage_force_sweep': None, 'current_force_sweep': None, 'resistance_force_sweep': None, 'frequency_force_sweep': None, 'i2c_read': None, 'i2c_write': None, 'voltage_trigger_hl': None, 'voltage_trigger_lh': None, 'voltage_trigger_lg': None, 'current_trigger_hl': None, 'current_trigger_lh': None, 'current_trigger_lg': None}