import inspect
from functools import lru_cache, partial, wraps
from typing import Any, Callable, Dict, List, Literal, Optional, Tuple, Union, no_type_check, overload

import numpy as np
import torch
from beartype import beartype
from numpy.typing import ArrayLike


@overload
def to_numpy(x: torch.Tensor, preserve_list: bool = ...) -> np.ndarray: ...
@overload
def to_numpy(x: np.ndarray, preserve_list: bool = ...) -> np.ndarray: ...
@overload
def to_numpy(x: ArrayLike, preserve_list: bool = ...) -> np.ndarray: ...
@overload
def to_numpy(x: None, preserve_list: bool = ...) -> None: ...
@overload
def to_numpy(x: Dict[Any, Any], preserve_list: bool = ...) -> Dict[Any, np.ndarray]: ...
@overload
def to_numpy(x: List[Any], preserve_list: Literal[True]) -> List[np.ndarray]: ...
@overload
def to_numpy(x: List[Any], preserve_list: Literal[False] = ...) -> np.ndarray: ...
@overload
def to_numpy(x: Tuple[Any, ...], preserve_list: Literal[True]) -> Tuple[np.ndarray, ...]: ...
@overload
def to_numpy(x: Tuple[Any, ...], preserve_list: Literal[False] = ...) -> np.ndarray: ...
def to_numpy(
    x: Any, preserve_list: bool = True
) -> Optional[Union[np.ndarray, Dict[Any, np.ndarray], List[np.ndarray], Tuple[np.ndarray, ...]]]:
    """Convert input to numpy array.

    Args:
        x (Any): Input to be converted.
        preserve_list (bool, optional): Whether to preserve list or convert to numpy array. Defaults to True.

    """
    if isinstance(x, np.ndarray):
        return x
    elif isinstance(x, torch.Tensor):
        return x.cpu().detach().numpy()
    elif x is None:
        return None
    elif isinstance(x, dict):
        return {k: to_numpy(v) for k, v in x.items()}
    elif preserve_list and isinstance(x, (list, tuple)):
        return type(x)(to_numpy(elem, preserve_list=preserve_list) for elem in x)
    try:
        return np.asarray(x)
    except Exception as _:
        return x


@overload
def to_torch(x: np.ndarray, preserve_list: bool = ...) -> torch.Tensor: ...
@overload
def to_torch(x: torch.Tensor, preserve_list: bool = ...) -> torch.Tensor: ...
@overload
def to_torch(x: None, preserve_list: bool = ...) -> None: ...
@overload
def to_torch(x: Dict[Any, Any], preserve_list: bool = ...) -> Dict[Any, torch.Tensor]: ...
@overload
def to_torch(x: List[Any], preserve_list: Literal[True]) -> List[torch.Tensor]: ...
@overload
def to_torch(x: List[Any], preserve_list: Literal[False] = ...) -> torch.Tensor: ...
@overload
def to_torch(x: Tuple[Any, ...], preserve_list: Literal[True]) -> Tuple[torch.Tensor, ...]: ...
@overload
def to_torch(x: Tuple[Any, ...], preserve_list: Literal[False] = ...) -> torch.Tensor: ...
def to_torch(
    x: Any, preserve_list: bool = True
) -> Optional[Union[torch.Tensor, Dict[Any, torch.Tensor], List[torch.Tensor], Tuple[torch.Tensor, ...]]]:
    """Convert input to torch tensor.

    Args:
        x (Any): Input to be converted.
        preserve_list (bool, optional): Whether to preserve list or convert to torch tensor. Defaults to True.
    """
    if isinstance(x, torch.Tensor):
        return x
    elif isinstance(x, np.ndarray):
        return torch.from_numpy(x)
    elif isinstance(x, dict):
        return {k: to_torch(v) for k, v in x.items()}
    elif preserve_list and isinstance(x, (list, tuple)):
        return type(x)(to_torch(elem, preserve_list=preserve_list) for elem in x)
    elif x is None:
        return None
    try:
        return torch.as_tensor(x)
    except Exception as _:
        return x


