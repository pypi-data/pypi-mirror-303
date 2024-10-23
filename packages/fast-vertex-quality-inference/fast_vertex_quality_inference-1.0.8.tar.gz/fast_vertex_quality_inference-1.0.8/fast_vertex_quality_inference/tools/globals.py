from rich.console import Console
from fast_vertex_quality_inference.tools.stopwatch import stopwatch
import pkg_resources
import os
import pandas as pd

stopwatches = stopwatch()

console = Console()

_verbose = False

MODELS_PATH = pkg_resources.resource_filename(
    "fast_vertex_quality_inference", "models/"
)

my_decay_splash = []


# Check environment variables
def get_environment_variable(var_name: str) -> str:
    value = os.environ.get(var_name)
    if value is None:
        raise EnvironmentError(f"Environment variable ${var_name} not set.")
    return value


rapidsim_settings = {}
rapidsim_settings["imported"] = False

if os.environ.get("RAPIDSIM_ROOT"):

    PARTICLES_FILE = "config/particles.dat"
    EVTGEN_ROOT_ENV = "EVTGEN_ROOT"
    RAPIDSIM_EXECUTABLE = "/build/src/RapidSim.exe"

    rapidsim_settings["RAPIDSIM_ROOT"] = os.environ.get("RAPIDSIM_ROOT")
    rapidsim_settings["RAPIDSIM_particles"] = (
        os.environ.get("RAPIDSIM_ROOT") + "/" + PARTICLES_FILE
    )
    rapidsim_settings["RAPIDSIM_particles_df"] = pd.read_csv(
        rapidsim_settings["RAPIDSIM_particles"], sep=r"\s+"
    )
    rapidsim_settings["USE_EVTGEN"] = (
        get_environment_variable(EVTGEN_ROOT_ENV) is not None
    )
    rapidsim_settings["rapidsim_exe"] = (
        f"{rapidsim_settings['RAPIDSIM_ROOT']}{RAPIDSIM_EXECUTABLE}"
    )
    rapidsim_settings["imported"] = True

# else: # Running without RapidSim


def global_print_my_decay_splash():
    if len(my_decay_splash) > 0:
        for counts, line in enumerate(my_decay_splash):
            if counts % 2 == 0:
                console.print("")
            console.print(line)
        console.print("")
