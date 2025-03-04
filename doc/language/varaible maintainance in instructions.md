

# 

---

# allow me to copy above email content.

---

**Subject: Proposal for Variable Name Option in Measurement Operations**

---



I’ve been thinking about our current approach, and I propose adding an option to provide a variable name during measurement operations. This would allow us to store the measured value in a database during test execution under the specified variable name.

### Proposed Approach:

1. **Instruction Writing:**
    - Example usage:

```python
VMEAS(signal='SDWN', unit=mV, variable='VarSDWN', comment='Measure voltage and store in variable')
```

    - Output (human-readable format):

```
Instruction 0: Voltage measurement: SDWN with respect to GND, unit: mV, save measurement to: VarSDWN (Measure voltage and store in variable)
```

    - Stored in the database:

```json
[
  {
    "instructionNo": 0,
    "instruction": "VMEAS",
    "Signal": "SDWN",
    "Reference": "GND",
    "unit": "mV",
    "Variable": "VarSDWN",
    "comment": "(Measure voltage and store in variable)"
  }
]
```

2. **Testing Level Execution:**
    - Execute the sequence of instructions from the database.
    - For example, upon encountering the instruction:

```json
{
  "instructionNo": 0,
  "instruction": "VMEAS",
  "Signal": "SDWN",
  "Reference": "GND",
  "unit": "mV",
  "Variable": "VarSDWN",
  "comment": "(Measure voltage and store in variable)"
}
```

    - The test engineer can write a measurement program for the signals and store the values in a global dictionary (in the test program, which is separate from the DFT writing stage).
    - Use formula calculations with AST (Abstract Syntax Tree). For example:

```python
self.Vars['VarSDWN'] = measured_value_from_instruction
self.Vars might contain multiple variables and their corresponding data (self.Vars -> {'VarSDWN': 0.1, ...})

formula = "(353/(1 + VarSDWN)) - CODE30"
vars = {"VarSDWN": 0.1, "CODE30": 0.4}
result = solve_formula(formula, vars)
print(f"Result VarSDWN: {result}")
```

    - Expected output:

```
Result VarSDWN: 320.5090909090909
```

3. **Additional Code Information:**
    - I will attach the `solve_formula` code for reference, but feel free to ignore it if it seems too technical.
```python
import ast
import operator

def solve_formula(formula_string, variables=None):
    """
    Safely evaluates a mathematical formula string with variable substitution.

    Args:
        formula_string: The mathematical formula as a string (e.g., "a + b * 2").
        variables: A dictionary containing variable names and their values (e.g., {"a": 10, "b": 5}).

    Returns:
        The result of the evaluated formula or None if invalid.
    """
    # Code implementation...
```





