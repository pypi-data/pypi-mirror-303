"""Summary

Attributes:
    diffusion_mean_time_v (TYPE): Description
"""
import stdpopsim
import msprime
import demes
import numpy as np
import pandas as pd
import scipy.integrate as integrate
from mpmath import exp
from contextlib import redirect_stdout
from multiprocessing import Pool
from copy import deepcopy
from dataclasses import dataclass, field
from tqdm import tqdm
import attr


@dataclass
class Parameters:
    """
    Create a class container to automatize sweep simulations using stdpopsim.
    """

    specie: str
    region: str
    genetic_map: str
    dfe: str
    demog: str
    sample: dict
    sweep_class: str
    sweep_status: str
    sweep_timing: str
    annotation: str = "exons"
    shape: float = 0.184
    mean_strength: float = -457
    proportions: list = field(default_factory=lambda: [0.25, 0.75])
    burn_in: int = 10
    rescale_factor: int = 10
    dominance: float = 0.5
    sweep_diffusion_time: list = field(default_factory=lambda: {})

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
        f = np.vectorize(self.diffusion_time_value)
        s_v = np.arange(20, 1001, 1)
        for i in tqdm(np.arange(0.2, 1.1, 0.1), desc="Diffusion mean time"):
            t_fix = f(N, s_v, 1 / (2 * N), i).astype(int)
            s_t = np.vstack([s_v, t_fix]).T
            self.sweep_diffusion_time[i.round(1)] = s_t


params = Parameters(
    specie="HomSap",
    region="chr2:135212517-136412517",
    genetic_map="/home/murgamoreno/Flex-sweep/FlexABC/data/decode_chr2_sexavg_2019.txt",
    dfe="Gamma_K17",
    demog="/home/murgamoreno/Flex-sweep/FlexABC/data/OutOfAfrica_2T12.yaml",
    sample={"AFR": 50},
    sweep_class="hard",
    sweep_status="incomplete",
    sweep_timing="young",
)

params.diffusion_time = params.diffusion_time(1e4)


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


def check_params(params):
    assert params.specie in [
        i.id for i in stdpopsim.all_species()
    ], "Please select a correct species among the catalog: {}".format(
        [i.id for i in stdpopsim.all_species()]
    )
    assert "yaml" in params.demog or params.demog in [
        i.id for i in stdpopsim.all_demographic_models()
    ], "Please select a correct demographic model among the catalog: {}".format(
        [i.id for i in stdpopsim.all_demographic_models()]
    )
    assert (
        params.annotation == "exons" or params.annotation == "cds"
    ), "Please select cds or exon annotations"
    assert (
        params.dfe == "neutral"
        or params.dfe == "custom"
        or params.dfe in [i.id for i in stdpopsim.all_dfes()]
    ), "Please select cds or exon annotations"
    assert params.sweep_class in [
        "hard",
        "soft",
    ], "Please select one the following categories: {}".format(["hard", "soft"])
    assert params.sweep_timing in [
        "young",
        "old",
    ], "Please select one the following categories: {}".format(["young", "old"])
    assert params.sweep_status in [
        "complete",
        "incomplete",
    ], "Please select one the following categories: {}".format(
        ["complete", "incomplete"]
    )


def mean_fixation_time(N, s, c=2):
    return (2 * np.log(c * N - 1)) / s


def s_mean_fixation_time(N, t, c=2):
    return (2 * np.log(c * N - 1)) / t


def s_limits(sweep_timing, sweep_status, N, replicas):
    # Define s range based on time and status.
    # Sweep cannot be young and complete unless s > s'
    # Sweep cannot be old and incomplete unless s < s'
    if (sweep_timing == "young") and (sweep_status == "complete"):
        s = np.random.uniform(600, 1000, replicas) / (2 * N)
    elif (sweep_timing == "young") & (sweep_status == "incomplete"):
        s = np.random.uniform(20, 1000, replicas) / (2 * N)
    elif (sweep_timing == "old") and (sweep_status == "complete"):
        s = np.random.uniform(20, 400, replicas) / (2 * N)
    elif (sweep_timing == "old") and (sweep_status == "incomplete"):
        s = np.random.uniform(20, 40, replicas) / (2 * N)

    s = s.round(5)

    return s


