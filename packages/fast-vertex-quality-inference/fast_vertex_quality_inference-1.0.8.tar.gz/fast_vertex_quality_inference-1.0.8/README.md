# Fast Vertexing Variables at LHCb - Inference Library

Full documentation is avalibale [**here**](https://fastvertexing.docs.cern.ch/index.html
).

## Description

This tool provides a quick approximation of the LHCb reconstruction process. Built on top of [**RapidSim**](https://github.com/gcowan/RapidSim), the `run` function automatically communicates with RapidSim to generate kinematic information which is then smeared before predictions of high-level vertexing variables are generated.

The software utilizes **Variational Autoencoders** (VAEs) to estimate these variables. These VAEs are trained on output from the LHCb simulation software.

Generated tuples can be integrated with other tools such as [**TriggerCalib**](https://pypi.org/project/triggercalib/) and [**PIDCalib2**](https://pypi.org/project/pidcalib2/), completing the full chain of estimation of reconstruction efficiencies and mass shapes for background studies at LHCb.

### Disclaimer

This tool is not designed to replace the full simulation software. It is designed to quickly return reasonable estimates of mass shapes and efficiencies.  

## Environment Setup

RaidSim is required to use the full functionalty of this library. The environment variables $RAPIDSIM_ROOT and $EVTGEN_ROOT that are used by the code to access the install. 

- `RAPIDSIM_ROOT`: The root directory for RapidSim.
- `EVTGEN_ROOT` (optional): The root directory for EVTGEN, if applicable.

## Example Usage

### `run()`

The `run()` function is the primary method to execute FastVertexing. It handles several key operations in the vertexing and event simulation process:

```python
from fast_vertex_quality_inference import run

run(
    events=1000,
    decay="B+ -> { D0b -> K+ e- anti-nue } pi+",
    naming_scheme="B_plus -> { NA -> K_plus e_minus NA } e_plus",
    decay_models="PHSP -> { ISGW2 -> PHSP PHSP PHSP } PHSP",
    mass_hypotheses={"e_plus": "e+"},
    intermediate_particle={"Jpsi": ["e_minus", "e_plus"]},
)
```

### `run_from_tuple()`

The `run_from_tuple()` function only executes the vertexing network on an existing tuple and can be used without a RapidSim installation.

```python

from fast_vertex_quality_inference import run_from_tuple

run_from_tuple(
    file="decay_tree.root",
    mother_particle="MOTHER",
    daughter_particles=["DAUGHTER1", "DAUGHTER2", "DAUGHTER3"],
    fully_reco=False,
    nPositive_missing_particles=0,
    nNegative_missing_particles=0,
    mass_hypotheses={"DAUGHTER2": "e+"},
    intermediate_particle={"INTERMEDIATE": ["DAUGHTER2", "DAUGHTER3"]},
    branch_naming_structure={"true_momenta_component": "{particle}_TRUE_P{dim}"},
)
```



