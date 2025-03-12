import sys, argparse, os

from anytree import find_by_attr

from dfttools.glob import g

import dfttools.instructions
import dfttools.units

from code import InteractiveConsole as InteractiveConsole

from ivm_audio_config.lib.DataInterface import DataInterface
from ivm_audio_config.lib.Block import Block
from box import ConfigBox
import yaml
from box.exceptions import BoxValueError

def read_yaml(path_to_yaml) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            # log.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


print('toy test language interpreter')

def do_run(di, args):
    pins = read_yaml('ivm6201/pinmap.yaml').pins
    
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

    os.write(sys.stdout.fileno(), 'c to store script x to end program >>> '.encode())
    instructions = []
    while True:
        l = sys.stdin.readline()
        if len(l) == 0:
            sys.exit(0)
        try:
            if l.strip('\n') == 'c':
                print(l)
                instructions_set = ''.join(instructions)
                ip = str(input('Enter IP :>'))
                folder_path = f'ivm6201/{ip}'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                test_script = str(input('Enter test name :>'))
                with open(f'{folder_path}/{test_script}.py','w') as file :
                    file.write(instructions_set)
            if not c.push(l):
                instructions.append(l)
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
