from dfttools.glob import g
from dfttools.hardware.force import apply_force_and_measure
       
def VFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    harware_availabel,measured_value = apply_force_and_measure(g, signal, reference, value, 'voltage_force')
    if not  harware_availabel:
        return {'signal': signal, 'reference': reference, 'value': value}
    
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value

def AFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'current_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value

def RESFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'resistance_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value

def FREQFORCE(signal: str = 'VCC', reference: str = 'GND', value: float = 0.0):
    hardware_available, measured_value = apply_force_and_measure(g, signal, reference, value, 'frequency_force')
    if not hardware_available:
        return {'signal': signal, 'reference': reference, 'value': value}
    
    g.output.append({'type': 'FORCE', 'signal': signal, 'reference': reference, 'value': value})
    return measured_value
