def apply_time_measure(g, signal, reference, meas_type, *args, **kwargs):
    """
    Check time measurement hardware availability and get measurement via callback.
    """
    if g.hardware_callbacks.get(meas_type, None):
        hardware_available, measured_value = g.hardware_callbacks[meas_type](signal, reference, *args, **kwargs)
        if hardware_available:
            return hardware_available, measured_value
        return False, 0.0
    return False, 0.0
