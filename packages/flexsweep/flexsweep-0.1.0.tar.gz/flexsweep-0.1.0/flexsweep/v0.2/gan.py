import stdpopsim
import msprime
import demes
import numpy as np
import pandas as pd
import scipy.integrate as integrate
import pickle
import signal
import itertools
import warnings
import logging
import os
import glob
import shutil

from scipy.interpolate import interp1d
from mpmath import exp
from contextlib import redirect_stdout
from functools import partial
from itertools import product, chain
from copy import deepcopy
from dataclasses import dataclass, field
from tqdm import tqdm

from collections import defaultdict, namedtuple
from joblib import Parallel, delayed


warnings.simplefilter(action="ignore", category=stdpopsim.SLiMScalingFactorWarning)
warnings.simplefilter(action="ignore", category=msprime.TimeUnitsMismatchWarning)


def frequency(ts, position):
    pos = ts.sites_position
    g = ts.genotype_matrix()[np.where(pos == position)[0]]

    if np.any(g == 2):
        g[g == 2] = 0

    freq = g.sum() / (ts.num_individuals * 2)

    return freq


@dataclass
class parameters:
    """
    Create a class container to automatize sweep simulations using stdpopsim.
    """

    specie: str
    region: str
    genetic_map: str
    dfe: str
    demes: str
    sample: dict
    sweep_class: str
    contig: stdpopsim.genomes.Contig = None
    model: stdpopsim.models = None
    slim_region: dict = None
    recombination_map: pd.DataFrame = None
    annotation: str = "exons"
    f_i: list = field(default_factory=lambda: [0.05, 0.1, 0.15, 0.2])
    f_t: list = field(default_factory=lambda: np.arange(0.2, 1.1, 0.1))
    del_dfe: dict = field(default_factory=lambda: {"mean_strength": 0, "shape": 0})
    proportions: list = field(default_factory=lambda: [0, 0])
    burn_in: int = 1
    rescale_factor: int = 1
    dominance: float = 0.5
    Ne: int = (1e4,)
    sweep_diffusion_time: list = field(default_factory=lambda: {"hard": {}, "soft": {}})

    def diffusion_time_value(self, N, s, f_i, f_t, c=2) -> float:
        """
        Calculate diffusion time value.

        Args:
        - N: Population size.
        - s: Selection coefficient.
        - f_i: Initial frequency.
        - f_t: Target frequency.
        - c: Constant value (default is 2).

        Returns:
        - float: Calculated diffusion time value.
        """
        _N = 2 * N
        s = s / _N
        result = integrate.quad(
            lambda x: (
                (exp(2 * c * _N * s * x) - 1) * (exp(2 * c * _N * s * (1 - x)) - 1)
            )
            / (s * x * (1 - x) * (exp(2 * c * _N * s) - 1)),
            f_i,
            f_t,
        )
        return result[0]

    def diffusion_time(self, N: int, nthreads: int):
        """
        Calculate diffusion time.

        Args:
        - N: Population size (integer).

        Returns:
        - None: The function updates the class variable `sweep_diffusion_time`.
        """
        current_sweep = self.sweep_class

        # Check if diffusion mean time is already estimated for current sweep
        if (
            len(self.sweep_diffusion_time[current_sweep]) != 0
            and list(self.sweep_diffusion_time[current_sweep].keys()) == self.f_t
        ):
            print("Diffusion mean time is estimated")
        else:
            func = np.vectorize(self.diffusion_time_value)
            s_v = np.arange(10, 2001, 1)  # Create range of selection coefficients

            if self.sweep_class == "hard":
                # For hard sweep, calculate diffusion times for given f_t values
                t_fix = Parallel(n_jobs=nthreads, backend="multiprocessing", verbose=0)(
                    delayed(func)(N, s_v, 1 / (2 * N), i) for i in self.f_t
                )
                for i, v in enumerate(self.f_t):
                    s_t = np.vstack([s_v, t_fix[i]]).T.astype(int)
                    self.sweep_diffusion_time[current_sweep][round(v, 2)] = s_t

                # for i in self.f_t:
                #     t_fix = func(N, s_v, 1 / (2 * N), i).astype(int)
                #     s_t = np.vstack([s_v, t_fix]).T
                #     self.sweep_diffusion_time[current_sweep][round(i, 2)] = s_t

            elif self.sweep_class == "soft":
                # For soft sweep, calculate diffusion times for combinations of f_t and f_i
                iterables = np.array(list(product(self.f_t, self.f_i)))
                iterables = iterables[iterables[:, 1] < iterables[:, 0]]

                t_fix = Parallel(n_jobs=nthreads, backend="multiprocessing", verbose=0)(
                    delayed(func)(N, s_v, start, end) for (end, start) in iterables
                )

                for i, (end, start) in enumerate(iterables):
                    # for end, start in iterables:
                    # t_fix = func(N, s_v, start, end).astype(int)
                    s_t = np.vstack([s_v, t_fix[i]]).T.astype(int)

                    # Update sweep_diffusion_time for each combination
                    if round(end, 1) not in self.sweep_diffusion_time[current_sweep]:
                        self.sweep_diffusion_time[current_sweep][round(end, 1)] = {}
                        self.sweep_diffusion_time[current_sweep][round(end, 1)].update(
                            {start: s_t}
                        )
                    else:
                        self.sweep_diffusion_time[current_sweep][round(end, 1)].update(
                            {start: s_t}
                        )

    def check_stdpopsim(self, return_df: bool = True):
        """
        Check stdpopsim species and associated annotation, DFE, and demographic model.

        Args:
        - return_df: Boolean indicating whether to return results as a DataFrame (default is True).

        Returns:
        - dict or DataFrame: Information about stdpopsim species, models, genetic maps, and dfes.
        """
        out = {}

        # Iterate over all species in stdpopsim
        for i in stdpopsim.all_species():
            tmp_specie = stdpopsim.get_species(i.id)

            # Collect models, genetic maps, and dfes for each species
            tmptmp_parameters.models = ", ".join(
                [i.id for i in tmp_specie.demographictmp_parameters.models]
            )
            tmp_dfes = ", ".join(
                [i.id for i in tmp_specie.demographictmp_parameters.models]
            )
            tmp_genetic_maps = ", ".join([i.id for i in tmp_specie.genetic_maps])

            # Store collected information for each species in 'out'
            out[i.id] = {
                "models": tmptmp_parameters.models,
                "genetic_maps": tmp_genetic_maps,
                "dfes": tmp_dfes,
            }

        # Print information about stdpopsim species
        print(
            "\n\nPlease check the available species and the associated annotation, DFE, and demographic model\n"
        )

        # Return the collected information as a dictionary or DataFrame based on 'return_df'
        if return_df:
            out = pd.DataFrame(out).T
        return out

    def check_parameters(self):
        # Ensure the specified species is among the available species
        assert self.specie in [
            i.id for i in stdpopsim.all_species()
        ], "Please select a correct species among the catalog: {}".format(
            [i.id for i in stdpopsim.all_species()]
        )

        # Ensure the specified demographic model is among available models or PiecewiseConstantSize
        assert "yaml" in self.demes or self.demes in np.array(
            [i.id for i in stdpopsim.all_demographic_models()]
            + ["PiecewiseConstantSize"]
        ), "Please select a correct demographic model among the catalog: {}".format(
            [i.id for i in stdpopsim.all_demographic_models()]
        )

        # Ensure the annotation type is either "exons" or "cds"
        assert (
            self.annotation == "exons" or self.annotation == "cds"
        ), "Please select cds or exon annotations"

        # Ensure the specified DFE (Distribution of Fitness Effects) is among available DFES or "neutral" or "custom"
        assert (
            self.dfe == "neutral"
            or self.dfe == "custom"
            or self.dfe in [i.id for i in stdpopsim.all_dfes()]
        ), "Please select cds or exon annotations"

        # Ensure the specified sweep class is either "hard" or "soft"
        assert self.sweep_class in [
            "hard",
            "soft",
        ], "Please select one the following categories: {}".format(["hard", "soft"])

    def deleterious_dfe(self):
        """
        Generate deleterious DFE.

        Returns:
        - stdpopsim.DFE: Deleterious DFE object.
        """
        muts = [
            stdpopsim.MutationType(
                dominance_coeff=self.dominance,
                distribution_type="f",
                distribution_args=[0],
            )
        ]

        muts.append(
            stdpopsim.MutationType(
                dominance_coeff=self.dominance,
                distribution_type="g",
                distribution_args=[self.del_dfe],
            )
        )
        return stdpopsim.DFE(
            id=self.dfe,
            description=self.dfe,
            long_description=self.dfe,
            mutation_types=muts,
            proportions=self.proportions,
        )

    def neutral_dfe(self):
        """
        Generate neutral DFE.

        Returns:
        - stdpopsim.DFE: Neutral DFE object.
        """
        muts = [
            stdpopsim.MutationType(
                dominance_coeff=self.dominance,
                distribution_type="f",
                distribution_args=[0],
            )
        ]
        return stdpopsim.DFE(
            id=self.dfe,
            description=self.dfe,
            long_description=self.dfe,
            mutation_types=muts,
            proportions=[1],
        )

    def create_model(self, nthreads=1, solve_diffusion_time=True):
        """
        Create the model based on parameters.

        Args:
        - solve_diffusion_time: Boolean indicating whether to solve diffusion times for sweeps.

        Returns:
        - None: Updates the class variables 'contig' and 'model'.
        """
        # Check and initialize parameters
        self.check_parameters()

        # Retrieve species information
        species = stdpopsim.get_species(self.specie)

        # Set population size
        self.Ne = species.population_size

        if self.sweep_class == "hard":
            self.f_i = [1 / self.Ne]

        if self.rescale_factor < 10:
            timeout = timeout * 10 / self.rescale_factor
        elif self.rescale_factor > 10:
            timeout = timeout * 1 / self.rescale_factor

        current_sweep = self.sweep_class

        # Load demes from specified file, create PiecewiseConstantSize model or retrieve the demographic model from stdpopsim
        if "yaml" in self.demes:
            pop_history = demes.load(self.demes)
            model = msprime.Demography().from_demes(pop_history)
            model = stdpopsim.DemographicModel(
                id=self.demes.split("/")[-1].split(".")[0],
                description="custom",
                long_description="custom",
                model=model,
            )
        elif self.demes == "PiecewiseConstantSize":
            model = stdpopsim.PiecewiseConstantSize(species.population_size)
            model.generation_time = species.generation_time
            # Force to sample to pop0 is PiecewiseConstantSize selected
            sample_tmp = {"pop_0": list(self.sample.values())[0]}
            self.sample = sample_tmp
        else:
            model = species.get_demographic_model(self.demes)

        # Handle annotation type
        if self.annotation == "exons":
            annotation = 0
        else:
            annotation = 1

        # Determine and create DFE
        if self.dfe == "neutral":
            dfe = self.neutral_dfe()
        elif self.dfe == "deleterious":
            dfe = deleterious_dfe(
                self.dfe,
                [self.shape / self.mean_strength, self.shape],
                self.proportions,
            )
        else:
            dfe = species.get_dfe(self.dfe)

        # Obtain chromosome and region information
        chrom = self.region.split(":")[0]
        region = list(map(int, self.region.split(":")[1].split("-")))

        # Retrieve contig with specified genetic map and region details, extract recombination map details from the genetic map file and create a DataFrame containing recombination map details
        if self.genetic_map in [i.id for i in species.genetic_maps]:
            contig = species.get_contig(
                chrom,
                genetic_map=self.genetic_map,
                mutation_rate=model.mutation_rate,
                left=region[0],
                right=region[1],
            )

            _rec_path = str(species.get_genetic_map(self.genetic_map).map_cache_dir)
            _rec_map = pd.read_csv(
                _rec_path + "/" + _rec_path.split("/")[-1] + "_" + chrom + ".txt",
                sep=" ",
            )
            _rec_map = _rec_map[_rec_map.iloc[:, 0] == chrom]
            recombination_map = pd.DataFrame(
                {
                    "chrom": chrom,
                    "id": _rec_map.index,
                    "genetic": _rec_map.iloc[:, -1],
                    "physical": _rec_map.iloc[:, 1],
                }
            )
        elif self.genetic_map.lower() == "uniform":
            contig = species.get_contig(
                chrom,
                mutation_rate=model.mutation_rate,
                left=region[0],
                right=region[1],
            )
            physical_positions = np.arange(region[0], region[1] + 1e5, 1e5).astype(int)
            rec_positions = np.arange(0, 1.2e6 + 1e5, 1e5)
            recombination_map = pd.DataFrame(
                {
                    "chrom": np.repeat(chrom, rec_positions.size),
                    "id": rec_positions,
                    "genetic": contig.recombination_map.get_cumulative_mass(
                        rec_positions
                    ),
                    "physical": physical_positions,
                }
            )
        else:
            contig = species.get_contig(
                chrom,
                mutation_rate=model.mutation_rate,
                left=region[0],
                right=region[1],
            )
            rate_map = msprime.RateMap.read_hapmap(self.genetic_map)
            rate_map_sliced = rate_map.slice(left=region[0], right=region[1], trim=True)
            contig.recombination_map = rate_map_sliced

            _rec_map = pd.read_csv(self.genetic_map, sep="\t")
            _rec_map = _rec_map[_rec_map.iloc[:, 0] == chrom]
            recombination_map = pd.DataFrame(
                {
                    "chrom": chrom,
                    "id": _rec_map.index,
                    "genetic": _rec_map.iloc[:, -1],
                    "physical": _rec_map.iloc[:, 1],
                }
            )

        self.recombination_map = recombination_map

        # Create a dictionary mapping indices to positions within the specified region
        slim_region = {i: v for (i, v) in enumerate(range(region[0], region[1] + 1))}

        # Update class variable 'slim_region' with the created mapping
        self.slim_region = slim_region

        # Retrieve raw annotations for the specified chromosome and annotation type
        raw_annotation = species.get_annotations(species.annotations[annotation].id)

        # Get intervals of annotations specifically for the chromosome
        annotations_intervals = raw_annotation.get_chromosome_annotations(chrom)

        # Add the derived DFE (Distribution of Fitness Effects) to the contig based on annotations
        contig.add_dfe(intervals=annotations_intervals, DFE=dfe)

        # Check if diffusion times need to be solved and if they haven't been calculated yet
        if (
            len(self.sweep_diffusion_time[self.sweep_class]) == 0
            and solve_diffusion_time
        ):
            # Warn about solving diffusion times for the specified sweeps
            logging.warning(
                "Solving diffusion times for {0} sweeps. It can take some time".format(
                    self.sweep_class
                )
            )
            # Calculate diffusion times based on Ne (effective population size)
            self.diffusion_time(self.Ne, nthreads)

        # Update class variables 'contig' and 'model' with the generated contig and model
        self.contig = contig
        self.model = model


