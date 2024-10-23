"""
Common code used in multiple modules.
"""
import types
import uuid
import inspect
import datetime
import builtins
from pprint import pformat
from collections import OrderedDict
from types import FunctionType, ModuleType, MethodType


class Symbol:
    __slots__ = ["name", "bool_val", "kwargs"]

    def __init__(self, name=".", bool_val=True, **kwargs):
        self.name = name
        self.bool_val = bool_val
        self.kwargs = kwargs

    def __repr__(self):
        return f"<Symbol({self.name})>"

    def __bool__(self):
        return bool(self.bool_val)

    def __eq__(self, other):
        return id(self) == id(other)


G_Symbol_UNSET = Symbol("UNSET", False)

##; @formatter:on
##; 不可变的简单类型（基本类型)
##; cannot import name 'NoneType' from 'types' !!!
K_Python_Basic_Types = (
    type(None),
    str,
    int,
    bool,
    float,
    bytes,

)
##; 复合类型（或容器类型） 
K_Python_Composite_types = (
    set,
    list,
    dict,
    tuple,  # ; immutable
    complex,  # ; immutable
)

K_Python_Common_Types = (
    *K_Python_Basic_Types,
    *K_Python_Composite_types,

    frozenset,
    bytearray,
    uuid.UUID,
    datetime.datetime,
    datetime.timedelta,
    datetime.date,
)

# K_Python_Object_Attrs = dir(object) 
K_Python_Object_Attrs = [
    '__class__', '__doc__',
    '__hash__', '__init__', '__new__',
    '__init_subclass__', '__subclasshook__',
    '__dir__', '__setattr__', '__delattr__',
    '__getattribute__', '__sizeof__',
    '__reduce__', '__reduce_ex__',
    '__str__', '__repr__', '__format__',
    '__eq__', '__ne__',
    '__ge__', '__gt__',
    '__le__', '__lt__',
]


##; @formatter:off

def list_builin_type_names():
    attr_list = dir(builtins)
    basic_types = [name for name in attr_list if isinstance(getattr(builtins, name), type)]
    return basic_types


def is_ignored_attr(
    k, v,
    nullable=True,
    _ignore_type=True,
    _ignore_function=True,
    _ignore_attr_=True,
    _ignore_module=True,
    _ignore_method=True,
):
    """
    @k: attr_name
    @v: attr_value
    @return: bool: is_ignored
    ;; 可使用 inspect.isfunction|.ismethod 等方法来进一步判断
    """
    ret = False
    if _ignore_attr_ and k.startswith('_'):
        ret = True
    elif _ignore_type and isinstance(v, type):
        ret = True
    elif _ignore_function and isinstance(v, FunctionType):
        ## common function + staticmethod 
        ret = True
    elif _ignore_method and inspect.ismethod(v):
        ## instance_method + classmethod
        ret = True
    elif _ignore_attr_ and isinstance(v, ModuleType):
        ret = True
    if not ret and not nullable:
        if v is None:
            ret = True
    return ret


def trim_dict(origin_dct, nullable=False, verbose=0, ignore_func=None,
              **kws
              ):
    data = dict()
    if ignore_func is None:
        ignore_func = is_ignored_attr
    for k, v in origin_dct.items():
        if v is None:
            if nullable:
                data[k] = v
        elif verbose <= 0:
            if isinstance(v, K_Python_Common_Types):
                data[k] = v
        elif not ignore_func(k, v):
            data[k] = v
    return data


def brief_object(obj, ordered=False, **kwargs):
    data = OrderedDict() if ordered else dict()
    for attr in dir(obj):
        if not attr.startswith('_'):
            value = getattr(obj, attr)
            if not callable(value):
                data[attr] = value
    return data


class CommonException(Exception):
    _description = ""
    errno = 40000
    error_msg = "customized details of error message"

    def __init__(self, error_msg=error_msg, **error_kws):
        self.error_msg = error_msg
        self.errno = error_kws.pop("errno", self.errno)
        self.error_kws = error_kws

    @property
    def description(self):
        if not self._description:
            self._description =f"[errno:{self.errno}]{self.error_msg}"
        return self._description
    
    def to_dict(self):
        ## v3
        return dict(
            errno=self.errno,
            error_msg=self.error_msg,
            error_kws=self.error_kws,
        )

    def __str__(self):
        return self.description
    
    def __repr__(self):
        return f"REPR {self.errno} {self.error_msg}" 