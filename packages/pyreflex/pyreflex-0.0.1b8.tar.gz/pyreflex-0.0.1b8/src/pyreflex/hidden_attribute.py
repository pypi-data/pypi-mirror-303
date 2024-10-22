from types import MethodType

def hidden(obj):
    obj.__ishidden__ = True
    return obj


def subclassvisible(obj):
    obj.__issubclassvisible__ = True
    return obj


class HiddenMeta(type):
    def __new__(metacls, name, bases, namespace):
        cls = super().__new__(metacls, name, bases, namespace)
        hidden_names = []
        for name, obj in namespace.items():
            if getattr(obj, '__ishidden__', False):
                hidden_names.append(name)
        if len(hidden_names) > 0:
            original_getattribute = cls.__getattribute__
            def __getattribute__(self, name: str):
                get_attr = MethodType(original_getattribute, self)
                if type(self) is cls and name in hidden_names:
                    self_dict: dict = get_attr('__dict__')
                    item = self_dict.get(name)
                    if item:
                        return item
                    else:
                        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
                else:
                    attr = get_attr(name)
                    if getattr(attr, '__ishidden__', False) and not getattr(attr, '__issubclassvisible__', False):
                        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
                    else:
                        return attr
            cls.__getattribute__ = __getattribute__
        return cls