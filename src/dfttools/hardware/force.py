def apply_force_and_measure(g, signal, reference, value, force_type,*args,**kwargs):
    # Check hardware availability using the callback if defined
    if g.hardware_callbacks.get(force_type, None) :
        hardware_available, measured_value = g.hardware_callbacks[force_type]( signal=signal, reference=reference, value=value,*args,**kwargs)
        if hardware_available:
            return hardware_available, measured_value 
        return False,0
    return False,0