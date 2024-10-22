import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_MAX_THREADS"] = "1"

from typing import Tuple, List
import numpy as np
import math
import pandas as pd
from tskit import load
from isafe import isafe
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

from copy import deepcopy
from collections import defaultdict, namedtuple
from numba import njit
from joblib import Parallel, delayed
from itertools import product, chain

# Set up logging configuration
# logging.basicConfig(level=logging.INFO, format="%(message)s")

pd_merger = partial(pd.merge, how="outer")

# Define the inner named tuple structure
summaries = namedtuple("summaries", ["snps", "window", "parameters"])


#################
def normalization(sweeps, neutral, center=[5e5, 7e5], nthreads=1):
    df_snps, df_window, params = sweeps
    df_neutral = neutral.snps

    expected, stdev = normalize_neutral(df_neutral)

    df_splitted = df_snps.groupby("iter")

    df_fv = Parallel(n_jobs=nthreads)(
        delayed(normalize_cut)(i, v, expected, stdev, center=center)
        for (i, v) in df_splitted
    )

    df_fv = pd.concat(df_fv)
    df_fv = pd.merge(df_fv, df_window)

    # params = params[:, [0, 1, 3, 4, ]]
    df_fv = pd.concat(
        [
            pd.DataFrame(
                # np.repeat(params, df_window.window.unique().size, axis=0),
                np.repeat(
                    params,
                    df_window.loc[:, ["center", "window"]].drop_duplicates().shape[0],
                    axis=0,
                ),
                columns=["s", "t", "t_end", "f_i", "f_t", "f_t_end"],
            ),
            df_fv,
        ],
        axis=1,
    )

    return df_fv.fillna(0)


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
    i,
    snps_values,
    expected,
    stdev,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
):
    binned_values = bin_values(snps_values)

    for stat in binned_values.columns[3:-1]:
        binned_values[stat] -= binned_values["freq_bins"].map(expected[stat])
        binned_values[stat] /= binned_values["freq_bins"].map(stdev[stat])

    binned_values = binned_values.drop(["daf", "freq_bins"], axis=1, inplace=False)

    out = []

    # cut window stats to only SNPs within the window around center
    centers = np.arange(center[0], center[1] + 1e4, 1e4)
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
    # out.insert(0, "window", windows)
    out.insert(0, "iter", i)
    return out


#################


def summary_statistics(sims, nthreads=1):
    """Summary

    Args:
        sims (TYPE): Description
        nthreads (TYPE): Description

    Returns:
        TYPE: Description
    """

    for k, s in sims.items():
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
            neutral = summaries(
                snps=summ_stats_snps,
                window=summ_stats_window,
                parameters=np.zeros(5),
            )
        else:
            params = np.row_stack(tuple(zip(*s))[-1])
            params[:, 0] = -np.log(params[:, 0])
            sweeps = summaries(
                snps=summ_stats_snps, window=summ_stats_window, parameters=params
            )

    K_neutral = neutral_hfs(sims["neutral"], 10, 110, 5, nthreads=nthreads)
    df_t_m = compute_t_m(
        sims["sweeps"], 10, 110, 5, K_neutral=K_neutral, nthreads=nthreads
    )

    df_fv = normalization(sweeps, neutral, nthreads)

    df_fv = pd.merge(df_fv, df_t_m, on=["iter", "window"])

    df_fv["model"] = "sweep"

    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_old_complete"
    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t < 0.9), "model"] = "hard_old_incomplete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_young_complete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t < 0.9), "model"] = "hard_young_incomplete"

    df_fv.loc[df_fv.f_i != df_fv.f_i.min(), "model"] = df_fv[
        df_fv.f_i != df_fv.f_i.min()
    ].model.str.replace("hard", "soft")

    df_fv_w = pd.pivot_table(
        df_fv,
        index=["iter", "s", "t", "t_end", "f_i", "f_t", "f_t_end", "model"],
        columns="window",
        values=df_fv[
            ~df_fv.isin(
                ["iter", "s", "t", "t_end", "f_i", "f_t", "f_t_end", "model", "window"]
            )
        ],
    )

    # df_fv_w.columns = [f"{col}_{window}" for col, window in df_fv_w.columns]
    df_fv_w.columns = [
        f"{col[0]}_{int(col[1])}_{int(col[2])}" for col in df_fv_w.columns
    ]
    df_fv_w.reset_index(inplace=True)

    return df_fv_windows


