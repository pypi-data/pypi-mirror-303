from ._common import CommonException, G_Symbol_UNSET


class ConverterMeta(type):
    ##; converter 主要关心的是把字符串转为目标类型
    _co_registered_cmap = {}
    _co_registered_class = []

    def __init__(rcls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        rcls._co_metatype = ConverterMeta
        _type = getattr(rcls, "_type", None)
        if _type is None:
            rcls._type = rcls
        ConverterMeta._co_registered_cmap[_type] = rcls
        ConverterMeta._co_registered_class.append(rcls)


    @property
    def _list_cousin_class(cls):
        return cls._co_registered_class

    def __instancecheck__(self, instance):
        return isinstance(instance, self._type)


class Converter(metaclass=ConverterMeta):
    """
    #;; 实现效果如下: 
    >>> a = Converter(1)
    >>> assert isinstance(a, Converter)
    >>> assert isinstance(a, str)
    """
    _type = str

    @property
    def __class__(self):
        return self._type


    @classmethod
    def convert(cls, v, **kwargs):
        ##; 只需要重构此函数, 反序列化（Deserialization） 
        return cls._type(v)

    @classmethod
    def stringify(cls, type_instance: _type):
        ##; 序列化（Serialization）
        return str(type_instance)
    
    def __new__(cls, v=None, **kwargs):
        self = cls.convert(v, **kwargs)
        return self

    @classmethod
    def _adapt_dict(cls, origin_dict: dict, flex_dict: dict, nullable=False):
        updated_kws = {}
        for k, v in flex_dict.items():
            if v is None and not nullable:
                continue
            v0 = origin_dict.get(k, G_Symbol_UNSET)
            if v != v0:
                origin_dict[k] = v
                updated_kws[k] = (v0, v)
        return updated_kws


def find_converter(obj):
    tp = type(obj)
    cvt = ConverterMeta._co_registered_cmap.get(tp, G_Symbol_UNSET)
    if cvt is not G_Symbol_UNSET:
        return cvt
    else:
        for x in ConverterMeta._co_registered_class:  # type:Converter
            if isinstance(obj, x._type):
                return x
