from typing import Optional, Callable
from types import MethodType
from copy import copy
from functools import wraps
from io import StringIO
import weakref
import inspect
from ..pybase import decref
from ..pybase import incref


# class SpecializedTypes(dict):
#     def get(self, key):
#         if not isinstance(key, tuple):
#             key = (key,)
#         item = super().get(key)
#         if item is not None:
#             item = item[0]
#         return item
    
#     def __getitem__(self, key):
#         if not isinstance(key, tuple):
#             key = (key,)
#         return super().__getitem__(key)[0]
    
#     def __setitem__(self, key, value):
#         if isinstance(key, tuple):
#             def finalize():
#                 _, finalizers = self.pop(key)
#                 (finalizer.detach() for finalizer in finalizers)
#             finalizers = [weakref.finalize(subkey, finalize) for subkey in key]
#             return super().__setitem__(key, (value, finalizers))
#         else:
#             tuple_key = (key,)
#             def finalize():
#                 self.pop(tuple_key)
#             weakref.finalize(key, finalize)
#             return super().__setitem__(tuple_key, (value, None))


class specialization(dict):
    def __getitem__(self, key):
        if isinstance(key, tuple):
            weakkey = tuple(weakref.ref(each) for each in key)
        else:
            weakkey = weakref.ref(key)
        return super().__getitem__(weakkey)[0]()
    
    def __setitem__(self, key, value):
        def remove_key(weakkey, selfref=weakref.ref(self)):
            self = selfref()
            if self is not None:
                try:
                    self.pop(weakkey)
                except KeyError: ...
        if isinstance(key, tuple):
            weakkey = tuple(weakref.ref(each) for each in key)
            def finalize(selfref=weakref.ref(self)):
                self = selfref()
                if self is not None:
                    try:
                        _, finalizers = self.pop(weakkey)
                        (finalizer.detach() for finalizer in finalizers)
                    except KeyError: ...
            finalizers = [weakref.finalize(subkey, finalize) for subkey in key]
        else:
            weakkey = weakref.ref(key)
            weakref.finalize(key, lambda: remove_key(weakkey))
            finalizers = None
        return super().__setitem__(weakkey, (weakref.ref(value, lambda _: remove_key(weakkey)), finalizers))
    
    def get(self, key):
        if isinstance(key, tuple):
            weakkey = tuple(weakref.ref(each) for each in key)
        else:
            weakkey = weakref.ref(key)
        item = super().get(weakkey)
        if item is not None:
            item = item[0]()
        return item


class generic:
    @staticmethod
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    
    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super(object).__init_subclass__()
        setattr(cls, f'__specialized_types', specialization())
    
    @classmethod
    def __class_getitem__(cls, *args):
        ...

__new__ = staticmethod(generic.__dict__['__new__'].__wrapped__)
__init_subclass__ = classmethod(generic.__dict__['__init_subclass__'].__wrapped__)
__class_getitem__ = classmethod(generic.__dict__['__class_getitem__'].__wrapped__)


class generic:
    __type__: Optional[type]
    __types__: Optional[tuple[type, ...]]
    
    @staticmethod
    def __new__(cls, *args, **kwargs):
        if cls is generic and len(args) == 1:
            maybe_func = args[0]
            if callable(maybe_func) or isinstance(maybe_func, classmethod):
                return dispatcher(maybe_func)
        return super().__new__(cls)
    
    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        setattr(cls, f'__specialized_types', specialization())
        if '__init_subclass__' not in cls.__dict__:
            setattr(cls, '__init_subclass__', __init_subclass__)
        if '__new__' not in cls.__dict__:
            setattr(cls, '__new__', __new__)
    
    @classmethod
    def __class_getitem__(cls, typelike) -> type:
        specialized_types: dict[type, type] = getattr(cls, '__specialized_types')
        result = specialized_types.get(typelike)
        if result is None:
            if isinstance(typelike, type):
                decref(typelike)
                inner_name = typelike.__qualname__
                is_multiple = False
            elif isinstance(typelike, tuple):
                inner_name = StringIO()
                length = len(typelike)
                for i, each_type in enumerate(typelike):
                    decref(each_type)
                    inner_name.write(each_type.__qualname__)
                    if i != length - 1:
                        inner_name.write(', ')
                inner_name = inner_name.getvalue()
                is_multiple = True
            else:
                raise TypeError("argument(s) in the '[]' should be type(s)")
            class TypedGeneric(cls): ...
            delattr(TypedGeneric, f'__specialized_types')
            setattr(TypedGeneric, '__class_getitem__', __class_getitem__)
            TypedGeneric.__name__ = f'{cls.__name__}[{inner_name}]'
            TypedGeneric.__qualname__ = f'{cls.__qualname__}[{inner_name}]'
            TypedGeneric.__module__ = cls.__module__
            if is_multiple:
                TypedGeneric.__types__ = typelike
                def finalize(types = tuple(weakref.ref(each) for each in typelike)):
                    for type in types:
                        type = type()
                        if type is not None:
                            incref(type)
                weakref.finalize(TypedGeneric, finalize)
            else:
                TypedGeneric.__type__ = typelike
                def finalize(type = weakref.ref(typelike)):
                    type = type()
                    if type is not None:
                        incref(type)
                weakref.finalize(TypedGeneric, finalize)
            result = TypedGeneric
            specialized_types[typelike] = result
        return result

