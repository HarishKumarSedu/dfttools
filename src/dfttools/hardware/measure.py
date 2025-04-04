def apply_force_and_measure(g, signal, reference, force_type,*args,**kwargs):
    # Check hardware availability using the callback if defined
    if g.hardware_callbacks[force_type]:
        hardware_available, measured_value = g.hardware_callbacks[force_type](g, signal, reference)
        if hardware_available:
            return hardware_available, measured_value 
        return False,0