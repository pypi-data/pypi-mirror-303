import os

# os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["NUMBA_NUM_THREADS"] = "1"
from numba import njit, set_num_threads, config

# set_num_threads(1)
# config.THREADING_LAYER = "workqueue"

import threadpoolctl
import subprocess

threadpoolctl.threadpool_limits(1)

from typing import Tuple, List
import numpy as np
import math
import pandas as pd
from tszip import load

# from isafe.isafeclass import iSafeClass
# from isafe.safeclass import SafeClass
from scipy import interpolate
import gzip
from functools import partial, reduce
import logging
from allel import (
    HaplotypeArray,
    ihs,
    nsl,
    garud_h,
    standardize_by_allele_count,
    sequence_diversity,
    mean_pairwise_difference,
    haplotype_diversity,
    moving_haplotype_diversity,
    tajima_d,
    sfs,
)
from allel.compat import memoryview_safe
from allel.opt.stats import ihh01_scan, ihh_scan
from allel.util import asarray_ndim, check_dim0_aligned, check_integer_dtype
from allel.stats.selection import compute_ihh_gaps

from copy import deepcopy
from collections import defaultdict, namedtuple
from itertools import product, chain
import tempfile

# from multiprocessing import Pool

# from safe_custom import *

from numba import njit
from joblib import Parallel, delayed
import warnings
import pickle

# Set up logging configuration
# logging.basicConfig(level=logging.INFO, format="%(message)s")

pd_merger = partial(pd.merge, how="outer")

# Define the inner named tuple structure
summaries = namedtuple("summaries", ["snps", "window", "K", "parameters"])

#################


def normalization(
    sweeps_stats,
    neutral_stats,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
    nthreads=1,
):
    df_snps, df_window, K, params = sweeps_stats
    df_neutral = neutral_stats.snps

    expected, stdev = normalize_neutral(df_neutral)

    df_splitted = df_snps.groupby("iter")

    df_fv_n = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(normalize_cut)(
            _iter, v, expected=expected, stdev=stdev, center=center, windows=windows
        )
        for _iter, v in df_splitted
    )

    df_fv_n = pd.concat(df_fv_n)
    df_fv_n = pd.merge(df_fv_n, df_window)

    # params = params[:, [0, 1, 3, 4, ]]
    df_fv_n = pd.concat(
        [
            pd.DataFrame(
                np.repeat(
                    params.copy(),
                    df_window.loc[:, ["center", "window"]].drop_duplicates().shape[0],
                    axis=0,
                ),
                columns=["s", "t", "f_i", "f_t"],
            ),
            df_fv_n,
        ],
        axis=1,
    )

    return df_fv_n


def normalize_neutral(neutral_stats):
    # df_snps, df_window = neutral_stats

    window_stats = [
        "h1",
        "h12",
        "h2_h1",
        "k",
        "haf",
        "zns",
        "pi",
        "tajima_d",
        "faywu_h",
        "zeng_e",
    ]

    # Get std and mean values from dataframe
    df_binned = bin_values(
        neutral_stats.loc[:, ~neutral_stats.columns.isin(window_stats)]
    )

    # get expected value (mean) and standard deviation
    expected = df_binned.iloc[:, 2:].groupby("freq_bins").mean()
    stdev = df_binned.iloc[:, 2:].groupby("freq_bins").std()

    expected.index = expected.index.astype(str)
    stdev.index = stdev.index.astype(str)

    return expected, stdev


def bin_values(values, freq=0.02):
    # Create a deep copy of the input variable
    values_copy = values.copy()

    # Modify the copy
    values["freq_bins"] = pd.cut(
        x=values["daf"],
        bins=np.arange(0, 1 + freq, freq),
        include_lowest=True,
        precision=2,
    ).astype(str)

    return values


def normalize_cut(
    _iter,
    snps_values,
    expected,
    stdev,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
):
    binned_values = bin_values(snps_values).copy()

    for stat in binned_values.columns[3:-1]:
        binned_values[stat] -= binned_values["freq_bins"].map(expected[stat])
        binned_values[stat] /= binned_values["freq_bins"].map(stdev[stat])

    binned_values = binned_values.drop(
        ["daf", "freq_bins"], axis=1, inplace=False
    ).copy()

    out = []

    # cut window stats to only SNPs within the window around center
    centers = np.arange(center[0], center[1] + 1e4, 1e4).astype(int)
    iter_c_w = list(product(centers, windows))
    for c, w in iter_c_w:
        # for w in [1000000]:
        lower = c - w / 2
        upper = c + w / 2
        cut_values = (
            binned_values[
                (binned_values["positions"] >= lower)
                & (binned_values["positions"] <= upper)
            ]
            .iloc[:, 2:]
            .abs()
            .mean()
        )

        # cut_values.index = cut_values.index + "_w" + str(w)
        out.append(cut_values)

    out = pd.concat(out, axis=1).T
    out = pd.concat([pd.DataFrame(iter_c_w), out], axis=1)
    out.columns = ["center", "window"] + list(out.columns)[2:]
    out.insert(0, "iter", _iter)
    return out


#################


class Fv:
    def __init__(self, sims, ou):
        self.sims = sims
        self.output_folder = output_folder

        def summary_statistics(self):
            """Summary

            Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            sims (TYPE): Description
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            nthreads (TYPE): Description

            Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            TYPE: Description
            """

            for k, s in self.sims.items():
                is_neutral = True if k == "neutral" else False

                pars = [(i[0], i[1]) for i in s]

                # Log the start of the scheduling
                logging.info("Scheduling {} {} simulations".format(len(s), k))

                # Use joblib to parallelize the execution
                summ_stats = Parallel(n_jobs=nthreads, verbose=5)(
                    delayed(calculate_stats)(ts, rec_map, index, is_neutral=is_neutral)
                    for index, (ts, rec_map) in enumerate(pars)
                )

                # Ensure params order
                summ_stats_snps, summ_stats_window = zip(*summ_stats)
                summ_stats_snps = pd.concat(summ_stats_snps).reset_index(drop=True)
                summ_stats_window = pd.concat(summ_stats_window).reset_index(drop=True)

                if is_neutral:
                    K_neutral = neutral_hfs(
                        sims["neutral"], 10, 110, 5, nthreads=nthreads
                    )
                    neutral_stats = summaries(
                        snps=summ_stats_snps,
                        window=summ_stats_window,
                        K_neutral=K_neutral,
                        parameters=np.zeros(5),
                    )
                else:
                    params = np.row_stack(tuple(zip(*s))[-1])
                    params[:, 0] = -np.log(params[:, 0])
                    sweeps_stats = summaries(
                        snps=summ_stats_snps,
                        window=summ_stats_window,
                        parameters=params,
                    )

            df_t_m = compute_t_m(
                sims["sweeps"], 10, 110, 5, K_neutral=K_neutral, nthreads=nthreads
            )

            df_fv_n = normalization(sweeps_stats, neutral_stats, nthreads=nthreads)

            df_fv = pd.merge(df_fv_n, df_t_m, on=["iter", "center", "window"])

            df_fv["model"] = "sweep"

            df_fv.loc[
                (df_fv.t >= 2000) & (df_fv.f_t >= 0.9), "model"
            ] = "hard_old_complete"
            df_fv.loc[
                (df_fv.t >= 2000) & (df_fv.f_t < 0.9), "model"
            ] = "hard_old_incomplete"
            df_fv.loc[
                (df_fv.t < 2000) & (df_fv.f_t >= 0.9), "model"
            ] = "hard_young_complete"
            df_fv.loc[
                (df_fv.t < 2000) & (df_fv.f_t < 0.9), "model"
            ] = "hard_young_incomplete"

            df_fv.loc[df_fv.f_i != df_fv.f_i.min(), "model"] = df_fv[
                df_fv.f_i != df_fv.f_i.min()
            ].model.str.replace("hard", "soft")

            # Unstack instead pivot since we only need to reshape based on window and center values

            df_fv.set_index(
                [
                    "iter",
                    "s",
                    "t",
                    "t_end",
                    "f_i",
                    "f_t",
                    "f_t_end",
                    "model",
                    "window",
                    "center",
                ],
                inplace=True,
            )
            df_fv_w = df_fv.unstack(level=["window", "center"])

            df_fv_w.columns = [
                f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_w.columns
            ]
            df_fv_w.reset_index(inplace=True)

            if not empirical_data:
                num_nans = df_fv_w.isnull().sum(axis=1)

                # dump fvs with more than 10% nans
                num_drop_fv = sum(num_nans > int(df_fv_w.shape[1] * 0.1))
                df_fv_w.drop(
                    df_fv_w[num_nans > int(df_fv_w.shape[1] * 0.1)].index, inplace=True
                )

            df_fv_w.fillna(0, inplace=True)

            return df_fv_w


def summary_statistics(
    sims,
    nthreads=1,
    neutral_save=None,
    center=[500000, 700000],
    windows=[50000, 100000, 200000, 500000, 1000000],
    step=10000,
):
    """Summary

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    sims (TYPE): Description
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    nthreads (TYPE): Description

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    TYPE: Description
    """

    if isinstance(sims, list) or isinstance(sims, tuple):
        sims = {"sweeps": sims, "neutral": []}

    assert len(sims["sweeps"]) > 0 and (
        len(sims["neutral"]) > 0 or neutral_save is not None
    ), "Please input neutral and sweep simulations"

    for k, s in sims.items():
        if k == "neutral" and neutral_save is not None:
            try:
                with open(neutral_save, "rb") as handle:
                    neutral_stats = pickle.load(handle)
                continue
            except:
                print("Neutral stats will be saved on {}".format(neutral_save))

        pars = [(i[0], i[1]) for i in s]

        # Log the start of the scheduling
        logging.info("Scheduling {} {} simulations".format(len(s), k))

        # Use joblib to parallelize the execution
        summ_stats = Parallel(n_jobs=nthreads, verbose=5)(
            delayed(calculate_stats)(
                ts,
                rec_map,
                index,
                center=center,
                windows=windows,
                step=step,
            )
            for index, (ts, rec_map) in enumerate(pars, 1)
        )

        # Ensure params order
        summ_stats_snps, summ_stats_window = zip(*summ_stats)
        summ_stats_snps = pd.concat(summ_stats_snps).reset_index(drop=True)
        summ_stats_window = pd.concat(summ_stats_window).reset_index(drop=True)

        params = np.row_stack(tuple(zip(*s))[-1])

        if k == "neutral":
            K_neutral = neutral_hfs(sims["neutral"], 10, 110, 5, nthreads=nthreads)
            neutral_stats = summaries(
                snps=summ_stats_snps,
                window=summ_stats_window,
                K=K_neutral,
                parameters=params,
            )
            if neutral_save is not None:
                with open(neutral_save, "wb") as handle:
                    pickle.dump(neutral_stats, handle)
        else:
            if ~np.all(params[:, 3] == 0):
                params[:, 0] = -np.log(params[:, 0])

            sweeps_stats = summaries(
                snps=summ_stats_snps,
                window=summ_stats_window,
                K=np.zeros(10),
                parameters=params,
            )

    df_fv_n = normalization(sweeps_stats, neutral_stats, nthreads=nthreads)
    df_t_m = compute_t_m(
        sims["sweeps"], 10, 110, 5, K_neutral=neutral_stats.K, nthreads=nthreads
    )

    df_fv = pd.merge(df_fv_n, df_t_m, on=["iter", "center", "window"])

    df_fv["model"] = "sweep"

    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_old_complete"
    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t < 0.9), "model"] = "hard_old_incomplete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_young_complete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t < 0.9), "model"] = "hard_young_incomplete"

    df_fv.loc[df_fv.f_i != df_fv.f_i.min(), "model"] = df_fv[
        df_fv.f_i != df_fv.f_i.min()
    ].model.str.replace("hard", "soft")

    if np.all(df_fv.s.values == 0):
        df_fv.loc[:, "model"] = "neutral"

    # Unstack instead pivot since we only need to reshape based on window and center values
    df_fv.set_index(
        [
            "iter",
            "s",
            "t",
            "f_i",
            "f_t",
            "model",
            "window",
            "center",
        ],
        inplace=True,
    )
    df_fv_w = df_fv.unstack(level=["window", "center"])

    df_fv_w.columns = [
        f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_w.columns
    ]
    df_fv_w.reset_index(inplace=True)

    # Normalizing neutral simulations
    if neutral_save is not None:
        df_fv_n_neutral = normalization(
            deepcopy(neutral_stats), neutral_stats, nthreads=nthreads
        )
        df_t_m_neutral = compute_t_m(
            sims["neutral"], 10, 110, 5, K_neutral=neutral_stats.K, nthreads=nthreads
        )

        df_fv_neutral = pd.merge(
            df_fv_n_neutral, df_t_m_neutral, on=["iter", "center", "window"]
        )

        df_fv_neutral["model"] = "neutral"

        # Unstack instead pivot since we only need to reshape based on window and center values
        df_fv_neutral.set_index(
            [
                "iter",
                "s",
                "t",
                "f_i",
                "f_t",
                "model",
                "window",
                "center",
            ],
            inplace=True,
        )

        df_fv_neutral_w = df_fv_neutral.unstack(level=["window", "center"])

        df_fv_neutral_w.columns = [
            f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_neutral_w.columns
        ]
        df_fv_neutral_w.reset_index(inplace=True)
        df_fv_w = pd.concat([df_fv_w, df_fv_neutral_w], axis=0)

        df_fv_w.loc[:, "iter"] = 0

    # if not empirical_data:
    num_nans = df_fv_w.isnull().sum(axis=1)

    # dump fvs with more than 10% nans
    num_drop_fv = sum(num_nans > int(df_fv_w.shape[1] * 0.1))
    df_fv_w.drop(df_fv_w[num_nans > int(df_fv_w.shape[1] * 0.1)].index, inplace=True)
    df_fv_w.fillna(0, inplace=True)

    return df_fv_w


