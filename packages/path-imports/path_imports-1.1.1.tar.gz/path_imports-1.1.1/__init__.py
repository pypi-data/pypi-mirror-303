
# Resides in the project root directory, making the project importable (since my
# projects folder is on the PYTHONPATH).

import sys
from pathlib import Path


here = Path(__file__).absolute().parent
name = here.stem

# Discard this dummy module and import the actual code
sys.path.insert(0, str(here))
del sys.modules[name]
sys.modules[__name__] = __import__(name)
del sys.path[0]