def conditioning_limits_by_t(N, s, s_t, t_max, t_min):
    # Define s range based on time .
    # Sweep cannot be young and complete unless s > s'
    # Sweep cannot be old and complete unless s < s'
    ## CHECK INCOMPLETE!

    return s


def conditioning_limits_by_s(N, s, s_t, t_max, t_min):
    # Define s range based on time .
    # Sweep cannot be young and complete unless s > s'
    # Sweep cannot be old and complete unless s < s'
    ## CHECK INCOMPLETE!

    t = []
    for j in range(s.size):
        # Subset mean to f given a random s value
        t_fix = s_t[s_t[:, 0] == s[j], 1][0]
        # t_fix = (t_fix * 0.25) + t_fix
        if t_fix < t_min:
            t_fix = t_min
        _t = np.random.uniform(t_max, t_fix)
        t.append(_t)

    t = np.array(t).astype(int)

    return t


def simulate(params, nthreads, replicas=1, recombination_rate=False):
    check_params(params)

    species = stdpopsim.get_species(params.specie)

    if "yaml" in params.demog:
        pop_history = demes.load(params.demog)
        model = msprime.Demography().from_demes(pop_history)
        model = stdpopsim.DemographicModel(
            id=params.demog.split("/")[-1].split(".")[0],
            description="custom",
            long_description="custom",
            model=model,
        )
    else:
        model = species.get_demographic_model(params.demog)

    if params.annotation == "exons":
        annotation = 0
    else:
        annotation = 1

    if params.dfe == "neutral":
        dfe = neutral_dfe(params.dfe)
    elif params.dfe == "deleterious":
        dfe = deleterious_dfe(
            params.dfe,
            [params.shape / params.mean_strength, params.shape],
            params.proportions,
        )
    else:
        dfe = species.get_dfe(params.dfe)

    chrom = params.region.split(":")[0]
    region = list(map(int, params.region.split(":")[1].split("-")))

    if params.genetic_map in [i.id for i in species.genetic_maps]:
        contig = species.get_contig(
            chrom,
            genetic_map=params.genetic_map,
            mutation_rate=model.mutation_rate,
            left=region[0],
            right=region[1],
        )
    elif params.genetic_map == "uniform":
        contig = species.get_contig(
            chrom, mutation_rate=model.mutation_rate, left=region[0], right=region[1]
        )
    else:
        contig = species.get_contig(
            chrom, mutation_rate=model.mutation_rate, left=region[0], right=region[1]
        )

        rate_map = msprime.RateMap.read_hapmap(params.genetic_map)
        rate_map = rate_map.slice(left=region[0], right=region[1], trim=True)
        contig.recombination_map = rate_map

    raw_annotation = species.get_annotations(species.annotations[annotation].id)
    annotations_intervals = raw_annotation.get_chromosome_annotations(chrom)
    N = species.population_size

    contig.add_dfe(intervals=annotations_intervals, DFE=dfe)

    if params.sweep_class == "hard":
        f_i = np.repeat(1 / species.population_size, replicas)
    else:
        f_i = np.random.uniform(
            1 / model.model.debug().population_size_history[0][-1], 0.25, replicas
        ).round(2)

    if params.sweep_timing == "old":
        t_lower, t_upper = (5000, 2000)
    else:
        t_lower, t_upper = (2000, 200)

    if params.sweep_status == "complete":
        f_t = np.repeat(1, replicas)

        t = []
        s = []
        for i in f_t:
            s_t_lower = params.sweep_diffusion_time[i.round(1)]

            _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
            _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

            while _s.size == 0:
                _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
                _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

            _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)

            t.append(_t)
            s.append(_s)

        t = np.hstack(t)
        s = np.hstack(s)
    else:
        f_t = np.random.uniform(0.2, 0.9, replicas).round(1)

        t = []
        s = []
        for i in f_t:
            s_t_lower = params.sweep_diffusion_time[i.round(1)]
            s_t_upper = params.sweep_diffusion_time[(i + 0.1).round(1)]
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

            t.append(_t)
            s.append(_s)

        t = np.hstack(t)
        s = np.hstack(s)

    # List of simulations, model, contig and sample are constant varaibles.
    pars = [
        (
            deepcopy(model),
            deepcopy(contig),
            params.sample,
            params.sweep_class,
            params.sweep_status,
            params.burn_in,
            params.rescale_factor,
            f_i[i],
            f_t[i],
            t[i],
            s[i] / (N),
        )
        for i in range(replicas)
    ]

    print("Running {0} simulations into {1} threads".format(replicas, nthreads))

    pool = Pool(processes=nthreads)
    sims = pool.starmap(sweep_simulation, zip(pars))
    pool.close()

    if recombination_rate:
        return (sims, np.vstack([s / N, t]).T, contig.recombination_map)
    else:
        return (sims, np.vstack([s / N, t]).T)


