# -*- coding: UTF-8 -*-
__author__ = "helios"

from xy_configure.Format.ConfigFormat import ConfigFormat

# 后台队列执行文本解析


class Raw(object):
    name: str = ""

    strict: bool = True

    config_format: ConfigFormat = ConfigFormat.AUTO

    _raw_value = None

    _raw_string: str = ""

    _raw_base_string: str = ""

    _raw_base_string_list: list = []

    def update(
        self,
        name: str,
        raw_value,
        raw_string: str,
        raw_base_string: str,
        raw_base_string_list: list,
    ):
        self.name = name
        self._raw_value = raw_value
        self._raw_string = raw_string
        self._raw_base_string = raw_base_string
        self._raw_base_string_list = raw_base_string_list

    def append(self, raw_string: str):
        self._raw_base_string_list.append(raw_string)

    @property
    def start_tag_list(self) -> list:
        start_tag_list = []
        return start_tag_list

    @property
    def end_tag_list(self) -> list:
        end_tag_list = []
        return end_tag_list

    @property
    def comment_string(self) -> str:
        return ""

    @property
    def raw_string(self) -> str:
        return ""

    def __str__(self):
        pass

    # def _load_raw(self) -> bool:

    #     if not self._configure:
    #         return False

    #     if self.config_format == ConfigFormat.TOML or self.config_format == ConfigFormat.INI:

    #         section_name = self.section_name
    #         raw_section_name = f"[{section_name}]"
    #         raw_section_string_list = []
    #         reading_section_tag = False
    #         raw_section_name_exists = False
    #         for config_string in self._raw_value_string_list:
    #             is_start_with_raw_section_name = config_string.strip().startswith(raw_section_name)
    #             is_start_with_raw_section_name_start_tag = config_string.strip().startswith("[")

    #             if not reading_section_tag:
    #                 if is_start_with_raw_section_name:
    #                     reading_section_tag = True
    #                     raw_section_name_exists = True
    #             else:
    #                 if is_start_with_raw_section_name_start_tag:
    #                     reading_section_tag = False
    #                     break
    #             raw_section_string_list.append(config_string.strip())

    #         if raw_section_name_exists:
    #             self._raw_section_string_list = raw_section_string_list
    #             self._configure.raw_value_map.setdefault(section_name, self._raw_section_string_list)

    # return True
