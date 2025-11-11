from typing import Union
import random
from dfttools import *
from dfttools.glob import db, g


def rise_time_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 's',  # seconds
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def fall_time_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 's',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def positive_pulse_width_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 's',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def negative_pulse_width_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 's',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def time_delay_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 's',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def positive_duty_cycle_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': '%',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def negative_duty_cycle_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': '%',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def time_period_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 's',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


# Register these callbacks:
g.hardware_callbacks['rise_time_measure'] = rise_time_measure_callback
g.hardware_callbacks['fall_time_measure'] = fall_time_measure_callback
g.hardware_callbacks['positive_pulse_width_measure'] = positive_pulse_width_measure_callback
g.hardware_callbacks['negative_pulse_width_measure'] = negative_pulse_width_measure_callback
g.hardware_callbacks['time_delay_measure'] = time_delay_measure_callback
g.hardware_callbacks['positive_duty_cycle_measure'] = positive_duty_cycle_measure_callback
g.hardware_callbacks['negative_duty_cycle_measure'] = negative_duty_cycle_measure_callback
g.hardware_callbacks['time_period_measure'] = time_period_measure_callback
