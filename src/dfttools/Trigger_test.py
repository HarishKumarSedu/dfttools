import random
# from callbacks.trig_custom_callbacks import *
# from glob import g
# from instructions.trigger import *
from dfttools import *
def assign_callbacks(assign: bool):
    """Assign or clear all trigger callbacks in the global context."""
    if assign:
        g.hardware_callbacks.update({
            'voltage_trigger_hl': vtrig_hl_callback,
            'voltage_trigger_lh': vtrig_lh_callback,
            'voltage_trigger_lg': vtrig_lg_callback,
            'current_trigger_hl': atrig_hl_callback,
            'current_trigger_lh': atrig_lh_callback,
            'current_trigger_lg': atrig_lg_callback,
        })
    else:
        for key in g.hardware_callbacks.keys():
            g.hardware_callbacks[key] = None

def test_scenario(hw_voltage: bool, hw_current: bool, callbacks_assigned: bool):
    """Run all trigger functions under specified hardware and callback conditions."""
    print("\n--- Test Scenario ---")
    print(f"Voltage Hardware Available: {hw_voltage}")
    print(f"Current Hardware Available: {hw_current}")
    print(f"Callbacks Assigned: {callbacks_assigned}")

    g.voltage_force_hardware_available = hw_voltage
    g.current_force_hardware_available = hw_current

    assign_callbacks(callbacks_assigned)

    triggers = [
        ('VTRIG_HL', VTRIG_HL, 3.0),
        ('VTRIG_LH', VTRIG_LH, 3.0),
        ('VTRIG_LG', VTRIG_LG, None),
        ('ATRIG_HL', ATRIG_HL, 0.01),
        ('ATRIG_LH', ATRIG_LH, 0.1),
        ('ATRIG_LG', ATRIG_LG, None),
    ]

    signals = ['VCC_CORE', 'PWR_RAIL']
    references = ['GND']

    for name, func, threshold in triggers:
        signal = random.choice(signals)
        reference = random.choice(references)
    
        if threshold is not None:
            noise = random.uniform(-0.2 * threshold, 0.2 * threshold)
            expected_value = threshold + noise
            # Call with threshold
            triggered = func(signal, threshold, reference, expected_value)
        else:
            # LG triggers without threshold
            expected_value = random.uniform(0.0, 0.05) if 'VTRIG' in name else random.uniform(0.0, 0.001)
            triggered = func(signal, reference, expected_value)
    
        print(f"\nTrigger: {name}, Signal: {signal}, Threshold: {threshold}, Expected Value: {expected_value:.4f}")
        print(f"Triggered: {triggered}")


if __name__ == "__main__":
    # Test all combinations of hardware availability and callback assignment
    for hw_v in [True, False]:
        for hw_c in [True, False]:
            for cb_assigned in [True, False]:
                test_scenario(hw_v, hw_c, cb_assigned)
