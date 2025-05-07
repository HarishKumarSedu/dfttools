def i2c_read_callback(device_address: int, register_address: int,*args, **kwargs):
    # Simulated read logic (replace with actual I2C logic)
    return 0xFF

def i2c_write_callback(device_address: int, register_address: int, value: int,*args, **kwargs):
    # Simulated write logic (replace with actual I2C logic)
    print(f"Writing {value} to device {device_address}, register {register_address}")
    return True
