from typing import Union, Dict
from ..exceptions import ParsingError

from ..units.volt import Volt, V
from ..units.current import Current, A
from ..units.reistance import Resistance, Ohm
from ..units.frequency import Frequency, Hz

from ..glob import g

from ..ops import VoltageMeasOperation,CurrentMeasOperation,ResistanceMeasOperation,FrequencyMeasOperation


# FIXME: make signal and reference actual python names by importing pin names
ddef VMEAS(signal: str, unit: Volt = V, variable: str = '', comment: str = ''):
    """
    Creates a voltage measurement operation.

    Args:
        signal (str): The signal to measure.
        unit (Volt): The unit of measurement (default is Volts).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(VoltageMeasOperation(unit=unit,
                                         signal=signal,
                                         reference='GND',
                                         variable=variable,
                                         comment=comment))


def DVMEAS(signal: str, reference: str, unit: Volt = V, variable: str = '', comment: str = ''):
    """
    Creates a differential voltage measurement operation.

    Args:
        signal (str): The primary signal to measure.
        reference (str): The reference signal.
        unit (Volt): The unit of measurement (default is Volts).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(VoltageMeasOperation(unit=unit,
                                         signal=signal,
                                         reference=reference,
                                         variable=variable,
                                         comment=comment))


def AMEAS(signal: str, unit: Current = A, variable: str = '', comment: str = ''):
    """
    Creates a current measurement operation.

    Args:
        signal (str): The signal to measure.
        unit (Current): The unit of measurement (default is Amperes).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(CurrentMeasOperation(unit=unit,
                                         signal=signal,
                                         reference='GND',
                                         variable=variable,
                                         comment=comment))


def DAMEAS(signal: str, reference: str, unit: Current = A, variable: str = '', comment: str = ''):
    """
    Creates a differential current measurement operation.

    Args:
        signal (str): The primary signal to measure.
        reference (str): The reference signal.
        unit (Current): The unit of measurement (default is Amperes).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(CurrentMeasOperation(unit=unit,
                                         signal=signal,
                                         reference=reference,
                                         variable=variable,
                                         comment=comment))


def RESMEAS(signal: str, unit: Resistance = Ohm, variable: str = '', comment: str = ''):
    """
    Creates a resistance measurement operation.

    Args:
        signal (str): The signal to measure.
        unit (Resistance): The unit of measurement (default is Ohms).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(ResistanceMeasOperation(unit=unit,
                                         signal=signal,
                                         reference='GND',
                                         variable=variable,
                                         comment=comment))


def DRESMEAS(signal: str, reference: str, unit: Resistance = Ohm, variable: str = '', comment: str = ''):
    """
    Creates a differential resistance measurement operation.

    Args:
        signal (str): The primary signal to measure.
        reference (str): The reference signal.
        unit (Resistance): The unit of measurement (default is Ohms).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(ResistanceMeasOperation(unit=unit,
                                         signal=signal,
                                         reference=reference,
                                         variable=variable,
                                         comment=comment))


def FREQMEAS(signal: str, unit: Frequency = Hz, variable: str = '', comment: str = ''):
    """
    Creates a frequency measurement operation.

    Args:
        signal (str): The signal to measure.
        unit (Frequency): The unit of measurement (default is Hertz).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(FrequencyMeasOperation(unit=unit,
                                         signal=signal,
                                         reference='GND',
                                         variable=variable,
                                         comment=comment))


def DFREQMEAS(signal: str, reference: str, unit: Frequency = Hz, variable: str = '', comment: str = ''):
    """
    Creates a differential frequency measurement operation.

    Args:
        signal (str): The primary signal to measure.
        reference (str): The reference signal.
        unit (Frequency): The unit of measurement (default is Hertz).
        variable (str): Optional variable name.
        comment (str): Optional comment for the operation.
    """
    g.output.append(FrequencyMeasOperation(unit=unit,
                                         signal=signal,
                                         reference=reference,
                                         variable=variable,
                                         comment=comment))