@overload
def to_number(x: None) -> None: ...
@overload
def to_number(x: int) -> int: ...
@overload
def to_number(x: float) -> float: ...
@overload
def to_number(x: np.ndarray) -> Union[int, float]: ...
@overload
def to_number(x: torch.Tensor) -> Union[int, float]: ...
def to_number(x: Any) -> Optional[Union[int, float]]:
    """Convert input to number.

    Args:
        x (Any): Input to be converted.

    """
    if x is None:
        return None
    elif isinstance(x, torch.Tensor):
        return x.item()
    elif isinstance(x, np.ndarray):
        return x.item()
    return x


@lru_cache(maxsize=None)
@beartype
def auto_cast(
    fn: Optional[Callable] = None, return_type: Literal["by_input", "by_func", "pt", "np"] = "by_input"
) -> Callable:
    """Automatically cast input and output of a function to numpy or torch tensors. Since the function simply converts
    the input and output to numpy or torch tensors, it may introduce overhead. It is recommended to use this function
    for functions that are not performance critical.

    Args:
        fn (Callable): Function to be wrapped.
        return_type (Literal["by_input", "by_func", "pt", "np"], optional): Type of return value. Defaults to "by_input".
            - "by_input": Return type is determined by the input argument type, first found array/tensor type is used.
            - "by_func": Return type is determined by the orginal function.
            - "pt": Return type is torch.Tensor.
            - "np": Return type is np.ndarray.

    Returns:
        Callable: Wrapped function.
    """
    if fn is None:
        return partial(auto_cast, return_type=return_type)

    sig = inspect.signature(fn)
    params = sig.parameters

    @no_type_check
    @wraps(fn)
    def wrapped(*args: Any, **kwargs: Any) -> Any:
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        input_type: Optional[Literal["pt", "np"]] = None
        for name, value in bound_args.arguments.items():
            param = params[name]
            expected_type = param.annotation

            if expected_type is inspect.Parameter.empty:
                continue
            if expected_type is np.ndarray:
                bound_args.arguments[name] = to_numpy(value)
                input_type = "np" if input_type is None else input_type
            elif expected_type is torch.Tensor:
                bound_args.arguments[name] = to_torch(value)
                input_type = "pt" if input_type is None else input_type

        result = fn(*bound_args.args, **bound_args.kwargs)  # type: ignore

        if (return_type == "by_input" and input_type == "np") or return_type == "np":
            return to_numpy(result)
        elif (return_type == "by_input" and input_type == "pt") or return_type == "pt":
            return to_torch(result)
        else:
            return result

    return wrapped


@overload
def atleast_nd(tensor: None, expected_ndim: int) -> None: ...
@overload
def atleast_nd(tensor: np.ndarray, expected_ndim: int) -> np.ndarray: ...
@overload
def atleast_nd(tensor: torch.Tensor, expected_ndim: int) -> torch.Tensor: ...
def atleast_nd(
    tensor: Optional[Union[np.ndarray, torch.Tensor]], expected_ndim: int
) -> Optional[Union[np.ndarray, torch.Tensor]]:
    """Convert input to at least nD tensor.

    .. note::
        Differs from `np.atleast_nd` and `torch.atleast_nd`,
        this function adds dimensions to the front of the tensor.

    """
    if tensor is None:
        return None
    actual_ndim = tensor.ndim
    if actual_ndim >= expected_ndim:
        return tensor
    num_dims_to_add = expected_ndim - actual_ndim
    if isinstance(tensor, np.ndarray):
        return np.expand_dims(tensor, axis=tuple(range(num_dims_to_add)))
    elif isinstance(tensor, torch.Tensor):
        return tensor.view((1,) * num_dims_to_add + tensor.shape)


__all__ = ["to_numpy", "to_torch", "to_number", "auto_cast", "atleast_nd"]
