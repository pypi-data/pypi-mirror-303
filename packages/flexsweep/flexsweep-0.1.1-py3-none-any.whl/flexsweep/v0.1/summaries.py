import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_MAX_THREADS"] = "1"

import numpy as np
import pandas as pd
from tskit import load
from isafe import isafe
from scipy import interpolate
from multiprocessing import Pool
import gzip
from functools import partial, reduce
import logging
from allel import HaplotypeArray, ihs, nsl, garud_h, standardize_by_allele_count
from copy import deepcopy
from collections import defaultdict, namedtuple
from sklearn.model_selection import train_test_split

pd_merger = partial(pd.merge, how="outer")

normalization = namedtuple("summaries", ["expected", "stdev"])

summaries = namedtuple("summaries", ["neutral", "sweeps"])


def pool_stats(sims, nthreads):
    pars = [(i[0], i[-1]) for i in sims]

    params = np.concatenate(tuple(zip(*sims))[1])

    # Log the start of the scheduling
    logging.info("Scheduling simulations")

    # Use joblib to parallelize the execution
    iter_stats = Parallel(n_jobs=nthreads, verbose=2)(
        delayed(calculate_stats)(ts, rec_map, index)
        for index, (ts, rec_map) in enumerate(pars)
    )

    # Ensure params order
    df_fv = pd.DataFrame.from_dict(dict(iter_stats), orient="index").sort_index()
    summ_stats = pd.concat([pd.DataFrame(params), df_fv], axis=1)

    num_nans = summ_stats.isnull().sum(axis=1) > 5

    return summ_stats[~num_nans].fillna(0)


def normalize_neutral(neutral_stats):
    # df_snps, df_window = neutral_stats
    # Get std and mean values from dataframe
    df_binned = bin_values(neutral_stats)

    # get expected value (mean) and standard deviation
    expected = df_binned.iloc[:, 2:].groupby("freq_bins").mean()
    stdev = df_binned.iloc[:, 2:].groupby("freq_bins").std()

    expected.index = expected.index.astype(str)
    stdev.index = stdev.index.astype(str)

    # df_window_binned = bin_values(df_window).dropna()
    # w_expected = df_window_binned.iloc[:, 1:].groupby("freq_bins").mean()
    # w_stdev = df_window.iloc[:, 1:].groupby("freq_bins").std()

    # w_expected.index = w_expected.index.astype(str)
    # w_stdev.index = w_stdev.index.astype(str)

    # expected = pd.concat([s_expected, w_expected], axis=1)
    # stdev = pd.concat([s_stdev, w_stdev], axis=1)

    return normalization(expected, stdev)


def bin_values(values, freq=0.02):
    # Create a deep copy of the input variable
    values_copy = deepcopy(values)

    # Modify the copy
    values_copy["freq_bins"] = pd.cut(
        x=values_copy["daf"],
        bins=np.arange(0, 1 + freq, freq),
        include_lowest=True,
        precision=2,
    )
    return values_copy


def cut(values, center, window):
    # cut window stats to only SNPs within the window around center
    lower = center - window / 2
    upper = center + window / 2
    cut_values = values[(values["positions"] >= lower) & (values["positions"] <= upper)]
    return cut_values


def normalize_sweeps(
    sweep_stats,
    neutral_normalization,
    center=(500000, 700000, 10000),
    windows=[50000, 100000, 200000, 500000, 1000000],
    nthreads=1,
):
    expected, stdev = neutral_normalization

    center_window = np.arange(center[0], center[1] + center[2], center[2])

    progress_bar = tqdm(total=len(sweep_stats.values()))
    with concurrent.futures.ProcessPoolExecutor(max_workers=nthreads) as executor:
        # Start the load operations and mark each future with its input value
        future_to_result = {
            executor.submit(
                norm_center_window, value, expected, stdev, center_window, windows
            ): i
            for i, (value) in enumerate(sweep_stats.values())
        }

        iter_stats = {}
        # errors = []
        for completed in concurrent.futures.as_completed(future_to_result):
            # iterate over the completed futures
            iter_sim = future_to_result[completed]
            # Get the result of the completed future, or raise a TimeoutError if it timed out
            # summ_stats[iter_sim] = completed.result(timeout=None)
            iter_stats[iter_sim] = completed.result(timeout=None)

            progress_bar.update()

    progress_bar.refresh()
    progress_bar.close()

    return iter_stats


