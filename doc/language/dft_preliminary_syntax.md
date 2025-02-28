# DFT Syntax and Examples

This document outlines the syntax and examples for defining Digital Functional Test (DFT) procedures.

## 1. Register Parse

**Grammar:** `WRITE_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, Value=<value> ; [Comment]`

This section describes commands for writing to specific registers.

| Input                      | `registers`                                                                  | `value` |
|----------------------------|------------------------------------------------------------------------------|---------|
| `0xFE__0x00`               | `[{ "address": "0xFE", "msb": 7, "lsb": 0 }]`                               | `0`     |
| `0x20[1]__0x01`              | `[{ "address": "0x20", "msb": 7, "lsb": 0 }]`                               | `1`     |
| `0xFE[2:1]__0x01`             | `[{ "address": "0xFE", "msb": 2, "lsb": 1 }]`                               | `1`     |
| `0xFE__0x01 "Select page 1"` | `[{ "address": "0xFE", "msb": 7, "lsb": 0 }]`                               | `1`     |
| `0xFE[1:1]__0x1 "hi" `      | `[{ "address": "0xFE", "msb": 1, "lsb": 1 }]`                               | `1`     |
| `0x01[5:3]__0x03[4:0]__0xA4`  | `[{ "address": "0x01", "msb": 5, "lsb": 3 }, { "address": "0x03", "msb": 4, "lsb": 0 }]` | `164`   |
| `0x01[5:3]__0x03[4:0]__0x6__0x8[1:2]__0xA4 "Hi" ` | `[{ "address": "0x01", "msb": 5, "lsb": 3 }, { "address": "0x03", "msb": 4, "lsb": 0 }, { "address": "0x6", "msb": 7, "lsb": 0 }, { "address": "0x8", "msb": 1, "lsb": 2 }]` | `164`   |

## 2. Wait Delay Parse

**Grammar:** `WAIT Value=<value>, Unit=<unit>`

This section describes commands for introducing a delay.

| Input             | `value` | `unit`        | `absValue`           |
|-------------------|---------|---------------|----------------------|
| `Wait__delay__0.5ms` | `0.5` | `milliseconds` | `0.0005` |
| `Wait__delay__250us` | `250.0` | `microseconds` | `0.00025` |
| `Wait__delay__100ns` | `100.0` | `nanoseconds` | `1.0000000000000001e-07` |
| `Wait__delay__100nS` | `100.0` | `nanoseconds` | `1.0000000000000001e-07` |

## 3. force_parse

**Grammar:** `FORCE <primary_signal>, [<secondary_signal>], Value=<value>, Unit=<unit>, [Multiplier=<multiplier>], [Comment]`

This section describes commands for forcing specific voltage or current values on pins.

| Input                      | `primary_signal` | `secondary_signal` | `value` | `multiplier` | `absValue` | `unit` | `comment`            |
|----------------------------|------------------|--------------------|---------|--------------|------------|--------|--------------------|
| `Force__SDWN__1.1V`         | `"SDWN"`           | `null`             | `"1.1"` | `""`         | `1.1`      | `"V"`  | `""`               |
| `Force__SDWN__0.1mA`        | `"SDWN"`           | `null`             | `"0.1"` | `"m"`        | `0.0001`   | `"A"`  | `""`               |
| `Force__V5VDRV__5.2V`       | `"V5VDRV"`         | `null`             | `"5.2"` | `""`         | `5.2`      | `"V"`  | `""`               |
| `Force__SDWN__0.1uA`        | `"SDWN"`           | `null`             | `"0.1"` | `"u"`        | `1e-07`     | `"A"`  | `""`               |
| `Force__VBSO__19V`          | `"VBSO"`           | `null`             | `"19"`  | `""`         | `19.0`     | `"V"`  | `""`               |
| `Force__SDWN__-1.1mA`       | `"SDWN"`           | `null`             | `"-1.1"`| `"m"`        | `-0.0011`  | `"A"`  | `""`               |
| `Force__SDWN__OPEN "Open the Pin Switch"` | `"SDWN"`           | `null`             | `"OPEN"`| `""`         | `"OPEN"` | `""`  | `"Open the Pin Switch"`|
| `Force__V5_VDRV__CLOSE`     | `"V5_VDRV"`        | `null`             | `"CLOSE"` | `""`         | `"CLOSE"` | `""`  | `""`               |
| `Force__OUTP1+__OUTP1-__-5V` | `"OUTP1+"`         | `"OUTP1-"`           | `"-5"`  | `""`         | `-5.0`     | `"V"`  | `""`               |
| `Force__SDWN__CD_DIAG__1.1V` | `"SDWN"`           | `"CD_DIAG"`          | `"1.1"` | `""`         | `1.1`      | `"V"`  | `""`               |
| `Force__Sdwn__VCC1+__0.1mA`  | `"Sdwn"`           | `"VCC1+"`            | `"0.1"` | `"m"`        | `0.0001`   | `"A"`  | `""`               |

