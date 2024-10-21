from __future__ import annotations
from typing import List, Union, Optional, TypeVar, Generic, Type
from pydantic import BaseModel
from queue import Empty
from multiprocessing import Queue, JoinableQueue
from rclib.utils.errors.decorators import enforce_type_hints_contracts
from rclib.multiprocessing.models import (
    ResultTaskPair,
)
from rclib.multiprocessing.tasks import (
    LogTask,
    ProgressTask,
    Task,
    ControlTask,
    Loggable,
)

T = TypeVar("T", bound=BaseModel)


class ModelQueue(Generic[T]):
    name: str
    joinable: bool = False
    queue: Union[JoinableQueue, Queue]
    model: Type[T]

    def __init__(self, name: str, model: Type[T], joinable: bool = False):
        self.name = name
        self.joinable = joinable
        self.model = model
        self.queue = JoinableQueue() if joinable else Queue()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        self.join()

    def put(self, item: T, block: bool = True, timeout: Optional[float] = None) -> bool:
        if not isinstance(item, self.model):
            return False
        try:
            self.queue.put(item, block=block, timeout=timeout)
            return True
        except Exception:
            return False

    def get(self, block: bool = True, timeout: Optional[float] = None) -> Optional[T]:
        return self.queue.get(block, timeout)

    def task_done(self):
        if not self.joinable:
            return
        self.queue.task_done()

    def join(self):
        if self.joinable:
            self.queue.join()
        else:
            self.queue.join_thread()

    def empty(self):
        return self.queue.empty()

    def full(self):
        return self.queue.full()

    def get_nowait(self):
        return self.queue.get_nowait()

    def put_nowait(self, obj):
        return self.queue.put_nowait(obj)

    def close(self):
        return self.queue.close()


def log_task(
    task: Loggable,
    message: str,
    queue: Optional[ModelQueue] = None,
    level: Optional[int] = None,
):
    """Log a message to the provided queue.

    Args:
        queue (ModelQueue[LogTask]): The queue to log to
        message (str): The message to log
        level (int, optional): The level suggested at the point of logging. If not set the tasks log_level will be used. Defaults to None.
    """
    if not queue:
        return
    task_is_loggable = isinstance(task, Loggable)
    if not task_is_loggable:
        return
    log_level = level if level else task.log_level
    log_task = LogTask(
        kwargs={
            "message": message,
            "level": log_level,
        },
    )
    queue.put(log_task)


@enforce_type_hints_contracts
def TaskQueue(name: str, joinable: bool = True) -> ModelQueue[Task]:
    return ModelQueue[Task](name=name, model=Task, joinable=joinable)


@enforce_type_hints_contracts
def ProgressQueue(name: str, joinable: bool = True) -> ModelQueue[ProgressTask]:
    return ModelQueue[ProgressTask](name=name, model=ProgressTask, joinable=joinable)


@enforce_type_hints_contracts
def ControlQueue(name: str, joinable: bool = True) -> ModelQueue[ControlTask]:
    return ModelQueue[ControlTask](name=name, model=ControlTask, joinable=joinable)


@enforce_type_hints_contracts
def ResultQueue(name: str, joinable: bool = False) -> ModelQueue[ResultTaskPair]:
    return ModelQueue[ResultTaskPair](
        name=name, model=ResultTaskPair, joinable=joinable
    )


@enforce_type_hints_contracts
def drain_queue(model_queue: ModelQueue) -> List[BaseModel]:
    results = []
    while not model_queue.empty():
        try:
            results.append(model_queue.get(block=False))
            model_queue.task_done()
        except Empty:
            break
    return results


@enforce_type_hints_contracts
def LogQueue(name: str, joinable: bool = True) -> ModelQueue[LogTask]:
    return ModelQueue[LogTask](name=name, model=LogTask, joinable=joinable)