setattr(generic, f'__specialized_types', specialization())


class dispatcher:
    __slots__ = ('function', 'instance', 'type', '__parameters', '__return_annotation', '__name__', '__qualname__', '__module', '__doc__')
    
    def __init__(self, function):
        self.function = function
        self.instance = None
        self.type = None
        
        if isinstance(function, staticmethod):
            function = function.__wrapped__
        elif isinstance(function, classmethod):
            function = function.__wrapped__
        self.__name__ = function.__name__
        self.__qualname__ = function.__qualname__
        self.__module = function.__module__
        self.__doc__ = function.__doc__
        
        signature = inspect.signature(function)
        self.__parameters = list(signature.parameters.values())
        self.__return_annotation = signature.return_annotation
    
    def __get__(self, instance, owner):
        self.instance = instance
        self.type = owner
        return self
    
    def __getitem__(self, typelike):
        params = copy(self.__parameters)
        function = self.function
        def get_final_function(wrapper): return wrapper
        if self.type is None or isinstance(self.function, staticmethod):
            params.pop(0)
            try:
                function = function.__wrapped__
            except AttributeError: ...
            @wraps(function)
            def wrapper(*args, **kwargs):
                return function(typelike, *args, **kwargs)
        elif isinstance(self.function, classmethod):
            params.pop(1)
            function = self.function.__wrapped__
            @wraps(function)
            def wrapper(cls, *args, **kwargs):
                return function(cls, typelike, *args, **kwargs)
            def get_final_function(wrapper): return MethodType(wrapper, self.type)
        else:
            params.pop(1)
            @wraps(function)
            def wrapper(instance, *args, **kwargs):
                return function(instance, typelike, *args, **kwargs)
            if self.instance is not None:
                def get_final_function(wrapper): return MethodType(wrapper, self.instance)
        if isinstance(typelike, tuple):
            type_output = StringIO()
            final_index = len(typelike) - 1
            for i, each in enumerate(typelike):
                type_output.write(each.__qualname__)
                if i != final_index:
                    type_output.write(', ')
            type_output = type_output.getvalue()
        else:
            type_output = typelike.__qualname__
        signature = inspect.Signature(parameters=params, return_annotation=self.__return_annotation)
        wrapper.__name__ = function.__name__
        wrapper.__qualname__ = f'{function.__qualname__}[{type_output}]'
        wrapper.__module__ = function.__module__
        wrapper.__doc__ = function.__doc__
        wrapper.__signature__ = signature
        return get_final_function(wrapper)
    
    def __call__(self, *args, **kwargs):
        function = self.function
        if self.type is None or isinstance(self.function, staticmethod):
            return function(None, *args, **kwargs)
        elif isinstance(self.function, classmethod):
            return function.__wrapped__(self.type, None, *args, **kwargs)
        else:
            if self.instance is None:
                first_arg_name = self.__parameters[0].name
                try:
                    instance = kwargs.pop(first_arg_name)
                    if len(args) > 0:
                        raise TypeError(f"{self.function.__qualname__}() got multiple values for argument '{first_arg_name}'")
                except KeyError:
                    instance = args[0]
                    args = args[1:]
            else:
                instance = self.instance
            return function(instance, None, *args, **kwargs)
    
    def __getattribute__(self, name):
        if name == '__class__':
            if self.instance is None or isinstance(self.function, staticmethod) or isinstance(self.function, classmethod):
                return Callable
            else:
                return MethodType
        elif name == '__module__':
            return self.__module
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        function = self.function
        return getattr(function, name)
    
    def __repr__(self):
        function = self.function
        qualname = function.__qualname__
        params = copy(self.__parameters)
        if self.type is None:
            typelike = params.pop(0)
        elif isinstance(self.function, staticmethod):
            function = self.function.__wrapped__
            typelike = params.pop(0)
        # elif isinstance(self.function, classmethod):
        #     function = self.function.__wrapped__
        #     typelike = params.pop(1)
        else:
            while True:
                if isinstance(self.function, classmethod):
                    anchor = repr(self.type)
                elif self.instance is None:
                    typelike = params.pop(1)
                    break
                else:
                    anchor = f'<{self.type.__module__}.{self.type.__name__} object at {hex(id(self.instance))}>'
                return f"<bound generic template method {qualname} of {anchor}>"
        signature = inspect.Signature(parameters=params, return_annotation=self.__return_annotation)
        return f"<generic template function {function.__module__}.{qualname}[{typelike.name}]{signature}>"
    
    def __instancecheck__(self, obj):
        return self.__subclasscheck__(type(obj))

    def __subclasscheck__(self, cls):
        return issubclass(cls, self.__class__)