## 4. savemeas_parse

**Grammar:** `MEASURE <unit>, <primary_signal>, [<secondary_signal>], [Save_Variable=<variable_name>]`

This section describes commands for measuring and saving measured values.

| Input                       | `unit`    | `primary_signal` | `secondary_signal` | `save_variable` |
|-----------------------------|-----------|------------------|--------------------|-----------------|
| `SaveMeas__Voltage__OutP__OutN__var2` | `"Voltage"` | `"OutP"`           | `"OutN"`           | `"var2"`        |
| `SaveMeas__Voltage__VBOOST1+__V1`     | `"Voltage"` | `"VBOOST1+"`       | `"V1"`           | `null`          |
| `SaveMeas__Voltage__SDWN1__var1`      | `"Voltage"` | `"SDWN1"`          | `"var1"`           | `null`          |
| `SaveMeas__Voltage__CD_DIAG1__GND`    | `"Voltage"` | `"CD_DIAG1"`       | `"GND"`            | `null`          |
| `SaveMeas__Current__ENABLE__GND`      | `"Current"` | `"ENABLE"`         | `"GND"`            | `null`          |

## 5. read_parse

**Grammar:** `READ_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, [Save_Variable=<variable_name>]`

This section describes commands for reading register values.

| Input                      | `registers`                                                  | `save_variable` |
|----------------------------|-------------------------------------------------------------|-----------------|
| `Read__0x1__Var0x1`         | `[{ "address": "0x1", "msb": 7, "lsb": 0 }]`              | `"Var0x1"`      |
| `Read__0x1[1:2]__Var0x1`    | `[{ "address": "0x1", "msb": 1, "lsb": 2 }]`              | `"Var0x1"`      |
| `Read__0x1[7:5]__0x2[4:2]__0x03__Var` | `[{ "address": "0x1", "msb": 7, "lsb": 5 }, { "address": "0x2", "msb": 4, "lsb": 2 }, { "address": "0x03", "msb": 7, "lsb": 0 }]` | `"Var"`         |
| `Read__0x1[7:5]__0x2[4:2]__0x03__0x05__0x06[1:2]__Var` | `[{ "address": "0x1", "msb": 7, "lsb": 5 }, { "address": "0x2", "msb": 4, "lsb": 2 }, { "address": "0x03", "msb": 7, "lsb": 0 }, { "address": "0x05", "msb": 7, "lsb": 0 }, { "address": "0x06", "msb": 1, "lsb": 2 }]` | `"Var"`         |

## 6. copy_parse

**Grammar:** `COPY_REGISTER Copy_Register=<address>, MSB=<msb>, LSB=<lsb>, Paste_Register=<address>, MSB=<msb>, LSB=<lsb>`

This section describes commands for copying data between registers.

| Input                 | `copy_register`                     | `paste_register`                     |
|-----------------------|-------------------------------------|--------------------------------------|
| `Copy__0x01__0x02`    | `{ "address": "0x01", "msb": 7, "lsb": 0 }` | `{ "address": "0x02", "msb": 7, "lsb": 0 }` |
| `Copy__0x1[2:1]__0x02[3:2]` | `{ "address": "0x1", "msb": 2, "lsb": 1 }`  | `{ "address": "0x02", "msb": 3, "lsb": 2 }` |
| `Copy__0x1[2:1]__0x02[3:2]` | `{ "address": "0x1", "msb": 2, "lsb": 1 }`  | `{ "address": "0x02", "msb": 3, "lsb": 2 }` |

## 7. save_parse

**Grammar:** `SAVE_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, Save_Variable=<variable_name>`

