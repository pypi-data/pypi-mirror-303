# -*- coding: UTF-8 -*-
__author__ = "helios"
# -*- coding: UTF-8 -*-
__author__ = "helios"
"""
  * @File    :   Option.py
  * @Time    :   2023/04/22 19:10:27
  * @Author  :   helios 
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""


from types import NoneType
from .Pair import Pair


class Option(Pair):
        
    def value(self, name: str | None = None, value_type: type = NoneType, default=None):
        name = self.get_name()
        if name:
            return super().value(name, value_type=value_type, default=default)
        else:
            return None
        