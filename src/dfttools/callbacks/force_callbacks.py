# Define callback functions
def voltage_force_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = 3.295  # Example dynamic measurement
    
    return force_hardware_available, measured_value

def current_force_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = 3.295  # Example dynamic measurement
    return force_hardware_available, measured_value

def resistance_force_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = 1000  # Example dynamic measurement
    return force_hardware_available, measured_value

def frequency_force_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = 100  # Example dynamic measurement
    return force_hardware_available, measured_value


