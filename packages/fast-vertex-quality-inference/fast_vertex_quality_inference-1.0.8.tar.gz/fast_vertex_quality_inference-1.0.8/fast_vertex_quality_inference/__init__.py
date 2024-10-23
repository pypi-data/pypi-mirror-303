import pkg_resources

DATA_PATH = pkg_resources.resource_filename("fast_vertex_quality_inference", "")

from .runner import run, run_from_tuple

__all__ = [
    "run",
    "run_from_tuple",
]  # controls what is imported if someone were to from <module> import *
