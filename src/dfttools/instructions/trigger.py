from typing import Union
import random
from ..glob import g
from ..units.volt import Volt, V
from ..units.current import Current, A
from ..units.resistance import Resistance, Ohm
from ..units.frequency import Frequency, Hz
from ..units.trig import Trig, LH,HL

from ..ops.triggerops import VoltageTriggerOperation, CurrentTriggerOperation, ResistanceTriggerOperation, FrequencyTriggerOperation

def VTRIG(signal: str, reference: str='GND', action:Union[Trig,bool]=LH ,unit:Volt=V, comment: str = ''):
    vtrig =         VoltageTriggerOperation(
            signal=signal,
            reference=reference,
            action=action,
            unit=unit,
            comment=comment
        )
    g.output.append(
        vtrig
    )
    return vtrig.to_dict()

def ATRIG(signal: str, reference: str='GND', action:Union[Trig,bool]=LH ,unit:Current=A, comment: str = ''):
    atrig =         CurrentTriggerOperation(
            signal=signal,
            reference=reference,
            action=action,
            unit=unit,
            comment=comment
        )
    g.output.append(
        atrig
    )
    return atrig.to_dict()

def RESTRIG(signal: str, reference: str='GND', action:Union[Trig,bool]=LH ,unit:Resistance=Ohm, comment: str = ''):
    restrig =         ResistanceTriggerOperation(
            signal=signal,
            reference=reference,
            action=action,
            unit=unit,
            comment=comment
        )
    g.output.append(
        restrig
        )
    return restrig.to_dict()

def FREQTRIG(signal: str, reference: str='GND', action:Union[Trig,bool]=LH ,unit:Frequency=Hz, comment: str = ''):
    freqtrig =         FrequencyTriggerOperation(
            signal=signal,
            reference=reference,
            action=action,
            unit=unit,
            comment=comment
        )
    g.output.append(
        freqtrig
        )
    return freqtrig.to_dict()