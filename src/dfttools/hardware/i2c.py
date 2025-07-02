# def apply_i2c_read_write(g, device_address: int, field_info: dict, operation: str, value: int = None):
#     """
#     Perform I2C read or write operation using the provided field information.

#     Args:
#         g (GlobalContext): The global context.
#         device_address (int): The address of the I2C device.
#         field_info (dict): A dictionary containing field name, length, and register details.
#         operation (str): The type of operation ('read' or 'write').
#         value (int): The value to be written if operation is 'write'. Defaults to None.

#     Returns:
#         int or bool: The read value if operation is 'read', True if write is successful, or None/False otherwise.
#     """
#     if operation == 'read':
#         # Read data from the device and rearrange according to register masks and lengths
#         read_data = []
#         for register in field_info['registers']:
#             register_address = int(register['REG'], 16)
#             mask = int(register['Mask'], 16)
#             field_length = register['Length']

#             # Dynamically invoke the read callback
#             callback_key = 'i2c_read'
#             if g.hardware_callbacks.get(callback_key, None):
#                 read_byte = g.hardware_callbacks[callback_key](device_address, register_address,register)
#                 if read_byte : 
#                     # Extract the field value based on the mask and length
#                     field_value = (read_byte & mask) >> register['FieldLSB']
#                     read_data.append(field_value)
#             else:
#                 return None  # No callback available


#         # Combine the field values into a single integer
#         read_value = 0
#         for i, field_value in enumerate(read_data):
#             read_value |= field_value << (i * field_info['registers'][i]['Length'])

#         return read_value

#     elif operation == 'write':
#         # Split the write value into fields based on register masks and lengths
#         field_values = []
#         remaining_value = int(value,16) if isinstance(value,str) else  value
#         write_allowed = True
#         for register in field_info['registers']:
#             field_length = register['Length']
#             mask = int(register['Mask'], 16)
#             attribute = register.get('Attribute', '')

#             # Check if the register is read-only
#             if 'RR' in attribute:
#                 print(f"Register {register['RegisterName']} is read-only. Skipping write operation.")
#                 write_allowed = False
#                 continue

#             # Extract the field value from the write value
#             # field_value = (remaining_value >> (len(field_values) * field_length)) & ((1 << field_length) - 1)
#             field_values.append(remaining_value)
#             # remaining_value &= ~(mask << register['FieldLSB'])
#         if not write_allowed:
#             return False

#         # Write each field value to the corresponding register
#         for i, register in enumerate(field_info['registers']):
#             if 'RR' in register.get('Attribute', ''):
#                 continue  # Skip read-only registers

#             register_address = int(register['REG'], 16)
#             callback_key = 'i2c_write'
#             if g.hardware_callbacks.get(callback_key, None):
#                 success = g.hardware_callbacks[callback_key](device_address, register_address, field_values[i],register)
#                 if success:
#                     return True  # Write operation sucess return value written inside the hadware availability and data written in register
#             #     else:
#             #         return False
#             # else:
#             #     return False  # No callback available

#         return True

#     return None

# def apply_i2c_reg_read_write(
#     g,
#     device_address: int,
#     register_address: int,
#     operation: str,
#     value: int = None
# ):
#     """
#     Perform I2C register read or write operation using hardware callbacks.

#     Args:
#         g: Global context containing hardware callbacks.
#         device_address (int): Address of the I2C device.
#         register_address (int): Address of the register to read or write.
#         operation (str): Operation type, either 'read' or 'write'.
#         value (int, optional): Value to write if operation is 'write'.

#     Returns:
#         bool or int or None: 
#             - True if write is successful.
#             - The read byte if read is successful.
#             - None if read callback is unavailable.
#             - False otherwise.
#     """
#     if operation == 'write':
#         callback_key = 'i2c_reg_write'
#         if g.hardware_callbacks.get(callback_key, None):
#             success = g.hardware_callbacks[callback_key](device_address, register_address, value)
#             if success:
#                 return True
#     elif operation == 'read':
#         callback_key = 'i2c_reg_read'
#         if g.hardware_callbacks.get(callback_key, None):
#             read_byte = g.hardware_callbacks[callback_key](device_address, register_address, No_bytes=1)
#             if read_byte:
#                 return read_byte
#         else:
#             return None
#     return False

# def apply_i2c_bit_read_write(
#     g,
#     device_address: int,
#     register_address: int,
#     operation: str,
#     msb: int = None,
#     lsb: int = None,
#     value: int = None
# ):
#     """
#     Perform I2C register read or write operation by passing MSB, LSB, and combined value to hardware callbacks.

#     Args:
#         g: Global context containing hardware callbacks.
#         device_address (int): Address of the I2C device.
#         register_address (int): Address of the register to read or write.
#         operation (str): Operation type, either 'read' or 'write'.
#         msb (int, optional): Most significant byte.
#         lsb (int, optional): Least significant byte.
#         value (int, optional): Combined 16-bit value.

