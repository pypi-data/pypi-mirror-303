import numpy as np
import uproot
import re
import pandas as pd
import fast_vertex_quality_inference.processing.transformers as tfs
import fast_vertex_quality_inference.processing.processing_tools as pts
from fast_vertex_quality_inference.rapidsim.rapidsim_tools import compute_combined_param

masses = {}
masses[321] = 493.677
masses[211] = 139.57039
masses[13] = 105.66
masses[11] = 0.51099895000  # * 1e-3
pid_list = [11, 13, 211, 321]


class tuple_manager:

    def map_branch_names(self):
        branch_names = list(self.tuple.keys())
        branch_names = [
            branch.replace(self.mother_particle_name, self.mother)
            for branch in branch_names
        ]
        if self.intermediate_particle_name:
            branch_names = [
                branch.replace(self.intermediate_particle_name, self.intermediate)
                for branch in branch_names
            ]
        temps = []
        for i in range(3):
            if (
                self.particles[i] in self.daughter_particle_names
                and self.particles[i] == self.daughter_particle_names[i]
            ):
                # all good - no need really even to replace
                replace_string = self.particles[i]
            else:
                replace_string = f"{self.particles[i][0]}_temp_{self.particles[i][1:]}"
                temps.append(i)
            branch_names = [
                branch.replace(self.daughter_particle_names[i], replace_string)
                for branch in branch_names
            ]
        for i in temps:
            replace_string = f"{self.particles[i][0]}_temp_{self.particles[i][1:]}"
            branch_names = [
                branch.replace(replace_string, self.particles[i])
                for branch in branch_names
            ]
        self.tuple.columns = branch_names

    def map_branch_names_list(self, branch_names):
        branch_names = [
            branch.replace(self.mother_particle_name, self.mother)
            for branch in branch_names
        ]
        if self.intermediate_particle_name:
            branch_names = [
                branch.replace(self.intermediate_particle_name, self.intermediate)
                for branch in branch_names
            ]
        temps = []
        for i in range(3):
            if (
                self.particles[i] in self.daughter_particle_names
                and self.particles[i] == self.daughter_particle_names[i]
            ):
                # all good - no need really even to replace
                replace_string = self.particles[i]
            else:
                replace_string = f"{self.particles[i][0]}_temp_{self.particles[i][1:]}"
                temps.append(i)
            branch_names = [
                branch.replace(self.daughter_particle_names[i], replace_string)
                for branch in branch_names
            ]
        for i in temps:
            replace_string = f"{self.particles[i][0]}_temp_{self.particles[i][1:]}"
            branch_names = [
                branch.replace(replace_string, self.particles[i])
                for branch in branch_names
            ]
        return branch_names

    def smearelectronE(self, E_smearing_output, particle):
        for column in E_smearing_output.columns:
            dim = column[-1]
            self.tuple[f"{particle}_P{dim}"] = (
                E_smearing_output[column]
                * (self.tuple[f"{particle}_P{dim}_TRUE"] + 1e-4)
            ) + self.tuple[f"{particle}_P{dim}_TRUE"]

    def recompute_combined_particles(self, combined_particles):

        # Recompute variables of reconstructed particles

        for combined_particle in combined_particles:
            particle_daughters = combined_particles[combined_particle]
            daughter_info = {}
            for daughter in particle_daughters:
                daughter_info[daughter] = {}
                for param in ["M", "PX", "PY", "PZ"]:
                    daughter_info[daughter][param] = self.tuple[f"{daughter}_{param}"]
            for param in ["M", "PX", "PY", "PZ"]:
                self.tuple[f"{combined_particle}_{param}"] = compute_combined_param(
                    daughter_info, param
                )
            self.tuple[f"{combined_particle}_P"] = np.sqrt(
                self.tuple[f"{combined_particle}_PX"] ** 2
                + self.tuple[f"{combined_particle}_PY"] ** 2
                + self.tuple[f"{combined_particle}_PZ"] ** 2
            )
            self.tuple[f"{combined_particle}_PT"] = np.sqrt(
                self.tuple[f"{combined_particle}_PX"] ** 2
                + self.tuple[f"{combined_particle}_PY"] ** 2
            )

    def recompute_reconstructed_mass(self):

        df = self.tuple

        i = self.particles[0]
        j = self.particles[1]
        k = self.particles[2]

        PE = (
            np.sqrt(
                df[f"{i}_M"] ** 2
                + df[f"{i}_PX"] ** 2
                + df[f"{i}_PY"] ** 2
                + df[f"{i}_PZ"] ** 2
            )
            + np.sqrt(
                df[f"{j}_M"] ** 2
                + df[f"{j}_PX"] ** 2
                + df[f"{j}_PY"] ** 2
                + df[f"{j}_PZ"] ** 2
            )
            + np.sqrt(
                df[f"{k}_M"] ** 2
                + df[f"{k}_PX"] ** 2
                + df[f"{k}_PY"] ** 2
                + df[f"{k}_PZ"] ** 2
            )
        )
        PX = df[f"{i}_PX"] + df[f"{j}_PX"] + df[f"{k}_PX"]
        PY = df[f"{i}_PY"] + df[f"{j}_PY"] + df[f"{k}_PY"]
        PZ = df[f"{i}_PZ"] + df[f"{j}_PZ"] + df[f"{k}_PZ"]

        mass = np.sqrt((PE**2 - PX**2 - PY**2 - PZ**2))

        return mass

    def __init__(
        self,
        tuple_location,
        fully_reco,
        nPositive_missing_particles,
        nNegative_missing_particles,
        mother_particle_name,
        intermediate_particle_name,  # make this optional
        daughter_particle_names,
        combined_particles,
        tree="DecayTree",
        entry_stop=None,
        branch_naming_structure=None,
    ):

        self.particles = ["DAUGHTER1", "DAUGHTER2", "DAUGHTER3"]

        swap_map = {
            user_name: network_name
            for network_name, user_name in zip(self.particles, daughter_particle_names)
        }
        if intermediate_particle_name in combined_particles:
            self.particles = []
            intermediate_recipe = combined_particles[intermediate_particle_name]
            new_order = [
                particle
                for particle in daughter_particle_names
                if particle not in intermediate_recipe
            ] + intermediate_recipe
            self.particles = [swap_map[particle] for particle in new_order]

        self.mother = "MOTHER"
        self.intermediate = "INTERMEDIATE"
        self.fully_reco = fully_reco
        self.nPositive_missing_particles = nPositive_missing_particles
        self.nNegative_missing_particles = nNegative_missing_particles

        self.mother_particle_name = mother_particle_name
        self.intermediate_particle_name = intermediate_particle_name
        self.daughter_particle_names = daughter_particle_names

        self.tree = tree
        self.tuple_location = tuple_location

        self.raw_tuple = uproot.open(self.tuple_location)[self.tree]

        list_of_branches = list(self.raw_tuple.keys())
        list_of_branches = [
            branch for branch in list_of_branches if "COV" not in branch
        ]

        if entry_stop:
            arrays = self.raw_tuple.arrays(
                list_of_branches, library="np", entry_stop=entry_stop
            )
            self.tuple = pd.DataFrame(arrays)
        else:
            arrays = self.raw_tuple.arrays(list_of_branches, library="np")
            self.tuple = pd.DataFrame(arrays)

        # IF BRANCH STRUCTURE DIFFERENT CONVERT TO RAPIDSIM CONVENTION
        self.branch_naming_structure = branch_naming_structure
        if self.branch_naming_structure:
            self.convert_branch_aliases(self.branch_naming_structure, to_rapidsim=True)

        self.map_branch_names()

        self.list_of_particles = []
        tag_to_find_particle_names = "origX_TRUE"
        for branch in self.tuple:
            if tag_to_find_particle_names in branch:
                self.list_of_particles.append(
                    branch.replace(f"_{tag_to_find_particle_names}", "")
                )

        self.original_branches = list(self.tuple.keys())

        self.tuple[f"{self.mother}_M"] = self.recompute_reconstructed_mass()

    def convert_branch_aliases(
        self, branch_naming_structures, to_rapidsim, specific_tuple=None
    ):

        rapidsim_conventions = {}

        rapidsim_conventions["momenta_component"] = "{particle}_P"
        rapidsim_conventions["true_momenta_component"] = "{particle}_P_TRUE"

        rapidsim_conventions["momenta_component"] = "{particle}_P{dim}"
        rapidsim_conventions["true_momenta_component"] = "{particle}_P{dim}_TRUE"

        rapidsim_conventions["pid"] = "{particle}_ID"
        rapidsim_conventions["true_pid"] = "{particle}_ID_TRUE"

        rapidsim_conventions["mass"] = "{particle}_M"
        rapidsim_conventions["true_mass"] = "{particle}_M_TRUE"

        rapidsim_conventions["origin"] = "{particle}_orig{dim}"
        rapidsim_conventions["true_origin"] = "{particle}_orig{dim}_TRUE"

        rapidsim_conventions["vertex"] = "{particle}_vtx{dim}"
        rapidsim_conventions["true_vertex"] = "{particle}_vtx{dim}_TRUE"

        if specific_tuple is not None:
            tuple_to_update = specific_tuple
        else:
            tuple_to_update = self.tuple

        if to_rapidsim:
            new_branches = []

            for branch in tuple_to_update:

                for (
                    branch_naming_structure,
                    pattern,
                ) in branch_naming_structures.items():

                    regex_pattern = pattern.replace(
                        "{particle}", r"(?P<particle>\w+)"
                    ).replace(
                        "{dim}", r"(?P<dim>\w)"
                    )  # Only a single character for {dim}
                    match = re.match(regex_pattern, branch)

                    if match:
                        particle = match.group("particle")
                        dim = match.group("dim")
                        updated_branch = rapidsim_conventions[
                            branch_naming_structure
                        ].format(particle=particle, dim=dim)
                        new_branches.append(updated_branch)
                    else:
                        new_branches.append(branch)

            tuple_to_update.columns = new_branches

        else:

            new_branches = []

            for branch in tuple_to_update:

                for (
                    branch_naming_structure,
                    custom_pattern,
                ) in branch_naming_structures.items():

                    pattern = rapidsim_conventions[branch_naming_structure]

                    regex_pattern = pattern.replace(
                        "{particle}", r"(?P<particle>\w+)"
                    ).replace(
                        "{dim}", r"(?P<dim>\w)"
                    )  # Only a single character for {dim}
                    match = re.match(regex_pattern, branch)

                    if match:
                        particle = match.group("particle")
                        dim = match.group("dim")
                        updated_branch = custom_pattern.format(
                            particle=particle, dim=dim
                        )
                        new_branches.append(updated_branch)
                    else:
                        new_branches.append(branch)

            tuple_to_update.columns = new_branches

    def write(
        self,
        new_branches_to_keep,
        output_location=None,
        keep_vertex_info=False,
        keep_tuple_structure=False,
    ):

        branches = self.original_branches + new_branches_to_keep

        if not keep_tuple_structure:
            # re-name columns
            branch_swaps = {}
            branch_swaps[self.mother] = self.mother_particle_name
            if self.intermediate_particle_name:
                branch_swaps[self.intermediate] = self.intermediate_particle_name
            branch_swaps[self.particles[0]] = self.daughter_particle_names[0]
            branch_swaps[self.particles[1]] = self.daughter_particle_names[1]
            branch_swaps[self.particles[2]] = self.daughter_particle_names[2]
            # add rest to list - will only be others if dropMissing=False
            named_particles = [self.mother] + [self.intermediate] + self.particles
            unnamed_particles = list(set(self.list_of_particles) - set(named_particles))
            for unnamed_particle in unnamed_particles:
                branch_swaps[unnamed_particle] = unnamed_particle

        tuple_to_write = self.tuple[branches]

        if not keep_tuple_structure:
            columns = list(tuple_to_write.columns)
            new_columns = []
            for column in columns:
                for to_swap in list(branch_swaps.keys()):
                    if column[: len(to_swap)] == to_swap:
                        new_columns.append(
                            column.replace(to_swap, branch_swaps[to_swap])
                        )
                        break

            # drop columns that might hang on but are not related to an individual particle, MCorr and nEvent for example
            drop_list = []
            for i in tuple_to_write.columns:
                # if i not in new_columns:
                if not any(s in i for s in list(branch_swaps.keys())):
                    drop_list.append(i)
            tuple_to_write = tuple_to_write.drop(drop_list, axis=1)

            tuple_to_write.columns = new_columns

            if not keep_vertex_info:
                for dim in ["X", "Y", "Z"]:
                    tuple_to_write = tuple_to_write.drop(
                        columns=[
                            col for col in tuple_to_write.columns if f"_vtx{dim}" in col
                        ]
                    )
                    tuple_to_write = tuple_to_write.drop(
                        columns=[
                            col
                            for col in tuple_to_write.columns
                            if f"_orig{dim}" in col
                        ]
                    )

            # re-order columns
            columns = tuple_to_write.columns
            if self.intermediate_particle_name:
                prefix_order = [
                    self.mother_particle_name,
                    self.intermediate_particle_name,
                    self.daughter_particle_names[0],
                    self.daughter_particle_names[1],
                    self.daughter_particle_names[2],
                ]
            else:
                prefix_order = [
                    self.mother_particle_name,
                    self.daughter_particle_names[0],
                    self.daughter_particle_names[1],
                    self.daughter_particle_names[2],
                ]

            for unnamed_particle in unnamed_particles:
                prefix_order.append(unnamed_particle)

            ordered_columns = []
            for prefix in prefix_order:
                cols_with_prefix = [col for col in columns if col.startswith(prefix)]
                ordered_columns.extend(cols_with_prefix)
            tuple_to_write = tuple_to_write[ordered_columns]

        if self.branch_naming_structure:
            self.convert_branch_aliases(
                self.branch_naming_structure,
                to_rapidsim=False,
                specific_tuple=tuple_to_write,
            )

        if not output_location:
            output_location = f"{self.tuple_location[:-5]}_reco.root"
        pts.write_df_to_root(tuple_to_write, output_location, self.tree)
        return output_location

    def add_branches(self, data_to_add):
        new_dataframes = []
        for branch in list(data_to_add.keys()):
            new_dataframes.append(pd.DataFrame({branch: data_to_add[branch]}))
        new_frame = pd.concat(new_dataframes, axis=1)
        self.tuple = pd.concat([self.tuple, new_frame], axis=1)

    def get_branches(
        self,
        branches,
        transformers=None,
        numpy=False,
        scale_factor=1.0,
        transform_by_index=False,
    ):
        data = self.tuple[branches] * scale_factor

        if transformers:

            data = tfs.transform_df(
                data, transformers, transform_by_index=transform_by_index
            )

        if numpy:
            data = np.asarray(data[branches])

        return data

    def smearPV(self, smeared_PV_output):

        # print("Need to implement function to move the origin vertex too")

        distance_buffer = {}
        for particle in self.particles:
            for coordinate in ["X", "Y", "Z"]:
                distance_buffer[f"{particle}_{coordinate}"] = np.asarray(
                    self.tuple[f"{particle}_orig{coordinate}_TRUE"]
                    - self.tuple[f"{self.mother}_vtx{coordinate}_TRUE"]
                )

        B_plus_TRUEORIGINVERTEX = [
            self.tuple[f"{self.mother}_origX_TRUE"],
            self.tuple[f"{self.mother}_origY_TRUE"],
            self.tuple[f"{self.mother}_origZ_TRUE"],
        ]
        B_plus_TRUEENDVERTEX = [
            self.tuple[f"{self.mother}_vtxX_TRUE"],
            self.tuple[f"{self.mother}_vtxY_TRUE"],
            self.tuple[f"{self.mother}_vtxZ_TRUE"],
        ]
        theta, phi = pts.compute_angles(B_plus_TRUEORIGINVERTEX, B_plus_TRUEENDVERTEX)

        for branch in list(smeared_PV_output.keys()):
            self.tuple[branch] = smeared_PV_output[branch]

        B_plus_TRUEORIGINVERTEX = [
            self.tuple[f"{self.mother}_origX_TRUE"],
            self.tuple[f"{self.mother}_origY_TRUE"],
            self.tuple[f"{self.mother}_origZ_TRUE"],
        ]
        (
            self.tuple[f"{self.mother}_vtxX_TRUE"],
            self.tuple[f"{self.mother}_vtxY_TRUE"],
            self.tuple[f"{self.mother}_vtxZ_TRUE"],
        ) = pts.redefine_endpoint(
            B_plus_TRUEORIGINVERTEX, theta, phi, self.tuple[f"{self.mother}_TRUE_FD"]
        )

        for particle in self.particles:
            for coordinate in ["X", "Y", "Z"]:
                self.tuple[f"{particle}_orig{coordinate}_TRUE"] = (
                    self.tuple[f"{self.mother}_vtx{coordinate}_TRUE"]
                    + distance_buffer[f"{particle}_{coordinate}"]
                )

    def append_conditional_information(self):

        for idx, particle in enumerate(self.particles):
            # self.tuple[f'{particle}_TRUEID'] = self.particles_TRUEID[idx]
            self.tuple[f"{particle}_TRUEID"] = self.tuple[f"{particle}_ID_TRUE"]

            mass = np.asarray(self.tuple[f"{particle}_TRUEID"]).astype("float32")
            for pid in pid_list:
                mass[np.where(np.abs(mass) == pid)] = masses[pid]
            self.tuple[f"{particle}_mass"] = mass

        self.tuple[f"{self.mother}_FLIGHT"] = pts.compute_distance_wrapped(
            self.tuple, self.mother, "vtx", self.mother, "orig"
        )
        self.tuple[f"{self.particles[0]}_FLIGHT"] = pts.compute_distance_wrapped(
            self.tuple, self.particles[0], "orig", self.mother, "vtx"
        )
        self.tuple[f"{self.particles[1]}_FLIGHT"] = pts.compute_distance_wrapped(
            self.tuple, self.particles[1], "orig", self.mother, "vtx"
        )
        self.tuple[f"{self.particles[2]}_FLIGHT"] = pts.compute_distance_wrapped(
            self.tuple, self.particles[2], "orig", self.mother, "vtx"
        )

        self.tuple[f"{self.mother}_P"], self.tuple[f"{self.mother}_PT"] = (
            pts.compute_reconstructed_mother_momenta(self.tuple, self.mother)
        )

        self.tuple[f"{self.intermediate}_P"], self.tuple[f"{self.intermediate}_PT"] = (
            pts.compute_reconstructed_intermediate_momenta(
                self.tuple, [self.particles[1], self.particles[2]]
            )
        )

        (
            self.tuple[f"missing_{self.mother}_P"],
            self.tuple[f"missing_{self.mother}_PT"],
        ) = pts.compute_missing_momentum(self.tuple, self.mother, self.particles)
        (
            self.tuple[f"missing_{self.intermediate}_P"],
            self.tuple[f"missing_{self.intermediate}_PT"],
        ) = pts.compute_missing_momentum(
            self.tuple, self.mother, [self.particles[1], self.particles[2]]
        )

        for particle_i in range(0, len(self.particles)):
            (
                self.tuple[f"delta_{particle_i}_P"],
                self.tuple[f"delta_{particle_i}_PT"],
            ) = pts.compute_reconstructed_momentum_residual(
                self.tuple, self.particles[particle_i]
            )

        for particle in self.particles:
            self.tuple[f"angle_{particle}"] = pts.compute_angle(
                self.tuple, self.mother, f"{particle}"
            )

        self.tuple[f"IP_{self.mother}_true_vertex"] = pts.compute_impactParameter(
            self.tuple, self.mother, self.particles
        )
        for particle in self.particles:
            self.tuple[f"IP_{particle}_true_vertex"] = pts.compute_impactParameter_i(
                self.tuple, self.mother, f"{particle}"
            )
        self.tuple[f"FD_{self.mother}_true_vertex"] = pts.compute_flightDistance(
            self.tuple, self.mother, self.particles
        )
        self.tuple[f"DIRA_{self.mother}_true_vertex"] = pts.compute_DIRA(
            self.tuple, self.mother, self.particles
        )

        if self.fully_reco:
            self.tuple["fully_reco"] = 1.0
        else:
            self.tuple["fully_reco"] = 0.0

        self.tuple[f"{self.mother}_nPositive_missing"] = float(
            self.nPositive_missing_particles
        )
        self.tuple[f"{self.mother}_nNegative_missing"] = float(
            self.nPositive_missing_particles
        )

        for particle in self.particles:
            self.tuple[f"{particle}_eta"] = -np.log(
                np.tan(
                    np.arcsin(
                        self.tuple[f"{particle}_PT"] / self.tuple[f"{particle}_P"]
                    )
                    / 2.0
                )
            )
