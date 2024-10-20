# -*- coding: UTF-8 -*-
__author__ = "helios"

from types import NoneType
from xy_configure.Pair.PairDelegate import PairDelegate
from xy_configure.Format.ConfigFormat import ConfigFormat
from xy_configure.Raw.Raw import Raw
from xy_configure.Raw import parse as raw_parse
import inspect


class Pair(dict):
    _name: str | None = ""

    _config_format: ConfigFormat = ConfigFormat.AUTO

    _raw: Raw = Raw()

    _raw_value = None

    _raw_string: str = ""

    _raw_base_string: str = ""

    _raw_base_string_list: list = []

    delegate: PairDelegate | None = None

    strict: bool = True

    def get_name(self) -> str | None:
        return self._name

    def set_name(self, name):
        self._name = name

    def __init__(
        self,
        raw_value=None,
        raw_string: str = "",
        raw_base_string: str = "",
        raw_base_string_list: list = [],
        config_format: ConfigFormat = ConfigFormat.AUTO,
        strict: bool = True,
    ):
        self.set_name(self.__class__.__name__.upper())
        self.reload(
            raw_value=raw_value,
            raw_string=raw_string,
            raw_base_string=raw_base_string,
            raw_base_string_list=raw_base_string_list,
            config_format=config_format,
            strict=strict,
        )

    def reload(
        self,
        raw_value,
        raw_string: str,
        raw_base_string: str,
        raw_base_string_list: list,
        config_format: ConfigFormat = ConfigFormat.AUTO,
        strict: bool = True,
    ):
        self._raw = raw_parse(
            name=str(self.get_name()),
            raw_value=raw_value,
            raw_string=raw_string,
            raw_base_string=raw_base_string,
            raw_base_string_list=raw_base_string_list,
            config_format=config_format,
            strict=strict,
        )
        self._raw_value = raw_value
        self._raw_string = raw_string
        self._config_format = config_format
        self._raw_base_string = raw_base_string
        self._raw_base_string_list = raw_base_string_list
        if isinstance(self._raw_value, dict):
            self.update(self._raw_value)
        self._load()

    @property
    def value_type(self) -> type:
        return type(self.get(self.get_name()))

    def value(
        self, name: str | None = None, value_type: type | None = None, default=None
    ):
        if not name:
            return None
        value = super().get(name)
        if value_type and isinstance(value, value_type):
            return value

        if isinstance(value_type, type) and callable(value_type):
            sig = inspect.signature(value_type.__init__)
            params = sig.parameters
            if value and len(params) > 1:
                try:
                    value = value_type(value)
                except:
                    pass
            else:
                pass
        else:
            if default:
                value = default

        return value

    def set_value(self, name: str | None, value=None, exist_ok: bool = True) -> bool:
        ok = False
        exists = False
        if name:
            exists = self.exists(name)
        if name:
            if exists is True:
                if exist_ok is True:
                    super().update({name: value})
                    ok = True
            else:
                super().setdefault(name, value)
                ok = True
        if self.delegate and hasattr(self.delegate, "should_set_value"):
            ok = self.delegate.should_set_value(name, value, exist_ok, ok)
        return ok

    def exists(self, name: str) -> bool:
        """
        判断传入名称对应的值是否存在

        _extended_summary_

        Args:
            name (str): 要判断的值对应的名称

        Returns:
            bool: 是否存在
        """
        exists = name in self.keys() and not isinstance(self.get(name), NoneType)
        return exists

    def __delitem__(self, __key) -> None:
        value = self.get(__key)
        if not value:
            return None
        ok = not isinstance(value, NoneType)
        if self.delegate:
            ok = self.delegate.should_delete(__key, ok)
        try:
            if ok:
                super().__delitem__(__key)
                return value
        except:
            return None
        return None

    def _load(self):
        pass
