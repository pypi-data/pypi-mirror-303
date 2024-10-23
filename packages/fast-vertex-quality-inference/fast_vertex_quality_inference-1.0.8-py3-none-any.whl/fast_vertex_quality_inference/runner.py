import fast_vertex_quality_inference.tools.globals as myGlobals
from fast_vertex_quality_inference.rapidsim.run_rapidsim import run_rapidsim
from fast_vertex_quality_inference.network.run_network import run_network
import fast_vertex_quality_inference.tools.display as display

import fast_vertex_quality_inference.params as p


def run_from_tuple(**kwargs):

    with p.execute_command(kwargs, p.fvqi_runFromTupleParameters) as params:

        combined_particles = {}
        combined_particles[params["mother_particle"]] = params["daughter_particles"]
        if params["intermediate_particle"] is not None:
            for intermediate_particle, daughters in params[
                "intermediate_particle"
            ].items():
                combined_particles[intermediate_particle] = daughters
            intermediate_particle_name = intermediate_particle

        # Run network with rapidsim output
        rapidsim_tuple_reco = run_network(
            params["file"],
            int(params["fully_reco"]),
            params["nPositive_missing_particles"],
            params["nNegative_missing_particles"],
            None,  # true_PID_scheme
            combined_particles,
            None,  # map_NA_codes, just dont use this
            False,  # dropMissing
            mother_particle_name=params["mother_particle"],
            intermediate_particle_name=intermediate_particle_name,
            daughter_particle_names=params["daughter_particles"],
            keep_tuple_structure=True,
            branch_naming_structure=params["branch_naming_structure"],
            stages=["run_vertexing"],  # dont run smearing networks
        )

        # Display timing and file information
        total_time = display.timings_table(only_vertexing=True)
        # myGlobals.global_print_my_decay_splash()
        display.print_file_info(rapidsim_tuple_reco, time=total_time)


def run(**kwargs):

    with p.execute_command(kwargs, p.fvqi_runParameters) as params:

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

        if params["only_rapidsim"]:
            total_time = display.timings_table(only_rapidsim=params["only_rapidsim"])
            display.print_file_info(rapidsim_tuple, time=total_time)
            return

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
