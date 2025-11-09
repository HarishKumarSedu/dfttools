from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    # Remove comments and empty lines
    return [line.strip() for line in lines if line.strip() and not line.startswith('#')]

setup(
    name='dfttools',
    version='0.1.0',
    author='Harish Kumar Shivaramappa',
    author_email='harishkumarsedu@gmail.com',
    description='A Python package for hardware operations and testing.',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=parse_requirements('requirements.txt'),  # Reads dependencies from requirements.txt
    python_requires='>=3.7',
)
