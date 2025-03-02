# python 13 has enums, should we use them ?

from typing import List, Tuple

class Enum():
    @property
    def value(self) -> int:
        return self._v
    @property
    def allowed_values(self) -> List[int]:
        return self.allowed
    def __init__(self, v:int, allowed:List[Tuple[int, str]]):
        self.allowed = allowed
        if v not in list(x[0] for x in allowed):
            raise ValueError
        self._v = v
    def __int__(self):
        return self.value
    def __hash__(self):
        return self.__repr__().__hash__() + self.value
    def __eq__(self, v) -> bool:
        if isinstance(v, Enum):
            return self.value == v.value
        elif isinstance(v, int):
            return self.value == v
        else:
            raise ValueError('can compare two Enums or an Enum and an int')
    def __repr__(self):
        return self.allowed[self._v][1]