def sweep_simulation(p, recipe="/home/murgamoreno/sweep.slim"):
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
    ) = p

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
        # start_generation_ago _t - 1000 to ensure the soft sweep achieve the desired freq (up to 0.25)
        extended_events = stdpopsim.ext.selective_sweep(
            single_site_id=_sweep_class,
            population=list(_sample.keys())[0],
            selection_coeff=_s,
            min_freq_at_end=_f_t,
            mutation_generation_ago=_t + (_t * 0.1),
            start_generation_ago=_t - 1000,
        )

    if _sweep_status == "incomplete":
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

    engine = stdpopsim.get_engine("slim")
    with open(recipe, "w") as f:
        with redirect_stdout(f):
            ts_sweep = engine.simulate(
                _model,
                _contig,
                params.sample,
                extended_events=extended_events,
                slim_scaling_factor=10,
                slim_burn_in=10,
                slim_script=True,
                verbosity=0,
            )

    ts_sweep = engine.simulate(
        _model,
        _contig,
        _sample,
        extended_events=extended_events,
        slim_scaling_factor=10,
        slim_burn_in=10,
    )

    return ts_sweep


def filter_biallelics(hap):
    non_biallelic_sites = np.unique(np.where((hap != 1) & (hap != 0))[0])

    biallelic_sites = np.arange(0, hap.shape[0])
    biallelic_sites = np.setdiff1d(biallelics, non_biallelics)

    return (hap[biallelic_sites, :], biallelic_sites)


def write_hap(ts, hap, map, recombination_rate=None):
    hap, biallelic_sites = filter_biallelics(ts.genotype_matrix())

    positions = ts.sites_position[biallelic_sites].astype(int)

    # if recombination_rate is not None:
    # else:

    pd.DataFrame(hap).to_csv(hap, index=False, header=False, sep=" ")
    pd.DataFrame(
        {
            "chrom": 1,
            "locus": np.arange(0, positions.size),
            "physical_pos": positions,
            "genetic_pos": positions,
        }
    ).to_csv(hap, index=False, header=False, sep="")


###############
import itertools
import warnings
from plotnine import *
from tskit import write_ms


params.genetic_map = "uniform"
out = []
for i in itertools.product(["young", "old"], ["complete", "incomplete"]):
    print(i)
    params.sweep_timing = i[0]
    params.sweep_status = i[1]

    trees, coeffs, r_rate = simulate(
        params, nthreads=5, replicas=10, recombination_rate=True
    )
    tmp = summary_statistics(trees, coeffs, r_rate, nthreads=5)
    tmp = pd.concat(tmp)
    tmp[["simulation"]] = "hard_" + "_".join(i)
    tmp[["r_pos"]] = 0.5

    out.append(tmp)

x = pd.concat(out).reset_index()

# df.f_t = df.f_t.round(1)

