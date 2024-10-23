# pylint: disable=C0103 # name doesn't conform to snake_case naming style
"""
__init__ module for rebrick package
"""
import os
import sys
__AGXVERSION__ = "2.38.0.2"
__version__ = "0.13.2"

# pylint doesn't like bare excepts, but we need to catch all exceptions here
# pylint: disable=W0702 # bare-except
# pylint doesn't like below errors which is normally ok, but this file is copied to the right place during build
# pylint: disable=E0402 # Attempted relative import beyond top-level
# pylint: disable=E0611 # Missing name in module
# pylint: disable=W0611 # Unused import
# pylint: disable=W0401 # Wildcard import

try:
    import agx
    if agx.__version__ != __AGXVERSION__:
        print(f"This version of brickagx is compiled for AGX {__AGXVERSION__} and may crash with your {agx.__version__} version, "+
              "update brickagx or AGX to make sure the versions are suited for eachother")
except:
    print("Failed finding AGX Dynamics, have you run setup_env?")
    sys.exit(255)


if "DEBUG_AGXBRICK" in os.environ:
    print("#### Using Debug build ####")
    try:
        from .debug.api import *
        from .debug import Core
        from .debug import Math
        from .debug import Physics
        from .debug import Simulation
    except:
        print("Failed finding rebrick modules or libraries, did you set PYTHONPATH correctly? "+
              "Should point to where rebrick directory with binaries are located")
        print("Also, make sure you are using the same Python version the libraries were built for.")
        sys.exit(255)
else:
    try:
        from .api import *
        from . import Core
        from . import Math
        from . import Physics
        from . import Simulation
    except:
        print("Failed finding rebrick modules or libraries, did you set PYTHONPATH correctly? "+
              "Should point to where rebrick directory with binaries are located")
        print("Also, make sure you are using the same Python version the libraries were built for.")
        sys.exit(255)
