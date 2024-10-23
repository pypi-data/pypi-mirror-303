from .coverage import *

coverage_start()

import os
import sys

# for unit testing
if os.environ.get("MANIPULATE_PYTHON_VERSION"):
    sys.version_info = (3, 7)

# for unit testing
if os.environ.get("MANIPULATE_SPHINX_VERSION"):
    import sphinx

    sphinx.version_info = (6, 1, 9)

from .main import *