def norm_center_window(sweep_stat, expected, stdev, center_window, windows):
    """
    doing all nan values instead of drop. need to solve eventually
    """

    norm_values = {c: {w: {} for w in windows} for c in center_window}

    tmp = sweep_stat[600000].drop(["isafe", "nsl", "ihs", "haf", "h12"], axis=1)
    haf_h12 = sweep_stat[600000][["haf", "h12"]].dropna()

    for c, w in product(center_window, windows):
        merged = pd.merge(sweep_stat[c], tmp, how="outer")
        binned_values = bin_values(merged)

        # now normalize using those bins values
        binned_values.index = binned_values["freq_bins"]
        binned_values["freq_bins"] = binned_values["freq_bins"].astype(str)

        # repeat the original data n times
        repeated_data = np.repeat(
            binned_values["freq_bins"].values[:, np.newaxis],
            binned_values.columns.size - 1,
            axis=1,
        )

        # create the DataFrame using the repeated data
        repeated_data = pd.DataFrame(repeated_data, columns=binned_values.columns[0:-1])
        repeated_data.index = binned_values.index

        for stat in repeated_data.columns[2:]:
            expected_col = repeated_data[stat].map(expected[stat])
            stdev_col = repeated_data[stat].map(stdev[stat])

            # Not normalizing haf nor h12
            if stat not in ["haf", "h12"]:
                binned_values[stat] = (binned_values[stat] - expected_col) / stdev_col

        cut_binned_values = cut(binned_values, c, w).iloc[:, :-1]
        cut_binned_values[["haf", "h12"]] = np.nan

        if not cut_binned_values.empty:
            cut_binned_values.iloc[-1, -2:] = haf_h12

        norm_values[c][w] = cut_binned_values

    return norm_values


