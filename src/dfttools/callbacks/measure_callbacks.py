from typing import Union
import random
from dfttools import *
from dfttools.glob import db, g


def voltage_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'V',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def current_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'A',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def resistance_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Ohm',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def frequency_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Hz',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


# Register these measure callbacks similarly:

def fft_compute_callback(signal, reference, expected_value: Union[int, float, dict], *args, **kwargs):
    record = {
        'Instruction': 'FFT',
        'Unit': '_',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False
g.hardware_callbacks['voltage_measure'] = voltage_measure_callback
g.hardware_callbacks['current_measure'] = current_measure_callback
g.hardware_callbacks['resistance_measure'] = resistance_measure_callback
g.hardware_callbacks['frequency_measure'] = frequency_measure_callback
g.hardware_callbacks['fft_compute'] = fft_compute_callback