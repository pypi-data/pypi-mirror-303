from numba import njit
import numpy as np
import pandas as pd


@njit
def rank_with_duplicates(x):
    sorted_arr = sorted(x, reverse=True)
    rank_dict = {}
    rank = 1
    prev_value = -1

    for value in sorted_arr:
        if value != prev_value:
            rank_dict[value] = rank
        rank += 1
        prev_value = value

    return np.array([rank_dict[value] for value in x])


@njit
def dot_nb(hap):
    return np.dot(hap.T, hap)


@njit
def dot_two_nb(x, y):
    return np.dot(x, y)


@njit
def neutrality_divergence_proxy(kappa, phi, freq, method=3):
    if method == 1:
        sigma2 = (kappa) * (1 - kappa)
        sigma2[sigma2 == 0] = 1.0
        sigma = sigma2**0.5
        p = (phi - kappa) / sigma
    elif method == 2:
        sigma2 = (freq) * (1 - freq)
        sigma2[sigma2 == 0] = 1.0
        sigma = sigma2**0.5
        p = (phi - kappa) / sigma
    elif method == 3:
        p1 = neutrality_divergence_proxy(kappa, phi, freq, 1)
        nu = freq[np.argmax(p1)]
        p2 = neutrality_divergence_proxy(kappa, phi, freq, 2)
        p = p1 * (1 - nu) + p2 * nu
    return p


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
    return H, K


@njit
def safe(hap):
    num_snps, num_haplotypes = hap.shape

    haf = dot_nb(hap.astype(np.float64)).sum(1)
    H, K = calc_H_K(hap, haf)

    phi = 1.0 * H / haf.sum()
    kappa = 1.0 * K / (np.unique(haf).shape[0])
    freq = hap.sum(1) / num_haplotypes
    safe_values = neutrality_divergence_proxy(kappa, phi, freq)

    # rank = np.zeros(safe_values.size)
    rank = rank_with_duplicates(safe_values)
    # rank = pd.DataFrame(safe_values).rank(method='min', ascending=False).values.flatten()

    return haf, safe_values, rank, phi, kappa, freq


# @njit
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
    return windows_stats, windows_haf, pd.concat(snp_summary).reset_index(drop=True)


@njit
def create_rolling_indices_nb(total_variant_count, w_size, w_step):
    # assert total_variant_count < w_size or w_size > 0

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

    if (num_snps < min_region_size_ps) | (total_window_size < min_region_size_bp):
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
