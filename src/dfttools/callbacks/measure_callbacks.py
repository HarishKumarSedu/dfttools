import random
from typing import Dict
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

def fft_compute_callback(signal, reference, signal_type, sample_number, sample_time, window, parameters):
    # Simulate hardware availability randomly
    hardware_available = random.choice([True, False])
    if hardware_available:
        # Return mock measured values for each requested parameter
        measured_values = {param: random.uniform(0.9, 1.1) * 100 for param in parameters}
        return True, measured_values
    else:
        return False, {}