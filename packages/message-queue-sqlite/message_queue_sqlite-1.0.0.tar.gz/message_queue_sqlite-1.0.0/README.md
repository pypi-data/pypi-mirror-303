# MESSAGE QUEUE SQLITE

[TOC]

## 介绍
这是一个基于消息队列的任务处理系统。使用 SQLite 作为中间件实现了异步任务的提交与处理，支持多线程处理任务和结果的回调。

## 特性
- **异步任务处理**: 利用线程池实现任务的并发处理。
- **动态任务注册**: 可以通过装饰器轻松注册新任务。
- **结果回调**: 支持任务执行后的结果回调函数。
- **状态管理**: 通过状态枚举管理任务的生命周期，包括未开始、运行中、已完成、失败等状态

## 目录结构
```
message_queue_sqlite/ 
 ├── cache/ 
 │    └── __init__.py # 缓存模块 
 ├── config/ 
 │    └── __init__.py # 配置模块 
 ├── constants/ # 常量模块 
 │    ├── __init__.py 
 │    └── task_status.py # 任务状态常量 
 ├── middleware/ # 中间件模块 
 │    ├── __init__.py 
 │    ├── client.py # 客户端中间件 
 │    └── server.py # 服务器中间件 
 ├── model/ # 结果模型模块 
 │    ├── __init__.py │ 
 |    └── task_result.py # 任务结果模型 
 ├── task_service/ # 任务服务模块 
 │    ├── service/ 
 │    │    ├── __init__.py 
 │    │    └── services.py # 服务回调模块 
 │    ├── task/ 
 │    │    ├── __init__.py 
 │    │    ├── discover.py # 动态任务挂载模块 
 │    │    ├── task_base.py # 任务基类 
 │    │    └── tasks.py # 任务函数管理模块
 │    └── __init__.py 
 └── __init__.py # 初始化模块 
```

## 安装

1. **创建虚拟环境**
   ```bash
   mkdir demo
   cd demo
   python -m venv venv
   source venv/bin/activate
   ```

2. **克隆仓库**
   ```bash
   git clone https://gitee.com/cai-xinpenge/message_queue.git
   ```
   cd message_queue

3. **安装**
   ```bash
   pip install .
   ```

## 使用示例

请参考以下示例代码以了解如何使用 `message_queue_sqlite`：

### 目录结构

```
demo/
├── app/
|    ├── engine/
|    |    ├── __init__.py
|    |    └── test.py # 回调函数
|    └── __init__.py
main.py
```


### 定义任务

`app/engine/test.py`
```python
from message_queue_sqlite import task_function

@task_function(use_cache=True)
def test(message):
    print(message)
    return "test"

@task_function()
def test1(message):
    print(f"{message}1")
    return "test1"
```

`app/engine/__init__.py`
```python
from .test import test, test1

__all__ = ["test", "test1"]
```

### 动态挂载任务并初始化服务

`app/__init__.py`
```python
from message_queue_sqlite import discover_and_mount_ts, init_server
from message_queue_sqlite.config import Config # 配置模块，可配置中间件路径和线程池大小

# 动态挂在 app.engine 目录下的任务
tasks = discover_and_mount_ts("app.engine")
tasks.get_all_task_names()

# 初始化服务
server, client, send_message = init_server(tasks, Config(middleware_path="message_queue.db", max_workers=5)) # config 参数可选，默认 middleware_path 为 message_queue.db，max_workers 为 5

__all__ = ["model", "server"]
```

### 启动服务

`main.py`
```python
from app import server, client, send_message
from message_queue_sqlite import stop_server, start_server
import sys
import time
from threading import Thread


if __name__ == '__main__':
    # 启动服务
    Thread(target=start_server, args=(server, client)).start()
    # 循环发送任务
    while(True):
        try:
            keyworded_args = {'message': 'hello world'}
            callback = lambda x: print(x)
            send_message('test', keyworded_args, callback, 1, True)
            send_message('test1', keyworded_args, callback, 2)
        except KeyboardInterrupt:
            break
    # 停止服务
    sys.exit(stop_server(server, client))
```

### 任务调用

```python
# 缓存模式
send_message('test', keyworded_args, callback, priority=1, use_cache=True)  # priority 值越大优先级越高
# 非缓存模式
send_message('test1', keyworded_args, callback, priority=2)
```

## 缓存模式

当task任务的参数类型不方便被序列化时，可以选择使用缓存模式。该模式会将参数存入 cache 模块中，但执行任务时会先从 cache 中获取参数，由于 cache 只在运行时存在，所以该模式不支持持久化，若程序意外退出，缓存数据也会丢失，该模式主要针对参数类型不方便被序列化的场景。

## 任务状态
任务的生命周期通过枚举类型 TaskStatus 管理，包括：

- NOT_STARTED: 任务尚未开始
- RUNNING: 任务正在执行
- FINISHED: 任务执行完成
- FAILED: 任务执行失败
- CALLBACKED: 任务结果已经回调

## 联系
如有问题，请联系作者：

- 姓名: chakcy
- 邮箱: 947105045@qq.com
- 仓库地址: https://gitee.com/cai-xinpenge/message_queue

## 许可

该项目遵循 MIT 许可证。请查看 [LICENSE](https://gitee.com/cai-xinpenge/message_queue/blob/master/LICENSE) 文件以获取更多信息。