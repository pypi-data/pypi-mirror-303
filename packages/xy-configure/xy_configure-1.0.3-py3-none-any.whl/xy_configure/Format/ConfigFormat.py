# -*- coding: UTF-8 -*-
__author__ = "helios"

from pathlib import Path
import tomllib
from enum import IntEnum
import json

from xy_file.File import File
from xy_configure.configparser.ConfigParser import ConfigParser


class ConfigFormat(IntEnum):
    """
    配置文件读取格式

    不支持py文件配置是由于担心动态注入

    Args:
        IntEnum (_type_): 父类

    Returns:
        _type_: 类型
    """

    AUTO = 0  # 根据文件名后缀读取， 若后缀不匹配， 则按顺序读取
    TOML = 1  # 默认读取配置格式
    INI = 2  # 包括ini和通常使用大部分的cfg格式
    JSON = 3  # 不支持注释，要求格式严格
    XML = 4  # 不支持注释

    @classmethod
    def parse(cls, config_format: str | int | None):
        if not config_format:
            return ConfigFormat(0)

        names = [member for member in cls if member.name.upper() == config_format]
        if not names and len(names) > 0:
            return names[0]

        values = [member for member in cls if member.value == config_format]
        if not values and len(values) > 0:
            return values[0]

        return ConfigFormat(0)

    ###############################  ##########################################

    def loads(self, config_string: str) -> dict | None:
        config = None
        match self:
            case ConfigFormat.TOML:
                config = ConfigFormat.load_toml_config(config_string)
            case ConfigFormat.INI:
                config = ConfigFormat.load_ini_config(config_string)
            case ConfigFormat.JSON:
                config = ConfigFormat.load_json_config(config_string)
            case ConfigFormat.XML:
                config = ConfigFormat.load_xml_config(config_string)
            case ConfigFormat.AUTO:
                for loadable_function in loadable_functions:
                    if config:
                        break
                    if callable(loadable_function):
                        config = loadable_function(config_string)

        return config

    def load(self, config_file_path: Path | str) -> dict | None:
        config_string = self.load_as_string(config_file_path=config_file_path)
        return self.loads(config_string=config_string)

    def load_as_string(self, config_file_path: Path | str) -> str:
        with open(config_file_path, "r", encoding="utf-8") as config_file:
            string = config_file.read()
            return string

    def load_as_lines(self, config_file_path: Path | str) -> list:
        with open(config_file_path, "r", encoding="utf-8") as config_file:
            return config_file.readlines()

    def dumps(self, config_file_path: Path | str, config_string: str) -> bool:
        if isinstance(config_file_path, str):
            config_file_path = Path(config_file_path)

        config = None
        try:
            config = json.loads(config_string)
        except:
            config = None
        if config:
            self.dump(config_file_path=config_file_path, config=config)
            return True
        else:
            return False

    def dump(self, config_file_path: Path, config: dict) -> bool:
        match self:
            case ConfigFormat.INI:
                return self._write_ini_config(config_file_path, config)
            case ConfigFormat.JSON:
                return self._write_json_config(config_file_path, config)
            case ConfigFormat.XML:
                return self._write_xml_config(config_file_path, config)
            case _:
                return self._write_toml_config(config_file_path, config)

    ###############################  ##########################################

    @classmethod
    def load_toml_config(cls, raw_config_string: str) -> dict | None:
        try:
            return tomllib.loads(raw_config_string)
        except:
            return None

    @classmethod
    def _write_toml_config(cls, toml_file_path: Path, config: dict) -> bool:
        if not toml_file_path.exists():
            toml_file_path = File.touch(toml_file_path)  # type: ignore

        # section_names = map(lambda name: f"[{name}]", config.keys())
        with open(toml_file_path, "w", encoding="utf-8") as toml_file:
            toml_file.write(json.dumps(config))
        return True

    @classmethod
    def load_ini_config(cls, raw_config_string: str) -> dict | None:
        config_parser = None
        try:
            config_parser = ConfigParser()
            config_parser.read_string(raw_config_string)
            config = config_parser.as_dict()
            del config_parser
            return config
        except:
            del config_parser
            return None

    @classmethod
    def _write_ini_config(cls, ini_file_path: Path, config: dict) -> bool:
        config_parser = ConfigParser()
        config_parser.read_dict(config)
        with open(ini_file_path, "w", encoding="utf-8") as ini_file:
            config_parser.write(ini_file)
        del config_parser
        return True

    @classmethod
    def load_json_config(cls, raw_config_string: str) -> dict | None:
        try:
            return json.loads(raw_config_string)
        except:
            return None

    @classmethod
    def _write_json_config(cls, json_file_path: Path, config: dict) -> bool:
        json_file_path.write_text(json.dumps(config))
        return True

    @classmethod
    def load_xml_config(cls, raw_config_string: str | None = None) -> dict | None:
        return {}

    @classmethod
    def _write_xml_config(cls, json_file_path: Path | str, config: dict) -> bool:
        return True


loadable_functions = [
    ConfigFormat.load_toml_config,
    ConfigFormat.load_ini_config,
    ConfigFormat.load_json_config,
    ConfigFormat.load_xml_config,
]
