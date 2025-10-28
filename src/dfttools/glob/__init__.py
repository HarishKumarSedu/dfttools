
class GlobalContext:
    """Global context for managing hardware availability and callback functions."""
    def __init__(self):
        self.output = []
        self.instructions = {}
        self.dut_description = None

        # Hardware availability flags
        self.voltage_force_hardware_available = False
        self.current_force_hardware_available = False
        self.resistance_force_hardware_available = False
        self.frequency_force_hardware_available = False

        # Callback functions for setting hardware availability and measured values
        self.hardware_callbacks = {
            'voltage_force': None,
            'current_force': None,
            'resistance_force': None,
            'frequency_force': None,
            'voltage_measure': None,
            'current_measure': None,
            'resistance_measure': None,
            'frequency_measure': None,
            'voltage_force_sweep': None,
            'current_force_sweep': None,
            'resistance_force_sweep':None ,
            'frequency_force_sweep':None ,
            'i2c_read':None ,
            'i2c_write':None ,
            'i2c_reg_read':None ,
            'i2c_reg_write':None ,
            'i2c_bit_read':None ,
            'i2c_bit_write':None ,
            'voltage_trigger_hl': None,
            'voltage_trigger_lh': None,
            'voltage_trigger_lg': None,
            'current_trigger_hl': None,
            'current_trigger_lh': None,
            'fft_compute': None,
            'rise_time_measure': None,
            'fall_time_measure': None,
            'positive_pulse_width_measure': None,
            'negative_pulse_width_measure': None,
            'time_delay_measure': None,
            'positive_duty_cycle_measure': None,
            'negative_duty_cycle_measure': None,
            'time_period_measure': None,
            'signal_phase_measure': None,
            'signal_peak_to_peak_measure': None,
            'signal_rms_measure': None,
            'signal_mean_measure': None,
            'signal_spectrum_measure': None,
            'signal_min_measure': None,
            'signal_max_measure': None,
            'signal_high_measure': None,
            'signal_low_measure': None,
            'signal_amplitude_measure': None,
            'signal_positive_pulse_count_measure': None,
            'signal_negative_pulse_count_measure': None,
            'signal_raising_edge_count_measure': None,
            'signal_falling_edge_count_measure': None,


        }
    @property
    def callback_keys(self):
        return self.hardware_callbacks.keys()
g = GlobalContext()
