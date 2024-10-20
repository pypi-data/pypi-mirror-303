# -*- coding: UTF-8 -*-
__author__ = "helios"


from .PairDelegate import PairDelegate

from pathlib import Path
from types import NoneType

from xy_configure.Format.ConfigFormat import ConfigFormat

from .Pair import Pair
from .Option import Option


class Section(Pair, metaclass=PairDelegate):
    __options: dict[str, Option] = {}

    def reload(
        self,
        raw_value,
        raw_string: str,
        raw_base_string: str,
        raw_base_string_list: list,
        config_format: ConfigFormat = ConfigFormat.AUTO,
        strict: bool = True,
    ):
        if isinstance(raw_value, dict) or issubclass(type(raw_value), dict):
            for option_name in raw_value:
                value = raw_value.get(option_name)
                option: Option = Option(
                    value,
                    raw_string,
                    raw_base_string,
                    raw_base_string_list,
                    config_format,
                    strict,
                )
                option.set_name(option_name)
                option.delegate = self  # type: ignore
                option.setdefault(option_name, value)
                self.__options.setdefault(option_name, option)
                self.setdefault(option_name, value)
        super().reload(
            raw_value,
            raw_string,
            raw_base_string,
            raw_base_string_list,
            config_format,
            strict,
        )

    def _sync_data(self, name: str, default):
        value = self.value(name, value_type=type(default))
        success = self.set_value(name, default, exist_ok=False)
        if success:
            value = default
        return value

    def _fetch_path(self, name: str, default: Path | None) -> Path | None:
        value = self._sync_data(name, str(default))
        if value and isinstance(value, str):
            return Path(value)
        return default

    def has_option(self, name: str) -> bool:
        return self.get_option(name=name) is not None

    def get_option(self, name: str) -> Option | None:
        option = self.__options.get(name)
        return option

    def set_option(self, option: Option | None, exist_ok: bool = True) -> bool:
        if not option or not option.get_name():
            return False
        option_name: str | None = ""
        if option.get_name():
            option_name = option.get_name()
        exist_option = self.get_option(option_name)  # type: ignore
        if exist_option and not exist_ok:
            return False
        option.delegate = self  # type: ignore
        self.__options.setdefault(option_name, option)  # type: ignore
        return True

    def del_option(self, option: Option | str) -> bool:
        option_name: str = ""
        if isinstance(option, str):
            option_name = option

        if isinstance(option, Option) or issubclass(type(option), Option):
            option_name = option.get_name()  # type: ignore

        exist_option = self.get_option(option_name)
        if exist_option and exist_option.get_name():
            del self.__options[option_name]
            del exist_option
            del option
            return True
        return False

    def set_value(self, name: str | None, value=None, exist_ok: bool = True) -> bool:
        if not name:
            return False
        option: Option | None = self.get_option(name)

        if not option:
            option = Option(
                value,
                self._raw_string,
                self._raw_base_string,
                self._raw_base_string_list,
                self._config_format,
                self.strict,
            )
            option.set_name(name)

        if not isinstance(option, NoneType):
            option.set_value(name, value, exist_ok=exist_ok)
            self.set_option(option=option, exist_ok=exist_ok)

        return super().set_value(name, value, exist_ok)

    def should_delete(self, name, ok: bool = False) -> bool:
        if name in self.keys():
            try:
                del self[name]
            except:
                ok = False
        return ok

    def __delitem__(self, __key) -> None:
        ok = self.del_option(__key)
        if ok:
            return super().__delitem__(__key)
        return None

    def setdefault(self, __key, __default):
        super().setdefault(__key, __default)
        has_option = self.has_option(__key)
        if not has_option:
            self.set_value(__key, __default)

    def update(self, __m):
        if not __m:
            return
        super().update(__m)
        names = self.__options.keys()
        keys = __m.keys()
        for key in keys:
            value = __m.get(key)
            if key in names:
                self.set_value(key, value)
            else:
                option = Option(
                    value,
                    self._raw_string,
                    self._raw_base_string,
                    self._raw_base_string_list,
                    self._config_format,
                    self.strict,
                )
                option.set_name(key)
                option.set_value(key, value)
                self.set_option(option=option)
