from __future__ import annotations

import glob
import logging
import os
import shutil
from typing import Any, Dict, Literal

import rich

from fastdev.constants import FDEV_CSRC_ROOT
from fastdev.utils.cuda_utils import cuda_toolkit_available, current_cuda_arch
from fastdev.utils.profile_utils import timeit

logger = logging.getLogger("fastdev")
console = rich.get_console()

os.environ["TORCH_CUDA_ARCH_LIST"] = current_cuda_arch()

_MODULE_SRC_DIR: Dict[str, str] = {
    "fastdev_point_mesh": "point_mesh",
    "fastdev_sample_farthest_points": "sample_farthest_points",
    "fastdev_knn": "knn",
    "fastdev_ball_query": "ball_query",
}


class LazyExtension:
    def __init__(self) -> None:
        self._extra_include_paths: list[str] = [FDEV_CSRC_ROOT]
        self._extra_cflags = ["-O3"]
        self._extra_cuda_cflags = ["-O3"]
        self._cuda_toolkit_available = cuda_toolkit_available()
        if self._cuda_toolkit_available:
            self._extra_cflags.append("-DWITH_CUDA")
            self._extra_cuda_cflags.append("-DWITH_CUDA")
        self._module: dict[str, Any] = {}

    def load_module(
        self,
        module_name: Literal[
            "fastdev_point_mesh",
            "fastdev_sample_farthest_points",
            "fastdev_knn",
            "fastdev_ball_query",
        ],
    ) -> Any:
        from torch.utils.cpp_extension import _get_build_directory, load

        if module_name not in self._module:
            build_dir = _get_build_directory(module_name, verbose=False)

            sources = []
            sources.extend(
                glob.glob(os.path.join(FDEV_CSRC_ROOT, _MODULE_SRC_DIR[module_name], "**/*.cpp"), recursive=True)
            )
            if self._cuda_toolkit_available:
                sources.extend(
                    glob.glob(os.path.join(FDEV_CSRC_ROOT, _MODULE_SRC_DIR[module_name], "**/*.cu"), recursive=True)
                )

            try:
                if os.listdir(build_dir) != []:
                    # If the build exists, we assume the extension has been built and we can load it.
                    with timeit(f"Loading {module_name} extension"):
                        self._module[module_name] = load(
                            name=module_name,
                            sources=sources,
                            extra_cflags=self._extra_cflags,
                            extra_cuda_cflags=self._extra_cuda_cflags,
                            extra_include_paths=self._extra_include_paths,
                        )
                else:
                    # Build from scratch. Remove the build directory just to be safe: pytorch jit might stuck
                    # if the build directory exists.
                    shutil.rmtree(build_dir, ignore_errors=True)
                    with timeit(f"Building {module_name} extension"), console.status(
                        f"Building {module_name} extension (This may take a few minutes the first time)",
                        spinner="bouncingBall",
                    ):
                        self._module[module_name] = load(
                            name=module_name,
                            sources=sources,
                            extra_cflags=self._extra_cflags,
                            extra_cuda_cflags=self._extra_cuda_cflags,
                            extra_include_paths=self._extra_include_paths,
                        )
            except Exception as e:
                logger.error(f"[bold red]Error building {module_name} extension: {e}")
                logger.error(f"The {module_name} will not be available.")
                self._module[module_name] = None

        return self._module[module_name]


FDEV_EXT = LazyExtension()

__all__ = ["FDEV_EXT"]
