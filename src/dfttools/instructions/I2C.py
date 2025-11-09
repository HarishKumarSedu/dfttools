from dfttools.glob import g
from dfttools.hardware.i2c import apply_i2c_read_write,apply_i2c_reg_read_write,apply_i2c_bit_read_write
# from glob import g
# from hardware.i2c import apply_i2c_read_write,apply_i2c_reg_read_write,apply_i2c_bit_read_write
from typing import Union, Dict  

from typing import Union, Dict
DEVICEADDR='0X00'
i2c_page_sel = {}
def I2C_READ(
    device_address: Union[int, str]=DEVICEADDR, 
    field_info: Dict=i2c_page_sel, 
    expected_value: Union[int, str]=0x1) :
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
    device_address: Union[int, str]=DEVICEADDR, 
    field_info: Dict=i2c_page_sel, 
    write_value: Union[int, str]=0x00,
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
def I2C_REG_WRITE(
    device_address: Union[int, str]=DEVICEADDR,
    register_address: Union[int, str]=0xFE,
    write_value: Union[int, str]=0x01,
    PageNo:int=0
) -> bool:
    """
    Write a value to a specific register of an I2C device.

    Args:
        g: Global context containing hardware callbacks.
        device_address (int or str): Address of the I2C device (integer or hex string, e.g., '0x48').
        register_address (int or str): Register address to write to (integer or hex string).
        write_value (int or str): Value to write to the register (integer or hex string).

    Returns:
        bool: True if the write operation was successful, False otherwise.
    """
    # Convert addresses and value to int if they are strings
    if isinstance(device_address, str):
        device_address = int(device_address, 0)
    if isinstance(register_address, str):
        register_address = int(register_address, 0)
    if isinstance(write_value, str):
        write_value = int(write_value, 0)

    hardware_available = g.hardware_callbacks.get('i2c_reg_write', None)
    if not hardware_available:
        return False

    return apply_i2c_reg_read_write(g, device_address, register_address, 'write', write_value,PageNo)
def I2C_REG_READ(
    device_address: Union[int, str],
    register_address: Union[int, str],
    expected_value: Union[int, str],
    PageNo:int=0,
) -> bool:
    """
    Write a value to a specific register of an I2C device.

    Args:
        g: Global context containing hardware callbacks.
        device_address (int or str): Address of the I2C device (integer or hex string, e.g., '0x48').
        register_address (int or str): Register address to write to (integer or hex string).
        write_value (int or str): Value to write to the register (integer or hex string).

    Returns:
        bool: True if the write operation was successful, False otherwise.
    """
    # Convert addresses and value to int if they are strings
    if isinstance(device_address, str):
        device_address = int(device_address, 0)
    if isinstance(register_address, str):
        register_address = int(register_address, 0)
    if isinstance(expected_value, str):
        expected_value = int(expected_value, 0)

    read_value = apply_i2c_reg_read_write(g, device_address, register_address, 'read', expected_value,PageNo)
    if read_value is None:
        return expected_value

    return read_value


def I2C_BIT_WRITE(
    device_address: Union[int, str]=DEVICEADDR,
    register_address: Union[int, str]=i2c_page_sel,
    msb: int =0,
    lsb: int=0,
    write_value: Union[int, str]=1,
    PageNo:int=0,
):
    """
    Read a value from a specific register of an I2C device and compare it to an expected value.

    Args:
 
        device_address (int or str): Address of the I2C device (integer or hex string, e.g., '0x48').
        register_address (int or str): Register address to read from (integer or hex string).
        expected_value (int or str): Expected value to compare against (integer or hex string).

    Returns:
        The read value if successful, or the expected value if the read fails.
    """
    # Convert addresses and expected value to int if they are strings
    if isinstance(device_address, str):
        device_address = int(device_address, 0)
    if isinstance(register_address, str):
        register_address = int(register_address, 0)
    if isinstance(write_value, str):
        write_value = int(write_value, 0)
    hardware_available = g.hardware_callbacks.get('i2c_bit_write', None)
    if not hardware_available:
        return False
    return apply_i2c_bit_read_write(g, device_address, register_address, 'write', lsb,msb,write_value,PageNo)


def I2C_BIT_READ(
    device_address: Union[int, str]=DEVICEADDR,
    register_address: Union[int, str]=0xFE,
    msb: int = 0,
    lsb: int = 0,
    expected_value: Union[int, str] = 0,
    PageNo:int=0,
) -> Union[int, tuple, None]:
    """
    Read from a specific register of an I2C device and optionally verify against expected value.

    Args:
        device_address (int or str): I2C device address.
        register_address (int or str): Register address.
        msb (int, optional): Expected most significant byte.
        lsb (int, optional): Expected least significant byte.
        expected_value (int or str, optional): Expected combined 16-bit value.

    Returns:
        int, tuple, or None: The read value(s) if successful, or None if read failed.
    """
    if isinstance(device_address, str):
        device_address = int(device_address, 0)
    if isinstance(register_address, str):
        register_address = int(register_address, 0)
    if expected_value is not None and isinstance(expected_value, str):
        expected_value = int(expected_value, 0)

    read_value = apply_i2c_bit_read_write(g, device_address, register_address, 'read', msb, lsb, expected_value,PageNo)
    if read_value is None:
        return expected_value
    return read_value