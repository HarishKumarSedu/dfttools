from dfttools import *
from dfttools import g 

def vtrig(*args,**kwargs):
    print(*args)
    return False,False
LH_Th = 2.25  # 2.25V threshold
error_spread = LH_Th*0.1 # 10% error spread
code_width = 5  # 5 bits trimming code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
force_voltage_low_limit = 2  # minimum voltage limit
force_voltage_high_limit = 3  # maximum voltage limit
g.hardware_callbacks = {
    # 'voltage_measure' : hwl.voltmeter_callback,
    # 'voltage_force' : hwl.voltage_source,
    'voltage_trigger_lh' : vtrig
}
force_voltage = force_voltage_low_limit
VTRIG_LH(signal='IODATA0', reference='GND', threshold=LH_Th, expected_value=force_voltage)