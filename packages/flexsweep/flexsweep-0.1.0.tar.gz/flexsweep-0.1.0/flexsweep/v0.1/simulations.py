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

from scipy.interpolate import interp1d
from mpmath import exp
from contextlib import redirect_stdout
from functools import partial
from itertools import product, chain
from copy import deepcopy
from dataclasses import dataclass, field

from collections import defaultdict, namedtuple
from joblib import Parallel, delayed


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
    sweep_status: str
    sweep_timing: str
    annotation: str = "exons"
    f_i: list = field(default_factory=lambda: [0.05, 0.1, 0.15, 0.2])
    f_t: list = field(default_factory=lambda: np.arange(0.2, 1.1, 0.1))
    shape: float = 0
    mean_strength: float = 0
    proportions: list = field(default_factory=lambda: [0, 0])
    burn_in: int = 1
    rescale_factor: int = 1
    dominance: float = 0.5
    filter_sim: bool = False
    Ne: int = 1e4
    sweep_diffusion_time: list = field(
        default_factory=lambda: {
            "hard": {},
            "soft": {},
            "hard_incomplete": {},
            "soft_complete": {},
            "soft_incomplete": {},
        }
    )

    def diffusion_time_value(self, N, s, f_i, f_t, c=2) -> float:
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

    def diffusion_time(self, N):
        current_sweep = self.sweep_class

        if (
            len(self.sweep_diffusion_time[current_sweep]) != 0
            and list(self.sweep_diffusion_time[current_sweep].keys()) == self.f_t
        ):
            print("Diffusion mean time is estimated")
        else:
            func = np.vectorize(self.diffusion_time_value)
            # s_v = np.arange(20,1001,1)
            # Correcting SLIM 1+s vs diffusion 1+2s on AA
            s_v = np.arange(10, 400, 1)

            if self.sweep_class == "hard":
                for i in self.f_t:
                    t_fix = func(N, s_v, 1 / (2 * N), i).astype(int)
                    s_t = np.vstack([s_v, t_fix]).T
                    self.sweep_diffusion_time[current_sweep][round(i, 2)] = s_t
            elif self.sweep_class == "soft":
                iterables = np.array(list(product(self.f_t, self.f_i)))
                iterables = iterables[iterables[:, 1] < iterables[:, 0]]

                for end, start in iterables:
                    # for (end,start) in tqdm(iterables,desc="Diffusion mean time"):

                    t_fix = func(N, s_v, start, end).astype(int)
                    s_t = np.vstack([s_v, t_fix]).T

                    if round(end, 1) not in self.sweep_diffusion_time[current_sweep]:
                        self.sweep_diffusion_time[current_sweep][round(end, 1)] = {}
                        self.sweep_diffusion_time[current_sweep][round(end, 1)].update(
                            {start: s_t}
                        )
                    else:
                        self.sweep_diffusion_time[current_sweep][round(end, 1)].update(
                            {start: s_t}
                        )

    def check_stdpopsim(self, return_df=True):
        out = {}
        for i in stdpopsim.all_species():
            tmp_specie = stdpopsim.get_species(i.id)
            tmp_models = ", ".join([i.id for i in tmp_specie.demographic_models])
            tmp_dfes = ", ".join([i.id for i in tmp_specie.demographic_models])
            tmp_genetic_maps = ", ".join([i.id for i in tmp_specie.genetic_maps])
            out[i.id] = {
                "models": tmp_models,
                "genetic_maps": tmp_genetic_maps,
                "dfes": tmp_dfes,
            }

        print(
            "\n\nPlease check the available specie and the asociated annotation, dfe and demographic model\n"
        )
        if return_df:
            out = pd.DataFrame(out).T
        return out

    def check_parameters(self):
        assert self.specie in [
            i.id for i in stdpopsim.all_species()
        ], "Please select a correct species among the catalog: {}".format(
            [i.id for i in stdpopsim.all_species()]
        )
        assert "yaml" in self.demes or self.demes in np.array(
            [i.id for i in stdpopsim.all_demographic_models()]
            + ["PiecewiseConstantSize"]
        ), "Please select a correct demographic model among the catalog: {}".format(
            [i.id for i in stdpopsim.all_demographic_models()]
        )
        assert (
            self.annotation == "exons" or self.annotation == "cds"
        ), "Please select cds or exon annotations"
        assert (
            self.dfe == "neutral"
            or self.dfe == "custom"
            or self.dfe in [i.id for i in stdpopsim.all_dfes()]
        ), "Please select cds or exon annotations"
        assert self.sweep_class in [
            "hard",
            "soft",
        ], "Please select one the following categories: {}".format(["hard", "soft"])
        assert self.sweep_timing in [
            "young",
            "old",
        ], "Please select one the following categories: {}".format(["young", "old"])
        assert self.sweep_status in [
            "complete",
            "incomplete",
        ], "Please select one the following categories: {}".format(
            ["complete", "incomplete"]
        )


