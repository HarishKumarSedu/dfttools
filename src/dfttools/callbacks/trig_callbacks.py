from typing import Union
from dfttools import *
from dfttools.glob import db, g

def voltage_trigger_hl_callback(signal: str = 'VCC',  reference: str = 'GND', threshold: Union[int, float] = 0.0,*args, **kwargs):
    record = {
        'Instruction': 'Trigger',
        'Type': 'voltage_trigger_hl',
        'signal': signal,
        'reference': reference,
        'threshold': threshold,
        'value':threshold,
        'comments': f'{args}, {kwargs}',
    }
    db.create(record_data=record)
    return False, False


def voltage_trigger_lh_callback(signal: str = 'VCC', reference: str = 'GND', threshold: Union[int, float] = 0.0, *args, **kwargs):
    record = {
        'Instruction': 'Trigger',
        'Type': 'voltage_trigger_lh',
        'signal': signal,
        'reference': reference,
        'threshold': threshold,
        'value':threshold,
        'comments': f'{args}, {kwargs}',
    }
    db.create(record_data=record)
    return False, False


def voltage_trigger_lg_callback(signal: str = 'VCC', reference: str = 'GND', threshold: Union[int, float] = 0.00, *args, **kwargs):
    record = {
        'Instruction': 'Trigger',
        'Type': 'voltage_trigger_lg',
        'signal': signal,
        'reference': reference,
        'value':threshold,
        'comments': f'{args}, {kwargs}',
    }
    db.create(record_data=record)
    return False, False


def current_trigger_hl_callback(signal: str = 'VCC', reference: str = 'GND', threshold: Union[int, float] = 0.0, *args, **kwargs):
    record = {
        'Instruction': 'Trigger',
        'Type': 'current_trigger_hl',
        'signal': signal,
        'reference': reference,
        'value':threshold,
        'comments': f'{args}, {kwargs}',
    }
    db.create(record_data=record)
    return False, False


def current_trigger_lh_callback(signal: str = 'VCC', reference: str = 'GND', threshold: Union[int, float] = 0.0, *args, **kwargs):
    record = {
        'Instruction': 'Trigger',
        'Type': 'current_trigger_lh',
        'signal': signal,
        'reference': reference,
        'value':threshold,
        'comments': f'{args}, {kwargs}',
    }
    db.create(record_data=record)
    return False, False


def current_trigger_lg_callback(signal: str = 'VCC', reference: str = 'GND', threshold: Union[int, float] = 0.000, *args, **kwargs):
    record = {
        'Instruction': 'Trigger',
        'Type': 'current_trigger_lg',
        'signal': signal,
        'reference': reference,
        'value':threshold,
        'comments': f'{args}, {kwargs}',
    }
    db.create(record_data=record)
    return False, False

g.hardware_callbacks['voltage_trigger_hl'] = voltage_trigger_hl_callback
g.hardware_callbacks['voltage_trigger_lh'] = voltage_trigger_lh_callback
g.hardware_callbacks['voltage_trigger_lg'] = voltage_trigger_lg_callback
g.hardware_callbacks['current_trigger_hl'] = current_trigger_hl_callback
g.hardware_callbacks['current_trigger_lh'] = current_trigger_lh_callback
g.hardware_callbacks['current_trigger_lg'] = current_trigger_lg_callback
