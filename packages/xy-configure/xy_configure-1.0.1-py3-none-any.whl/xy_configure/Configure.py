# -*- coding: UTF-8 -*-
__author__ = "helios"
"""
  * @File    :   Configure.py
  * @Time    :   2023/04/22 18:33:40
  * @Author  :   helios 
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

__doc__ = "配置类"

import logging
from multiprocessing import Value
import os
import json
from pathlib import Path
from types import NoneType
from typing import Any

from .Pair.Section import Section
from .Format.ConfigFormat import ConfigFormat


class Configure(dict):
    strict: bool = True

    config_format: ConfigFormat = ConfigFormat.AUTO

    config_file_path: Path

    # 拥有Section对象和Option对象的存储映射，动态更新
    _config: dict[str, Section] = {}

    # 配置文件中的配置, 静态
    _raw_config: dict = {}

    # 配置文件中的文本
    _raw_config_string: str = ""

    # 配置文件中的文本列表
    _raw_config_string_list: list = []

    def __init__(self):
        pass

    def load_dict(
        self,
        config: dict,
        a_config_format: str | int = "auto",
        strict: bool = True,
    ):
        if (
            not config
            or not isinstance(config, dict)
            or not issubclass(type(config), dict)
        ):
            raise ValueError("请传入相应格式字符串类型的配置文本")
        if a_config_format is None:
            self.config_format = ConfigFormat.parse("auto")
        else:
            self.config_format = ConfigFormat.parse(a_config_format)
        self.strict = strict
        self._raw_config = config
        try:
            self._raw_config_string = json.dumps(self._raw_config)
            self._raw_config_string_list = self._raw_config_string.split("\n")
        except:
            raise ValueError("请传入符合json规范的配置")
        self._load_config()

    def loads(
        self,
        config_string: str,
        a_config_format: str | int = "auto",
        strict: bool = True,
    ):
        if (
            not config_string
            or not isinstance(config_string, str)
            or not issubclass(type(config_string), str)
        ):
            raise ValueError("请传入相应格式字符串类型的配置文本")
        if a_config_format is None:
            self.config_format = ConfigFormat.parse("auto")
        else:
            self.config_format = ConfigFormat.parse(a_config_format)
        self.strict = strict
        self._raw_config_string = config_string
        self._raw_config_string_list = config_string.split("\n")
        raw_config = None
        try:
            raw_config = json.loads(config_string)
        except:
            raise ValueError("请传入符合json规范的配置文本")
        if isinstance(raw_config, dict):
            self._raw_config = raw_config
        self._load_config()

    def load(
        self,
        config_file_path: Path,
        a_config_format: str | int = "auto",
        strict: bool = True,
    ):
        if not Configure.check_config_file_path(config_file_path=config_file_path):
            raise ValueError(f"请传入正确的配置文件路径参数: {config_file_path}")

        if Configure.validate_config_file(config_file_path):
            if isinstance(config_file_path, str):
                config_file_path = Path(config_file_path)
            self.config_file_path = config_file_path
            if a_config_format is None:
                self.config_format = ConfigFormat.parse("auto")
            else:
                self.config_format = ConfigFormat.parse(a_config_format)
            self.strict = strict
            self._raw_config_string = self.config_format.load_as_string(
                self.config_file_path
            )
            self._raw_config_string_list = self.config_format.load_as_lines(
                self.config_file_path
            )
            raw_config = self.config_format.load(self.config_file_path)
            if isinstance(raw_config, dict):
                self._raw_config = raw_config
            self._load_config()
        else:
            raise PermissionError(f"操作配置文件({config_file_path})失败!")

    def register_section(self, section: Section | None, exist_ok=True) -> bool:
        if isinstance(section, NoneType) or not section.get_name():
            return False

        if section:
            section_name = section.get_name()
            if section_name:
                has_section = self.has_section(section_name)
                if has_section and not exist_ok:
                    return False
                exist_section: Section | dict | None = self._raw_config.get(
                    section_name
                )
                section_cache = {}
                section_cache.update(section)
                if exist_section:
                    try:
                        section_cache.update(exist_section)
                    except:
                        pass
                section.reload(
                    section_cache,
                    self._raw_config_string,
                    json.dumps(section),
                    self._raw_config_string_list,
                    self.config_format,
                )
                if exist_section:
                    for name in exist_section:
                        value = exist_section.get(name)
                        section.set_value(name, value)
                self.set_section(section=section, exist_ok=exist_ok)
                return True
        else:
            return False

    def _load_config(self):
        if not self._raw_config:
            raise ValueError(
                "配置加载失败，请正确使用配置文件的格式，当前支持(toml, ini, json, xml)格式, 并且文件必须非空"
            )
        else:
            for section_name in self._raw_config:
                section_dict = self._raw_config.get(section_name)
                if not isinstance(section_dict, dict):
                    section_dict = {}
                section = Section(
                    section_dict,
                    self._raw_config_string,
                    json.dumps(section_dict),
                    self._raw_config_string_list,
                    self.config_format,
                )
                section.set_name(section_name)
                self.set_section(section)

    @staticmethod
    def check_config_file_path(config_file_path: Path | str | None) -> bool:
        if not config_file_path:
            return False

        if not isinstance(config_file_path, Path) and not isinstance(
            config_file_path, str
        ):
            return False

        return True

    @staticmethod
    def validate_config_file(config_file_path: Path | str) -> bool:
        if isinstance(config_file_path, str):
            config_file_path = Path(config_file_path)

        if not config_file_path or not config_file_path.exists():
            raise FileNotFoundError(f"配置文件({config_file_path})不存在!")

        if not os.access(config_file_path, os.R_OK):
            raise PermissionError(f"配置文件({config_file_path})无法访问, 对该文件没有读取权限")

        return True

    def get_section(
        self, section_name: str, default: Section | None = None
    ) -> Section | None:
        section = self.get(section_name)
        if (
            not section
            or not isinstance(section, Section)
            or not issubclass(type(section), Section)
        ):
            section = default
        return section

    def set_section(self, section: Section, exist_ok: bool = False) -> bool:
        if not isinstance(section, Section) and not issubclass(type(section), Section):
            return False

        has_section = self.has_section(section.get_name())
        if has_section and not exist_ok:
            return False

        if section:
            if has_section:
                self.update({section.get_name(): section})
            else:
                self.setdefault(section.get_name(), section)
            return True
        return False

    def del_section(self, section_name: str) -> bool:
        has_section = self.has_section(section_name)
        if has_section:
            try:
                del self[section_name]
                return True
            except Exception as exception:
                logging.error(exception)
                return False

        return False

    def get_value(
        self,
        section_name: str,
        option: str,
        value_type: type | None = None,
        default=None,
    ) -> Any:
        section: Section | None = self.get_section(section_name, default=default)
        if section:
            return section.value(option, value_type=value_type, default=default)
        return None

    def getstr(self, section_name: str, option: str, default=None) -> str | None:
        return self.get_value(
            section_name=section_name, option=option, value_type=str, default=default
        )

    def getdict(self, section_name: str, option: str, default=None) -> dict | None:
        return self.get_value(
            section_name=section_name, option=option, value_type=dict, default=default
        )

    def getlist(self, section_name: str, option: str, default=None) -> list | None:
        return self.get_value(
            section_name=section_name, option=option, value_type=list, default=default
        )

    def getboolean(self, section_name: str, option: str, default=None) -> bool | None:
        return self.get_value(
            section_name=section_name, option=option, value_type=bool, default=default
        )

    def getint(self, section_name: str, option: str, default=None) -> int | None:
        return self.get_value(
            section_name=section_name, option=option, value_type=int, default=default
        )

    def getfloat(self, section_name: str, option: str, default=None) -> float | None:
        return self.get_value(
            section_name=section_name, option=option, value_type=float, default=default
        )

    def has_section(self, section_name: str | None) -> bool:
        if not section_name:
            return False
        exist_section: Section | None = self.get_section(section_name)
        if exist_section:
            return True
        return False

    def has_option(self, section_name: str, option_name: str) -> bool:
        section = self.get_section(section_name)
        if section:
            return section.exists(option_name)
        return False

    def set_value(self, section_name: str, option_name: str, value) -> bool:
        section = self.get_section(section_name)
        if section:
            section.set_value(option_name, value)
            return True
        return False

    def dumps(self):
        self.config_format.dumps(self.config_file_path, json.dumps(self))
