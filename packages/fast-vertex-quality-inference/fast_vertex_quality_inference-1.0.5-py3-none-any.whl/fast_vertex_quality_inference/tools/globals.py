from rich.console import Console
from fast_vertex_quality_inference.tools.stopwatch import stopwatch
import pkg_resources

stopwatches = stopwatch()

console = Console()

_verbose = False

MODELS_PATH = pkg_resources.resource_filename('fast_vertex_quality_inference', 'models/')

my_decay_splash = []

def global_print_my_decay_splash():
    if len(my_decay_splash) > 0:
        for counts, line in enumerate(my_decay_splash):
            if counts % 2 == 0: console.print("")
            console.print(line)
        console.print("")

