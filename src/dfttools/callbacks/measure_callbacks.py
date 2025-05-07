# Define callback functions for measurement
def voltage_measure_callback( signal, reference):
    measure_hardware_available = True
    measured_value = 3.3  # Simulated voltage measurement
    return measure_hardware_available, measured_value

def current_measure_callback( signal, reference):
    measure_hardware_available = True
    measured_value = 1.2  # Simulated current measurement
    return measure_hardware_available, measured_value

def resistance_measure_callback( signal, reference):
    measure_force_hardware_available = True
    measured_value = 1000  # Simulated resistance measurement
    return measure_force_hardware_available, measured_value

def frequency_measure_callback( signal, reference):
    measure_hardware_available = True
    measured_value = 50  # Simulated frequency measurement
    return measure_hardware_available, measured_value

