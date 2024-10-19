#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2024-10-16 21:33:03
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   Config 配置
'''

class Config:
    def __init__(self, max_workers: int = 10, middleware_path: str = "./message_queue.db"):
        self.max_workers = max_workers
        self.middleware_path = middleware_path