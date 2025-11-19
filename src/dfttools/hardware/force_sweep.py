from dfttools.hardware.force import apply_force_and_measure
import time
def apply_force_and_measure_sweep(g, signal, reference, initial_value, end_value, step, step_time, force_type,*args, **kwargs):
    sweep_results = []
    
    # Check hardware availability using the callback if defined
    if g.hardware_callbacks[force_type]:
        current_value = initial_value
        while current_value <= end_value:
            hardware_available, measured_value = apply_force_and_measure(g, signal, reference, current_value, force_type,*args, **kwargs)
            if hardware_available:
                sweep_results.append(measured_value)
                # Simulate waiting for step_time
                time.sleep(step_time)
            current_value += step
    
    return sweep_results
