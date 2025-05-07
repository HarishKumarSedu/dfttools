def apply_i2c_read_write(g, device_address: int, field_info: dict, operation: str, value: int = None):
    """
    Perform I2C read or write operation using the provided field information.

    Args:
        g (GlobalContext): The global context.
        device_address (int): The address of the I2C device.
        field_info (dict): A dictionary containing field name, length, and register details.
        operation (str): The type of operation ('read' or 'write').
        value (int): The value to be written if operation is 'write'. Defaults to None.

    Returns:
        int or bool: The read value if operation is 'read', True if write is successful, or None/False otherwise.
    """
    if operation == 'read':
        # Read data from the device and rearrange according to register masks and lengths
        read_data = []
        for register in field_info['registers']:
            register_address = int(register['REG'], 16)
            mask = int(register['Mask'], 16)
            field_length = register['Length']

            # Dynamically invoke the read callback
            callback_key = 'i2c_read'
            if g.hardware_callbacks.get(callback_key, None):
                read_byte = g.hardware_callbacks[callback_key](device_address, register_address,register)
                if read_byte : 
                    # Extract the field value based on the mask and length
                    field_value = (read_byte & mask) >> register['FieldLSB']
                    read_data.append(field_value)
            else:
                return None  # No callback available


        # Combine the field values into a single integer
        read_value = 0
        for i, field_value in enumerate(read_data):
            read_value |= field_value << (i * field_info['registers'][i]['Length'])

        return read_value

    elif operation == 'write':
        # Split the write value into fields based on register masks and lengths
        field_values = []
        remaining_value = int(value,16) if isinstance(value,str) else  value
        write_allowed = True
        for register in field_info['registers']:
            field_length = register['Length']
            mask = int(register['Mask'], 16)
            attribute = register.get('Attribute', '')

            # Check if the register is read-only
            if 'RR' in attribute:
                print(f"Register {register['RegisterName']} is read-only. Skipping write operation.")
                write_allowed = False
                continue

            # Extract the field value from the write value
            # field_value = (remaining_value >> (len(field_values) * field_length)) & ((1 << field_length) - 1)
            field_values.append(remaining_value)
            # remaining_value &= ~(mask << register['FieldLSB'])
        if not write_allowed:
            return False

        # Write each field value to the corresponding register
        for i, register in enumerate(field_info['registers']):
            if 'RR' in register.get('Attribute', ''):
                continue  # Skip read-only registers

            register_address = int(register['REG'], 16)
            callback_key = 'i2c_write'
            if g.hardware_callbacks.get(callback_key, None):
                success = g.hardware_callbacks[callback_key](device_address, register_address, field_values[i],register)
                if not success:
                    return False  # Write operation failed
            else:
                return False  # No callback available

        return True

    return None