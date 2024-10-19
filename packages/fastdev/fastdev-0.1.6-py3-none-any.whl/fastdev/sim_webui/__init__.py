from beartype.claw import beartype_this_package

beartype_this_package()

from fastdev.sim_webui.webui import SimWebUI  # noqa: E402

__all__ = ["SimWebUI"]
