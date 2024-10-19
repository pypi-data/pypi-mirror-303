import threading

class ThreadSet(set):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()

    def add(self, item):
        with self.lock:
            super().add(item)

    def remove(self, item):
        with self.lock:
            super().remove(item)

    def discard(self, item):
        with self.lock:
            super().discard(item)

    def __contains__(self, item):
        with self.lock:
            return super().__contains__(item)

    def clear(self):
        with self.lock:
            super().clear()

    def update(self, *args, **kwargs):
        with self.lock:
            super().update(*args, **kwargs)

    def intersection_update(self, *args, **kwargs):
        with self.lock:
            super().intersection_update(*args, **kwargs)

    def difference_update(self, *args, **kwargs):
        with self.lock:
            super().difference_update(*args, **kwargs)

    def symmetric_difference_update(self, *args, **kwargs):
        with self.lock:
            super().symmetric_difference_update(*args, **kwargs)

    def pop(self):
        with self.lock:
            return super().pop()

    def __len__(self):
        with self.lock:
            return super().__len__()

    # def __iter__(self):
    #     with self.lock:
    #         # 返回一个迭代器的副本，确保线程安全
    #         return iter(super().__copy__())