This section describes commands for saving register values to a variable.

| Input                      | `registers`                                                  | `save_variable` |
|----------------------------|-------------------------------------------------------------|-----------------|
| `Save__0x01__var0x1`       | `[{ "address": "0x01", "msb": 7, "lsb": 0 }]`              | `"var0x1"`      |
| `Save__0x1[2:1]__var0x2`  | `[{ "address": "0x1", "msb": 2, "lsb": 1 }]`              | `"var0x2"`      |
| `Save__0x1[1:2]__0x2[3:4]__0x4__0x5__Varmulti` | `[{ "address": "0x1", "msb": 2, "lsb": 1 }, { "address": "0x2", "msb": 4, "lsb": 3 }, { "address": "0x4", "msb": 7, "lsb": 0 }, { "address": "0x5", "msb": 7, "lsb": 0 }]` | `"Varmulti"`      |

## 8. restore_parse

**Grammar:** `RESTORE_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, Restore_Variable=<variable_name>`

This section describes commands for restoring register values from a variable.

| Input                      | `registers`                                                  | `restore_variable` |
|----------------------------|-------------------------------------------------------------|--------------------|
| `Restore__0x01__var0x1`    | `[{ "address": "0x01", "msb": 7, "lsb": 0 }]`              | `"var0x1"`         |
| `Restore__0x1[2:1]__var0x2` | `[{ "address": "0x1", "msb": 2, "lsb": 1 }]`              | `"var0x2"`         |
| `Restore__0x1[1:2]__0x2[3:4]__0x4__0x5__Varmulti` | `[{ "address": "0x1", "msb": 2, "lsb": 1 }, { "address": "0x2", "msb": 4, "lsb": 3 }, { "address": "0x4", "msb": 7, "lsb": 0 }, { "address": "0x5", "msb": 7, "lsb": 0 }]` | `"Varmulti"`         |

## 9. force_sweep_parse

**Grammar:** `SWEEP <primary_signal>, [<secondary_signal>], Initial_Value=<value>, Unit=<unit>, Final_Value=<value>, Unit=<unit>, [Step_Size=<value>, Multiplier=<multiplier>, Unit=<unit>], [Sweep_Time=<value>, Multiplier=<multiplier>, Unit=<unit>] ; [Comment]`

This section describes commands for sweeping voltage or current on a pin.

| Input                                     | `primary_signal` | `secondary_signal` | `initial_value`                                                     | `final_value`                                                     | `step_size`                                                         | `sweep_time`                                                         |
|-------------------------------------------|------------------|--------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| `Force__Sweep__VBAT`                      | `null`           | `null`             | `null`                                                              | `null`                                                              | `null`                                                              | `null`                                                              |
| `Force__Sweep__VBOOST__VCC2+__3V__5V__0.01mV__1mS` | `"VBOOST"`         | `"VCC2+"`          | `{ "raw_value": 3.0, "multiplier": 1, "unit": "V", "final_value": 3.0, "multiplier_prefix": "" }` | `{ "raw_value": 5.0, "multiplier": 1, "unit": "V", "final_value": 5.0, "multiplier_prefix": "" }` | `{ "raw_value": 0.01, "multiplier": 0.001, "unit": "V", "final_value": 1.0E-5, "multiplier_prefix": "m" }` | `{ "raw_value": 1.0, "multiplier": 0.001, "unit": "S", "final_value": 0.001, "multiplier_prefix": "m" }` |
| `Force__Sweep__VBAT__2V__1V`               | `"VBAT"`           | `"GND"`            | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `null`                                                              | `null`                                                              |
| `Force__Sweep__VBAT__SDWN__2V__1V`        | `"VBAT"`           | `"SDWN"`           | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `null`                                                              | `null`                                                              |
| `Force__Sweep__VBAT__GND__2V__1V__1mV`     | `"VBAT"`           | `"GND"`            | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 0.001, "unit": "V", "final_value": 0.001, "multiplier_prefix": "m" }` | `null`                                                              |
| `Force__Sweep__VBAT__GND__2V__1V__1mV__100uS` | `"VBAT"`           | `"GND"`            | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 0.001, "unit": "V", "final_value": 0.001, "multiplier_prefix": "m" }` | `{ "raw_value": 100.0, "multiplier": 1.0E-6, "unit": "S", "final_value": 9.999999999999999E-5, "multiplier_prefix": "u" }` |

