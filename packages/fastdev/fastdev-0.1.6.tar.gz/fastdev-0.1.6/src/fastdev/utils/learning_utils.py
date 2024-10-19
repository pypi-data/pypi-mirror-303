import math
import os
import random
from typing import List, Tuple, Union

import numpy as np
import rich
import torch
import torch.nn as nn
from rich.table import Table

console = rich.get_console()


# Ref: https://github.com/open-mmlab/mmcv/blob/bfdd1f9c4281316f4f654672f0e9dbe1b0624ff0/mmcv/runner/utils.py#L74
def seed_everything(seed: int, deterministic: bool = False):
    """Seed all random number generators.

    Args:
        seed (int): Seed to be used.
        deterministic (bool): Whether to set the deterministic option for
            CUDNN backend, i.e., set `torch.backends.cudnn.deterministic`
            to True and `torch.backends.cudnn.benchmark` to False.
            Default: False.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

    if deterministic:
        torch.use_deterministic_algorithms(True)


PARAMETER_NUM_UNITS = [" ", "K", "M", "B", "T"]


# Ref: https://github.com/Lightning-AI/pytorch-lightning/blob/8ad3e29816a63d8ce5c00ac104b14729a4176f4f/src/lightning/pytorch/utilities/model_summary/model_summary.py#L434
def get_human_readable_count(number: Union[int, float]) -> str:
    """Abbreviates an integer number with K, M, B, T for thousands, millions, billions and trillions, respectively.

    Examples:
        >>> get_human_readable_count(123)
        '123  '
        >>> get_human_readable_count(1234)  # (one thousand)
        '1.2 K'
        >>> get_human_readable_count(2e6)   # (two million)
        '2.0 M'
        >>> get_human_readable_count(3e9)   # (three billion)
        '3.0 B'
        >>> get_human_readable_count(4e14)  # (four hundred trillion)
        '400 T'
        >>> get_human_readable_count(5e15)  # (more than trillion)
        '5,000 T'

    Args:
        number: a positive integer number

    Return:
        A string formatted according to the pattern described above.

    """
    assert number >= 0
    labels = PARAMETER_NUM_UNITS
    num_digits = int(math.floor(math.log10(number)) + 1 if number > 0 else 1)
    num_groups = int(math.ceil(num_digits / 3))
    num_groups = min(num_groups, len(labels))  # don't abbreviate beyond trillions
    shift = -3 * (num_groups - 1)
    number = number * (10**shift)
    index = num_groups - 1
    if index < 1 or number >= 100:
        return f"{int(number):,d} {labels[index]}"

    return f"{number:,.1f} {labels[index]}"


# Ref: https://github.com/Lightning-AI/pytorch-lightning/blob/8ad3e29816a63d8ce5c00ac104b14729a4176f4f/src/lightning/pytorch/callbacks/rich_model_summary.py#L83
def summarize_model(model: nn.Module, max_depth: int = 1):
    if not isinstance(max_depth, int) or max_depth < -1:
        raise ValueError(f"`max_depth` can be -1, 0 or > 0, got {max_depth}.")

    mods: List[Tuple[str, nn.Module]]
    if max_depth == 0:
        mods = []
    elif max_depth == 1:
        # the children are the top-level modules
        mods = list(model.named_children())
    else:
        mods = model.named_modules()
        mods = list(mods)[1:]  # do not include root module (nn.Module)

    if max_depth >= 1:
        mods = [m for m in mods if m[0].count(".") < max_depth]

    # do not count modules without parameters
    mod_num_params = {name: sum(p.numel() for p in mod.parameters()) for name, mod in mods}
    mod_num_trainable_params = {name: sum(p.numel() for p in mod.parameters() if p.requires_grad) for name, mod in mods}

    table = Table(title=f"Model Summary: [bold magenta]{model.__class__.__name__}[/]", header_style="bold magenta")
    table.add_column("", style="dim")
    table.add_column("Name", justify="left", no_wrap=True)
    table.add_column("Type")
    table.add_column("Params", justify="right")
    table.add_column("Trainable Params", justify="right")
    for idx, (name, mod) in enumerate(mods):
        if mod_num_params[name] == 0:
            continue
        table.add_row(
            str(idx),
            name,
            mod.__class__.__name__,
            get_human_readable_count(mod_num_params[name]),
            get_human_readable_count(mod_num_trainable_params[name]),
        )
    console.print(table)

    total_params = sum(mod_num_params.values())
    total_trainable_params = sum(mod_num_trainable_params.values())
    grid = Table.grid(expand=True)
    grid.add_column()
    grid.add_column()
    grid.add_row(f"[bold]Total params[/]: {get_human_readable_count(total_params)}")
    grid.add_row(f"[bold]Trainable params[/]: {get_human_readable_count(total_trainable_params)}")
    grid.add_row(f"[bold]Non-trainable params[/]: {get_human_readable_count(total_params - total_trainable_params)}")
    console.print(grid)
