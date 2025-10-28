from dfttools.glob import g
import random
from dfttools.hadware.time import apply_time_measure 

def TOFF_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure time_off between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_toff_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def PERIOD_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure period time between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_period_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def PULSE_WIDTH_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure pulse width time between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_pulse_width_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def RISE_TIME_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure rise time between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_rise_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def FALL_TIME_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure fall time between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_fall_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def TON_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure time on between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_ton_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def MIN_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure minimum time between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_min_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def MAX_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure maximum time between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_max_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value