from . import mirror
from .mirror import *
from .converter import cast
from .inspection import *
from . import pybase
from .type_attribute import typeattr
from .hidden_attribute import hidden, HiddenMeta


def function_name(depth = 0):
    from sys import _getframe
    return _getframe(depth + 1).f_code.co_name