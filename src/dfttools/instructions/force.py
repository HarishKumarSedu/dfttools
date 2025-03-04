from typing import Union, Dict
from ..exceptions import ParsingError

from ..units.volt import Volt, V
from ..units.current import Current, A
from ..units.resistance import Resistance, Ohm
from ..units.frequency import Frequency, Hz  # Assuming this is still needed for other parts

from ..glob import g

from ..ops.forceops import VoltageForceOperation, CurrentForceOperation, ResistanceForceOperation, ClockForceOperation


# FIXME: make signal and reference actual python names by importing pin names
def VFORCE(signal: str, unit: Volt = V, comment: str = ''):
    """
    Creates a voltage force operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Volt): The unit of measurement (default is Volts).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(VoltageForceOperation(unit=unit,
                                           signal=signal,
                                           reference='GND',
                                           comment=comment))


def DVFORCE(signal: str, reference: str, unit: Volt = V, comment: str = ''):
    """
    Creates a differential voltage force operation.

    Args:
        signal (str): The primary signal to apply the force.
        reference (str): The reference signal.
        unit (Volt): The unit of measurement (default is Volts).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(VoltageForceOperation(unit=unit,
                                           signal=signal,
                                           reference=reference,
                                           comment=comment))


def AFORCE(signal: str, unit: Current = A, comment: str = ''):
    """
    Creates a current force operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Current): The unit of measurement (default is Amperes).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(CurrentForceOperation(unit=unit,
                                           signal=signal,
                                           reference='GND',
                                           comment=comment))


def DAFORCE(signal: str, reference: str, unit: Current = A, comment: str = ''):
    """
    Creates a differential current force operation.

    Args:
        signal (str): The primary signal to apply the force.
        reference (str): The reference signal.
        unit (Current): The unit of measurement (default is Amperes).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(CurrentForceOperation(unit=unit,
                                           signal=signal,
                                           reference=reference,
                                           comment=comment))


def RESFORCE(signal: str, unit: Resistance = Ohm, comment: str = ''):
    """
    Creates a resistance force operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Resistance): The unit of measurement (default is Ohms).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(ResistanceForceOperation(unit=unit,
                                              signal=signal,
                                              reference='GND',
                                              comment=comment))


def DRESFORCE(signal: str, reference: str, unit: Resistance = Ohm, comment: str = ''):
    """
    Creates a differential resistance force operation.

    Args:
        signal (str): The primary signal to apply the force.
        reference (str): The reference signal.
        unit (Resistance): The unit of measurement (default is Ohms).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(ResistanceForceOperation(unit=unit,
                                              signal=signal,
                                              reference=reference,
                                              comment=comment))


def CLKFORCE(signal: str, unit: Frequency = Hz, comment: str = ''):
    """
    Creates a clock force operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Frequency): The unit of measurement (default is Hertz).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(ClockForceOperation(unit=unit,
                                         signal=signal,
                                         reference='GND',
                                         comment=comment))


def DCLKFORCE(signal: str, reference: str, unit: Frequency = Hz, comment: str = ''):
    """
    Creates a differential clock force operation.

    Args:
        signal (str): The primary signal to apply the force.
        reference (str): The reference signal.
        unit (Frequency): The unit of measurement (default is Hertz).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    g.output.append(ClockForceOperation(unit=unit,
                                         signal=signal,
                                         reference=reference,
                                         comment=comment))
