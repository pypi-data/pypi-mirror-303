import os


def make_func_to_filter_string_of_OR(
    prefix="", suffix="",
    contains="", exclude="",
    ignore_case=True
):
    if prefix + suffix + contains + exclude == "":
        return lambda x: True

    def _valid_str(vstr: str):
        _ig = lambda x: x
        if ignore_case:
            vstr = vstr.lower()
            _ig = lambda x: x.lower()
        if prefix and vstr.startswith(_ig(prefix)):
            return True
        if suffix and vstr.endswith(_ig(prefix)):
            return True
        if exclude and vstr.find(_ig(exclude)) == -1:
            return True
        if contains and vstr.find(_ig(contains)) > 0:
            return True
        return False

    return _valid_str


def make_func_to_filter_string_of_AND(
    prefix="", suffix="",
    contains="", exclude="",
    ignore_case=True
):
    if prefix + suffix + contains + exclude == "":
        return lambda x: True

    def _valid_str(vstr: str):
        _ig = lambda x: x
        if ignore_case:
            vstr = vstr.lower()
            _ig = lambda x: x.lower()

        is_ok = bool(vstr)
        if is_ok and prefix and not vstr.startswith(_ig(prefix)):
            is_ok = False
        if is_ok and suffix and not vstr.endswith(_ig(suffix)):
            is_ok = False
        if is_ok and contains and vstr.find(_ig(contains)) == -1:
            is_ok = False
        if is_ok and exclude and vstr.find(_ig(exclude)) > -1:
            is_ok = False
        return is_ok

    return _valid_str


def _gen_file_from_dir(
    pardir, prefix="", suffix="",
    contains="", exclude="", ignore_case=True
):
    _chk = make_func_to_filter_string_of_AND(
        prefix=prefix, suffix=suffix,
        contains=contains, exclude=exclude,
        ignore_case=ignore_case,
    )
    for root, dirs, files in os.walk(pardir):
        for filename in files:  # type: str
            if _chk(filename):
                yield root, filename, os.path.join(root, filename)


def list_file_from_dir(
    pardir, prefix="", suffix="",
    contains="", exclude="", ignore_case=True
):
    gen_ = map(
        lambda x: x[-1],
        _gen_file_from_dir(
            pardir, prefix=prefix, suffix=suffix,
            contains=contains, exclude=exclude,
            ignore_case=ignore_case
        )
    )
    return list(gen_)
