import fast_vertex_quality_inference.tools.globals as myGlobals

from fast_vertex_quality_inference.processing.data_manager import tuple_manager
from fast_vertex_quality_inference.processing.network_manager import network_manager
import fast_vertex_quality_inference.tools.display as display
from pathlib import Path
import os
import re


def remove_file(file):
    if Path(file).is_file():
        os.system(f"rm {file}")


def run_network(
    rapidsim_tuple,
    fully_reco,
    nPositive_missing_particles,
    nNegative_missing_particles,
    true_PID_scheme,
    combined_particles,
    map_NA_codes,
    dropMissing,
    mother_particle_name,
    intermediate_particle_name,
    daughter_particle_names,
    keep_tuple_structure=False,  # just append to existing file
    branch_naming_structure=None,
    stages=["smear_PV", "smear_electrons"],
):

    re_smear_electrons = True
    keep_vertex_info = False

    myGlobals.stopwatches.click("Networks - config")
    with display.status_execution(
        status_message="[bold green]Initialising networks...",
        complete_message="[bold green]Networks initialised :white_check_mark:",
    ):

        if "smear_PV" in stages:
            with display.log_execution("Initialising smearing network"):
                rapidsim_PV_smearing_network = network_manager(
                    network=f"{myGlobals.MODELS_PATH}smearing_decoder_model.onnx",
                    config=f"{myGlobals.MODELS_PATH}smearing_configs.pkl",
                    # transformers=f"{myGlobals.MODELS_PATH}smearing_transfomers.pkl",
                    transformers=f"{myGlobals.MODELS_PATH}smearing_transfomer_quantiles.pkl",
                )
        if "smear_electrons" in stages:
            if any(
                value in (11, -11) for value in true_PID_scheme.values()
            ):  # electrons present
                with display.log_execution("Initialising electron smearing network"):
                    electron_smearing_network = network_manager(
                        network=f"{myGlobals.MODELS_PATH}E_smearing_generator_model.onnx",
                        config=f"{myGlobals.MODELS_PATH}E_smearing_configs.pkl",
                        # transformers=f"{myGlobals.MODELS_PATH}E_smearing_transfomers.pkl",
                        transformers=f"{myGlobals.MODELS_PATH}E_smearing_transfomer_quantiles.pkl",
                    )
        with display.log_execution("Initialising vertexing network"):
            vertexing_network = network_manager(
                network=f"{myGlobals.MODELS_PATH}vertexing_decoder_model.onnx",
                config=f"{myGlobals.MODELS_PATH}vertexing_configs.pkl",
                # transformers=f"{myGlobals.MODELS_PATH}vertexing_transfomers.pkl",
                transformers=f"{myGlobals.MODELS_PATH}vertexing_transfomer_quantiles.pkl",
            )

    myGlobals.stopwatches.click("Networks - config")

    myGlobals.stopwatches.click("Networks - processing")
    with display.status_execution(
        status_message="[bold green]Staging RapidSim tuple...",
        complete_message="[bold green]RapidSim tuple staged :white_check_mark:",
    ):

        ####
        # LOAD RAPIDSIM TUPLE
        ###

        with display.log_execution("Reading RapidSim tuple"):
            data_tuple = tuple_manager(
                tuple_location=rapidsim_tuple,
                fully_reco=fully_reco,
                nPositive_missing_particles=nPositive_missing_particles,
                nNegative_missing_particles=nNegative_missing_particles,
                mother_particle_name=mother_particle_name,
                intermediate_particle_name=intermediate_particle_name,
                daughter_particle_names=daughter_particle_names,
                combined_particles=combined_particles,
                branch_naming_structure=branch_naming_structure,
            )
    myGlobals.stopwatches.click("Networks - processing")

    ####
    # SMEAR PV
    ###
    if "smear_PV" in stages:
        with display.status_execution(
            status_message="[bold green]Smearing primary vertex...",
            complete_message="[bold green]Primary vertex smeared :white_check_mark:",
        ):

            myGlobals.stopwatches.click("Networks - processing")
            with display.log_execution("Computing conditional variables"):
                smearing_conditions = data_tuple.get_branches(
                    rapidsim_PV_smearing_network.conditions,
                    rapidsim_PV_smearing_network.Transformers,
                    numpy=True,
                )
            myGlobals.stopwatches.click("Networks - processing")

            myGlobals.stopwatches.click("Networks - generation")
            with display.log_execution("Querying network"):
                smeared_PV_output = rapidsim_PV_smearing_network.query_network(
                    ["noise", smearing_conditions],
                )
            myGlobals.stopwatches.click("Networks - generation")

            myGlobals.stopwatches.click("Networks - processing")
            with display.log_execution("Applying smearing"):
                data_tuple.smearPV(smeared_PV_output)
            myGlobals.stopwatches.click("Networks - processing")

    # ####
    # # SMEAR ELECTRONS
    # ###
    if "smear_electrons" in stages:
        if re_smear_electrons:
            for particle in true_PID_scheme:
                if true_PID_scheme[particle] in (11, -11):

                    if dropMissing and (
                        re.match(r"^NA_\d{8}$", particle) or particle == "NA"
                    ):
                        continue

                    if re.match(r"^NA_\d{8}$", particle) or particle == "NA":
                        particle = map_NA_codes[particle]

                    with display.status_execution(
                        status_message=f"[bold green]Manually smearing electron momenta ({particle})...",
                        complete_message=f"[bold green]{particle} momenta smeared :white_check_mark:",
                    ):

                        mapped_particle = data_tuple.map_branch_names_list([particle])[
                            0
                        ]

                        new_conditions = list(electron_smearing_network.conditions)
                        new_conditions = [
                            condition.replace("DAUGHTER3", mapped_particle)
                            for condition in new_conditions
                        ]

                        relevant_electron_smearing_network_Transformers = {
                            "DAUGHTER3_PX_TRUE": electron_smearing_network.Transformers[
                                "DAUGHTER3_PX_TRUE"
                            ],
                            "DAUGHTER3_PY_TRUE": electron_smearing_network.Transformers[
                                "DAUGHTER3_PY_TRUE"
                            ],
                            "DAUGHTER3_PZ_TRUE": electron_smearing_network.Transformers[
                                "DAUGHTER3_PZ_TRUE"
                            ],
                        }

                        myGlobals.stopwatches.click("Networks - processing")
                        with display.log_execution("Computing conditional variables"):
                            E_smearing_conditions = data_tuple.get_branches(
                                new_conditions,
                                relevant_electron_smearing_network_Transformers,
                                numpy=True,
                                transform_by_index=True,
                            )
                        myGlobals.stopwatches.click("Networks - processing")

                        myGlobals.stopwatches.click("Networks - generation")
                        with display.log_execution("Querying network"):
                            E_smearing_output = electron_smearing_network.query_network(
                                ["noise", E_smearing_conditions],
                            )

                            new_columns = list(E_smearing_output.columns)
                            new_columns = [
                                column.replace("DAUGHTER3", mapped_particle)
                                for column in new_columns
                            ]
                            E_smearing_output.columns = new_columns

                        myGlobals.stopwatches.click("Networks - generation")

                        myGlobals.stopwatches.click("Networks - processing")
                        with display.log_execution("Applying smearing"):
                            data_tuple.smearelectronE(
                                E_smearing_output, mapped_particle
                            )
                    myGlobals.stopwatches.click("Networks - processing")

            if any(
                value in (11, -11) for value in true_PID_scheme.values()
            ):  # electrons present
                # re compute combined particles
                mapped_combined_particles = {}
                for key in combined_particles:
                    mapped_mother = data_tuple.map_branch_names_list([key])[0]
                    mapped_combined_particles[mapped_mother] = [
                        data_tuple.map_branch_names_list([d])[0]
                        for d in list(combined_particles[key])
                    ]
                data_tuple.recompute_combined_particles(mapped_combined_particles)

    ####
    # COMPUTE CONDITIONS AND RUN VERTEXING NETWORK
    ###
    with display.status_execution(
        status_message="[bold green]Running vertexing...",
        complete_message="[bold green]Vertexing complete :white_check_mark:",
    ):

        myGlobals.stopwatches.click("Networks - processing")
        with display.log_execution("Computing conditional variables"):
            data_tuple.append_conditional_information()
            vertexing_conditions = data_tuple.get_branches(
                vertexing_network.conditions,
                vertexing_network.Transformers,
                numpy=True,
            )
        myGlobals.stopwatches.click("Networks - processing")

        myGlobals.stopwatches.click("Networks - generation")
        with display.log_execution("Querying network"):
            vertexing_output = vertexing_network.query_network(
                ["noise", vertexing_conditions],
            )
        myGlobals.stopwatches.click("Networks - generation")

        myGlobals.stopwatches.click("Networks - processing")
        with display.log_execution("Appending new branches"):
            data_tuple.add_branches(vertexing_output)

            ####
            # WRITE TUPLE
            ###

            output_location = data_tuple.write(
                new_branches_to_keep=vertexing_network.targets,
                keep_vertex_info=keep_vertex_info,
                keep_tuple_structure=keep_tuple_structure,
            )
        myGlobals.stopwatches.click("Networks - processing")

    if not keep_tuple_structure:
        remove_file(rapidsim_tuple)

    return output_location
