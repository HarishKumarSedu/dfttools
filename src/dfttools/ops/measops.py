from typing import Union
from ..enum import Enum
from . import TestOperation
import json
from . import Instructions

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
        super().__init__(t=Instructions.WAIT, unit=unit,
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
        super().__init__(t=Instructions.MEAS, signal1=signal,
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
            'type': 'MEASURE',
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
        super().__init__(t=Instructions.MEAS, signal1=signal,
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
            'type': 'MEASURE',
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
        super().__init__(t=Instructions.MEAS, signal1=signal,
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
            'type': 'MEASURE',
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
        super().__init__(t=Instructions.MEAS, signal1=signal,
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
            'type': 'MEASURE',
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
