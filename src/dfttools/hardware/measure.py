def apply_force_and_measure(g, signal, reference, meas_type,expected_value,*args,**kwargs):
    # Check hardware availability using the callback if defined
    if g.hardware_callbacks.get(meas_type,None):
        hardware_available, measured_value = g.hardware_callbacks[meas_type]( signal=signal, reference=reference,expected_value=expected_value,*args,**kwargs)
        if hardware_available:
            return hardware_available, measured_value 
        return False,0
    return False,0
# Your fft_measure function as provided
def fft_measure(g, signal, reference, Signal_Type, Sample_number, Sample_time, window, parameters, meas_type, value,*args, **kwargs):
    if g.hardware_callbacks.get(meas_type, None):
        hardware_available, measured_values = g.hardware_callbacks[meas_type](
            signal, reference, Signal_Type, Sample_number, Sample_time, window, parameters
        )
        if hardware_available:
            return hardware_available, measured_values
        return False, {}
    return False, {}
