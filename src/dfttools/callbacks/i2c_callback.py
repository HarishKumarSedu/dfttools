from dfttools import *
from dfttools.glob import g, db
import re 
def i2c_reg_write_callback( device_address: int, register_address: int, value: int,PgaeNo:int,*args,**kwargs) -> bool:
    record = {
        'Instruction': 'I2C',
        'Unit'       : 'WR-Reg',
        'SAD'        : hex(device_address),
        'ADD'        : hex(register_address),
        'DATA'       : hex(value),
        'MSB'        : '',
        'LSB'        : '',
        'PAGE'       : PgaeNo
        }
    db.create(record_data=record)
    return True


def i2c_reg_read_callback( device_address: int, register_address: int, value: int,PgaeNo:int,*args,**kwargs) -> bool:
    record = {
        'Instruction': 'I2C',
        'Unit'       : 'RR-Reg',
        'SAD'        : hex(device_address),
        'ADD'        : hex(register_address),
        'DATA'       : hex(value),
        'MSB'        : '',
        'LSB'        : '',
        'PAGE'       : PgaeNo
        }
    db.create(record_data=record)
    
    return value
def i2c_bit_write_callback( device_address: int, register_address: int, msb: int, lsb: int, value: int,PageNo:int) -> bool:
    """Write bits to an I2C register using the MCP bridge."""
    # This example assumes full byte write; bit masking can be added if needed.
    record = db.find_last_record({'Instruction':'I2C','SAD':hex(device_address),'ADD':hex(register_address),'PAGE':PageNo})
    mask = ((1<<(msb -lsb+1)) -1)<<lsb
    if record:
        record.pop('_id')
        record.pop('_created')
        data = int(record.get('DATA',None),0)
        if data != None:
            # data = (data & mask) | (value << register.get('POS',8))
            data = (data & ~mask) | value << lsb
        else:
            data = (0x00 & ~mask) | value << lsb
        record.update(
            {
             'Unit'       : 'WR-bit',
             'DATA'       : hex(data),
            }
        )
    else:
        record = {
        'Instruction': 'I2C',
        'Unit'       : 'WR-bit',
        'SAD'        : hex(device_address),
        'ADD'        : hex(register_address),
        'DATA'       : hex(value << lsb),
        'MSB'        : '',
        'LSB'        : '',
        'PAGE'       : PageNo,
        }
    db.create(record_data=record)
    return True
def i2c_bit_read_callback( device_address: int, register_address: int, msb: int, lsb: int, value: int,PageNo:int) -> bool:
    """Write bits to an I2C register using the MCP bridge."""
    # This example assumes full byte write; bit masking can be added if needed.
    record = db.find_last_record({'Instruction':'I2C','SAD':hex(device_address),'ADD':hex(register_address),'PAGE':PageNo})
    mask = ((1<<(msb -lsb+1)) -1)<<lsb
    if record:
        record.pop('_id')
        record.pop('_created')
        data = int(record.get('DATA',None),0)
        if data != None:
            # data = (data & mask) | (value << register.get('POS',8))
            data = (data & ~mask) | value << lsb
        else:
            data = (0x00 & ~mask) | value << lsb
        record.update(
            {
             'Unit'       : 'WR-bit',
             'DATA'       : hex(data),
            }
        )
    else:
        record = {
        'Instruction': 'I2C',
        'Unit'       : 'WR-bit',
        'SAD'        : hex(device_address),
        'ADD'        : hex(register_address),
        'DATA'       : hex(value << lsb),
        'MSB'        : '',
        'LSB'        : '',
        'PAGE'       : PageNo,
        }
    db.create(record_data=record)
    return (value & mask)
