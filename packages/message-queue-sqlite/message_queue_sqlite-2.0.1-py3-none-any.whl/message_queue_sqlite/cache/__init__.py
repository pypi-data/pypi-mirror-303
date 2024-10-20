#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2024-10-16 21:33:41
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   Cache 缓存
'''

from ..model import ThreadDict
from typing import Union


class Cache:
    cache = ThreadDict()
    
    @classmethod
    def set(cls, key, value: dict):
        cls.cache[key] = value

    @classmethod
    def get(cls, key) -> Union[dict, None]:
        return cls.cache.get(key)

    @classmethod
    def delete(cls, key):
        del cls.cache[key]
        