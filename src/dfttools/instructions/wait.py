from typing import Union
from ..exceptions import ParsingError

from ..units import *

from ..glob import g

from ..ops import WaitOperation

def WAIT(t: Union[int, float], unit: time.Time, comment = ''):
    g.output.append(WaitOperation(unit = unit, delay = t, comment = comment))
