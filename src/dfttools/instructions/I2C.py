from dfttools.glob import g
from dfttools.hardware.i2c import apply_i2c_read_write
from typing import Union, Dict  

from typing import Union, Dict

def I2C_READ(
    device_address: Union[int, str], 
    field_info: Dict, 
    expected_value: Union[int, str]) :
    """
    Read data from an I2C device using the provided field information.

    Args:
        device_address (int or str): The address of the I2C device (int or hex string like '0x48').
        field_info (dict): A dictionary containing field name, length, and register details.
        expected_value (int or str): The expected value to return if no hardware is found (int or hex string).

    Returns:
        int: The read value rearranged according to the register masks and lengths,
             or the expected value if hardware is not available.
    """

    # Convert device_address and expected_value to int if they are strings (hex or decimal)
    if isinstance(device_address, str):
        device_address = int(device_address, 0)  # base 0 interprets '0x...' as hex
    if isinstance(expected_value, str):
        expected_value = int(expected_value, 0)

    read_value = apply_i2c_read_write(g, device_address, field_info, 'read')
    if read_value is None:
        return expected_value

    return read_value

def I2C_WRITE(
    device_address: Union[int, str], 
    field_info: Dict, 
    write_value: Union[int, str]
) :
    """
    Write data to an I2C device using the provided field information.

    Args:
        g (GlobalContext): The global context.
        device_address (int or str): The address of the I2C device (int or hex string like '0x48').
        field_info (dict): A dictionary containing field name, length, and register details.
        write_value (int or str): The value to be written to the device (int or hex string).

    Returns:
        bool: True if the write operation was successful, False otherwise.
    """

    # Convert device_address and write_value to int if they are strings (hex or decimal)
    if isinstance(device_address, str):
        device_address = int(device_address, 0)  # base 0 interprets '0x...' as hex
    if isinstance(write_value, str):
        write_value = int(write_value, 0)

    hardware_available = g.hardware_callbacks.get('i2c_write', None)

    if not hardware_available:
        return False

    return apply_i2c_read_write(g, device_address, field_info, 'write', write_value)