def summary_statistics_n(
    sims,
    nthreads=1,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
    step=1e4,
    empirical_data=True,
    is_neutral=False,
):
    """Summary

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    sims (TYPE): Description
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    nthreads (TYPE): Description

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    TYPE: Description
    """

    with open(neutral, "rb") as handle:
        neutral_stats = pickle.load(handle)

    # K_neutral = np.array([0.29887643, 0.21941123, 0.18215679, 0.1583835, 0.14117205])
    K_neutral = np.array(
        [
            0.20436602,
            0.14638576,
            0.11938808,
            0.10226463,
            0.08996455,
            0.08050419,
            0.07288281,
            0.0664993,
            0.06111408,
            0.05663059,
        ]
    )

    # K_neutral_ooa = np.array([0.19580091, 0.14290259, 0.11815059, 0.10237552, 0.09095834, 0.08209725, 0.0748855 , 0.06897778, 0.06410654, 0.05974498])

    if isinstance(sims, dict):
        sims = sims["sweeps"]
        params = np.row_stack(tuple(zip(*sims))[-1])
        params[:, 0] = -np.log(params[:, 0])
    else:
        params = np.zeros((len(sims), 6))

    pars = [(i[0], i[1]) for i in sims]

    # Use joblib to parallelize the execution
    summ_stats = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(calculate_stats)(ts, rec_map, index, is_neutral=is_neutral)
        for index, (ts, rec_map) in enumerate(pars, 1)
    )

    # func = partial(calculate_stats, is_neutral=False)
    # with Pool(processes=nthreads) as pool:
    #     summ_stats = pool.starmap(calculate_stats, pars)

    # Ensure params order
    summ_stats_snps, summ_stats_window = zip(*summ_stats)
    summ_stats_snps = pd.concat(summ_stats_snps).reset_index(drop=True)
    summ_stats_window = pd.concat(summ_stats_window).reset_index(drop=True)

    sweeps_stats = summaries(
        snps=summ_stats_snps, window=summ_stats_window, parameters=params
    )

    df_fv_n = normalization(sweeps_stats, neutral_stats, nthreads=nthreads)

    df_t_m = compute_t_m(
        sims,
        10,
        110,
        5,
        K_neutral=K_neutral,
        nthreads=nthreads,
        windows=windows,
        center=center,
        step=step,
    )

    df_fv = pd.merge(df_fv_n, df_t_m, on=["iter", "center", "window"])

    df_fv["model"] = "sweep"

    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_old_complete"
    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t < 0.9), "model"] = "hard_old_incomplete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_young_complete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t < 0.9), "model"] = "hard_young_incomplete"

    df_fv.loc[df_fv.f_i >= 0.001, "model"] = df_fv[
        df_fv.f_i >= 0.001
    ].model.str.replace("hard", "soft")

    df_fv.set_index(
        [
            "iter",
            "s",
            "t",
            "t_end",
            "f_i",
            "f_t",
            "f_t_end",
            "model",
            "window",
            "center",
        ],
        inplace=True,
    )

    # Unstack to pivot the data
    df_fv_w = df_fv.unstack(level=["window", "center"])

    df_fv_w.columns = [
        f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_w.columns
    ]
    df_fv_w.reset_index(inplace=True)

    if not empirical_data:
        #     df_fv_w = df_fv_w.iloc[:,8:]
        # else:
        num_nans = df_fv_w.isnull().sum(axis=1)

        # dump fvs with more than 10% nans
        num_drop_fv = sum(num_nans > int(df_fv_w.shape[1] * 0.1))
        df_fv_w.drop(
            df_fv_w[num_nans > int(df_fv_w.shape[1] * 0.1)].index, inplace=True
        )

    df_fv_w.fillna(0, inplace=True)
    return df_fv_w


def open_tree(ts, rec_map):
    try:
        hap = HaplotypeArray(ts.genotype_matrix())
    except:
        try:
            hap = HaplotypeArray(ts)
        except:
            hap = HaplotypeArray(load(ts).genotype_matrix())

    positions = rec_map[:, 2]
    physical_position = rec_map[:, 2]

    # HAP matrix centered to analyse whole chromosome
    hap_01, ac, biallelic_mask = filter_biallelics(hap)
    hap_int = hap_01.astype(np.int8)
    rec_map_01 = rec_map[biallelic_mask]
    position_masked = rec_map_01[:, 2]
    sequence_length = int(1.2e6)

    freqs = ac.to_frequencies()[:, 1]

    return (
        hap_01,
        ac,
        biallelic_mask,
        hap_int,
        rec_map_01,
        position_masked,
        sequence_length,
        freqs,
    )


def filter_biallelics(hap: HaplotypeArray) -> tuple:
    """
    Filter out non-biallelic loci from the haplotype data.

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    hap (allel.GenotypeArray): Haplotype data represented as a GenotypeArray.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    tuple: A tuple containing three elements:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - hap_biallelic (allel.GenotypeArray): Filtered biallelic haplotype data.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - ac_biallelic (numpy.ndarray): Allele counts for the biallelic loci.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - biallelic_mask (numpy.ndarray): Boolean mask indicating biallelic loci.
    """
    ac = hap.count_alleles()
    biallelic_mask = ac.is_biallelic_01()
    return (hap.subset(biallelic_mask), ac[biallelic_mask, :], biallelic_mask)


def calculate_stats(
    ts,
    rec_map,
    i=0,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
    step=1e4,
):
    warnings.filterwarnings(
        "ignore",
        category=RuntimeWarning,
        message="invalid value encountered in scalar divide",
    )
    np.seterr(divide="ignore", invalid="ignore")

    # Open and filtering data
    (
        hap_01,
        ac,
        biallelic_mask,
        hap_int,
        rec_map_01,
        position_masked,
        sequence_length,
        freqs,
    ) = open_tree(ts, rec_map)

    # iSAFE
    # df_isafe = isafe_custom(hap_01, position_masked)
    df_isafe = run_isafe(hap_int, position_masked)

    # iHS and nSL
    ihs_v, delta_ihh = ihs_ihh(
        hap_01,
        position_masked,
        min_maf=0.05,
        min_ehh=0.1,
        include_edges=True,
    )

    try:
        ihs_s = standardize_by_allele_count(
            ihs_v, ac[:, 1], n_bins=50, diagnostics=False
        )[0]
        # delta_ihh_s = standardize_by_allele_count(
        #     delta_ihh, ac[:, 1], n_bins=50, diagnostics=False
        # )[0]
    except:
        ihs_s = np.repeat(np.nan, ihs_v.size)
        # delta_ihh_s = np.repeat(np.nan, delta_ihh.size)

    df_ihs = pd.DataFrame(
        {
            "positions": position_masked,
            "daf": freqs,
            "ihs": np.abs(ihs_v),
        }
    ).dropna()

    # df_delta_ihh = pd.DataFrame(
    #     {
    #         "positions": position_masked,
    #         "daf": freqs,
    #         "delta_ihh": np.abs(delta_ihh_s),
    #     }
    # ).dropna()

    nsl_v = nsl(hap_01.subset(freqs >= 0.05), use_threads=False)

    df_nsl = pd.DataFrame(
        {
            "positions": position_masked[freqs >= 0.05],
            "daf": freqs[freqs >= 0.05],
            "nsl": np.abs(nsl_v),
        }
    ).dropna()

    # Flex-sweep stats
    df_dind_high_low = dind_high_low(hap_int, ac, rec_map_01)

    df_s_ratio = s_ratio(hap_int, ac, rec_map_01)
    df_hapdaf_o = hapdaf_o(hap_int, ac, rec_map_01)
    df_hapdaf_s = hapdaf_s(hap_int, ac, rec_map_01)

    # Merge stats
    df_summaries = reduce(
        pd_merger,
        [
            df_isafe,
            df_ihs,
            # df_delta_ihh,
            df_nsl,
            df_dind_high_low,
            # df_dind,
            # df_high_freq,
            # df_low_freq,
            df_s_ratio,
            df_hapdaf_o,
            df_hapdaf_s,
        ],
    )

    df_summaries = df_summaries.sort_values(by="positions").reset_index(drop=True)

    df_summaries.insert(0, "iter", i)

    if len(center) == 1:
        centers = np.arange(center[0], center[0] + step, step).astype(int)
    else:
        centers = np.arange(center[0], center[1] + step, step).astype(int)

    r2_matrix_values, freq_filter = r2_matrix(hap_int, position_masked)
    df_window = []

    for c, w in product(centers, windows):
        # for w in windows:
        lower = c - w / 2
        upper = c + w / 2

        # Check whether the hap subset is empty or not
        if hap_int[(position_masked > lower) & (position_masked < upper)].size == 0:
            # h1_v,h12_v,h2_h1_v,k,k_1,k_2,k_3,k_4,k_5,haf_v,zns,omega_max,pi_v,d_v,h_v,e_v = = 0
            (
                h1_v,
                h12_v,
                h2_h1_v,
                k,
                k_1,
                k_2,
                k_3,
                k_4,
                k_5,
                haf_v,
                zns_v,
                # omega_max,
                pi_v,
                d_v,
                h_v,
                e_v,
            ) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            # ) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            h1_v, h12_v, h2_h1_v, h123_v, k, k_c = h12_custom(
                hap_int, position_masked, start=lower, stop=upper
            )

            k_1, k_2, k_3, k_4, k_5 = k_c

            # haf_v = haf_top(hap_int.astype(np.int64), position_masked, window=w)
            haf_v = haf_top(
                hap_int.astype(np.float64), position_masked, start=lower, stop=upper
            )

            # LD stats
            # zns_v, omega_max = Ld(hap_int, position_masked, start=lower, stop=upper)
            zns_v, omega_max = Ld(
                r2_matrix_values, freq_filter, position_masked, start=lower, stop=upper
            )

            # SFS stats
            S_mask = (position_masked >= lower) & (position_masked <= upper)
            pi_v = mean_pairwise_difference(ac[S_mask]).sum() / hap_01.shape[0]
            d_v = tajima_d(ac, position_masked, start=lower, stop=upper + 1)
            h_v = fay_wu_h_normalized(hap_01, position_masked, start=lower, stop=upper)[
                -1
            ]
            e_v = zeng_e(hap_01, position_masked, start=lower, stop=upper)
            # pi_v, d_v, h_v,e_v = (0,0, 0, 0)

        df_window.append(
            np.array(
                [
                    i,
                    c,
                    w,
                    h1_v,
                    h12_v,
                    h2_h1_v,
                    k,
                    k_1,
                    k_2,
                    k_3,
                    k_4,
                    k_5,
                    haf_v,
                    zns_v,
                    # omega_max,
                    pi_v,
                    d_v,
                    h_v,
                    e_v,
                ]
                # [h1_v, h12_v, h2_h1_v, k, haf_v, zns, pi_v, d_v, h_v, e_v]
            )
        )

    df_window = pd.DataFrame(
        df_window,
        columns=[
            "iter",
            "center",
            "window",
            "h1",
            "h12",
            "h2_h1",
            "K",
            "K_1",
            "K_2",
            "K_3",
            "K_4",
            "K_5",
            "haf",
            "zns",
            # "omega_max",
            "pi",
            "tajima_d",
            "faywu_h",
            "zeng_e",
        ],
    )

    # df_window.insert(0, "window", np.array(windows))

    # df_window.insert(0, "iter", i)

    return df_summaries.sort_values("positions"), df_window


def ihs_ihh(
    h,
    pos,
    map_pos=None,
    min_ehh=0.05,
    min_maf=0.05,
    include_edges=False,
    gap_scale=20000,
    max_gap=200000,
    is_accessible=None,
):
    # check inputs
    h = asarray_ndim(h, 2)
    check_integer_dtype(h)
    pos = asarray_ndim(pos, 1)
    check_dim0_aligned(h, pos)
    h = memoryview_safe(h)
    pos = memoryview_safe(pos)

    # compute gaps between variants for integration
    gaps = compute_ihh_gaps(pos, map_pos, gap_scale, max_gap, is_accessible)

    # setup kwargs
    kwargs = dict(min_ehh=min_ehh, min_maf=min_maf, include_edges=include_edges)

    # scan forward
    ihh0_fwd, ihh1_fwd = ihh01_scan(h, gaps, **kwargs)

    # scan backward
    ihh0_rev, ihh1_rev = ihh01_scan(h[::-1], gaps[::-1], **kwargs)

    # handle reverse scan
    ihh0_rev = ihh0_rev[::-1]
    ihh1_rev = ihh1_rev[::-1]

    # compute unstandardized score
    ihh0 = ihh0_fwd + ihh0_rev
    ihh1 = ihh1_fwd + ihh1_rev

    # og estimation
    ihs = np.log(ihh0 / ihh1)

    delta_ihh = np.abs(ihh1 - ihh0)

    df_ihs = pd.DataFrame(
        {
            "positions": pos,
            "daf": h.sum(1) / h.shape[1],
            "ihs": ihs,
            "delta_ihh": delta_ihh,
        }
    ).dropna()

    return df_ihs


def run_hapbin(
    hap,
    rec_map,
    _iter=0,
    cutoff=0.05,
    hapbin="/home/jmurgamoreno/software/hapbin/build/ihsbin",
    binom=False,
):
    df_hap = pd.DataFrame(hap)

    df_rec_map = pd.DataFrame(rec_map)

    # Generate a temporary file name
    hap_file = "/tmp/tmp_" + str(_iter) + ".hap"
    map_file = "/tmp/tmp_" + str(_iter) + ".map"

    df_hap.to_csv(hap_file, index=False, header=None, sep=" ")
    df_rec_map.to_csv(map_file, index=False, header=None, sep=" ")

    hapbin_ihs = (
        hapbin
        + " --hap "
        + hap_file
        + " --map "
        + map_file
        + " --minmaf 0.05 --cutoff "
        + str(cutoff)
    )
    if binom:
        hapbin_ihs += " -a"

    with subprocess.Popen(hapbin_ihs.split(), stdout=subprocess.PIPE) as process:
        df_ihs = pd.read_csv(process.stdout, sep="\t").iloc[:, [1, 2, 5]]

    os.remove(hap_file)
    os.remove(map_file)

    df_ihs.columns = ["positions", "daf", "ihs"]
    df_ihs.loc[:, "positions"] = (
        df_rec_map[df_rec_map.iloc[:, 1].isin(df_ihs.positions.values.tolist())]
        .iloc[:, -1]
        .values
    )
    return df_ihs


def isafe_custom(
    hap,
    positions,
    max_freq=1,
    min_region_size_bp=49000,
    min_region_size_ps=300,
    ignore_gaps=True,
    window=300,
    step=150,
    topk=1,
    max_rank=15,
):
    """
    Estimate iSAFE or SAFE when not possible using default Flex-Sweep values.

    Args:
     hap (TYPE): Description
     total_window_size (TYPE): Description
     positions (TYPE): Description
     max_freq (int, optional): Description
     min_region_size_bp (int, optional): Description
     min_region_size_ps (int, optional): Description
     ignore_gaps (bool, optional): Description
     window (int, optional): Description
     step (int, optional): Description
     topk (int, optional): Description
     max_rank (int, optional): Description

    Returns:
     TYPE: Description

    Raises:
     ValueError: Description
    """

    snp_matrix = pd.DataFrame(hap, index=positions)
    tmp_pos = np.asarray(snp_matrix.index)
    total_window_size = tmp_pos.max() - tmp_pos.min()
    # snp_matrix = snp_matrix.loc[
    #     (snp_matrix.index >= 1) & (snp_matrix.index <= total_window_size)
    # ]

    dp = np.diff(positions)
    num_gaps = sum(dp > 6000000)
    f = snp_matrix.mean(1)
    snp_matrix = snp_matrix.loc[((1 - f) * f) > 0]
    num_snps = snp_matrix.shape[0]

    if (num_snps < min_region_size_ps) | (total_window_size < min_region_size_bp):
        # raise ValueError(
        #     (
        #         "The region Size is %i SNPs and %ikbp. When the region size is less than --MinRegionSize-ps (%i) SNPs or --MinRegionSize-bp (%ikbp), "
        #         "the region is too small for iSAFE analysis and better to use --SAFE flag to report "
        #         "the SAFE score of the entire region."
        #         % (
        #             num_snps,
        #             total_window_size / 1e3,
        #             min_region_size_ps,
        #             min_region_size_bp / 1e3,
        #         )
        #     )
        # )
        obj_safe = SafeClass(snp_matrix.values.T)

        df_safe = obj_safe.creat_dataframe().rename(
            columns={"safe": "isafe", "freq": "daf"}
        )
        df_safe["positions"] = snp_matrix.index
        return df_safe.loc[:, ["positions", "daf", "isafe"]]
    else:
        obj_isafe = iSafeClass(snp_matrix, window, step, topk, max_rank)
        obj_isafe.fire(status=False)
        df_isafe = (
            obj_isafe.isafe.loc[obj_isafe.isafe["freq"] < max_freq]
            .sort_values("ordinal_pos")
            .rename(columns={"id": "positions", "isafe": "isafe", "freq": "daf"})
        )
        df_isafe = df_isafe[df_isafe.daf < max_freq]
        return df_isafe.loc[:, ["positions", "daf", "isafe"]]


