from __future__ import annotations
from uuid import uuid4
from typing import (
    List,
    Any,
    Optional,
    Dict,
    Callable,
)
from pydantic import BaseModel, Field, UUID4
from enum import Enum
from rclib.utils.errors.decorators import enforce_type_hints_contracts
import logging


@enforce_type_hints_contracts
def simple_backoff(
    retries: int, initial_delay: float | int, max_delay: float | int
) -> float:
    """Simple backoff function. Same delay for each retry until max_delay is reached."""
    return min(max_delay, initial_delay * retries)


@enforce_type_hints_contracts
def exponential_backoff(
    retries: int,
    initial_delay: float | int,
    max_delay: float | int,
    multiplier: float | int,
) -> float:
    """Exponential backoff function. Delay increases exponentially with each retry until max_delay is reached."""
    return min(max_delay, initial_delay * (multiplier**retries))


class ResultTaskPair(BaseModel):
    """This represents a tuple of a task and a result."""

    task: Actionable
    result: Any

    def __str__(self) -> str:
        return f"{self.task} => {self.result}"


class Trackable(BaseModel):
    path: List[str]

    def track(self, action: str):
        self.path.append(action)


class Loggable(BaseModel):
    """Mixin that provides a log_level for tasks which should yield log events during their execution."""

    log_level: int = logging.INFO


class Identifiable(BaseModel):
    """Mixin that provides an id field with a default value of a new UUID4."""

    id: UUID4 = Field(default_factory=lambda: uuid4())


class Actionable(BaseModel):
    """Mixin that indicates a task maps to a prepared function and provides an action field."""

    action: str = Field(
        ...,
        description="The action to be performed by the task. Expected to map to a key in the Workers Action dictionary.",
    )


class PositionalActionable(Actionable):
    """Mixin that provides a list of positional arguments for an actionable task."""

    args: List[Any] = []


class KeywordActionable(Actionable):
    """Mixin that provides a dictionary of keyword arguments for an actionable task."""

    kwargs: Dict[str, Any] = {}


class MixedActionable(PositionalActionable, KeywordActionable):
    """Mixin that allows both positional and keyword arguments for an actionable task."""

    pass


class TaskState(Enum):
    """Enumeration of possible task states over the course of a Task lifecycle."""

    create = "create"  # Task has been created but not yet queued
    queue = "queue"  # Task has been queued
    attempt = "attempt"  # Task is being attempted
    retry = "retry"  # Task is being retried according to its retry policy
    fail = "fail"  # Task has failed completely
    success = "success"  # Task has completed successfully


class Lifecycle(BaseModel):
    """Mixin that provides a status field for task lifecycle tracking."""

    status: TaskState = Field(
        default=TaskState.create, description="The current status of the task."
    )


class Progresses(BaseModel):
    weight: float = Field(ge=0.0, le=1.0, default=1.0)


class Evaluatable[T](BaseModel):
    evaluator: Optional[Callable[[T], bool]] = None

    def evaluate(self, data: T):
        if self.evaluator:
            return self.evaluator(data)
        else:
            # This is fine, it just means the task is presumed to succeed if it doesn't raise an exception
            return True


class Retryable(Evaluatable, Lifecycle):
    tries: int = Field(
        ge=0, default=0, description="The number of times the task has been attempted."
    )
    max_tries: int = Field(
        ge=0,
        default=3,
        description="The maximum number of times the task can be attempted.",
    )
    initial_delay: float = Field(
        ge=0.0, default=2, description="The initial delay before the first retry."
    )
    max_delay: float = Field(
        ge=0.0, default=60.0, description="The maximum delay between retries."
    )

    def remaining(self) -> int:
        """Calculate the number of remaining retries.

        Returns:
            int: The number of remaining retries.
        """
        return max(0, self.max_tries - 1 - self.tries)

    def attempt(self):
        if self.tries < self.max_tries - 1:
            self.status = TaskState.retry
            self.tries += 1
        else:
            self.status = TaskState.fail

    def backoff(self):
        return exponential_backoff(self.tries, self.initial_delay, self.max_delay, 2.0)


class RequiresProps(BaseModel):
    """Mixin that provides a requires_props field for tasks that require specific props to be passed to them by their worker."""

    requires_props: List[str] = Field(
        default_factory=list,
        description="A list of required props that the task expects to be passed to it.",
    )
    include_all_props: bool = Field(
        default=False,
        description="Whether to include all props in the kwargs passed to the task or just the required props.",
    )

    def filter_props(self, props: Dict[str, Any] | BaseModel) -> Dict[str, Any]:
        if self.include_all_props:
            if isinstance(props, BaseModel):
                return props.model_dump()
            return props
        props = props.model_dump() if isinstance(props, BaseModel) else props
        return {k: v for k, v in props.items() if k in self.requires_props}


class ProgressUpdate(BaseModel):
    task_id: int
    total: int = 0
    completed: int = 0
    elapsed: float = 0.0
    remaining: float = 0.0
    failures: int = 0
    retries: int = 0
    status: str = "created"
