def apply_trig_and_measure(g, signal, reference, threshold, force_type, simulated_measured_value=None,*args, **kwargs):
    """
    Apply trigger check and measure using hardware callback if available.
    If hardware unavailable, use simulated_measured_value to compare with threshold:
      - HL triggers: True if measured_value < threshold
      - LH triggers: True if measured_value > threshold

    Args:
        g: Global context.
        signal: Signal name.
        reference: Reference signal.
        threshold: Threshold for trigger.
        force_type: Type of trigger (e.g., 'voltage_trigger_hl').
        simulated_measured_value: Simulated measurement if hardware unavailable.

    Returns:
        (hardware_available: bool, triggered: bool)
    """
    callback = g.hardware_callbacks.get(force_type)
    if callback:
        hardware_available, triggered = callback(signal=signal, reference=reference, threshold=threshold,simulated_measured_value=simulated_measured_value,*args, **kwargs)
        if hardware_available:
            return hardware_available, triggered

    # Hardware not available, fallback to software check
    if simulated_measured_value is None:
        raise ValueError("Simulated measured value must be provided if hardware is unavailable.")
    if force_type.endswith('_hl'):  # High-to-Low trigger
        triggered = simulated_measured_value < threshold
    elif force_type.endswith('_lh'):  # Low-to-High trigger
        triggered = simulated_measured_value > threshold
    elif force_type.endswith('_lg'):  # Low-Ground trigger (special case)
        triggered = simulated_measured_value < 0.05
    else:
        # Default fallback
        triggered = False

    return False, triggered
