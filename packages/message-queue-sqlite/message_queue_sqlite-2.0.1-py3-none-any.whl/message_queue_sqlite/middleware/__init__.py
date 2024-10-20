#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2024-10-16 21:30:22
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   middleware
'''

from typing import Type
import os

from .server import ServerMiddleware
from .client import ClientMiddleware
from ..task_service import Tasks
from ..task_service import Services
from ..config import Config


def init_server(tasks: Type[Tasks], config=Config()):
    os.makedirs(config.middleware_path, exist_ok=True)
    server = ServerMiddleware(tasks, config)
    for i in range(config.middleware_num):
        middleware_path_num = os.path.join(config.middleware_path, f"./middleware_{i}.db")
        server.initialize_database(middleware_path_num)
    client = ClientMiddleware(Services, config)
    return server, client, client.services.create_send_message(config)

def start_server(server: ServerMiddleware, client: ClientMiddleware):
    server.start_server()
    client.start_client()
    server.join_server()
    client.join_client()

def stop_server(server: ServerMiddleware, client: ClientMiddleware):
    server.stop_server()
    client.stop_client()
    return 0
