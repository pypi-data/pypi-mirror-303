import warnings
from enum import IntEnum
from ._convert_meta import Converter, G_Symbol_UNSET
from ._int_exts import pretty_int2str, uint_from_str


def parse_int(value, default_value=0, default_base=10, **kwargs):
    if isinstance(value, (int, float, bool)):
        return int(value)
    elif value is None:
        return default_value
    elif value is G_Symbol_UNSET:
        return default_value
    elif isinstance(value, str):
        sign = value[0]
        if sign == "+":
            vstr = value[1:]
        elif sign == "-":
            vstr = value[1:]
        else:
            sign = '+'
            vstr = value
        ##; update@202404: 支持使用自定义的扩张进制符
        vnum = uint_from_str(
            vstr,
            default_value=default_value,
            default_base=default_base, **kwargs
        )
        if sign == '-':
            return 0 - vnum
        else:
            return vnum
    else:
        ##;如果异常就直接抛出
        return int(value)


def HexString(value, width=-1, default_value=0, ignore_error=True):
    ##; HexString(16, width=6)  == '0x000010'
    v = parse_int(value, default_value=default_value, ignore_error=ignore_error)
    ##; s = "0x{:04X}".format(self.tp_id_first)
    if width > 0:
        fmt = f"0x{{:0{width}X}}"
        v2 = fmt.format(v)
    else:
        v2 = hex(v)
    return v2


class FloatFmt(Converter, float):
    _type = float

    @classmethod
    def convert(cls, v, **kwargs):
        ##;  float("-1e1")
        ##;  -10.0
        return float(v)


class BoolIntFmt(Converter, int):
    _type = int

    ##; 设定：把bool值转为三种状态：明确的 True(1), False(0), Unset(None)
    default_null = None
    default_values_map = {
        "": default_null,
        "null": default_null,
        "none": default_null,
        "false": 0,
        "0": 0,
        "no": 0,
        "n": 0,
        "f": 0,
    }

    @classmethod
    def convert(cls, value=None, **kwargs):
        if isinstance(value, str):
            v = value.strip().lower()
            return cls.default_values_map.get(v, 1)
        elif value is None:
            return cls.default_null
        elif isinstance(value, int):
            return value
        else:
            vb = bool(value)
            v = 1 if vb else 0
            return v


class IntegerFmt(Converter, int):
    _type = int
    default_base = 10

    @classmethod
    def stringify(cls, value: int, base=default_base,
                  zfill_width=-1, **kwargs
                  ):
        v = pretty_int2str(
            value, base=base,
            zfill_width=zfill_width, **kwargs
        )
        return v

    @classmethod
    def convert(cls, value, default_value=0, **kwargs):
        default_base = kwargs.pop("default_base", cls.default_base)
        return parse_int(value, default_value=default_value, default_base=default_base, **kwargs)
