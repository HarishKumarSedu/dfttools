Itest = 0.1
vmeas = VMEAS('SDWN')
WRITE_BITFIELDS((ptn_en,1))
VFORCE('SDWN','GND')
resistance = vmeas / Itest 
