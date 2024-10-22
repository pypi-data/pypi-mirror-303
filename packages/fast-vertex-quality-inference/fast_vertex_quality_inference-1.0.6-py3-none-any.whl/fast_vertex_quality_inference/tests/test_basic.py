import fast_vertex_quality_inference as fvqi

N = 10


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
