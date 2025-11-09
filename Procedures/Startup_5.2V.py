Test_Name = 'Startup_5.2V'
print(f'............ {Test_Name} ........')
from dfttools import *

VFORCE(signal="CD_DIAG", reference="GND", value=1.8)
VFORCE(signal="VCC1_Plus", reference="GND", value=5.2)  
VFORCE(signal="VCC1_Minus", reference="GND", value=5.2)  
VFORCE(signal="VCC2_Plus", reference="GND", value=5.2)  
VFORCE(signal="VCC2_Minus", reference="GND", value=5.2)  
VFORCE(signal="VCC3_Plus", reference="GND", value=5.2) 
VFORCE(signal="VCC3_Minus", reference="GND", value=5.2)  
VFORCE(signal="VCC4_Plus", reference="GND", value=5.2)  
VFORCE(signal="VCC4_Minus", reference="GND", value=5.2)  
VFORCE(signal="VCC", reference="GND", value=5.2) 