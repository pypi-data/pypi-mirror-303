from typing import Any, Callable, Optional
import functools
import random
import time

from slupy.dates.utils import get_timetaken_fstring


def timer(func: Callable) -> Callable:
    """Decorator that prints the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_taken_in_secs = round(end - start, 6)
        timetaken_fstring = get_timetaken_fstring(num_seconds=time_taken_in_secs)
        print(f"Executed function '{func.__name__}' in: {timetaken_fstring}")
        return result
    return wrapper_timer


def slow_down(func: Callable) -> Callable:
    """
    Decorator that slows down the execution of the decorated function.
    Slows down the execution by 10-20 minutes.
    """
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        num_seconds_delayed = random.randint(600, 1200)
        time.sleep(num_seconds_delayed)
        return func(*args, **kwargs)
    return wrapper_slow_down


def repeat(*, num_times: int) -> Callable:
    """Decorator that executes the decorated function `num_times` times"""
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Repeating function '{func.__name__}' {num_times} times")
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat_decorator


def functionality_injector(
        *,
        before: Optional[Callable] = None,
        after: Optional[Callable] = None,
    ) -> Callable:
    """
    Decorator that injects some functionality which gets executed before/after the decorated function.

    Parameters:
        - before (callable): Executes just before calling the decorated function.
        - after (callable): Executes just after calling the decorated function.
    """
    def outer_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner_func(*args: Any, **kwargs: Any) -> Any:
            if before:
                before()
            result = func(*args, **kwargs)
            if after:
                after()
            return result
        return inner_func
    return outer_func
