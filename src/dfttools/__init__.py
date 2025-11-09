from dfttools.instructions.force import *
from dfttools.instructions.meas import *
from dfttools.instructions.force_sweep import *
from dfttools.instructions.I2C import *
from dfttools.instructions.trigger import *
from dfttools.instructions.time import *
from dfttools.instructions.signal import *
from dfttools.glob import g
from dfttools.callbacks.force_callbacks import *
from dfttools.callbacks.measure_callbacks import *
from dfttools.callbacks.force_sweep_callbacks import *
from dfttools.callbacks.i2c_callback import *
from dfttools.callbacks.trig_callbacks import *
from dfttools.callbacks.trig_custom_callbacks import *

import importlib
import inspect

__all__ = [name for name in dir() if not name.startswith("_")]

# module = importlib.import_module("dfttools")  # Pass the module name as a string
        
# Unified list for all suggestions
# suggestions = set()

# # Get functions with their definitions (signatures and docstrings)
# for name, obj in inspect.getmembers(module, inspect.isfunction):
#     func_signature = inspect.signature(obj)
#     suggestions.add(f"{name}{func_signature}")

# Get keywords (includes attributes, classes, etc.)
# for keyword in dir(module):
#     suggestions.add(f"{keyword}")
# print(suggestions)