#     Returns:
#         bool or int or tuple or None:
#             - True if write is successful.
#             - The read value (int or tuple) if read is successful.
#             - None if read callback is unavailable.
#             - False otherwise.
#     """
#     if operation == 'write':
#         callback_key = 'i2c_bit_write'
#         if g.hardware_callbacks.get(callback_key, None):
#             # Pass msb, lsb, and combined value to the callback if it supports them
#             success = g.hardware_callbacks[callback_key](
#                 device_address, register_address, msb, lsb, value
#             )
#             if success:
#                 return True
#     elif operation == 'read':
#         callback_key = 'i2c_bit_read'
#         if g.hardware_callbacks.get(callback_key, None):
#             # Pass device and register, optionally msb, lsb, value if needed for verification
#             read_result = g.hardware_callbacks[callback_key](
#                 device_address, register_address, msb, lsb, value
#             )
#             if read_result is not None:
#                 return read_result
#         else:
#             return None
#     return False
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
        read_data = []
        for register in field_info['registers']:
            register_address = int(register['REG'], 16)
            mask = int(register['Mask'], 16)
            field_lsb = register['FieldLSB']

            callback_key = 'i2c_read'
            if g.hardware_callbacks.get(callback_key, None):
                read_byte = g.hardware_callbacks[callback_key](device_address, register_address, register)
                if read_byte is not None:
                    # Extract field value from masked bits shifted by FieldLSB
                    field_value = (read_byte & mask) >> field_lsb
                    read_data.append((field_value, field_lsb))
                else:
                    return None
            else:
                return None  # No callback available

        # Combine all field values into single integer using their bit positions
        read_value = 0
        for field_value, field_lsb in read_data:
            read_value |= (field_value << field_lsb)

        return read_value

    elif operation == 'write':
        if value is None:
            return False

        combined_value = int(value, 16) if isinstance(value, str) else value
        write_allowed = True
        field_values = []

        for register in field_info['registers']:
            attribute = register.get('Attribute', '')
            if 'RR' in attribute:
                print(f"Register {register['RegisterName']} is read-only. Skipping write operation.")
                write_allowed = False
                continue

            field_length = register['Length']
            field_lsb = register['FieldLSB']
            # Extract bits for this field from combined value
            field_mask = (1 << field_length) - 1
            field_value = (combined_value >> field_lsb) & field_mask
            field_values.append(field_value)

        if not write_allowed:
            return False

        # Write each field value to its register
        for i, register in enumerate(field_info['registers']):
            if 'RR' in register.get('Attribute', ''):
                continue  # Skip read-only registers

            register_address = int(register['REG'], 16)
            callback_key = 'i2c_write'
            if g.hardware_callbacks.get(callback_key, None):
                success = g.hardware_callbacks[callback_key](device_address, register_address, field_values[i], register)
                if not success:
                    return False
            else:
                return False  # No callback available

        return True

    return None


def apply_i2c_reg_read_write(
    g,
    device_address: int,
    register_address: int,
    operation: str,
    value: int = None,
    PageNo:int=0,
):
    """
    Perform I2C register read or write operation using hardware callbacks.

    Args:
        g: Global context containing hardware callbacks.
        device_address (int): Address of the I2C device.
        register_address (int): Address of the register to read or write.
        operation (str): Operation type, either 'read' or 'write'.
        value (int, optional): Value to write if operation is 'write'.

    Returns:
        bool or int or None: 
            - True if write is successful.
            - The read byte if read is successful.
            - None if read callback is unavailable.
            - False otherwise.
    """
    if operation == 'write':
        callback_key = 'i2c_reg_write'
        if g.hardware_callbacks.get(callback_key, None):
            success = g.hardware_callbacks[callback_key](device_address, register_address, value,PageNo)
            if success:
                return True
    elif operation == 'read':
        callback_key = 'i2c_reg_read'
        if g.hardware_callbacks.get(callback_key, None):
            read_byte = g.hardware_callbacks[callback_key](device_address, register_address, PageNo,No_bytes=1)
            if read_byte:
                return read_byte
        else:
            return None
    return False


def apply_i2c_bit_read_write(
    g,
    device_address: int,
    register_address: int,
    operation: str,
    msb: int = None,
    lsb: int = None,
    value: int = None,
    PageNo:int=0,
):
    """
    Perform I2C register read or write operation by passing MSB, LSB, and combined value to hardware callbacks.

    Args:
        g: Global context containing hardware callbacks.
        device_address (int): Address of the I2C device.
        register_address (int): Address of the register to read or write.
        operation (str): Operation type, either 'read' or 'write'.
        msb (int, optional): Most significant byte.
        lsb (int, optional): Least significant byte.
        value (int, optional): Combined 16-bit value.

    Returns:
        bool or int or tuple or None:
            - True if write is successful.
            - The read value (int or tuple) if read is successful.
            - None if read callback is unavailable.
            - False otherwise.
    """
    if operation == 'write':
        callback_key = 'i2c_bit_write'
        if g.hardware_callbacks.get(callback_key, None):
            success = g.hardware_callbacks[callback_key](
                device_address, register_address, msb, lsb, value,PageNo
            )
            if success:
                return True
    elif operation == 'read':
        callback_key = 'i2c_bit_read'
        if g.hardware_callbacks.get(callback_key, None):
            read_result = g.hardware_callbacks[callback_key](
                device_address, register_address, msb, lsb, value,PageNo
            )
            if read_result is not None:
                return read_result
        else:
            return None
    return False
