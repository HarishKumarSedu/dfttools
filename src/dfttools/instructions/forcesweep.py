from typing import Union
from ..glob import g
from ..units.volt import Volt, V
from ..units.current import Current, A
from ..units.resistance import Resistance, Ohm
from ..units.frequency import Frequency, Hz
from ..units.time import Time, S
from ..ops.forcesweepops import VoltageForceSweepOperation, CurrentForceSweepOperation, ResistanceForceSweepOperation, ClockForceSweepOperation

# Voltage Force Sweep Operation
def VFORCESWEEP(signal: str, unit: Volt = V, reference: str = 'GND', 
                initialvalue: Union[int, float] = 0.0, finalvalue: Union[int, float] = 5.0,
                stepsize: Union[int, float] = 1.0, stepunit: Volt = V, 
                timestep: Union[int, float] = 0.1, timestepunit: Time = S, comment: str = ''):
    """
    Creates a voltage force sweep operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Volt): The unit of measurement (default is Volts).
        reference (str): The reference signal (default is 'GND').
        initialvalue (Union[int, float]): The starting voltage value for sweeping.
        finalvalue (Union[int,float]): The ending voltage value for sweeping.
        stepsize (Union[int,float]): The increment/decrement step size for voltage.
        stepunit (Volt): The unit for the step size (default is Volts).
        timestep (Union[int,float]): The time between steps in voltage sweep.
        timestepunit (Time): The unit for the time step in voltage sweep (default is Seconds).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    vforcesweep = VoltageForceSweepOperation(unit=unit,
                                               signal=signal,
                                               reference=reference,
                                               initialvalue=initialvalue,
                                               finalvalue=finalvalue,
                                               stepsize=stepsize,
                                               stepunit=stepunit,
                                               timestep=timestep,
                                               timestepunit=timestepunit,
                                               comment=comment)
    g.output.append(vforcesweep)
    return vforcesweep.to_dict()


# Current Force Sweep Operation
def AFORCESWEEP(signal: str, unit: Current = A, reference: str = 'GND', 
                initialvalue: Union[int, float] = 0.0, finalvalue: Union[int, float] = 5.0,
                stepsize: Union[int, float] = 1.0, stepunit: Current = A, 
                timestep: Union[int, float] = 0.1, timestepunit: Time = S, comment: str = ''):
    """
    Creates a current force sweep operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Current): The unit of measurement (default is Amperes).
        reference (str): The reference signal (default is 'GND').
        initialvalue (Union[int,float]): The starting current value for sweeping.
        finalvalue (Union[int,float]): The ending current value for sweeping.
        stepsize (Union[int,float]): The increment/decrement step size for current.
        stepunit (Current): The unit for the step size (default is Amperes).
        timestep (Union[int,float]): The time between steps in current sweep.
        timestepunit (Time): The unit for the time step in current sweep (default is Seconds).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    aforcesweep = CurrentForceSweepOperation(unit=unit,
                                               signal=signal,
                                               reference=reference,
                                               initialvalue=initialvalue,
                                               finalvalue=finalvalue,
                                               stepsize=stepsize,
                                               stepunit=stepunit,
                                               timestep=timestep,
                                               timestepunit=timestepunit,
                                               comment=comment)
    g.output.append(aforcesweep)
    return aforcesweep.to_dict()
# Resistance Force Sweep Operation
def RESFORCESWEEP(signal: str, unit: Resistance = Ohm, reference: str = 'GND', 
                  initialvalue: Union[int, float] = 0.0, finalvalue: Union[int, float] = 10.0,
                  stepsize: Union[int, float] = 1.0, stepunit: Resistance = Ohm, 
                  timestep: Union[int, float] = 0.1, timestepunit: Time = S, comment: str = ''):
    """
    Creates a resistance force sweep operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Resistance): The unit of measurement (default is Ohms).
        reference (str): The reference signal (default is 'GND').
        initialvalue (Union[int,float]): The starting resistance value for sweeping.
        finalvalue (Union[int,float]): The ending resistance value for sweeping.
        stepsize (Union[int,float]): The increment/decrement step size for resistance.
        stepunit (Resistance): The unit for the step size (default is Ohms).
        timestep (Union[int,float]): The time between steps in resistance sweep.
        timestepunit (Time): The unit for the time step in resistance sweep (default is Seconds).
        comment (str, optional): Optional comment for the operation. Defaults to ''.
    """
    resforcesweep = ResistanceForceSweepOperation(unit=unit,
                                                  signal=signal,
                                                  reference=reference,
                                                  initialvalue=initialvalue,
                                                  finalvalue=finalvalue,
                                                  stepsize=stepsize,
                                                  stepunit=stepunit,
                                                  timestep=timestep,
                                                  timestepunit=timestepunit,
                                                  comment=comment)
    g.output.append(resforcesweep)
    return resforcesweep.to_dict()


# Clock Force Sweep Operation
def CLKFORCESWEEP(signal: str, unit: Frequency = Hz, reference: str = 'GND', 
                  initialvalue: Union[int, float] = 1.0, finalvalue: Union[int, float] = 10.0,
                  stepsize: Union[int, float] = 1.0, stepunit: Frequency = Hz, 
                  timestep: Union[int, float] = 0.1, timestepunit: Time = S, comment: str = ''):
    """
    Creates a clock force sweep operation.

    Args:
        signal (str): The signal to apply the force.
        unit (Frequency): The unit of measurement (default is Hertz).
        reference (str): The reference signal (default is 'GND').
        initialvalue (Union[int,float]): The starting clock frequency value for sweeping.
        finalvalue (Union[int,float]): The ending clock frequency value for sweeping.
        stepsize (Union[int,float]): The increment/decrement step size for clock frequency sweep.
        stepunit(Frequency) : Unit of Step Size
        timestep : Time between Steps
        timestepunits : Unit of Time Steps
        comment(str) : Optional comment for the operation. Defaults to ''.
    """
    clkforcesweep = ClockForceSweepOperation(unit=unit,
                                             signal=signal,
                                             reference=reference,
                                             initialvalue=initialvalue,
                                             finalvalue=finalvalue,
                                             stepsize=stepsize,
                                             stepunit=stepunit,
                                             timestep=timestep,
                                             timestepunit=timestepunit,
                                             comment=comment)
    g.output.append(clkforcesweep)
    return clkforcesweep.to_dict()
