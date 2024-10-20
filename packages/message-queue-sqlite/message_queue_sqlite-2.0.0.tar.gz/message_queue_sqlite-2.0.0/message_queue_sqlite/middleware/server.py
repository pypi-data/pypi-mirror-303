#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2024-10-16 21:31:55
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   server middleware
'''

import sqlite3
import os
from typing import Type
import json
import time
from threading import Thread, Lock
import logging
from concurrent.futures import ThreadPoolExecutor

from ..task_service.task.tasks import Tasks
from ..config import Config
from ..constants import TaskStatus


class ServerMiddleware:
    def __init__(self, tasks: Type[Tasks], config=Config()):
        self.tasks = tasks
        self.is_running = True
        self.executor = ThreadPoolExecutor(max_workers=config.max_workers)
        self.middleware_path = config.middleware_path
        self.lock = Lock()
        self.config = config
        os.makedirs(self.middleware_path, exist_ok=True)
        for i in range(config.middleware_num):
            middleware_path_num = os.path.join(self.middleware_path, f"./middleware_{i}.db")
            self.initialize_database(middleware_path_num)

    def initialize_database(self, middleware_num):
        conn = sqlite3.connect(middleware_num)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                content TEXT NOT NULL,
                status INTEGER NOT NULL DEFAULT 1,
                result TEXT DEFAULT NULL,
                priority INTEGER NOT NULL,
                back_id INTEGER 
            );
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS changes_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                change_type TEXT,
                change_time DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        conn.execute(
            """
            CREATE TRIGGER IF NOT EXISTS after_insert
            AFTER INSERT ON messages
            BEGIN
                INSERT INTO changes_log (change_type) VALUES ('INSERT');
            END;
            """
        )
        conn.execute(
            """
            CREATE TRIGGER IF NOT EXISTS after_update
            AFTER UPDATE ON messages
            BEGIN
                INSERT INTO changes_log (change_type) VALUES ('UPDATE');
            END;
            """
        )
        conn.commit()
        conn.close()

    def start_server(self):
        logging.info("Starting server ...")
        for i in range(self.config.middleware_num):
            with self.lock:
                middleware_name = os.path.join(self.middleware_path, f"./middleware_{i}.db")
                self.initialize_database(middleware_name)
                setattr(self, f"server_thread_{i}", Thread(target=self.listen_for_messages, 
                                    args=(middleware_name, )))

        for i in range(self.config.middleware_num):
            getattr(self, f"server_thread_{i}").start()

        logging.info("Server started.")

    def join_server(self):
        for i in range(self.config.middleware_num):
            getattr(self, f"server_thread_{i}").join()

    def stop_server(self):
        logging.info("Stopping server ...")
        self.is_running = False

    def listen_for_messages(self, middleware_num):
        conn = sqlite3.connect(middleware_num)
        self.initialize_database(middleware_num)
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
                    status = {TaskStatus.NOT_STARTED.value}
                """
            )
            count = cursor.fetchone()[0]
            if count > 0:
                try:
                    cursor.execute(
                        f"""
                        SELECT 
                            id,
                            content
                        FROM
                            messages
                        WHERE
                            status = {TaskStatus.NOT_STARTED.value}
                        ORDER BY
                            priority DESC
                        LIMIT {self.executor._max_workers}
                        """
                    )
                    task_list = cursor.fetchall()
                    cursor.executemany(
                        f"""
                        UPDATE
                            messages
                        SET
                            status = {TaskStatus.RUNNING.value}
                        WHERE
                            id =?
                        """,
                        [(task_id,) for task_id, _ in task_list]
                    )
                except Exception as e:
                    logging.error(f"Error processing message: {e}")
                conn.commit()

                for message_id, content in task_list: # type: ignore
                    try:
                        self.executor.submit(self.tasks.task_executor,
                                              message_id, 
                                              content, 
                                              middleware_num, 
                                              json.loads(content).get("task_args"), 
                                              count,
                                              self.executor._max_workers)
                    except RuntimeError as e:
                        logging.error(f"Error while submitting task: {e}")
                        break
                    except Exception as e:
                        logging.error(f"Error submitting task: {e}")
                polling_interval = max(polling_interval / (count / self.executor._max_workers), 0.001) 
            else:
                polling_interval = min(polling_interval + 0.02, 1)  # 增加轮询间隔
            time.sleep(polling_interval)
        conn.close()
        logging.info("Server stopped.")
        