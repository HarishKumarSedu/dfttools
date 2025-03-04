
from ..enum import Enum


class Time(Enum):
    ps = 0
    ns = 1
    us = 2
    ms = 3
    s = 4
    S=5

    def __init__(self, v: int):
        super().__init__(v, [(self.ps, 'ps'),
                             (self.ns, 'ns'),
                             (self.us, 'us'),
                             (self.ms, 'ms'),
                             (self.s, 's')])

ps = Time(Time.ps)
ns = Time(Time.ns)
us = Time(Time.us)
ms = Time(Time.ms)
s = Time(Time.s)
S = Time(Time.s)

__all__ = [ 'Time', 'ps', 'ns', 'us', 'ms', 's','S' ]
