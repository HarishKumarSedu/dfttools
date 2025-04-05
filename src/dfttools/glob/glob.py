
class CallbackMeta(type):
    """Metaclass to inject callback keys as class meta information."""
    def __new__(cls, name, bases, dct):
        # Add callback keys as meta information
        dct['callback_keys'] = list(dct.get('hardware_callbacks', {}).keys())
        return super().__new__(cls, name, bases, dct)

class GlobalContext(metaclass=CallbackMeta):
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
        }
    @property
    def __call__(self):
        return list(self.hardware_callbacks.keys())
g = GlobalContext()
