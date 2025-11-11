from typing import Union
import random
from dfttools import *
from dfttools.glob import db, g

def signal_phase_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'phase',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_peak_to_peak_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Vpp',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_rms_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Vrms',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_mean_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Vmean',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_spectrum_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'spectrum',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_min_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Vmin',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_max_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Vmax',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_high_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Vhigh',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_low_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'Vlow',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_amplitude_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
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


def signal_positive_pulse_count_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'count',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_negative_pulse_count_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'count',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_raising_edge_count_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'count',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False


def signal_falling_edge_count_measure_callback(signal: str, reference: str, expected_value: Union[int, float], *args, **kwargs):
    record = {
        'Instruction': 'Measure',
        'Unit': 'count',
        'signal': signal,
        'reference': reference,
        'value': expected_value,
        'comments': f'args={args}, kwargs={kwargs}',
    }
    db.create(record_data=record)
    return False, False

# Register callbacks for easy use
g.hardware_callbacks['signal_phase_measure'] = signal_phase_measure_callback
g.hardware_callbacks['signal_peak_to_peak_measure'] = signal_peak_to_peak_measure_callback
g.hardware_callbacks['signal_rms_measure'] = signal_rms_measure_callback
g.hardware_callbacks['signal_mean_measure'] = signal_mean_measure_callback
g.hardware_callbacks['signal_spectrum_measure'] = signal_spectrum_measure_callback
g.hardware_callbacks['signal_min_measure'] = signal_min_measure_callback
g.hardware_callbacks['signal_max_measure'] = signal_max_measure_callback
g.hardware_callbacks['signal_high_measure'] = signal_high_measure_callback
g.hardware_callbacks['signal_low_measure'] = signal_low_measure_callback
g.hardware_callbacks['signal_amplitude_measure'] = signal_amplitude_measure_callback
g.hardware_callbacks['signal_positive_pulse_count_measure'] = signal_positive_pulse_count_measure_callback
g.hardware_callbacks['signal_negative_pulse_count_measure'] = signal_negative_pulse_count_measure_callback
g.hardware_callbacks['signal_raising_edge_count_measure'] = signal_raising_edge_count_measure_callback
g.hardware_callbacks['signal_falling_edge_count_measure'] = signal_falling_edge_count_measure_callback
