from dfttools import *
from time import sleep

Test_Name = 'Trim_BG'
from Procedures import Startup , Startup_REF
print(f'............ {Test_Name} ........')

I2C_WRITE(device_address=0x68,field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address=0x68,field_info={'fieldname': 'otp_burnt_b', 'length': 1, 'registers': [{'REG': '0x40', 'POS': 7, 'RegisterName': 'OTP register 0', 'RegisterLength': 8, 'Name': 'otp_burnt_b', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '80', 'User': '00000000', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
I2C_WRITE(device_address=0x68,field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address=0x68,field_info={'fieldname': 'amux2_en', 'length': 1, 'registers': [{'REG': '0x20', 'POS': 1, 'RegisterName': 'Analog test 3', 'RegisterLength': 8, 'Name': 'amux2_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '0000YYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address=0x68,field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x1E', 'POS': 5, 'RegisterName': 'Analog test 1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address=0x68,field_info={'fieldname': 'diag_status_reg1_ch3', 'length': 8, 'registers': [{'REG': '0x1F', 'POS': 0, 'RegisterName': 'Status REG15', 'RegisterLength': 8, 'Name': 'diag_status_reg1_ch3[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x6)

# Initial value
percentage = 0.1 # 10% difference
typical_value = 1.242
low_value = typical_value - typical_value*percentage
high_value = typical_value + typical_value*percentage

# Step size
step_size = 0.077625 # **mV

# Number of steps width of the field / bits
num_steps = 2**4  # 4-bit

# Standard deviation for white noise
noise_std_dev = 0.025

# Initialize minimum error and optimal code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None

for i in range(num_steps):
    # sweep trimg code
    I2C_WRITE(device_address=0x68,field_info={'fieldname': 'ref_vbg_trim', 'length': 4, 'registers': [{'REG': '0xC1', 'POS': 4, 'RegisterName': 'OTP register 129', 'RegisterLength': 8, 'Name': 'ref_vbg_trim[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(i))
    # Generate monotonic values with step size
    expected_value = low_value + i * step_size 
    # Add white noise to each value
    measured_value = VMEASURE(signal="HWMute", reference="GND", expected_value=expected_value,error_spread=noise_std_dev)
    error = abs(measured_value - typical_value)/abs(typical_value) *100
    if error < min_error:
        min_error = error
        optimal_code = hex(i)
        optimal_measured_value = measured_value
    sleep(0.1)
# Check for limits
if low_value < optimal_measured_value < high_value:
    print(f'............ {Test_Name} Passed ........')
    # write the optimized code if the trim passed
    I2C_WRITE(device_address=0x68,field_info={'fieldname': 'ref_vbg_trim', 'length': 4, 'registers': [{'REG': '0xC1', 'POS': 4, 'RegisterName': 'OTP register 129', 'RegisterLength': 8, 'Name': 'ref_vbg_trim[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
else:
    print(f'............ {Test_Name} Failed ........')
    # if the trimh failed program detult zero
    I2C_WRITE(device_address=0x68,field_info={'fieldname': 'ref_vbg_trim', 'length': 4, 'registers': [{'REG': '0xC1', 'POS': 4, 'RegisterName': 'OTP register 129', 'RegisterLength': 8, 'Name': 'ref_vbg_trim[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'FRO', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0)
print(f"Optimal Code: {optimal_code}")
print(f"Optimal measured value : {optimal_measured_value}V, Target vlaue : {typical_value}V")
print(f"Minimum Error: {min_error}%")
