from dfttools.glob import g
import random
from dfttools.hardware.time import apply_time_measure 

import random

def RISE_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure rise time. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'rise_time_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'rise_time', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def FALL_TIME_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure fall time. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'fall_time_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'fall_time', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def POSITIVE_PULSE_WIDTH_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure positive pulse width. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'positive_pulse_width_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'positive_pulse_width', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def NEGATIVE_PULSE_WIDTH_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure negative pulse width. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'negative_pulse_width_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'negative_pulse_width', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def TIME_DELAY_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure time delay. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_delay_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'time_delay', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def POSITIVE_DUTY_CYCLE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure positive duty cycle. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'positive_duty_cycle_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'positive_duty_cycle', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def NEGATIVE_DUTY_CYCLE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure negative duty cycle. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'negative_duty_cycle_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'negative_duty_cycle', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def TIME_PERIOD_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure time period. Return expected value if hardware unavailable.
    """
    hardware_available, measured_value = apply_time_measure(g, signal, reference, 'time_period_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'time_period', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value