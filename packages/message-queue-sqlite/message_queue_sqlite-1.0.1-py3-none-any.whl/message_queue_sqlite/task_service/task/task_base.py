#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   task_base.py
@Time    :   2024-10-16 21:27:23
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   task 基类
'''

from abc import ABC, abstractmethod
import time
import logging
from typing import Callable
import threading

from ...constants import TaskStatus
from ...model import TaskResult
from ...cache import Cache

class TaskBase(ABC):
    def __init__(self, task_name: str, use_cache: bool = False):
        self.task_id = ""
        self.task_name = task_name
        self.start_time = 0.0
        self.end_time = 0.0
        self.status = TaskStatus.NOT_STARTED
        self.result = None
        self.use_cache = use_cache
        self.db_lock = threading.Lock()

    def run(self, **kwargs):
        self.start_time = time.time()
        self.status = TaskStatus.RUNNING
        if self.use_cache:
            new_kwargs = {}
            task_cache = Cache.get(self.task_id)
            Cache.delete(self.task_id)
            for key, value in kwargs.items():
                try:
                    new_kwargs[key] = task_cache[value] # type: ignore
                except Exception as e:
                    logging.error(f"Task {self.task_name} failed with error: {str(e)}")
            kwargs = new_kwargs
        try:
            self.result = self.execute(**kwargs)
            self.status = TaskStatus.FINISHED
            logging.info(f"Task {self.task_name} finished with result: {self.result}")
        
        except Exception as e:
            self.status = TaskStatus.FAILED
            self.result = str(e)
            logging.error(f"Task {self.task_name} failed with error: {str(e)}")
        
        finally:
            self.end_time = time.time()

    @abstractmethod
    def execute(self):
        pass

    def get_task_result(self, task_id, **kwargs):
        with self.db_lock:
            self.task_id = task_id
            self.run(**kwargs)
            if self.task_id == "" or\
                    self.start_time == 0.0 or\
                    self.end_time == 0.0 or\
                    self.status == TaskStatus.NOT_STARTED:
                raise ValueError("Task result is already available")
            else:
                result = TaskResult(task_id=self.task_id,
                                task_name=self.task_name,
                                start_time=self.start_time,
                                end_time=self.end_time,
                                status=self.status,
                                result=self.result)
            return result
    
def create_task(task_name: str, execute_func: Callable, use_cache: bool = False) -> TaskBase:
    class CustomTask(TaskBase):
        def __init__(self, task_name, use_cache):
            super().__init__(task_name, use_cache)

        def execute(self, **kwargs):
            return execute_func(**kwargs)
    return CustomTask(task_name, use_cache)

def task_function(use_cache: bool = False) -> Callable:
    def decorator(func: Callable) -> Callable:
        func.is_task = True # type: ignore
        func.use_cache = use_cache # type: ignore
        return func
    
    return decorator

