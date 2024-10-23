from typing import Optional
from types import MethodType
from copy import copy
from functools import wraps
from io import StringIO
import weakref
import inspect
from pyreflex.pybase import deepcopy_class


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


def class_typing(cls):
    try:
        return cls.__type__
    except AttributeError:
        try:
            return cls.__types__
        except ArithmeticError: ...


class specialization(dict):
    def __getitem__(self, key):
        if isinstance(key, tuple):
            weakkey = tuple(weakref.ref(each) for each in key)
        else:
            weakkey = weakref.ref(key)
        return super().__getitem__(weakkey)[0]
    
    def __setitem__(self, key, value):
        from pyreflex.pybase import decref, incref
        def remove_key(weakkey, selfref=weakref.ref(self)):
            self = selfref()
            if self is not None:
                try:
                    self.pop(weakkey)
                except KeyError: ...
        if isinstance(key, tuple):
            weakkey = tuple((weakref.ref(each), decref(each))[0] for each in key)
            def finalize_key(selfref=weakref.ref(self)):
                self = selfref()
                if self is not None:
                    try:
                        _, finalizers = self.pop(weakkey)
                        (finalizer.detach() for finalizer in finalizers)
                    except KeyError: ...
            finalizers = [weakref.finalize(subkey, finalize_key) for subkey in key]
            def finalize_value():
                for type in weakkey:
                    type = type()
                    if type is not None:
                        incref(type)
                remove_key(weakkey)
        else:
            decref(key)
            weakkey = weakref.ref(key)
            weakref.finalize(key, lambda: remove_key(weakkey))
            finalizers = None
            def finalize_value():
                type = weakkey()
                if type is not None:
                    incref(type)
                remove_key(weakkey)
        weakref.finalize(value, finalize_value)
        return super().__setitem__(weakkey, (value, finalizers))
    
    def get(self, key):
        if isinstance(key, tuple):
            weakkey = tuple(weakref.ref(each) for each in key)
        else:
            weakkey = weakref.ref(key)
        item = super().get(weakkey)
        if item is not None:
            item = item[0]
        return item



class generic: ...
_blank_generic = generic
class generic(_blank_generic):
    @staticmethod
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super(object).__init_subclass__()
        setattr(cls, f'__specialized_types', specialization())
_subclass_generic = generic
class generic(_blank_generic):
    @staticmethod
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super(object).__init_subclass__()
    @classmethod
    def __class_getitem__(cls, *args): ...
_typed_generic = generic


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
        bases = tuple(_subclass_generic if base is generic else base for base in cls.__bases__)
        cls.__bases__ = bases
    
    @classmethod
    def __class_getitem__(cls, typelike) -> type:
        specialized_types: dict[type, type] = getattr(cls, '__specialized_types')
        result = specialized_types.get(typelike)
        if result is None:
            if isinstance(typelike, type):
                inner_name = typelike.__qualname__
                is_multiple = False
            elif isinstance(typelike, tuple):
                inner_name = StringIO()
                length = len(typelike)
                for i, each_type in enumerate(typelike):
                    inner_name.write(each_type.__qualname__)
                    if i != length - 1:
                        inner_name.write(', ')
                inner_name = inner_name.getvalue()
                is_multiple = True
            else:
                raise TypeError("argument(s) in the '[]' should be type(s)")
            typed_generic = deepcopy_class(_typed_generic)
            typed_generic.__bases__ = (cls,)
            class TypedGeneric(typed_generic): ...
            TypedGeneric.__name__ = f'{cls.__name__}[{inner_name}]'
            TypedGeneric.__qualname__ = f'{cls.__qualname__}[{inner_name}]'
            TypedGeneric.__module__ = cls.__module__
            if is_multiple:
                TypedGeneric.__types__ = typelike
            else:
                TypedGeneric.__type__ = typelike
            result = TypedGeneric
            specialized_types[typelike] = result
        return result

_subclass_generic.__bases__ = (generic,)
setattr(generic, f'__specialized_types', specialization())