def make_fv(
    sims,
    summ_stats,
    center=(500000, 700000, 10000),
    windows=[50000, 100000, 200000, 500000, 1000000],
    stats=[
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
    ],
    nthreads=1,
):
    neutral_normalization = normalize_neutral(summ_stats.neutral)
    sweeps_normalization = normalize_sweeps(
        summ_stats.sweeps, neutral_normalization, nthreads=nthreads
    )

    out = {}

    center_window = np.arange(center[0], center[1] + center[2], center[2])

    index_order = [
        i[0] + "_w" + str(i[2]) + "_c" + str(i[1])
        for i in product(stats, center_window, windows)
    ]

    for i, v in sweeps_normalization.items():
        out_inner = []
        for c, w in product(center_window, windows):
            tmp = (
                v[c][w]
                .iloc[:, 2:]
                .mean()
                .loc[
                    [
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
                ]
            )
            tmp.index = tmp.index + "_w" + str(w) + "_c" + str(c)
            out_inner.append(tmp)
        out[i] = pd.concat(out_inner).reindex(index_order).values

    df_fv = pd.DataFrame.from_dict(out, orient="index")

    # Unpack simulated parameters
    params = pd.DataFrame(list(zip(*sims.sweeps))[-1])
    df_fv = pd.concat([params, df_fv], axis=1)

    num_nans = df_fv.isnull().sum(axis=1) > 115
    df_fv.columns = ["s", "tau", "f_i", "f_t"] + index_order

    return df_fv.loc[~num_nans, :]


def decimal(x):
    y = "{:.12f}".format(x)
    return y


def make_fv_s(
    sims,
    summ_stats,
    center=(500000, 700000, 10000),
    windows=[50000, 100000, 200000, 500000, 1000000],
    stats=[
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
    ],
    nthreads=1,
):
    neutral_normalization = normalize_neutral(summ_stats.neutral)

    return df_fv.loc[~num_nans, :]


# numNans = fullFeatureFile.isnull().sum(axis=1)
# numDropFV = sum(numNans > 115)
# fullFeatureFile.drop(fullFeatureFile[numNans > 115].index, inplace=True) # dump fvs with more than 10% nans
# print(f"Removing {numDropFV} feature vectors because more than 10% of statistics are nan")
# fullFeatureFile=fullFeatureFile.fillna(0) # replace remaining nans with 0s

# x_2 = pd.concat([x_1.iloc[:,:4] , x_1.iloc[:,(x_1.columns.str.contains("c600000")) & (x_1.columns.str.contains("w1000000"))]],axis=1)

# train, test = train_test_split(x_2, test_size=0.01)

# train.to_csv("/home/jmurgamoreno/prior.txt",sep='\t',index=False)
# test.iloc[:,:4].to_csv("/home/jmurgamoreno/data.txt",sep='\t',index=False)


########################


def filter_biallelics(hap):
    ac = hap.count_alleles()
    biallelic_maks = ac.is_biallelic_01()
    return (hap.subset(biallelic_maks), ac[biallelic_maks, :], biallelic_maks)


def frequency(freqs, positions, adaptive):
    adaptative_index = positions == adaptive

    if np.any(adaptative_index):
        f = freqs[adaptative_index][0]
    else:
        f = 1
    return f


def write_hap(ts, output_file, recombination_hapmap=None, sep=""):
    hap_01, ac, biallelic_maks = filter_biallelics(HaplotypeArray(ts.genotype_matrix()))

    # Save the array to the file
    np.savetxt(output_file + ".hap", hap_01, fmt="%d", delimiter=sep, newline="\n")

    # Compress the file using gzip through a subprocess
    subprocess.run(["gzip", "-f", output_file + ".hap"])

    if recombination_hapmap is not None:
        pd.DataFrame(recombination_hapmap[biallelic_maks, :]).to_csv(
            output_file + ".map.gz", index=False, header=False, sep=" "
        )


def write_discoal(ts, recombination_hapmap, output_file):
    hap_01, ac, biallelic_maks = filter_biallelics(HaplotypeArray(ts.genotype_matrix()))

    with open(output_file, "w") as f:
        f.write("/discoal/discoal 50 1 1200000\n\n")
        f.write("//\n")
        f.write("segsites: " + str(hap_01.shape[0]) + "\n")
        f.write(
            "positions: "
            + " ".join(
                ["{:.6f}".format(i) for i in recombination_hapmap[:, 2] / 1200000]
            )
            + "\n"
        )
        for i in hap_01.T:
            f.write("".join(i.astype(str)) + "\n")


def read_hap(hap_file, map_file):
    hap = np.vstack(
        [
            np.array(list((map(int, i[0]))))
            for i in pd.read_csv(hap_file, header=None).values
        ]
    )

    rec_map = pd.read_csv(map_file, sep=" ", header=None).values

    return hap, rec_map


def summary_statistics(sims, nthreads):
    """Summary

    Args:
        sims (TYPE): Description
        nthreads (TYPE): Description

    Returns:
        TYPE: Description
    """
    # neutral_stats = pool_stats(
    #     calculate_region_stats, sims.neutral, nthreads, "neutral"
    # )

    sweep_stats = pool_stats(calculate_windows_stats, sims.sweeps, nthreads, "sweeps")

    return summaries(neutral=neutral_stats, sweeps=sweep_stats)


# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(message)s")


def pool_stats(f, sims_class, nthreads, sim_type):
    pars = [(i[0], i[1]) for i in sims_class]

    # Log the start of the scheduling
    logging.info("Scheduling {} simulations".format(sim_type))

    # progress_bar = tqdm(desc='Simulating {0} {1} {2} {3} sweeps into {4} threads'.format(len(pars),params.sweep_class,params.sweep_timing,params.sweep_status,nthreads),total=len(pars))

    iter_stats = defaultdict.fromkeys(range(len(pars)))

    progress_bar = tqdm(total=len(pars))
    with concurrent.futures.ProcessPoolExecutor(max_workers=nthreads) as executor:
        # Start the load operations and mark each future with its input value
        future_to_result = {
            executor.submit(f, ts, rec_map): i for i, (ts, rec_map) in enumerate(pars)
        }

        # errors = []
        for completed in concurrent.futures.as_completed(future_to_result):
            # iterate over the completed futures
            iter_sim = future_to_result[completed]
            # Get the result of the completed future, or raise a TimeoutError if it timed out
            # summ_stats[iter_sim] = completed.result(timeout=None)
            iter_stats[iter_sim] = completed.result(timeout=None)
            # summ_stats.append(completed.result(timeout=None))

            progress_bar.update()

    progress_bar.refresh()
    progress_bar.close()

    if f.__name__ == "calculate_region_stats":
        # Join summaries from simulations into a DF
        summ_stats = pd.concat(
            iter_stats.values(), keys=iter_stats.keys(), names=["simulation", "index"]
        )

        # df_snps, df_window = zip(*iter_stats.values())

        # df_snps = pd.concat(
        #     df_snps, keys=iter_stats.keys(), names=["simulation", "index"]
        # )
        # df_window = pd.concat(
        #     df_window, keys=iter_stats.keys(), names=["simulation", "index"]
        # )
        # summ_stats = summaries(snps=df_snps, window=df_window)
    else:
        summ_stats = iter_stats
    return summ_stats


def calculate_windows_stats(ts, rec_map, center=(500000, 700000, 10000), window=500000):
    # Open and filtering data
    try:
        hap = HaplotypeArray(ts.genotype_matrix())
    except:
        try:
            hap = HaplotypeArray(ts)
        except:
            hap = HaplotypeArray(load(ts).genotype_matrix())

    positions = rec_map[:, 2]
    physical_position = rec_map[:, 2]

    # Estimate summary by windows
    center_window = np.arange(center[0], center[1] + center[2], center[2])

    stat_center = {}
    for i in center_window:
        haf_h12_row = np.concatenate([np.array([i, 1]), np.repeat(np.nan, 11)])

        min_position = int(i - 1e6 / 2)
        max_position = int(i + 1e6 / 2)

        positions_mask = (positions >= min_position) & (positions <= max_position)
        positions_window = positions[positions_mask]

        hap_window = hap.subset(positions_mask)
        rec_map_window = rec_map[positions_mask, :]
        hap_window_01, ac, biallelic_maks = filter_biallelics(hap_window)
        positions_window_01 = positions_window[biallelic_maks]
        rec_map_01 = rec_map_window[biallelic_maks]
        sequence_length = max_position - min_position

        freqs = ac.to_frequencies()[:, 1]
        f_t_simulated = frequency(freqs, positions_window_01, 6e5)

        # iSAFE
        df_isafe = isafe_custom(hap_window_01.astype(np.int64), positions_window_01)
        # print((i, hap_window_01.shape, df_isafe.shape))

        # iHS and nSL
        ihs_v = ihs(
            hap_window_01,
            positions_window_01,
            min_maf=0.05,
            min_ehh=0.1,
            use_threads=False,
        )

        try:
            ihs_s = standardize_by_allele_count(
                ihs_v, ac[:, 1], n_bins=50, diagnostics=False
            )[0]
        except:
            ihs_s = np.repeat(np.nan, ihs_v.size)

        df_ihs = (
            pd.DataFrame({"positions": positions_window_01, "daf": freqs, "ihs": ihs_s})
            .dropna()
            .abs()
        )

        nsl_v = nsl(hap_window_01.subset(freqs >= 0.05), use_threads=False)
        df_nsl = (
            pd.DataFrame(
                {
                    "positions": positions_window_01[freqs >= 0.05],
                    "daf": freqs[freqs >= 0.05],
                    "nsl": nsl_v,
                }
            )
            .dropna()
            .abs()
        )

        df_summaries = reduce(pd_merger, [df_isafe, df_ihs, df_nsl])
        df_summaries.sort_values("positions", inplace=True)

        # Check true center to analyze whole chromosome on the other stats. i == (center[1] + window)
        if i == 6e5:
            # HAP matrix centered to analyse whole chromosome
            hap_01, ac, biallelic_maks = filter_biallelics(hap)
            hap_int = hap_01.astype(np.int8)
            rec_map_01 = rec_map[biallelic_maks]
            position_masked = rec_map_01[:, 2]
            sequence_length = int(1.2e6)
            # sequence_length            = ts.sequence_length

            # H12 and HAF
            h12_v = garud_h(hap_01.subset((freqs >= 0.05) & (freqs <= 1)))[1]
            haf_v = haf_top(hap_01, position_masked)

            # Flex-sweep stats
            df_dind = dind(hap_int, ac, rec_map_01)
            df_high_freq = high_freq(hap_int, ac, rec_map_01)
            df_low_freq = low_freq(hap_int, ac, rec_map_01)
            df_s_ratio = s_ratio(hap_int, ac, rec_map_01)
            df_hapdaf_o = hapdaf_o(hap_int, ac, rec_map_01)
            df_hapdaf_s = hapdaf_s(hap_int, ac, rec_map_01)

            # Merge and overwrite stats
            df_summaries = reduce(
                pd_merger,
                [
                    df_summaries,
                    df_dind,
                    df_high_freq,
                    df_low_freq,
                    df_s_ratio,
                    df_hapdaf_o,
                    df_hapdaf_s,
                ],
            )

            # Add haf and h12 to sweep dataframe
            df_summaries[["haf", "h12"]] = np.nan
            if 6e5 in df_summaries.positions.values:
                df_summaries.loc[df_summaries.positions == 6e5, ["haf", "h12"]] = (
                    haf_v,
                    h12_v,
                )
            else:
                haf_h12_row[-2:] = haf_v, h12_v
                df_summaries = pd.concat(
                    [
                        df_summaries,
                        pd.DataFrame(haf_h12_row, index=df_summaries.columns).T,
                    ]
                ).reset_index(drop=True)

            df_summaries.sort_values("positions", inplace=True)

        stat_center[i] = df_summaries

    return stat_center


def calculate_region_stats(ts, rec_map, window=500000):
    # Open and filtering data
    try:
        hap = HaplotypeArray(ts.genotype_matrix())
    except:
        try:
            hap = HaplotypeArray(ts)
        except:
            hap = HaplotypeArray(load(ts).genotype_matrix())

    haf_h12_row = np.concatenate([np.array([6e5, 1]), np.repeat(np.nan, 11)])

    # hap                        = HaplotypeArray(ts)
    positions = rec_map[:, 2]
    physical_position = rec_map[:, 2]

    # HAP matrix centered to analyse whole chromosome
    hap_01, ac, biallelic_maks = filter_biallelics(hap)
    hap_int = hap_01.astype(np.int8)
    rec_map_01 = rec_map[biallelic_maks]
    position_masked = rec_map_01[:, 2]
    sequence_length = int(1.2e6)

    freqs = ac.to_frequencies()[:, 1]

    # iSAFE
    df_isafe = isafe_custom(hap_01, position_masked)

    # iHS and nSL
    ihs_v = ihs(
        hap_01,
        position_masked,
        min_maf=0.05,
        min_ehh=0.1,
        use_threads=False,
        include_edges=False,
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
            "ihs": ihs_s,
        }
    ).dropna()

    nsl_v = nsl(hap_01.subset(freqs >= 0.05), use_threads=False)
    df_nsl = pd.DataFrame(
        {
            "positions": position_masked[freqs >= 0.05],
            "daf": freqs[freqs >= 0.05],
            "nsl": nsl_v,
        }
    ).dropna()

    # H12 and HAF
    # h12_v = garud_h(hap_01.subset((freqs >= 0.05) & (freqs <= 1)))[1]
    h12_v = h12_custom(hap_01, position_masked)
    haf_v = haf_top(hap_01, position_masked)

    # Flex-sweep stats
    df_dind = dind(hap_int, ac, rec_map_01)
    df_high_freq = high_freq(hap_int, ac, rec_map_01)
    df_low_freq = low_freq(hap_int, ac, rec_map_01)
    df_s_ratio = s_ratio(hap_int, ac, rec_map_01)
    df_hapdaf_o = hapdaf_o(hap_int, ac, rec_map_01)
    df_hapdaf_s = hapdaf_s(hap_int, ac, rec_map_01)

    # Merge stats
    df_summaries = reduce(
        pd_merger,
        [
            df_isafe,
            df_ihs,
            df_nsl,
            df_dind,
            df_high_freq,
            df_low_freq,
            df_s_ratio,
            df_hapdaf_o,
            df_hapdaf_s,
        ],
    )

    # Add haf and h12 to sweep dataframe
    df_summaries[["haf", "h12"]] = np.nan

    if 6e5 in df_summaries.positions:
        df_summaries.loc[df_summaries.positions == 6e5, ["haf", "h12"]] = haf_v, h12_v
    else:
        haf_h12_row[-2:] = haf_v, h12_v
        df_summaries = pd.concat(
            [
                df_summaries,
                pd.DataFrame(haf_h12_row, index=df_summaries.columns).T,
            ]
        ).reset_index(drop=True)

    return df_summaries.sort_values(by="positions").reset_index(drop=True)


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
    out = np.hstack([info, np.array(results).reshape(len(results), 1)])

    df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "s_ratio"])

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

    out = np.hstack(
        [np.delete(info, nan_index, axis=0), np.array(results).reshape(len(results), 1)]
    )

    df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "hapdaf_o"])

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

    out = np.hstack(
        [np.delete(info, nan_index, axis=0), np.array(results).reshape(len(results), 1)]
    )

    df_out = pd.DataFrame(out[:, [0, 1, 4]], columns=["positions", "daf", "hapdaf_s"])

    return df_out


