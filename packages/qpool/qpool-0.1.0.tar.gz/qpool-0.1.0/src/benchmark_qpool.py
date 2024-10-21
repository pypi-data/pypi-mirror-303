import asyncio
import time
from multiprocessing import cpu_count
from rclib.multiprocessing.qpool import Orchestrator, Task
import traceback
import math


def simple_task(t):
    try:
        time.sleep(t)
        return True
    except Exception as e:
        print(e)
        traceback.print_exc()
        return False


async def async_simple_task(t):
    try:
        await asyncio.sleep(t)
        return True
    except Exception as e:
        print(e)
        traceback.print_exc()
        return False


class SimpleTask(Task):
    action: str = "simple_task"


# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Worker function to find primes in a given range
def find_primes_in_range(start, end):
    for num in range(start, end):
        if is_prime(num):
            pass


async def benchmark_qpool():
    results = {}
    num_workers = cpu_count()
    start_time = time.monotonic()
    print("Running baseline...")
    range_start: int = 100_000
    range_end: int = 100_000_000

    # Calculate the chunk size for each worker
    chunk_size = (range_end - range_start) // num_workers
    ranges = [
        (range_start + i * chunk_size, range_start + (i + 1) * chunk_size)
        for i in range(num_workers)
    ]
    num_jobs = len(ranges)

    find_primes_in_range(range_start, range_end)

    baseline_duration = time.monotonic() - start_time

    results["no_pool"] = {
        "duration": baseline_duration,
        "items_per_second": num_jobs / (baseline_duration),
    }
    # Adjust the last range to include any remaining numbers
    ranges[-1] = (ranges[-1][0], range_end)

    # Get num_jobs copies of simple_task
    tasks = [SimpleTask(args=x) for x in ranges]

    # Benchmark using QPool with different numbers of processes
    for num_processes in [4, 8, 12, 16, 24, 32]:
        print(f"Benchmarking {num_processes}...")
        # Create a QPool and add tasks to it
        orchestrator = Orchestrator(
            num_workers=cpu_count(),
            actions={"simple_task": find_primes_in_range},
            show_progress=True,  # Enable progress monitoring
        )
        hold = orchestrator.add_tasks(tasks)
        start_time = time.monotonic()
        await hold

        job_results = await orchestrator.stop_workers()
        duration = time.monotonic() - start_time
        results[f"{num_processes}_processes"] = {
            "duration": duration,
            "items_per_second": num_jobs / duration,
        }
        print(f"Results returns: {len(job_results)}")
        assert len(job_results) == len(tasks)

    # Print the results
    for config, result in results.items():
        duration = result["duration"]
        items_per_second = result["items_per_second"]
        baseline_duration = results["no_pool"]["duration"]
        change = baseline_duration / duration
        print(
            f"{config}: {duration:.2f} seconds, processing {items_per_second}/s which is a {change:.2f}x change from the baseline"
        )


if __name__ == "__main__":
    asyncio.run(benchmark_qpool())
