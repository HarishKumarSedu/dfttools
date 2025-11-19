from dfttools.glob import g
from dfttools.hardware.trig import apply_trig_and_measure

def VTRIG_HL(signal: str='VCC',  reference: str = 'GND', threshold: float=0.0, expected_value: float = 2.7,*args, **kwargs):
    """
    Voltage trigger: High-to-Low (trigger when voltage drops below threshold).
    """
    simulated_measured_value = expected_value
    hardware_available, triggered = apply_trig_and_measure(
        g, signal, reference, threshold, 'voltage_trigger_hl', simulated_measured_value,
        *args, **kwargs
    )
    g.output.append({'type': 'TRIGGER', 'trigger': 'VTRIG_HL', 'signal': signal, 'triggered': triggered})
    return triggered


def VTRIG_LH(signal: str='VCC', reference: str = 'GND', threshold: float=0.0,expected_value: float = 3.3,*args, **kwargs):
    """
    Voltage trigger: Low-to-High (trigger when voltage rises above threshold).
    """
    simulated_measured_value = expected_value
    hardware_available, triggered = apply_trig_and_measure(
        g, signal, reference, threshold, 'voltage_trigger_lh', simulated_measured_value,
         *args, **kwargs
    )
    g.output.append({'type': 'TRIGGER', 'trigger': 'VTRIG_LH', 'signal': signal, 'triggered': triggered})
    return triggered


def VTRIG_LG(signal: str='VCC', reference: str = 'GND', expected_value: float = 0.02,*args, **kwargs):
    """
    Voltage trigger: Low-to-Ground (trigger when voltage is near ground).
    Threshold is fixed internally (0.05V).
    """
    simulated_measured_value = expected_value
    hardware_available, triggered = apply_trig_and_measure(
        g, signal, reference, None, 'voltage_trigger_lg', simulated_measured_value,
        *args, **kwargs
    )
    g.output.append({'type': 'TRIGGER', 'trigger': 'VTRIG_LG', 'signal': signal, 'triggered': triggered})
    return triggered


def ATRIG_HL(signal: str='VCC', reference: str = 'GND',threshold: float=0.0,  expected_value: float = 0.005,*args, **kwargs):
    """
    Current trigger: High-to-Low (trigger when current drops below threshold).
    """
    simulated_measured_value = expected_value
    hardware_available, triggered = apply_trig_and_measure(
        g, signal, reference, threshold, 'current_trigger_hl', simulated_measured_value,
        *args, **kwargs
    )
    g.output.append({'type': 'TRIGGER', 'trigger': 'ATRIG_HL', 'signal': signal, 'triggered': triggered})
    return triggered


def ATRIG_LH(signal: str='VCC',reference: str = 'GND',threshold: float=0.0,  expected_value: float = 0.15,*args, **kwargs):
    """
    Current trigger: Low-to-High (trigger when current rises above threshold).
    """
    simulated_measured_value = expected_value
    hardware_available, triggered = apply_trig_and_measure(
        g, signal, reference, threshold, 'current_trigger_lh', simulated_measured_value,
        *args, **kwargs
    )
    g.output.append({'type': 'TRIGGER', 'trigger': 'ATRIG_LH', 'signal': signal, 'triggered': triggered})
    return triggered


def ATRIG_LG(signal: str='VCC', reference: str = 'GND', expected_value: float = 0.001,*args, **kwargs):
    """
    Current trigger: Low-to-Ground (trigger when current is near zero).
    Threshold is fixed internally (0.001A).
    """
    simulated_measured_value = expected_value
    hardware_available, triggered = apply_trig_and_measure(
        g, signal, reference, None, 'current_trigger_lg', simulated_measured_value,
        *args, **kwargs
    )
    g.output.append({'type': 'TRIGGER', 'trigger': 'ATRIG_LG', 'signal': signal, 'triggered': triggered})
    return triggered
