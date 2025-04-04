from dfttools.hardware.force import apply_force_and_measure
import time
def apply_force_and_measure_sweep(g, signal, reference, initial_value, end_value, step, step_time, force_type):
    """
    Perform a sweep operation by applying values from initial_value to end_value with specified step and step_time.
    
    Args:
        g (GlobalContext): The global context.
        signal (str): The signal name.
        reference (str): The reference signal.
        initial_value (float): The starting value of the sweep.
        end_value (float): The ending value of the sweep.
        step (float): The step size for the sweep.
        step_time (float): The time to wait between each step.
        force_type (str): The type of force operation ('voltage_force', 'current_force', etc.).
    
    Returns:
        list: A list of measured values at each step of the sweep.
    """
    sweep_results = []
    
    # Check hardware availability using the callback if defined
    if g.hardware_callbacks[force_type]:
        current_value = initial_value
        while current_value <= end_value:
            hardware_available, measured_value = apply_force_and_measure(g, signal, reference, current_value, force_type)
            if hardware_available:
                sweep_results.append(measured_value)
                # Simulate waiting for step_time
                time.sleep(step_time)
            current_value += step
    
    return sweep_results
