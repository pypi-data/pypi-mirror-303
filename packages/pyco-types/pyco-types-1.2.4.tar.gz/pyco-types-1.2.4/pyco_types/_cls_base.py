from __future__ import absolute_import

from typing import List
from collections import namedtuple

python_obj_attrs = dir(object())


def super_inherit(self, args: tuple, kwargs: dict, ori_cls, baseClasses):
    for base_class in baseClasses:
        if hasattr(base_class, "__init__"):
            # print("base_cls", base_class)
            base_class.__init__(self, *args, **kwargs)
    if hasattr(ori_cls, "__init__"):
        # print("ori_cls", ori_cls)
        ori_cls.__init__(self, *args, **kwargs)


def create_class(ori_cls, *baseClasses, class_name=None):
    """
    @DecoExtKwsClass
    class MyClass():
        pass    
    """
    # base_class = CoExtBase
    if not class_name:
        class_name = f'PycoWrapped.{ori_cls.__name__}'

    WrappedClass = type(
        class_name, (ori_cls, *baseClasses),
        {
            '__init__': lambda self, *args, **kwargs: super_inherit(
                self, args, kwargs, ori_cls, baseClasses
            )
        }
    )

    return WrappedClass


def add_base_class(*baseClasses, class_name=None):
    def _deco(cls):
        """
        @add_base_class(baseCls1,BaseCls2)
        class MyClass():
            pass    
        """
        new_cls = create_class(cls, baseClasses, class_name=class_name)
        return new_cls

    return _deco


def wrapped_class(*BaseClass):
    """
    @wrap_base_class(BaseClass)
    class ParentClass():
        def __init__(self, *args, **kwargs):
            print("ParentClass __init__ called")
            
    new_cls = wrap_base_class(BaseClass)(OriClass)  #type: WrappedClass
    """

    def decorator(cls):
        class WrappedClass(cls, *BaseClass):
            def __init__(self, *args, **kwargs):
                super_inherit(self, args, kwargs, cls, BaseClass)
                self._inited_args = args
                self._inited_kwargs = kwargs

        return WrappedClass

    return decorator
