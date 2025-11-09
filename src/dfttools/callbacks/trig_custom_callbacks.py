import random

def vtrig_hl_callback(g, signal, reference, threshold):
    hardware_available = g.voltage_force_hardware_available
    measured_voltage = threshold - 0.1 + random.uniform(-0.2, 0.2)
    triggered = measured_voltage < threshold if hardware_available else False
    print(f"[vtrig_hl_callback] HW avail: {hardware_available}, Measured: {measured_voltage:.3f}, Threshold: {threshold}, Triggered: {triggered}")
    return hardware_available, triggered

def vtrig_lh_callback(g, signal, reference, threshold):
    hardware_available = g.voltage_force_hardware_available
    measured_voltage = threshold + 0.1 + random.uniform(-0.2, 0.2)
    triggered = measured_voltage > threshold if hardware_available else False
    print(f"[vtrig_lh_callback] HW avail: {hardware_available}, Measured: {measured_voltage:.3f}, Threshold: {threshold}, Triggered: {triggered}")
    return hardware_available, triggered

def vtrig_lg_callback(g, signal, reference, _):
    hardware_available = g.voltage_force_hardware_available
    measured_voltage = random.uniform(0, 0.1)
    triggered = measured_voltage < 0.05 if hardware_available else False
    print(f"[vtrig_lg_callback] HW avail: {hardware_available}, Measured: {measured_voltage:.3f}, Triggered: {triggered}")
    return hardware_available, triggered

def atrig_hl_callback(g, signal, reference, threshold):
    hardware_available = g.current_force_hardware_available
    measured_current = threshold - 0.001 + random.uniform(-0.002, 0.002)
    triggered = measured_current < threshold if hardware_available else False
    print(f"[atrig_hl_callback] HW avail: {hardware_available}, Measured: {measured_current:.6f}, Threshold: {threshold}, Triggered: {triggered}")
    return hardware_available, triggered

def atrig_lh_callback(g, signal, reference, threshold):
    hardware_available = g.current_force_hardware_available
    measured_current = threshold + 0.001 + random.uniform(-0.002, 0.002)
    triggered = measured_current > threshold if hardware_available else False
    print(f"[atrig_lh_callback] HW avail: {hardware_available}, Measured: {measured_current:.6f}, Threshold: {threshold}, Triggered: {triggered}")
    return hardware_available, triggered

def atrig_lg_callback(g, signal, reference, _):
    hardware_available = g.current_force_hardware_available
    measured_current = random.uniform(0, 0.001)
    triggered = measured_current < 0.001 if hardware_available else False
    print(f"[atrig_lg_callback] HW avail: {hardware_available}, Measured: {measured_current:.6f}, Triggered: {triggered}")
    return hardware_available, triggered
