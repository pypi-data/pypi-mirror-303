#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   task_status.py
@Time    :   2024-10-16 21:32:40
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   Task 状态枚举
'''

from enum import Enum


class TaskStatus(Enum):
    NOT_STARTED = 1
    RUNNING = 2
    FINISHED = 3
    FAILED = 4
    CALLBACKED = 5
