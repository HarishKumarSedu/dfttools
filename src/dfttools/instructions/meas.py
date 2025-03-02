from typing import Union, Dict
from ..exceptions import ParsingError

from ..units.volt import Volt, V

from ..glob import g

from ..ops import VoltageMeasOperation


# FIXME: make signal and reference actual python names by importing pin names
def VMEAS(signal: str, unit: Volt = V, comment = ''):
    g.output.append(VoltageMeasOperation(unit = unit,
                                         signal = signal,
                                         reference = 'GND',
                                         comment = comment))


def DVMEAS(signal: str, reference: str, unit: Volt = V, comment = ''):
    g.output.append(VoltageMeasOperation(unit = unit,
                                         signal = signal,
                                         reference = reference,
                                         comment = comment))
