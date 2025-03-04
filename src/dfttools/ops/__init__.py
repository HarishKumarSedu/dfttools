import json
from typing import Union
from ..enum import Enum
import collections 
from box import Box

instructions_dict = {'WAIT':0,
                     'MEAS':1,
                     'FORCE':2,
                     'REGOP':3,
                     'FORCESWEEP':4,
                     'READREG_STORE':5,
                     'COPYREG_TO_REG':6,
                     'RESTOREREG_FRO_MVAR':7,
                     'MEAS_MATCH':8
                     }
Instructions = Box(instructions_dict)

class TestOperation(Enum):
    MEAS  = Instructions.MEAS
    WAIT  = Instructions.WAIT
    FORCE = Instructions.FORCE
    REGOP = Instructions.REGOP 
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
        self._t = t
        self._unit = kwargs.get('unit', None)
        self._comment = comment
        self._signal1 = signal1
        self._signal2 = signal2
        self._variable = kwargs.get('variable', None)
        super().__init__(t, zip(Instructions.values(),Instructions.keys()))

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
