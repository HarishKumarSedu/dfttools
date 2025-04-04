from enum import Enum

class Frequency(Enum):
    Hz = 'Hz'  # Hertz (1)
    kHz = 'kHz'  # Kilohertz (10^3)
    MHz = 'MHz'  # Megahertz (10^6)
    GHz = 'GHz'  # Gigahertz (10^9)

base_values = {
    Frequency.Hz.value: 1,
    Frequency.kHz.value: 1e3,
    Frequency.MHz.value: 1e6,
    Frequency.GHz.value: 1e9,
}