def sq_freq_pairs_np(hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size):
    # Compute counts and freqs once, the iter pairs combinations
    hap_derived = hap
    hap_ancestral = np.bitwise_xor(hap_derived, 1)

    derived_count = ac[:, 1]
    ancestral_count = ac[:, 0]
    freqs = ac.to_frequencies()[:, 1]
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

    size = window_size / 2

    z = np.flatnonzero(np.abs(rec_map[i, 2] - rec_map[:, 2]) <= size)

    if i < end:
        x, y = (i + 1, z[-1])
    else:
        x, y = (z[0], i - 1)

    derived = hap_derived[x : (y + 1), :]
    derived_count = hap_count[x : (y + 1)]
    f_d = (focal_derived[j] & derived).sum(axis=1) / focal_derived_count[j]
    f_a = (focal_ancestral[j] & derived).sum(axis=1) / focal_ancestral_count[j]
    f_tot = hap_freqs[x : y + 1]

    if end == 0:
        f_d = f_d[::-1]
        f_a = f_a[::-1]
        f_tot = f_tot[::-1]

    return np.array((f_d, f_a, f_tot)).T


def get_duplicates(pos):
    unique_values, inverse_indices, counts = np.unique(
        pos, return_inverse=True, return_counts=True
    )

    duplicated_indices = np.where(counts[inverse_indices] > 1)[0]

    x = np.split(duplicated_indices, np.where(np.diff(duplicated_indices) != 1)[0] + 1)

    return x


def h12_custom(hap, pos, min_freq=0.05, max_freq=1, window=500000):
    haf_range = np.arange(600000 - (window / 2), 600000 + (window / 2) + 200, 200)

    freqs = hap.sum(axis=1) / hap.shape[1]

    hap_filter = hap[(freqs >= min_freq) & (freqs <= max_freq)]
    pos_filter = pos[(freqs >= min_freq) & (freqs <= max_freq)]

    x = (pos_filter / 100).astype(int) * 100
    y = np.unique(x[(x >= haf_range[0]) & (x <= haf_range[-1])])

    h = hap_filter[np.where(np.isin(x, y))[0], :]

    return garud_h(h)[1]