hard_params = parameters(
    specie="HomSap",
    region="chr2:135212517-136412517",
    genetic_map="uniform",
    dfe="neutral",
    demes="PiecewiseConstantSize",
    sample={"AFR": 50},
    sweep_class="hard",
    rescale_factor=10,
)

soft_params = parameters(
    specie="HomSap",
    region="chr2:135212517-136412517",
    genetic_map="uniform",
    dfe="neutral",
    demes="PiecewiseConstantSize",
    sample={"AFR": 50},
    sweep_class="soft",
    rescale_factor=10,
)

# t, s, f_i, f_t, _burn_in = timing_selection(parameters,sweep_replicas,5000,200)


class Simulator:
    def __init__(self, parameters):
        self.parameters = parameters
        self.timeout = 180
        self.output_folder = None
        self.reset_simulations = False

    def timing_selection(
        self, f_t, t_lower=5000, t_upper=200, mutation_generation_ago=None
    ):
        f_i = np.random.choice(self.parameters.f_i)

        # Check if can acomplish f_t at the fixed timing
        if (mutation_generation_ago is not None) and (mutation_generation_ago >= 2000):
            if self.parameters.sweep_class == "soft":
                mutation_generation_ago = (
                    2000
                    + self.parameters.sweep_diffusion_time[self.parameters.sweep_class][
                        f_t
                    ][f_i][-1, 1]
                )
            else:
                mutation_generation_ago = (
                    2000
                    + self.parameters.sweep_diffusion_time[self.parameters.sweep_class][
                        f_t
                    ][-1, 1]
                )
            logging.warning(
                "Changing sweep mutation to generation {} to achieve the desired sweep frequency {}".format(
                    mutation_generation_ago, f_t
                )
            )

        if self.parameters.sweep_class == "soft" and f_i == 0.0:
            f_i = 0.05

        if f_t - round(f_i, 1) < 0.2:
            f_t += 0.2

        if f_t == 1:
            _t, _t_end, _s = self.timing_selection_complete_sweep(
                f_t, f_i, t_lower, t_upper, mutation_generation_ago
            )

        else:
            _t, _t_end, _s = self.timing_selection_incomplete_sweep(
                f_t, f_i, t_lower, t_upper, mutation_generation_ago
            )

        if self.parameters.sweep_class == "hard":
            # Reduce _burn_in but increasing a little bit to avoid problems drawing the mutation
            _burn_in = round((_t + 1) / self.parameters.Ne, 2)
            _burn_in = _burn_in + 0.01
        else:
            # Neutral arise 5000 gens ago from selection
            _burn_in = round((_t + 5001) / self.parameters.Ne, 2)
            _burn_in = _burn_in + 0.01

        return (_s / self.parameters.Ne, _t, _t_end, f_i, f_t, _burn_in)

    def timing_selection_complete_sweep(
        self, i, j, t_lower, t_upper, mutation_generation_ago=None
    ):
        current_sweep = self.parameters.sweep_class

        t = []
        s = []
        # for (i,j) in tqdm(zip(f_t,f_i),total=f_i.size,desc="Sampling uniform t [{0},{1}] and s [{2},{3}]".format(t_lower,t_upper,20,1000)):

        s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][1]

        if current_sweep == "soft":
            s_t_lower = s_t_lower[round(j + 0.01, 1)]

        if mutation_generation_ago is None:
            _t = np.random.uniform(t_lower, t_upper, 1).astype(int)[0]
        else:
            _t = mutation_generation_ago

        _s = s_t_lower[(s_t_lower[:, 1] <= (_t - t_upper)), 0]

        while _s.size == 0:
            if mutation_generation_ago is None:
                _t = np.random.uniform(t_lower, t_upper, 1).astype(int)[0]
            else:
                _t = mutation_generation_ago

            _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

        _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)[0]

        return (_t, 0, _s)

    def timing_selection_incomplete_sweep(
        self, i, j, t_lower, t_upper, mutation_generation_ago=None
    ):
        current_sweep = self.parameters.sweep_class

        t = []
        s = []

        s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][round(i, 1)]
        s_t_upper = self.parameters.sweep_diffusion_time[current_sweep][
            round(i + 0.1, 1)
        ]

        # We search for the previous diffusion mean value to ensure the condition.
        # Otherwise the rounded values search for the nearest estimated value and some condition cannot achieve because of the arise time is shorter than expected
        # Diffusion value are estimated in the range [0:0.05:1]
        if j > 0.05:
            _j = round(round(j, 1) - 0.05, 2)
        else:
            _j = j

        if self.parameters.sweep_class == "soft":
            # Check rounded init frequency not equal or greater than end frequence.
            # Otherwise change value and array.
            while _j >= i:
                _j = round(np.random.uniform(self.parameters.f_i[0], j), 2)

                if _j > 0.05:
                    _j = round(round(j, 1) - 0.05, 2)

                # f_i[k] = _j
                # print(f_i[k])
            s_t_lower = s_t_lower[_j]
            s_t_upper = s_t_upper[_j]

        # Minimum number of simulation to achieve current frequency in old sweeps
        min_gen = s_t_lower[-1, 1]

        if mutation_generation_ago is None:
            _t = np.random.uniform(t_lower, t_upper + min_gen, 1).astype(int)[0]
        else:
            _t = mutation_generation_ago

        if _t > 2000:
            # Checking if mutation_generation_ago or random t is greater than the minimum amount diffusion time estimated
            # Otherwise there is no s value to achieve f_t at generations 2000.
            _t_limit = np.random.choice(np.arange(2000, _t), 1)[0]

            if (_t - _t_limit) < min_gen:
                _t_limit -= min_gen

            s_lower = s_t_lower[s_t_lower[:, 1] <= (_t - _t_limit), 0]
            s_upper = s_t_lower[s_t_upper[:, 1] >= (_t - _t_limit), 0]
            _s = np.intersect1d(s_lower, s_upper)
            _t_end = _t_limit
        else:
            s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
            s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
            _s = np.intersect1d(s_lower, s_upper)
            _t_end = 0
        while _s.size == 0:
            if mutation_generation_ago is None:
                _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
            else:
                _t = np.array([mutation_generation_ago])

                s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
                s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
                _s = np.intersect1d(s_lower, s_upper)

        _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)[0]

        return (_t, _t_end, _s)

    def simulate(self, num_sweeps, num_neutral=1e4, nthreads=1, max_tries=3):
        self.parameters.f_t = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        sims_1 = self.sweep_simulation(num_sweeps, nthreads, t_lower=2000, t_upper=200)

        # Reset to False to add simulations
        self.reset_simulations = False
        sims_2 = self.sweep_simulation(num_sweeps, nthreads, t_lower=5000, t_upper=2000)

        self.parameters.f_t = np.array([1.0])
        sims_3 = self.sweep_simulation(num_sweeps, nthreads, t_lower=2000, t_upper=200)

        sims_4 = self.sweep_simulation(num_sweeps, nthreads, t_lower=5000, t_upper=2000)

        # If output_folder is defined then each run is reading previous simulated files in folder
        if self.output_folder is None:
            sims = sims_1 + sims_2 + sims_3 + sims_4
        else:
            sims = sims_4

        neutral = self.neutral_simulation(num_neutral, nthreads)

        sims_d = defaultdict()
        sims_d["sweeps"] = sims
        sims_d["neutral"] = neutral

        return sims_d

    def sweep_simulation(
        self,
        num_simulations,
        nthreads=1,
        t_lower=5000,
        t_upper=200,
        mutation_generation_ago=None,
        max_tries=3,
    ):
        # self.timing_selection
        num_simulations = int(num_simulations)

        simulated_list = np.arange(1, num_simulations + 1).astype(int)

        if self.output_folder is not None:
            os.makedirs(self.output_folder, exist_ok=True)
            os.makedirs(self.output_folder + "/sweeps/", exist_ok=True)

            sweep_list = glob.glob(self.output_folder + "/sweeps/*trees")

            if self.reset_simulations and os.path.exists(self.output_folder):
                shutil.rmtree(self.output_folder)
            elif len(sweep_list) == 0:
                next
            else:
                sweep_list = np.sort(
                    np.array(
                        [
                            x.replace(self.output_folder + "/sweeps/", "")
                            .replace("sweep_", "")
                            .replace(".trees", "")
                            for x in sweep_list
                        ],
                        dtype=int,
                    )
                )

                lost_sims = np.setdiff1d(np.arange(1, sweep_list.max()), sweep_list)

                simulated_list = np.concatenate(
                    [
                        lost_sims,
                        np.arange(
                            sweep_list.max() + 1, sweep_list.max() + 1 + num_simulations
                        ),
                    ]
                ).astype(int)

                if simulated_list.size > num_simulations:
                    simulated_list = simulated_list[:num_simulations]

        f_t = np.random.choice(self.parameters.f_t, simulated_list.size).round(1)

        if (
            (mutation_generation_ago is not None)
            and (t_upper >= 2000)
            and (np.any(f_t < 1.0))
        ):
            logging.warning(
                "The software will change the selected generation where mutation arise {} to achieve the sweep frequency for old incomplete sweep to the minumum time according to the estimated diffusion times and selection coefficients".format(
                    mutation_generation_ago
                )
            )

        params = [
            self.timing_selection(f_t[i], t_lower, t_upper, mutation_generation_ago)
            + (simulated_list[i],)
            for i in range(simulated_list.size)
        ]

        sims = Parallel(n_jobs=nthreads, backend="multiprocessing", verbose=1)(
            delayed(self.generate_simulation)(params[i])
            for i in range(simulated_list.size)
        )

        if self.parameters.sweep_class == "soft":
            # self.timeout = int(self.timeout / 2)

            check_sims = np.array(
                [
                    i
                    for (i, item) in enumerate(sims)
                    if all(elem is None for elem in item)
                ]
            )

            while check_sims.size > 0:
                logging.error(
                    "A total of {} soft sweeps simulation cannot be completed. Restarting to avoid memory leak until completed".format(
                        check_sims.size
                    )
                )

                for i in check_sims:
                    params[i] = self.timing_selection(
                        f_t[i], t_lower, t_upper, mutation_generation_ago
                    ) + (simulated_list[i],)

                _sims = []

                _sims = Parallel(n_jobs=nthreads, backend="multiprocessing", verbose=1)(
                    delayed(self.generate_simulation)(params[i]) for i in check_sims
                )

                for i, j in zip(check_sims, _sims):
                    sims[i] = j

                check_sims = np.array(
                    [
                        i
                        for (i, item) in enumerate(sims)
                        if all(elem is None for elem in item)
                    ]
                )

                if check_sims.size == 0:
                    break

        sims = [item for item in sims if not all(elem is None for elem in item)]

        if self.output_folder is not None:
            if os.path.exists(self.output_folder + "/sims.pickle"):
                try:
                    sims_old = self.read_simulations()
                    sims = sims_old["sweeps"] + sims
                except:
                    sims_old = defaultdict()
            else:
                sims_old = defaultdict()

            sims_d = {}
            sims_d["sweeps"] = sims

            if "neutral" not in sims_old.keys():
                sims_d["neutral"] = []
            else:
                sims_d["neutral"] = sims_old["neutral"]

            with open(self.output_folder + "/sims.pickle", "wb") as handle:
                pickle.dump(sims_d, handle)

        return sims

    def generate_simulation(self, param_iter):
        (_s, _t, _t_end, _f_i, _f_t, _burn_in, iteration) = param_iter

        # if _t > 2000:
        #     _t_end = 2000
        # else:
        #     _t_end = 0

        tmp_parameters = deepcopy(self.parameters)

        # adaptive_position = np.random.randint(1.2e6*0.25,1.2e6*0.75)
        adaptive_position = sum(tmp_parameters.contig.original_coordinates[1:]) / 2

        tmp_parameters.contig.add_single_site(
            id=tmp_parameters.sweep_class, coordinate=adaptive_position
        )

        if tmp_parameters.sweep_class == "hard":
            extended_events = stdpopsim.ext.selective_sweep(
                single_site_id=tmp_parameters.sweep_class,
                population=list(tmp_parameters.sample.keys())[0],
                selection_coeff=_s,
                min_freq_at_end=_f_t,
                mutation_generation_ago=_t,
                end_generation_ago=_t_end,
            )

        else:
            # start_generation_ago _t + 5000 to ensure the soft sweep achieve the desired freq (up to 0.25)
            extended_events = stdpopsim.ext.selective_sweep(
                single_site_id=tmp_parameters.sweep_class,
                population=list(tmp_parameters.sample.keys())[0],
                selection_coeff=_s,
                min_freq_at_start=_f_i,
                min_freq_at_end=_f_t,
                mutation_generation_ago=_t + 5000,
                end_generation_ago=_t_end,
                start_generation_ago=_t,
            )

            end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
                start_time=_t,
                end_time=_t,
                single_site_id=tmp_parameters.sweep_class,
                population=list(tmp_parameters.sample)[0],
                op="<=",
                allele_frequency=_f_i + 0.1,
            )

            extended_events.append(end_condition)

        if _f_t != 1:
            # f_step = 0.1 if _f_t == 0.9 else 0.1

            end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
                start_time=_t_end,
                end_time=_t_end,
                single_site_id=tmp_parameters.sweep_class,
                population=list(tmp_parameters.sample)[0],
                op="<",
                allele_frequency=_f_t + 0.1,
            )

            extended_events.append(end_condition)

        engine = stdpopsim.get_engine("slim")

        def timeout_handler(signum, frame):
            raise TimeoutError("Execution timed out")

        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(self.timeout)
        timeout_occurred = False

        with open("/home/jmurgamoreno/test.slim", "w") as f:
            with redirect_stdout(f):
                ts_sweep = engine.simulate(
                    tmp_parameters.model,
                    tmp_parameters.contig,
                    tmp_parameters.sample,
                    extended_events=extended_events,
                    slim_scaling_factor=tmp_parameters.rescale_factor,
                    slim_burn_in=_burn_in,
                    slim_script=True,
                    verbosity=0,
                )
        try:
            ts_sweep = engine.simulate(
                tmp_parameters.model,
                tmp_parameters.contig,
                tmp_parameters.sample,
                extended_events=extended_events,
                slim_scaling_factor=tmp_parameters.rescale_factor,
                slim_burn_in=_burn_in,
            )
        except TimeoutError:
            timeout_occurred = True
        finally:
            signal.alarm(0)

        if timeout_occurred:
            return (None, None, None, None)

        if self.output_folder is not None:
            ts_string = (
                self.output_folder + "/sweeps/sweep_" + str(iteration) + ".trees"
            )
            ts_sweep.dump(ts_string)

            return (
                ts_string,
                self.interpolate_genetic_map(ts_sweep),
                np.column_stack([_s, _t, _t_end, _f_i, _f_t]).flatten(),
            )
        else:
            return (
                ts_sweep,
                self.interpolate_genetic_map(ts_sweep),
                np.column_stack([_s, _t, _t_end, _f_i, _f_t]).flatten(),
            )

    def neutral_simulation(
        self,
        num_simulations,
        nthreads,
    ):
        # self.timing_selection
        simulated_list = np.arange(1, num_simulations + 1)

        if self.output_folder is not None:
            os.makedirs(self.output_folder, exist_ok=True)
            os.makedirs(self.output_folder + "/neutral", exist_ok=True)

            neutral_list = glob.glob(self.output_folder + "/neutral/*trees")

            if self.reset_simulations and os.path.exists(
                self.output_folder + "/neutral"
            ):
                shutil.rmtree(self.output_folder + "/neutral")
            elif len(neutral_list) >= simulated_list.size:
                simulated_list = np.array([])
            else:
                neutral_list = np.sort(
                    np.array(
                        [
                            x.replace(self.output_folder + "/neutral/", "")
                            .replace("neutral_", "")
                            .replace(".trees", "")
                            for x in neutral_list
                        ],
                        dtype=int,
                    )
                )

                simulated_list = np.setdiff1d(simulated_list, neutral_list)

                # simulated_list = np.concatenate(
                #     [
                #         lost_sims,
                #         np.arange(
                #             neutral_list.max() + 1,
                #             neutral_list.max() + num_simulations + 1,
                #         ),
                #     ]
                # )

                if simulated_list.size > num_simulations:
                    simulated_list = simulated_list[:num_simulations]

            os.makedirs(self.output_folder + "/neutral/", exist_ok=True)

        if simulated_list.size == 0:
            sims = []
        else:
            sims = Parallel(n_jobs=nthreads, backend="multiprocessing", verbose=2)(
                delayed(self.generate_neutral)(i) for i in simulated_list
            )
            sims = [item for item in sims if not all(elem is None for elem in item)]

        if self.output_folder is not None:
            try:
                sims_old = self.read_simulations()
                sims = sims_old["neutral"] + sims
            except:
                sims_old = defaultdict()

            sims_d = {}
            sims_d["neutral"] = sims

            if "sweeps" not in sims_old.keys():
                sims_d["sweeps"] = []
            else:
                sims_d["sweeps"] = sims_old["sweeps"]

            with open(self.output_folder + "/sims.pickle", "wb") as handle:
                pickle.dump(sims_d, handle)

        return sims

    def generate_neutral(self, iteration):
        tmp_parameters = deepcopy(self.parameters)

        engine = stdpopsim.get_engine("msprime")

        def timeout_handler(signum, frame):
            raise TimeoutError("Execution timed out")

        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(self.timeout)
        timeout_occurred = False

        try:
            ts_neutral = engine.simulate(
                tmp_parameters.model,
                tmp_parameters.contig,
                tmp_parameters.sample,
            )
        except TimeoutError:
            timeout_occurred = True
        finally:
            signal.alarm(0)

        if timeout_occurred:
            return (None, None, None)

        if self.output_folder is not None:
            ts_string = (
                self.output_folder + "/neutral/neutral_" + str(iteration) + ".trees"
            )
            ts_neutral.dump(ts_string)

            return (ts_string, self.interpolate_genetic_map(ts_neutral))
        else:
            return (ts_neutral, self.interpolate_genetic_map(ts_neutral))

    def read_simulations(self):
        try:
            with open(self.output_folder + "/sims.pickle", "rb") as handle:
                sims = pickle.load(handle)
            return sims
        except:
            print("Set the simulation output folder before reading simulations")

    def interpolate_genetic_map(self, ts):
        _coordinates = np.array(
            [(self.parameters.slim_region[i], i) for i in ts.sites_position]
        )

        if self.parameters.recombination_map is None:
            recombination_hapmap = np.column_stack(
                [
                    np.repeat(1, ts.sites_position.size),
                    np.arange(1, ts.sites_position.size + 1),
                    _coordinates[:, 1],
                    _coordinates[:, 1],
                ]
            )
        else:
            f = interp1d(
                self.parameters.recombination_map.physical.values,
                self.parameters.recombination_map.genetic.values,
            )
            recombination_hapmap = np.column_stack(
                [
                    np.repeat(1, ts.sites_position.size),
                    np.arange(1, ts.sites_position.size + 1),
                    _coordinates[:, 1],
                    f(_coordinates[:, 0]),
                ]
            )

        return recombination_hapmap

    def update_params(self, parameters):
        self.model = parameters


