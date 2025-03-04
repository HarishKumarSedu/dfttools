from ..enum import Enum

class Current(Enum):
    pA = 0  # Picoamperes
    nA = 1  # Nanoamperes
    uA = 2  # Microamperes
    mA = 3  # Milliamperes
    A = 4   # Amperes

    def __init__(self, v: int):
        super().__init__(v, [(self.pA, 'pA'),
                             (self.nA, 'nA'),
                             (self.uA, 'uA'),
                             (self.mA, 'mA'),
                             (self.A, 'A')])

# Creating instances for easy access
pA = Current(Current.pA)
nA = Current(Current.nA)
uA = Current(Current.uA)
mA = Current(Current.mA)
A = Current(Current.A)

__all__ = ['Current', 'pA', 'nA', 'uA', 'mA', 'A']
