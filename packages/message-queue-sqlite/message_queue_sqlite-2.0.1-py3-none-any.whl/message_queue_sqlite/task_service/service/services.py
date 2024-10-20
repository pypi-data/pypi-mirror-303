#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   services.py
@Time    :   2024-10-16 21:28:40
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   service functions
'''

import sqlite3
import os
import logging
import uuid
import json
from typing import Callable
import threading
import queue

from ...cache import Cache
from ...config import Config
from ...model import ThreadDict
from ...constants import TaskStatus


class Services:
    services_callbacks = ThreadDict()
    lock = threading.Lock()
    message_args = queue.Queue()
    callback_result = ThreadDict()
    count = 0
    middleware_num = 0

    @classmethod
    def register_function(cls, task_id, function: Callable):
        cls.services_callbacks[task_id] = function

    @classmethod
    def run_callback(cls, task_id, back_id, result, count, middleware_path, max_workers):
        callback = cls.services_callbacks.get(back_id, None)
        cls.count = count
        try:
            if callback:
                callback(result)
                if middleware_path not in cls.callback_result:
                    cls.callback_result[middleware_path] = ThreadDict()
                cls.callback_result[middleware_path][task_id] = TaskStatus.CALLBACKED.value
                logging.info(f"Callback for task {back_id} executed successfully")
            else:
                cls.callback_result[middleware_path][task_id] = TaskStatus.FAILED.value
                logging.warning(f"No callback registered for task {back_id}")
        except Exception as e:
            cls.callback_result[middleware_path][task_id] = TaskStatus.FAILED.value
            logging.error(f"Error while running callback for task {back_id}: {e}")
        finally:
            if count < max_workers or len(cls.callback_result[middleware_path]) >= max_workers:
                logging.info(f"Waiting for {max_workers} tasks to complete")
                cls.update_task_status(middleware_path)

    @classmethod
    def update_task_status(cls, middleware_path="./message_queue.db"):
        conn = sqlite3.connect(middleware_path)
        with cls.lock:
            conn.cursor().executemany(
                """
                UPDATE
                    messages
                SET
                    status = ?
                WHERE
                    id =?
                """,
                [(status, task_id) for task_id, status  in cls.callback_result[middleware_path].items()],
            )
            conn.commit()
            conn.close()
            cls.callback_result[middleware_path].clear()
    
    @classmethod
    def create_send_message(cls, config=Config()):
        def send_message(task_name:str, 
                         task_args: dict, 
                         callback: Callable = lambda x: None,
                         priority: int = 0,
                         use_cache: bool = False):
            task_id = str(uuid.uuid4())

            conn = sqlite3.connect(os.path.join(config.middleware_path, f"./middleware_{cls.middleware_num}.db"))
            if use_cache:
                new_task_args = {}
                cache_args = {}
                for key, value in task_args.items():
                    try:
                        new_task_args[key] = f"|{key}|"
                        cache_args[f"|{key}|"] = value
                    except Exception as e:
                        logging.error(f"Error while caching task_args: {e}")
                Cache.set(task_id, cache_args)
                task_args = new_task_args
            message = {
                "task_name": task_name,
                "task_args": task_args
            }
            back_id = id(callable)
            cls.message_args.put({"task_id": task_id, "message": message, "priority": priority, "back_id": back_id, "callback": callback})
            if cls.message_args.qsize() < config.max_workers and cls.count > config.max_workers:
                return
            with cls.lock:
                cursor = conn.cursor()
                message_args_list = list(cls.message_args.queue)
                for message_args in message_args_list:
                    cls.register_function(message_args["back_id"], message_args["callback"])
                cursor.executemany(
                    """
                    INSERT INTO 
                        messages (id, content, priority, back_id)
                        VALUES (?,?,?,?)
                    """,
                    [(status["task_id"], json.dumps(status["message"]), status["priority"], status["back_id"]) for status in message_args_list]
                )
                conn.commit()
                conn.close()
            cls.message_args.queue.clear()
            cls.middleware_num += 1
            if cls.middleware_num == config.middleware_num:
                cls.middleware_num = 0
        return send_message
    