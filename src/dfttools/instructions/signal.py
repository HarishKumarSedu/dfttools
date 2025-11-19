from dfttools.glob import g
from dfttools.hardware.signal import apply_signal_measure
import random 
import random

def SIGNAL_PHASE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_phase_measure', expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_phase', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_PEAK_TO_PEAK_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_peak_to_peak_measure', expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_peak_to_peak', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_RMS_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_rms_measure', expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_rms', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_MEAN_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_mean_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_mean', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_SPECTRUM_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value=None, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_spectrum_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value if expected_value is not None else {}
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_spectrum', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_MIN_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_min_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_min', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_MAX_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_max_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_max', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_HIGH_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_high_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_high', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_LOW_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_low_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_low', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_AMPLITUDE_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: float = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_amplitude_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value + random.uniform(-error_spread, error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_amplitude', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_POSITIVE_PULSE_COUNT_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: int = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_positive_pulse_count_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_positive_pulse_count', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_NEGATIVE_PULSE_COUNT_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: int = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_negative_pulse_count_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_negative_pulse_count', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_RAISING_EDGE_COUNT_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: int = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_raising_edge_count_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_raising_edge_count', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def SIGNAL_FALLING_EDGE_COUNT_MEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: int = 0.0, error_spread=0.0,*args, **kwargs):
    hardware_available, measured_value = apply_signal_measure(g, signal, reference, 'signal_falling_edge_count_measure',  expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    g.output.append({'type': 'MEASURE', 'measurement': 'signal_falling_edge_count', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value