def footprinting(N, s, r):
    return np.ceil(s / (np.log(N * s) * r))


def neutral_simulation(self, timeout=180):
    engine = stdpopsim.get_engine("msprime")

    species = stdpopsim.get_species("HomSap")
    model = stdpopsim.PiecewiseConstantSize(10000)
    samples = {"pop_0": 50}
    contig = species.get_contig("22", right=1e6)

    def timeout_handler(signum, frame):
        raise TimeoutError("Execution timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    try:
        ts_neutral = engine.simulate(
            parameters.model, parameters.contig, parameters.sample
        )
        with open("/home/jmurgamoreno/test_neutral.slim", "w") as f:
            with redirect_stdout(f):
                ts_sweep = engine.simulate(
                    parameters.model,
                    parameters.contig,
                    parameters.sample,
                    slim_scaling_factor=10,
                    slim_burn_in=10,
                    slim_script=True,
                    verbosity=0,
                )

    finally:
        signal.alarm(0)

    return ts_neutral


def ms_to_numpy(ms_file):
    """Reads in a ms file and outputs the positions and the genotypes.
    Genotypes are a numpy array of 0s and 1s with shape (num_segsites, num_samples).
    """
    with open(ms_file) as file:
        # Read in number of segregating sites and positions
        for line in file:
            if "discoal" in line:
                seq_len = int(line.strip().split()[3])
            if line.startswith("segsites"):
                num_segsites = int(line.strip().split()[1])
                if num_segsites == 0:
                    # Shape of data array for 0 segregating sites should be (0, 1)
                    return np.array([]), np.array([], ndmin=2, dtype=np.uint8).T
            elif line.startswith("positions"):
                positions = np.array([float(x) for x in line.strip().split()[1:]])
                positions = np.floor(positions * seq_len).astype(int)
                break
            else:
                continue
        # Now read in the data
        data = np.array([list(line.strip()) for line in file], dtype=np.int8)
        rec_map = np.column_stack(
            [
                np.repeat(1, positions.size),
                np.arange(positions.size),
                positions,
                positions,
            ]
        )
    return data.T, rec_map, positions


def ts_to_ms(trees, ms_file, normalize_positions=True, header_line="", seed=""):
    header = "\n".join([header_line, str(seed), "", "//"])
    num_segsites = trees.num_sites
    segsites_line = f"segsites: {num_segsites}"
    positions = [trees.site(mut.site).position for mut in trees.mutations()]
    if normalize_positions:
        positions = [pos / trees.sequence_length for pos in positions]
    positions.sort()
    positions_line = "positions: " + " ".join(f"{pos:.6f}" for pos in positions)

    haplotypes_block = []
    for hap in trees.genotype_matrix().T:
        haplotypes_block.append("".join(map(str, hap)))

    with open(ms_file, "w") as f:
        f.write(
            "\n".join(
                [header, segsites_line, positions_line, "\n".join(haplotypes_block)]
            )
        )


def plot_tree(ts, position, path):
    ts.at(position).draw_svg(
        path,
        size=(2000, 1000),
        node_labels={},  # Remove all node labels for a clearer viz
    )


##########################


# @dataclass
# class parameters:
#     """
#     Create a class container to automatize sweep simulations using stdpopsim.
#     """

#     specie: str
#     region: str
#     genetic_map: str
#     dfe: str
#     demes: str
#     sample: dict
#     contig: stdpopsim.genomes.Contig = None
#     model: stdpopsim.models = None
#     slim_region: dict = None
#     recombination_map: pd.DataFrame = None
#     annotation: str = "exons"
#     f_i: list = field(default_factory=lambda: [0.05, 0.1, 0.15, 0.2])
#     f_t: list = field(default_factory=lambda: np.arange(0.2, 1.1, 0.1))
#     del_dfe: dict = field(default_factory=lambda: {"mean_strength": 0, "shape": 0})
#     proportions: list = field(default_factory=lambda: [0, 0])
#     burn_in: int = 1
#     rescale_factor: int = 1
#     dominance: float = 0.5
#     Ne: int = (1e4,)
#     sweep_diffusion_time: list = field(default_factory=lambda: {"hard": {}, "soft": {}})

#     def diffusion_time_value(self, N, s, f_i, f_t, c=2) -> float:
#         _N = 2 * N
#         s = s / _N
#         result = integrate.quad(
#             lambda x: (
#                 (exp(2 * c * _N * s * x) - 1) * (exp(2 * c * _N * s * (1 - x)) - 1)
#             )
#             / (s * x * (1 - x) * (exp(2 * c * _N * s) - 1)),
#             f_i,
#             f_t,
#         )
#         return result[0]

#     def diffusion_time(self, N):
#         if (
#             len(self.sweep_diffusion_time["hard"]) != 0
#             and list(self.sweep_diffusion_time["hard"].keys()) == self.f_t
#             and len(self.sweep_diffusion_time["soft"]) != 0
#             and list(self.sweep_diffusion_time["soft"].keys()) == self.f_t
#         ):
#             print("Diffusion mean time is estimated")
#         else:
#             func = np.vectorize(self.diffusion_time_value)
#             # Hard sweeps

#             # s_v = np.arange(20,1001,1)
#             # Correcting SLIM 1+s vs diffusion 1+2s on AA
#             s_v = np.arange(10, 1001, 1)
#             for i in self.f_t:
#                 t_fix = func(N, s_v, 1 / (2 * N), i).astype(int)
#                 s_t = np.vstack([s_v, t_fix]).T
#                 self.sweep_diffusion_time["hard"][round(i, 2)] = s_t

#             # Soft sweeps
#             iterables = np.array(list(product(self.f_t, self.f_i)))
#             iterables = iterables[iterables[:, 1] < iterables[:, 0]]

#             for end, start in iterables:
#                 # for (end,start) in tqdm(iterables,desc="Diffusion mean time"):

#                 t_fix = func(N, s_v, start, end).astype(int)
#                 s_t = np.vstack([s_v, t_fix]).T

#                 if round(end, 1) not in self.sweep_diffusion_time["soft"]:
#                     self.sweep_diffusion_time["soft"][round(end, 1)] = {}
#                     self.sweep_diffusion_time["soft"][round(end, 1)].update(
#                         {start: s_t}
#                     )
#                 else:
#                     self.sweep_diffusion_time["soft"][round(end, 1)].update(
#                         {start: s_t}
#                     )

#     def check_stdpopsim(self, return_df=True):
#         out = {}
#         for i in stdpopsim.all_species():
#             tmp_specie = stdpopsim.get_species(i.id)
#             tmp_parameters.models = ", ".join(
#                 [i.id for i in tmp_specie.demographictmp_parameters.models]
#             )
#             tmp_dfes = ", ".join(
#                 [i.id for i in tmp_specie.demographictmp_parameters.models]
#             )
#             tmp_genetic_maps = ", ".join([i.id for i in tmp_specie.genetic_maps])
#             out[i.id] = {
#                 "models": tmptmp_parameters.models,
#                 "genetic_maps": tmp_genetic_maps,
#                 "dfes": tmp_dfes,
#             }

#         print(
#             "\n\nPlease check the available specie and the asociated annotation, dfe and demographic model\n"
#         )
#         if return_df:
#             out = pd.DataFrame(out).T
#         return out

#     def check_parameters(self):
#         assert self.specie in [
#             i.id for i in stdpopsim.all_species()
#         ], "Please select a correct species among the catalog: {}".format(
#             [i.id for i in stdpopsim.all_species()]
#         )
#         assert "yaml" in self.demes or self.demes in np.array(
#             [i.id for i in stdpopsim.all_demographic_models()]
#             + ["PiecewiseConstantSize"]
#         ), "Please select a correct demographic model among the catalog: {}".format(
#             [i.id for i in stdpopsim.all_demographic_models()]
#         )
#         assert (
#             self.annotation == "exons" or self.annotation == "cds"
#         ), "Please select cds or exon annotations"
#         assert (
#             self.dfe == "neutral"
#             or self.dfe == "custom"
#             or self.dfe in [i.id for i in stdpopsim.all_dfes()]
#         ), "Please select cds or exon annotations"

#     def deleterious_dfe(self):
#         muts = [
#             stdpopsim.MutationType(
#                 dominance_coeff=self.dominance,
#                 distribution_type="f",
#                 distribution_args=[0],
#             )
#         ]

#         muts.append(
#             stdpopsim.MutationType(
#                 dominance_coeff=self.dominance,
#                 distribution_type="g",
#                 distribution_args=[self.del_dfe],
#             )
#         )
#         return stdpopsim.DFE(
#             id=self.dfe,
#             description=self.dfe,
#             long_description=self.dfe,
#             mutation_types=muts,
#             proportions=self.proportions,
#         )

#     def neutral_dfe(self):
#         muts = [
#             stdpopsim.MutationType(
#                 dominance_coeff=self.dominance,
#                 distribution_type="f",
#                 distribution_args=[0],
#             )
#         ]
#         return stdpopsim.DFE(
#             id=self.dfe,
#             description=self.dfe,
#             long_description=self.dfe,
#             mutation_types=muts,
#             proportions=[1],
#         )

#     def create_model(self):
#         self.check_parameters()

#         species = stdpopsim.get_species(self.specie)

#         self.Ne = species.population_size

#         # if self.rescale_factor < 10:
#         #     timeout = timeout * 10 / self.rescale_factor
#         # elif self.rescale_factor > 10:
#         #     timeout = timeout * 1 / self.rescale_factor

#         if "yaml" in self.demes:
#             pop_history = demes.load(self.demes)
#             model = msprime.Demography().from_demes(pop_history)
#             model = stdpopsim.DemographicModel(
#                 id=self.demes.split("/")[-1].split(".")[0],
#                 description="custom",
#                 long_description="custom",
#                 model=model,
#             )
#         elif self.demes == "PiecewiseConstantSize":
#             model = stdpopsim.PiecewiseConstantSize(species.population_size)
#             model.generation_time = species.generation_time
#             # Force to sample to pop0 is PiecewiseConstantSize selected
#             sample_tmp = {"pop_0": list(self.sample.values())[0]}
#             self.sample = sample_tmp
#         else:
#             model = species.get_demographic_model(self.demes)

#         if self.annotation == "exons":
#             annotation = 0
#         else:
#             annotation = 1

#         if self.dfe == "neutral":
#             dfe = self.neutral_dfe()
#         elif self.dfe == "deleterious":
#             dfe = deleterious_dfe(
#                 self.dfe,
#                 [self.shape / self.mean_strength, self.shape],
#                 self.proportions,
#             )
#         else:
#             dfe = species.get_dfe(self.dfe)

#         chrom = self.region.split(":")[0]
#         region = list(map(int, self.region.split(":")[1].split("-")))

#         # Need to save original map
#         if self.genetic_map in [i.id for i in species.genetic_maps]:
#             contig = species.get_contig(
#                 chrom,
#                 genetic_map=self.genetic_map,
#                 mutation_rate=model.mutation_rate,
#                 left=region[0],
#                 right=region[1],
#             )

#             _rec_path = str(species.get_genetic_map(self.genetic_map).map_cache_dir)
#             _rec_map = pd.read_csv(
#                 _rec_path + "/" + _rec_path.split("/")[-1] + "_" + chrom + ".txt",
#                 sep=" ",
#             )
#             _rec_map = _rec_map[_rec_map.iloc[:, 0] == chrom]
#             recombination_map = pd.DataFrame(
#                 {
#                     "chrom": chrom,
#                     "id": _rec_map.index,
#                     "genetic": _rec_map.iloc[:, -1],
#                     "physical": _rec_map.iloc[:, 1],
#                 }
#             )

#         elif self.genetic_map.lower() == "uniform":
#             contig = species.get_contig(
#                 chrom,
#                 mutation_rate=model.mutation_rate,
#                 left=region[0],
#                 right=region[1],
#             )
#             recombination_map = None
#         else:
#             contig = species.get_contig(
#                 chrom,
#                 mutation_rate=model.mutation_rate,
#                 left=region[0],
#                 right=region[1],
#             )
#             rate_map = msprime.RateMaparameters.read_hapmap(self.genetic_map)
#             rate_map_sliced = rate_maparameters.slice(
#                 left=region[0], right=region[1], trim=True
#             )
#             contig.recombination_map = rate_map_sliced

#             _rec_map = pd.read_csv(self.genetic_map, sep="\t")
#             _rec_map = _rec_map[_rec_map.iloc[:, 0] == chrom]
#             recombination_map = pd.DataFrame(
#                 {
#                     "chrom": chrom,
#                     "id": _rec_map.index,
#                     "genetic": _rec_map.iloc[:, -1],
#                     "physical": _rec_map.iloc[:, 1],
#                 }
#             )
#         self.recombination_map = recombination_map

#         slim_region = {i: v for (i, v) in enumerate(range(region[0], region[1] + 1))}

#         self.slim_region = slim_region

#         raw_annotation = species.get_annotations(species.annotations[annotation].id)
#         annotations_intervals = raw_annotation.get_chromosome_annotations(chrom)

#         contig.add_dfe(intervals=annotations_intervals, DFE=dfe)

#         if (
#             len(self.sweep_diffusion_time["hard"]) == 0
#             or len(self.sweep_diffusion_time["soft"]) == 0
#         ):
#             logging.info("Solving sweep diffusion times")
#             self.diffusion_time(self.Ne)

#         self.contig = contig
#         self.model = model


# params = parameters(
#     specie="HomSap",
#     region="chr2:135212517-136412517",
#     genetic_map="uniform",
#     dfe="neutral",
#     demes="PiecewiseConstantSize",
#     sample={"AFR": 50},
#     rescale_factor=10,
# )


# class Generator:
#     def __init__(self, parameters):
#         self.parameters = parameters
#         self.model = None
#         self.timing_selection(1)
#         self.timeout = 180

#     def timing_selection(self, f_t, t_lower=5000, t_upper=200):
#         # f_i = np.random.choice(np.hstack([(1 / self.parameters.Ne),self.parameters.f_i]))
#         # f_t = np.random.choice(self.parameters.f_t).round(1)
#         # f_i = 1 / 1e4
#         # f_t = np.random.choice(self.parameters.f_t).round(1)
#         f_i = np.random.choice(self.parameters.f_i).round(1)

#         if f_t - round(f_i, 1) < 0.2:
#             f_t += 0.2

#         if f_t == 1:
#             _t, _s = self.timing_selection_complete_sweep(f_t, f_i, t_lower, t_upper)
#         else:
#             _t, _s = self.timing_selection_incomplete_sweep(f_t, f_i, t_lower, t_upper)

#         if self.parameters.sweep_class == "hard":
#             # Reduce _burn_in but increasing a little bit to avoid problems drawing the mutation
#             _burn_in = ((_t + 1) / self.parameters.Ne).round(2)
#             _burn_in = _burn_in + 0.01
#         else:
#             # Neutral arise 5000 gens ago from selection
#             _burn_in = ((_t + 5001) / self.parameters.Ne).round(2)
#             _burn_in = _burn_in + 0.01

#         self.model = (_s / self.parameters.Ne, _t, f_i, f_t, _burn_in)

#     def timing_selection_complete_sweep(self, i, j, t_lower, t_upper):
#         current_sweep = np.random.choice(["hard", "soft"])

#         t = []
#         s = []
#         # for (i,j) in tqdm(zip(f_t,f_i),total=f_i.size,desc="Sampling uniform t [{0},{1}] and s [{2},{3}]".format(t_lower,t_upper,20,1000)):

#         s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][1]

#         if self.parameters.sweep_class == "soft":
#             s_t_lower = s_t_lower[round(j + 0.01, 1)]

#         _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#         _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

#         while _s.size == 0:
#             _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#             _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

#         _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)

#         return (_t[0], _s[0])

#     def timing_selection_incomplete_sweep(self, i, j, t_lower, t_upper):
#         current_sweep = np.random.choice(["hard", "soft"])

#         t = []
#         s = []

#         s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][round(i, 1)]
#         s_t_upper = self.parameters.sweep_diffusion_time[current_sweep][
#             round(i + 0.1, 1)
#         ]

#         # We search for the previous diffusion mean value to ensure the condition.
#         # Otherwise the rounded values search for the nearest estimated value and some condition cannot achieve because of the arise time is shorter than expected
#         # Diffusion value are estimated in the range [0:0.05:1]
#         if j > 0.05:
#             _j = round(round(j, 1) - 0.05, 2)
#         else:
#             _j = j

#         if self.parameters.sweep_class == "soft":
#             # Check rounded init frequency not equal or greater than end frequence.
#             # Otherwise change value and array.
#             while _j >= i:
#                 _j = round(np.random.uniform(self.parameters.f_i[0], j), 2)

#                 if _j > 0.05:
#                     _j = round(round(j, 1) - 0.05, 2)

#                 f_i[k] = _j

#             s_t_lower = s_t_lower[_j]
#             s_t_upper = s_t_upper[_j]

#         _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#         s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
#         s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
#         _s = np.intersect1d(s_lower, s_upper)

#         while _s.size == 0:
#             _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#             s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
#             s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
#             _s = np.intersect1d(s_lower, s_upper)

#         _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)

#         return (_t[0], _s[0])

#     def sweep_simulation(self, num_simulations, f_t, t_lower=5000, t_upper=200):
#         results = []
#         self.parameters
#         for _ in range(num_simulations):
#             # Generate simulation
#             ts_sweep, genetic_map, params = self.generate_simulation(
#                 f_t, t_lower, t_upper
#             )

#             if ts_sweep is not None:
#                 results.append((ts_sweep, genetic_map, params))

#         return results

#     def generate_simulation(self, f_t, t_lower=5000, t_upper=200):
#         self.timing_selection(f_t, t_lower, t_upper)

#         tmp_parameters = deepcopy(self.parameters)
#         sweep_class = np.random.choice(["hard", "soft"])

#         (_s, _t, _f_i, _f_t, _burn_in) = self.model

#         # adaptive_position = np.random.randint(1.2e6*0.25,1.2e6*0.75)
#         adaptive_position = sum(tmp_parameters.contig.original_coordinates[1:]) / 2

#         tmp_parameters.contig.add_single_site(
#             id=sweep_class, coordinate=adaptive_position
#         )

#         if sweep_class == "hard":
#             extended_events = stdpopsim.ext.selective_sweep(
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample.keys())[0],
#                 selection_coeff=_s,
#                 min_freq_at_end=_f_t,
#                 mutation_generation_ago=_t,
#             )
#         else:
#             # start_generation_ago _t + 5000 to ensure the soft sweep achieve the desired freq (up to 0.25)
#             extended_events = stdpopsim.ext.selective_sweep(
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample.keys())[0],
#                 selection_coeff=_s,
#                 min_freq_at_start=_f_i,
#                 min_freq_at_end=_f_t,
#                 mutation_generation_ago=_t + 5000,
#                 start_generation_ago=_t,
#             )

