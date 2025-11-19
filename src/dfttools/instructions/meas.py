from dfttools.glob import g
from dfttools.hardware.measure import apply_force_and_measure,fft_measure
import random
from typing import Literal, Optional, Dict, Union
import random

def VMEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0,*args, **kwargs):
    """
    Measure voltage between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference,  'voltage_measure',expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def AMEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0,*args, **kwargs):
    """
    Measure current between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference,  'current_measure',expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def RESMEASURE(signal: str = 'R1', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0,*args, **kwargs):
    """
    Measure resistance between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, 'resistance_measure',expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def FREQMEASURE(signal: str = 'CLK', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0,*args, **kwargs):
    """
    Measure frequency between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, 'frequency_measure',expected_value=expected_value,*args, **kwargs)
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value
def FFT(
    signal: str = 'CLK',
    reference: str = 'GND',
    signal_type: Literal['Analog', 'Digital'] = 'Analog',
    sample_number: int = 0,
    sample_time: Union[int, float] = 0.0,
    window: str = 'Hanning',
    expected_values: Optional[Dict[str, float]] = None,
    error_spreads: Optional[Dict[str, float]] = None,
    *args, **kwargs
) -> Dict[str, float]:
    expected_values = expected_values or {}
    error_spreads = error_spreads or {}

    hardware_available, measured_values = fft_measure(
        g, signal, reference, signal_type, sample_number,
        sample_time, window, list(expected_values.keys()), 'fft_compute',*args, **kwargs
    )

    if not hardware_available:
        adjusted_values = {}
        for key in expected_values:
            value = expected_values[key]
            spread = error_spreads.get(key, 0)
            adjusted_values[key] = value + random.uniform(-spread, spread)
        return adjusted_values

    return measured_values