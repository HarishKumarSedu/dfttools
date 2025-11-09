def voltage_force_sweep_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = value  # Example dynamic measurement
    
    return force_hardware_available, measured_value

def current_force_sweep_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = value  # Example dynamic measurement
    return force_hardware_available, measured_value

def resistance_force_sweep_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = value  # Example dynamic measurement
    return force_hardware_available, measured_value

def frequency_force_sweep_callback( signal, reference, value):
    force_hardware_available = True  # Set hardware availability dynamically
    measured_value = value  # Example dynamic measurement
    return force_hardware_available, measured_value
