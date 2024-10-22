from typing import Optional
from pydantic import BaseModel, validator, StrictStr, ValidationError
import traceback
import re

import fast_vertex_quality_inference.tools.globals as myGlobals
from fast_vertex_quality_inference.rapidsim.run_rapidsim import run_rapidsim
from fast_vertex_quality_inference.network.run_network import run_network
import fast_vertex_quality_inference.tools.display as display


class fvqiParameters(BaseModel):
    events: int
    decay: StrictStr
    naming_scheme: StrictStr
    decay_models: Optional[StrictStr] = None
    mass_hypotheses: Optional[dict] = None
    intermediate_particle: Optional[dict] = None
    geometry: StrictStr = "LHCb"
    acceptance: StrictStr = "AllIn"
    useEvtGen: StrictStr = "TRUE"
    evtGenUsePHOTOS: StrictStr = "TRUE"
    dropMissing: bool = True
    verbose: bool = False
    workingDir: StrictStr = "./decay"

    @validator("useEvtGen", "evtGenUsePHOTOS")
    def check_boolean_strings(cls, value):
        if value not in ("TRUE", "FALSE"):
            raise ValueError(f"{value} must be either 'TRUE' or 'FALSE'")
        return value

    @validator("decay", "naming_scheme", "decay_models")
    def remove_double_spaces(cls, v):
        cleaned_value = re.sub(r"\s+", " ", v)
        return cleaned_value.strip()

    @validator("decay")
    def check_decay_format(cls, v):
        if "->" not in v:
            raise ValueError(f"'{v}' is invalid; it must contain '->'.")
        mothers = v.split("->")[0].replace("  ", " ").split(" ")
        num_mothers = len([mother for mother in mothers if mother != ""])
        if num_mothers != 1:
            raise ValueError(f"'{v}' is invalid; must define one mother particle.")
        # check particles are in rapidsim?
        return v

    @validator("naming_scheme", "decay_models")
    def check_naming_scheme_structure(cls, v, values):
        if v is not None:
            if "->" not in v:
                raise ValueError(f"'{v}' is invalid; it must contain '->'.")
            if len(v.replace("  ", "").split(" ")) != len(
                values["decay"].replace("  ", "").split(" ")
            ):
                decay = values["decay"]
                raise ValueError(
                    f"'{v}' is invalid; the structure must match that of decay '{decay}' (replace any spaces in individual items with underscores)."
                )
        else:  # as naming_scheme is a required argument, it should never go here
            v = ""
            for particle in values["decay"].replace("  ", "").split(" "):
                if particle in ["{", "}", "", "->"]:
                    v += f"{particle} "
                else:
                    v += "PHSP "  # fill with PHSP if decay_models == None
            v = v[:-1]

        return v

    @validator("naming_scheme", allow_reuse=True)
    def check_naming_scheme(cls, v):
        for split in v.replace("  ", "").split(" "):
            if split not in ["{", "}", "->", " ", ""]:
                if len(split) <= 1:
                    raise ValueError(
                        f"particle names need to be longer than 1 character, offending name: {split}."
                    )
        return v

    @validator("mass_hypotheses")
    def check_mass_hypotheses(cls, v, values):
        naming_scheme = values.get("naming_scheme")
        if naming_scheme:
            if v is not None:
                for particle_name in v:
                    if particle_name not in naming_scheme[
                        naming_scheme.find("->") :
                    ].split(" "):
                        raise ValueError(
                            f"'{particle_name}' is invalid; particle not present in naming_scheme '{values['naming_scheme']}'."
                        )
        return v

    @validator("intermediate_particle")
    def check_intermediate_particle(cls, v, values):
        naming_scheme = values.get("naming_scheme")
        if naming_scheme:
            if v is not None:
                for intermediate_name in v:
                    for particle_name in v[intermediate_name]:
                        if particle_name not in naming_scheme[
                            naming_scheme.find("->") :
                        ].split(" "):
                            raise ValueError(
                                f"'{intermediate_name}' cannot be built; '{particle_name}' not present in naming_scheme '{values['naming_scheme']}'."
                            )
        return v

    @validator("geometry")
    def check_geometry(cls, v):
        rapidsim_options = ["4pi", "LHCb"]
        if v not in rapidsim_options:
            raise ValueError(
                f"'{v}' not in RapidSim options: [green]{rapidsim_options}[/green]"
            )
        return v

    @validator("acceptance")
    def check_acceptance(cls, v):
        rapidsim_options = ["Any", "ParentIn", "AllIn", "AllDownstream"]
        if v not in rapidsim_options:
            raise ValueError(
                f"'{v}' not in RapidSim options: [green]{rapidsim_options}[/green]"
            )
        return v


def run(**kwargs):
    try:
        params = fvqiParameters(**kwargs)
        run_func(**params.dict())
    except ValidationError as ve:
        # Handle Pydantic validation errors
        myGlobals.console.print(
            "[red3][bold]Validation error in fvqi.run()[/bold][/red3]"
        )
        for error in ve.errors():
            myGlobals.console.print(
                f"[red3][bold]{error['loc'][0]}[/bold][/red3] - " f"{error['msg']}"
            )
    except Exception as e:
        # Handle general exceptions and print the stack trace
        myGlobals.console.print("[red3][bold]Error in fvqi.run()[/bold][/red3]")
        myGlobals.console.print(f"[red3][bold]Exception:[/bold][/red3] {str(e)}")
        myGlobals.console.print(
            f"[red3][bold]Traceback:[/bold][/red3]\n{traceback.format_exc()}"
        )
        raise


def run_func(**params):

    # Set verbosity if needed
    if params["verbose"]:
        myGlobals._verbose = True

    # Unpack the required parameters for run_rapidsim and run_network
    rapidsim_output = run_rapidsim(
        params["workingDir"],
        params["events"],
        params["decay"],
        params["naming_scheme"],
        params["decay_models"],
        params["mass_hypotheses"],
        params["intermediate_particle"],
        params["geometry"],
        params["acceptance"],
        params["useEvtGen"],
        params["evtGenUsePHOTOS"],
        params["dropMissing"],
    )

    (
        rapidsim_tuple,
        fully_reco,
        nPositive_missing_particles,
        nNegative_missing_particles,
        mother_particle,
        daughter_particles,
        true_PID_scheme,
        combined_particles,
        map_NA_codes,
    ) = rapidsim_output

    # Display events table
    display.events_table(params["events"], rapidsim_tuple)

    # Handle intermediate_particle
    intermediate_particle_name = None
    if params["intermediate_particle"] and params["intermediate_particle"].keys():
        intermediate_particle_name = list(params["intermediate_particle"].keys())[0]

    # Run network with rapidsim output
    rapidsim_tuple_reco = run_network(
        rapidsim_tuple,
        fully_reco,
        nPositive_missing_particles,
        nNegative_missing_particles,
        true_PID_scheme,
        combined_particles,
        map_NA_codes,
        params["dropMissing"],
        mother_particle_name=mother_particle,
        intermediate_particle_name=intermediate_particle_name,
        daughter_particle_names=daughter_particles,
    )

    # Display timing and file information
    total_time = display.timings_table()
    # myGlobals.global_print_my_decay_splash()
    display.print_file_info(rapidsim_tuple_reco, time=total_time)
