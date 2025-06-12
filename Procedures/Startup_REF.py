Test_Name = 'Startup_REF'

print(f'............ {Test_Name} ........')

from dfttools import *

'''

Force__ENABLE__4V

ForceClock_I2SCLK_3.072MHz_50%D_ VL_0_VH_VDDIO)

"I2SCLK is also called BCLK"

Wait__delay__5ms

Force__V5VDR__5.2V

"Force__VDDIO__1.8V"

0xFE__0x00 "Select page 0"

0x00__0x05 "{'fieldname': 'i2c_unlock', 'length': 1, 'registers': [{'REG': '0x00', 'POS': 0, 'RegisterName': 'Config REG1', 'RegisterLength': 8, 'Name': 'i2c_unlock', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '000YYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]} and tdm config"

0xF7__0xAA "Unlock test page"

0xF7__0xBB "Unlock test page"

0xFE__0x01"Select page 1"

0x20[5:5]__0x01 "Force PLL EN =1"

0x20[6:6]__0x01 "Force PLL EN =1"

0xFE__0x00 "Select page 0"

"0x40[7:7]__0x00"{'fieldname': 'otp_burnt_b', 'length': 1, 'registers': [{'REG': '0x40', 'POS': 7, 'RegisterName': 'OTP register 0', 'RegisterLength': 8, 'Name': 'otp_burnt_b', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '80', 'User': '00000000', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG1'}]}=0 to make effective writting otp""

0x94[3:3]__0x01 "Force ppart enable"

0x9D[4:4]__0x1 "{'fieldname': 'cld_hfirc_clk_en_ch1', 'length': 1, 'registers': [{'REG': '0x9D', 'POS': 4, 'RegisterName': 'Protection reg 4', 'RegisterLength': 8, 'Name': 'cld_hfirc_clk_en_ch1', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '33', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]} to 1"

0x9D[5:5]__0x1 "cld_hfirc_clk_en_ch2to 1"

0x9D[6:6]__0x1 "{'fieldname': 'cld_hfirc_clk_en_ch3', 'length': 1, 'registers': [{'REG': '0x9D', 'POS': 6, 'RegisterName': 'Protection reg 4', 'RegisterLength': 8, 'Name': 'cld_hfirc_clk_en_ch3', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '33', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]} to 1"

0x9D[7:7]__0x1 "{'fieldname': 'cld_hfirc_clk_en_ch4', 'length': 1, 'registers': [{'REG': '0x9D', 'POS': 7, 'RegisterName': 'Protection reg 4', 'RegisterLength': 8, 'Name': 'cld_hfirc_clk_en_ch4', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '33', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]} to 1"

0x88[2:0]__0x2 "{'fieldname': 'pwm_hys_dly', 'length': 3, 'registers': [{'REG': '0x88', 'POS': 4, 'RegisterName': 'Modulator reg 1', 'RegisterLength': 8, 'Name': 'pwm_hys_dly[2:0]', 'Mask': '0x70', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '37', 'User': '0YYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]}[2:0] = 4, {'fieldname': 'pwm_filt_band_sel', 'length': 4, 'registers': [{'REG': '0x88', 'POS': 0, 'RegisterName': 'Modulator reg 1', 'RegisterLength': 8, 'Name': 'pwm_filt_band_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '37', 'User': '0YYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]}[3:0] = 2 (K=14) "

0x88[3:0]__0x03

0xFE__0x01 "Select page 1"

Remove__CD_DIAG

"If total current consumption from VCCs is less than 10mA, BCLK is not reaching the IC"



Remove__ENABLE "Leave it open"





'''

VFORCE(signal="Enable", reference="GND", value=4.0)

FREQFORCE(signal="I2Cclk", reference="GND", value=3.07e6)

