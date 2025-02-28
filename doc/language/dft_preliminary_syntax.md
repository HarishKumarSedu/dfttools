# DFT Syntax and Examples

This document outlines the syntax used for defining Digital Functional Test (DFT) procedures. It provides examples for various DFT commands based on a structured format.

## 1. Register Parse

Describes commands for writing to registers.

**Syntax:** `WRITE_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, Value=<value> ; [Comment]`

| Input        | Output (DFT Syntax) | `registers`                                                                       | `value` |
|--------------|---------------------|-----------------------------------------------------------------------------------|---------|
| `0xFE__0x00` |                     | `[{ "address": "0xFE", "msb": 7, "lsb": 0 }]`                                   | `0`     |
| `0x20[1]__0x01` |                     | `[{ "address": "0x20", "msb": 7, "lsb": 0 }]`                                   | `1`     |
| `0xFE[2:1]__0x01` |                     | `[{ "address": "0xFE", "msb": 2, "lsb": 1 }]`                                   | `1`     |
| `0xFE__0x01 "Select page 1"` |                     | `[{ "address": "0xFE", "msb": 7, "lsb": 0 }]`                                   | `1`     |
| `0xFE[1:1]__0x1 "hi" ` |                     | `[{ "address": "0xFE", "msb": 1, "lsb": 1 }]`                                   | `1`     |
| `0x01[5:3]__0x03[4:0]__0xA4` |                     | `[{ "address": "0x01", "msb": 5, "lsb": 3 }, { "address": "0x03", "msb": 4, "lsb": 0 }]` | `164`   |
| `0x01[5:3]__0x03[4:0]__0x6__0x8[1:2]__0xA4 "Hi" ` |                     | `[{ "address": "0x01", "msb": 5, "lsb": 3 }, { "address": "0x03", "msb": 4, "lsb": 0 }, { "address": "0x6", "msb": 7, "lsb": 0 }, { "address": "0x8", "msb": 1, "lsb": 2 }]` | `164`   |

## 2. Wait Delay Parse

Describes commands for introducing delays.

**Syntax:** `WAIT Value=<value>, Unit=<unit>`

| Input             | Output (DFT Syntax) | `value` | `unit`        | `absValue`           |
|-------------------|---------------------|---------|---------------|----------------------|
| `Wait__delay__0.5ms` |                     | `100.0` | `nanoseconds` | `1.0000000000000001e-7` |
| `Wait__delay__250us` |                     | `100.0` | `nanoseconds` | `1.0000000000000001e-7` |
| `Wait__delay__100ns` |                     | `100.0` | `nanoseconds` | `1.0000000000000001e-7` |
| `Wait__delay__100nS` |                     | `100.0` | `nanoseconds` | `1.0000000000000001e-7` |

## 3. Const Parse

Describes commands for defining constant values.

**Syntax:** `DEFINE <constant_name>, Value=<value>, Unit=<unit>, Multiplier=<multiplier> ; [Comment]`

| Input                             | Output (DFT Syntax) | `constant_name` | `value`   | `unit`       | `multiplier` |
|-----------------------------------|---------------------|-----------------|-----------|--------------|--------------|
| `Const__Itest= 100mA "itest current" ` |                     | `Itest`         | `0.1`       | `current`    | `0.001`      |
| `Const__Vbias= 3.3V`                |                     | `Vbias`         | `3.3`       | `voltage`    | `1.0`        |
| `Const__Rload= 1kOhm`               |                     | `Rload`         | `1000.0`    | `resistance` | `1000.0`     |
| `Const__freq= 10MHz`                |                     | `freq`          | `10000000.0` | `frequency`  | `1000000.0`    |
| `Const__Ileak= 10uA`                |                     | `Ileak`         | `9.999999...` | `current`    | `1e-6`       |
| `Const__Cap= 10pF`                  |                     | `Cap`           | `null`      |              |              |
| `Const__Res= 10Ohm`                 |                     | `Res`           | `10.0`      | `unknown`    | `1.0`        |
| `Const__Current = 5.5 mA`           |                     | `Current`       | `null`      |              |              |
| `Const__Voltage = 10.89V`           |                     | `Voltage`       | `null`      |              |              |

## 4. Force Parse

Describes commands for forcing specific voltage or current values on pins.

**Syntax:** `FORCE <primary_signal>, [<secondary_signal>], Value=<value>, Unit=<unit>, [Multiplier=<multiplier>], [Comment]`

