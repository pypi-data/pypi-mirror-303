from rich.traceback import install

from synaptic.state import State

from .main import cli

install()
from rich.pretty import install  # noqa: E402

install()

__all__ = ['cli', 'State']