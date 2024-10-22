from numba import njit
import numpy as np
from typing import Tuple, List


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
    hap: np.ndarray, pos: np.ndarray, K_truncation: int, window: int, step: int
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
    K_count = []
    K_spectrum = []
    windows_centers = []
    S, n = hap.shape
    for i in np.arange(0, S, step):
        hap_subset = hap[i : i + window, :]

        # Calculate window center based on median SNP position
        windows_centers.append(np.median(pos[i : i + window]))

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
            total_exp = np.sum(np.exp(-headinds))
            theadd = (np.exp(-ival) / total_exp) * neutdiff_all
            altspect[ival - 1] += theadd

        altspect[m_val:] = tailclasses

        output = easy_likelihood(altspect, K_count, K_truncation)
    else:
        output = easy_likelihood(K_neutral, K_count, K_truncation)

    return output


def T_m_statistic(K_counts, K_neutral, windows, K_truncation):
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

    for i, w in enumerate(windows):
        # if(i==132):
        # break
        K_iter = K_counts[i]

        null_likelihood = easy_likelihood(K_neutral, K_iter, K_truncation)

        alt_likelihoods_by_e = []

        for e in epsilon_values:
            alt_likelihoods_by_m = []
            for m in range(1, m_vals):
                alt_like = sweep_likelihood2(
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
            [out_intermediate, np.array([K_neutral[-1], sweep_mode, w])]
        )

        output.append(out_intermediate)

    return np.array(output)


#############

# @njit
# def hap_to_ssx(hap):
#     tmp = hap.reshape(hap.shape[0], -1, 2)
#     out = np.zeros((tmp.shape[0], tmp.shape[1]), dtype=np.int32)

#     for i in range(tmp.shape[0]):
#         for j in range(tmp.shape[1]):
#             if tmp[i, j, 0] == 0 and tmp[i, j, 1] == 0:
#                 out[i, j] = 1
#             elif tmp[i, j, 0] == 0 and tmp[i, j, 1] == 1:
#                 out[i, j] = 2
#             elif tmp[i, j, 0] == 1 and tmp[i, j, 1] == 0:
#                 out[i, j] = 3
#             elif tmp[i, j, 0] == 1 and tmp[i, j, 1] == 1:
#                 out[i, j] = 4
#             else:
#                 out[i, j] = 0  # Default return or handle other cases as needed

#     return out


# @njit
# def sweep_likelihood(
#     K_neutral, K_count, K_truncation, m_val, epsilon, epsilon_max):
#     """
#     Computes the likelihood of a sweep under optimized parameters
#     """

#     if m_val != K_truncation:
#         altspect = []

#         tailclasses = []
#         neutdiff = []
#         tailinds = range(m_val + 1, K_truncation + 1)

#         for ti in tailinds:
#             try:
#                 the_ns = epsilon_max - (
#                     float(ti - m_val - 1) / float(K_truncation - m_val - 1)
#                 ) * (epsilon_max - epsilon)
#                 tailclasses.append(the_ns)
#                 neutdiff.append(K_neutral[ti - 1] - the_ns)
#             except:
#                 if float(ti - m_val - 1) == float(K_truncation - m_val - 1):
#                     tailclasses.append(epsilon)
#                     neutdiff.append(K_neutral[ti - 1] - epsilon)

#         headinds = range(1, m_val + 1)

#         for hd in headinds:
#             altspect.append(K_neutral[hd - 1])

#         neutdiff_all = sum(neutdiff)

#         for ival in headinds:
#             # Going for sweep model 3
#             total_exp = 0.0
#             for x in headinds:
#                 total_exp += np.exp(-x)
#             theadd = (np.exp(-ival) / total_exp) * neutdiff_all
#             altspect[ival - 1] += theadd

#         for tc in tailclasses:
#             altspect.append(tc)

#         output = easy_likelihood(np.array(altspect), K_count, K_truncation)
#     else:
#         output = easy_likelihood(K_neutral, K_count, K_truncation)

#     return output
