from typing import Union
from .enum import Enum

class TestOperation(Enum):
    WAIT = 0
    MEAS = 1
    FORCE = 2
    REGOP = 3

    def __init__(self, t: int, signal1: str = None, signal2: str = None,
                 comment: str = "", **kwargs):
        self._unit = kwargs['unit'] if 'unit' in kwargs else None
        self._comment = comment
        self._signal1 = signal1
        self._signal2 = signal2
        self._variable = kwargs['variable'] if 'variable' in kwargs else None
        super().__init__(t, [(self.WAIT, 'WAIT'),
                             (self.MEAS, 'MEAS'),
                             (self.FORCE, 'FORCE'),
                             (self.REGOP, 'REGOP')])


class WaitOperation(TestOperation):
    def __init__(self, unit: Enum, delay: Union[int, float], **kwargs):
        self.delay = delay
        super().__init__(t = TestOperation.WAIT, unit = unit,
                         comment = kwargs['comment'] if 'comment' in \
                         kwargs else None)
    def __repr__(self):
        return f'time delay, {self.delay}{self._unit}'

class VoltageMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND',variable:str='' ,comment = None):
        super().__init__(t = TestOperation.MEAS, signal1 = signal,
                         signal2 = reference, comment = comment,
                         variable=variable,unit = unit)

    def __repr__(self):
        if self._signal2 == 'GND':
            what = ''
        else:
            what = 'Differential '
        return f'{what}  voltage measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "savemeas to varaible"+self._variable  if self._variable is not None else "" } { "( " + self._comment + " )" if self._comment is not None else ""}'
    
class CurrentMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND',variable:str='' ,comment = None):
        super().__init__(t = TestOperation.MEAS, signal1 = signal,
                         signal2 = reference, comment = comment,
                         variable=variable,unit = unit)

    def __repr__(self):
        if self._signal2 == 'GND':
            what = ''
        else:
            what = 'Differential '
        return f'{what}  Current measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "savemeas to varaible"+self._variable  if self._variable is not None else "" } { "( " + self._comment + " )" if self._comment is not None else ""}'
    
class ReistanceMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND',variable:str='' ,comment = None):
        super().__init__(t = TestOperation.MEAS, signal1 = signal,
                         signal2 = reference, comment = comment,
                         variable=variable,unit = unit)

    def __repr__(self):
        if self._signal2 == 'GND':
            what = ''
        else:
            what = 'Differential '
        return f'{what}  Resistance measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "savemeas to varaible"+self._variable  if self._variable is not None else "" } { "( " + self._comment + " )" if self._comment is not None else ""}'
    
class FrequencyMeasOperation(TestOperation):
    def __init__(self, unit: Enum, signal: str,
                 reference: str = 'GND',variable:str='' ,comment = None):
        super().__init__(t = TestOperation.MEAS, signal1 = signal,
                         signal2 = reference, comment = comment,
                         variable=variable,unit = unit)

    def __repr__(self):
        if self._signal2 == 'GND':
            what = ''
        else:
            what = 'Differential '
        return f'{what}  Resistance measurement: {self._signal1} wrt {self._signal2}, unit: {self._unit} { "savemeas to varaible"+self._variable  if self._variable is not None else "" } { "( " + self._comment + " )" if self._comment is not None else ""}'
    


        

    
