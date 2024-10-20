#-*- coding: UTF-8 -*-
__author__ = 'helios'
'''
  * @File    :   ConfigParser.py
  * @Time    :   2023/04/22 20:07:28
  * @Author  :   helios 
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
'''

from configparser import ConfigParser as pyConfigParser


class ConfigParser(pyConfigParser):
    def as_dict(self):
        sections = dict(self._sections)  # type: ignore
        for key in sections:
            sections.setdefault(key, dict(sections.get(key)))  # type: ignore
        return sections
