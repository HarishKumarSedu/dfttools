from dfttools.glob import g
from dfttools.hardware.signal import apply_signal_measure
import random 



def SIGNAL_PEAK_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure signal peak value. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_peak_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_PEAK_TO_PEAK_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure signal peak-to-peak value. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_peak_to_peak_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_RMS_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure RMS value of a signal. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_rms_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_AVERAGE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure average value of a signal. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_average_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_SPECTRUM_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value=None, error_spread=0.0):
    """
    Measure signal spectrum. Return expected value if hardware is unavailable.
    Expected value can be None or a spectrum representation.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_spectrum_measure', expected_value=expected_value)
    if not hardware_available:
        # For spectrum, return expected_value or an empty/fake spectrum
        return expected_value if expected_value is not None else {}

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_MIN_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure minimum signal level. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_min_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)

    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_MAX_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0, error_spread=0.0):
    """
    Measure maximum signal level. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_max_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_DUTY_CYCLE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure signal duty cycle. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_duty_cycle_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_NEGATIVE_DUTY_CYCLE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure negative duty cycle of the signal. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_negative_duty_cycle_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_POSITIVE_DUTY_CYCLE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure positive duty cycle of the signal. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_positive_duty_cycle_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_PHASE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0):
    """
    Measure signal phase relative to reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_phase_measure', expected_value=expected_value)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value
