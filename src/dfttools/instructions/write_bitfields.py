
from typing import Tuple
from collections import namedtuple

from ..exceptions import ParsingError

from ..glob import g

WriteBitFieldArg = namedtuple('WriteBitFieldArg', 'name, value')


# This is private, we only make WRITE_BITFIELDS usable
def _WRITE_BITFIELD(a: WriteBitFieldArg, **kwargs):
    try:
        bitfield = g.dut_description.registers[a.name]
    except Exception as e:
        raise ParsingError(f'Error looking for bitfield {a.name}')
    else:
        # Translate the operation and add it to the output list of operations
        g.output.extend(bitfield.write(a.value))

#
# WRITE_BITFIELDS((name1, int1), (name2, int2), ...., comment = "blabla")
# where name? ARE the SAME NAMES USED IN THE REGMAP
#
def WRITE_BITFIELDS(*args: Tuple[str, int], **kwargs):
    for a in args:
        if not isinstance(a, tuple) or len(a) != 2:
            raise ParsingError('Use WRITE_BITFIELDS((name,value),...')
        arg = WriteBitFieldArg(*a)
        try:
            _WRITE_BITFIELD(arg, **kwargs)
        except Exception as e:
            raise ParsingError(f'Error running instruction: {e}')
