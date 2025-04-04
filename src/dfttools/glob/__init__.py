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
            'voltage': None,
            'current': None,
            'resistance': None,
            'frequency': None
        }

g = GlobalContext()