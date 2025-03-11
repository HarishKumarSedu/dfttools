
from ..enum import Enum


class Trig(Enum):
    HL = 0
    LH = 1

    def __init__(self, v: int):
        super().__init__(v, [(self.HL, 'HL'),
                             (self.LH, 'LH')])

LH = Trig(Trig.LH)
HL = Trig(Trig.HL)

__all__ = [ 'LH', 'HL']