#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   task_resutl.py
@Time    :   2024-10-16 21:29:37
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   task 结果模型
'''

from typing import Any

from ..constants import TaskStatus


class TaskResult:
    def __init__(self, task_id: str, task_name: str, start_time: float, end_time: float, status: TaskStatus, result: Any):
        self.task_id = task_id
        self.task_name = task_name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.result = result

    def model_dump_json(self):
        return {
            "task_id": self.task_id,
            "task_name": self.task_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "status": self.status.value,
            "result": self.result
        }
        