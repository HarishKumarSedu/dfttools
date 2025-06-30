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
g.hardware_callbacks = {
    'i2c_reg_write': i2c_reg_write,
    'i2c_reg_read': i2c_reg_read,
    'i2c_bit_write': i2c_bit_write,
    'i2c_bit_read': i2c_bit_read,
}

# Test I2C_REG_WRITE
device_addr = '0x50'
register_addr = '0x01'
write_val = '0xAB'

print("\n--- Testing I2C_REG_WRITE ---")
success = I2C_REG_WRITE( device_addr, register_addr, write_val)
print(f"Write success: {success}")

# Test I2C_REG_READ
print("\n--- Testing I2C_REG_READ ---")
read_val = I2C_REG_READ( device_addr, register_addr, expected_value=write_val)
print(f"Read value: 0x{read_val:X}")

# Test I2C_BIT_WRITE
msb_val = 2
lsb_val = 1
combined_val = (msb_val << 8) | lsb_val

print("\n--- Testing I2C_BIT_WRITE ---")
bit_write_success = I2C_BIT_WRITE( device_addr, register_addr, msb_val, lsb_val, combined_val)
print(f"Bit write success: {bit_write_success}")

# Test I2C_BIT_READ
print("\n--- Testing I2C_BIT_READ ---")
bit_read_val = I2C_BIT_READ( device_addr, register_addr, msb=msb_val, lsb=lsb_val, expected_value=combined_val)
print(f"Bit read value: {read_val}")
