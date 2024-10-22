@njit
def sq_freq_pairs(hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size):
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
    for j in range(len(focal_index)):
        i = focal_index[j]

        # Calculate the size of the window
        size = window_size / 2

        # Find indices within the window
        z = np.flatnonzero(np.abs(rec_map[i, 2] - rec_map[:, 2]) <= size)

        # Determine indices for slicing the arrays
        x_r, y_r = (i + 1, z[-1])
        x_l, y_l = (z[0], i - 1)

        derived_l = hap_derived[x_l : (y_l + 1), :]
        derived_count_l = derived_count[x_l : (y_l + 1)]

        derived_r = hap_derived[x_r : (y_r + 1), :]
        derived_count_r = derived_count[x_r : (y_r + 1)]

        f_d_l = (focal_derived[j] & derived_l).sum(axis=1) / focal_derived_count[j]
        f_a_l = (focal_ancestral[j] & derived_l).sum(axis=1) / focal_ancestral_count[j]
        f_tot_l = freqs[x_l : y_l + 1]

        f_d_r = (focal_derived[j] & derived_r).sum(axis=1) / focal_derived_count[j]
        f_a_r = (focal_ancestral[j] & derived_r).sum(axis=1) / focal_ancestral_count[j]
        f_tot_r = freqs[x_r : y_r + 1]

        sq_freqs = np.concatenate(
            (
                np.vstack((f_d_l[::-1], f_a_l[::-1], f_tot_l[::-1])).T,
                np.vstack((f_d_r, f_a_r, f_tot_r)).T,
            )
        )

        sq_out.append(sq_freqs)

        info.append(
            (rec_map[i, 2], freqs[i], focal_derived_count[j], focal_ancestral_count[j])
        )

    return (sq_out, info)


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
    sq_freqs, info = sq_freq_pairs(
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

        s_ratio_v = num / den
        s_ratio_v_flip = den / num
        results.append((s_ratio_v, s_ratio_v_flip))

    try:
        # out = np.hstack([info, np.array(results).reshape(len(results), 1)])
        out = np.hstack([info, np.array(results)])
        df_out = pd.DataFrame(
            out[:, [0, 1, 4, 5]],
            columns=["positions", "daf", "s_ratio", "s_ratio_flip"],
        )
    except:
        df_out = pd.DataFrame(
            [], columns=["positions", "daf", "s_ratio", "s_ratio_flip"]
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
    sq_freqs, info = sq_freq_pairs(
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

        dind_v = num / den
        dind_v_flip = den / num

        results.append((dind_v, dind_v_flip))

    # out = np.hstack([info, np.array(results).reshape(len(results), 1)])
    out = np.hstack([info, np.array(results)])

    df_out = pd.DataFrame(
        out[:, [0, 1, 4, 5]], columns=["positions", "daf", "dind", "dind_flip"]
    )

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
    sq_freqs, info = sq_freq_pairs(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )

    results = []

    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]
        f_a = v[:, 1]

        f_diff = f_d[f_d > max_ancest_freq] ** 2
        f_diff_flip = f_a[f_a > max_ancest_freq] ** 2

        hf_v = f_diff.sum() / len(f_diff)
        hf_v_flip = f_diff_flip.sum() / len(f_diff_flip)
        results.append((hf_v, hf_v_flip))

    # out = np.hstack([info, np.array(results).reshape(len(results), 1)])
    out = np.hstack([info, np.array(results)])

    df_out = pd.DataFrame(
        out[:, [0, 1, 4, 5]],
        columns=["positions", "daf", "high_freq", "high_freq_flip"],
    )

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
    sq_freqs, info = sq_freq_pairs(
        hap, ac, rec_map, min_focal_freq, max_focal_freq, window_size
    )
    results = []

    for i, v in enumerate(sq_freqs):
        f_d = v[:, 0]
        f_a = v[:, 1]

        f_diff = (1 - f_d[f_d < max_ancest_freq]) ** 2
        f_diff_flip = (1 - f_a[f_a < max_ancest_freq]) ** 2

        lf_v = f_diff.sum() / len(f_diff)
        lf_v_flip = f_diff_flip.sum() / len(f_diff_flip)
        results.append((lf_v, lf_v_flip))

    # out = np.hstack([info, np.array(results).reshape(len(results), 1)])
    out = np.hstack([info, np.array(results)])

    df_out = pd.DataFrame(
        out[:, [0, 1, 4, 5]], columns=["positions", "daf", "low_freq", "low_freq_flip"]
    )

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
    sq_freqs, info = sq_freq_pairs(
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

        # Flipping derived to ancestral, ancestral to derived
        f_d2f = (
            f_a[(f_a > f_d) & (f_d <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )
        f_a2f = (
            f_d[(f_a > f_d) & (f_d <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )

        if len(f_d2) != 0 and len(f_a2) != 0:
            hapdaf = (f_d2 - f_a2).sum() / f_d2.shape[0]
        else:
            hapdaf = np.nan

        if len(f_d2f) != 0 and len(f_a2f) != 0:
            hapdaf_flip = (f_d2f - f_a2f).sum() / f_d2f.shape[0]
        else:
            hapdaf_flip = np.nan

        results.append((hapdaf, hapdaf_flip))

    try:
        out = np.hstack(
            [
                info,
                np.array(results),
                # np.array(results).reshape(len(results), 1),
            ]
        )
        df_out = pd.DataFrame(
            out[:, [0, 1, 4, 5]],
            columns=["positions", "daf", "hapdaf_o", "hapdaf_o_flip"],
        )
    except:
        df_out = pd.DataFrame(
            [], columns=["positions", "daf", "hapdaf_o", "hapdaf_o_flip"]
        )

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
    sq_freqs, info = sq_freq_pairs(
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

        # Flipping derived to ancestral, ancestral to derived
        f_d2f = (
            f_a[(f_a > f_d) & (f_d <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )
        f_a2f = (
            f_d[(f_a > f_d) & (f_d <= max_ancest_freq) & (f_tot >= min_tot_freq)] ** 2
        )

        if len(f_d2) != 0 and len(f_a2) != 0:
            hapdaf = (f_d2 - f_a2).sum() / f_d2.shape[0]
        else:
            hapdaf = np.nan

        if len(f_d2f) != 0 and len(f_a2f) != 0:
            hapdaf_flip = (f_d2f - f_a2f).sum() / f_d2f.shape[0]
        else:
            hapdaf_flip = np.nan

        results.append((hapdaf, hapdaf_flip))

    try:
        out = np.hstack(
            [
                info,
                np.array(results),
                # np.array(results).reshape(len(results), 1),
            ]
        )
        df_out = pd.DataFrame(
            out[:, [0, 1, 4, 5]],
            columns=["positions", "daf", "hapdaf_s", "hapdaf_s_flip"],
        )
    except:
        df_out = pd.DataFrame(
            [], columns=["positions", "daf", "hapdaf_s", "hapdaf_s_flip"]
        )

    return df_out


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
    sq_freqs, info = sq_freq_pairs(
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

        dind_v = num / den
        dind_v_flip = den / num

        if np.isinf(dind_v):
            dind_v = np.nan

        if np.isinf(dind_v_flip):
            dind_v_flip = np.nan

        hap_dind = (dind_v, dind_v_flip)
        #####
        f_diff = f_d[f_d > max_ancest_freq] ** 2
        f_diff_flip = f_a[f_a > max_ancest_freq] ** 2

        hf_v = f_diff.sum() / len(f_diff)
        hf_v_flip = f_diff_flip.sum() / len(f_diff_flip)

        hap_high = (hf_v, hf_v_flip)
        #####

        f_diff = (1 - f_d[f_d < max_ancest_freq]) ** 2
        f_diff_flip = (1 - f_a[f_a < max_ancest_freq]) ** 2

        lf_v = f_diff.sum() / len(f_diff)
        lf_v_flip = f_diff_flip.sum() / len(f_diff_flip)
        hap_low = (lf_v, lf_v_flip)
        #####
        results_dind.append(hap_dind)
        results_high.append(hap_high)
        results_low.append(hap_low)

    try:
        out = np.hstack(
            [
                info,
                np.array(results_dind),
                np.array(results_high),
                np.array(results_low),
            ]
        )
        df_out = pd.DataFrame(
            out[:, [0, 1, 4, 5, 6, 7, 8, 9]],
            columns=[
                "positions",
                "daf",
                "dind",
                "dind_flip",
                "high_freq",
                "high_freq_flip",
                "low_freq",
                "low_freq_flip",
            ],
        )
    except:
        df_out = pd.DataFrame(
            [],
            columns=[
                "positions",
                "daf",
                "dind",
                "dind_flip",
                "high_freq",
                "high_freq_flip",
                "low_freq",
                "low_freq_flip",
            ],
        )

    return df_out