# ggplot(df[(df.isafe >=0.1) & (df.simulation == 'hard_young_incomplete')],aes(x='pos',y='isafe')) + geom_point() + facet_wrap('~f_t+r_pos') + geom_vline(aes(xintercept = 6e5)) + theme_bw()


def pool_stats(f, sims_class, nthreads):
    pars = [(i[0], i[1]) for i in sims_class]

    # Log the start of the scheduling
    logging.info("Task scheduling started")

    # progress_bar = tqdm(desc='Simulating {0} {1} {2} {3} sweeps into {4} threads'.format(len(pars),params.sweep_class,params.sweep_timing,params.sweep_status,nthreads),total=len(pars))
    progress_bar = tqdm(total=len(pars))
    with concurrent.futures.ProcessPoolExecutor(max_workers=nthreads) as executor:
        # Start the load operations and mark each future with its input value
        future_to_result = {
            executor.submit(f, ts, rec_map): i for i, (ts, rec_map) in enumerate(pars)
        }

        summ_stats = {}
        errors = []
        for completed in concurrent.futures.as_completed(future_to_result):
            # iterate over the completed futures
            iter_sim = future_to_result[completed]
            try:
                # Get the result of the completed future, or raise a TimeoutError if it timed out
                result = completed.result(timeout=None)
                summ_stats[iter_sim] = result
            except Exception as e:
                logging.error(f"Estimation failed for iteration {iter_sim}: {e}")
                errors.append(iter_sim)
                progress_bar.refresh()
                progress_bar.close()
                break
            progress_bar.update()

    progress_bar.refresh()
    progress_bar.close()

    return summ_stats, errors


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
    try:
        ts_sweep = engine.simulate(
            _model,
            _contig,
            _sample,
            extended_events=extended_events,
            slim_scaling_factor=_rescale_factor,
            slim_burn_in=_burn_in,
        )
    finally:
        signal.alarm(0)

    return ts_sweep


