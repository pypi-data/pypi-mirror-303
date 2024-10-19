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
import json
import time
from threading import Thread, Lock
from typing import Type
import logging
from concurrent.futures import ThreadPoolExecutor

from ..task_service import Services
from ..config import Config


class ClientMiddleware:
    def __init__(self, services: Type[Services], config=Config()):
        self.services = services
        self.is_running = True
        self.polling_interval = 1
        self.executor = ThreadPoolExecutor(max_workers=config.max_workers)
        self.config = config
        self.middleware_path = config.middleware_path
        self.lock = Lock()
        print(f"Middleware path: {self.middleware_path}")

    def start_client(self):
        logging.info("Starting client ...")
        self.server_thread = Thread(target=self.listen_for_messages)
        self.server_thread.start()
        logging.info("Client started.")

    def join_client(self):
        self.server_thread.join()

    def stop_client(self):
        logging.info("Stopping client ...")
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
                        status = 3
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
                                status = 3
                            ORDER BY
                                priority DESC
                            LIMIT {self.executor._max_workers}
                            """
                        )
                        message_list = cursor.fetchall()
                        cursor.executemany(
                            """
                            UPDATE
                                messages
                            SET
                                status = 2
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
                            self.executor.submit(self.services.run_callback, task_id, back_id, result, count, self.middleware_path, self.config)
                        except RuntimeError as e:
                            logging.error(f"Error while submitting task: {e}")
                            break
                        except Exception as e:
                            logging.error(f"Error while running callback: {e}")
                    if count > self.executor._max_workers:
                        self.polling_interval = 0.01
                    else:
                        self.polling_interval = 1
                else:
                    self.polling_interval = min(self.polling_interval + 0.02, 5)
                time.sleep(self.polling_interval)
        conn.close()
        logging.info("Client stopped.")