| Input                      | Output (DFT Syntax) | `primary_signal` | `secondary_signal` | `value` | `multiplier` | `absValue` | `unit` | `comment`            |
|----------------------------|---------------------|------------------|--------------------|---------|--------------|------------|--------|--------------------|
| `Force__SDWN__1.1V`         |                     | `SDWN`           | `null`             | `"1.1"` | `""`         | `1.1`      | `"V"`  | `""`               |
| `Force__SDWN__0.1mA`        |                     | `SDWN`           | `null`             | `"0.1"` | `"m"`        | `0.0001`   | `"A"`  | `""`               |
| `Force__V5VDRV__5.2V`       |                     | `V5VDRV`         | `null`             | `"5.2"` | `""`         | `5.2`      | `"V"`  | `""`               |
| `Force__SDWN__0.1uA`        |                     | `SDWN`           | `null`             | `"0.1"` | `"u"`        | `1e-7`     | `"A"`  | `""`               |
| `Force__VBSO__19V`          |                     | `VBSO`           | `null`             | `"19"`  | `""`         | `19.0`     | `"V"`  | `""`               |
| `Force__SDWN__-1.1mA`       |                     | `SDWN`           | `null`             | `"-1.1"`| `"m"`        | `-0.0011`  | `"A"`  | `""`               |
| `Force__SDWN__OPEN "Open the Pin Switch"` |                     | `SDWN`           | `null`             | `"OPEN"`| `""`         | `"OPEN"` | `""`  | `"Open the Pin Switch"`|
| `Force__V5_VDRV__CLOSE`     |                     | `V5_VDRV`        | `null`             | `"CLOSE"` | `""`         | `"CLOSE"` | `""`  | `""`               |
| `Force__OUTP1+__OUTP1-__-5V` |                     | `OUTP1+`         | `OUTP1-`           | `"-5"`  | `""`         | `-5.0`     | `"V"`  | `""`               |
| `Force__SDWN__CD_DIAG__1.1V` |                     | `SDWN`           | `CD_DIAG`          | `"1.1"` | `""`         | `1.1`      | `"V"`  | `""`               |
| `Force__Sdwn__VCC1+__0.1mA`  |                     | `Sdwn`           | `VCC1+`            | `"0.1"` | `"m"`        | `0.0001`   | `"A"`  | `""`               |

## 5. SaveMeas Parse

Describes commands for measuring and saving measured values.

**Syntax:** `MEASURE <unit>, <primary_signal>, [<secondary_signal>], [Save_Variable=<variable_name>]`

| Input                       | Output (DFT Syntax) | `unit`    | `primary_signal` | `secondary_signal` | `save_variable` |
|-----------------------------|---------------------|-----------|------------------|--------------------|-----------------|
| `SaveMeas__Voltage__OutP__OutN__var2` |                     | `"Voltage"` | `"OutP"`           | `"OutN"`           | `"var2"`        |
| `SaveMeas__Voltage__VBOOST1+__V1`     |                     | `"Voltage"` | `"VBOOST1+"`       | `"V1"`           | `null`          |
| `SaveMeas__Voltage__SDWN1__var1`      |                     | `"Voltage"` | `"SDWN1"`          | `"var1"`           | `null`          |
| `SaveMeas__Voltage__CD_DIAG1__GND`    |                     | `"Voltage"` | `"CD_DIAG1"`       | `"GND"`            | `null`          |
| `SaveMeas__Current__ENABLE__GND`      |                     | `"Current"` | `"ENABLE"`         | `"GND"`            | `null`          |

## 6. Read Parse

Describes commands for reading register values.

**Syntax:** `READ_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, [Save_Variable=<variable_name>]`

| Input                      | Output (DFT Syntax) | `registers`                                                  | `save_variable` |
|----------------------------|---------------------|-------------------------------------------------------------|-----------------|
| `Read__0x1__Var0x1`         |                     | `[{ "address": "0x1", "msb": 7, "lsb": 0 }]`              | `"Var0x1"`      |
| `Read__0x1[1:2]__Var0x1`    |                     | `[{ "address": "0x1", "msb": 1, "lsb": 2 }]`              | `"Var0x1"`      |
| `Read__0x1[7:5]__0x2[4:2]__0x03__Var` |                     | `[{ "address": "0x1", "msb": 7, "lsb": 5 }, { "address": "0x2", "msb": 4, "lsb": 2 }, { "address": "0x03", "msb": 7, "lsb": 0 }]` | `"Var"`         |
| `Read__0x1[7:5]__0x2[4:2]__0x03__0x05__0x06[1:2]__Var` |                     | `[{ "address": "0x1", "msb": 7, "lsb": 5 }, { "address": "0x2", "msb": 4, "lsb": 2 }, { "address": "0x03", "msb": 7, "lsb": 0 }, { "address": "0x05", "msb": 7, "lsb": 0 }, { "address": "0x06", "msb": 1, "lsb": 2 }]` | `"Var"`         |

## 7. Copy Parse

Describes commands for copying data between registers.

**Syntax:** `COPY_REGISTER Copy_Register=<address>, MSB=<msb>, LSB=<lsb>, Paste_Register=<address>, MSB=<msb>, LSB=<lsb>`

| Input                 | Output (DFT Syntax) | `copy_register`                     | `paste_register`                     |
|-----------------------|---------------------|-------------------------------------|--------------------------------------|
| `Copy__0x01__0x02`    |                     | `{ "address": "0x01", "msb": 7, "lsb": 0 }` | `{ "address": "0x02", "msb": 7, "lsb": 0 }` |
| `Copy__0x1[2:1]__0x02[3:2]` |                     | `{ "address": "0x1", "msb": 2, "lsb": 1 }`  | `{ "address": "0x02", "msb": 3, "lsb": 2 }` |
| `Copy__0x1[2:1]__0x02[3:2]` |                     | `{ "address": "0x1", "msb": 2, "lsb": 1 }`  | `{ "address": "0x02", "msb": 3, "lsb": 2 }` |

