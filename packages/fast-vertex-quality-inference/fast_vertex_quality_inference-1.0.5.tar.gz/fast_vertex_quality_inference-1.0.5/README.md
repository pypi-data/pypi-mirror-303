# Fast Vertexing Variables at LHCb - Inference Library

## Description

This tool provides a quick approximation of the LHCb reconstruction process. Built on top of **RapidSim** ([GitHub Repository](https://github.com/gcowan/RapidSim)), the `run` function automatically communicates with RapidSim to generate useful outputs.

The `run` function generates tuples that include kinematic information (both true and smeared) and high-level reconstruction variables for each event. The software utilizes **Variational Autoencoders** to estimate these variables, trained on comprehensive LHCb simulations.

These tuples can be integrated with other tools to estimate Particle Identification (PID) and trigger responses, enabling the estimation of reconstruction efficiencies and mass shapes for background studies at LHCb.

### Environment Setup

Before running the script, ensure that the following environment variables are set:

- `RAPIDSIM_ROOT`: The root directory for RapidSim.
- `EVTGEN_ROOT` (optional): The root directory for EVTGEN, if applicable.

## Example Usage

Here's a simple example demonstrating how to use the library:

```python
import fast_vertex_quality_inference as fvqi

# Define the number of events to generate (in 4π)
N = 250

# Define the decay string using the same formatting as RapidSim
decay = "B+ -> { D0b ->  K+ e- anti-nue } pi+"

# Define the naming scheme for reconstructed particles, leaving missing particles as 'NA'
naming_scheme = "MOTHER -> { NA ->  DAUGHTER1 DAUGHTER2 NA } DAUGHTER3"

# Specify the EVTGEN model for each decay using the same format as the naming scheme
models = "PHSP -> { ISGW2 ->  PHSP PHSP PHSP } PHSP"

# Map the naming scheme to particle hypotheses for any misidentifications
mass_hypotheses = { 
    "DAUGHTER3": 'e+'
} 

# Set this to recompute masses/momenta of combined particles. If None, defaults to using all named particles to reconstruct the mother.
intermediate_particle = {
    "INTERMEDIATE": ["DAUGHTER2", "DAUGHTER3"]
}

# Run the Fast Vertexing Inference
fvqi.run(
    events=N, 
    decay=decay, 
    naming_scheme=naming_scheme, 
    decay_models=models, 
    mass_hypotheses=mass_hypotheses, 
    intermediate_particle=intermediate_particle, 
    dropMissing=True,
)
```



