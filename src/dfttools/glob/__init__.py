
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
            'voltage_trigger_hl': None,
            'voltage_trigger_lh': None,
            'voltage_trigger_lg': None,
            'current_trigger_hl': None,
            'current_trigger_lh': None,
            'current_trigger_lg': None,
        }
    @property
    def callback_keys(self):
        return self.hardware_callbacks.keys()
g = GlobalContext()
