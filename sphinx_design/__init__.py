"""A sphinx extension for designing beautiful, view size responsive web components."""
from typing import TYPE_CHECKING

__version__ = "0.0.12"

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> dict:
    from .extension import setup_extension

    setup_extension(app)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
