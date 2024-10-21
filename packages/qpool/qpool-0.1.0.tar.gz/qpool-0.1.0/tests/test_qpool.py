import pytest
import pytest_check as check
import asyncio
from uuid import UUID, uuid4
from rclib.multiprocessing.qpool import (
    Loggable,
    Lifecycle,
    Atomic,
    Identifiable,
    Actionable,
    Attemptable,
    IdentifiableTask,
    RetryableTask,
    Finish,
    Drain,
    Terminate,
    Exit,
)


async def test_retryable_backoff():
    """Test Retryable's backoff mechanism and status transitions."""
    finish_task = Finish(max_retries=3, initial_delay=1.0, max_delay=10.0)

    # Test initial state
    check.equal(finish_task.retries, 0)
    check.equal(finish_task.status, "queued")

    # Test retry and status change
    finish_task.retry()
    check.equal(finish_task.retries, 1)
    check.equal(finish_task.status, "attempting")

    # Test the backoff delay calculation
    delay = finish_task.calculate_backoff()
    check.equal(delay, 2.0)  # 1.0 initial delay * 2^1 (multiplier)

    # Simulate waiting for retry (using asyncio.sleep)
    await finish_task.wait_before_retry()

    # Retry again
    finish_task.retry()
    check.equal(finish_task.retries, 2)
    check.equal(finish_task.status, "attempting")

    # Test the backoff delay calculation after second retry
    delay = finish_task.calculate_backoff()
    check.equal(delay, 4.0)  # 1.0 initial delay * 2^2 (multiplier)

    # Retry until the task fails
    finish_task.retry()
    finish_task.retry()  # This should hit the max retries
    check.equal(finish_task.status, "failed")


def test_atomic_inheritance_error():
    """Ensure Atomic cannot be inherited with Stateful."""
    with pytest.raises(TypeError):

        class InvalidAtomic(Atomic, Lifecycle):
            pass


def test_identifiable():
    """Test Identifiable model for generating unique UUIDs."""
    task1 = Identifiable()
    task2 = Identifiable()
    check.is_instance(task1.id, UUID)
    check.is_instance(task2.id, UUID)
    check.not_equal(task1.id, task2.id)  # Ensure different UUIDs are generated


def test_actionable():
    """Test Actionable model."""
    task = Actionable(action="process", args=[1, 2, 3])
    check.equal(task.action, "process")
    check.equal(task.args, [1, 2, 3])


def test_finish_task():
    """Test Finish task which inherits from RetryableTask and Loggable."""
    finish_task = Finish(max_retries=3, initial_delay=1.0)
    check.equal(finish_task.action, "finish")
    check.equal(finish_task.retries, 0)
    check.equal(finish_task.status, "queued")
    check.equal(finish_task.log_level, "INFO")


def test_drain_task():
    """Test Drain task which is atomic and does not retry."""
    drain_task = Drain(action="drain", args=[])
    check.equal(drain_task.action, "drain")
    check.equal(drain_task.log_level, "INFO")
    check.is_instance(drain_task.id, UUID)
    check.equal(drain_task.args, [])


def test_terminate_task():
    """Test Terminate task, which should behave as an atomic task."""
    terminate_task = Terminate(action="terminate", args=[])
    check.equal(terminate_task.action, "terminate")
    check.equal(terminate_task.log_level, "INFO")
    check.is_instance(terminate_task.id, UUID)
    check.equal(terminate_task.args, [])


def test_exit_task():
    """Test Exit task, which behaves similarly to Drain."""
    exit_task = Exit(action="exit", args=[])
    check.equal(exit_task.action, "exit")
    check.equal(exit_task.log_level, "INFO")
    check.is_instance(exit_task.id, UUID)
    check.equal(exit_task.args, [])


async def test_wait_before_retry():
    """Test the wait_before_retry function."""
    retry_task = Finish(max_retries=3, initial_delay=1.0)
    retry_task.retry()
    delay = retry_task.calculate_backoff()

    check.equal(delay, 2.0)

    # Ensure the wait happens (mocking asyncio.sleep if needed, here we wait for real)
    await retry_task.wait_before_retry()


if __name__ == "__main__":
    pytest.main()