def haf_top_np(hap, pos, cutoff=0.1, window=500000):
    haf_range = np.arange(600000 - (window / 2), 600000 + (window / 2), 100)[[0, -1]]

    freqs = hap.sum(axis=1) / hap.shape[1]
    hap_tmp = hap[(freqs > 0) & (freqs < 1)]
    pos_tmp = pos[(freqs > 0) & (freqs < 1)]
    hap_tmp = hap_tmp[(pos_tmp >= haf_range[0]) & (pos_tmp <= haf_range[1])]

    haf_num = (np.dot(hap_tmp.T, hap_tmp) / hap.shape[1]).sum(axis=1)

    haf_den = hap_tmp.sum(axis=0)

    haf = np.sort(haf_num / haf_den)

    idx_low = int(cutoff * haf.size)
    idx_high = int((1 - cutoff) * haf.size)

    # 10% higher
    haf_top = haf[idx_high:].sum()

    return haf_top


def haf_top(hap, pos, cutoff=0.1, start=None, stop=None):
    if start is not None or stop is not None:
        loc = (pos >= start) & (pos <= stop)
        pos = pos[loc]
        hap = hap[loc, :]

    freqs = hap.sum(axis=1) / hap.shape[1]
    hap_tmp = hap[(freqs > 0) & (freqs < 1)]
    haf_num = (np.dot(hap_tmp.T, hap_tmp) / hap.shape[1]).sum(axis=1)
    haf_den = hap_tmp.sum(axis=0)

    haf = np.sort(haf_num / haf_den)

    idx_low = int(cutoff * haf.size)
    idx_high = int((1 - cutoff) * haf.size)

    # 10% higher
    haf_top = haf[idx_high:].sum()

    return haf_top


def haf_snps(hap, pos, num_snps=401, cutoff=0.1):
    freqs = hap.sum(axis=1) / hap.shape[1]

    hap_filter = hap[(freqs >= 0) & (freqs <= 1)]
    pos_filter = pos[(freqs >= 0) & (freqs <= 1)]

    # Define the center position and desired mutation count
    center = 6e5

    # Find the index of the center position in the genomic_positions array
    center_index = np.argmin(np.abs(pos_filter - center))

    # Calculate the indices for slicing
    left_index = max(center_index - num_snps // 2, 0)
    right_index = min(center_index + num_snps // 2, pos_filter.size)

    h = hap_filter[left_index:right_index, :]

    haf_num = (dot_nb(h) / hap.shape[1]).sum(axis=1)
    haf_den = h.sum(axis=0)

    haf = np.sort(haf_num / haf_den)

    idx_low = int(cutoff * haf.size)
    idx_high = int((1 - cutoff) * haf.size)

    # 10% higher
    haf_top = haf[idx_high:].sum()

    return haf_top


def dind_high_low(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.25,
    min_tot_freq=0,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_np(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    results_dind = []
    results_high = []
    results_low = []
    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]
        f_a = v[:, 1]

        focal_derived_count = info[i][-2]
        focal_ancestral_count = info[i][-1]

        f_d2 = f_d * (1 - f_d) * focal_derived_count / (focal_derived_count - 1)
        f_a2 = (
            f_a
            * (1 - f_a)
            * focal_ancestral_count
            / (focal_ancestral_count - 1 + 0.001)
        )

        num = (f_d2 - f_d2 + f_a2).sum()
        den = (f_a2 - f_a2 + f_d2).sum() + 0.001

        hap_dind = num / den

        #####
        f_d = v[:, 0]

        f_diff_high = f_d[f_d > max_ancest_freq] ** 2

        hap_high = f_diff_high.sum() / len(f_diff_high)
        #####

        f_d = v[:, 0]

        f_diff_low = (1 - f_d[f_d < max_ancest_freq]) ** 2

        hap_low = f_diff_low.sum() / len(f_diff_low)

        results_dind.append(hap_dind)
        results_high.append(hap_high)
        results_low.append(hap_low)

    try:
        out = np.hstack(
            [
                info,
                np.array(results_dind).reshape(len(results_dind), 1),
                np.array(results_high).reshape(len(results_high), 1),
                np.array(results_low).reshape(len(results_low), 1),
            ]
        )
        df_out = pd.DataFrame(
            out[:, [0, 1, 4, 5, 6]],
            columns=["positions", "daf", "dind", "high_freq", "low_freq"],
        )
    except:
        df_out = pd.DataFrame(
            [], columns=["positions", "daf", "dind", "high_freq", "low_freq"]
        )

    return df_out


def dind(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.25,
    min_tot_freq=0,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_np(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    results = []

    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]
        f_a = v[:, 1]

        focal_derived_count = info[i][-2]
        focal_ancestral_count = info[i][-1]

        f_d2 = f_d * (1 - f_d) * focal_derived_count / (focal_derived_count - 1)
        f_a2 = (
            f_a
            * (1 - f_a)
            * focal_ancestral_count
            / (focal_ancestral_count - 1 + 0.001)
        )

        num = (f_d2 - f_d2 + f_a2).sum()
        den = (f_a2 - f_a2 + f_d2).sum() + 0.001

        hapdaf = num / den
        results.append(hapdaf)

    out = np.hstack([info, np.array(results).reshape(len(results), 1)])

    df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "dind"])

    return df_out


def high_freq(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.25,
    min_tot_freq=0,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_np(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    results = []

    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]

        f_diff = f_d[f_d > max_ancest_freq] ** 2

        hapdaf = f_diff.sum() / len(f_diff)
        results.append(hapdaf)

    out = np.hstack([info, np.array(results).reshape(len(results), 1)])

    df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "high_freq"])

    return df_out


def low_freq(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.25,
    min_tot_freq=0,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_np(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )
    results = []

    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]

        f_diff = (1 - f_d[f_d < max_ancest_freq]) ** 2

        hapdaf = f_diff.sum() / len(f_diff)
        results.append(hapdaf)

    out = np.hstack([info, np.array(results).reshape(len(results), 1)])

    df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "low_freq"])

    return df_out


def s_ratio(
    hap,
    ac,
    rec_map,
    max_ancest_freq=1,
    min_tot_freq=0,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_np(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )
    results = []

    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]
        f_a = v[:, 1]

        f_d2 = np.zeros(f_d.shape)
        f_a2 = np.zeros(f_a.shape)

        f_d2[(f_d > 0.0000001) & (f_d < 1)] = 1
        f_a2[(f_a > 0.0000001) & (f_a < 1)] = 1

        num = (f_d2 - f_d2 + f_a2 + 1).sum()
        den = (f_a2 - f_a2 + f_d2 + 1).sum()
        # redefine to add one to get rid of blowup issue introduced by adding 0.001 to denominator

        hapdaf = num / den
        results.append(hapdaf)

    try:
        out = np.hstack([info, np.array(results).reshape(len(results), 1)])
        df_out = pd.DataFrame(
            out[:, [0, 1, 4]], columns=["positions", "daf", "s_ratio"]
        )
    except:
        df_out = pd.DataFrame([], columns=["positions", "daf", "s_ratio"])

    return df_out


