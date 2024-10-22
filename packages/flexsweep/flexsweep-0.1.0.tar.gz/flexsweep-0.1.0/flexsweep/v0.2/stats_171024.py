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


@njit("float64(int8[:], int8[:])", cache=True)
def r2(locus_A: np.ndarray, locus_B: np.ndarray) -> float:
    """
    Calculate r^2 and D between the two loci A and B.

    Args:locus_A (numpy.ndarray): 1D array representing alleles at locus A.
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


def get_duplicates(pos):
    unique_values, inverse_indices, counts = np.unique(
        pos, return_inverse=True, return_counts=True
    )

    duplicated_indices = np.where(counts[inverse_indices] > 1)[0]

    x = np.split(duplicated_indices, np.where(np.diff(duplicated_indices) != 1)[0] + 1)

    return x
