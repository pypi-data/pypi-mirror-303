#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tasks.py
@Time    :   2024-10-16 21:27:58
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   task functions
'''

import logging
import json
import sqlite3
import threading
from .task_base import TaskBase
from ...model import ThreadDict, TaskResult
from typing import Dict


class Tasks:
    tasks_functions = {}
    tasks_result: Dict[str, Dict[str, TaskResult]] = ThreadDict()
    lock = threading.Lock()

    @classmethod
    def register(cls, task_name, task):
        cls.tasks_functions[task_name] = task

    @classmethod
    def get_task_function(cls, task_name) -> TaskBase:
        return cls.tasks_functions.get(task_name, None)
    
    @classmethod
    def task_executor(cls, message_id, content, middleware_path, task_args, count, max_workers):
        args = json.loads(content)

        result = cls.get_task_function(args.get("task_name")).\
            get_task_result(task_id=message_id, **task_args)
        if middleware_path not in cls.tasks_result:
            cls.tasks_result[middleware_path] = ThreadDict()
        cls.tasks_result[middleware_path][message_id] = result
        if count < max_workers or len(cls.tasks_result[middleware_path]) >= max_workers:
            conn = sqlite3.connect(middleware_path)
            with cls.lock:
                conn.cursor().executemany(
                    """
                    UPDATE
                        messages
                    SET
                        status = ?,
                        result = ?
                    WHERE
                        id = ?
                    """,
                    [(result.status.value, json.dumps(result.model_dump_json()), key) for key, result in cls.tasks_result[middleware_path].items()]
                )
                conn.commit()
                conn.close()
                cls.tasks_result[middleware_path].clear()

    @classmethod
    def get_all_task_names(cls):
        tasks_list = [task_name for task_name in cls.tasks_functions.keys()]
        logging.info(f"All tasks: {tasks_list}")
        return tasks_list
    