## 10. trigger_parse

**Grammar:** `TRIGGER <action>`

This section describes commands for setting trigger conditions.

| Input        | `action` | `value` | `description`            | `opposite_action` | `opposite_value` |
|--------------|----------|---------|--------------------------|-------------------|------------------|
| `Trigger__LH` | `"LH"`   | `1`     | `"Output change from L to H"` | `"HL"`            | `0`                |
| `Trigger__HL` | `"HL"`   | `0`     | `"Output change from H to L"` | `"LH"`            | `1`                |

## 11. trim_parse

**Grammar:** `TRIM <register_address>`

This section describes commands for trimming specific registers.

| Input                      | `registers`                                  |
|----------------------------|---------------------------------------------|
| `Trim__0x1`                | `[{ "address": "0x1", "msb": 7, "lsb": 0 }]`|
| `Trim__0x1[2:1]`           | `[{ "address": "0x1", "msb": 2, "lsb": 1 }]`|
| `Trim__0x1[1:1]__0x2[4:2]` | `[{ "address": "0x1", "msb": 1, "lsb": 1 }, { "address": "0x2", "msb": 4, "lsb": 2 }]`|
| `Trim__0x1[1:2]__0x2[5:4]__0x3` | `[{ "address": "0x1", "msb": 2, "lsb": 1 }, { "address": "0x2", "msb": 5, "lsb": 4 }, { "address": "0x3", "msb": 7, "lsb": 0 }]`|
| `Trim__0xBA[2:0]__0xBB[2:1]  "Trimming for OCP_LS_CH1 to have toggling on SDO"` | `[{ "address": "0xBA", "msb": 2, "lsb": 0 }, { "address": "0xBB", "msb": 2, "lsb": 1 }]`|
| `Trim__0xBB[0]__0xBC[2:0]__0xBD[2] "Trimming for OCP_LS_CH2 to have toggling on CD_DIAG"` | `[{ "address": "0xBB", "msb": "0", "lsb": "0" }, { "address": "0xBC", "msb": 2, "lsb": 0 }, { "address": "0xBD", "msb": "2", "lsb": "2" }]`|

## 12. run_parse

**Grammar:** `RUN <procedure_name>`

This section describes commands for running specific procedures.

| Input              | `output`       |
|--------------------|----------------|
| `Run__startup`     | `"startup"`    |
| `Run__startup_5.5v` | `"startup_5.5v"`|
| `Start__procedure` | `null`         |
| `Run__`            | `null`         |

## 13. meas_match_parse

**Grammar:** `MEASURE_MATCH <unit>, <primary_signal>, <secondary_signal>, <value>`

This section describes commands for measuring and matching values.

| Input                                                                                                | `unit`       | `primary_signal` | `secondary_signal` | `value`   |
|------------------------------------------------------------------------------------------------------|--------------|------------------|--------------------|-----------|
| `Meas__Match__Current__SDWN__VCC__100mA "Measure the Current from SDWN with Respect to the Ground match with Expected Value is 100mA"` | `"Current"`  | `"SDWN"`           | `"VCC"`            | `0.1`       |
| `Meas__Match__Voltage__Vbat__4.0V`                                                                 | `"Voltage"`  | `"Vbat"`           | `"GND"`            | `4.0`       |
| `Meas__Match__Frequency__CLK__10kHz`                                                              | `"Frequency"`| `"CLK"`            | `"GND"`            | `10000.0`   |
| `Meas__Match__Resistance__Rload__1kOhm`                                                            | `"Resistance"`| `"Rload"`          | `"GND"`            | `1000.0`    |
| `Meas__Match__resistance__Rload__1kOhm`                                                            | `"resistance"`| `"Rload"`          | `"GND"`            | `1000.0`    |
| `Meas__Match__voltage__Vload__1kV`                                                                  | `"Voltage"`  | `"Vload"`          | `"GND"`            | `1000.0`    |
| `Meas__Match__Current__Enable__627nA`                                                               | `"Current"`  | `"Enable"`         | `"GND"`            | `6.27e-07`|
| `Meas__Match__Voltage__Enable__0.5mV`                                                               | `"Voltage"`  | `"Enable"`         | `"GND"`            | `0.0005`    |
| `Meas__Match__Voltage__Enable__0.5mA`                                                               | `null`  | `null`         | `null`            | `null`    |
| `Meas__Match__Current__Enable__5Ohm`                                                                | `null`  | `null`         | `null`            | `null`    |
| `Meas__Match__Frequency__Enable__5V`                                                                 | `null`  | `null`         | `null`            | `null`    |
| `Meas__Match__Resistance__Enable__5Hz`                                                              | `null`  | `null`         | `null`            | `null`    |

