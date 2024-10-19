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
from typing import Type
import json
import time
from threading import Thread, Lock
import logging
from concurrent.futures import ThreadPoolExecutor

from ..task_service.task.tasks import Tasks
from ..config import Config

class ServerMiddleware:
    def __init__(self, tasks: Type[Tasks], config=Config()):
        self.tasks = tasks
        self.is_running = True
        self.polling_interval = 1
        self.executor = ThreadPoolExecutor(max_workers=config.max_workers)
        self.middleware_path = config.middleware_path
        self.lock = Lock()
        self.config = config
        self.initialize_database()

    def initialize_database(self):
        with self.lock:
            conn = sqlite3.connect(self.middleware_path)
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
        self.server_thread = Thread(target=self.listen_for_messages)
        self.server_thread.start()
        logging.info("Server started.")

    def join_server(self):
        self.server_thread.join()

    def stop_server(self):
        logging.info("Stopping server ...")
        self.is_running = False

    def listen_for_messages(self):
        conn = sqlite3.connect(self.middleware_path)
        cursor = conn.cursor()
        while self.is_running:
            with self.lock:
                cursor.execute(
                    """
                    SELECT 
                        COUNT(*)
                    FROM
                        messages
                    WHERE
                        status = 1
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
                                status = 1
                            ORDER BY
                                priority DESC
                            LIMIT {self.executor._max_workers}
                            """
                        )
                        task_list = cursor.fetchall()
                        cursor.executemany(
                            """
                            UPDATE
                                messages
                            SET
                                status = 2
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
                                                  self.config.middleware_path, 
                                                  json.loads(content).get("task_args"), 
                                                  count,
                                                  self.executor._max_workers)
                        except RuntimeError as e:
                            logging.error(f"Error while submitting task: {e}")
                            break
                        except Exception as e:
                            logging.error(f"Error submitting task: {e}")
                    if count > self.executor._max_workers:
                        self.polling_interval = 0.01  # 短轮询间隔用于高负载
                    else:
                        self.polling_interval = 1  # 恢复默认快速轮询
                else:
                    self.polling_interval = min(self.polling_interval + 0.02, 5)  # 增加轮询间隔
                time.sleep(self.polling_interval)
        conn.close()
        logging.info("Server stopped.")
        