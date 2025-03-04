from ..enum import Enum

class Frequency(Enum):
    """
    Enumeration for frequency units.
    """
    pHz = 0  # PicoHertz
    nHz = 1  # NanoHertz
    uHz = 2  # MicroHertz
    mHz = 3  # MilliHertz
    Hz = 4   # Hertz
    kHz = 5  # Kilohertz
    MHz = 6  # Megahertz
    GHz = 7  # Gigahertz
    THz = 8  # Terahertz

    def __init__(self, v: int):
        super().__init__(v, [(self.pHz, 'pHz'),
                             (self.nHz, 'nHz'),
                             (self.uHz, 'uHz'),
                             (self.mHz, 'mHz'),
                             (self.Hz, 'Hz'),
                             (self.kHz, 'kHz'),
                             (self.MHz, 'MHz'),
                             (self.GHz, 'GHz'),
                             (self.THz, 'THz')])

# Creating instances for easy access
pHz = Frequency(Frequency.pHz)
nHz = Frequency(Frequency.nHz)
uHz = Frequency(Frequency.uHz)
mHz = Frequency(Frequency.mHz)
Hz = Frequency(Frequency.Hz)
kHz = Frequency(Frequency.kHz)
MHz = Frequency(Frequency.MHz)
GHz = Frequency(Frequency.GHz)
THz = Frequency(Frequency.THz)

__all__ = ['Frequency', 'pHz', 'nHz', 'uHz', 'mHz', 'Hz', 'kHz', 'MHz', 'GHz', 'THz']