def i2c_write_callback( device_address: int, register_address: int, value: int, register: dict) -> bool:
    page = register.get('PageName',0) # default as the page 0
    pageNo = page_list[0] if  (page_list :=re.findall(r'\d+', page)) and  isinstance(page,str) else 0
    record = db.find_last_record({'Instruction':'I2C','SAD':hex(device_address),'ADD':hex(register_address),'PAGE':pageNo})
    mask = (2**register.get('RegisterLength',8) - int(register.get('Mask','0xFF'),0) -1)
    if record:
        record.pop('_id')
        record.pop('_created')
        data = int(record.get('DATA',None),0)
        if data != None:
            data = (data & mask) | (value)
        else:
            data = (int(register.get('Default','0x00'),0) & mask) | (value)
        record.update(
            {
             'Unit'       : 'WR-Reg',
             'DATA'       : hex(data),
            }
        )
    else:
        data = (int(register.get('Default','0x00'),0) & mask) | (value)
        record = {
        'Instruction': 'I2C',
        'Unit'       : 'WR-Reg',
        'SAD'        : hex(device_address),
        'ADD'        : hex(register_address),
        'DATA'       : hex(data),
        'MSB'        : '',
        'LSB'        : '',
        'PAGE'       : pageNo
        }
    db.create(record_data=record)
    return True,False
# I2C read callback with optional bit masking
def i2c_read_callback( device_address: int, register_address: int,value:int ,register: dict = None) -> int:
    page = register.get('PageName',0) # default as the page 0
    pageNo = page_list[0] if  (page_list :=re.findall(r'\d+', page)) and  isinstance(page,str) else 0
    record = db.find_last_record({'Instruction':'I2C','SAD':hex(device_address),'ADD':hex(register_address),'PAGE':pageNo})
    mask = (2**register.get('RegisterLength',8) - int(register.get('Mask','0xFF'),0) -1)
    if record:
        record.pop('_id')
        record.pop('_created')
        data = int(record.get('DATA',None),0)
        if data != None:
            data = (data & mask) | (value)
        else:
            data = (int(register.get('Default','0x00'),0) & mask) | (value)
        record.update(
            {
             'Unit'       : 'RR-Reg',
             'DATA'       : hex(data),
            }
        )
    else:
        data = (int(register.get('Default','0x00'),0) & mask) | (value)
        record = {
        'Instruction': 'I2C',
        'Unit'       : 'RR-Reg',
        'SAD'        : hex(device_address),
        'ADD'        : hex(register_address),
        'DATA'       : hex(data),
        'MSB'        : '',
        'LSB'        : '',
        'PAGE'       : pageNo
        }
    db.create(record_data=record)
    return value >> register.get('POS',0)
i2c_callbacks = {
    'i2c_reg_write': i2c_reg_write_callback,
    'i2c_reg_read': i2c_reg_read_callback,
    'i2c_bit_write': i2c_bit_write_callback,
    'i2c_bit_read': i2c_bit_read_callback,
    'i2c_write': i2c_write_callback,
    'i2c_read': i2c_read_callback,
}

for name, func in i2c_callbacks.items():
    g.hardware_callbacks[name] = func

# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x4)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x4)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
# I2C_REG_WRITE(0x38,0x11,0x30,0)
# I2C_BIT_WRITE(0x38,0x11,1,0,2,0)
# I2C_BIT_READ(0x38,0x11,1,0,1,0)
# print(hex(I2C_REG_READ(0x38,0x11,0x30,0)))
# data = I2C_READ(device_address="0x38",field_info={'fieldname': 'ngif_out_filt_sample', 'length': 2, 'registers': [{'REG': '0x16', 'POS': 6, 'RegisterName': 'NGIF settings 2', 'RegisterLength': 8, 'Name': 'ngif_out_filt_sample[1:0]', 'Mask': '0xC0', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NN00NNNN', 'Default': '0x0B', 'User': '0000YYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x1)
# data = I2C_READ("0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},expected_value=0x10f) # turn on outp side / saturate the dac in postive side 
# I2C_WRITE("0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x01)
# print(hex(data))