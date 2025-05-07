from dfttools.glob import g
from dfttools.hardware.i2c import apply_i2c_read_write

def I2C_READ( device_address: int, field_info: dict, expected_value: int):
    """
    Read data from an I2C device using the provided field information.

    Args:
        g (GlobalContext): The global context.
        device_address (int): The address of the I2C device.
        field_info (dict): A dictionary containing field name, length, and register details.
        expected_value (int): The expected value to return if no hardware is found.

    Returns:
        int: The read value rearranged according to the register masks and lengths,
             or the expected value if hardware is not available.
    """
    read_value = apply_i2c_read_write(g, device_address, field_info, 'read')
    if read_value is None:
        return expected_value
    
    return read_value

def I2C_WRITE( device_address: int, field_info: dict, write_value: int):
    """
    Write data to an I2C device using the provided field information.

    Args:
        g (GlobalContext): The global context.
        device_address (int): The address of the I2C device.
        field_info (dict): A dictionary containing field name, length, and register details.
        write_value (int): The value to be written to the device.

    Returns:
        bool: True if the write operation was successful, False otherwise.
    """
    hardware_available = g.hardware_callbacks.get('i2c_write', None)

    if not hardware_available:
        return False

    return apply_i2c_read_write(g, device_address, field_info, 'write', write_value)