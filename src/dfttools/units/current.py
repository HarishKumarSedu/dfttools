from enum import Enum

class Current(Enum):
    pA = 'pA'  # Picoampere (10^-12)
    nA = 'nA'  # Nanoampere (10^-9)
    uA = 'uA'  # Microampere (10^-6)
    mA = 'mA'  # Milliampere (10^-3)
    A = 'A'    # Ampere (1)

base_values = {
    Current.pA.value: 1e-12,
    Current.nA.value: 1e-9,
    Current.uA.value: 1e-6,
    Current.mA.value: 1e-3,
    Current.A.value: 1,
}
