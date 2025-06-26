def vtrig_hl_callback( signal, reference, threshold):
    """
    Voltage High-to-Low trigger callback.
    Returns True if measured voltage < threshold.
    """
    hardware_available = True  # Assume hardware present
    measured_voltage = 2.7     # Replace with actual measurement code
    triggered = measured_voltage < threshold
    return hardware_available, triggered


def vtrig_lh_callback( signal, reference, threshold,*args,**kwargs):
    """
    Voltage Low-to-High trigger callback.
    Returns True if measured voltage > threshold.
    """
    hardware_available = True
    measured_voltage = 3.3
    triggered = measured_voltage > threshold
    return hardware_available, triggered


def vtrig_lg_callback( signal, reference, _,*args,**kwargs):
    """
    Voltage Low-to-Ground trigger callback.
    Returns True if measured voltage < 0.05V.
    """
    hardware_available = True
    measured_voltage = 0.02
    triggered = measured_voltage < 0.05
    return hardware_available, triggered


def atrig_hl_callback( signal, reference, threshold,*args,**kwargs):
    """
    Current High-to-Low trigger callback.
    Returns True if measured current < threshold.
    """
    hardware_available = True
    measured_current = 0.005
    triggered = measured_current < threshold
    return hardware_available, triggered


def atrig_lh_callback( signal, reference, threshold,*args,**kwargs):
    """
    Current Low-to-High trigger callback.
    Returns True if measured current > threshold.
    """
    hardware_available = True
    measured_current = 0.15
    triggered = measured_current > threshold
    return hardware_available, triggered


def atrig_lg_callback( signal, reference, _,*args,**kwargs):
    """
    Current Low-to-Ground trigger callback.
    Returns True if measured current < 0.001A.
    """
    hardware_available = True
    measured_current = 0.0005
    triggered = measured_current < 0.001
    return hardware_available, triggered
