import json
from typing import Union
from ..enum import Enum
from . import Instructions


class TriggerTestOperation(Enum):
    TRIGGER = Instructions.TRIGGER

    def __init__(self, t: int, signal1: str = None, signal2: str = None,
                 comment: str = "", unit: Enum = None, 
                 action: Enum = None, **kwargs):
        self._unit = unit
        self._comment = comment
        self._signal1 = signal1
        self._signal2 = signal2
        self._action = action
        super().__init__(t, zip(Instructions.values(), Instructions.keys()))

    def to_dict(self) -> dict:
        return {
            'type': 'TRIGGER',
            'signal1': self._signal1,
            'signal2': self._signal2,
            'unit': str(self._unit) if self._unit else None,
            'comment': self._comment,
            'action': str(self._action) if isinstance(self._action, Enum) else self._action
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

class VoltageTriggerOperation(TriggerTestOperation):
    def __init__(self, signal: str, reference: str = 'GND', 
                 action: Enum = None,
                 unit: Enum = None, comment: str = ''):
        super().__init__(t=Instructions.TRIGGER,
                         signal1=signal,
                         signal2=reference,
                         comment=comment,
                         unit=unit,
                         action=action)

    def __repr__(self):
        base_str = f"Voltage Trigger on {self._signal1} ({self._unit})"
        if self._signal2 != 'GND':
            base_str += f" differential with {self._signal2}"
        base_str += f" - Action: {self._action}"
        if self._comment:
            base_str += f" ({self._comment})"
        return base_str

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict.update({'type': 'VOLTAGETRIGGER'})
        return base_dict
    
class CurrentTriggerOperation(TriggerTestOperation):
    def __init__(self, signal: str, reference: str = 'GND', 
                 action:Enum = None,
                 unit: Enum = None, comment: str = ''):
        super().__init__(t=Instructions.TRIGGER,
                         signal1=signal,
                         signal2=reference,
                         comment=comment,
                         unit=unit,
                         action=action)

    def __repr__(self):
        base_str = f"Current Trigger on {self._signal1} ({self._unit})"
        if self._signal2 != 'GND':
            base_str += f" differential with {self._signal2}"
        base_str += f" - Action: {self._action}"
        if self._comment:
            base_str += f" ({self._comment})"
        return base_str

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict.update({'type': 'CURRENTTRIGGER'})
        return base_dict
class ResistanceTriggerOperation(TriggerTestOperation):
    def __init__(self, signal: str, reference: str = 'GND', 
                 action: Enum = None,
                 unit: Enum = None, comment: str = ''):
        super().__init__(t=Instructions.TRIGGER,
                         signal1=signal,
                         signal2=reference,
                         comment=comment,
                         unit=unit,
                         action=action)

    def __repr__(self):
        base_str = f"Resistance Trigger on {self._signal1} ({self._unit})"
        if self._signal2 != 'GND':
            base_str += f" differential with {self._signal2}"
        base_str += f" - Action: {self._action}"
        if self._comment:
            base_str += f" ({self._comment})"
        return base_str

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict.update({'type': 'RESISTANCETRIGGER'})
        return base_dict

class FrequencyTriggerOperation(TriggerTestOperation):
    def __init__(self, signal: str, reference: str = 'GND', 
                 action: Enum = None,
                 unit: Enum = None, comment: str = ''):
        super().__init__(t=Instructions.TRIGGER,
                         signal1=signal,
                         signal2=reference,
                         comment=comment,
                         unit=unit,
                         action=action)

    def __repr__(self):
        base_str = f"Frequency Trigger on {self._signal1} ({self._unit})"
        if self._signal2 != 'GND':
            base_str += f" differential with {self._signal2}"
        base_str += f" - Action: {self._action}"
        if self._comment:
            base_str += f" ({self._comment})"
        return base_str

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict.update({'type': 'FREQUENCYTRIGGER'})
        return base_dict