## 8. Save Parse

Describes commands for saving register values to a variable.

**Syntax:** `SAVE_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, Save_Variable=<variable_name>`

| Input                      | Output (DFT Syntax) | `registers`                                                  | `save_variable` |
|----------------------------|---------------------|-------------------------------------------------------------|-----------------|
| `Save__0x01__var0x1`       |                     | `[{ "address": "0x01", "msb": 7, "lsb": 0 }]`              | `"var0x1"`      |
| `Save__0x1[2:1]__var0x2`  |                     | `[{ "address": "0x1", "msb": 2, "lsb": 1 }]`              | `"var0x2"`      |
| `Save__0x1[1:2]__0x2[3:4]__0x4__0x5__Varmulti` |                     | `[{ "address": "0x1", "msb": 2, "lsb": 1 }, { "address": "0x2", "msb": 4, "lsb": 3 }, { "address": "0x4", "msb": 7, "lsb": 0 }, { "address": "0x5", "msb": 7, "lsb": 0 }]` | `"Varmulti"`      |

## 9. Restore Parse

Describes commands for restoring register values from a variable.

**Syntax:** `RESTORE_REGISTER Address=<address>, MSB=<msb>, LSB=<lsb>, Restore_Variable=<variable_name>`

| Input                      | Output (DFT Syntax) | `registers`                                                  | `restore_variable` |
|----------------------------|---------------------|-------------------------------------------------------------|--------------------|
| `Restore__0x01__var0x1`    |                     | `[{ "address": "0x01", "msb": 7, "lsb": 0 }]`              | `"var0x1"`         |
| `Restore__0x1[2:1]__var0x2` |                     | `[{ "address": "0x1", "msb": 2, "lsb": 1 }]`              | `"var0x2"`         |
| `Restore__0x1[1:2]__0x2[3:4]__0x4__0x5__Varmulti` |                     | `[{ "address": "0x1", "msb": 2, "lsb": 1 }, { "address": "0x2", "msb": 4, "lsb": 3 }, { "address": "0x4", "msb": 7, "lsb": 0 }, { "address": "0x5", "msb": 7, "lsb": 0 }]` | `"Varmulti"`         |

## 10. Force Sweep Parse

Describes commands for sweeping voltage or current on a pin.

**Syntax:** `SWEEP <primary_signal>, [<secondary_signal>], Initial_Value=<value>, Unit=<unit>, Final_Value=<value>, Unit=<unit>, [Step_Size=<value>, Multiplier=<multiplier>, Unit=<unit>], [Sweep_Time=<value>, Multiplier=<multiplier>, Unit=<unit>] ; [Comment]`

| Input                                     | Output (DFT Syntax) | `primary_signal` | `secondary_signal` | `initial_value`                                                     | `final_value`                                                     | `step_size`                                                         | `sweep_time`                                                         |
|-------------------------------------------|---------------------|------------------|--------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| `Force__Sweep__VBAT`                      |                     | `null`           | `null`             | `null`                                                              | `null`                                                              | `null`                                                              | `null`                                                              |
| `Force__Sweep__VBOOST__VCC2+__3V__5V__0.01mV__1mS` |                     | `"VBOOST"`         | `"VCC2+"`          | `{ "raw_value": 3.0, "multiplier": 1, "unit": "V", "final_value": 3.0, "multiplier_prefix": "" }` | `{ "raw_value": 5.0, "multiplier": 1, "unit": "V", "final_value": 5.0, "multiplier_prefix": "" }` | `{ "raw_value": 0.01, "multiplier": 0.001, "unit": "V", "final_value": 1.0E-5, "multiplier_prefix": "m" }` | `{ "raw_value": 1.0, "multiplier": 0.001, "unit": "S", "final_value": 0.001, "multiplier_prefix": "m" }` |
| `Force__Sweep__VBAT__2V__1V`               |                     | `"VBAT"`           | `"GND"`            | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `null`                                                              | `null`                                                              |
| `Force__Sweep__VBAT__SDWN__2V__1V`        |                     | `"VBAT"`           | `"SDWN"`           | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `null`                                                              | `null`                                                              |
| `Force__Sweep__VBAT__GND__2V__1V__1mV`     |                     | `"VBAT"`           | `"GND"`            | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 0.001, "unit": "V", "final_value": 0.001, "multiplier_prefix": "m" }` | `null`                                                              |
| `Force__Sweep__VBAT__GND__2V__1V__1mV__100uS` |                     | `"VBAT"`           | `"GND"`            | `{ "raw_value": 2.0, "multiplier": 1, "unit": "V", "final_value": 2.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 1, "unit": "V", "final_value": 1.0, "multiplier_prefix": "" }` | `{ "raw_value": 1.0, "multiplier": 0.001, "unit": "V", "final_value": 0.001, "multiplier_prefix": "m" }` | `{ "raw_value": 100.0, "multiplier": 1.0E-6, "unit": "S", "final_value": 9.999999999999999E-5, "multiplier_prefix": "u" }` |