#             end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
#                 start_time=_t,
#                 end_time=_t,
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample)[0],
#                 op="<",
#                 allele_frequency=_f_i + 0.1,
#             )

#             extended_events.append(end_condition)

#         if _f_t != 1:
#             f_step = 0.1 if _f_t == 0.9 else 0.1
#             end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
#                 start_time=0,
#                 end_time=0,
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample)[0],
#                 op="<",
#                 allele_frequency=_f_t + 0.1,
#             )

#             extended_events.append(end_condition)

#         engine = stdpopsim.get_engine("slim")

#         with open("/home/jmurgamoreno/test.slim", "w") as f:
#             with redirect_stdout(f):
#                 ts_sweep = engine.simulate(
#                     tmp_parameters.model,
#                     tmp_parameters.contig,
#                     tmp_parameters.sample,
#                     extended_events=extended_events,
#                     slim_scaling_factor=tmp_parameters.rescale_factor,
#                     slim_burn_in=_burn_in,
#                     slim_script=True,
#                     verbosity=0,
#                 )

#         def timeout_handler(signum, frame):
#             raise TimeoutError("Execution timed out")

#         signal.signal(signal.SIGALRM, timeout_handler)
#         signal.alarm(self.timeout)
#         timeout_occurred = False
#         try:
#             ts_sweep = engine.simulate(
#                 tmp_parameters.model,
#                 tmp_parameters.contig,
#                 tmp_parameters.sample,
#                 extended_events=extended_events,
#                 slim_scaling_factor=tmp_parameters.rescale_factor,
#                 slim_burn_in=_burn_in,
#             )
#         except TimeoutError:
#             timeout_occurred = True
#         finally:
#             signal.alarm(0)