VFORCE(signal="V5VDR", reference="GND", value=5.2)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'i2c_unlock', 'length': 1, 'registers': [{'REG': '0x00', 'POS': 0, 'RegisterName': 'Config REG1', 'RegisterLength': 8, 'Name': 'i2c_unlock', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '000YYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'tdm_fsyn_rate_mnt_en', 'length': 1, 'registers': [{'REG': '0x55', 'POS': 7, 'RegisterName': 'Clock monitor settings 1', 'RegisterLength': 8, 'Name': 'tdm_fsyn_rate_mnt_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': 'E1', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'unlock_tst_addr', 'length': 1, 'registers': [{'REG': '0xF7', 'POS': 0, 'RegisterName': 'Unlock register', 'RegisterLength': 8, 'Name': 'unlock_tst_addr', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000R', 'Default': '00', 'User': '00000000', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0xaa)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'unlock_tst_addr', 'length': 1, 'registers': [{'REG': '0xF7', 'POS': 0, 'RegisterName': 'Unlock register', 'RegisterLength': 8, 'Name': 'unlock_tst_addr', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000R', 'Default': '00', 'User': '00000000', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0xbb)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'force_pll_en', 'length': 1, 'registers': [{'REG': '0x20', 'POS': 5, 'RegisterName': 'Analog test 3', 'RegisterLength': 8, 'Name': 'force_pll_en', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '0000YYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'pll_en_m', 'length': 1, 'registers': [{'REG': '0x20', 'POS': 6, 'RegisterName': 'Analog test 3', 'RegisterLength': 8, 'Name': 'pll_en_m', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '0000YYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'cld_force_ppart_en', 'length': 1, 'registers': [{'REG': '0x94', 'POS': 3, 'RegisterName': 'ClassD reg 3', 'RegisterLength': 8, 'Name': 'cld_force_ppart_en', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': '0000NNNN', 'Default': '60', 'User': 'YYYY00YY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'cld_hfirc_clk_en_ch1', 'length': 1, 'registers': [{'REG': '0x9D', 'POS': 4, 'RegisterName': 'Protection reg 4', 'RegisterLength': 8, 'Name': 'cld_hfirc_clk_en_ch1', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '33', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'cld_hfirc_clk_en_ch2', 'length': 1, 'registers': [{'REG': '0x9D', 'POS': 5, 'RegisterName': 'Protection reg 4', 'RegisterLength': 8, 'Name': 'cld_hfirc_clk_en_ch2', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '33', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'cld_hfirc_clk_en_ch3', 'length': 1, 'registers': [{'REG': '0x9D', 'POS': 6, 'RegisterName': 'Protection reg 4', 'RegisterLength': 8, 'Name': 'cld_hfirc_clk_en_ch3', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '33', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'cld_hfirc_clk_en_ch4', 'length': 1, 'registers': [{'REG': '0x9D', 'POS': 7, 'RegisterName': 'Protection reg 4', 'RegisterLength': 8, 'Name': 'cld_hfirc_clk_en_ch4', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '33', 'User': 'YYYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'pwm_hys_dly', 'length': 3, 'registers': [{'REG': '0x88', 'POS': 4, 'RegisterName': 'Modulator reg 1', 'RegisterLength': 8, 'Name': 'pwm_hys_dly[2:0]', 'Mask': '0x70', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '37', 'User': '0YYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x2)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'pwm_hys_dly', 'length': 3, 'registers': [{'REG': '0x88', 'POS': 4, 'RegisterName': 'Modulator reg 1', 'RegisterLength': 8, 'Name': 'pwm_hys_dly[2:0]', 'Mask': '0x70', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '37', 'User': '0YYYYYYY', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x3)

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)

# remove "CD_DIAG"

VFORCE(signal="CD_DIAG", reference="GND", value=float('inf'))



if AMEASURE(signal="VCC",reference="GND",expected_value=10e-3) < 10e-3:

  print('!!!!!! BCLK not reaching to the IC!!!!!!')

# remove Open Remove

VFORCE(signal="Enable", reference="GND", value=float('inf'))



