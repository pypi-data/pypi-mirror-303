from ._common import CommonException, G_Symbol_UNSET


class CoDict(dict):
    ##; attr 只能使用 getattr 的方法访问
    _prviate_attr_map = {}  # type: dict
    ##; data 是缺省字段表, 
    _default_data_map = {}  # type: dict
    ##; TODO
    # _symbol_unset_val = G_Symbol_UNSET
    # _x_ignore_error_if_unset_attr = True

    def __init__(
        self,
        _default_data_map=None,
        _prviate_attr_map=None,
        **kwargs
    ):

        super().__init__(**kwargs)
        if isinstance(_default_data_map, dict):
            self._default_data_map = _default_data_map
        if isinstance(_prviate_attr_map, dict):
            self._prviate_attr_map = _prviate_attr_map

    def x_set_attr_map(self, **kwargs):
        self._prviate_attr_map = kwargs

    def x_set_defaults(self, **kwargs):
        self._default_data_map = kwargs

    @property
    def private_attr_map(self):
        ## protected 
        if not isinstance(self._prviate_attr_map, dict):
            self._prviate_attr_map = {}
        return self._prviate_attr_map

    @property
    def default_data_map(self):
        if self._default_data_map is None:
            self._default_data_map = {}
        elif not isinstance(self._default_data_map, dict):
            self._default_data_map = dict(self._default_data_map)
        return self._default_data_map

    def to_dict(self, verbose=0):
        if isinstance(verbose, int):
            if verbose <= 0:
                return self
            elif verbose == 1:
                data = dict(self.default_data_map, **self)
                return data
            elif verbose == 2:
                data = dict(self.default_data_map, **self)
                data.update(self.private_attr_map)
                return data
            elif verbose == 3:
                return dict(
                    _default_data_map=self.default_data_map,
                    _private_attr_map=self._prviate_attr_map,
                    data=self
                )
            else:
                return dict(
                    _default_data_map=self.default_data_map,
                    _private_attr_map=self._prviate_attr_map,
                    **self,
                )
        return dict(self)

    def __getitem__(self, key):
        v = super().get(key, G_Symbol_UNSET)
        if v is G_Symbol_UNSET:
            errno = 0
            if not self.default_data_map:
                errno = 40040
            else:
                v = self.default_data_map.get(key, G_Symbol_UNSET)
                if v is G_Symbol_UNSET:
                    errno = 40041
            if errno:
                raise CommonException(
                    error_msg=f"<CoDict>.getitem({key}) failed! "
                              f"suggest to update with $.x_set_defaults()",
                    errno=errno,
                    _entity=self.to_dict(verbose=3),
                )
        return v

    def __getattr__(self, key):
        ##; 先调用 __getattribute__，然后因为属性不存在调用 __getattr__
        value = self.private_attr_map.get(key, G_Symbol_UNSET)
        if value is not G_Symbol_UNSET:
            return value
        try:
            return self[key]
        except Exception as e:
            raise CommonException(
                f"<CoDict>.getattr({key}) failed! ({self})",
                errno=40042,
                origin_data=self,
            )

    def __setattr__(self, key: str, value):
        ##; 所有的内部属性，必须使用 "_" 作为前缀
        if key.startswith("_"):
            # Assign to the special 'my_attr' property
            super().__setattr__(key, value)
        else:
            self._prviate_attr_map.update({key: value})
            # Set the normal dictionary key-value pair
            self[key] = value

    def __delattr__(self, item: str):
        try:
            ori_val = self._prviate_attr_map.pop(item, G_Symbol_UNSET)
            del self[item]
            return ori_val
        except KeyError:
            raise AttributeError(f"<CoDict>:: delattr({self}), {item}")
