import fast_vertex_quality_inference.tools.globals as myGlobals
from pydantic import BaseModel, validator, StrictStr, ValidationError
from typing import Optional
import re
from contextlib import contextmanager
import inspect
import traceback


@contextmanager
def execute_command(kwargs, param_class):

    caller_function = inspect.stack()[-2].function

    try:
        params = param_class(**kwargs)  # Use the passed parameter class
        yield params.dict()  # Pass the validated params to the `with` block
    except ValidationError as ve:
        # Handle Pydantic validation errors
        myGlobals.console.print(
            f"[red3][bold]Validation error in {caller_function}()[/bold][/red3]"
        )
        for error in ve.errors():
            myGlobals.console.print(
                f"[red3][bold]{error['loc'][0]}[/bold][/red3] - " f"{error['msg']}"
            )
    except Exception as e:
        # Handle general exceptions and print the stack trace
        myGlobals.console.print(
            f"[red3][bold]Error in {caller_function}()[/bold][/red3]"
        )
        myGlobals.console.print(f"[red3][bold]Exception:[/bold][/red3] {str(e)}")
        myGlobals.console.print(
            f"[red3][bold]Traceback:[/bold][/red3]\n{traceback.format_exc()}"
        )
        raise


class fvqi_runFromTupleParameters(BaseModel):
    file: StrictStr
    mother_particle: StrictStr
    daughter_particles: list
    fully_reco: bool
    nPositive_missing_particles: int
    nNegative_missing_particles: int
    mass_hypotheses: Optional[dict] = None
    intermediate_particle: Optional[dict] = None
    branch_naming_structure: Optional[dict] = None

    @validator("branch_naming_structure")
    def check_decay_format(cls, v):
        rapidsim_options = [
            "momenta_component",
            "true_momenta_component",
            "momenta_component",
            "true_momenta_component",
            "pid",
            "true_pid",
            "mass",
            "true_mass",
            "origin",
            "true_origin",
            "vertex",
            "true_vertex",
        ]
        for key in v:
            if key not in rapidsim_options:
                raise ValueError(
                    f"'{v}' is not a valid option; must be one of {rapidsim_options}."
                )
        return v

    @validator("mass_hypotheses")
    def check_mass_hypotheses(cls, v, values):
        if v:
            for particle_name in v:
                if particle_name not in values.get("daughter_particles"):
                    raise ValueError(
                        f"'{particle_name}' is invalid; not present in daughter_particles '{values.get('daughter_particles')}'."
                    )
        return v

    @validator("intermediate_particle")
    def check_intermediate_particle(cls, v, values):
        if v:
            for intermediate_name, particle_names in v.items():
                for particle_name in particle_names:
                    if particle_name not in values.get("daughter_particles"):
                        raise ValueError(
                            f"'{intermediate_name}' cannot be built; '{particle_name}' not present in daughter_particles '{values.get('daughter_particles')}'."
                        )
        return v


class fvqi_runParameters(BaseModel):
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
    only_rapidsim: bool = False
    workingDir: StrictStr = "./decay"

    @validator("useEvtGen", "evtGenUsePHOTOS")
    def check_boolean_strings(cls, value):
        normalized_value = value.strip().upper()
        if normalized_value not in {"TRUE", "FALSE"}:
            raise ValueError(f"'{value}' must be either 'TRUE' or 'FALSE'")
        return normalized_value

    @validator("decay", "naming_scheme", "decay_models")
    def remove_double_spaces(cls, v):
        return re.sub(r"\s+", " ", v).strip()

    @validator("decay")
    def check_decay_format(cls, v):
        if "->" not in v:
            raise ValueError(f"'{v}' is invalid; it must contain '->'.")
        mothers = v.split("->", 1)[0].split()  # split only once
        num_mothers = len([mother for mother in mothers if mother])
        if num_mothers != 1:
            raise ValueError(
                f"'{v}' is invalid; must define exactly one mother particle."
            )
        return v

    @validator("naming_scheme", "decay_models")
    def check_naming_scheme_structure(cls, v, values):
        decay = values.get("decay")
        if decay is None:
            raise ValueError(
                "Decay structure must be provided before validating naming_scheme."
            )
        decay_tokens = decay.split()
        if v:
            if "->" not in v:
                raise ValueError(f"'{v}' is invalid; it must contain '->'.")
            v_tokens = v.split()
            if len(v_tokens) != len(decay_tokens):
                raise ValueError(
                    f"'{v}' is invalid; it must match the structure of decay '{decay}' (replace any spaces in individual items with underscores)."
                )
        else:
            # Automatically generate naming scheme if not provided
            v = " ".join(
                "PHSP" if token not in {"{", "}", "->"} else token
                for token in decay_tokens
            )
        return v

    @validator("naming_scheme", allow_reuse=True)
    def check_naming_scheme(cls, v):
        tokens = v.split()
        for token in tokens:
            if token not in {"{", "}", "->"} and len(token) <= 1:
                raise ValueError(
                    f"Particle names must be longer than 1 character, offending name: '{token}'."
                )
        return v

    @validator("mass_hypotheses")
    def check_mass_hypotheses(cls, v, values):
        naming_scheme = values.get("naming_scheme")
        if naming_scheme and v:
            valid_particles = set(naming_scheme.split())
            for particle_name in v:
                if particle_name not in valid_particles:
                    raise ValueError(
                        f"'{particle_name}' is invalid; not present in naming_scheme '{naming_scheme}' (you might need to pad out particles with spaces)."
                    )
        return v

    @validator("intermediate_particle")
    def check_intermediate_particle(cls, v, values):
        naming_scheme = values.get("naming_scheme")
        if naming_scheme and v:
            valid_particles = set(naming_scheme.split())
            for intermediate_name, particle_names in v.items():
                for particle_name in particle_names:
                    if particle_name not in valid_particles:
                        raise ValueError(
                            f"'{intermediate_name}' cannot be built; '{particle_name}' not present in naming_scheme '{naming_scheme}' (you might need to pad out particles with spaces)."
                        )
        return v

    @validator("geometry")
    def check_geometry(cls, v):
        rapidsim_options = {"4pi", "LHCb"}
        if v not in rapidsim_options:
            raise ValueError(
                f"'{v}' is not a valid option; must be one of {rapidsim_options}."
            )
        return v

    @validator("acceptance")
    def check_acceptance(cls, v):
        rapidsim_options = {"Any", "ParentIn", "AllIn", "AllDownstream"}
        if v not in rapidsim_options:
            raise ValueError(
                f"'{v}' is not a valid option; must be one of {rapidsim_options}."
            )
        return v
