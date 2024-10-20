from contextlib import suppress
import os
os.environ["ZFIT_DISABLE_TF_WARNINGS"] = "1"

from .runner import run

import pkg_resources
DATA_PATH = pkg_resources.resource_filename('fast_vertex_quality_inference', '')