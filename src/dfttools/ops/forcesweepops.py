import json
from typing import Union
from ..enum import Enum
from . import Instructions

class ForceSweepTestOperation(Enum):

    FORCESWEEP=Instructions.FORCESWEEP

    def __init__(self, t: int, signal1: str = None, signal2: str = None,
                 comment: str = "", unit: Enum = None, initialvalue: Union[int, float] = None,
                 finalvalue: Union[int, float] = None, stepsize: Union[int, float] = None,
                 stepunit: Enum = None, timestep: Union[int, float] = None,
                 timestepunit: Enum = None, **kwargs):
        """
        Initializes a TestOperation.

        Args:
            t (int): The type of test operation.
            signal1 (str, optional): The primary signal. Defaults to None.
            signal2 (str, optional): The secondary signal. Defaults to None.
            comment (str, optional): A comment for the operation. Defaults to "".
            unit (Enum, optional): The unit of measurement. Defaults to None.
            initialvalue (Union[int, float], optional): Initial value for sweep operations. Defaults to None.
            finalvalue (Union[int, float], optional): Final value for sweep operations. Defaults to None.
            stepsize (Union[int, float], optional): Step size for sweep operations. Defaults to None.
            stepunit (Enum, optional): Unit for step size in sweep operations. Defaults to None.
            timestep (Union[int, float], optional): Time step for sweep operations. Defaults to None.
            timestepunit (Enum, optional): Unit for time step in sweep operations. Defaults to None.
            **kwargs: Additional keyword arguments.
        """
        self._unit = unit
        self._comment = comment
        self._signal1 = signal1
        self._signal2 = signal2
        self._initialvalue = initialvalue
        self._finalvalue = finalvalue
        self._stepsize = stepsize
        self._stepunit = stepunit
        self._timestep = timestep
        self._timestepunit = timestepunit
        super().__init__(t, zip(Instructions.values(),Instructions.keys()))

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': 'FORCESWEEP',
            'signal1': self._signal1,
            'signal2': self._signal2,
            'unit': str(self._unit) if self._unit else None,
            'comment': self._comment,
            'initialvalue': self._initialvalue,
            'finalvalue': self._finalvalue,
            'stepsize': self._stepsize,
            'stepunit': str(self._stepunit) if self._stepunit else None,
            'timestep': self._timestep,
            'timestepunit': str(self._timestepunit) if self._timestepunit else None
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())

class VoltageForceSweepOperation(ForceSweepTestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str, initialvalue: Union[int, float], 
                 finalvalue: Union[int,float], stepsize: Union[int, float], 
                 stepunit: Enum, timestep: Union[int, float], 
                 timestepunit: Enum, comment=None):
         """
         Initializes a VoltageForceSweepOperation.

         Args:
             unit (Enum): The unit for voltage sweeping forces.
             signal (str): The voltage signal for sweeping.
             reference (str): The reference signal.
             initialvalue (Union[int, float]): The starting voltage value for sweeping.
             finalvalue (Union[int,float]): The ending voltage value for sweeping.
             stepsize (Union[int,float]): The increment/decrement step size for voltage.
             stepunit (Enum): The unit for the step size.
             timestep (Union[int,float]): The time between steps in voltage sweep.
             timestepunit (Enum): The unit for the time step in voltage sweep.
             comment (str, optional): A comment for the operation. Defaults to None.
         """
         super().__init__(t=Instructions.FORCESWEEP,
                          signal1=signal,
                          signal2=reference,
                          comment=comment,
                          unit=unit,
                          initialvalue=initialvalue,
                          finalvalue=finalvalue,
                          stepsize=stepsize,
                          stepunit=stepunit,
                          timestep=timestep,
                          timestepunit=timestepunit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        repr_str = f'{what}voltage force Sweep: {self._signal1} wrt {self._signal2}, from {self._initialvalue}{self._unit} to {self._finalvalue}{self._unit}'
        if self._stepsize and self._stepunit:
            repr_str += f', stepsize: {self._stepsize}{self._stepunit}'
        if self._timestep and self._timestepunit:
            repr_str += f', sweeptime: {self._timestep}{self._timestepunit}'
        if self._comment:
            repr_str += f' ( {self._comment} )'
        return repr_str

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        base_dict = super().to_dict()
        base_dict.update({'type': 'VOLTAGEFORCESWEEP'})
        return base_dict

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())

