from dfttools.glob import g
from dfttools.hardware.measure import apply_force_and_measure
import random
def VMEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0):
    """
    Measure voltage between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference,  'voltage_measure')
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def AMEASURE(signal: str = 'VCC', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0):
    """
    Measure current between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference,  'current_measure')
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def RESMEASURE(signal: str = 'R1', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0):
    """
    Measure resistance between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, 'resistance_measure')
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value

def FREQMEASURE(signal: str = 'CLK', reference: str = 'GND', expected_value: (int|float) = 0.0,error_spread=0.0):
    """
    Measure frequency between a signal and a reference. Return expected value if hardware is unavailable.
    """
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, 'frequency_measure')
    if not hardware_available:
        return expected_value+random.uniform(-error_spread,error_spread)
    
    g.output.append({'type': 'MEASURE', 'signal': signal, 'reference': reference, 'measured_value': measured_value})
    return measured_value