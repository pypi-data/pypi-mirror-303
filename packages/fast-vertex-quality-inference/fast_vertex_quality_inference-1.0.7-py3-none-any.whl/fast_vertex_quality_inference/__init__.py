import os

os.environ["ZFIT_DISABLE_TF_WARNINGS"] = "1"

import pkg_resources

DATA_PATH = pkg_resources.resource_filename("fast_vertex_quality_inference", "")

from .runner import run

__all__ = ["run"]
