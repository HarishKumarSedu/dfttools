from enum import Enum

class Resistance(Enum):
    pOhm = 'pOhm'  # Picoohm (10^-12)
    nOhm = 'nOhm'  # Nanoohm (10^-9)
    uOhm = 'uOhm'  # Microohm (10^-6)
    mOhm = 'mOhm'  # Milliohm (10^-3)
    Ohm = 'Ohm'    # Ohm (1)

base_values = {
    Resistance.pOhm.value: 1e-12,
    Resistance.nOhm.value: 1e-9,
    Resistance.uOhm.value: 1e-6,
    Resistance.mOhm.value: 1e-3,
    Resistance.Ohm.value: 1,
}