hard_params = parameters(
    specie="HomSap",
    region="chr2:135212517-136412517",
    genetic_map="Uniform",
    dfe="neutral",
    demes="PiecewiseConstantSize",
    sample={"AFR": 100},
    sweep_class="hard",
    sweep_status="incomplete",
    sweep_timing="young",
    burn_in=1,
    rescale_factor=10,
    filter_sim=False,
)


def deleterious_dfe(id, del_dfe, proportions, dominance=0.5):
    muts = [
        stdpopsim.MutationType(
            dominance_coeff=dominance, distribution_type="f", distribution_args=[0]
        )
    ]

    muts.append(
        stdpopsim.MutationType(
            dominance_coeff=dominance, distribution_type="g", distribution_args=del_dfe
        )
    )
    return stdpopsim.DFE(
        id=id,
        description=id,
        long_description=id,
        mutation_types=muts,
        proportions=proportions,
    )


def neutral_dfe(id, dominance=0.5):
    muts = [
        stdpopsim.MutationType(
            dominance_coeff=dominance, distribution_type="f", distribution_args=[0]
        )
    ]
    return stdpopsim.DFE(
        id=id, description=id, long_description=id, mutation_types=muts, proportions=[1]
    )


def simulate(
    parameters,
    nthreads=1,
    sweep_replicas=1,
    timeout=180,
    output_folder=None,
    keep_simulations=False,
    max_tries=3,
):
    parameters.check_parameters()

    species = stdpopsim.get_species(parameters.specie)

    parameters.Ne = species.population_size

    if parameters.rescale_factor < 10:
        timeout = timeout * 10 / parameters.rescale_factor
    elif parameters.rescale_factor > 10:
        timeout = timeout * 1 / parameters.rescale_factor

    current_sweep = "_".join([parameters.sweep_class, parameters.sweep_status])

    if "yaml" in parameters.demes:
        pop_history = demes.load(parameters.demes)
        model = msprime.Demography().from_demes(pop_history)
        model = stdpopsim.DemographicModel(
            id=parameters.demes.split("/")[-1].split(".")[0],
            description="custom",
            long_description="custom",
            model=model,
        )
    elif parameters.demes == "PiecewiseConstantSize":
        model = stdpopsim.PiecewiseConstantSize(species.population_size)
        model.generation_time = species.generation_time
        # Force to sample to pop0 is PiecewiseConstantSize selected
        sample_tmp = {"pop_0": list(parameters.sample.values())[0]}
        parameters.sample = sample_tmp
    else:
        model = species.get_demographic_model(parameters.demes)

    if parameters.annotation == "exons":
        annotation = 0
    else:
        annotation = 1

    if parameters.dfe == "neutral":
        dfe = neutral_dfe(parameters.dfe)
    elif parameters.dfe == "deleterious":
        dfe = deleterious_dfe(
            parameters.dfe,
            [parameters.shape / parameters.mean_strength, parameters.shape],
            parameters.proportions,
        )
    else:
        dfe = species.get_dfe(parameters.dfe)

    chrom = parameters.region.split(":")[0]
    region = list(map(int, parameters.region.split(":")[1].split("-")))

    # Need to save original map
    if parameters.genetic_map in [i.id for i in species.genetic_maps]:
        contig = species.get_contig(
            chrom,
            genetic_map=parameters.genetic_map,
            mutation_rate=model.mutation_rate,
            left=region[0],
            right=region[1],
        )

        _rec_path = str(species.get_genetic_map(parameters.genetic_map).map_cache_dir)
        _rec_map = pd.read_csv(
            _rec_path + "/" + _rec_path.split("/")[-1] + "_" + chrom + ".txt", sep=" "
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

    elif parameters.genetic_map.lower() == "uniform":
        contig = species.get_contig(
            chrom, mutation_rate=model.mutation_rate, left=region[0], right=region[1]
        )
        recombination_map = None
    else:
        contig = species.get_contig(
            chrom, mutation_rate=model.mutation_rate, left=region[0], right=region[1]
        )
        rate_map = msprime.RateMap.read_hapmap(parameters.genetic_map)
        rate_map_sliced = rate_map.slice(left=region[0], right=region[1], trim=True)
        contig.recombination_map = rate_map_sliced

        _rec_map = pd.read_csv(parameters.genetic_map, sep="\t")
        _rec_map = _rec_map[_rec_map.iloc[:, 0] == chrom]
        recombination_map = pd.DataFrame(
            {
                "chrom": chrom,
                "id": _rec_map.index,
                "genetic": _rec_map.iloc[:, -1],
                "physical": _rec_map.iloc[:, 1],
            }
        )

    slim_region = {i: v for (i, v) in enumerate(range(region[0], region[1] + 1))}
    raw_annotation = species.get_annotations(species.annotations[annotation].id)
    annotations_intervals = raw_annotation.get_chromosome_annotations(chrom)

    contig.add_dfe(intervals=annotations_intervals, DFE=dfe)

    if len(parameters.sweep_diffusion_time[parameters.sweep_class]) == 0:
        logging.info(
            "Solving diffusion times for {0} sweeps".format(parameters.sweep_class)
        )
        parameters.diffusion_time(parameters.Ne)

    t, s, f_i, f_t, _burn_in = timing_selection(parameters, sweep_replicas, 5000, 200)

    # Folder to save simulations. Keep_simulations will add sweep_replicas from last simulated iteration
    simulated_list = np.arange(sweep_replicas)
    if output_folder is not None:
        os.makedirs(output_folder + "/sweeps/", exist_ok=True)
        # os.makedirs(output_folder + "/neutral/", exist_ok=True)
        if keep_simulations:
            simulated_list = glob.glob(output_folder + "/sweeps/*trees")

            simulated_list = np.array(
                [
                    x.replace(output_folder + "/sweeps/", "")
                    .replace("sweep_", "")
                    .replace(".trees", "")
                    for x in simulated_list
                ],
                dtype=int,
            ).max()

            simulated_list = np.arange(
                simulated_list + 1, simulated_list + sweep_replicas + 1
            )

    # Aa have fitness 1+s and AA have fitness 1+2s in diffusion theory
    # SLIM set AA fitness == 1+s and Aa fitness == 1+s/2
    # Correcting s as s=alpha/N instead s=alpha/2N to approximate mean times properly
    # s = alpha/2N do not satified estimated times. Infinity conditions on SLIM
    # pars = [(model,deepcopy(contig),parameters.sample,parameters.sweep_class,parameters.sweep_status,parameters.burn_in,parameters.rescale_factor,f_i[i],f_t[i],t[i],s[i]/(N)) for i in range(sweep_replicas)]

    pars = [
        (
            model,
            contig,
            parameters.sample,
            parameters.sweep_class,
            parameters.sweep_status,
            _burn_in[i],
            parameters.rescale_factor,
            f_i[i],
            f_t[i],
            t[i],
            s[i] / parameters.Ne,
            v,
        )
        for (i, v) in enumerate(simulated_list)
    ]

    # SLIM simulations. Return index error if cannot fit the conditions due to errors or timeout condition
    logging.info("Starting sweeps simulations")
    sims = pool_exec(
        sweep_simulation,
        pars,
        recombination_map,
        slim_region,
        nthreads,
        output_folder,
        timeout,
        1,
    )

    sims_k = list(sims.keys())
    sims = tuple(sims.values())

    print(
        "\n{0}/{1} sweep simulations were performed".format(len(sims), sweep_replicas)
    )

    _errors = sweep_replicas - len(sims)

    if _errors != 0:
        print("Re-running simulations")
        sims_retry = []
        for i in range(max_tries):
            if nthreads > _errors:
                nthreads = _errors

            simulated_list = np.setdiff1d(simulated_list, sims_k)

            sims_tries, sims_k = retry_simulation(
                parameters,
                simulated_list,
                contig,
                model,
                recombination_map,
                slim_region,
                timeout,
                nthreads,
                output_folder,
            )

            _errors = _errors - len(sims_tries)
            sims_retry.append(sims_tries)

            # Stop if finish or tries ends
            if _errors == 0:
                break

        sims_retry = tuple(chain(*sims_retry))
        sims = sims + sims_retry

    if output_folder is not None:
        if keep_simulations:
            sims_old = read_simulations(output_folder)
            sims = sims_old + sims
        with open(output_folder + "/sims.pickle", "wb") as handle:
            pickle.dump(sims, handle)

    # return tuple(sims.values())
    return sims


def pool_exec(
    f,
    pars,
    recombination_map,
    slim_region,
    nthreads=1,
    output_folder=None,
    timeout=180,
    batch_size=1,
):
    f_maps = partial(
        interpolate_genetic_map,
        recombination_map=recombination_map,
        slim_region=slim_region,
    )

    def process_sim(p, timeout):
        try:
            result = f(p, timeout)
            r_map = f_maps(result[1])

            if output_folder is None:
                return result + (r_map,)
            else:
                result[1].dump(
                    output_folder + "/sweeps/sweep_" + str(result[0]) + ".trees"
                )
                return (
                    (result[0],)
                    + (output_folder + "/sweeps/sweep_" + str(result[0]) + ".trees",)
                    + (result[-1],)
                    + (r_map,)
                )
        except:
            return None

    # Use joblib to parallelize the execution
    sims_p = Parallel(n_jobs=nthreads, batch_size=batch_size, verbose=2)(
        delayed(process_sim)(p, timeout) for p in pars
    )

    sims_p = [s for s in sims_p if s is not None]

    keys, *values = zip(*sims_p)
    sims_dict = dict(zip(keys, zip(*values)))

    return sims_dict


def sweep_simulation(p, timeout=180):
    (
        _model,
        _contig,
        _sample,
        _sweep_class,
        _sweep_status,
        _burn_in,
        _rescale_factor,
        _f_i,
        _f_t,
        _t,
        _s,
        _iter,
    ) = p

    # adaptive_position = np.random.randint(1.2e6*0.25,1.2e6*0.75)
    adaptive_position = sum(_contig.original_coordinates[1:]) / 2

    _contig.add_single_site(id=_sweep_class, coordinate=adaptive_position)

    if _sweep_class == "hard":
        extended_events = stdpopsim.ext.selective_sweep(
            single_site_id=_sweep_class,
            population=list(_sample.keys())[0],
            selection_coeff=_s,
            min_freq_at_end=_f_t,
            mutation_generation_ago=_t,
        )
    else:
        # start_generation_ago _t + 5000 to ensure the soft sweep achieve the desired freq (up to 0.25)
        extended_events = stdpopsim.ext.selective_sweep(
            single_site_id=_sweep_class,
            population=list(_sample.keys())[0],
            selection_coeff=_s,
            min_freq_at_start=_f_i,
            min_freq_at_end=_f_t,
            mutation_generation_ago=_t + 5000,
            start_generation_ago=_t,
        )

    if _sweep_class == "soft":
        end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
            start_time=_t,
            end_time=_t,
            single_site_id=_sweep_class,
            population=list(_sample)[0],
            op="<",
            allele_frequency=_f_i + 0.1,
        )

        extended_events.append(end_condition)

    if _f_t != 1:
        f_step = 0.1 if _f_t == 0.9 else 0.1
        end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
            start_time=0,
            end_time=0,
            single_site_id=_sweep_class,
            population=list(_sample)[0],
            op="<",
            allele_frequency=_f_t + 0.1,
        )

        extended_events.append(end_condition)

    engine = stdpopsim.get_engine("slim")

    with open("/home/jmurgamoreno/test.slim", "w") as f:
        with redirect_stdout(f):
            ts_sweep = engine.simulate(
                _model,
                _contig,
                _sample,
                extended_events=extended_events,
                slim_scaling_factor=_rescale_factor,
                slim_burn_in=_burn_in,
                slim_script=True,
                verbosity=0,
            )

    def timeout_handler(signum, frame):
        raise TimeoutError("Execution timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    timeout_occurred = False
    try:
        ts_sweep = engine.simulate(
            _model,
            _contig,
            _sample,
            extended_events=extended_events,
            slim_scaling_factor=_rescale_factor,
            slim_burn_in=_burn_in,
        )
    except TimeoutError:
        timeout_occurred = True
    finally:
        signal.alarm(0)

    if timeout_occurred:
        return (_iter, None, None)
    else:
        if _f_t != 1:
            _f_t = frequency(ts_sweep, 6e5)
        return (_iter, ts_sweep, np.column_stack([_s, _t, _f_i, _f_t]))


def timing_selection(parameters, sweep_replicas, t_lower, t_upper):
    if parameters.sweep_class == "hard":
        f_i = np.repeat(1 / parameters.Ne, sweep_replicas)
    else:
        f_i = np.random.uniform(
            parameters.f_i[0], parameters.f_i[-1], sweep_replicas
        ).round(2)

    f_t = np.random.uniform(
        parameters.f_t[0], parameters.f_t[-1], sweep_replicas
    ).round(1)
    # Otherwise cannot find any parameter combination
    f_t[np.where(f_t - f_i.round(1) < 0.2)[0]] = (
        f_t[np.where(f_t - f_i.round(1) < 0.2)[0]] + 0.2
    )

    s = []
    t = []
    for i, j in zip(f_t.round(1), f_i):
        if i == 1:
            _t, _s = timing_selection_complete_sweep(parameters, i, j, t_lower, t_upper)
        else:
            _t, _s = timing_selection_incomplete_sweep(
                parameters, i, j, t_lower, t_upper
            )

        t.append(_t)
        s.append(_s)

    t = np.hstack(t)
    s = np.hstack(s)

    if parameters.sweep_class == "hard":
        # Reduce _burn_in but increasing a little bit to avoid problems drawing the mutation
        _burn_in = ((t + 1) / parameters.Ne).round(2)
        _burn_in = _burn_in + 0.01
    else:
        # Neutral arise 5000 gens ago from selection
        _burn_in = ((t + 5001) / parameters.Ne).round(2)

    return t, s, f_i, f_t, _burn_in


def timing_selection_complete_sweep(parameters, i, j, t_lower, t_upper):
    current_sweep = parameters.sweep_class

    t = []
    s = []
    # for (i,j) in tqdm(zip(f_t,f_i),total=f_i.size,desc="Sampling uniform t [{0},{1}] and s [{2},{3}]".format(t_lower,t_upper,20,1000)):

    s_t_lower = parameters.sweep_diffusion_time[current_sweep][1]

    if parameters.sweep_class == "soft":
        s_t_lower = s_t_lower[round(j + 0.01, 1)]

    _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
    _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

    while _s.size == 0:
        _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
        _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

    _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)

    return (_t, _s)


