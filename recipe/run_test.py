try:
    from importlib.resources import files as resources_files
except ImportError:
    from importlib_resources import files as resources_files


# Check if DLL exist
base_path = resources_files('pythonnet') / 'runtime'
for ext in ['deps.json', 'dll', 'pdb']:
    if not (base_path / f'Python.Runtime.{ext}').exists():
        raise FileNotFoundError(f'DLL runtime/Python.Runtime.{ext} not found in package.')


import clr
import System.IO
from System.IO import *


# Check if import dotnet-modules work
assert 'FileStream' in globals()
