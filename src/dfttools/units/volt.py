from enum import Enum

class Volt(Enum):
    nV = 'nV'  # Nanovolt (10^-9)
    uV = 'uV'  # Microvolt (10^-6)
    mV = 'mV'  # Millivolt (10^-3)
    V = 'V'    # Volt (1)

base_values = {
    Volt.nV.value: 1e-9,
    Volt.uV.value: 1e-6,
    Volt.mV.value: 1e-3,
    Volt.V.value: 1,
}
