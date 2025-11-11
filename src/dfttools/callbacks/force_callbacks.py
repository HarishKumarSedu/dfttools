from typing import Union
import random
from dfttools import *
from dfttools.glob import db, g


def voltage_force_callback(signal: str, reference: str, value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Force',
        'Unit': 'V',
        'signal': signal,
        'reference': reference,
        'value': value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def current_force_callback(signal: str, reference: str, value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Force',
        'Unit': 'A',
        'signal': signal,
        'reference': reference,
        'value': value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def resistance_force_callback(signal: str, reference: str, value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Force',
        'Unit': 'Ohm',
        'signal': signal,
        'reference': reference,
        'value': value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def frequency_force_callback(signal: str, reference: str, value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Force',
        'Unit': 'Hz',
        'signal': signal,
        'reference': reference,
        'value': value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


# Register them all in the hardware_callbacks dictionary
g.hardware_callbacks['voltage_force'] = voltage_force_callback
g.hardware_callbacks['current_force'] = current_force_callback
g.hardware_callbacks['resistance_force'] = resistance_force_callback
g.hardware_callbacks['frequency_force'] = frequency_force_callback


def fft_compute_callback(signal, reference, signal_type, sample_number, sample_time, window, parameters):
    # Simulate hardware availability randomly
    hardware_available = random.choice([True, False])
    if hardware_available:
        # Return mock measured values for each requested parameter
        measured_values = {param: random.uniform(0.9, 1.1) * 100 for param in parameters}
        return True, measured_values
    else:
        return False, {}