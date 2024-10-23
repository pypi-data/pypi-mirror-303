import fast_vertex_quality_inference as fvqi
import uproot

N = 250


def test_basic():
    fvqi.run(
        events=N,
        decay="B+ -> { D0b -> K+ e- anti-nue } pi+",
        naming_scheme="MOTHER -> { NA -> DAUGHTER1 DAUGHTER3 NA } DAUGHTER2",
        decay_models="PHSP -> { ISGW2 -> PHSP PHSP PHSP } PHSP",
        mass_hypotheses={"DAUGHTER2": "e+"},
        intermediate_particle={"INTERMEDIATE": ["DAUGHTER2", "DAUGHTER3"]},
        dropMissing=True,
    )


def test_no_intermediate():
    fvqi.run(
        events=N,
        decay="B+ -> { D0b -> K+ e- anti-nue } pi+",
        naming_scheme="MOTHER -> { NA -> DAUGHTER1 DAUGHTER3 NA } DAUGHTER2",
        decay_models="PHSP -> { ISGW2 -> PHSP PHSP PHSP } PHSP",
        mass_hypotheses={"DAUGHTER2": "e+"},
        intermediate_particle=None,
        dropMissing=True,
    )


def test_naming():
    fvqi.run(
        events=N,
        decay="B+ -> K+ e+ e-",
        naming_scheme="B_plus -> K_plus e_plus e_minus",
        decay_models="BTOSLLBALL_6 -> PHSP PHSP PHSP",
        mass_hypotheses=None,
        intermediate_particle={"INTERMEDIATE": ["e_plus", "e_minus"]},
        dropMissing=True,
    )


def test_swap_intermediates():
    fvqi.run(
        events=N,
        decay="B+ -> K+ e+ e-",
        naming_scheme="B_plus -> K_plus e_plus e_minus",
        decay_models="BTOSLLBALL_6 -> PHSP PHSP PHSP",
        mass_hypotheses=None,
        intermediate_particle={"INTERMEDIATE": ["K_plus", "e_minus"]},
        dropMissing=True,
    )


def test_dropMissing_False():
    fvqi.run(
        events=N,
        decay="B+ -> K+ e+ e-",
        naming_scheme="B_plus -> K_plus e_plus e_minus",
        decay_models="BTOSLLBALL_6 -> PHSP PHSP PHSP",
        mass_hypotheses=None,
        intermediate_particle={"INTERMEDIATE": ["K_plus", "e_minus"]},
        dropMissing=False,
    )


def test_run_from_tuple():

    fvqi.run(
        events=N,
        decay="B+ -> { D0b -> K+ e- anti-nue } pi+",
        naming_scheme="MOTHER -> { NA -> DAUGHTER1 DAUGHTER3 NA } DAUGHTER2",
        decay_models="PHSP -> { ISGW2 -> PHSP PHSP PHSP } PHSP",
        mass_hypotheses={"DAUGHTER2": "e+"},
        intermediate_particle={"INTERMEDIATE": ["DAUGHTER2", "DAUGHTER3"]},
        dropMissing=True,
        only_rapidsim=True,
    )

    # change some branch structure
    # change '{particle}_P{dim}_TRUE'
    # to '{particle}_TRUE_P{dim}'
    rapidsim_tuple = uproot.open("decay_tree.root")["DecayTree"]
    arrays = rapidsim_tuple.arrays(library="np")
    new_arrays = {}
    for key in arrays:
        if any(substring in key for substring in ["PX_TRUE", "PY_TRUE", "PZ_TRUE"]):
            dim = key.split("_")[-2][1]
            new_arrays[key.replace(f"P{dim}_TRUE", f"TRUE_P{dim}")] = arrays[key]
        else:
            new_arrays[key] = arrays[key]
    with uproot.recreate("decay_tree_modified.root") as new_file:
        new_file["DecayTree"] = new_arrays

    fvqi.run_from_tuple(
        file="decay_tree_modified.root",
        mother_particle="MOTHER",
        daughter_particles=["DAUGHTER1", "DAUGHTER2", "DAUGHTER3"],
        fully_reco=False,
        nPositive_missing_particles=0,
        nNegative_missing_particles=0,
        mass_hypotheses={"DAUGHTER2": "e+"},
        intermediate_particle={"INTERMEDIATE": ["DAUGHTER2", "DAUGHTER3"]},
        branch_naming_structure={"true_momenta_component": "{particle}_TRUE_P{dim}"},
    )