def summary_statistics_n(
    sims,
    nthreads=1,
    neutral="/labstorage/jmurgamoreno/flexabc/raw_data/sims/neutral.pickle",
    center=[5e5, 7e5],
):
    """Summary

    Args:
        sims (TYPE): Description
        nthreads (TYPE): Description

    Returns:
        TYPE: Description
    """

    with open(neutral, "rb") as handle:
        neutral = pickle.load(handle)

    pars = [(i[0], i[1]) for i in sims["sweeps"]]

    # Log the start of the scheduling
    logging.info("Scheduling {} {} simulations".format(len(pars), "sweeps"))

    # Use joblib to parallelize the execution
    summ_stats = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(calculate_stats)(ts, rec_map, index, is_neutral=False)
        for index, (ts, rec_map) in enumerate(pars)
    )

    # for index, (ts, rec_map) in enumerate(pars):
    #     if index == 20682:
    #         break
    #         print(index)
    #         calculate_stats(ts, rec_map, index, is_neutral=False)

    # Ensure params order
    summ_stats_snps, summ_stats_window = zip(*summ_stats)
    summ_stats_snps = pd.concat(summ_stats_snps).reset_index(drop=True)
    summ_stats_window = pd.concat(summ_stats_window).reset_index(drop=True)

    params = np.row_stack(tuple(zip(*sims["sweeps"]))[-1])
    params[:, 0] = -np.log(params[:, 0])
    sweeps = summaries(
        snps=summ_stats_snps, window=summ_stats_window, parameters=params
    )

    df_fv = normalization(sweeps, neutral, nthreads)

    # K_neutral = neutral_hfs(sims = hard["neutral"], K_truncation = 10, w_size = 110, step = 10, nthreads=nthreads)
    # K_neutral = np.array([0.19457523,0.14225372,0.11785444,0.10229021,0.09108094,0.0823794,0.07519522,0.0692076,0.06448256,0.06068068,])
    K_neutral = np.array([0.29818113, 0.21918679, 0.18227112, 0.15867943, 0.14168153])
    # K_neutral = np.array([0.23409616, 0.15726036, 0.12269969, 0.10131767, 0.08624637,0.07483728, 0.06581304, 0.0584341 , 0.05226489, 0.04703044])

    df_t_m = compute_t_m(
        sims=sims["sweeps"],
        K_truncation=5,
        w_size=110,
        step=10,
        K_neutral=K_neutral,
        nthreads=nthreads,
    )

    df_fv = pd.merge(df_fv, df_t_m, on=["iter", "window"])

    df_fv["model"] = "sweep"

    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_old_complete"
    df_fv.loc[(df_fv.t >= 2000) & (df_fv.f_t < 0.9), "model"] = "hard_old_incomplete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t >= 0.9), "model"] = "hard_young_complete"
    df_fv.loc[(df_fv.t < 2000) & (df_fv.f_t < 0.9), "model"] = "hard_young_incomplete"

    return df_fv


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
    hap_01, ac, biallelic_maks = filter_biallelics(hap)
    hap_int = hap_01.astype(np.int8)
    rec_map_01 = rec_map[biallelic_maks]
    position_masked = rec_map_01[:, 2]
    sequence_length = int(1.2e6)

    freqs = ac.to_frequencies()[:, 1]

    return (
        hap_01,
        ac,
        biallelic_maks,
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
    biallelic_maks = ac.is_biallelic_01()
    return (hap.subset(biallelic_maks), ac[biallelic_maks, :], biallelic_maks)


# def calculate_stats(ts, rec_map, i=0, center=6e5, window=500000, is_neutral=False):


def calculate_stats_nb(
    ts,
    rec_map,
    i=0,
    center=[5e5, 7e5],
    windows=[50000, 100000, 200000, 500000, 1000000],
    is_neutral=False,
):
    # Open and filtering data
    (
        hap_01,
        ac,
        biallelic_maks,
        hap_int,
        rec_map_01,
        position_masked,
        sequence_length,
        freqs,
    ) = open_tree(ts, rec_map)

    # iSAFE
    df_isafe = isafe_custom(hap_01, position_masked)

    # iHS and nSL
    ihs_v = ihs(
        hap_01,
        position_masked,
        min_maf=0.05,
        min_ehh=0.1,
        use_threads=False,
        include_edges=True,
    )

    try:
        ihs_s = standardize_by_allele_count(
            ihs_v, ac[:, 1], n_bins=50, diagnostics=False
        )[0]
    except:
        ihs_s = np.repeat(np.nan, ihs_v.size)

    df_ihs = pd.DataFrame(
        {
            "positions": position_masked,
            "daf": freqs,
            "ihs": np.abs(ihs_v),
        }
    ).dropna()

    nsl_v = nsl(hap_01.subset(freqs >= 0.05), use_threads=False)
    df_nsl = pd.DataFrame(
        {
            "positions": position_masked[freqs >= 0.05],
            "daf": freqs[freqs >= 0.05],
            "nsl": np.abs(nsl_v),
        }
    ).dropna()

    # Flex-sweep stats
    # df_dind = dind(hap_int, ac, rec_map_01)
    # df_high_freq = high_freq(hap_int, ac, rec_map_01)
    # df_low_freq = low_freq(hap_int, ac, rec_map_01)
    np_dind_high_low = dind_high_low_nb(hap_int, ac.values, rec_map_01)
    df_dind_high_low = pd.DataFrame(
        np_dind_high_low[:, [0, 1, 4, 5, 6]],
        columns=["positions", "daf", "dind", "high_freq", "low_freq"],
    )

    np_s_ratio = s_ratio_nb(hap_int, ac.values, rec_map_01)
    df_s_ratio = pd.DataFrame(
        np_s_ratio[:, [0, 1, 4]], columns=["positions", "daf", "s_ratio"]
    )

    np_hapdaf_o = hapdaf_o_nb(hap_int, ac.values, rec_map_01)
    df_hapdaf_o = pd.DataFrame(
        np_hapdaf_o[:, [0, 1, 4]], columns=["positions", "daf", "hapdaf_s"]
    )

    np_hapdaf_s = hapdaf_s_nb(hap_int, ac.values, rec_map_01)
    df_hapdaf_s = pd.DataFrame(
        np_hapdaf_s[:, [0, 1, 4]], columns=["positions", "daf", "hapdaf_s"]
    )

    # Merge stats
    df_summaries = reduce(
        pd_merger,
        [
            df_isafe,
            df_ihs,
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

    if is_neutral:
        df_window = []
        df_window = pd.DataFrame(
            df_window,
            columns=[
                "h1",
                "h12",
                "h2_h1",
                "k",
                "haf",
                "zns",
                "omega_max",
                "pi",
                "tajima_d",
                "faywu_h",
                "zeng_e",
            ],
        )
        df_window.insert(0, "window", np.array(windows))

    else:
        df_window = []

        centers = np.arange(center[0], center[1] + 1e4, 1e4)

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
                    zns,
                    pi_v,
                    d_v,
                    h_v,
                    e_v,
                ) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                h1_v, h12_v, h2_h1_v, h123_v, k, k_c = h12_custom(
                    hap_int, position_masked, start=lower, stop=upper
                )

                k_1, k_2, k_3, k_4, k_5 = k_c

                haf_v = haf_top(hap_int.astype(np.int64), position_masked, window=w)

                # LD stats
                # zns, omega_max = Ld(hap_int, position_masked, start=lower, stop=upper)
                zns, omega_max = (0, 0)
                # SFS stats
                S_mask = (position_masked >= lower) & (position_masked <= upper)
                pi_v = mean_pairwise_difference(ac[S_mask]).sum() / hap_01.shape[0]
                d_v = tajima_d(ac, position_masked, start=lower, stop=upper + 1)
                h_v = fay_wu_h_normalized(
                    hap_01, position_masked, start=lower, stop=upper
                )[-1]
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
                        zns,
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
                "k",
                "k_1",
                "k_2",
                "k_3",
                "k_4",
                "k_5",
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
        raise ValueError(
            (
                "The region Size is %i SNPs and %ikbp. When the region size is less than --MinRegionSize-ps (%i) SNPs or --MinRegionSize-bp (%ikbp), "
                "the region is too small for iSAFE analysis and better to use --SAFE flag to report "
                "the SAFE score of the entire region."
                % (
                    num_snps,
                    total_window_size / 1e3,
                    min_region_size_ps,
                    min_region_size_bp / 1e3,
                )
            )
        )
        obj_safe = isafe.SafeClass(snp_matrix.values.T)

        df_safe = obj_safe.create_dataframe().rename(
            columns={"safe": "SAFE", "freq": "daf"}
        )
        df_safe["positions"] = snp_matrix.index
        return df_safe.loc[:, ["positions", "daf", "SAFE"]]
    else:
        obj_isafe = isafe.iSafeClass(snp_matrix, window, step, topk, max_rank)
        obj_isafe.fire(status=False)
        df_isafe = (
            obj_isafe.isafe.loc[obj_isafe.isafe["freq"] < max_freq]
            .sort_values("ordinal_pos")
            .rename(columns={"id": "positions", "isafe": "isafe", "freq": "daf"})
        )
        df_isafe = df_isafe[df_isafe.daf < max_freq]
        return df_isafe.loc[:, ["positions", "daf", "isafe"]]


def haf_top(hap, pos, cutoff=0.1, window=500000):
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
    # haf_range = np.arange(600000 - (window / 2), 600000 + (window / 2), 100)[[0, -1]]

    freqs = hap.sum(axis=1) / hap.shape[1]
    hap_tmp = hap[(freqs > 0) & (freqs < 1)]
    # pos_tmp = pos[(freqs > 0) & (freqs < 1)]
    # hap_tmp = hap_tmp[(pos_tmp >= haf_range[0]) & (pos_tmp <= haf_range[1])]

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

    haf_num = (np.dot(h.T, h) / hap.shape[1]).sum(axis=1)
    haf_den = h.sum(axis=0)

    haf = np.sort(haf_num / haf_den)

    idx_low = int(cutoff * haf.size)
    idx_high = int((1 - cutoff) * haf.size)

    # 10% higher
    haf_top = haf[idx_high:].sum()

    return haf_top


@njit
def s_ratio_nb(
    hap,
    ac,
    rec_map,
    max_ancest_freq=1,
    min_tot_freq=0,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_nb(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    results = np.zeros((len(sq_freqs), 1))

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
        results[i] = hapdaf

    out = np.hstack((info, results))

    # df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "s_ratio"])

    return out


@njit
def hapdaf_o_nb(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.25,
    min_tot_freq=0.25,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_nb(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    results = np.zeros((len(sq_freqs), 1))

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
            results[i] = (f_d2 - f_a2).sum() / f_d2.shape[0]
        else:
            results[i] = np.nan

    out = np.hstack((info, results))
    # df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "hapdaf_o"])

    return out


@njit
def hapdaf_s_nb(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.1,
    min_tot_freq=0.1,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_nb(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )
    results = np.zeros((len(sq_freqs), 1))

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
            results[i] = (f_d2 - f_a2).sum() / f_d2.shape[0]
        else:
            results[i] = np.nan

    out = np.hstack((info, results))

    return out


@njit
def dind_high_low_nb(
    hap,
    ac,
    rec_map,
    max_ancest_freq=0.25,
    min_tot_freq=0,
    min_focal_freq=0.25,
    max_focal_freq=0.95,
    window_size=50000,
):
    sq_freqs, info = sq_freq_pairs_nb(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    # results_dind = []
    # results_high = []
    # results_low = []

    results_dind = np.zeros(len(sq_freqs))
    results_high = np.zeros(len(sq_freqs))
    results_low = np.zeros(len(sq_freqs))
    i = 0
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

        results_dind[i] = hap_dind
        results_high[i] = hap_high
        results_low[i] = hap_low

    # out = np.hstack(
    #     [
    #         info,results_dind,results_high,results_low
    #     ]
    # )
    results = np.vstack((results_dind, results_high, results_low)).T
    out = np.hstack((info, results))

    return out


@njit
def sq_freq_pairs_nb(hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size):
    # Compute counts and freqs once, the iter pairs combinations
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
    info = np.zeros((len(focal_index), 4))
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
                sq_nb(j, pars, rec_map, 0, window_size),
                sq_nb(j, pars, rec_map, freqs.size, window_size),
            )
        )

        # info.append(
        #     (rec_map[i, 2], freqs[i], focal_derived_count[j], focal_ancestral_count[j])
        # )
        info[j] = [
            rec_map[i, 2],
            freqs[i],
            focal_derived_count[j],
            focal_ancestral_count[j],
        ]
        sq_out.append(sq_freqs)

    return (sq_out, info)


@njit(cache=True)
def sq_nb(j, pars, rec_map, end, window_size):
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
    hap_cluster, k, k_c = cluster_similar_rows(hap_filter.T, np.ceil(S * 0.2))

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
    S = hap_filter.shape[0]
    zns = r2_matrix.sum() / math.comb(S, 2)
    # Index combination to iter
    # c_1, c_2 = np.triu_indices(r2_matrix.shape[0], 1)
    # omega_max = omega(r2_matrix)
    # omega_max = dps.omega(r2_matrix)[0]

    return zns, 0
    # return zns, omega_max


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


@njit("int64(int8[:],int8[:])", cache=True)
def hamming_distance(row1, row2):
    return np.count_nonzero(row1 != row2)


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
                if hamming_distance(hap[i], hap[j]) <= threshold:
                    cluster_indices[j] = i
                    out[j] = hap[i]

    k_c = np.sort(np.unique(cluster_indices, return_counts=True)[-1])[::-1]
    k = k_c.size
    if k < 5:
        k_c = np.concatenate([k_c, np.zeros((5 - k), dtype=int)])
    return out.T, k, k_c[:5]


@njit
def cluster_similar_rows_nb(hap, pos, start=None, stop=None, threshold=1.0):
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
                if hamming_distance(hap[i], hap[j]) <= threshold:
                    cluster_indices[j] = i
                    out[j] = hap[i]
    return out, cluster_indices


def get_empir_freqs_np(hap: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
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
        Kcount = np.concatenate(Kcount, np.zeros(K_truncation - Kcount.size))

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
        biallelic_maks,
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
        for index, (ts, rec_map) in enumerate(pars)
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
    sims, K_truncation, w_size, step, center=[5e5, 7e5], K_neutral=None, nthreads=1
):
    pars = [(i[0], i[1]) for i in sims]

    # Log the start of the scheduling
    logging.info("Estimating HFS")

    # Use joblib to parallelize the execution
    hfs_stats = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(LASSI_spectrum_and_Kspectrum)(ts, rec_map, K_truncation, w_size, step)
        for index, (ts, rec_map) in enumerate(pars)
    )

    K_counts, K_spectrum, windows = zip(*hfs_stats)

    if K_neutral is None:
        K_neutral = neut_average(np.vstack(K_spectrum))

    logging.info("Estimating T and m statistics")

    t_m = Parallel(n_jobs=nthreads, verbose=5)(
        delayed(T_m_statistic)(kc, K_neutral, windows[index], K_truncation, i=index)
        for index, (kc) in enumerate(K_counts)
    )
    t_m_cut = Parallel(n_jobs=nthreads, verbose=0)(
        delayed(cut_t_m_argmax)(t, center=center) for t in t_m
    )

    return pd.concat(t_m_cut)


def cut_t_m(
    df_t_m, windows=[10000, 25000, 50000, 100000, 200000, 500000, 1000000], center=6e5
):
    out = []
    for w in windows:
        # for w in [1000000]:
        lower = center - w / 2
        upper = center + w / 2

        df_t_m_subset = df_t_m[
            (df_t_m.iloc[:, 5] > lower) & (df_t_m.iloc[:, 5] < upper)
        ]
        try:
            max_t = df_t_m_subset.iloc[:, 0].argmax()
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
    df_t_m, windows=[50000, 100000, 200000, 500000, 1000000], center=[5e5, 7e5]
):
    out = []
    centers = np.arange(center[0], center[1] + 1e4, 1e4)
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
            df_t_m_subset = df_t_m_subset.iloc[max_t : max_t + 1, :]
            df_t_m_subset = df_t_m_subset.loc[
                :,
                ~df_t_m_subset.columns.isin(
                    ["iter", "frequency", "e", "model", "window_lassi"]
                ),
            ]
            df_t_m_subset.insert(0, "window", w)
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