def neutral_simulation(p, timeout=180):
    (
        _model,
        _contig,
        _sample,
        _sweep_class,
        _sweep_status,
        _burn_in,
        _rescale_factor,
        _rec_map,
        _mu,
    ) = p
    _contig.recombination_map = _rec_map
    _contig.mutation_rate = _mu
    engine = stdpopsim.get_engine("msprime")

    def timeout_handler(signum, frame):
        raise TimeoutError("Execution timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        ts_neutral = engine.simulate(_model, _contig, _sample)
        # with open("/home/jmurgamoreno/test.slim", "w") as f:
        # with redirect_stdout(f):
        #   ts_sweep = engine.simulate(
        #   _model,
        #   _contig,
        #   _sample,
        #   slim_scaling_factor=10,
        #   slim_burn_in=10,
        #   slim_script=True,
        #   verbosity=0,
        # )

    finally:
        signal.alarm(0)

    return ts_neutral


def pool_exec(
    f,
    pars,
    abc_parameters,
    recombination_map,
    slim_region,
    nthreads=1,
    output_folder=None,
    timeout=180,
):
    f_maps = partial(
        interpolate_genetic_map,
        recombination_map=recombination_map,
        slim_region=slim_region,
    )

    # Define a tqdm progress bar with the total number of tasks to be completed
    progress_bar = tqdm(total=len(pars))
    # progress_bar = tqdm(desc='Simulating {0} {1} {2} {3} sweeps into {4} threads'.format(len(pars),parameters.sweep_class,parameters.sweep_timing,parameters.sweep_status,nthreads),total=len(pars))
    with concurrent.futures.ProcessPoolExecutor(max_workers=nthreads) as executor:
        # with concurrent.futures.ThreadPoolExecutor(max_workers=nthreads) as executor:
        # Start the load operations and mark each future with its input value
        future_to_result = {
            executor.submit(f, p, timeout=timeout): i for (i, p) in enumerate(pars)
        }

        sims = defaultdict.fromkeys(range(len(pars)))
        errors = []
        for completed in concurrent.futures.as_completed(
            future_to_result, timeout=None
        ):
            # iterate over the completed futures
            iter_sim = future_to_result[completed]

            try:
                # get the result of the completed future, or raise a TimeoutError if it timed out
                result = completed.result(timeout=None)
                r_map = f_maps(result)

                if f.__name__ == "neutral_simulation":
                    if output_folder is None:
                        sims[iter_sim] = (result, r_map)
                    else:
                        result.dump(
                            output_folder
                            + "/neutral/neutral_"
                            + str(iter_sim)
                            + ".trees"
                        )
                        sims[iter_sim] = (
                            output_folder
                            + "/neutral/neutral_"
                            + str(iter_sim)
                            + ".trees",
                            r_map,
                        )
                else:
                    if output_folder is None:
                        sims[iter_sim] = (result, r_map, abc_parameters[iter_sim, :])
                    else:
                        result.dump(
                            output_folder + "/sweeps/sweep_" + str(iter_sim) + ".trees"
                        )
                        sims[iter_sim] = (
                            output_folder + "/sweeps/sweep_" + str(iter_sim) + ".trees",
                            r_map,
                            abc_parameters[iter_sim, :],
                        )

            except concurrent.futures.TimeoutError:
                # handle the case where the future timed out
                errors.append(iter_sim)
            except Exception as exc:
                # handle any other exceptions that occurred
                errors.append(iter_sim)

            progress_bar.update()

    progress_bar.refresh()
    progress_bar.close()

    return (sims, np.array(errors))


def retry_simulation(
    parameters,
    _errors,
    N,
    contig,
    model,
    recombination_map,
    slim_region,
    timeout,
    nthreads,
    max_tries=3,
):
    abc_parameters = []
    sims = []

    # Iter tries
    for j in range(max_tries):
        if j == 0:
            _errors_j = _errors

        t_lower, t_upper = (5000, 200)
        # New f_t and f_i parameters
        if parameters.sweep_class == "hard":
            _f_t = np.random.uniform(
                parameters.f_t[0], parameters.f_t[-1], sweep_replicas
            ).round(1)
            # Otherwise cannot find any parameter combination
            _f_t[np.where(_f_t - f_i.round(1) < 0.2)[0]] = (
                _f_t[np.where(_f_t - f_i.round(1) < 0.2)[0]] + 0.2
            )
            t, s = timing_selection(parameters, f_t, f_i, t_lower, t_upper)

        # Change t and s
        if parameters.sweep_class == "complete":
            _f_t = np.repeat(1, len(_errors_j))
            _t, _s = timing_selection_complete_sweep(
                parameters, _f_t, _f_i, t_lower, t_upper
            )
        else:
            _f_t = np.random.uniform(0.2, 0.9, len(_errors_j)).round(1)
            _f_t[np.where(_f_t - _f_i.round(1) < 0.2)[0]] = (
                _f_t[np.where(_f_t - _f_i.round(1) < 0.2)[0]] + 0.2
            )

            _t, _s = timing_selection_incomplete_sweep(
                parameters, _f_t, _f_i, t_lower, t_upper
            )

        _pars = [
            (
                model,
                deepcopy(contig),
                parameters.sample,
                parameters.sweep_class,
                parameters.sweep_status,
                parameters.burn_in,
                parameters.rescale_factor,
                _f_i[i],
                _f_t[i],
                _t[i],
                _s[i] / (N),
            )
            for i in range(len(_errors_j))
        ]

        _abc_parameters_j = np.column_stack([_s / N, _t, _f_i, _f_t])

        # Reduce timeout to init faster simulations in during tries
        _sims_j, _errors_j = pool_exec(
            _pars,
            _abc_parameters_j,
            recombination_map,
            slim_region,
            nthreads,
            int(timeout / 2),
        )

        sims.append(_sims_j)
        abc_parameters.append(np.delete(_abc_parameters_j, _errors_j.tolist(), axis=0))

        if len(_errors_j) == 0:
            print("Done, exiting retries.")
            return (sims, abc_parameters)

    return (sims, abc_parameters)
