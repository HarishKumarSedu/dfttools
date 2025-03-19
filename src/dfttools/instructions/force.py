from typing import Union, Dict
from ..exceptions import ParsingError

from ..units.volt import Volt, V
from ..units.current import Current, A
from ..units.resistance import Resistance, Ohm
from ..units.frequency import Frequency, Hz

from ..glob import g

from ..ops.forceops import VoltageForceOperation, CurrentForceOperation, ResistanceForceOperation, ClockForceOperation

def VFORCE(signal: str, value: Union[int, float], unit: Volt = V, comment: str = ''):
    """
    Creates a voltage force operation.

    Args:
        signal (str): The signal to apply the force
        value (Union[int, float]): Voltage value to force
        unit (Volt): Unit of measurement (default Volts)
        comment (str, optional): Optional operation comment
    """
    g.output.append(VoltageForceOperation(unit=unit,
                                          value=value,
                                          signal=signal,
                                          reference='GND',
                                          comment=comment))

def DVFORCE(signal: str, reference: str, value: Union[int, float], unit: Volt = V, comment: str = ''):
    """
    Creates a differential voltage force operation.

    Args:
        signal (str): Primary signal to force
        reference (str): Reference signal
        value (Union[int, float]): Voltage value to force
        unit (Volt): Unit of measurement (default Volts)
        comment (str, optional): Optional operation comment
    """
    g.output.append(VoltageForceOperation(unit=unit,
                                          value=value,
                                          signal=signal,
                                          reference=reference,
                                          comment=comment))

# Similarly updated for all other force functions:

def AFORCE(signal: str, value: Union[int, float], unit: Current = A, comment: str = ''):
    g.output.append(CurrentForceOperation(unit=unit,
                                          value=value,
                                          signal=signal,
                                          reference='GND',
                                          comment=comment))

def DAFORCE(signal: str, reference: str, value: Union[int, float], unit: Current = A, comment: str = ''):
    g.output.append(CurrentForceOperation(unit=unit,
                                          value=value,
                                          signal=signal,
                                          reference=reference,
                                          comment=comment))

def RESFORCE(signal: str, value: Union[int, float], unit: Resistance = Ohm, comment: str = ''):
    g.output.append(ResistanceForceOperation(unit=unit,
                                             value=value,
                                             signal=signal,
                                             reference='GND',
                                             comment=comment))

def DRESFORCE(signal: str, reference: str, value: Union[int, float], unit: Resistance = Ohm, comment: str = ''):
    g.output.append(ResistanceForceOperation(unit=unit,
                                             value=value,
                                             signal=signal,
                                             reference=reference,
                                             comment=comment))

def CLKFORCE(signal: str, value: Union[int, float], unit: Frequency = Hz, comment: str = ''):
    g.output.append(ClockForceOperation(unit=unit,
                                        value=value,
                                        signal=signal,
                                        reference='GND',
                                        comment=comment))

def DCLKFORCE(signal: str, reference: str, value: Union[int, float], unit: Frequency = Hz, comment: str = ''):
    g.output.append(ClockForceOperation(unit=unit,
                                        value=value,
                                        signal=signal,
                                        reference=reference,
                                        comment=comment))
