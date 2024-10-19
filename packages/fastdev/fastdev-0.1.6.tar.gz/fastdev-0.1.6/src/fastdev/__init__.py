import logging
from warnings import filterwarnings

import rich
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from rich.logging import RichHandler

rich.reconfigure(log_path=False)
filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)

logger = logging.getLogger("fastdev")
logger.propagate = False
logger.setLevel("INFO")
logger.addHandler(RichHandler(console=rich.get_console(), show_path=False, log_time_format="[%X]"))
