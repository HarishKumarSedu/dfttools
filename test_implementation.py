from PyMCP2221A import PyMCP2221A
from multimeter import mul_34401A
from dfttools import *
from dfttools import g

def custom_i2c_write_callback(device_address: int, register_address: int, value: int,register):
    # Simulated write logic (replace with actual I2C logic)
    # mcp2221 = PyMCP2221A.PyMCP2221A()
    # mcp2221.I2C_Init()
    default = int(register['Default'], 16)
    mask = int(register['Mask'], 16)
    LSB = register['POS'] 
    print(f"Writing {hex(value)} to device {hex(device_address)}, register {hex(register_address)},")
    # value = ((default & mask) | value << LSB) & 0xFF
    # mcp2221.I2C_Write(device_address,bytearray([register_address,value]))
    return True
    # Define callback functions for measurement
    
def custom_voltage_measure_callback( signal, reference):
    # multimeter = mul_34401A('USB0::0x2A8D::0x1401::MY57229870::INSTR')
    # if (Voltage := multimeter.meas_V()):
    #     measure_hardware_available = True
    #     return measure_hardware_available, Voltage
    # else:
    #     measure_hardware_available = False
    #     return measure_hardware_available, None
    pass

g.hardware_callbacks = {
    'i2c_write': custom_i2c_write_callback,
    # 'voltage_measure': custom_voltage_measure_callback,
}
print(g.hardware_callbacks.keys())    
def trail():
    import Trim_BG as Trim_BG

    
if __name__ == "__main__":
    trail()

'''
............ Trim_BG ........
Writing 0x0 to device 0x68, register 0xfe,
Writing 0x1 to device 0x68, register 0x0,
Writing 0x1 to device 0x68, register 0x55,
Writing 0xaa to device 0x68, register 0xf7,
Writing 0xbb to device 0x68, register 0xf7,
Writing 0x1 to device 0x68, register 0xfe,
Writing 0x0 to device 0x68, register 0x40,
Writing 0x1 to device 0x68, register 0x20,
Writing 0x1 to device 0x68, register 0x1e,
Writing 0x6 to device 0x68, register 0x1f,
Writing 0x0 to device 0x68, register 0xc1,
Writing 0x1 to device 0x68, register 0xc1,
Writing 0x2 to device 0x68, register 0xc1,
Writing 0x3 to device 0x68, register 0xc1,
Writing 0x4 to device 0x68, register 0xc1,
Writing 0x5 to device 0x68, register 0xc1,
Writing 0x6 to device 0x68, register 0xc1,
Writing 0x7 to device 0x68, register 0xc1,
Writing 0x8 to device 0x68, register 0xc1,
Writing 0x9 to device 0x68, register 0xc1,
Writing 0xa to device 0x68, register 0xc1,
Writing 0xb to device 0x68, register 0xc1,
Writing 0xc to device 0x68, register 0xc1,
Writing 0xd to device 0x68, register 0xc1,
Writing 0xe to device 0x68, register 0xc1,
Writing 0xf to device 0x68, register 0xc1,
............ Trim_BG Passed ........
Writing 0xd to device 0x68, register 0xc1,
Optimal Code: 0xd
Optimal measured value : 1.2318761V, Target vlaue : 1.242V
Minimum Error: 0.8151288244766476%
'''