import logging
import os
import sys
from types import FunctionType, MethodType

from ._common import CommonException, G_Symbol_UNSET


class CoExtBase():
    ##; ERROR: for dict

    def __new__(cls, *args, _args=None, _extra_kws=None, **kwargs):
        self = super().__new__(cls)
        self._kwargs = kwargs

        if args and _args and (_args != args):
            raise CommonException(f"[{cls.__name__}] initial with conflict *args({args}) and _args({_args})")
        elif _args:
            self._args = _args
        else:
            self._args = args

        if isinstance(_extra_kws, dict):
            self._extra_kws = _extra_kws
        else:
            self._extra_kws = {}

        self.__map_attrs = None
        self.__map_props = None
        self.__map_funcs = None
        self._ext_attr_names = [
            "__dict__",
            "__map_attrs",
            "__map_props",
            "__map_funcs",
            "_CoExtBase__map_attrs",
            "_CoExtBase__map_props",
            "_CoExtBase__map_funcs",
        ]
        return self

    ##; NOTE@NICO(2024-10-12): already set $._args and $._kwargs with $.__new__
    # def __init__(self, *args, _extra_kws=None, **kwargs):
    #     self._args = args
    #     self._kwargs = kwargs
    #     if isinstance(_extra_kws, dict):
    #         self._extra_kws = _extra_kws
    #     else:
    #         self._extra_kws = {}

    def __iter__(self):
        yield from self._args
        yield from self._kwargs.values()

    def __str__(self):
        tp = self.__class__.__name__
        return f"<{tp}:args={self._args},kwargs={self._kwargs}," \
               f"extra_kws={self._extra_kws}>"

    def __call__(self, kwargs: dict):
        self._kwargs.update(kwargs)
        return self

    def __bool__(self):
        return self._args or self._kwargs
        
    def __repr__(self):
        tp = self.__class__.__name__
        # args = (*self._args, f"**{self._kwargs}", f"_extra_kws={self._extra_kws}")
        return f"<{tp}{self._args}({self._kwargs})>"

    if sys.version_info > (3, 6) and os.environ.get("DEBUG", True):
        def __init_subclass__(cls, *args, **kwargs):
            logging.debug(f"[DEBUG]: Initializing class, <{cls.__name__}(CoExtBase)>")
            super().__init_subclass__(**kwargs)


    def _map_attrs(self):
        # ms = getattr(self, "__map_attrs", None)
        ms = self.__map_attrs
        if not ms:
            attrs = dir(self)
            ls = set(attrs) - set(dir(object)) - set(self._ext_attr_names)
            ms = [(k, getattr(self, k, G_Symbol_UNSET)) for k in ls]
            self.__map_attrs = ms
        return ms

    def _map_props(self):
        # ps = getattr(self, "__map_props", None)
        ps = self.__map_props
        if not ps:
            ms = self._map_attrs()
            ps = list(filter(lambda m: not isinstance(m[1], (FunctionType, MethodType)), ms))
            self.__map_props = ps
        return ps

    def _map_funcs(self):
        # ps = getattr(self, "__map_funcs", None)
        ps = self.__map_funcs
        if not ps:
            ms = self._map_attrs()
            ps = list(filter(lambda m: isinstance(m[1], (FunctionType, MethodType)), ms))
            self.__map_funcs = ps
        return ps


    def to_dict(self, verbose=0, **kwargs):
        ##; 注意不要修改 kwargs
        if not verbose:
            return self._kwargs
        seed = dict(
            self._kwargs,
            _args=self._args,
        )
        if isinstance(verbose, int):
            if verbose <= 1:
                return seed
            elif verbose >= 2:
                seed.update(_extra_kws=self._extra_kws)
            elif verbose >= 3:
                seed.update(_struct_=self.__class__.__name__)
        return seed
    
    def __setitem__(self, key, value):
        return self._kwargs.__setitem__(key, value)
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._args[key]
        elif key == "_args":
            return self._args
        v = self._kwargs.get(key, G_Symbol_UNSET)
        if v is G_Symbol_UNSET:
            v = self._extra_kws.get(key, G_Symbol_UNSET)
            if v is G_Symbol_UNSET:
                raise Exception(f"Invalid {type(self)}.$key={key}")
        return v

    def __getattr__(self, item):
        ##; 先调用 __getattribute__，然后因为属性不存再调用 __getattr__
        try:
            return self[item]
        except Exception as e:
            raise CommonException(
                f"<{self.__class__.__name__}>.getattr({item}) failed! ({self})",
                errno=40042,
                origin_data=self,
            )

    def __eq__(self, other):
        if self._args == other._args:
            if self._kwargs == other._kwargs:
                return True
        return False


def DecoExtKwsClass(cls):
    """
    @DecoExtKwsClass
    class MyClass():
        pass    
    """
    base_class = CoExtBase
    class_name = f'PycoWrapped.{cls.__name__}'

    WrappedClass = type(
        class_name, (cls, base_class),
        {
            '__init__':
                lambda self, *args, **kwargs: (
                    base_class.__init__(self, *args, **kwargs)
                    if hasattr(base_class, '__init__'
                               ) else None and cls.__init__(
                        self, *args, **kwargs
                    ) if hasattr(cls, '__init__') else None
                )
        }
    )

    return WrappedClass
