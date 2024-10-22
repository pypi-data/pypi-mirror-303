import ctypes


# class pytype(type):
#     def __init__(self, obj: object, /) -> None: ...
#     def __new__(cls, obj: object, /) -> type:
#         from .private import _pytype
#         return _pytype(obj)


decref = ctypes.pythonapi.Py_DecRef
decref.argtypes = [ctypes.py_object]
decref.restype = None


incref = ctypes.pythonapi.Py_IncRef
incref.argtypes = [ctypes.py_object]
incref.restype = None


class framelocals:
    def __init__(self, frame):
        self.frame = frame
    
    def __reversed__(self):
        return reversed(self.frame.f_locals)
    
    def __len__(self):
        return len(self.frame.f_locals)
    
    def __contains__(self, key: str):
        return self.frame.f_locals.__contains__(key)
    
    def __iter__(self):
        return iter(self.frame.f_locals)
    
    def __getitem__(self, key: str):
        return self.frame.f_locals[key]
    
    def __setitem__(self, key: str, value):
        from .private import modify_frame_locals
        modify_frame_locals(self.frame, key, value)
    
    def __delitem__(self, key: str):
        from .private import delete_from_frame_locals
        delete_from_frame_locals(self.frame, key)
    
    def update(self, new_dict: dict):
        from .private import add_to_frame_locals
        add_to_frame_locals(self.frame, new_dict)
    
    def get(self, key: str):
        return self.frame.f_locals.get(key)
    
    def pop(self, key: str):
        from .private import delete_from_frame_locals
        delete_from_frame_locals(self.frame, key)
    
    def copy(self):
        return self.frame.f_locals.copy()
    
    def setdefault(self, key: str, default = None):
        return self.frame.f_locals.setdefault(key, default)
    
    def items(self):
        return self.frame.f_locals.items()
    
    def keys(self):
        return self.frame.f_locals.keys()
    
    def values(self):
        return self.frame.f_locals.values()