from typing import overload, Optional, Callable, Any
import inspect


def get_type_attribute(input_type: type, name: str, condition: Optional[Callable[[Any], bool]] = None):
    if condition is None:
        return _get_type_attribute_without_condition(input_type, name)
    else:
        return _get_type_attribute(input_type, name, condition)


def _get_type_attribute_without_condition(input_type: type, key: str):
    for current_type in input_type.__mro__:
        item = current_type.__dict__.get(key)
        if item is not None:
            break
    return item


def _get_type_attribute(input_type: type, key: str, condition: Callable[[Any], bool]):
    for current_type in input_type.__mro__:
        item = current_type.__dict__.get(key)
        if item is not None and condition(item):
            break
    return item


class typeattrbase:
    @overload
    def __init__(self, type: type):
        ...
    
    @overload
    def __init__(self, instance: Any):
        ...
    
    @overload
    def __init__(self, condition: Callable[[Any], bool]):
        ...
    
    @overload
    def __init__(self, type: type, condition: Callable[[Any], bool]):
        ...
    
    @overload
    def __init__(self, instance: Any, condition: Callable[[Any], bool]):
        ...
    
    def __init__(self, *args):
        from .inspection import self_from_frame
        length = len(args)
        self.__condition = None
        if length == 0:
            last_self = self_from_frame(inspect.currentframe().f_back)
        elif length == 1:
            if type(args[0]) is type:
                last_self = None
                self_type = args[0]
            elif callable(args[0]):
                last_self = self_from_frame(inspect.currentframe().f_back)
                self.__condition = args[0]
            else:
                last_self = args[0]
        elif length == 2:
            if type(args[0]) is type:
                last_self = None
                self_type = args[0]
            else:
                last_self = args[0]
            if callable(args[1]):
                self.__condition = args[1]
        else:
            raise TypeError(f"`{type(self).__class__.__name__}.__init__` takes up to 1 argument.")
        if last_self is not None:
            self_type = type(last_self)
        elif self_type is not None:
            raise TypeError(f"the class `{type(self).__class__.__name__}` without a type argument should be used in a class.")
        self.__type = self_type
        if not self.__condition:
            self.__condition = lambda _: True
    
    def condition(self, item):
        return self.__condition(item)
    
    def __getitem__(self, key):
        return get_type_attribute(self.__type, key, self.condition)
    
    def __getattr__(self, name):
        return self[name]
    
    def __repr__(self) -> str:
        main_str = str(self.__type)
        splitted = main_str.split("'")
        if len(splitted) > 2:
            return f"<'{splitted[1]}': {self.__type.__dict__}>"
        else:
            return main_str


class typeattr(typeattrbase):
    @property
    def __base__(self):
        instance = super().__new__(typeattr)
        instance.__type = self.__type.__base__
        return instance