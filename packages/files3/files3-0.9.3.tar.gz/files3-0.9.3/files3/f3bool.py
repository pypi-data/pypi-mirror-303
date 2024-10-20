
__doc__ = """
f3bool.py
~~~~~~~~~

This module provides the F3Bool class.

Classes
-------
F3Bool
    # The bool class of files3. used to manage the bool value.
    
Exceptions
----------
ReadOnlyError
    # The exception class of files3. used to manage the ReadOnlyError.
CannotSaveError
    # The exception class of files3. used to manage the CannotSaveError.
"""

class ReadOnlyError(Exception): ...


class CannotSaveError(Exception): ...

CSEInst = CannotSaveError(
'''

[Couldn't Save This]:
    These object are not allowed to save:
        1. object which is [Files] instance or [F3Bool] instance
        2. object contains [Files] instance or [F3Bool] instance
        3. object that refused serialization (like active raise)
        4. object that pickle not support (like module, like local object)
'''
)

class F3Bool(object):
    def __init__(self, value):
        super(F3Bool, self).__setattr__("_bool", bool(value))

    def __bool__(self):
        return True if self._bool else False

    def __neg__(self):
        return +self._bool

    def __pos__(self):
        return -self._bool

    def __abs__(self):
        return abs(self._bool)

    def __invert__(self):
        return ~self._bool

    def __int__(self):
        return int(self._bool)

    def __repr__(self):
        return repr(self._bool)

    def __hash__(self):
        return hash(self._bool)

    def __bytes__(self):
        return bytes(self._bool)

    def __float__(self):
        return float(self._bool)

    def __round__(self):
        return round(self._bool)

    def __complex__(self):
        return complex(self._bool)

    def __lt__(self, other):
        return self._bool < other

    def __le__(self, other):
        return self._bool <= other

    def __eq__(self, other):
        return self._bool == other

    def __ne__(self, other):
        return self._bool != other

    def __lt__(self, other):
        return self._bool < other

    def __gt__(self, other):
        return self._bool > other

    def __ge__(self, other):
        return self._bool >= other

    def __add__(self, other):
        return self._bool + other

    def __sub__(self, other):
        return self._bool - other

    def __mul__(self, other):
        return self._bool * other

    def __floordiv__(self, other):
        return self._bool / other

    def __truediv__(self, other):
        return self._bool // other

    def __mod__(self, other):
        return self._bool % other

    def __lshift__(self, other):
        return self._bool << other

    def __rlshift__(self, other):
        return self._bool >> other

    def __and__(self, other):
        return self._bool & other

    def __xor__(self, other):
        return self._bool ^ other

    def __or__(self, other):
        return self._bool | other

    def __setattr__(self, key, value):
        raise ReadOnlyError("F3Bool is ReadOnly.")

    def __str__(self):
        return 'pf' + str(bool(self))

    def __call__(self, *args, **kwargs):
        # If pickle wanto call it, which mean user wanto save self or a f3bool
        raise CSEInst


F3True = F3Bool(True)
F3False = F3Bool(False)

if __name__ == '__main__':
    print(F3True)