#         if timeout_occurred:
#             return (None, None, None)
#         else:
#             if _f_t != 1:
#                 _f_t = frequency(ts_sweep, 6e5)
#             return (
#                 ts_sweep,
#                 self.interpolate_genetic_map(ts_sweep),
#                 np.column_stack([_s, _t, _f_i, _f_t]),
#             )
#             # return np.concatenate(
#             #     [
#             #         np.hstack([_s, _t, _f_i, _f_t]),
#             #         calculate_stats(ts_sweep, self.interpolate_genetic_map(ts_sweep))[
#             #             -1
#             #         ].values.flatten()[44:],
#             #     ]
#             # )

#     def interpolate_genetic_map(self, ts):
#         _coordinates = np.array(
#             [(self.parameters.slim_region[i], i) for i in ts.sites_position]
#         )

#         if self.parameters.recombination_map is None:
#             recombination_hapmap = np.column_stack(
#                 [
#                     np.repeat(1, ts.sites_position.size),
#                     np.arange(1, ts.sites_position.size + 1),
#                     _coordinates[:, 1],
#                     _coordinates[:, 1],
#                 ]
#             )
#         else:
#             f = interp1d(
#                 self.parameters.recombination_map.physical.values,
#                 self.parameters.recombination_map.genetic.values,
#             )
#             recombination_hapmap = np.column_stack(
#                 [
#                     np.repeat(1, ts.sites_position.size),
#                     np.arange(1, ts.sites_position.size + 1),
#                     _coordinates[:, 1],
#                     f(_coordinates[:, 0]),
#                 ]
#             )

#         return recombination_hapmap

#     def update_params(self, parameters):
#         self.model = parameters
