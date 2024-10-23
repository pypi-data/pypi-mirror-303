# from . import form_data

from enum import IntEnum
from collections import OrderedDict
from ._common import brief_object


class KeyNoteMeta(type):
    def __getattribute__(self, item):
        m = super().__getattribute__(item)
        if isinstance(item, str) and item.startswith('_'):
            return m
        elif isinstance(m, str) and m.startswith(self._annotate_):
            return item
        return m


class KeyNote(metaclass=KeyNoteMeta):
    """
    Use key as value, and use value to note for usage.
    No more stupid enums like `mode="mode"`, and always singleton.

    >>> KeyNote.usage == "usage" # True
    >>> KeyNote._usage_ != "_usage_"
    >>> object.__getattribute__(KeyNote, "usage") == KeyNote._usage_
    >>> m = KeyNote()
    >>> assert m._usage_ == m.usage == object.__getattribute__(m, "usage")
    """
    _annotate_ = '#'
    _cache_data = None  # type: dict
    _usage_ = "{} {{K:V}} => {{key:note(以{}为前缀备注)}}".format(_annotate_, _annotate_)
    usage = _usage_  # type: str

    def __getattribute__(self, item):
        """
        :param item: name of attribute / function
        since the value is mocked , use `vars()` to raw {K:V}
        """
        m = super().__getattribute__(item)
        if isinstance(item, str) and item.startswith('_'):
            return m
        elif isinstance(m, str) and m.startswith(self._annotate_):
            return item
        return m

    @classmethod
    def to_dict(cls):
        ## {enum_field: enum_field_or_value}
        if not cls._cache_data:
            cls._cache_data = brief_object(cls)
        return cls._cache_data

    @classmethod
    def raw_dict(cls):
        ## {enum_field: #NOTE}
        d = {}
        for k, v in vars(cls).items():
            if not k.startswith('_'):
                d[k] = v
        return d


class CoEnumBase():
    """
    custom Enum, instead of `from enum import Enum`
    usage: select options on webpage  
    - updated@2021-08-19 Nico, 
    """
    # __field_name__ = __qualname__ or ""
    __field_key = ''  ## str: 枚举项的项名, 比如国家，语言等
    __field_options = OrderedDict()
    __cache_dmap = None  # type: dict
    __cache_values = None  # type: list
    _DEFAULT = None

    @classmethod
    def field_key(cls):
        if not cls.__field_key:
            cls.__field_key = cls.__name__.rsplit("Enum", 1)[0]
        return cls.__field_key

    @classmethod
    def get_attr_map(cls, force_reload=False):
        # vars(cls) 包括内置属性
        if not cls.__cache_dmap or force_reload:
            cls.__cache_dmap = brief_object(cls, ordered=True)
        return cls.__cache_dmap

    @classmethod
    def list_options(cls, as_dict=True, order_asc=None):
        if not cls.__cache_values:
            m = cls.get_attr_map()
            vs = m.values()
            if order_asc is None:
                vs = list(vs)
            else:
                vs = sorted(vs, reverse=not (order_asc))
            cls.__cache_values = vs
        if as_dict and callable(getattr(cls, "to_dict", None)):
            return [v.to_dict() for v in cls.__cache_values]
        else:
            return cls.__cache_values

    @classmethod
    def opt_vk(cls, vk, ignore_case=True, default=None):
        """
        case insensitive for key-value
        :param vk:  field/value of option
        :param default: optional value of this CoEnum
        :return: OptionEntity or None(default)
        """
        mp = cls.get_attr_map()
        if isinstance(vk, str):
            value = mp.get(vk)
            if value is not None:
                return value

            if vk.startswith("_"):
                return default

        for k, v in mp.items():
            if v == vk:
                return v
            elif k == vk:
                return v
            elif ignore_case and str(k).lower() == str(vk).lower():
                return v
        return default

    @classmethod
    def opt_enum(cls, vk, ignore_case=True, default=None):
        return cls.opt_vk(vk, ignore_case=ignore_case, default=default)

    @classmethod
    def reform(cls, form: dict, nullable=True, **kwargs):
        ##; 从表单中获取枚举项的值，如果项值有效（不为None)，则修改表单 
        ##; nullable 指的是返回可为 None, 但不修改 form[key]=None
        default = kwargs.get("default", cls._DEFAULT)
        key = kwargs.get("key", cls.field_key())
        v = form.pop(key, None)
        if v is not None:
            vk = cls.opt_enum(v)
        elif not nullable:
            vk = default
        else:
            vk = None
        if vk is not None:
            form[key] = vk
        return vk


    @classmethod
    def description(cls, verbose=True):
        name = cls.__name__
        if verbose:
            m = cls.get_attr_map()
            vs = [f"{k}={v}" for k, v in m.items()]
            desc = ', '.join(vs)
            return f"<{name}>: {desc} "
        else:
            vs = list(cls.list_options(as_dict=True))
            return f"<{name}>: {vs} "


    def __str__(self):
        return self.description(verbose=False)


class CoEnum(CoEnumBase, IntEnum):
    def __new__(cls, value: int, phrase="", description=""):
        if isinstance(value, int):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj.phrase = phrase
            obj.description = description
            # cls.__field_options[phrase] = obj
            return obj
        return value

    def to_dict(self):
        return dict(
            name=self.name,
            value=self.value,
            phrase=self.phrase,
            description=self.description,
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other._value_ == self._value_
        elif isinstance(other, self._value_.__class__):
            return other == self._value_
        elif isinstance(other, self.phrase.__class__):
            return other == self.phrase
        elif other and isinstance(other, (tuple, list)):
            return other[0] == self._value_

    def __str__(self):
        return f"[{self.name}:{self.value}] {self.phrase} - {self.description} "

    def __repr__(self):
        return f"[{self.name}:{self.value}]"

    @classmethod
    def list_options(cls, as_dict=True, order_asc=True):
        return super(CoEnum, cls).list_options(as_dict=as_dict, order_asc=order_asc)
    
