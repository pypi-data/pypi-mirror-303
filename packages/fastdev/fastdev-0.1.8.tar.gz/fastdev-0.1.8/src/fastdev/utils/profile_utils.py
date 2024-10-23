# pyright: reportPossiblyUnboundVariable =false
import logging
from contextlib import ContextDecorator
from time import perf_counter
from typing import Optional

try:
    import torch

    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False

logger = logging.getLogger("fastdev")


class timeit(ContextDecorator):
    """
    Measure the time of a block of code.

    Args:
        print_tmpl (str, optional): The template to print the time. Defaults to None. Can be a
             string with a placeholder for the time, e.g., "func foo costs {:.5f} s" or a
             string without a placeholder, e.g., "func foo".

    Examples:
        >>> # doctest: +SKIP
        >>> with timeit():
        ...     time.sleep(1)
        it costs 1.00000 s
        >>> @timeit("func foo")
        ... def foo():
        ...     time.sleep(1)
        func foo costs 1.00000 s
    """

    def __init__(self, print_tmpl: Optional[str] = None):
        if print_tmpl is None:
            print_tmpl = "it costs {:.5f} s"

        if "{" not in print_tmpl and "}" not in print_tmpl:  # no placeholder
            print_tmpl = print_tmpl + " costs {:.5f} s"

        self._print_tmpl: str = print_tmpl
        self._start_time: float

    def __enter__(self):
        self._start_time = perf_counter()

    def __exit__(self, exec_type, exec_value, traceback):
        logger.info(self._print_tmpl.format(perf_counter() - self._start_time))


class cuda_timeit(ContextDecorator):
    """
    Measure the time of a block of code that may involve CUDA operations. We use CUDA events
    and synchronization for the accurate measurements.

    Args:
        print_tmpl (str, optional): The template to print the time. Defaults to None. Can be a
             string with a placeholder for the time, e.g., "func foo costs {:.5f} s" or a
             string without a placeholder, e.g., "func foo".
    """

    def __init__(self, print_tmpl: Optional[str] = None):
        if not TORCH_AVAILABLE or not torch.cuda.is_available():
            raise RuntimeError("CUDA is not available")

        if print_tmpl is None:
            print_tmpl = "it costs {:.5f} s"
        if "{" not in print_tmpl and "}" not in print_tmpl:  # no placeholder
            print_tmpl = print_tmpl + " costs {:.5f} s"

        self._print_tmpl: str = print_tmpl
        self._start_event = torch.cuda.Event(enable_timing=True)
        self._end_event = torch.cuda.Event(enable_timing=True)

    def __enter__(self):
        # https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html#demonstrating-speedups
        self._start_event.record()  # type: ignore

    def __exit__(self, exec_type, exec_value, traceback):
        self._end_event.record()  # type: ignore
        torch.cuda.synchronize()
        logger.info(self._print_tmpl.format(self._start_event.elapsed_time(self._end_event) / 1e3))


__all__ = ["timeit", "cuda_timeit"]
