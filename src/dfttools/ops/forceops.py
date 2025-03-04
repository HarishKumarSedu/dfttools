import json
from typing import Union
from ..enum import Enum
from . import TestOperation
from . import Instructions

class VoltageForceOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', comment=None):
        """
        Initializes a VoltageForceOperation.

        Args:
            unit (Enum): The unit of voltage force.
            signal (str): The signal to force.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}voltage force: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': 'FORCE',
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class CurrentForceOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', comment=None):
        """
        Initializes a CurrentForceOperation.

        Args:
            unit (Enum): The unit of current force.
            signal (str): The signal to force.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}current force: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': 'FORCE',
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class ResistanceForceOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', comment=None):
        """
        Initializes a ResistanceForceOperation.

        Args:
            unit (Enum): The unit of resistance force.
            signal (str): The signal to force.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}resistance force: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': 'FORCE',
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class ClockForceOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', comment=None):
        """
        Initializes a ClockForceOperation.

        Args:
            unit (Enum): The unit of clock frequency.
            signal (str): The signal to force.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=Instructions.FORCE, signal1=signal,
                         signal2=reference, comment=comment, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}clock force: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': 'FORCE',
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())
