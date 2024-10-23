import logging
from inspect import getframeinfo, stack
from typing import Callable, List, TypeVar, Union

import rich
from rich.progress import (
    BarColumn,
    Progress,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)

logger = logging.getLogger("fastdev")

T = TypeVar("T")
R = TypeVar("R")


def parallel_track(
    func: Callable[[T], R],
    args: List[T],
    num_workers: int = 8,
    description: str = "Processing",
) -> List[R]:
    from multiprocessing import Pool

    columns = [
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(elapsed_when_finished=True),
    ]
    progress = Progress(*columns, console=rich.get_console())
    with progress:
        task = progress.add_task(description, total=len(args))
        results = []
        with Pool(processes=num_workers) as p:
            for result in p.imap(func, args):
                results.append(result)
                progress.update(task, advance=1)
    return results


_name_to_level = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "warn": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
}
_has_logged = set()


def log_once(message: str, level: Union[str, int] = logging.INFO):
    """
    Log a message only once (based on the message content and the source code location).

    Args:
        message (str): message to log
        level (str or int): log level, could be "critical", "error", "warning", "info", "debug" or corresponding int value (default: "info")
    """
    frame = getframeinfo(stack()[1][0])
    key = (frame.filename, frame.lineno, message)
    if key not in _has_logged:
        if isinstance(level, str):
            level = _name_to_level[level.lower()]
        logger.log(level, message)
        _has_logged.add(key)


__all__ = ["parallel_track", "log_once"]
