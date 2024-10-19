#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2024-10-16 21:26:16
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   task
'''

from .discover import discover_and_mount_ts
from .task_base import task_function
from .tasks import Tasks

__all__ = ['discover_and_mount_ts', 'task_function', 'Tasks']