from typing import List, Sequence, Tuple, Union

import torch
from torch import Tensor


def list_to_padded(
    x: Union[List[Tensor], Tuple[Tensor]],
    pad_size: Union[Sequence[int], None] = None,
    pad_value: Union[float, int] = 0.0,
    equisized: bool = False,
) -> Tensor:
    """
    Transforms a list of N tensors each of shape (Si_0, Si_1, ... Si_D)
    into:
    - a single tensor of shape (N, pad_size(0), pad_size(1), ..., pad_size(D))
      if pad_size is provided
    - or a tensor of shape (N, max(Si_0), max(Si_1), ..., max(Si_D)) if pad_size is None.

    Args:
      x: list of Tensors
      pad_size: list(int) specifying the size of the padded tensor.
        If `None` (default), the largest size of each dimension
        is set as the `pad_size`.
      pad_value: float value to be used to fill the padded tensor
      equisized: bool indicating whether the items in x are of equal size
        (sometimes this is known and if provided saves computation)

    Returns:
      x_padded: tensor consisting of padded input tensors stored
        over the newly allocated memory.
    """
    if equisized:
        return torch.stack(x, 0)

    if not all(torch.is_tensor(y) for y in x):
        raise ValueError("All items have to be instances of a torch.Tensor.")

    # we set the common number of dimensions to the maximum
    # of the dimensionalities of the tensors in the list
    element_ndim = max(y.ndim for y in x)

    # replace empty 1D tensors with empty tensors with a correct number of dimensions
    x = [(y.new_zeros([0] * element_ndim) if (y.ndim == 1 and y.nelement() == 0) else y) for y in x]

    if any(y.ndim != x[0].ndim for y in x):
        raise ValueError("All items have to have the same number of dimensions!")

    if pad_size is None:
        pad_dims: Sequence[int] = [max(y.shape[dim] for y in x if len(y) > 0) for dim in range(x[0].ndim)]
    else:
        if any(len(pad_size) != y.ndim for y in x):
            raise ValueError("Pad size must contain target size for all dimensions.")
        pad_dims = pad_size

    N = len(x)
    x_padded = x[0].new_full((N, *pad_dims), pad_value)
    for i, y in enumerate(x):
        if len(y) > 0:
            slices = (i, *(slice(0, y.shape[dim]) for dim in range(y.ndim)))
            x_padded[slices] = y  # type: ignore
    return x_padded


def padded_to_list(x: Tensor, split_size: Union[Sequence[int], None] = None, dim: int = 0) -> List[Tensor]:
    """
    Transforms a padded tensor of shape (N, S_1, S_2, ..., S_D) into a list
    of N tensors of shape:
    - (Si_1, Si_2, ..., Si_D) where (Si_1, Si_2, ..., Si_D) is specified in split_size(i)
    - or (S_1, S_2, ..., S_D) if split_size is None
    - or (Si_1, S_2, ..., S_D) if split_size(i) is an integer.

    Args:
      x: tensor
      split_size: optional 1D list/tuple of ints defining the number of
        items for each tensor.

    Returns:
      x_list: a list of tensors sharing the memory with the input.
    """
    x_list = list(x.unbind(dim=dim))

    if split_size is None:
        return x_list

    N = len(split_size)
    if x.shape[dim] != N:
        raise ValueError("Split size must be of same length as inputs first dimension")

    for i in range(N):
        x_list[i] = torch.narrow(x_list[i], dim, 0, split_size[i])
    return x_list


def list_to_packed(x: List[Tensor]) -> Tuple[Tensor, Tensor, Tensor, Tensor]:
    """
    Transforms a list of N tensors each of shape (Mi, K, ...) into a single
    tensor of shape (sum(Mi), K, ...).

    Args:
      x: list of tensors.

    Returns:
        4-element tuple containing

        - x_packed: tensor consisting of packed input tensors along the
          1st dimension.
        - num_items: tensor of shape N containing Mi for each element in x.
        - item_packed_first_idx: tensor of shape N indicating the index of
          the first item belonging to the same element in the original list.
        - item_packed_to_list_idx: tensor of shape sum(Mi) containing the
          index of the element in the list the item belongs to.
    """
    if not x:
        raise ValueError("Input list is empty")

    device = x[0].device
    sizes = [xi.shape[0] for xi in x]
    sizes_total = sum(sizes)
    num_items = torch.tensor(sizes, dtype=torch.int64, device=device)
    item_packed_first_idx = torch.zeros_like(num_items)
    item_packed_first_idx[1:] = torch.cumsum(num_items[:-1], dim=0)
    item_packed_to_list_idx = torch.arange(sizes_total, dtype=torch.int64, device=device)
    item_packed_to_list_idx = torch.bucketize(item_packed_to_list_idx, item_packed_first_idx, right=True) - 1
    x_packed = torch.cat(x, dim=0)

    return x_packed, num_items, item_packed_first_idx, item_packed_to_list_idx


def packed_to_list(x: Tensor, split_size: Union[Sequence[int], int]) -> List[Tensor]:
    """
    Transforms a tensor of shape (sum(Mi), K, L, ...) to N set of tensors of
    shape (Mi, K, L, ...) where Mi's are defined in split_size

    Args:
      x: tensor
      split_size: list, tuple or int defining the number of items for each tensor
        in the output list.

    Returns:
      x_list: A list of Tensors
    """
    return x.split(split_size, dim=0)


def padded_to_packed(
    x: torch.Tensor,
    split_size: Union[list, tuple],
    dim: int = 0,
):
    """
    Transforms a padded tensor of shape (..., N, M, ...) into a packed tensor of shape:
    - (..., sum(split_size), ...) if split_size is provided
    - (..., N * M, ...) if split_size is None

    Args:
      x: tensor of shape (..., N, M, ...)
      split_size: list, tuple defining the number of items for each tensor in the output list.
      dim: the `N` dimension in the input tensor

    Returns:
      x_packed: a packed tensor
    """
    x_packed = x.reshape(x.shape[:dim] + (-1,) + x.shape[dim + 2 :])

    # Convert to packed using split sizes
    N, M = x.shape[dim], x.shape[dim + 1]
    if N != len(split_size):
        raise ValueError("Split size must be of same length as inputs first dimension")
    if not all(isinstance(i, int) for i in split_size):
        raise ValueError("Support only 1-dimensional unbinded tensor. Split size for more dimensions provided")

    padded_to_packed_idx = torch.cat(
        [torch.arange(v, dtype=torch.int64, device=x.device) + i * M for (i, v) in enumerate(split_size)], dim=0
    )

    return x_packed.index_select(dim, padded_to_packed_idx)


__all__ = ["list_to_padded", "padded_to_list", "list_to_packed", "packed_to_list"]
