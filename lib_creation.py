import os

def create_directory_structure(root_dir):
    # Create root directory if it doesn't exist
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Create subdirectories
    subdirectories = [
        os.path.join(root_dir, 'enum'),
        os.path.join(root_dir, 'exceptions'),
        os.path.join(root_dir, 'glob'),
        os.path.join(root_dir, 'instructions'),
        os.path.join(root_dir, 'ops'),
        os.path.join(root_dir, 'units'),
    ]

    for dir_path in subdirectories:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Create files
    files = [
        os.path.join(root_dir, '__init__.py'),
        os.path.join(root_dir, 'enum', '__init__.py'),
        os.path.join(root_dir, 'enum', 'enum.py'),
        os.path.join(root_dir, 'exceptions', '__init__.py'),
        os.path.join(root_dir, 'exceptions', 'exceptions.py'),
        os.path.join(root_dir, 'glob', '__init__.py'),
        os.path.join(root_dir, 'glob', 'glob.py'),
        os.path.join(root_dir, 'instructions', '__init__.py'),
        os.path.join(root_dir, 'instructions', 'force.py'),
        os.path.join(root_dir, 'instructions', 'meas.py'),
        os.path.join(root_dir, 'ops', '__init__.py'),
        os.path.join(root_dir, 'ops', 'forceops.py'),
        os.path.join(root_dir, 'ops', 'measops.py'),
        os.path.join(root_dir, 'units', '__init__.py'),
        os.path.join(root_dir, 'units', 'current.py'),
        os.path.join(root_dir, 'units', 'frequency.py'),
        os.path.join(root_dir, 'units', 'resistance.py'),
        os.path.join(root_dir, 'units', 'time.py'),
        os.path.join(root_dir, 'units', 'volt.py'),
    ]

    for file_path in files:
        if not os.path.exists(file_path):
            open(file_path, 'w').close()  # Create empty file

if __name__ == '__main__':
    root_dir = 'dfttools'
    create_directory_structure(root_dir)
    print(f"Directory structure created for {root_dir}")