## 14. sweep_trig_parse

**Grammar:** `SWEEP_TRIGGER_STORE SWEEP_SIGNAL <sweep_signal>, SWEEPER_REFERENCE <sweeper_reference>, <initial_value>, <final_value>, [Step_Size <step_size>], [Sweep_Time <sweep_time>], TRIGGER_SIGNAL <trig_signal>, TRIGGER_REFERENCE <trig_reference>, TRIGGER_STATE <trig_state>  ; [Variable]`

This section describes commands combining sweeping with triggering for complex measurements.

| Input                                                                                                | `sweep_signal` | `sweeper_reference` | `initial_value` | `final_value` | `step_size` | `sweep_time` | `unit` | `trig_signal` | `trig_reference` | `trig_state` | `variable`         |
|------------------------------------------------------------------------------------------------------|----------------|---------------------|-----------------|-----------------|-------------|--------------|--------|---------------|------------------|--------------|------------------|
| `Sweep__Trig__Store___Sweep__Signal__Signal_1+__Sweeper__Reference__Reference1-__10V__20V__1V__1mS___Trig__Signal__Signal_A-__Trig__Reference__Reference_A+__TrigState__HL___VariableData` | `"Signal_1+"` | `"Reference1-"` | `10.0`         | `20.0`         | `1.0`       | `0.001`   | `"V"`  | `"Signal_A-"` | `"Reference_A+"` | `"HL"`      | `"VariableData"` |
| `Sweep__Trig__Store___Sweep__Signal__Signal2__Sweeper__Reference__Reference2__5mA__15mA__0.1mA___Trig__Signal__SignalB__Trig__Reference__ReferenceB__TrigState__LH___AnotherVariable`    | `"Signal2"`   | `"Reference2"`   | `0.005`         | `0.015`         | `0.0001`   | `null`   | `"A"`  | `"SignalB"`   | `"ReferenceB"`   | `"LH"`      | `"AnotherVariable"`|
| `Sweep__Trig__Store___Sweep__Signal__Signal2__Sweeper__Reference__Reference2__5mA__15mA___Trig__Signal__SignalB__Trig__Reference__ReferenceB__TrigState__LH___AnotherVariable`         | `null`   | `null`   | `null`         | `null`         | `null`   | `null`   | `null`  | `null`   | `null`   | `null`      | `null`|
| `Sweep__Trig__Store___Sweep__Signal__Sig_nal3+__Sweeper__Reference__Reference3__0A__0A__0A___Trig__Signal__SignalC__Trig__Reference__ReferenceC__TrigState__HL___`                   | `"Sig_nal3+"` | `"Reference3"`   | `null`         | `null`         | `null`   | `null`   | `"A"`  | `"SignalC"`   | `"ReferenceC"`   | `"HL"`      | `""`|
| `Sweep__Trig__Store___Sweep__Signal__Signal4__Sweeper__Reference__Reference4__-2.5V__-1.5V__-0.5V__10uS___Trig__Signal__SignalD__Trig__Reference__ReferenceD__TrigState__LH___NegativeValues` | `"Signal4"`   | `"Reference4"`   | `-2.5`         | `-1.5`         | `-0.5`   | `9.99...e-06`| `"V"`  | `"SignalD"`   | `"ReferenceD"`   | `"LH"`      | `"NegativeValues"`|

## 15. calculate_parse

**Grammar:** `CALCULATE <variable_name> [ , <variable_name>=<expression>] ; [Comment]`

This section describes commands performing calculations.

| Input                             |       |
|-----------------------------------|-------|
| `Calculate__GAINLOCAL_1__GAIN_1=V1/10` |       |
| `Calculate__GAINLOCAL`             |       |
| `Calculate__MinError "this is"`     |       |

