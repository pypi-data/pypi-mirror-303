from ._common import G_Symbol_UNSET


class CoFunc():
    def __init__(self, func, *args, _mocked_return=G_Symbol_UNSET, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._mocked_return = _mocked_return

    @property
    def mocked_return(self):
        return self._mocked_return

    @mocked_return.setter
    def mocked_return(self, value):
        self._mocked_return = value

    def fork(self, **kwargs):
        kws = dict(self._kwargs, **kwargs)
        return self.__class__(
            self._func,
            self._args, _mocked_return=self._mocked_return, **kws
        )

    def __call__(self):
        return self._func(*self._args, **self._kwargs)