def hapdaf_o(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.25,
    min_tot_freq=0.25,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_np(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    results = []
    nan_index = []

    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]
        f_a = v[:, 1]
        f_tot = v[:, 2]

        f_d2 = (
            f_d[(f_d > f_a) & (f_a <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )
        f_a2 = (
            f_a[(f_d > f_a) & (f_a <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )

        if len(f_d2) != 0 and len(f_a2) != 0:
            hapdaf = (f_d2 - f_a2).sum() / f_d2.shape[0]
            results.append(hapdaf)
        else:
            nan_index.append(i)

    try:
        out = np.hstack(
            [
                np.delete(info, nan_index, axis=0),
                np.array(results).reshape(len(results), 1),
            ]
        )
        df_out = pd.DataFrame(
            out[:, [0, 1, 4]], columns=["positions", "daf", "hapdaf_o"]
        )
    except:
        df_out = pd.DataFrame([], columns=["positions", "daf", "s_ratio"])

    return df_out


def hapdaf_s(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.1,
    min_tot_freq=0.1,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_np(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )
    results = []
    nan_index = []
    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]
        f_a = v[:, 1]
        f_tot = v[:, 2]

        f_d2 = (
            f_d[(f_d > f_a) & (f_a <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )
        f_a2 = (
            f_a[(f_d > f_a) & (f_a <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )

        if len(f_d2) != 0 and len(f_a2) != 0:
            hapdaf = (f_d2 - f_a2).sum() / f_d2.shape[0]
            results.append(hapdaf)
        else:
            nan_index.append(i)

    try:
        out = np.hstack(
            [
                np.delete(info, nan_index, axis=0),
                np.array(results).reshape(len(results), 1),
            ]
        )

        df_out = pd.DataFrame(
            out[:, [0, 1, 4]], columns=["positions", "daf", "hapdaf_s"]
        )
    except:
        df_out = pd.DataFrame([], columns=["positions", "daf", "s_ratio"])

    return df_out


def sq_freq_pairs_np(hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size):
    # Compute counts and freqs once, then iter pairs combinations
    hap_derived = hap
    hap_ancestral = np.bitwise_xor(hap_derived, 1)

    derived_count = ac[:, 1]
    ancestral_count = ac[:, 0]
    # freqs = ac.to_frequencies()[:, 1]
    freqs = ac[:, 1] / ac.sum(axis=1)
    focal_filter = (freqs >= min_focal_freq) & (freqs <= max_focal_freq)

    focal_derived = hap_derived[focal_filter, :]
    focal_derived_count = derived_count[focal_filter]
    focal_ancestral = hap_ancestral[focal_filter, :]
    focal_ancestral_count = ancestral_count[focal_filter]
    focal_index = focal_filter.nonzero()[0]

    sq_out = []
    info = []
    out = []
    for j, i in enumerate(focal_index):
        pars = (
            i,
            hap_derived,
            derived_count,
            freqs,
            focal_derived,
            focal_derived_count,
            focal_ancestral,
            focal_ancestral_count,
        )

        sq_freqs = np.concatenate(
            (
                sq(j, pars, rec_map, 0, window_size),
                sq(j, pars, rec_map, freqs.size, window_size),
            )
        )

        sq_out.append(sq_freqs)

        # out.append(b+d)

        info.append(
            (rec_map[i, 2], freqs[i], focal_derived_count[j], focal_ancestral_count[j])
        )

    return (sq_out, np.array(info))


@njit(cache=True)
def sq(j, pars, rec_map, end, window_size):
    (
        i,
        hap_derived,
        hap_count,
        hap_freqs,
        focal_derived,
        focal_derived_count,
        focal_ancestral,
        focal_ancestral_count,
    ) = pars

    # Calculate the size of the window
    size = window_size / 2

    # Find indices within the window
    z = np.flatnonzero(np.abs(rec_map[i, 2] - rec_map[:, 2]) <= size)

    # Determine indices for slicing the arrays
    if i < end:
        x, y = (i + 1, z[-1])
    else:
        x, y = (z[0], i - 1)

    derived = hap_derived[x : (y + 1), :]
    derived_count = hap_count[x : (y + 1)]
    f_d = (focal_derived[j] & derived).sum(axis=1) / focal_derived_count[j]
    # f_d_flipped = (focal_ancestral[j] & derived).sum(axis=1) / focal_derived_count[j]
    f_a = (focal_ancestral[j] & derived).sum(axis=1) / focal_ancestral_count[j]
    f_tot = hap_freqs[x : y + 1]

    if end == 0:
        f_d = f_d[::-1]
        # f_d_flipped = f_d_flipped[::-1]
        f_a = f_a[::-1]
        f_tot = f_tot[::-1]

    # return np.array((f_d, f_a, f_tot)).T
    return np.vstack((f_d, f_a, f_tot)).T
    # return np.vstack((f_d,f_d_flipped, f_a, f_tot)).T


def get_duplicates(pos):
    unique_values, inverse_indices, counts = np.unique(
        pos, return_inverse=True, return_counts=True
    )

    duplicated_indices = np.where(counts[inverse_indices] > 1)[0]

    x = np.split(duplicated_indices, np.where(np.diff(duplicated_indices) != 1)[0] + 1)

    return x


def h12_snps(hap, pos, min_freq=0.05, max_freq=1, num_snps=401):
    freqs = hap.sum(axis=1) / hap.shape[1]

    hap_filter = hap[(freqs >= min_freq) & (freqs <= max_freq)]
    pos_filter = pos[(freqs >= min_freq) & (freqs <= max_freq)]

    # Define the center position and desired mutation count
    center = 6e5

    # Find the index of the center position in the genomic_positions array
    center_index = np.argmin(np.abs(pos_filter - center))

    # Calculate the indices for slicing
    left_index = max(center_index - num_snps // 2, 0)
    right_index = min(center_index + num_snps // 2, pos_filter.size)

    h = hap_filter[left_index:right_index, :]

    h = cluster_similar_rows(h.T, num_snps * 0.2).T

    h1, h12, h123, h2_h1 = garud_h(h)

    k = HaplotypeArray(h).distinct_counts().size

    return (h1, h12, h2_h1, h123, k)


def h12_custom(hap, pos, min_freq=0.05, max_freq=1, start=None, stop=None):
    if start is not None or stop is not None:
        loc = (pos >= start) & (pos <= stop)
        pos = pos[loc]
        hap = hap[loc, :]

    freqs = hap.sum(axis=1) / hap.shape[1]

    hap_filter = hap[(freqs >= min_freq) & (freqs <= max_freq)]
    pos_filter = pos[(freqs >= min_freq) & (freqs <= max_freq)]

    S = hap_filter.shape[1]
    hap_cluster, k, k_c = cluster_similar_rows_nb(hap_filter.T, np.ceil(S * 0.2))

    h1, h12, h123, h2_h1 = garud_h(hap_cluster)

    # k_c = HaplotypeArray(hap_cluster).distinct_counts()

    return (h1, h12, h2_h1, h123, k, k_c)


def fay_wu_h_normalized(hap: np.ndarray, pos, start=None, stop=None) -> tuple:
    """
    Compute Fay-Wu's H test statistic and its normalized version.

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    hap (numpy.ndarray): 2D array representing haplotype data.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Rows correspond to different mutations, and columns
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     correspond to chromosomes.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    tuple: A tuple containing two values:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - h (float): Fay-Wu H test statistic.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - h_normalized (float): Normalized Fay-Wu H test statistic.
    """

    if start is not None or stop is not None:
        loc = (pos >= start) & (pos <= stop)
        pos = pos[loc]
        hap = hap[loc, :]

    # Count segregating and chromosomes
    S, n = hap.shape
    # Create SFS to count ith mutation in sample
    Si = sfs(hap.sum(axis=1), n)[1:-1]
    # ith mutations
    i = np.arange(1, n)

    # (n-1)th harmonic numbers
    an = np.sum(1 / i)
    bn = np.sum(1 / i**2)
    bn_1 = bn + 1 / (n**2)

    # calculate theta_w absolute value
    theta_w = S / an

    # calculate theta_pi absolute value
    theta_pi = ((2 * Si * i * (n - i)) / (n * (n - 1))).sum()

    # calculate theta_h absolute value
    theta_h = ((2 * Si * np.power(i, 2)) / (n * (n - 1))).sum()

    # calculate theta_l absolute value
    theta_l = (np.arange(1, n) * Si).sum() / (n - 1)

    theta_square = (S * (S - 1)) / (an**2 + bn)

    h = theta_pi - theta_h

    var_1 = (n - 2) / (6 * (n - 1)) * theta_w

    var_2 = (
        (
            (18 * (n**2) * (3 * n + 2) * bn_1)
            - ((88 * (n**3) + 9 * (n**2)) - (13 * n + 6))
        )
        / (9 * n * ((n - 1) ** 2))
    ) * theta_square

    # cov = (((n+1) / (3*(n-1)))*theta_w) + (((7*n*n+3*n-2-4*n*(n+1)*bn_1)/(2*(n-1)**2))*theta_square)

    # var_theta_l = (n * theta_w)/(2.0 * (n - 1.0)) + (2.0 * np.power(n/(n - 1.0), 2.0) * (bn_1 - 1.0) - 1.0) * theta_square;
    # var_theta_pi = (3.0 * n *(n + 1.0) * theta_w + 2.0 * ( n * n + n + 3.0) * theta_square)/ (9 * n * (n -1.0));

    h_normalized = h / np.sqrt(var_1 + var_2)

    # h_prime = h / np.sqrt(var_theta_l+var_theta_pi - 2.0 * cov)

    return (h, h_normalized)


def zeng_e(hap: np.ndarray, pos, start=None, stop=None) -> float:
    """
    Compute Zeng's E test statistic.

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    hap (numpy.ndarray): 2D array representing haplotype data.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Rows correspond to different mutations, and columns
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     correspond to chromosomes.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float: Zeng's E test statistic.
    """

    if start is not None or stop is not None:
        loc = (pos >= start) & (pos <= stop)
        pos = pos[loc]
        hap = hap[loc, :]

    # Count segregating and chromosomes
    S, n = hap.shape
    # Create SFS to count ith mutation in sample
    Si = sfs(hap.sum(axis=1), n)[1:-1]
    # ith mutations
    i = np.arange(1, n)

    # (n-1)th harmonic numbers
    an = np.sum(1.0 / i)
    bn = np.sum(1.0 / i**2.0)

    # calculate theta_w absolute value
    theta_w = S / an

    # calculate theta_l absolute value
    theta_l = (np.arange(1, n) * Si).sum() / (n - 1)

    theta_square = S * (S - 1.0) / (an**2 + bn)

    # Eq. 14
    var_1 = (n / (2.0 * (n - 1.0)) - 1.0 / an) * theta_w
    var_2 = (
        bn / an**2
        + 2 * (n / (n - 1)) ** 2 * bn
        - 2 * (n * bn - n + 1) / ((n - 1) * an)
        - (3 * n + 1) / (n - 1)
    ) * theta_square

    (
        (bn / an**2)
        + (2 * (n / (n - 1)) ** 2 * bn)
        - (2 * (n * bn - n + 1) / ((n - 1) * an))
        - ((3 * n + 1) / (n - 1)) * theta_square
    )
    e = (theta_l - theta_w) / (var_1 + var_2) ** 0.5
    return e


def Ld(
    hap: np.ndarray, pos: np.ndarray, min_freq=0.05, max_freq=1, start=None, stop=None
) -> tuple:
    """
    Compute Kelly Zns statistic (1997) and omega_max. Average r2
    among every pair of loci in the genomic window.

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    hap (numpy.ndarray): 2D array representing haplotype data.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Rows correspond to different mutations, and columns
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     correspond to chromosomes.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    pos (numpy.ndarray): 1D array representing the positions of mutations.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    min_freq (float, optional): Minimum frequency threshold. Default is 0.05.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    max_freq (float, optional): Maximum frequency threshold. Default is 1.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    window (int, optional): Genomic window size. Default is 500000.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    tuple: A tuple containing two values:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - kelly_zns (float): Kelly Zns statistic.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - omega_max (float): Nielsen omega max.
    """

    if start is not None or stop is not None:
        loc = (pos >= start) & (pos <= stop)
        pos = pos[loc]
        hap = hap[loc, :]

    freqs = hap.sum(axis=1) / hap.shape[1]

    hap_filter = hap[(freqs >= min_freq) & (freqs <= max_freq)]

    r2_matrix = compute_r2_matrix(hap_filter)
    # r2_matrix = r2_torch(hap_filter)
    S = hap_filter.shape[0]
    zns = r2_matrix.sum() / math.comb(S, 2)
    # Index combination to iter
    # omega_max = omega(r2_matrix)
    # omega_max = dps.omega(r2_matrix)[0]

    return zns, 0
    # return zns, omega_max


def r2_matrix(
    hap: np.ndarray, pos: np.ndarray, min_freq=0.05, max_freq=1, start=None, stop=None
):
    """
    Compute Kelly Zns statistic (1997) and omega_max. Average r2
    among every pair of loci in the genomic window.

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    hap (numpy.ndarray): 2D array representing haplotype data.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Rows correspond to different mutations, and columns
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     correspond to chromosomes.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    pos (numpy.ndarray): 1D array representing the positions of mutations.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    min_freq (float, optional): Minimum frequency threshold. Default is 0.05.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    max_freq (float, optional): Maximum frequency threshold. Default is 1.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    window (int, optional): Genomic window size. Default is 500000.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    tuple: A tuple containing two values:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - kelly_zns (float): Kelly Zns statistic.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    - omega_max (float): Nielsen omega max.
    """

    # if start is not None or stop is not None:
    #     loc = (pos >= start) & (pos <= stop)
    #     pos = pos[loc]
    #     hap = hap[loc, :]

    freqs = hap.sum(axis=1) / hap.shape[1]
    freq_filter = (freqs >= min_freq) & (freqs <= max_freq)
    hap_filter = hap[freq_filter]

    r2_matrix = compute_r2_matrix(hap_filter)
    # r2_matrix = r2_torch(hap_filter)
    # S = hap_filter.shape[0]
    # zns = r2_matrix.sum() / math.comb(S, 2)
    # Index combination to iter
    # omega_max = omega(r2_matrix)
    # omega_max = dps.omega(r2_matrix)[0]

    return r2_matrix, freq_filter
    # return zns, omega_max


def Ld(
    r2_subset,
    freq_filter,
    pos: np.ndarray,
    min_freq=0.05,
    max_freq=1,
    start=None,
    stop=None,
):
    pos_filter = pos[freq_filter]
    if start is not None or stop is not None:
        loc = (pos_filter >= start) & (pos_filter <= stop)
        pos_filter = pos_filter[loc]
        r2_subset = r2_subset[loc, :][:, loc]

    # r2_subset_matrix = compute_r2_subset_matrix(hap_filter)
    # r2_subset_matrix = r2_subset_torch(hap_filter)
    S = r2_subset.shape[0]
    kelly_zns = r2_subset.sum() / math.comb(S, 2)
    # omega_max = omega(r2_subset)

    return kelly_zns, 0


@njit("float64(int8[:], int8[:])", cache=True)
def r2(locus_A: np.ndarray, locus_B: np.ndarray) -> float:
    """
    Calculate r^2 and D between the two loci A and B.

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    locus_A (numpy.ndarray): 1D array representing alleles at locus A.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    locus_B (numpy.ndarray): 1D array representing alleles at locus B.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float: r^2 value.
    """

    n = locus_A.size
    # Frequency of allele 1 in locus A
    a1 = locus_A.sum() / n
    # Frequency of allele 1 in locus B
    b1 = locus_B.sum() / n
    # This probably is the speed bottleneck:
    # count_a1b1 = sum(hap == (1, 1) for hap in zip(locus_A, locus_B))
    count_a1b1 = 0
    for i in zip(locus_A, locus_B):
        if i == (1, 1):
            count_a1b1 += 1

    # Frequency of haplotype 11 between the two loci.
    a1b1 = count_a1b1 / n
    D = a1b1 - a1 * b1

    r2 = (D**2) / (a1 * (1 - a1) * b1 * (1 - b1))
    return r2


@njit("float64(int8[:], int8[:])", cache=True)
def r2(locus_A: np.ndarray, locus_B: np.ndarray) -> float:
    """
    Calculate r^2 and D between the two loci A and B.

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    locus_A (numpy.ndarray): 1D array representing alleles at locus A.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    locus_B (numpy.ndarray): 1D array representing alleles at locus B.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float: r^2 value.
    """
    n = locus_A.size
    # Frequency of allele 1 in locus A and locus B
    a1 = 0
    b1 = 0
    count_a1b1 = 0

    for i in range(n):
        a1 += locus_A[i]
        b1 += locus_B[i]
        count_a1b1 += locus_A[i] * locus_B[i]

    a1 /= n
    b1 /= n
    a1b1 = count_a1b1 / n
    D = a1b1 - a1 * b1

    r_squared = (D**2) / (a1 * (1 - a1) * b1 * (1 - b1))
    return r_squared


@njit("float64[:,:](int8[:,:])", cache=True)
def compute_r2_matrix(hap):
    num_sites = hap.shape[0]

    # r2_matrix = OrderedDict()
    sum_r_squared = 0
    r2_matrix = np.zeros((num_sites, num_sites))
    # Avoid itertool.combination, not working on numba
    # for pair in combinations(range(num_sites), 2):

    # Check index from triangular matrix of size num_sites x num_sites. Each indices correspond to one one dimension of the array. Same as combinations(range(num_sites), 2)
    c_1, c_2 = np.triu_indices(num_sites, 1)

    for i, j in zip(c_1, c_2):
        r2_matrix[i, j] = r2(hap[i, :], hap[j, :])
        # r2_matrix[pair[0], pair[1]] = r2(hap[pair[0], :], hap[pair[1], :])

    return r2_matrix


@njit("float64(float64[:,:])", cache=True)
def omega(r2_matrix):
    """
    Calculates Kim and Nielsen's (2004, Genetics 167:1513) omega_max statistic. Adapted from PG-Alignments-GAN

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    r2_matrix (numpy.ndarray): 2D array representing r2 values.

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float: Kim and Nielsen's omega max.
    """

    omega_max = 0
    S_ = r2_matrix.shape[1]

    if S_ < 3:
        omega_max = 0
    else:
        for l_ in range(3, S_ - 2):
            sum_r2_L = 0
            sum_r2_R = 0
            sum_r2_LR = 0

            for i in range(S_):
                for j in range(i + 1, S_):
                    ld_calc = r2_matrix[i, j]
                    if i < l_ and j < l_:
                        sum_r2_L += ld_calc

                    elif i >= l_ and j >= l_:
                        sum_r2_R += ld_calc

                    elif i < l_ and j >= l_:
                        sum_r2_LR += ld_calc

            # l_ ## to keep the math right outside of indexing
            omega_numerator = (
                1 / ((l_ * (l_ - 1) / 2) + ((S_ - l_) * (S_ - l_ - 1) / 2))
            ) * (sum_r2_L + sum_r2_R)
            omega_denominator = (1 / (l_ * (S_ - l_))) * sum_r2_LR

            if omega_denominator == 0:
                omega = 0
            else:
                omega = np.divide(omega_numerator, omega_denominator)

            if omega > omega_max:
                omega_max = omega

    return omega_max


def h(hap, pos, min_freq=0.05, max_freq=1, center=6e5, window=5e5):
    lower_bound = center - window / 2
    upper_bound = center + window / 2

    mask = (pos >= lower_bound) & (pos <= upper_bound)

    S, n = hap.shape
    freqs = hap.sum(axis=1) / n
    hap_filter = hap[(freqs >= min_freq) & (freqs <= max_freq) & mask]
    pos_filter = pos[(freqs >= min_freq) & (freqs <= max_freq) & mask]

    hap_cluster, k, k_c = cluster_similar_rows_nb(hap_filter, pos_filter, threshold=0.2)
    # f = HaplotypeArray(hap_filter).distinct_frequencies()

    # compute H12
    # h12 = (
    #     np.sum(k_c[:2] / hap_filter.shape[1]) ** 2
    #     + np.sum(k_c[:2] / hap_filter.shape[1]) ** 2
    # )
    h12 = (k_c[0] / n + k_c[1] / n) * (k_c[0] / n + k_c[1] / n)

    # h12 = np.sum(f[:2]) ** 2

    # compute H12
    # h12 = np.sum(f[:2])**2 + np.sum(f[2:]**2)

    # compute H123
    # h123 = np.sum(f[:3])**2 + np.sum(f[3:]**2)

    # compute H2/H1
    # h2 = h1 - f[0]**2
    # h2_h1 = h2 / h1

    return h12


def cluster_similar_rows(hap, pos, start=None, stop=None, threshold=1.0):
    if start is not None or stop is not None:
        loc = (pos >= start) & (pos <= stop)
        pos = pos[loc]
        hap = hap[loc, :]

    num_rows, num_cols = hap.shape
    out = np.zeros((num_rows, num_cols)).astype(np.int8)
    cluster_indices = np.arange(num_rows)

    for i in range(num_rows):
        if cluster_indices[i] == i:
            cluster_indices[i] = i

            out[i] = hap[i]
            for j in range(i + 1, num_rows):
                diff, tot = hamming_distance(hap[i], hap[j])
                if diff / tot <= threshold:
                    cluster_indices[j] = i
                    out[j] = hap[i]

    k_c = np.sort(np.unique(cluster_indices, return_counts=True)[-1])[::-1]
    k = k_c.size
    if k < 5:
        k_c = np.concatenate([k_c, np.zeros((5 - k), dtype=int)])
    return out.T, k, k_c[:5]


def cluster_similar_rows_nb(hap, pos, start=None, stop=None, threshold=1.0):
    if start is not None or stop is not None:
        loc = (pos >= start) & (pos <= stop)
        pos = pos[loc]
        hap = hap[loc, :]

    # out, cluster_indices = cluster_nb(hap.T,threshold)
    out, cluster_indices = cluster_nb(hap.T, threshold)
    k_c = np.sort(np.unique(cluster_indices, return_counts=True)[-1])[::-1]
    k_c
    k = k_c.size
    if k < 5:
        k_c = np.concatenate([k_c, np.zeros((5 - k), dtype=int)])
    return out.T, k, k_c[:5]


@njit
def cluster_nb(hap, threshold=1.0):
    num_rows, num_cols = hap.shape
    out = np.zeros((num_rows, num_cols)).astype(np.int8)
    cluster_indices = np.arange(num_rows)

    for i in range(num_rows):
        if cluster_indices[i] == i:
            cluster_indices[i] = i

            out[i] = hap[i]
            for j in range(i + 1, num_rows):
                diff, tot = hamming_distance(hap[i], hap[j])
                if diff / tot <= threshold:
                    cluster_indices[j] = i
                    out[j] = hap[i]
    return out, cluster_indices


# @njit("int64(int8[:],int8[:])", cache=True)
@njit
def hamming_distance(row1, row2):
    identical = np.sum((row1 == 1) & (row2 == 1))
    different = np.sum((row1 == 0) & (row2 == 1)) + np.sum((row1 == 1) & (row2 == 0))
    total = identical + different
    if total == 0:
        total = row1.size
    return different, total


def get_empir_freqs_np(hap):
    """
    Calculate the empirical frequencies of haplotypes.

    Parameters:
    - hap (numpy.ndarray): Array of haplotypes where each column represents an individual and each row represents a SNP.

    Returns:
    - k_counts (numpy.ndarray): Counts of each unique haplotype.
    - h_f (numpy.ndarray): Empirical frequencies of each unique haplotype.
    """
    S, n = hap.shape

    # Count occurrences of each unique haplotype
    hap_f, k_counts = np.unique(hap, axis=1, return_counts=True)

    # Sort counts in descending order
    k_counts = np.sort(k_counts)[::-1]

    # Calculate empirical frequencies
    h_f = k_counts / n
    return k_counts, h_f


def process_spectra(
    k: np.ndarray, h_f: np.ndarray, K_truncation: int, n_ind: int
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Process haplotype count and frequency spectra.

    Parameters:
    - k (numpy.ndarray): Counts of each unique haplotype.
    - h_f (numpy.ndarray): Empirical frequencies of each unique haplotype.
    - K_truncation (int): Number of haplotypes to consider.
    - n_ind (int): Number of individuals.

    Returns:
    - Kcount (numpy.ndarray): Processed haplotype count spectrum.
    - Kspect (numpy.ndarray): Processed haplotype frequency spectrum.
    """
    # Truncate count and frequency spectrum
    Kcount = k[:K_truncation]
    Kspect = h_f[:K_truncation]

    # Normalize count and frequency spectra
    Kcount = Kcount / Kcount.sum() * n_ind
    Kspect = Kspect / Kspect.sum()

    # Pad with zeros if necessary
    if Kcount.size < K_truncation:
        Kcount = np.concatenate([Kcount, np.zeros(K_truncation - Kcount.size)])
        Kspect = np.concatenate([Kspect, np.zeros(K_truncation - Kspect.size)])

    return Kcount, Kspect


def LASSI_spectrum_and_Kspectrum(
    ts, rec_map, K_truncation: int, window: int, step: int
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute haplotype count and frequency spectra within sliding windows.

    Parameters:
    - hap (numpy.ndarray): Array of haplotypes where each column represents an individual and each row represents a SNP.
    - pos (numpy.ndarray): Array of SNP positions.
    - K_truncation (int): Number of haplotypes to consider.
    - window (int): Size of the sliding window.
    - step (int): Step size for sliding the window.

    Returns:
    - K_count (numpy.ndarray): Haplotype count spectra for each window.
    - K_spectrum (numpy.ndarray): Haplotype frequency spectra for each window.
    - windows_centers (numpy.ndarray): Centers of the sliding windows.
    """
    (
        hap_01,
        ac,
        biallelic_mask,
        hap_int,
        rec_map_01,
        position_masked,
        sequence_length,
        freqs,
    ) = open_tree(ts, rec_map)

    K_count = []
    K_spectrum = []
    windows_centers = []
    S, n = hap_int.shape
    for i in range(0, S, step):
        hap_subset = hap_int[i : i + window, :]

        # Calculate window center based on median SNP position
        windows_centers.append(np.median(position_masked[i : i + window]))

        # Compute empirical frequencies and process spectra for the window
        k, h_f = get_empir_freqs_np(hap_subset)
        K_count_subset, K_spectrum_subset = process_spectra(k, h_f, K_truncation, n)

        K_count.append(K_count_subset)
        K_spectrum.append(K_spectrum_subset)
        if hap_subset.shape[0] < window:
            break

    return np.array(K_count), np.array(K_spectrum), np.array(windows_centers)


def neut_average(K_spectrum: np.ndarray) -> np.ndarray:
    """
    Compute the neutral average of haplotype frequency spectra.

    Parameters:
    - K_spectrum (numpy.ndarray): Haplotype frequency spectra.

    Returns:
    - out (numpy.ndarray): Neutral average haplotype frequency spectrum.
    """
    weights = []
    S, n = K_spectrum.shape
    # Compute mean spectrum
    gwide_K = np.mean(K_spectrum, axis=0)

    # Calculate weights for averaging
    if S % 5e4 == 0:
        weights.append(5e4)
    else:
        small_weight = S % 5e4
        weights.append(small_weight)

    # Compute weighted average
    out = np.average([gwide_K], axis=0, weights=weights)

    return out


@njit("float64(float64[:],float64[:],int64)", cache=True)
def easy_likelihood(K_neutral, K_count, K_truncation):
    """
    Basic computation of the likelihood function; runs as-is for neutrality, but called as part of a larger process for sweep model
    """

    likelihood_list = []

    for i in range(K_truncation):
        likelihood_list.append(K_count[i] * np.log(K_neutral[i]))

    likelihood = sum(likelihood_list)

    return likelihood


@njit("float64(float64[:],float64[:],int64,int64,float64,float64)", cache=True)
def sweep_likelihood(K_neutral, K_count, K_truncation, m_val, epsilon, epsilon_max):
    """
    Computes the likelihood of a sweep under optimized parameters
    """

    if m_val != K_truncation:
        altspect = np.zeros(K_truncation)
        tailclasses = np.zeros(K_truncation - m_val)
        neutdiff = np.zeros(K_truncation - m_val)
        tailinds = np.arange(m_val + 1, K_truncation + 1)

        for i in range(len(tailinds)):
            ti = tailinds[i]
            denom = K_truncation - m_val - 1
            if denom != 0:
                the_ns = epsilon_max - ((ti - m_val - 1) / denom) * (
                    epsilon_max - epsilon
                )
            else:
                the_ns = epsilon
            tailclasses[i] = the_ns
            neutdiff[i] = K_neutral[ti - 1] - the_ns

        headinds = np.arange(1, m_val + 1)

        for hd in headinds:
            altspect[hd - 1] = K_neutral[hd - 1]

        neutdiff_all = np.sum(neutdiff)

        for ival in headinds:
            # class 3
            # total_exp = np.sum(np.exp(-headinds))
            # theadd = (np.exp(-ival) / total_exp) * neutdiff_all
            # class 5
            theadd = (1 / float(m_val)) * neutdiff_all
            altspect[ival - 1] += theadd

        altspect[m_val:] = tailclasses

        output = easy_likelihood(altspect, K_count, K_truncation)
    else:
        output = easy_likelihood(K_neutral, K_count, K_truncation)

    return output


def T_m_statistic(K_counts, K_neutral, windows, K_truncation, sweep_mode=5, i=0):
    output = []
    m_vals = K_truncation + 1
    epsilon_min = 1 / (K_truncation * 100)

    _epsilon_values = list(map(lambda x: x * epsilon_min, range(1, 101)))
    epsilon_max = K_neutral[-1]
    epsilon_values = []

    for ev in _epsilon_values:
        # ev = e * epsilon_min
        if ev <= epsilon_max:
            epsilon_values.append(ev)
    epsilon_values = np.array(epsilon_values)

    for j, w in enumerate(windows):
        # if(i==132):
        # break
        K_iter = K_counts[j]

        null_likelihood = easy_likelihood(K_neutral, K_iter, K_truncation)

        alt_likelihoods_by_e = []

        for e in epsilon_values:
            alt_likelihoods_by_m = []
            for m in range(1, m_vals):
                alt_like = sweep_likelihood(
                    K_neutral, K_iter, K_truncation, m, e, epsilon_max
                )
                alt_likelihoods_by_m.append(alt_like)

            alt_likelihoods_by_m = np.array(alt_likelihoods_by_m)
            likelihood_best_m = 2 * (alt_likelihoods_by_m.max() - null_likelihood)

            if likelihood_best_m > 0:
                ml_max_m = (alt_likelihoods_by_m.argmax()) + 1
            else:
                ml_max_m = 0

            alt_likelihoods_by_e.append([likelihood_best_m, ml_max_m, e])

        alt_likelihoods_by_e = np.array(alt_likelihoods_by_e)

        likelihood_real = max(alt_likelihoods_by_e[:, 0])

        out_index = np.flatnonzero(alt_likelihoods_by_e[:, 0] == likelihood_real)

        out_intermediate = alt_likelihoods_by_e[out_index]

        if out_intermediate.shape[0] > 1:
            constarg = min(out_intermediate[:, 1])

            outcons = np.flatnonzero(out_intermediate[:, 1] == constarg)

            out_cons_intermediate = out_intermediate[outcons]

            if out_cons_intermediate.shape[0] > 1:
                out_cons_intermediate = out_cons_intermediate[0]

            out_intermediate = out_cons_intermediate

        outshape = out_intermediate.shape

        if len(outshape) != 1:
            out_intermediate = out_intermediate[0]

        out_intermediate = np.concatenate(
            [out_intermediate, np.array([K_neutral[-1], sweep_mode, w]), K_iter]
        )

        output.append(out_intermediate)

    # output = np.array(output)
    # return output[output[:, 0].argmax(), :]

    K_names = ["Kcounts_" + str(i) for i in range(1, K_iter.size + 1)]
    output = pd.DataFrame(output)
    output.insert(output.shape[1], "iter", i)

    output.columns = (
        [
            "t_statistic",
            "m",
            "frequency",
            "e",
            "model",
            "window_lassi",
        ]
        + K_names
        + ["iter"]
    )
    return output


def neutral_hfs(sims, K_truncation, w_size, step, nthreads=1):
    pars = [(i[0], i[1]) for i in sims]

    # Log the start of the scheduling
    # logging.info("Scheduling {} {} simulations".format(len(s), k))

    # Use joblib to parallelize the execution
    hfs_stats = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(LASSI_spectrum_and_Kspectrum)(ts, rec_map, K_truncation, w_size, step)
        for index, (ts, rec_map) in enumerate(pars, 1)
    )

    K_counts, K_spectrum, windows = zip(*hfs_stats)

    return neut_average(np.vstack(K_spectrum))

    # t_m = Parallel(n_jobs=nthreads, verbose=5)(
    #     delayed(T_m_statistic)(kc, K_neutral, windows[index], K_truncation)
    #     for index, (kc) in enumerate(K_counts)
    # )
    # return (
    #     pd.DataFrame(t_m, columns=["t", "m", "frequency", "e", "model", "window"]),
    #     K_neutral,
    # )


def compute_t_m(
    sims,
    K_truncation,
    w_size,
    step,
    K_neutral=None,
    windows=[50000, 100000, 200000, 500000, 1000000],
    center=[5e5, 7e5],
    nthreads=1,
):
    pars = [(i[0], i[1]) for i in sims]

    # Log the start of the scheduling
    logging.info("Estimating HFS")

    # Use joblib to parallelize the execution
    hfs_stats = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(LASSI_spectrum_and_Kspectrum)(ts, rec_map, K_truncation, w_size, step)
        for index, (ts, rec_map) in enumerate(pars, 1)
    )

    K_counts, K_spectrum, windows_lassi = zip(*hfs_stats)

    if K_neutral is None:
        K_neutral = neut_average(np.vstack(K_spectrum))

    logging.info("Estimating T and m statistics")

    t_m = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(T_m_statistic)(
            kc, K_neutral, windows_lassi[index - 1], K_truncation, i=index
        )
        for index, (kc) in enumerate(K_counts, 1)
    )
    t_m_cut = Parallel(n_jobs=nthreads, verbose=0)(
        delayed(cut_t_m_argmax)(t, windows=windows, center=center) for t in t_m
    )

    return pd.concat(t_m_cut)


def cut_t_m(df_t_m, windows=[50000, 100000, 200000, 500000, 1000000], center=6e5):
    out = []
    for w in windows:
        # for w in [1000000]:
        lower = center - w / 2
        upper = center + w / 2

        df_t_m_subset = df_t_m[
            (df_t_m.iloc[:, 5] > lower) & (df_t_m.iloc[:, 5] < upper)
        ]
        try:
            # max_t = df_t_m_subset.iloc[:, 0].argmax()
            max_t = df_t_m_subset.iloc[:, 1].argmin()
            # df_t_m_subset = df_t_m_subset.iloc[max_t:max_t+1, [0,1,-1]]
            # df_t_m_subset.insert(0,'window',w*2)
            m = df_t_m_subset.m.mode()

            if m.size > 1:
                m = df_t_m_subset.iloc[max_t : max_t + 1, 1]

            out.append(
                pd.DataFrame(
                    {
                        "iter": df_t_m_subset["iter"].unique(),
                        "window": w,
                        "t_statistic": df_t_m_subset.t.mean(),
                        "m": m,
                    }
                )
            )
        except:
            out.append(
                pd.DataFrame(
                    {
                        "iter": df_t_m["iter"].unique(),
                        "window": w,
                        "t_statistic": 0,
                        "m": 0,
                    }
                )
            )

    out = pd.concat(out).reset_index(drop=True)

    return out


def cut_t_m_argmax(
    df_t_m,
    windows=[50000, 100000, 200000, 500000, 1000000],
    center=[5e5, 7e5],
    step=1e4,
):
    out = []
    centers = np.arange(center[0], center[1] + step, step).astype(int)
    iter_c_w = list(product(centers, windows))
    for c, w in iter_c_w:
        # for w in [1000000]:
        lower = c - w / 2
        upper = c + w / 2

        df_t_m_subset = df_t_m[
            (df_t_m.iloc[:, 5] > lower) & (df_t_m.iloc[:, 5] < upper)
        ]
        try:
            max_t = df_t_m_subset.iloc[:, 0].argmax()

            # df_t_m_subset = df_t_m_subset[df_t_m_subset.m > 0]
            # max_t = df_t_m_subset[df_t_m_subset.m > 0].m.argmin()
            df_t_m_subset = df_t_m_subset.iloc[max_t : max_t + 1, :]

            df_t_m_subset = df_t_m_subset.loc[
                :,
                ~df_t_m_subset.columns.isin(
                    ["iter", "frequency", "e", "model", "window_lassi"]
                ),
            ]
            df_t_m_subset.insert(0, "window", w)
            df_t_m_subset.insert(0, "center", c)
            df_t_m_subset.insert(0, "iter", df_t_m.iter.unique())

            out.append(df_t_m_subset)

        except:
            K_names = pd.DataFrame(
                {
                    k: 0
                    for k in df_t_m.columns[
                        df_t_m.columns.str.contains("Kcount")
                    ].values
                },
                index=[0],
            )

            out.append(
                pd.concat(
                    [
                        pd.DataFrame(
                            {
                                "iter": df_t_m["iter"].unique(),
                                "center": c,
                                "window": w,
                                "t_statistic": 0,
                                "m": 0,
                            }
                        ),
                        K_names,
                    ],
                    axis=1,
                )
            )

    out = pd.concat(out).reset_index(drop=True)

    return out


########


def fuli_f_star(hap, ac):
    """Calculates Fu and Li's D* statistic"""
    S, n = hap.shape

    an = np.sum(np.divide(1.0, range(1, n)))
    bn = np.sum(np.divide(1.0, np.power(range(1, n), 2)))
    an1 = an + np.true_divide(1, n)

    vfs = (
        (
            (2 * (n**3.0) + 110.0 * (n**2.0) - 255.0 * n + 153)
            / (9 * (n**2.0) * (n - 1.0))
        )
        + ((2 * (n - 1.0) * an) / (n**2.0))
        - ((8.0 * bn) / n)
    ) / ((an**2.0) + bn)
    ufs = (
        (
            n / (n + 1.0)
            + (n + 1.0) / (3 * (n - 1.0))
            - 4.0 / (n * (n - 1.0))
            + ((2 * (n + 1.0)) / ((n - 1.0) ** 2)) * (an1 - ((2.0 * n) / (n + 1.0)))
        )
        / an
    ) - vfs

    pi = mean_pairwise_difference(ac).sum()
    ss = np.sum(np.sum(hap, axis=1) == 1)
    Fstar1 = (pi - (((n - 1.0) / n) * ss)) / ((ufs * S + vfs * (S**2.0)) ** 0.5)
    return Fstar1


def fuli_f(hap, ac):
    an = np.sum(np.divide(1.0, range(1, n)))
    an1 = an + 1.0 / n
    bn = np.sum(np.divide(1.0, np.power(range(1, n), 2)))

    ss = np.sum(np.sum(hap, axis=1) == 1)
    pi = mean_pairwise_difference(ac).sum()

    if n == 2:
        cn = 1
    else:
        cn = 2.0 * (n * an - 2.0 * (n - 1.0)) / ((n - 1.0) * (n - 2.0))

    v = (
        cn + 2.0 * (np.power(n, 2) + n + 3.0) / (9.0 * n * (n - 1.0)) - 2.0 / (n - 1.0)
    ) / (np.power(an, 2) + bn)
    u = (
        1.0
        + (n + 1.0) / (3.0 * (n - 1.0))
        - 4.0 * (n + 1.0) / np.power(n - 1, 2) * (an1 - 2.0 * n / (n + 1.0))
    ) / an - v
    F = (pi - ss) / sqrt(u * S + v * np.power(S, 2))

    return F


def fuli_d_star(hap):
    """Calculates Fu and Li's D* statistic"""

    S, n = hap.shape
    an = np.sum(np.divide(1.0, range(1, n)))
    bn = np.sum(np.divide(1.0, np.power(range(1, n), 2)))
    an1 = an + np.true_divide(1, n)

    cn = 2 * (((n * an) - 2 * (n - 1))) / ((n - 1) * (n - 2))
    dn = (
        cn
        + np.true_divide((n - 2), ((n - 1) ** 2))
        + np.true_divide(2, (n - 1)) * (3.0 / 2 - (2 * an1 - 3) / (n - 2) - 1.0 / n)
    )

    vds = (
        ((n / (n - 1.0)) ** 2) * bn
        + (an**2) * dn
        - 2 * (n * an * (an + 1)) / ((n - 1.0) ** 2)
    ) / (an**2 + bn)
    uds = ((n / (n - 1.0)) * (an - n / (n - 1.0))) - vds

    ss = np.sum(np.sum(hap, axis=1) == 1)
    Dstar1 = ((n / (n - 1.0)) * S - (an * ss)) / (uds * S + vds * (S ^ 2)) ** 0.5
    return Dstar1


def fuli_d(hap):
    S, n = hap.shape

    an = np.sum(np.divide(1.0, range(1, n)))
    bn = np.sum(np.divide(1.0, np.power(range(1, n), 2)))

    ss = np.sum(np.sum(hap, axis=1) == 1)

    if n == 2:
        cn = 1
    else:
        cn = 2.0 * (n * an - 2.0 * (n - 1.0)) / ((n - 1.0) * (n - 2.0))

    v = 1.0 + (np.power(an, 2) / (bn + np.power(an, 2))) * (cn - (n + 1.0) / (n - 1.0))
    u = an - 1.0 - v
    D = (S - ss * an) / sqrt(u * S + v * np.power(S, 2))
    return D


# def r2_torch(hap):
#     device = "cpu"

#     g = HaplotypeArray(hap).to_genotypes(2)
#     g = np.array(g)
#     g = torch.tensor(g, dtype=torch.float32)
#     g = torch.reshape(g, (g.shape[0], g.shape[1] * 2))
#     # filter_lst = ~torch.all(g == 1, dim=1)
#     # g = g[filter_lst]

#     n = g.shape[1]
#     g = g.to(device)
#     gT = torch.transpose(g, 0, 1)
#     pAB = (g @ gT) / n
#     pAb = (g @ (1 - gT)) / n
#     paB = ((1 - g) @ gT) / n
#     pab = ((1 - g) @ (1 - gT)) / n

#     gn_s = torch.mean(g, dim=1)
#     pA, pB = torch.meshgrid(gn_s, gn_s, indexing="xy")

#     del gn_s
#     del g
#     del gT
#     D = pAB * (pab) - (pAb * paB)

#     D_squared = D**2
#     del D

#     r_squared = D_squared / (pA * (1 - pA) * pB * (1 - pB))
#     r_squared = torch.tril(r_squared, diagonal=-1)

#     del D_squared
#     del pA
#     del pB

#     return r_squared.numpy().T


### iSAFE


@njit("int64[:](float64[:])", cache=True)
def rank_with_duplicates(x):
    # sorted_arr = sorted(x, reverse=True)
    sorted_arr = np.sort(x)[::-1]
    rank_dict = {}
    rank = 1
    prev_value = -1

    for value in sorted_arr:
        if value != prev_value:
            rank_dict[value] = rank
        rank += 1
        prev_value = value

    return np.array([rank_dict[value] for value in x])


# @njit("float64[:,:](float64[:,:])", cache=True)
@njit(parallel=False)
def dot_nb(hap):
    return np.dot(hap.T, hap)


@njit
def dot_two_nb(x, y):
    return np.dot(x, y)


@njit
def neutrality_divergence_proxy(kappa, phi, freq, method=3):
    sigma1 = (kappa) * (1 - kappa)
    sigma1[sigma1 == 0] = 1.0
    sigma1 = sigma1**0.5
    p1 = (phi - kappa) / sigma1
    sigma2 = (freq) * (1 - freq)
    sigma2[sigma2 == 0] = 1.0
    sigma2 = sigma2**0.5
    p2 = (phi - kappa) / sigma2
    nu = freq[np.argmax(p1)]
    p = p1 * (1 - nu) + p2 * nu

    if method == 1:
        return p1
    elif method == 2:
        return p2
    elif method == 3:
        return p


# @njit('UniTuple(float64[:],2)(int64[:,:], float64[:])')
@njit
def calc_H_K(hap, haf):
    """
    :param snp_matrix: Binary SNP Matrix
    :return: H: Sum of HAF-score of carriers of each mutation.
    :return: N: Number of distinct carrier haplotypes of each mutation.

    """
    num_snps, num_haplotypes = hap.shape

    haf_matrix = haf * hap

    K = np.zeros((num_snps))

    for j in range(num_snps):
        ar = haf_matrix[j, :]
        K[j] = len(np.unique(ar[ar > 0]))
    H = np.sum(haf_matrix, 1)
    return (H, K)


def safe(hap):
    num_snps, num_haplotypes = hap.shape

    haf = dot_nb(hap.astype(np.float64)).sum(1)
    # haf = np.dot(hap.T, hap).sum(1)
    H, K = calc_H_K(hap, haf)

    phi = 1.0 * H / haf.sum()
    kappa = 1.0 * K / (np.unique(haf).shape[0])
    freq = hap.sum(1) / num_haplotypes
    safe_values = neutrality_divergence_proxy(kappa, phi, freq)

    # rank = np.zeros(safe_values.size)
    # rank = rank_with_duplicates(safe_values)
    rank = (
        pd.DataFrame(safe_values).rank(method="min", ascending=False).values.flatten()
    )

    return haf, safe_values, rank, phi, kappa, freq


def creat_windows_summary_stats_nb(hap, pos, w_size=300, w_step=150):
    num_snps, num_haplotypes = hap.shape
    rolling_indices = create_rolling_indices_nb(num_snps, w_size, w_step)
    windows_stats = {}
    windows_haf = []
    snp_summary = []
    for i, I in enumerate(rolling_indices):
        window_i_stats = {}
        haf, safe_values, rank, phi, kappa, freq = safe(hap[I[0] : I[1], :])
        tmp = pd.DataFrame(
            np.asarray(
                [
                    safe_values,
                    rank,
                    phi,
                    kappa,
                    freq,
                    pos[I[0] : I[1]],
                    np.arange(I[0], I[1]),
                    np.repeat(i, w_size),
                ]
            ).T,
            columns=[
                "safe",
                "rank",
                "phi",
                "kappa",
                "freq",
                "pos",
                "ordinal_pos",
                "window",
            ],
        )
        # tmp = np.vstack((safe_values, rank, phi, kappa, freq, pos[I[0]:I[1]],np.arange(I[0],I[1]),np.repeat(i,w_size))).T
        window_i_stats["safe"] = tmp
        windows_haf.append(haf)
        windows_stats[i] = window_i_stats
        snp_summary.append(tmp)
    return (
        windows_stats,
        windows_haf,
        pd.concat(snp_summary).reset_index(drop=True).astype(float),
    )


@njit
def create_rolling_indices_nb(total_variant_count, w_size, w_step):
    assert total_variant_count < w_size or w_size > 0

    rolling_indices = []
    w_start = 0
    while True:
        w_end = min(w_start + w_size, total_variant_count)
        if w_end >= total_variant_count:
            break
        rolling_indices.append([w_start, w_end])
        # rolling_indices += [range(int(w_start), int(w_end))]
        w_start += w_step

    return rolling_indices


def run_isafe(
    hap,
    positions,
    max_freq=1,
    min_region_size_bp=49000,
    min_region_size_ps=300,
    ignore_gaps=True,
    window=300,
    step=150,
    top_k=1,
    max_rank=15,
):
    """
    Estimate iSAFE or SAFE when not possible using default Flex-Sweep values.

    Args:
     hap (TYPE): Description
     total_window_size (TYPE): Description
     positions (TYPE): Description
     max_freq (int, optional): Description
     min_region_size_bp (int, optional): Description
     min_region_size_ps (int, optional): Description
     ignore_gaps (bool, optional): Description
     window (int, optional): Description
     step (int, optional): Description
     top_k (int, optional): Description
     max_rank (int, optional): Description

    Returns:
     TYPE: Description

    Raises:
     ValueError: Description
    """

    total_window_size = positions.max() - positions.min()

    dp = np.diff(positions)
    num_gaps = sum(dp > 6000000)
    f = hap.mean(1)
    freq_filter = ((1 - f) * f) > 0
    hap_filtered = hap[freq_filter, :]
    positions_filtered = positions[freq_filter]
    num_snps = hap_filtered.shape[0]

    if (num_snps <= min_region_size_ps) | (total_window_size < min_region_size_bp):
        haf, safe_values, rank, phi, kappa, freq = safe(hap_filtered)

        df_safe = pd.DataFrame(
            np.asarray(
                [
                    safe_values,
                    rank,
                    phi,
                    kappa,
                    freq,
                    positions_filtered,
                ]
            ).T,
            columns=["isafe", "rank", "phi", "kappa", "daf", "positions"],
        )

        return df_safe.loc[:, ["positions", "daf", "isafe"]].sort_values("positions")
    else:
        df_isafe = isafe(
            hap_filtered, positions_filtered, window, step, top_k, max_rank
        )
        df_isafe = (
            df_isafe.loc[df_isafe.freq < max_freq]
            .sort_values("ordinal_pos")
            .rename(columns={"id": "positions", "isafe": "isafe", "freq": "daf"})
        )

        df_isafe = df_isafe[df_isafe.daf < max_freq]
        return df_isafe.loc[:, ["positions", "daf", "isafe"]]


def isafe(hap, pos, w_size=300, w_step=150, top_k=1, max_rank=15):
    windows_summaries, windows_haf, snps_summary = creat_windows_summary_stats_nb(
        hap, pos, w_size, w_step
    )
    df_top_k1 = get_top_k_snps_in_each_window(snps_summary, k=top_k)

    ordinal_pos_snps_k1 = np.sort(df_top_k1["ordinal_pos"].unique()).astype(np.int64)

    psi_k1 = step_function(creat_matrix_Psi_k_nb(hap, windows_haf, ordinal_pos_snps_k1))

    df_top_k2 = get_top_k_snps_in_each_window(snps_summary, k=max_rank)
    temp = np.sort(df_top_k2["ordinal_pos"].unique())

    ordinal_pos_snps_k2 = np.sort(np.setdiff1d(temp, ordinal_pos_snps_k1)).astype(
        np.int64
    )

    psi_k2 = step_function(creat_matrix_Psi_k_nb(hap, windows_haf, ordinal_pos_snps_k2))

    alpha = psi_k1.sum(0) / psi_k1.sum()

    iSAFE1 = pd.DataFrame(
        data={"ordinal_pos": ordinal_pos_snps_k1, "isafe": np.dot(psi_k1, alpha)}
    )
    iSAFE2 = pd.DataFrame(
        data={"ordinal_pos": ordinal_pos_snps_k2, "isafe": np.dot(psi_k2, alpha)}
    )

    iSAFE1["tier"] = 1
    iSAFE2["tier"] = 2
    iSAFE = pd.concat([iSAFE1, iSAFE2]).reset_index(drop=True)
    iSAFE["id"] = pos[iSAFE["ordinal_pos"].values]
    freq = hap.mean(1)
    iSAFE["freq"] = freq[iSAFE["ordinal_pos"]]
    df_isafe = iSAFE[["ordinal_pos", "id", "isafe", "freq", "tier"]]

    return df_isafe


@njit
def creat_matrix_Psi_k_nb(hap, hafs, Ifp):
    P = np.zeros((len(Ifp), len(hafs)))
    for i in range(len(Ifp)):
        for j in range(len(hafs)):
            P[i, j] = isafe_kernel_nb(hafs[j], hap[Ifp[i], :])
    return P


@njit
def isafe_kernel_nb(haf, snp):
    phi = haf[snp == 1].sum() * 1.0 / haf.sum()
    kappa = len(np.unique(haf[snp == 1])) / (1.0 * len(np.unique(haf)))
    f = np.mean(snp)
    sigma2 = (f) * (1 - f)
    if sigma2 == 0:
        sigma2 = 1.0
    sigma = sigma2**0.5
    p = (phi - kappa) / sigma
    return p


def step_function(P0):
    P = P0.copy()
    P[P < 0] = 0
    return P


def get_top_k_snps_in_each_window(df_snps, k=1):
    """
    :param df_snps:  this datafram must have following columns: ["safe","ordinal_pos","window"].
    :param k:
    :return: return top k snps in each window.
    """
    return df_snps.loc[
        df_snps.groupby("window")["safe"].nlargest(k).index.get_level_values(1), :
    ].reset_index(drop=True)


# def normalization(
#     sweeps_stats,
#     neutral_stats,
#     center=[5e5, 7e5],
#     windows=[50000, 100000, 200000, 500000, 1000000],
#     nthreads=1,
# ):
#     df_snps, df_window, params = sweeps_stats
#     df_neutral = neutral_stats.snps

#     expected, stdev = normalize_neutral(df_neutral)

#     df_splitted = df_snps.groupby("iter")

#     # df_fv = Parallel(n_jobs=nthreads, verbose=5)(
#     #     delayed(normalize_cut)(
#     #         i, v, expected=expected, stdev=stdev, center=center, windows=windows
#     #     )
#     #     for (i, v) in df_splitted
#     # )

#     func = partial(
#         normalize_cut, expected=expected, stdev=stdev, center=center, windows=windows
#     )
#     with Pool(processes=nthreads) as pool:
#         df_fv = pool.starmap(func, df_splitted)

#     df_fv = pd.concat(df_fv)
#     df_fv = pd.merge(df_fv, df_window)

#     # params = params[:, [0, 1, 3, 4, ]]
#     df_fv = pd.concat(
#         [
#             pd.DataFrame(
#                 # np.repeat(params, df_window.window.unique().size, axis=0),
#                 np.repeat(
#                     params,
#                     df_window.loc[:, ["center", "window"]].drop_duplicates().shape[0],
#                     axis=0,
#                 ),
#                 columns=["s", "t", "t_end", "f_i", "f_t", "f_t_end"],
#             ),
#             df_fv,
#         ],
#         axis=1,
#     )

#     return df_fv
#########################################


# Define the inner named tuple structure
summaries = namedtuple("summaries", ["stats", "parameters"])


def normalization2(
    sweeps_stats,
    neutral_stats_norm,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
    nthreads=1,
):
    df_stats, params = sweeps_stats
    df_stats_neutral, params_neutral = neutral_stats_norm

    expected, stdev = normalize_neutral2(df_stats_neutral)

    # Too fast execution to schedule properly. 10 threads is enough
    if nthreads >= 100:
        nthreads /= 10
    df_fv_n = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(normalize_cut2)(
            _iter, v, expected=expected, stdev=stdev, center=center, windows=windows
        )
        for _iter, v in enumerate(df_stats, 1)
    )

    df_window = (
        pd.concat([i.loc[:, ["iter", "h12", "haf"]] for i in df_stats])
        .dropna()
        .reset_index(drop=True)
    )
    df_fv_n = pd.concat(df_fv_n)
    df_fv_n = pd.merge(df_fv_n, df_window, how="outer")

    # params = params[:, [0, 1, 3, 4, ]]
    df_fv_n = pd.concat(
        [
            pd.DataFrame(
                np.repeat(
                    params.copy(),
                    df_fv_n.loc[:, ["center", "window"]].drop_duplicates().shape[0],
                    axis=0,
                ),
                columns=["s", "t", "f_i", "f_t"],
            ),
            df_fv_n,
        ],
        axis=1,
    )

    return df_fv_n, {"expected": expected, "stdev": stdev}


def normalize_neutral2(df_stats_neutral):
    # df_snps, df_window = df_stats_neutral

    window_stats = ["h12", "haf"]

    # Get std and mean values from dataframe
    tmp_neutral = pd.concat(df_stats_neutral)
    df_binned = bin_values2(tmp_neutral.loc[:, ~tmp_neutral.columns.isin(window_stats)])

    # get expected value (mean) and standard deviation
    expected = df_binned.iloc[:, 5:].groupby("freq_bins").mean()
    stdev = df_binned.iloc[:, 5:].groupby("freq_bins").std()

    expected.index = expected.index.astype(str)
    stdev.index = stdev.index.astype(str)

    return expected, stdev


def bin_values2(values, freq=0.02):
    # Create a deep copy of the input variable
    values_copy = values.copy()

    # Modify the copy
    values_copy.loc[:, "freq_bins"] = pd.cut(
        x=values["daf"],
        bins=np.arange(0, 1 + freq, freq),
        include_lowest=True,
        precision=2,
    ).astype(str)

    return values_copy


def normalize_cut2(
    _iter,
    snps_values,
    expected,
    stdev,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
):
    binned_values = bin_values2(snps_values.iloc[:, :-2]).copy()

    for stat in binned_values.columns[5:-1]:
        binned_values[stat] -= (
            binned_values.loc[:, [stat, "freq_bins"]]
            .dropna()
            .freq_bins.map(expected[stat])
        )
        binned_values[stat] /= binned_values["freq_bins"].map(stdev[stat])

    binned_values = binned_values.drop(
        ["daf", "freq_bins"], axis=1, inplace=False
    ).copy()
    out = []
    # cut window stats to only SNPs within the window around center
    centers = np.arange(center[0], center[1] + 1e4, 1e4).astype(int)
    iter_c_w = list(product(centers, windows))

    tmp_2 = binned_values.loc[
        (binned_values.center == 6e5) & (binned_values.window == 1e6),
        ~binned_values.columns.isin(
            ["isafe", "delta_ihh", "ihs", "nsl", "center", "window"]
        ),
    ]

    for c, w in iter_c_w:
        tmp_1 = binned_values.loc[
            (binned_values.center == c) & (binned_values.window == 1e6),
            ["iter", "positions", "isafe", "ihs", "nsl"],
        ]
        tmp = pd.merge(tmp_1, tmp_2, how="outer")
        lower = c - w / 2
        upper = c + w / 2
        cut_values = (
            tmp[(tmp["positions"] >= lower) & (tmp["positions"] <= upper)]
            .iloc[:, 2:]
            .mean()
        )

        out.append(cut_values)

    out = pd.concat(out, axis=1).T
    out = pd.concat([pd.DataFrame(iter_c_w), out], axis=1)
    out.columns = ["center", "window"] + list(out.columns)[2:]
    out.insert(0, "iter", _iter)
    return out


def run_h12(
    hap,
    rec_map,
    _iter=1,
    neutral=True,
    script="/home/jmurgamoreno/software/calculate_H12_modified.pl",
):
    df_hap = pd.DataFrame(hap)
    df_rec_map = pd.DataFrame(rec_map)
    hap_file = "/tmp/tmp_" + str(_iter) + ".hap"
    map_file = "/tmp/tmp_" + str(_iter) + ".map"
    with open(hap_file, "w") as f:
        for row in df_hap.itertuples(index=False, name=None):
            f.write("".join(map(str, row)) + "\n")

    df_rec_map.to_csv(map_file, index=False, header=None, sep=" ")

    h12_enard = "perl " + script + " " + hap_file + " " + map_file + " out "
    h12_enard += "500000 " if neutral else "1200000"

    with subprocess.Popen(h12_enard.split(), stdout=subprocess.PIPE) as process:
        h12_v = float(process.stdout.read())

    os.remove(hap_file)
    os.remove(map_file)

    return h12_v


def calculate_stats2(
    ts,
    rec_map,
    i=1,
    center=[5e5, 7e5],
    windows=[1000000],
    step=1e4,
    neutral=False,
):
    warnings.filterwarnings(
        "ignore",
        category=RuntimeWarning,
        message="invalid value encountered in scalar divide",
    )
    np.seterr(divide="ignore", invalid="ignore")
    # Open and filtering data
    (
        hap_01,
        ac,
        biallelic_mask,
        hap_int,
        rec_map_01,
        position_masked,
        sequence_length,
        freqs,
    ) = open_tree(ts, rec_map)
    if len(center) == 1:
        centers = np.arange(center[0], center[0] + step, step).astype(int)
    else:
        centers = np.arange(center[0], center[1] + step, step).astype(int)

    stats = [
        "dind",
        "haf",
        "hapdaf_o",
        "isafe",
        "high_freq",
        "hapdaf_s",
        "nsl",
        "s_ratio",
        "low_freq",
        "ihs",
        "h12",
    ]

    df_dind_high_low = dind_high_low(hap_int, ac, rec_map_01)
    df_s_ratio = s_ratio(hap_int, ac, rec_map_01)
    df_hapdaf_o = hapdaf_o(hap_int, ac, rec_map_01)
    df_hapdaf_s = hapdaf_s(hap_int, ac, rec_map_01)

    # h12_v = h(hap_int, position_masked)
    h12_v = run_h12(ts, rec_map, _iter=i, neutral=neutral)
    haf_v = haf_top(hap_int.astype(np.float64), position_masked)

    df_snps = reduce(
        pd_merger,
        [
            df_dind_high_low,
            df_s_ratio,
            df_hapdaf_o,
            df_hapdaf_s,
        ],
    )

    df_snps.insert(0, "window", int(1e6))
    df_snps.insert(0, "center", int(6e5))
    df_snps.insert(0, "iter", i)
    df_snps.positions = df_snps.positions.astype(int)

    df_window = pd.DataFrame(
        [[i, int(6e5), int(1e6), int(5e5), 1.0, h12_v, haf_v]],
        columns=["iter", "center", "window", "positions", "daf", "h12", "haf"],
    )

    df_snps_centers = []
    # nsl_d ={}
    for c, w in product(centers, windows):
        lower = c - w / 2
        upper = c + w / 2

        p_mask = (position_masked >= lower) & (position_masked <= upper)
        f_mask = freqs >= 0.05

        # Check whether the hap subset is empty or not
        if hap_int[p_mask].shape[0] == 0:
            df_centers_stats = pd.DataFrame(
                {
                    "iter": i,
                    "center": c,
                    "window": w,
                    "positions": np.nan,
                    "daf": np.nan,
                    "isafe": np.nan,
                    "ihs": np.nan,
                    "nsl": np.nan,
                },
                index=[0],
            )
        else:
            df_isafe = run_isafe(hap_int[p_mask], position_masked[p_mask])

            # iHS and nSL
            df_ihs = ihs_ihh(
                hap_01[p_mask],
                position_masked[p_mask],
                min_ehh=0.05,
                min_maf=0.05,
                include_edges=False,
            )
            # df_ihs = run_hapbin(hap_int[p_mask], rec_map_01[p_mask], _iter=i, cutoff=0.05)

            nsl_v = nsl(hap_01.subset((p_mask) & (f_mask)), use_threads=False)

            df_nsl = pd.DataFrame(
                {
                    "positions": position_masked[(p_mask) & (f_mask)],
                    "daf": freqs[(p_mask) & (f_mask)],
                    "nsl": nsl_v,
                }
            )

            df_centers_stats = reduce(pd_merger, [df_isafe, df_ihs, df_nsl])
            # df_centers_stats = reduce(pd_merger, [df_isafe, df_ihs])

            df_centers_stats.insert(0, "window", w)
            df_centers_stats.insert(0, "center", c)
            df_centers_stats.insert(0, "iter", i)
            df_centers_stats = df_centers_stats.astype(object)
            # df_nsl.insert(0, "window", w)
            # df_nsl.insert(0, "center", c)
            # df_nsl.insert(0, "iter", i)

            # nsl_d[c] = df_nsl

        df_snps_centers.append(df_centers_stats)

    df_snps_centers = pd.concat(df_snps_centers)
    df_snps_centers = df_snps_centers.infer_objects()
    df_snps = pd.merge(df_snps_centers, df_snps, how="outer")

    df_snps = df_snps.sort_values(by=["center", "window", "positions"]).reset_index(
        drop=True
    )

    df_stats = pd.merge(df_snps, df_window, how="outer")
    if neutral:
        # Whole chromosome statistic to normalize
        df_isafe = run_isafe(hap_int, position_masked)
        df_ihs = ihs_ihh(hap_01, position_masked, min_ehh=0.1, include_edges=True)
        # df_ihs = run_hapbin(hap_01, rec_map_01, _iter=i, cutoff=0.1)

        nsl_v = nsl(hap_01.subset(freqs >= 0.05), use_threads=False)

        df_nsl = pd.DataFrame(
            {
                "positions": position_masked[freqs >= 0.05],
                "daf": freqs[freqs >= 0.05],
                "nsl": nsl_v,
            }
        )

        df_snps_norm = reduce(
            pd_merger,
            [
                df_snps[df_snps.center == 6e5].iloc[
                    :,
                    ~df_snps.columns.isin(
                        ["iter", "center", "window", "delta_ihh", "ihs", "isafe", "nsl"]
                    ),
                ],
                df_isafe,
                df_ihs,
                df_nsl,
            ],
        )

        df_snps_norm.insert(0, "window", int(1.2e6))
        df_snps_norm.insert(0, "center", int(6e5))
        df_snps_norm.insert(0, "iter", i)

        df_snps_norm = df_snps_norm.sort_values(
            by=["center", "window", "positions"]
        ).reset_index(drop=True)

        df_stats_norm = pd.merge(df_snps_norm, df_window, how="outer")

        return df_stats, df_stats_norm
    else:
        return df_stats


def summary_statistics2(
    sims,
    nthreads=1,
    neutral_save=None,
    center=[500000, 700000],
    windows=[1000000],
    step=10000,
):
    """ """

    if isinstance(sims, list) or isinstance(sims, tuple):
        sims = {"sweeps": sims, "neutral": []}

    assert len(sims["sweeps"]) > 0 and (
        len(sims["neutral"]) > 0 or neutral_save is not None
    ), "Please input neutral and sweep simulations"

    for k, s in sims.items():
        pars = [(i[0], i[1]) for i in s]

        # Log the start of the scheduling
        logging.info("Scheduling {} {} simulations".format(len(s), k))

        # Use joblib to parallelize the execution
        summ_stats = Parallel(n_jobs=nthreads, verbose=5)(
            delayed(calculate_stats2)(
                ts,
                rec_map,
                index,
                center=center,
                step=step,
                neutral=True if k == "neutral" else False,
            )
            for index, (ts, rec_map) in enumerate(pars, 1)
        )
        # Ensure params order
        params = np.row_stack(tuple(zip(*s))[-1])

        if k == "neutral":
            summ_stats, summ_stats_norm = zip(*summ_stats)
            neutral_stats = summaries(
                stats=summ_stats,
                parameters=params,
            )
            neutral_stats_norm = summaries(
                stats=summ_stats_norm,
                parameters=params,
            )
        else:
            if ~np.all(params[:, 3] == 0):
                params[:, 0] = -np.log(params[:, 0])
            # summ_stats, summ_nsl = zip(*summ_stats)
            sweeps_stats = summaries(
                stats=summ_stats,
                parameters=params,
            )

    df_fv_sweep, neutral_norm = normalization2(
        sweeps_stats, neutral_stats_norm, nthreads=nthreads
    )
    # df_fv_sweep, neutral_norm = normalization2(sweeps_stats, neutral_stats, nthreads=nthreads)

    df_fv_sweep["model"] = "sweep"

    df_fv_sweep.loc[
        (df_fv_sweep.t >= 2000) & (df_fv_sweep.f_t >= 0.9), "model"
    ] = "hard_old_complete"
    df_fv_sweep.loc[
        (df_fv_sweep.t >= 2000) & (df_fv_sweep.f_t < 0.9), "model"
    ] = "hard_old_incomplete"
    df_fv_sweep.loc[
        (df_fv_sweep.t < 2000) & (df_fv_sweep.f_t >= 0.9), "model"
    ] = "hard_young_complete"
    df_fv_sweep.loc[
        (df_fv_sweep.t < 2000) & (df_fv_sweep.f_t < 0.9), "model"
    ] = "hard_young_incomplete"

    df_fv_sweep.loc[df_fv_sweep.f_i != df_fv_sweep.f_i.min(), "model"] = df_fv_sweep[
        df_fv_sweep.f_i != df_fv_sweep.f_i.min()
    ].model.str.replace("hard", "soft")

    if np.all(df_fv_sweep.s.values == 0):
        df_fv_sweep.loc[:, "model"] = "neutral"

    # Unstack instead pivot since we only need to reshape based on window and center values
    df_fv_sweep.set_index(
        [
            "iter",
            "s",
            "t",
            "f_i",
            "f_t",
            "model",
            "window",
            "center",
        ],
        inplace=True,
    )
    df_fv_sweep_w = df_fv_sweep.unstack(level=["window", "center"])

    df_fv_sweep_w.columns = [
        f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_sweep_w.columns
    ]
    df_fv_sweep_w.reset_index(inplace=True)

    # Normalizing neutral simulations
    # Redoing normalized neutral, faster enough.
    df_fv_neutral, tmp_norm = normalization2(
        neutral_stats, neutral_stats_norm, nthreads=nthreads
    )

    df_fv_neutral["model"] = "neutral"

    # Unstack instead pivot since we only need to reshape based on window and center values
    df_fv_neutral.set_index(
        [
            "iter",
            "s",
            "t",
            "f_i",
            "f_t",
            "model",
            "window",
            "center",
        ],
        inplace=True,
    )

    df_fv_neutral_w = df_fv_neutral.unstack(level=["window", "center"])

    df_fv_neutral_w.columns = [
        f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_neutral_w.columns
    ]
    df_fv_neutral_w.reset_index(inplace=True)

    df_fv_w = pd.concat([df_fv_sweep_w, df_fv_neutral_w], axis=0)

    # dump fvs with more than 10% nans
    num_nans = df_fv_w.iloc[:, 6:].isnull().sum(axis=1)
    df_fv_w = df_fv_w[int(df_fv_w.iloc[:, 6:].shape[1] * 0.1) > num_nans]
    df_fv_w = df_fv_w.fillna(0)

    return df_fv_w


def normalization3(
    sweeps_stats,
    neutral_stats_norm,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
    nthreads=1,
):
    df_stats, params = sweeps_stats
    df_stats_neutral, params_neutral = neutral_stats_norm

    expected, stdev = normalize_neutral2(df_stats_neutral)

    # Too fast execution to schedule properly. 10 threads is enough
    if nthreads >= 100:
        nthreads /= 10
    df_fv_n = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(normalize_cut3)(
            _iter, v, expected=expected, stdev=stdev, center=center, windows=windows
        )
        for _iter, v in enumerate(df_stats, 1)
    )

    df_window = (
        pd.concat([i.loc[:, ["iter", "h12", "haf"]] for i in df_stats])
        .dropna()
        .reset_index(drop=True)
    )
    df_fv_n = pd.concat(df_fv_n)
    df_fv_n = pd.merge(df_fv_n, df_window, how="outer")

    # params = params[:, [0, 1, 3, 4, ]]
    df_fv_n = pd.concat(
        [
            pd.DataFrame(
                np.repeat(
                    params.copy(),
                    df_fv_n.loc[:, ["center", "window"]].drop_duplicates().shape[0],
                    axis=0,
                ),
                columns=["s", "t", "f_i", "f_t"],
            ),
            df_fv_n,
        ],
        axis=1,
    )

    return df_fv_n, {"expected": expected, "stdev": stdev}


def normalize_cut3(
    _iter,
    snps_values,
    expected,
    stdev,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
):
    binned_values = bin_values2(snps_values.iloc[:, :-2]).copy()

    for stat in binned_values.columns[5:-1]:
        binned_values[stat] -= binned_values["freq_bins"].map(expected[stat])
        binned_values[stat] /= binned_values["freq_bins"].map(stdev[stat])

    binned_values = binned_values.drop(
        ["center", "window", "daf", "freq_bins"], axis=1, inplace=False
    ).copy()

    out = []
    # cut window stats to only SNPs within the window around center
    centers = np.arange(center[0], center[1] + 1e4, 1e4).astype(int)
    iter_c_w = list(product(centers, windows))
    for c, w in iter_c_w:
        lower = c - w / 2
        upper = c + w / 2
        cut_values = (
            binned_values[
                (binned_values["positions"] >= lower)
                & (binned_values["positions"] <= upper)
            ]
            .iloc[:, 2:]
            .mean()
        )
        out.append(cut_values)

    out = pd.concat(out, axis=1).T
    out = pd.concat([pd.DataFrame(iter_c_w), out], axis=1)
    out.columns = ["center", "window"] + list(out.columns)[2:]
    out.insert(0, "iter", _iter)
    return out


def calculate_stats3(
    ts, rec_map, i=1, center=[5e5, 7e5], windows=[1000000], step=1e4, neutral=False
):
    warnings.filterwarnings(
        "ignore",
        category=RuntimeWarning,
        message="invalid value encountered in scalar divide",
    )
    np.seterr(divide="ignore", invalid="ignore")

    # Open and filtering data
    (
        hap_01,
        ac,
        biallelic_mask,
        hap_int,
        rec_map_01,
        position_masked,
        sequence_length,
        freqs,
    ) = open_tree(ts, rec_map)
    if len(center) == 1:
        centers = np.arange(center[0], center[0] + step, step).astype(int)
    else:
        centers = np.arange(center[0], center[1] + step, step).astype(int)

    df_dind_high_low = dind_high_low(hap_int, ac, rec_map_01)
    df_s_ratio = s_ratio(hap_int, ac, rec_map_01)
    df_hapdaf_o = hapdaf_o(hap_int, ac, rec_map_01)
    df_hapdaf_s = hapdaf_s(hap_int, ac, rec_map_01)
    df_isafe = run_isafe(hap_int, position_masked)

    # iHS and nSL
    # df_ihs = ihs_ihh(
    #     hap_01, position_masked, min_ehh=0.05, min_maf=0.05, include_edges=False
    # )
    df_ihs = run_hapbin(hap_int, rec_map_01, _iter=i, cutoff=0.05)
    nsl_v = nsl(hap_01.subset(freqs >= 0.05), use_threads=False)

    df_nsl = pd.DataFrame(
        {
            "positions": position_masked[freqs >= 0.05],
            "daf": freqs[freqs >= 0.05],
            "nsl": nsl_v,
        }
    ).dropna()

    df_snps = reduce(
        pd_merger,
        [
            df_isafe,
            df_ihs,
            df_nsl,
            df_dind_high_low,
            df_s_ratio,
            df_hapdaf_o,
            df_hapdaf_s,
        ],
    )

    df_snps.insert(0, "window", int(1e6))
    df_snps.insert(0, "center", int(6e5))
    df_snps.insert(0, "iter", i)

    df_snps = df_snps.sort_values(by=["center", "window", "positions"]).reset_index(
        drop=True
    )

    # h12_v = h(hap_int, position_masked)
    h12_v = run_h12(ts, rec_map, _iter=i, neutral=neutral)
    haf_v = haf_top(hap_int.astype(np.float64), position_masked)

    df_window = pd.DataFrame(
        [[i, int(6e5), int(1e6), int(5e5), 1.0, h12_v, haf_v]],
        columns=["iter", "center", "window", "positions", "daf", "h12", "haf"],
    )

    df_stats = pd.merge(df_snps, df_window, how="outer")
    return df_stats


def summary_statistics3(
    sims,
    nthreads=1,
    neutral_save=None,
    center=[500000, 700000],
    windows=[1000000],
    step=10000,
):
    """Summary

    Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    sims (TYPE): Description
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    nthreads (TYPE): Description

    Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    TYPE: Description
    """

    if isinstance(sims, list) or isinstance(sims, tuple):
        sims = {"sweeps": sims, "neutral": []}

    assert len(sims["sweeps"]) > 0 and (
        len(sims["neutral"]) > 0 or neutral_save is not None
    ), "Please input neutral and sweep simulations"

    for k, s in sims.items():
        pars = [(i[0], i[1]) for i in s]

        # Log the start of the scheduling
        logging.info("Scheduling {} {} simulations".format(len(s), k))

        # Use joblib to parallelize the execution
        summ_stats = Parallel(n_jobs=nthreads, verbose=5)(
            delayed(calculate_stats3)(
                ts,
                rec_map,
                i=index,
                center=center,
                step=step,
                neutral=True if k == "neutral" else False,
            )
            for index, (ts, rec_map) in enumerate(pars, 1)
        )

        # Ensure params order
        params = np.row_stack(tuple(zip(*s))[-1])

        if k == "neutral":
            neutral_stats = summaries(
                stats=summ_stats,
                parameters=params,
            )
        else:
            if ~np.all(params[:, 3] == 0):
                params[:, 0] = -np.log(params[:, 0])

            sweeps_stats = summaries(
                stats=summ_stats,
                parameters=params,
            )

    df_fv, neutral_norm = normalization3(sweeps_stats, neutral_stats, nthreads=nthreads)

    df_fv["model"] = "sweep"

    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_old_complete"
    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t < 0.9), "model"] = "hard_old_incomplete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_young_complete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t < 0.9), "model"] = "hard_young_incomplete"

    df_fv.loc[df_fv.f_i != df_fv.f_i.min(), "model"] = df_fv[
        df_fv.f_i != df_fv.f_i.min()
    ].model.str.replace("hard", "soft")

    if np.all(df_fv.s.values == 0):
        df_fv.loc[:, "model"] = "neutral"

    # Unstack instead pivot since we only need to reshape based on window and center values
    df_fv.set_index(
        [
            "iter",
            "s",
            "t",
            "f_i",
            "f_t",
            "model",
            "window",
            "center",
        ],
        inplace=True,
    )
    df_fv_w = df_fv.unstack(level=["window", "center"])

    df_fv_w.columns = [
        f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_w.columns
    ]
    df_fv_w.reset_index(inplace=True)

    # Normalizing neutral simulations
    # Redoing normalized neutral, faster enough.
    df_fv_neutral, tmp_norm = normalization3(
        deepcopy(neutral_stats), neutral_stats, nthreads=nthreads
    )

    df_fv_neutral["model"] = "neutral"

    # Unstack instead pivot since we only need to reshape based on window and center values
    df_fv_neutral.set_index(
        [
            "iter",
            "s",
            "t",
            "f_i",
            "f_t",
            "model",
            "window",
            "center",
        ],
        inplace=True,
    )

    df_fv_neutral_w = df_fv_neutral.unstack(level=["window", "center"])

    df_fv_neutral_w.columns = [
        f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_neutral_w.columns
    ]
    df_fv_neutral_w.reset_index(inplace=True)
    # df_fv_neutral_w.loc[:, "iter"] = 0
    df_fv_w = pd.concat([df_fv_w, df_fv_neutral_w], axis=0)

    # dump fvs with more than 10% nans
    num_nans = df_fv_w.iloc[:, 6:].isnull().sum(axis=1)
    df_fv_w = df_fv_w[int(df_fv_w.iloc[:, 6:].shape[1] * 0.1) > num_nans]
    df_fv_w.fillna(0, inplace=True)

    return df_fv_w


def mispolarize(hap, proportion=0.1):
    # Get shape of haplotype matrix
    S, n = hap.shape

    # Generate haplotype indices matrix of shape (S, n)
    haplotype_indices = np.tile(np.arange(n), (S, 1))

    # Shuffle each row using random permutations without in-place modification
    shuffled_indices = np.apply_along_axis(np.random.permutation, 1, haplotype_indices)

    # Select the column indices to flip based on the given proportion
    to_flip = shuffled_indices[:, : int(n * proportion)]

    # Create a copy of the original hap matrix to avoid in-place modification
    hap_copy = hap.copy()

    # Flip the selected elements using vectorized operations
    for row, flip_indices in zip(hap_copy, to_flip):
        row[flip_indices] ^= 1  # Perform XOR to flip bits

    return hap_copy


@njit("int8[:,:](int8[:,:],float64)")
def mispolarize_nb(hap, proportion):
    # Get the shape of the haplotype matrix
    S, n = hap.shape

    # Calculate how many haplotypes to flip based on the proportion
    num_to_flip = int(n * proportion)

    # Create a copy of the hap matrix to avoid in-place modification
    hap_copy = hap.copy()

    # For each row in the hap matrix
    for i in range(S):
        # Generate a random permutation of indices for each variant (row)
        indices = np.random.permutation(n)

        # Select the indices to flip
        to_flip = indices[:num_to_flip]

        # Perform the flip using XOR on the selected haplotypes
        for j in to_flip:
            hap_copy[i, j] ^= 1  # XOR flips between 0 and 1

    return hap_copy


def h12_enard(ts, rec_map, window_size=500000):
    coords, haplos, true_coords, count_coords = process_hap_map(ts, rec_map)

    maxhaplos = {}
    secondhaplos = {}
    thirdhaplos = {}
    keep_haplo_freq = {}

    key_001 = 600000
    coord = key_001
    int_coord = (coord // 100) * 100
    inf = int_coord - window_size // 2
    sup = int_coord + window_size // 2
    hap_line = "1" * 100
    hap = list(hap_line)

    ongoing_haplos = defaultdict(str)

    for i in range(1, window_size // 200):
        inf_i = int_coord - i * 100
        low_bound = inf_i

        if inf_i <= 0:
            break

        if inf_i in coords.keys():
            chain = coords[inf_i]
            splitter_chain = chain.split()
            for true_coord in splitter_chain:
                true_coord = int(true_coord)
                if true_coord != coord:
                    haplotype = haplos[true_coord]
                    current_haplo = list(haplotype)
                    for k, h in enumerate(hap):
                        if h == "1":
                            ongoing_haplos[str(k)] += f"{current_haplo[k]} "

        if i * 100 >= window_size // 2:
            break

    for i in range(1, window_size // 200):
        sup_i = int_coord + i * 100
        up_bound = sup_i

        if sup_i >= 1200000:
            break

        if sup_i in coords.keys():
            chain = coords[sup_i]
            splitter_chain = chain.split()
            for true_coord in splitter_chain:
                true_coord = int(true_coord)
                if true_coord != coord:
                    haplotype = haplos[true_coord]
                    current_haplo = list(haplotype)
                    for k, h in enumerate(hap):
                        if h == "1":
                            ongoing_haplos[str(k)] += f"{current_haplo[k]} "

        if i * 100 >= window_size // 2:
            break

    haplos_number = defaultdict(int)
    for key_ongo in sorted(ongoing_haplos.keys()):
        haplo = ongoing_haplos[key_ongo]
        haplos_number[haplo] += 1

    max_haplo = ""
    second_haplo = ""
    third_haplo = ""

    best_haplos = {}
    revert_number = defaultdict(str)

    # Populate revert_number dictionary
    for key_numb in sorted(haplos_number.keys()):
        number = haplos_number[key_numb]
        revert_number[number] += f"{key_numb}_"

    counter_rev = 0
    done_rev = 0

    # Sort revert_number keys in descending order and process
    for key_rev in sorted(revert_number.keys(), reverse=True):
        chain = revert_number[key_rev]
        splitter_chain = chain.split("_")
        for f, haplo in enumerate(splitter_chain):
            if haplo:  # Check if the haplo is not empty
                done_rev += 1
                best_haplos[done_rev] = haplo
                keep_haplo_freq[done_rev] = key_rev

        counter_rev += done_rev

        if counter_rev >= 10:
            break

    similar_pairs = defaultdict(str)
    done = {}

    # Ensure best_haplos has string keys
    best_haplos = {str(k): v for k, v in best_haplos.items()}

    # Initialize similar_pairs
    for key_compf in sorted(best_haplos.keys(), key=int):
        similar_pairs[key_compf] = ""

    for key_comp in sorted(best_haplos.keys(), key=int):
        for key_comp2 in sorted(best_haplos.keys(), key=int):
            if key_comp != key_comp2 and f"{key_comp} {key_comp2}" not in done:
                haplo_1 = best_haplos[key_comp]
                haplo_2 = best_haplos[key_comp2]
                splitter_haplo_1 = haplo_1.split()
                splitter_haplo_2 = haplo_2.split()

                identical = 0
                different = 0
                total = 0

                for h1, h2 in zip(splitter_haplo_1, splitter_haplo_2):
                    if h1 == "1" and h2 == "1":
                        identical += 1
                        total += 1
                    elif (h1 == "0" and h2 == "1") or (h1 == "1" and h2 == "0"):
                        different += 1
                        total += 1

                if total > 0 and different / total <= 0.2:
                    similar_pairs[key_comp] += f"{key_comp2} "
                    done[f"{key_comp} {key_comp2}"] = "yes"
                    done[f"{key_comp2} {key_comp}"] = "yes"

    exclude = {}
    counter_rev2 = 0
    max_haplo = ""
    second_haplo = ""
    third_haplo = ""

    for key_rev2 in sorted(similar_pairs, key=int):
        key_rev2 = str(key_rev2)
        if key_rev2 not in exclude:
            chain = best_haplos[key_rev2]
            similar = similar_pairs[key_rev2]
            if similar != "":
                splitter_similar = similar.split()
                for cur_rev in splitter_similar:
                    exclude[cur_rev] = "yes"
                    chain += "_" + best_haplos[cur_rev]

            counter_rev2 += 1

            if counter_rev2 == 1:
                max_haplo = chain
            elif counter_rev2 == 2:
                second_haplo = chain
            elif counter_rev2 == 3:
                third_haplo = chain
                break

    freq_1 = 0
    freq_2 = 0
    freq_3 = 0
    toto = 0

    for key_ongo2 in sorted(ongoing_haplos.keys()):
        ongoing = ongoing_haplos[key_ongo2]
        toto += 1

        if ongoing in max_haplo:
            freq_1 += 1
        elif ongoing in second_haplo:
            freq_2 += 1
        elif ongoing in third_haplo:
            freq_3 += 1

    H12 = ((freq_1 / toto) + (freq_2 / toto)) ** 2

    return H12
