from xy_configure.Format.ConfigFormat import ConfigFormat
from xy_configure.Raw.Format.Toml import Toml
from xy_configure.Raw.Format.Ini import Ini
from xy_configure.Raw.Format.Json import Json
from xy_configure.Raw.Format.Xml import Xml


def simple_parse(config_format: ConfigFormat = ConfigFormat.AUTO):
    match config_format:
        case ConfigFormat.INI:
            return Ini()
        case ConfigFormat.JSON:
            return Json()
        case ConfigFormat.XML:
            return Xml()
        case _:
            return Toml()


def parse(
    name: str,
    raw_value,
    raw_string: str,
    config_format: ConfigFormat = ConfigFormat.AUTO,
    strict: bool = True,
    raw_base_string: str = "",
    raw_base_string_list: list = [],
):
    raw = simple_parse(config_format)
    raw.strict = strict
    raw.name = name
    raw.update(
        name=name,
        raw_value=raw_value,
        raw_string=raw_string,
        raw_base_string=raw_base_string,
        raw_base_string_list=raw_base_string_list,
    )
    return raw
