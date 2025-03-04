import json
from typing import Union
from ..enum import Enum
from . import TestOperation

# class TestOperation(Enum):
#     WAIT = 0
#     MEAS = 1
#     FORCE = 2
#     REGOP = 3

#     def __init__(self, t: int, signal1: str = None, signal2: str = None,
#                  comment: str = "", **kwargs):
#         """
#         Initializes a TestOperation.

#         Args:
#             t (int): The type of test operation.
#             signal1 (str, optional): The primary signal. Defaults to None.
#             signal2 (str, optional): The secondary signal. Defaults to None.
#             comment (str, optional): A comment for the operation. Defaults to "".
#             **kwargs: Additional keyword arguments, including 'unit'.
#         """
#         self._unit = kwargs.get('unit', None)
#         self._comment = comment
#         self._signal1 = signal1
#         self._signal2 = signal2
#         super().__init__(t, [(self.WAIT, 'WAIT'),
#                              (self.MEAS, 'MEAS'),
#                              (self.FORCE, 'FORCE'),
#                              (self.REGOP, 'REGOP')])

#     def to_dict(self) -> dict:
#         """
#         Returns the initialized values as a dictionary.

#         Returns:
#             dict: A dictionary representation of the initialized values.
#         """
#         return {
#             'type': 'FORCE',
#             'signal1': self._signal1,
#             'signal2': self._signal2,
#             'unit': str(self._unit),
#             'comment': self._comment
#         }

#     def to_json(self) -> str:
#         """
#         Returns the initialized values as a JSON string.

#         Returns:
#             str: A JSON string representation of the initialized values.
#         """
#         return json.dumps(self.to_dict())


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
        super().__init__(t=TestOperation.FORCE, signal1=signal,
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
        super().__init__(t=TestOperation.FORCE, signal1=signal,
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
        super().__init__(t=TestOperation.FORCE, signal1=signal,
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
        super().__init__(t=TestOperation.FORCE, signal1=signal,
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
