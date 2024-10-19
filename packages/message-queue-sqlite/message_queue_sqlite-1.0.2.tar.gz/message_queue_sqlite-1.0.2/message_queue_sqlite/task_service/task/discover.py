#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   discover.py
@Time    :   2024-10-16 21:27:00
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   task 动态挂载
'''

import pkgutil
from importlib import import_module

from .tasks import Tasks
from .task_base import create_task


def discover_and_mount_ts(base_package: str):
    package = import_module(base_package)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__, package.__name__ + '.'):
        module = import_module(module_name)
        for name, obj in vars(module).items():
            if callable(obj) and hasattr(obj, 'is_task') and hasattr(obj, 'use_cache'):
                task = create_task(obj.__name__, obj, obj.use_cache)
                Tasks.register(task.task_name, task)
    return Tasks
