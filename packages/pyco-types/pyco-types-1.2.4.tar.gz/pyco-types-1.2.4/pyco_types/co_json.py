import json
import uuid
# import inspect
import orjson
import logging

from pprint import pformat
from datetime import datetime, date
from ._convert_meta import find_converter, Converter
from ._common import K_Python_Common_Types, CommonException, G_Symbol_UNSET


def pformat_any(data, depth=2, width=80, indent=2, **kwargs):
    return " :: ".join([str(type(data)), pformat(data, indent=indent, width=width, depth=depth)])


def parse_json(data, **kwargs):
    if isinstance(data, str) and data.startswith('"') and data.endswith('"'):
        try:
            # obj = json.loads(data, **kwargs)
            obj = orjson.loads(data)
            return obj
        except:
            ## import json5
            return data
    else:
        return data


class CustomJSONEncoder(json.JSONEncoder):
    """
    default support datetime.datetime and uuid.UUID
    enable convert object by custom `http exception`
    usually:
        "to_json":  Common Class
        "to_dict":  Custom Model
        "as_dict"： SQLAlchemy Rows
        "get_json": json response
        "__html__": jinja templates

    """
    _jsonify_methods = [
        "jsonify",
        "to_json",
        "get_json",  # json response
        "to_dict",
        "as_dict",  # SQLAlchemy Rows
        "__html__",  # jinja templates
        "_asdict",  ## collections, namedtuple 
        "toJson",
        "getJson",  # json response
        "toDict",
        "asDict",  # SQLAlchemy Rows
    ]

    ##； @_jsonify_strict: 如果设置为 True, 则尝试使用原生 JSON, 可能会异常
    ##； @_jsonify_strict: 如果设置为 False, 则不管怎样都能返回 序列化的结果（不一定符合预期）
    _jsonify_strict = False
    _jsonify_logger = logging.getLogger()
    __stringify_map = dict()  # (k:Type, v:Tuple(func, msg))

    @classmethod
    def _get_stringify(cls, obj,
                       with_converter=True,
                       with_methods=True,
                       flag_property=True,
                       **kwargs,
                       ):
        cvt, _ = cls.__stringify_map.get(type(obj), (G_Symbol_UNSET, "_"))
        if cvt is G_Symbol_UNSET:
            if with_converter:
                cvter = find_converter(obj)
                if isinstance(cvter, Converter):
                    ##; stringify with Converter class_method
                    cvt = cvter.stringify
                    cls.register_stringify(type(obj), cvt, f"converter={cvter}")
                    return cvt
            if with_methods:
                for k in cls._jsonify_methods:
                    fn = getattr(obj, k, G_Symbol_UNSET)  ## instance_method
                    if fn is G_Symbol_UNSET:
                        continue
                    elif callable(fn):
                        ##; stringify with instance_method
                        cvt = lambda x, method=k: getattr(x, method)()
                        cls.register_stringify(type(obj), cvt, f"method={k}")
                        break
                    elif isinstance(fn, K_Python_Common_Types) and flag_property:
                        ##; stringify with instance_property
                        cvt = lambda x, property=k: getattr(x, property, G_Symbol_UNSET)
                        cls.register_stringify(type(obj), cvt, f"property={k}")
                        break
        return cvt

    @classmethod
    def register_stringify(cls, otype, str_func, msg="-"):
        cls.__stringify_map[otype] = (str_func, msg)
        cls._jsonify_logger.info(f"[CustomJSONEncoder] register_stringify: ({otype}:{str_func}),{msg}")

    @classmethod
    def serialize(cls, obj, strict=False, **kwargs):
        ##; common types
        cvt = cls._get_stringify(obj, **kwargs)
        if callable(cvt):
            return cvt(obj)
        elif not strict:
            func = kwargs.get("default", pformat_any)
            return func(obj)
        else:
            raise CommonException(
                f"Object({type(obj)}) is not registered with stringify"
                f"\nobj:{obj}",
                errno=50020,
                origin=obj,
                _kwargs=kwargs,
            )

    def default(self, obj):
        return self.serialize(obj, strict=self._jsonify_strict)


CustomJSONEncoder.register_stringify(
    date,
    lambda x: x.strftime('%Y-%m-%d'),
    msg="fmt:'%Y-%m-%d'"
)
CustomJSONEncoder.register_stringify(
    datetime,
    lambda x: x.strftime('%Y-%m-%d %H:%M:%S'),
    msg="fmt:'%Y-%m-%d' %Y-%m-%d %H:%M:%S"
)
CustomJSONEncoder.register_stringify(
    uuid.UUID,
    str,
)


def json_format(data, indent=2, autoflat=True, cls=CustomJSONEncoder, ensure_ascii=False, default=None, **kwargs):
    if isinstance(data, str) and autoflat:
        data = parse_json(data)
    if cls is None:
        return json.dumps(data, indent=indent, default=default)
    return json.dumps(
        data, indent=indent,
        cls=cls, ensure_ascii=ensure_ascii, **kwargs
    )


def json_dumps(data, default=CustomJSONEncoder.serialize):
    return orjson.dumps(
        data,
        default=default,
        option=(
            orjson.OPT_NON_STR_KEYS
            | orjson.OPT_APPEND_NEWLINE
            | orjson.OPT_PASSTHROUGH_DATETIME
            | orjson.OPT_SERIALIZE_UUID
            | orjson.OPT_SERIALIZE_NUMPY
        )
    )  # type: bytes
