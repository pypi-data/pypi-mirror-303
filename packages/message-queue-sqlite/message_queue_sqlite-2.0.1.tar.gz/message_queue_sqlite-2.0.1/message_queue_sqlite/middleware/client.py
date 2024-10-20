#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client.py
@Time    :   2024-10-16 21:30:39
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   client middleware
'''

import sqlite3
import os
import json
import time
from threading import Thread, Lock
from typing import Type
import logging
from concurrent.futures import ThreadPoolExecutor

from ..task_service import Services
from ..config import Config
from ..constants import TaskStatus


class ClientMiddleware:
    def __init__(self, services: Type[Services], config=Config()):
        self.services = services
        self.is_running = True
        self.executor = ThreadPoolExecutor(max_workers=config.max_workers)
        self.config = config
        self.middleware_path = config.middleware_path
        self.lock = Lock()
        print(f"Middleware path: {self.middleware_path}")

    def start_client(self):
        logging.info("Starting client ...")
        for i in range(self.config.middleware_num):
            with self.lock:
                middleware_name = os.path.join(self.middleware_path, f"./middleware_{i}.db")
                setattr(self, f"server_thread_{i}", Thread(target=self.listen_for_messages, 
                                    args=(middleware_name, )))
        
        for i in range(self.config.middleware_num):
            getattr(self, f"server_thread_{i}").start()

        logging.info("Client started.")

    def join_client(self):
        for i in range(self.config.middleware_num):
            getattr(self, f"server_thread_{i}").join()

    def stop_client(self):
        logging.info("Stopping client ...")
        self.is_running = False

    def listen_for_messages(self, middleware_num):
        conn = sqlite3.connect(middleware_num)
        polling_interval = 0.1
        cursor = conn.cursor()
        while self.is_running:
            cursor.execute(
                f"""
                SELECT
                    COUNT(*)
                FROM
                    messages
                WHERE
                    status = {TaskStatus.FINISHED.value}
                """
            )
            count = cursor.fetchone()[0]
            if count > 0:
                try:
                    cursor.execute(
                        f"""
                        SELECT
                            id,
                            back_id,
                            result
                        FROM
                            messages
                        WHERE
                            status = {TaskStatus.FINISHED.value}
                        ORDER BY
                            priority DESC
                        LIMIT {self.executor._max_workers}
                        """
                    )
                    message_list = cursor.fetchall()
                    cursor.executemany(
                        f"""
                        UPDATE
                            messages
                        SET
                            status = {TaskStatus.CALLBACKING.value}
                        WHERE
                            id =?
                        """,
                        [(task_id,) for task_id, _, _ in message_list]
                    )
                except Exception as e:
                    logging.error(f"Error processing message: {e}")
                conn.commit()
                for task_id, back_id, result in message_list: # type: ignore
                    result = json.loads(result)
                    try:
                        self.executor.submit(self.services.run_callback, task_id, back_id, result, count, middleware_num, self.config.max_workers)
                    except RuntimeError as e:
                        logging.error(f"Error while submitting task: {e}")
                        break
                    except Exception as e:
                        logging.error(f"Error while running callback: {e}")
                polling_interval = max(polling_interval / (count / self.executor._max_workers), 0.001) 
            else:
                polling_interval = min(polling_interval + 0.02, 1)
            time.sleep(polling_interval)
        conn.close()
        logging.info("Client stopped.")
