from typing import Any, Iterator
from io import StringIO
from itertools import chain
import sys


class namedtuple(tuple):
    __namedvalues__: dict[str, Any]
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, args)
        instance.__namedvalues__ = kwargs
        return instance
    
    @property
    def unnamed_values(self) -> tuple:
        return tuple(super().__iter__())
    
    @property
    def named_values(self) -> dict:
        return self.__namedvalues__.copy()
    
    def keys(self):
        return chain(range(super().__len__()), self.__namedvalues__.keys())
    
    def values(self):
        return self.__iter__()
    
    def items(self):
        return chain(zip(range(super().__len__()), super().__iter__()), self.__namedvalues__.items())
    
    def __len__(self) -> int:
        return super().__len__() + len(self.__namedvalues__)
    
    def __contains__(self, key: Any) -> bool:
        return super().__contains__(key) or key in self.__namedvalues__.values()
    
    def __getattr__(self, name: str) -> Any:
        return self.__namedvalues__[name]
    
    def __getitem__(self, key: Any) -> Any:
        if isinstance(key, str):
            return self.__namedvalues__[key]
        else:
            return super().__getitem__(key)
    
    def __iter__(self) -> Iterator[Any]:
        return chain(super().__iter__(), self.__namedvalues__.values())
    
    def __repr__(self) -> str:
        output = StringIO()
        output.write('(')
        for value in super().__iter__():
            output.write(f'{value}, ')
        named_length = len(self.__namedvalues__)
        length = super().__len__()
        if named_length == 0:
            output = output.getvalue()
            if length == 0:
                return '(,)'
            elif length == 1:
                output[-1] = ')'
                return output
            else:
                output[-2] = ')'
                return output[:-1]
        for i, (key, value) in enumerate(self.__namedvalues__.items()):
            output.write(f'{key}={repr(value)}')
            if i != named_length - 1:
                output.write(', ')
        output.write(')')
        return output.getvalue()
    
    def __lt__(self, value) -> bool:
        tuple_result = super().__lt__(value)
        if isinstance(value, namedtuple):
            for key, val in self.__namedvalues__.items():
                tuple_result = tuple_result and (value.__namedvalues__[key] < val)
        return tuple_result
    
    def __le__(self, value: tuple[Any, ...]) -> bool:
        tuple_result = super().__le__(value)
        if isinstance(value, namedtuple):
            for key, val in self.__namedvalues__.items():
                tuple_result = tuple_result and (value.__namedvalues__[key] <= val)
        return tuple_result
    
    def __gt__(self, value: tuple[Any, ...]) -> bool:
        tuple_result = super().__gt__(value)
        if isinstance(value, namedtuple):
            for key, val in self.__namedvalues__.items():
                tuple_result = tuple_result and (value.__namedvalues__[key] > val)
        return tuple_result
    
    def __ge__(self, value: tuple[Any, ...]) -> bool:
        tuple_result = super().__ge__(value)
        if isinstance(value, namedtuple):
            for key, val in self.__namedvalues__.items():
                tuple_result = tuple_result and (value.__namedvalues__[key] >= val)
        return tuple_result
    
    def __eq__(self, value: Any) -> bool:
        tuple_result = super().__eq__(value)
        if isinstance(value, namedtuple):
            for key, val in self.__namedvalues__.items():
                try:
                    tuple_result = tuple_result and (value.__namedvalues__[key] == val)
                except KeyError:
                    return False
            return tuple_result
        return False
    
    def __hash__(self) -> int:
        return super().__hash__()
    
    def __add__(self, value: tuple[Any, ...]) -> tuple[Any, ...]:
        tuple_result = namedtuple(*super().__add__(value), **self.__namedvalues__)
        if isinstance(value, namedtuple):
            for key in tuple_result.__namedvalues__.keys():
                if key in value.__namedvalues__:
                    value.__namedvalues__[f'{key}_'] = value.__namedvalues__.pop(key)
            tuple_result.__namedvalues__.update(value.__namedvalues__)
        return tuple_result

    def count(self, value: Any) -> int:
        return super().count(value) + sum([1 if value == val else 0 for val in self.__namedvalues__.values()])
    
    def index(self, value: Any, start = 0, stop = sys.maxsize, /) -> int:
        try:
            return super().index(value, start, stop)
        except ValueError:
            for key, val in self.__namedvalues__.items():
                if value == val and key >= start and key < stop:
                    return key