class CurrentForceSweepOperation(ForceSweepTestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str, initialvalue: Union[int, float], 
                 finalvalue: Union[int,float], stepsize: Union[int, float], 
                 stepunit: Enum, timestep: Union[int, float], 
                 timestepunit: Enum, comment=None):
         """
         Initializes a CurrentForceSweepOperation.

         Args:
             unit (Enum): The unit for current sweeping forces.
             signal (str): The current signal for sweeping.
             reference (str): The reference signal.
             initialvalue (Union[int,float]): The starting current value for sweeping.
             finalvalue (Union[int,float]): The ending current value for sweeping.
             stepsize (Union[int,float]): The increment/decrement step size for current.
             stepunit (Enum): The unit for the step size.
             timestep (Union[int,float]): The time between steps in current sweep.
             timestepunit (Enum): The unit for the time step in current sweep.
             comment (str, optional): A comment for the operation. Defaults to None.
         """
         super().__init__(t=Instructions.FORCESWEEP,
                          signal1=signal,
                          signal2=reference,
                          comment=comment,
                          unit=unit,
                          initialvalue=initialvalue,
                          finalvalue=finalvalue,
                          stepsize=stepsize,
                          stepunit=stepunit,
                          timestep=timestep,
                          timestepunit=timestepunit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        repr_str = f'{what}current force Sweep: {self._signal1} wrt {self._signal2}, from {self._initialvalue}{self._unit} to {self._finalvalue}{self._unit}'
        if self._stepsize and self._stepunit:
            repr_str += f', stepsize: {self._stepsize}{self._stepunit}'
        if self._timestep and self._timestepunit:
            repr_str += f', sweeptime: {self._timestep}{self._timestepunit}'
        if self._comment:
            repr_str += f' ( {self._comment} )'
        return repr_str

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        base_dict = super().to_dict()
        base_dict.update({'type': 'CURRENTFORCESWEEP'})
        return base_dict

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())

class ResistanceForceSweepOperation(ForceSweepTestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str, initialvalue: Union[int,float], 
                 finalvalue: Union[int,float], stepsize: Union[int,float], 
                 stepunit: Enum, timestep: Union[int,float], 
                 timestepunit: Enum, comment=None):
         """
         Initializes a ResistanceForceSweepOperation.

         Args:
             unit (Enum): The unit for resistance sweeping forces.
             signal (str): The resistance signal for sweeping.
             reference (str): The reference signal.
             initialvalue (Union[int,float]): The starting resistance value for sweeping.
             finalvalue (Union[int,float]): The ending resistance value for sweeping.
             stepsize (Union[int,float]): The increment/decrement step size for resistance.
             stepunit (Enum): The unit for the step size.
             timestep (Union[int,float]): The time between steps in resistance sweep.
             timestepunit (Enum): The unit for the time step in resistance sweep.
             comment (str, optional): A comment for the operation. Defaults to None.
         """
         super().__init__(t=Instructions.FORCESWEEP,
                          signal1=signal,
                          signal2=reference,
                          comment=comment,
                          unit=unit,
                          initialvalue=initialvalue,
                          finalvalue=finalvalue,
                          stepsize=stepsize,
                          stepunit=stepunit,
                          timestep=timestep,
                          timestepunit=timestepunit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        repr_str = f'{what}resistance force Sweep: {self._signal1} wrt {self._signal2}, from {self._initialvalue}{self._unit} to {self._finalvalue}{self._unit}'
        if self._stepsize and self._stepunit:
            repr_str += f', stepsize: {self._stepsize}{self._stepunit}'
        if self._timestep and self._timestepunit:
            repr_str += f', sweeptime: {self._timestep}{self._timestepunit}'
        if self._comment:
            repr_str += f' ( {self._comment} )'
        return repr_str

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        base_dict = super().to_dict()
        base_dict.update({'type': 'RESISTANCEFORCESWEEP'})
        return base_dict

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())

class ClockForceSweepOperation(ForceSweepTestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str, initialvalue: Union[int,float], 
                 finalvalue: Union[int,float], stepsize: Union[int,float], 
                 stepunit: Enum,timestep : Union[int,float],
                 timestepunit : Enum ,comment=None):
         """
         Initializes a ClockForceSweepOperation.

         Args:
             unit (Enum): The unit for clock frequency sweeping forces.
             signal (str): The clock frequency signal for sweeping.
             reference (str): The reference signal.
             initialvalue (Union[int,float]): The starting clock frequency value for sweeping.
             finalvalue (Union[int,float]): The ending clock frequency value for sweeping.
             stepsize (Union[int,float]): The increment/decrement step size for clock frequency sweep..
             stepunit(Enum) : Unit of Step Size
             timestep : Time between Steps
             timestepunits : Unit of Time Steps
         """
         super().__init__(t=Instructions.FORCESWEEP,
                          signal1=signal,
                          signal2=reference,
                          comment=comment,
                          unit=unit,
                          initialvalue=initialvalue,
                          finalvalue=finalvalue,
                          stepsize=stepsize,
                          stepunit=stepunit,
                          timestep=timestep,
                          timestepunit=timestepunit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        repr_str = f'{what}clock force Sweep: {self._signal1} wrt {self._signal2}, from {self._initialvalue}{self._unit} to {self._finalvalue}{self._unit}'
        if self._stepsize and self._stepunit:
            repr_str += f', stepsize: {self._stepsize}{self._stepunit}'
        if self._timestep and self._timestepunit:
            repr_str += f', sweeptime: {self._timestep}{self._timestepunit}'
        if self._comment:
            repr_str += f' ( {self._comment} )'
        return repr_str

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        base_dict = super().to_dict()
        base_dict.update({'type': 'CLOCKFORCESWEEP'})
        return base_dict

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())
