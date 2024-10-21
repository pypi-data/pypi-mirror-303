r"""
 ________    ___  ___   _____ ______    ________   ___    ___  ________   ___    ___
|\   ___  \ |\  \|\  \ |\   _ \  _   \ |\   __  \ |\  \  /  /||\   __  \ |\  \  /  /|
\ \  \\ \  \\ \  \\\  \\ \  \\\__\ \  \\ \  \|\  \\ \  \/  / /\ \  \|\  \\ \  \/  / /
 \ \  \\ \  \\ \  \\\  \\ \  \\|__| \  \\ \   ____\\ \    / /  \ \   ____\\ \    / /
  \ \  \\ \  \\ \  \\\  \\ \  \    \ \  \\ \  \___| \/  /  /    \ \  \___| \/  /  /
   \ \__\\ \__\\ \_______\\ \__\    \ \__\\ \__\  __/  / /       \ \__\  __/  / /
    \|__| \|__| \|_______| \|__|     \|__| \|__| |\___/ /         \|__| |\___/ /
                                                 \|___|/                \|___|/

NumPyPy
==========

(It is an alias for PyPyNum) PyPyNum is a Python library for math & science computations, covering algebra, calculus,
stats, with data structures like matrices, vectors, tensors. It offers numerical tools, programs, and supports
computational ops, functions, processing, simulation, & visualization in data science & ML, crucial for research,
engineering, & data processing.

Copyright
==========

- Author: Shen Jiayi
- Email: 2261748025@qq.com
- Copyright: Copyright (c) 2023, Shen Jiayi. All rights reserved.
"""

__author__ = "Shen Jiayi"
__email__ = "2261748025@qq.com"
__copyright__ = "Copyright (c) 2023, Shen Jiayi. All rights reserved."

import sys

stdout = sys.stdout
sys.stdout = None

try:
    from pypynum import *
    from pypynum import __version__ as version
except ImportError:
    raise RuntimeError("You may not have downloaded PyPyNum, please use the command 'pip install PyPyNum' or other "
                       "methods to download it.")
sys.stdout = stdout
__version__ = "1.16.1"
if version != __version__:
    raise RuntimeError("The version {} of PyPyNum does not match the version {} of NumPyPy. "
                       "Please update both packages to the latest version.".format(version, __version__))
print("NumPyPy", "Version -> " + __version__, "It is an alias for PyPyNum",
      "See also PyPI link for PyPyNum -> https://pypi.org/project/PyPyNum/", sep=" | ")


def test():
    from pypynum import test
    return test


def this():
    from pypynum import this
    return this
