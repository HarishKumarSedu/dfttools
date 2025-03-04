import json
from typing import Union
from ..enum import Enum

class TestOperation(Enum):
    WAIT = 0
    MEAS = 1
    FORCE = 2
    REGOP = 3

    def __init__(self, t: int, signal1: str = None, signal2: str = None,
                 comment: str = "", **kwargs):
        """
        Initializes a TestOperation.

        Args:
            t (int): The type of test operation.
            signal1 (str, optional): The primary signal. Defaults to None.
            signal2 (str, optional): The secondary signal. Defaults to None.
            comment (str, optional): A comment for the operation. Defaults to "".
            **kwargs: Additional keyword arguments, including 'unit' and 'variable'.
        """
        self._unit = kwargs.get('unit', None)
        self._comment = comment
        self._signal1 = signal1
        self._signal2 = signal2
        self._variable = kwargs.get('variable', None)
        super().__init__(t, [(self.WAIT, 'WAIT'),
                             (self.MEAS, 'MEAS'),
                             (self.FORCE, 'FORCE'),
                             (self.REGOP, 'REGOP')])

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': self._t,
            'signal1': self._signal1,
            'signal2': self._signal2,
            'unit': str(self._unit),
            'variable': self._variable,
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class WaitOperation(TestOperation):
    def __init__(self, unit: Enum, delay: Union[int, float], **kwargs):
        """
        Initializes a WaitOperation.

        Args:
            unit (Enum): The unit of time for the delay.
            delay (Union[int, float]): The duration of the delay.
            **kwargs: Additional keyword arguments, including 'comment'.
        """
        self.delay = delay
        super().__init__(t=TestOperation.WAIT, unit=unit,
                         comment=kwargs.get('comment', None))

    def __repr__(self):
        return f'time delay, {self.delay}{self._unit}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        base_dict = super().to_dict()
        base_dict.update({'delay': self.delay})
        return base_dict

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class VoltageMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', variable: str = '', comment=None):
        """
        Initializes a VoltageMeasOperation.

        Args:
            unit (Enum): The unit of voltage measurement.
            signal (str): The signal to measure.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            variable (str, optional): The variable to store the measurement. Defaults to ''.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=TestOperation.MEAS, signal1=signal,
                         signal2=reference, comment=comment,
                         variable=variable, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}voltage measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} {"savemeas to : " + self._variable if self._variable is not None else ""} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': self._t,
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'variable': self._variable,
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class CurrentMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', variable: str = '', comment=None):
        """
        Initializes a CurrentMeasOperation.

        Args:
            unit (Enum): The unit of current measurement.
            signal (str): The signal to measure.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            variable (str, optional): The variable to store the measurement. Defaults to ''.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=TestOperation.MEAS, signal1=signal,
                         signal2=reference, comment=comment,
                         variable=variable, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}Current measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} {"savemeas to : " + self._variable if self._variable is not None else ""} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': self._t,
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'variable': self._variable,
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class ResistanceMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', variable: str = '', comment=None):
        """
        Initializes a ResistanceMeasOperation.

        Args:
            unit (Enum): The unit of resistance measurement.
            signal (str): The signal to measure.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            variable (str, optional): The variable to store the measurement. Defaults to ''.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=TestOperation.MEAS, signal1=signal,
                         signal2=reference, comment=comment,
                         variable=variable, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}Resistance measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} {"savemeas to : " + self._variable if self._variable is not None else ""} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': self._t,
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'variable': self._variable,
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())


class FrequencyMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND', variable: str = '', comment=None):
        """
        Initializes a FrequencyMeasOperation.

        Args:
            unit (Enum): The unit of frequency measurement.
            signal (str): The signal to measure.
            reference (str, optional): The reference signal. Defaults to 'GND'.
            variable (str, optional): The variable to store the measurement. Defaults to ''.
            comment (str, optional): A comment for the operation. Defaults to None.
        """
        super().__init__(t=TestOperation.MEAS, signal1=signal,
                         signal2=reference, comment=comment,
                         variable=variable, unit=unit)

    def __repr__(self):
        what = '' if self._signal2 == 'GND' else 'Differential '
        return f'{what}Frequency measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} {"savemeas to : " + self._variable if self._variable is not None else ""} { "( " + self._comment + " )" if self._comment is not None else ""}'

    def to_dict(self) -> dict:
        """
        Returns the initialized values as a dictionary.

        Returns:
            dict: A dictionary representation of the initialized values.
        """
        return {
            'type': self._t,
            'signal': self._signal1,
            'reference': self._signal2,
            'unit': str(self._unit),
            'variable': self._variable,
            'comment': self._comment
        }

    def to_json(self) -> str:
        """
        Returns the initialized values as a JSON string.

        Returns:
            str: A JSON string representation of the initialized values.
        """
        return json.dumps(self.to_dict())
