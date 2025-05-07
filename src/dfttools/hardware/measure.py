def apply_force_and_measure(g, signal, reference, meas_type,*args,**kwargs):
    # Check hardware availability using the callback if defined
    if g.hardware_callbacks[meas_type]:
        hardware_available, measured_value = g.hardware_callbacks[meas_type]( signal, reference)
        if hardware_available:
            return hardware_available, measured_value 
        return False,0
    return False,0
    