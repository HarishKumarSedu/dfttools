import sys, argparse, os

from anytree import find_by_attr

from dfttools.glob import g

import dfttools.instructions
import dfttools.units

from code import InteractiveConsole as InteractiveConsole

from ivm_audio_config.lib.DataInterface import DataInterface
from ivm_audio_config.lib.Block import Block


print('toy test language interpreter')

def do_run(di, args):

    dev = di.get_device(args.dev_type)
    b = Block(None, dev)

    # Temporary, at the moment we use the pattern generator only
    g.dut_description = find_by_attr(b, 'PTN.0', maxlevel = 2)

    for m in dfttools.instructions.__all__:
        exec(f'from dfttools.instructions.{m} import *')

    # ut -> unit type (time, voltage, current, ...)
    # un -> unit name (ps, ns, us, ms, s, uV, mV, ....)
    for ut in dfttools.units.__all__:
        exec(f'from dfttools.units.{ut} import *')

    for bf in g.dut_description.registers:
        locals().update({ bf: bf })
        
    locals().update({'g': g})
        
    c = InteractiveConsole(locals())

    os.write(sys.stdout.fileno(), '>>> '.encode())

    while True:
        l = sys.stdin.readline()
        if len(l) == 0:
            sys.exit(0)
        print(l)
        try:
            if not c.push(l):
                # No more input required, print translation and new prompt
                k = 0
                # print(g.output)
                for i in g.output:
                    print(f'instruction {k}: {str(i)}')
                    k += 1
                w = os.write(sys.stdout.fileno(), '>>> '.encode())
            else:
                print("\t", end='')
        except Exception as e:
            print(f'Error: {e}')
            sys.exit(127)


def run():
    try:
        di = DataInterface()
    except Exception as e:
        print(f'cannot create data interface ({e})')
        sys.exit(127)

    devtypes = di.get_codecs_types()


    parser = argparse.ArgumentParser(description='toy test language parser')
    parser.add_argument('--dev-type', dest='dev_type',
                        help=f'dev type: one of: {str(devtypes)}',
                        default='ivm6303')
    args = parser.parse_args()
    do_run(di, args)
