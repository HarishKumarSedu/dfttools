
from ..enum import Enum


class Volt(Enum):
    nV = 0
    uV = 1
    mV = 2
    V = 3

    def __init__(self, v: int):
        super().__init__(v, [(self.nV, 'nV'),
                             (self.uV, 'uV'),
                             (self.mV, 'mV'),
                             (self.V, 'V')])

nV = Volt(Volt.nV)
uV = Volt(Volt.uV)
mV = Volt(Volt.mV)
V = Volt(Volt.V)

__all__ = [ 'Volt', 'nV', 'uV', 'mV', 'V' ]
