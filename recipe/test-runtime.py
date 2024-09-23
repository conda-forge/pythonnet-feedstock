import sys

from importlib.resources import files as resources_files
from pythonnet import load


# Check if DLL exist
base_path = resources_files('pythonnet') / 'runtime'
for ext in ['deps.json', 'dll', 'pdb']:
    if not (base_path / f'Python.Runtime.{ext}').exists():
        raise FileNotFoundError(f'DLL runtime/Python.Runtime.{ext} not found in package.')

runtime = sys.argv[1]
if runtime not in ['mono', 'netfx', 'coreclr']:
    raise ValueError(f'Invalid runtime: {runtime}, must be one of mono, netfx, coreclr.')
load(runtime)

import clr
import System.IO
from System.IO import *


# Check if import dotnet-modules work
assert 'FileStream' in globals()

# Report success
print(f'Loaded {runtime} runtime successfully.')