def timing_selection_incomplete_sweep(parameters, i, j, t_lower, t_upper):
    current_sweep = parameters.sweep_class

    t = []
    s = []

    # for k,(i,j) in tqdm(enumerate(zip(f_t,f_i)),total=f_i.size,desc="Sampling uniform t [{0},{1}] and s [{2},{3}]".format(t_lower,t_upper,20,1000)):

    s_t_lower = parameters.sweep_diffusion_time[current_sweep][round(i, 1)]
    s_t_upper = parameters.sweep_diffusion_time[current_sweep][round(i + 0.1, 1)]

    # We search for the previous diffusion mean value to ensure the condition.
    # Otherwise the rounded values search for the nearest estimated value and some condition cannot achieve because of the arise time is shorter than expected
    # Diffusion value are estimated in the range [0:0.05:1]
    if j > 0.05:
        _j = round(round(j, 1) - 0.05, 2)
    else:
        _j = j

    if parameters.sweep_class == "soft":
        # Check rounded init frequency not equal or greater than end frequence.
        # Otherwise change value and array.
        while _j >= i:
            _j = round(np.random.uniform(parameters.f_i[0], j), 2)

            if _j > 0.05:
                _j = round(round(j, 1) - 0.05, 2)

            f_i[k] = _j

        s_t_lower = s_t_lower[_j]
        s_t_upper = s_t_upper[_j]

    _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
    s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
    s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
    _s = np.intersect1d(s_lower, s_upper)

    while _s.size == 0:
        _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
        s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
        s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
        _s = np.intersect1d(s_lower, s_upper)

    _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)

    return (_t, _s)


