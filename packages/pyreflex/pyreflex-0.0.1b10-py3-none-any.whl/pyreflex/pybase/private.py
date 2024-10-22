from types import FrameType
import ctypes
import sys

class PyObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_ssize_t),
                ("ob_type", ctypes.c_void_p)]


def _pytype(obj) -> type:
    py_obj = PyObject.from_address(id(obj))
    return ctypes.cast(py_obj.ob_type, ctypes.py_object).value


if (sys.version_info.major, sys.version_info.minor) < (3, 13):
    def modify_frame_locals(frame: FrameType, key: str, value):
        frame.f_locals[key] = value
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(0))


    def add_to_frame_locals(frame: FrameType, new_dict: dict):
        frame.f_locals.update(new_dict)
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(0))
    
    
    def delete_from_frame_locals(frame: FrameType, key: str):
        frame.f_locals.pop(key)
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(0))
    
    
    def modify_frame_locals_temporarily(frame: FrameType, key: str, value):
        frame.f_locals[key] = value
    
    
    def add_to_frame_locals_temporarily(frame: FrameType, new_dict: dict):
        frame.f_locals.update(new_dict)
    
    
    def delete_from_frame_locals_temporarily(frame: FrameType, key: str):
        frame.f_locals.pop(key)
else:
    def _get_framelocalsproxy():
        return type(sys._getframe().f_locals)
    FrameLocalsProxy = _get_framelocalsproxy()
    
    
    def modify_frame_locals(frame: FrameType, key: str, value):
        frame.f_locals[key] = value


    def add_to_frame_locals(frame: FrameType, new_dict: dict):
        frame.f_locals.update(new_dict)
    
    
    def delete_from_frame_locals(frame: FrameType, key: str):
        frame.f_locals.__delitem__(key)
    
    
    modify_frame_locals_temporarily = modify_frame_locals
    add_to_frame_locals_temporarily = add_to_frame_locals
    delete_from_frame_locals_temporarily = delete_from_frame_locals