"""
##; 扩展 Python 内置的 int(v:str, base)
##; 内置只支持 base < 36, 字母不区分大小写
##; 扩展后，可以支持 base<=64, 字母支持区分大小写
 
python -W{option} script.py
-Wdefault  # Warn once per call location
-Werror    # Convert to exceptions
-Walways   # Warn every time
-Wmodule   # Warn once per calling module
-Wonce     # Warn once per Python process
-Wignore   # Never warn
"""
import math
import string
import warnings
from pprint import pformat


STD_BASE64_V1 = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
STD_BASE64_V2 = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_"
##; -_  可以兼容 URI， 所以默认使用v2
STD_BASE64 = STD_BASE64_V2
DEFAUTL_BASE64 = STD_BASE64_V2

STD_BASE_PREFIX_MAP = {
    "10": "",
    "2": "0b",
    "8": "0o",
    "16": "0x",
}
EXT_BASE_PREFIX_MAP = {
    "36": "0+",
    "62": "0#",
    "64": "0@",
}
DEF_BASE_PREFIX_MAP = dict(STD_BASE_PREFIX_MAP, **EXT_BASE_PREFIX_MAP)

STD_PREFIX_BASE_MAP = {
    "0b": 2,
    "0B": 2,
    "0o": 8,
    "0O": 8,
    "0x": 16,
    "0X": 16,
}

###; 注意，以下用到的字符，都是 URL 不安全的
EXT_PREFIX_BASE_MAP = {
    "0+": 36,  ##; default, 36进制自定义的前缀:[0-10]+[a/A-z/Z] 不区分大小写
    "0#": 62,  ##; default, 62进制自定义的前缀:[0-10]+[az]+[AZ] 区分大小写
    "0|": 36,  ##; extent, 36进制自定义的前缀:[0-10]+[a/A-z/Z] 不区分大小写
    "0&": 62,  ##; extent, 62进制自定义的前缀:[0-10]+[az]+[AZ] 区分大小写
    "0@": 64,  ##; extent, 64进制自定义的前缀:[0-10]+[az]+[AZ]+[-_] 区分大小写, 注意，不同于 BASE64
}
DEF_PREFIX_BASE_MAP = dict(STD_PREFIX_BASE_MAP, **EXT_BASE_PREFIX_MAP)

##; 统一: 数值+大写+小写，和 ascii 顺序一致，及标准 python int 的内置 36 进制一致
##; 注意，一般不建议使用base64，base64的用途主要是"二进制数据(文件内容)转可读字符串"
##; 且标准的base64(大写+小写+数字+/“_-”或“._”变种过多，不做适配）
##; 在URL安全的Base64编码中，加号（+）和斜杠（/）分别被替换为连字符（-）和下划线（_）
DEF_INTSTR_CHARSETS = string.digits + string.ascii_uppercase + string.ascii_lowercase + "._"
DEF_INTSTR_CHAR_MAP = dict((c, v) for v, c in enumerate(DEF_INTSTR_CHARSETS))

##; 数字和字母容易混的有: l(1),o(0),s(5),z(2),b(6),g(9)
EXT_INTSTR_FUZZY_CASE = 'loszgb'
EXT_ILLEGAL_URL_CHARS = [
    (";", "参数分隔符"),
    ("/", "路径分隔符"),
    ("?", "查询字符串开始"),
    (":", "资源和端口之间的分隔符"),
    ("#", "在URL中用于锚点"),
    ("@", "用户名和密码分隔符"),
    ("&", "查询字符串中的参数分隔符"),
    ("=", "查询字符串中的键值对分隔符"),
    ("+", "空格的编码（在查询字符串中）"),
    ("$", "在某些上下文中用作分隔符"),
    (",", "在某些上下文中用作分隔符"),
]


def str2int(vstr: str, base: int, charsets=None, **kwargs):
    # charsets = kwargs.get("charsets", EXT_INTSTR_CHARSETS)
    if isinstance(charsets, str):
        char_map = dict((c, v) for v, c in enumerate(charsets))
    else:
        char_map = kwargs.get("char_map", DEF_INTSTR_CHAR_MAP)
    num = 0
    for i, char in enumerate(vstr):
        v = char_map.get(char, None)
        if v is None or v >= base:
            raise Exception(f"invalid $base({base}), with $vstr[{i}]={char}({v})")
        else:
            num = num * base + v
    return num


def int2str(vnum: int, base: int, charsets=DEF_INTSTR_CHARSETS):
    """
    @base: int: [2, 62], base <=2 and base >=62
    @return: str
    ##; return ''.join(
    #     [charsets[(vnum // base ** i) % base]
    #      for i in range(int(math.log(vnum, base)), -1, -1)]
    # )
    """
    max_b = len(charsets)
    if base > max_b or base < 2:
        raise ValueError(
            f"int2str(): $base must be ranged in [2, {max_b}]"
            f",$charsets={charsets}"
        )

    # if base == 10:
    #     return str(int(vnum))
    # elif base == 2:
    #     return bin(vnum)[2:]
    # elif base == 8:
    #     return oct(vnum)[2:]
    # elif base == 16:
    #     return hex(vnum)[2:]

    result = []
    num = int(vnum)
    while num > 0:
        num, remainder = divmod(num, base)
        result.append(charsets[remainder])
    return ''.join(reversed(result))


def pretty_int2str(vnum: int, base=10, zfill_width=-1,
                   charsets=DEF_INTSTR_CHARSETS, **kwargs
                   ):
    if base == 10:
        t = str(vnum)
        return t.zfill(zfill_width)

    t = int2str(vnum, base, charsets=charsets)
    prefix_map = kwargs.get("prefix_map", DEF_BASE_PREFIX_MAP)
    prefix = prefix_map.get(str(base), None)
    if prefix is None:
        raise ValueError(
            f"Invald $base={base}, expected $prefix_map={pformat(prefix_map)}"
        )
    return f"{prefix}{t.zfill(zfill_width)}"


def uint_from_str(
    vstr: str, default_base: int = 10,
    default_value=0, charsets=DEF_INTSTR_CHARSETS, **kwargs
):
    ##; NOTE: 只支持无符号的整形数值，不支持浮点数
    if not vstr:
        return default_value

    max_b = len(charsets)
    if default_base > max_b:
        raise ValueError(
            f"Invalid $default_base=({default_base}), it must be ranged in [2, {max_b}]"
            f", or <= 0(default=10, -1 is depends on $vstr.prefix), $charsets={charsets}"
        )

    prefix_map = kwargs.get("prefix_map", DEF_PREFIX_BASE_MAP)  # type: dict
    p = vstr[:2]
    base = prefix_map.get(p, None)
    char_map = dict((c, v) for v, c in enumerate(charsets))
    if base is None:
        if p.isdigit() and default_base <= 36:
            return int(vstr, default_base)
        elif default_base > 2:
            return str2int(vstr, default_base, char_map=char_map)
        else:
            raise ValueError(
                f"Invalid $default_base={default_base}, $vstr.prefix={p},\n"
                f"Expected $prefix_map=({pformat(prefix_map)})"
                f",$vstr.size=len({vstr}({vstr[:20]})"
            )
    else:
        if default_base > 2 and default_base != base:
            warnings.warn(f"check $base={base}({p}), but$default_base={default_base}")
        return str2int(vstr[2:], base, char_map=char_map)