def interpolate_genetic_map(ts, recombination_map, slim_region):
    _coordinates = np.array([(slim_region[i], i) for i in ts.sites_position])

    if recombination_map is None:
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
            recombination_map.physical.values, recombination_map.genetic.values
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


def frequency(ts, position):
    pos = ts.sites_position
    g = ts.genotype_matrix()[np.where(pos == position)[0]]

    if np.any(g == 2):
        g[g == 2] = 0

    freq = g.sum() / (ts.num_individuals * 2)

    return freq


def neutral_simulation(p, timeout=180):
    (
        _model,
        _contig,
        _sample,
        _sweep_class,
        _sweep_status,
        _burn_in,
        _rescale_factor,
        _f_i,
        _f_t,
        _t,
        _s,
        _iter,
    ) = p

    # adaptive_position = np.random.randint(1.2e6*0.25,1.2e6*0.75)

    engine = stdpopsim.get_engine("msprime")

    def timeout_handler(signum, frame):
        raise TimeoutError("Execution timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    timeout_occurred = False
    try:
        ts_neutral = engine.simulate(
            _model,
            _contig,
            _sample,
        )
    except TimeoutError:
        timeout_occurred = True
    finally:
        signal.alarm(0)

    if timeout_occurred:
        return (_iter, None, None)
    else:
        return (_iter, ts_neutral)


def read_simulations(folder_path: str):
    with open(folder_path + "/sims.pickle", "rb") as handle:
        tmp = pickle.load(handle)

    return tmp


def plot_tree(ts, position, path):
    ts.at(position).draw_svg(
        path,
        size=(2000, 1000),
        node_labels={},  # Remove all node labels for a clearer viz
    )


# Check pop size when beneficial mutation is added
def check_ne(model, parameters):
    dd = model.model.debug()

    epochs = sorted(dd.epochs, key=lambda e: e.start_time, reverse=True)
    T = [round(e.start_time * demographic_model.generation_time) for e in epochs]

    N = np.empty(shape=(dd.num_populations, len(epochs)), dtype=int)

    for j, epoch in enumerate(epochs):
        for i, pop in enumerate(epoch.populations):
            N[i, j] = int(pop.end_size * contig.ploidy / 2)


def retry_simulation(
    parameters,
    _errors,
    contig,
    model,
    recombination_map,
    slim_region,
    timeout,
    nthreads,
    output_folder,
):
    _errors_n = len(_errors)

    t, s, f_i, f_t, _burn_in = timing_selection(parameters, _errors_n, 5000, 200)

    # Folder to save simulations. Keep_simulations will add sweep_replicas from last simulated iteration
    if output_folder is not None:
        os.makedirs(output_folder + "/sweeps/", exist_ok=True)
        # os.makedirs(output_folder + "/neutral/", exist_ok=True)

    # Aa have fitness 1+s and AA have fitness 1+2s in diffusion theory
    # SLIM set AA fitness == 1+s and Aa fitness == 1+s/2
    # Correcting s as s=alpha/N instead s=alpha/2N to approximate mean times properly
    # s = alpha/2N do not satified estimated times. Infinity conditions on SLIM
    # pars = [(model,deepcopy(contig),parameters.sample,parameters.sweep_class,parameters.sweep_status,parameters.burn_in,parameters.rescale_factor,f_i[i],f_t[i],t[i],s[i]/(N)) for i in range(sweep_replicas)]

    pars = [
        (
            model,
            contig,
            parameters.sample,
            parameters.sweep_class,
            parameters.sweep_status,
            _burn_in[i],
            parameters.rescale_factor,
            f_i[i],
            f_t[i],
            t[i],
            s[i] / parameters.Ne,
            v,
        )
        for (i, v) in enumerate(_errors)
    ]

    # SLIM simulations. Return index error if cannot fit the conditions due to errors or timeout condition
    logging.info("Starting sweeps simulations")
    sims_r = pool_exec(
        sweep_simulation,
        pars,
        recombination_map,
        slim_region,
        nthreads,
        output_folder,
        timeout,
        1,
    )

    return tuple(sims_r.values()), list(sims_r.keys())
