from dfttools import *
def frequency_measure(*args,**kwargs):
  print(args,kwargs)
  return False,False
g.hardware_callbacks['frequency_measure'] = frequency_measure

print("Frequency Measurement:", FREQMEASURE(signal='CLK', reference='GND', expected_value=60))