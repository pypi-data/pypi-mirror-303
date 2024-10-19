from beartype.claw import beartype_this_package

from fastdev.utils.profile_utils import timeit

beartype_this_package()

__all__ = ["timeit"]
