### Time Measurement API Documentation

These functions measure time-related signal parameters relative to a reference. If hardware is unavailable, they return a fallback `expected_value` with optional simulated noise.

***

#### API Function Calls and Description

- **`RISE_TIME_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures rise time — duration for signal to transition from low to high.
Returns: `float`
- **`FALL_TIME_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures fall time — duration for signal to transition from high to low.
Returns: `float`
- **`POSITIVE_PULSE_WIDTH_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures positive pulse width duration.
Returns: `float`
- **`NEGATIVE_PULSE_WIDTH_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures negative pulse width duration.
Returns: `float`
- **`TIME_DELAY_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures delay time between signal events.
Returns: `float`
- **`POSITIVE_DUTY_CYCLE_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures positive duty cycle percentage of the signal.
Returns: `float` (percentage)
- **`NEGATIVE_DUTY_CYCLE_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures negative duty cycle percentage of the signal.
Returns: `float` (percentage)
- **`TIME_PERIOD_MEASURE(signal='VCC', reference='GND', expected_value=0.0, error_spread=0.0)`**
Measures the time period of the signal waveform.
Returns: `float`

***

#### Usage Notes

- All functions rely on the hardware layer function `apply_time_measure` that queries registered hardware callbacks.
- Output is appended to `g.output` with metadata for measurement traceability.
- When hardware is unavailable, the function returns the `expected_value` plus or minus a random error defined by `error_spread`.
- Default parameters allow easy call with just signal and reference names.
