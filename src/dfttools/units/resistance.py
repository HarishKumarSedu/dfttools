from ..enum import Enum

class Resistance(Enum):
    """
    Enumeration for resistance units.
    """
    pOhm = 0  # Picoohm
    nOhm = 1  # Nanoohm
    uOhm = 2 # Microohm
    mOhm = 3  # Milliohm
    Ohm = 4   # Ohm
    kOhm = 5  # Kilohm
    MOhm = 6  # Megaohm
    GOhm = 7  # Gigaohm
    TOhm = 8  # Teraohm

    def __init__(self, v: int):
        super().__init__(v, [(self.pOhm, 'pOhm'),
                             (self.nOhm, 'nOhm'),
                             (self.uOhm, 'uOhm'),
                             (self.mOhm, 'mOhm'),
                             (self.Ohm, 'Ohm'),
                             (self.kOhm, 'kOhm'),
                             (self.MOhm, 'MOhm'),
                             (self.GOhm, 'GOhm'),
                             (self.TOhm, 'TOhm')])

# Creating instances for easy access
pOhm = Resistance(Resistance.pOhm)
nOhm = Resistance(Resistance.nOhm)
uOhm = Resistance(Resistance.uOhm)
mOhm = Resistance(Resistance.mOhm)
Ohm = Resistance(Resistance.Ohm)
kOhm = Resistance(Resistance.kOhm)
MOhm = Resistance(Resistance.MOhm)
GOhm = Resistance(Resistance.GOhm)
TOhm = Resistance(Resistance.TOhm)

__all__ = ['Ohm', 'pOhm', 'nOhm','uOhm', 'mOhm', 'Ohm', 'kOhm', 'MOhm', 'GOhm', 'TOhm']
