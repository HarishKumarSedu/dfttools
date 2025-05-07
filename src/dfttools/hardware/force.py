def apply_force_and_measure(g, signal, reference, value, force_type):
    # Check hardware availability using the callback if defined
    if g.hardware_callbacks[force_type]:
        hardware_available, measured_value = g.hardware_callbacks[force_type]( signal, reference, value)
        if hardware_available:
            return hardware_available, measured_value 
        return False,0
    return False,0