class dispatcher:
    __slots__ = ('_dispatcher__specialized_types', '_dispatcher__function', '_dispatcher__function_type', '_dispatcher__instance', '_dispatcher__type', '_dispatcher__parameters', '_dispatcher__return_annotation')
    
    def __init__(self, function):
        self.__specialized_types = specialization()
        self.__instance = None
        self.__type = None

        function_type = type(function)
        self.__function_type = function_type
        if issubclass(function_type, staticmethod):
            function = function.__wrapped__
        elif issubclass(function_type, classmethod):
            function = function.__wrapped__
        else:
            function = function
        self.__function = function
        
        signature = inspect.signature(function)
        self.__parameters = list(signature.parameters.values())
        self.__return_annotation = signature.return_annotation
    
    def __get__(self, instance, owner):
        self.__instance = instance
        self.__type = owner
        return self
    
    def __getitem__(self, typelike):
        params = copy(self.__parameters)
        function = self.__function
        def get_final_function(wrapper): return wrapper
        if self.__type is None or issubclass(self.__function_type, staticmethod):
            params.pop(0)
            @wraps(function)
            def wrapper(*args, **kwargs):
                return function(typelike, *args, **kwargs)
        elif issubclass(self.__function_type, classmethod):
            params.pop(1)
            @wraps(function)
            def wrapper(cls, *args, **kwargs):
                return function(cls, typelike, *args, **kwargs)
            def get_final_function(wrapper): return MethodType(wrapper, self.__type)
        else:
            params.pop(1)
            @wraps(function)
            def wrapper(instance, *args, **kwargs):
                return function(instance, typelike, *args, **kwargs)
            if self.__instance is not None:
                def get_final_function(wrapper): return MethodType(wrapper, self.__instance)
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
        function = self.__function
        if self.__type is None or issubclass(self.__function_type, staticmethod):
            return function(None, *args, **kwargs)
        elif issubclass(self.__function_type, classmethod):
            return function(self.__type, None, *args, **kwargs)
        else:
            if self.__instance is None:
                first_arg_name = self.__parameters[0].name
                try:
                    instance = kwargs.pop(first_arg_name)
                    if len(args) > 0:
                        raise TypeError(f"{self.__function.__qualname__}() got multiple values for argument '{first_arg_name}'")
                except KeyError:
                    instance = args[0]
                    args = args[1:]
            else:
                instance = self.__instance
            return function(instance, None, *args, **kwargs)
    
    def __getattribute__(self, name):
        if name == '__name__':
            return self.__function.__name__
        elif name == '__qualname__':
            return self.__function.__qualname__
        elif name == '__module__':
            return self.__function.__module__
        # elif name == '__class__':
        #     if self.__instance is None or issubclass(self.__function_type, staticmethod) or issubclass(self.__function_type, classmethod):
        #         return Callable
        #     else:
        #         return MethodType
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        function = self.__function
        return getattr(function, name)
    
    def __repr__(self):
        function = self.__function
        qualname = function.__qualname__
        params = copy(self.__parameters)
        if self.__type is None:
            typelike = params.pop(0)
        elif issubclass(self.__function_type, staticmethod):
            typelike = params.pop(0)
        # elif issubclass(self.__function_type, classmethod):
        #     typelike = params.pop(1)
        else:
            while True:
                if issubclass(self.__function_type, classmethod):
                    anchor = repr(self.__type)
                elif self.__instance is None:
                    typelike = params.pop(1)
                    break
                else:
                    anchor = f'<{self.__type.__module__}.{self.__type.__name__} object at {hex(id(self.__instance))}>'
                return f"<bound generic template method {qualname} of {anchor}>"
        signature = inspect.Signature(parameters=params, return_annotation=self.__return_annotation)
        return f"<generic template function {function.__module__}.{qualname}[{typelike.name}]{signature}>"
    
    def __instancecheck__(self, obj):
        return self.__subclasscheck__(type(obj))

    def __subclasscheck__(self, cls):
        return issubclass(cls, self.__class__)
    
    def __reduce_ex__(self, protocol):
        function_type = self.__function_type
        if issubclass(function_type, classmethod) or issubclass(function_type, staticmethod):
            function = function_type(self.__function)
        else:
            function = self.__function
        return (type(self), (function,))
    
    # def __getstate__(self):
    #     state = {}
    #     for name in self.__slots__:
    #         state[name] = _get_attribute(self, name)
    #     return state
    
    # def __setstate__(self, state):
    #     for name in self.__slots__:
    #         _set_attribute(self, name, state[name])


# def _get_attribute(obj, name: str):
#     if name.startswith('__'):
#         return obj.__getattribute__(f'_{type(obj).__name__}{name}')
#     else:
#         return obj.__getattribute__(name)


# def _set_attribute(obj, name: str, value):
#     if name.startswith('__'):
#         return obj.__setattr__(f'_{type(obj).__name__}{name}', value)
#     else:
#         return obj.__setattr__(name, value)