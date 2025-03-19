import json
from typing import Union
from ..enum import Enum
from . import Instructions

class ForceTestOperation(Enum):
    FORCE = Instructions.FORCE

    def __init__(self, t: int, signal1: str = None, signal2: str = None,
                 comment: str = "", unit: Enum = None, value: Union[int, float] = None,
                 variable: Enum = None, **kwargs):
        """
        Initializes a ForceTestOperation.

        Args:
            t (int): The type of test operation.
            signal1 (str, optional): The primary signal. Defaults to None.
            signal2 (str, optional): The secondary signal. Defaults to None.
            comment (str, optional): A comment for the operation. Defaults to "".
            unit (Enum, optional): The unit of measurement. Defaults to None.
            value (Union[int, float], optional): The value to apply for the force operation. Defaults to None.
            variable (Enum, optional): Additional variable for the operation. Defaults to None.
            **kwargs: Additional keyword arguments.
        """
        self._unit = unit
        self._comment = comment
        self._signal1 = signal1
        self._signal2 = signal2
        self._value = value
        self._variable = variable
        super().__init__(t, zip(Instructions.values(), Instructions.keys()))

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': 'FORCE',
            'signal1': self._signal1,
            'signal2': self._signal2,
            'unit': str(self._unit) if self._unit else None,
            'value': self._value,
            'variable': str(self._variable) if self._variable else None,
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())

    def __repr__(self):
        """
        Returns a string representation of the ForceTestOperation.

        Returns:
            str: A string representation of the operation.
        """
        return f'Force Test Operation: {self._signal1} wrt {self._signal2}, ' \
               f'value: {self._value}, unit: {self._unit}, variable: {self._variable}, ' \
               f'{"( " + self._comment + " )" if self._comment else ""}'

class VoltageForceOperation(ForceTestOperation):
    def __init__(self, unit: Enum, signal: str, value: Union[float, int],
                 reference: str = 'GND', comment=None):
        """
        Initializes a VoltageForceOperation.

        Args:
            unit (Enum): The unit of voltage force
            signal (str): The signal to force
            value (Union[float, int]): Force value to apply
            reference (str, optional): Reference signal. Defaults to 'GND'
            comment (str, optional): Operation comment. Defaults to None
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, 
                         unit=unit, value=value)
    def to_json(self):
        return super().to_json()
    
    def __repr__(self):
        return super().__repr__()

    def to_dict(self) -> dict:
        return  super().to_dict()

class CurrentForceOperation(ForceTestOperation):
    def __init__(self, unit: Enum, signal: str, value: Union[float, int],
                 reference: str = 'GND', comment=None):
        """
        Initializes a CurrentForceOperation.

        Args:
            unit (Enum): The unit of current force
            signal (str): The signal to force
            value (Union[float, int]): Force value to apply
            reference (str, optional): Reference signal. Defaults to 'GND'
            comment (str, optional): Operation comment. Defaults to None
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, 
                         unit=unit, value=value)
    def to_json(self):
        return super().to_json()
    def __repr__(self):
        return super().__repr__()

    def to_dict(self) -> dict:
        return  super().to_dict()

class ResistanceForceOperation(ForceTestOperation):
    def __init__(self, unit: Enum, signal: str, value: Union[float, int],
                 reference: str = 'GND', comment=None):
        """
        Initializes a ResistanceForceOperation.

        Args:
            unit (Enum): The unit of resistance force
            signal (str): The signal to force
            value (Union[float, int]): Force value to apply
            reference (str, optional): Reference signal. Defaults to 'GND'
            comment (str, optional): Operation comment. Defaults to None
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, 
                         unit=unit, value=value)
    def to_json(self):
        return super().to_json()
    def __repr__(self):
        return super().__repr__()

    def to_dict(self) -> dict:
        return  super().to_dict()

class ClockForceOperation(ForceTestOperation):
    def __init__(self, unit: Enum, signal: str, value: Union[float, int],
                 reference: str = 'GND', comment=None):
        """
        Initializes a ClockForceOperation.

        Args:
            unit (Enum): The unit of clock frequency
            signal (str): The signal to force
            value (Union[float, int]): Force value to apply
            reference (str, optional): Reference signal. Defaults to 'GND'
            comment (str, optional): Operation comment. Defaults to None
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, 
                         unit=unit, value=value)
    def to_json(self):
        return super().to_json()
    def __repr__(self):
        return super().__repr__()

    def to_dict(self) -> dict:
        return  super().to_dict()
