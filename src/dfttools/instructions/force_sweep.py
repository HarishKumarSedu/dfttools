from glob import g
from hardware.force_sweep import apply_force_and_measure_sweep

def VFORCESWEEP(signal: str = 'VCC', reference: str = 'GND', initial_value: float = 0.0, end_value: float = 5.0, step: float = 0.1, step_time: float = 0.01):
    """
    Perform a voltage sweep from initial_value to end_value with specified step and step_time.
    """
    sweep_results = apply_force_and_measure_sweep(g, signal, reference, initial_value, end_value, step, step_time, 'voltage_force_sweep')
    if not sweep_results:
        return {'signal': signal, 'reference': reference, 'sweep_results': []}
    
    g.output.append({'type': 'SWEEP', 'signal': signal, 'reference': reference, 'sweep_results': sweep_results})
    return sweep_results

def AFORCESWEEP(signal: str = 'VCC', reference: str = 'GND', initial_value: float = 0.0, end_value: float = 5.0, step: float = 0.1, step_time: float = 0.01):
    """
    Perform a current sweep from initial_value to end_value with specified step and step_time.
    """
    sweep_results = apply_force_and_measure_sweep(g, signal, reference, initial_value, end_value, step, step_time, 'current_force_sweep')
    if not sweep_results:
        return {'signal': signal, 'reference': reference, 'sweep_results': []}
    
    g.output.append({'type': 'SWEEP', 'signal': signal, 'reference': reference, 'sweep_results': sweep_results})
    return sweep_results

def RESFORCESWEEP(signal: str = 'R1', reference: str = 'GND', initial_value: float = 0.0, end_value: float = 1000.0, step: float = 10.0, step_time: float = 0.01):
    """
    Perform a resistance sweep from initial_value to end_value with specified step and step_time.
    """
    sweep_results = apply_force_and_measure_sweep(g, signal, reference, initial_value, end_value, step, step_time, 'resistance_force_sweep')
    if not sweep_results:
        return {'signal': signal, 'reference': reference, 'sweep_results': []}
    
    g.output.append({'type': 'SWEEP', 'signal': signal, 'reference': reference, 'sweep_results': sweep_results})
    return sweep_results

def FREQFORCESWEEP(signal: str = 'CLK', reference: str = 'GND', initial_value: float = 0.0, end_value: float = 100.0, step: float = 1.0, step_time: float = 0.01):
    """
    Perform a frequency sweep from initial_value to end_value with specified step and step_time.
    """
    sweep_results = apply_force_and_measure_sweep(g, signal, reference, initial_value, end_value, step, step_time, 'frequency_force_sweep')
    if not sweep_results:
        return {'signal': signal, 'reference': reference, 'sweep_results': []}
    
    g.output.append({'type': 'SWEEP', 'signal': signal, 'reference': reference, 'sweep_results': sweep_results})
    return sweep_results
