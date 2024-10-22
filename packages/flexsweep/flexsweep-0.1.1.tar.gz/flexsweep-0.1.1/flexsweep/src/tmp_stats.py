#################


# def cluster_increasing(hap, pos, threshold, center=6e5):
#     hap_c = deepcopy(hap)
#     for w in [25000, 50000, 100000, 250000, 500000]:
#         out, k_c = cluster_similar_rows(hap_c, pos, start=center - w, stop=center + w)
#         hap_c[(pos >= start) & (pos <= stop), :] = out

#     print(np.unique(hap_c, axis=1).shape)

#     return hap_c

# @njit("float64(int64,float64[:,:],int64[:],int64[:])", cache=True)
# def omega_at_snp(l, r2_matrix, c_1, c_2):
#     o_sum = 0.0
#     o_sum_l = 0.0
#     o_sum_r = 0.0
#     l_count = 0.0
#     r_count = 0.0
#     cross_count = 0.0

#     for idx in range(len(c_1)):
#         i = c_1[idx]
#         j = c_2[idx]
#         r2_val = r2_matrix[i, j]
#         if r2_val >= 0.0:
#             if i < l and j >= l:
#                 o_sum += r2_val
#                 cross_count += 1
#             elif i < l and j < l:
#                 o_sum_l += r2_val
#                 l_count += 1
#             elif i >= l and j >= l:
#                 o_sum_r += r2_val
#                 r_count += 1

#     denom = o_sum * (1.0 / cross_count) if cross_count > 0 else 1.0
#     numer = (
#         (o_sum_l + o_sum_r) / (l_count + r_count) if (l_count + r_count) > 0 else 1.0
#     )

#     return numer / denom


# @njit("float64(float64[:,:],int64[:],int64[:])", cache=True)
# def omega(r2_matrix: np.ndarray) -> float:
#     """
#     Calculates Kim and Nielsen's (2004, Genetics 167:1513) omega_max statistic

#     Args:
#         r2_matrix (numpy.ndarray): 2D array representing r2 values.

#     Returns:
#         float: Kim and Nielsen's omega max.
#     """
#     num_sites = r2_matrix.shape[0]
#     omega_max = 0.0

#     if num_sites < 3:
#         omega_max = 0.0
#     else:
#         c_1, c_2 = np.triu_indices(num_sites, 1)
#         out = np.zeros(num_sites)
#         for l in range(3, num_sites - 2):
#             out[l] = omega_at_snp(l, r2_matrix, c_1, c_2)
#         omega_max = out.max()
#     return omega_max

# @njit("float64(int64,float64[:,:])", cache=True)
# def omega_at_snp(l, r2_matrix):
#     o_sum = 0.0
#     o_sum_l = 0.0
#     o_sum_r = 0.0
#     l_count = 0.0
#     r_count = 0.0
#     cross_count = 0.0
#     num_sites = r2_matrix.shape[0]

#     c_1, c_2 = np.triu_indices(num_sites, 1)

#     for i, j in zip(c_1, c_2):
#         if r2_matrix[i, j] >= 0.0:
#             r2_val = r2_matrix[i, j]
#             if i < l and j >= l:
#                 o_sum += r2_val
#                 cross_count += 1
#             elif i < l and j < l:
#                 o_sum_l += r2_val
#                 l_count += 1
#             elif i >= l and j >= l:
#                 o_sum_r += r2_val
#                 r_count += 1
#     denom = o_sum * (1.0 / cross_count)
#     numer = 1.0 / (l_count + r_count)
#     numer *= o_sum_l + o_sum_r
#     return numer / denom


# @njit("float64(float64[:,:])", cache=True)
# def omega(r2_matrix: np.ndarray) -> float:
#     """
#     Calculates Kim and Nielsen's (2004, Genetics 167:1513) omega_max statistic

#     Args:
#         r2_matrix (numpy.ndarray): 2D array representing r2 values.

#     Returns:
#         float: Kim and Nielsen's omega max.
#     """
#     num_sites = r2_matrix.shape[0]
#     omega_max = 0.0
#     if num_sites < 3:
#         omega_max = 0.0
#     else:
#         for l in range(3, num_sites - 2):
#             tmp = omega_at_snp(l, r2_matrix)
#             if tmp > omega_max:
#                 omega_max = tmp
#     return omega_max


# def normalize_neutral(neutral_stats):
#     # df_snps, df_window = neutral_stats

#     window_stats = [
#         "daf"
#         "h1",
#         "h12",
#         "h2_h1",
#         "k",
#         "haf",
#         "zns",
#         "pi",
#         "tajima_d",
#         "faywu_h",
#         "zeng_e",
#     ]

#     # Get std and mean values from dataframe
#     df_binned = bin_values(
#         neutral_stats.loc[:, ~neutral_stats.columns.isin(window_stats)]
#     )

#     # get expected value (mean) and standard deviation
#     expected = df_binned.iloc[:, 3:].groupby("freq_bins").mean()
#     stdev = df_binned.iloc[:, 3:].groupby("freq_bins").std()

#     expected.index = expected.index.astype(str)
#     stdev.index = stdev.index.astype(str)

#     return expected, stdev

# def bin_values(values, freq=0.02):
#     # Create a deep copy of the input variable
#     values_copy = values.copy()

#     # Modify the copy
#     values["freq_bins"] = pd.cut(
#         x=values["daf"],
#         bins=np.arange(0, 1 + freq, freq),
#         include_lowest=True,
#         precision=2,
#     ).astype(str)

#     return values

# def normalize_sweeps(sweeps, neutral):
#     df_snps, df_window, params = deepcopy(sweeps)
#     expected, stdev = deepcopy(neutral)

#     binned_values = bin_values(df_snps)

#     for stat in binned_values.columns[3:-1]:
#         binned_values[stat] = (
#             binned_values[stat] - binned_values["freq_bins"].map(expected[stat])
#         ) / binned_values["freq_bins"].map(stdev[stat])

#     df_fv = (
#         binned_values[binned_values.iter < 10].drop(["daf", "freq_bins"], axis=1, inplace=False)
#         .groupby("iter")
#         .apply(cut)
#         .reset_index(level=0)
#     )

#     df_fv = pd.merge(df_fv, df_window, how="outer")

#     params = params[:, [0, 1, 3, 4]]
#     df_fv = pd.concat(
#         [
#             pd.DataFrame(
#                 np.repeat(params, 5, axis=0), columns=["s", "t", "f_i", "f_t"]
#             ),
#             df_fv,
#         ],
#         axis=1,
#     )

#     return df_fv.fillna(0)

# def cut(vl,center=6e5, windows=[50000, 100000, 200000, 500000, 1000000]):

#     out = []
#     # cut window stats to only SNPs within the window around center
#     for w in windows:
#         # for w in [1000000]:
#         lower = center - w / 2
#         upper = center + w / 2
#         cut_values = (
#             vl[(vl["positions"] >= lower) & (vl["positions"] <= upper)]
#             .iloc[:, 2:]
#             .abs()
#             .mean()
#         )

#         # cut_values.index = cut_values.index + "_w" + str(w)
#         out.append(cut_values)

#     out = pd.concat(out, axis=1).T
#     out.insert(0, "window", windows)

#     return out

# def calculate_stats_nowindows(ts, rec_map, i=0, center=6e5, window=500000):
#     # Open and filtering data
#     try:
#         hap = HaplotypeArray(ts.genotype_matrix())
#     except:
#         try:
#             hap = HaplotypeArray(ts)
#         except:
#             hap = HaplotypeArray(load(ts).genotype_matrix())

#     positions = rec_map[:, 2]
#     physical_position = rec_map[:, 2]

#     # HAP matrix centered to analyse whole chromosome
#     hap_01, ac, biallelic_maks = filter_biallelics(hap)
#     hap_int = hap_01.astype(np.int8)
#     rec_map_01 = rec_map[biallelic_maks]
#     position_masked = rec_map_01[:, 2]
#     sequence_length = int(1.2e6)

#     freqs = ac.to_frequencies()[:, 1]

#     # iSAFE
#     df_isafe = isafe_custom(hap_01, position_masked)

#     # iHS and nSL
#     ihs_v = ihs(
#         hap_01,
#         position_masked,
#         min_maf=0.05,
#         min_ehh=0.1,
#         use_threads=False,
#         include_edges=True,
#     )

#     try:
#         ihs_s = standardize_by_allele_count(
#             ihs_v, ac[:, 1], n_bins=50, diagnostics=False
#         )[0]
#     except:
#         ihs_s = np.repeat(np.nan, ihs_v.size)

#     df_ihs = pd.DataFrame(
#         {
#             "positions": position_masked,
#             "daf": freqs,
#             "ihs": np.abs(ihs_v),
#         }
#     ).dropna()

#     nsl_v = nsl(hap_01.subset(freqs >= 0.05), use_threads=False)
#     df_nsl = pd.DataFrame(
#         {
#             "positions": position_masked[freqs >= 0.05],
#             "daf": freqs[freqs >= 0.05],
#             "nsl": np.abs(nsl_v),
#         }
#     ).dropna()

#     # Flex-sweep stats
#     df_dind = dind(hap_int, ac, rec_map_01)
#     df_high_freq = high_freq(hap_int, ac, rec_map_01)
#     df_low_freq = low_freq(hap_int, ac, rec_map_01)
#     df_s_ratio = s_ratio(hap_int, ac, rec_map_01)
#     df_hapdaf_o = hapdaf_o(hap_int, ac, rec_map_01)
#     df_hapdaf_s = hapdaf_s(hap_int, ac, rec_map_01)

#     # Merge stats
#     df_summaries = reduce(
#         pd_merger,
#         [
#             df_isafe,
#             df_ihs,
#             df_nsl,
#             df_dind,
#             df_high_freq,
#             df_low_freq,
#             df_s_ratio,
#             df_hapdaf_o,
#             df_hapdaf_s,
#         ],
#     )

#     df_summaries = df_summaries.sort_values(by="positions").reset_index(drop=True)

#     # H12 and HAF
#     df_window = []

#     w = 5e5
#     # H12, HAF
#     h1_v, h12_v, h2_h1_v, h123_v, k = h12_snps(hap_int, position_masked)

#     haf_v = haf_top(hap_int.astype(np.int64), position_masked)

#     # LD stats
#     # zns, omega_max = Ld(hap_int, position_masked, start=center - w, stop=center + w)
#     zns = Ld(hap_int, position_masked, start=center - w, stop=center + w)

#     # SFS stats
#     pi_v = (
#         mean_pairwise_difference(
#             ac[(position_masked >= center - w) & (position_masked <= center + w)]
#         ).sum()
#         / position_masked.size
#     )

#     d_v = tajima_d(ac, position_masked, start=center - w, stop=center + 1)

#     h_v = fay_wu_h_normalized(
#         hap_01, position_masked, start=center - w, stop=center + w
#     )[-1]

#     e_v = zeng_e(hap_01, position_masked, start=center - w, stop=center + w)

#     df_window = pd.DataFrame(
#         {
#             "positions": 6e5,
#             "daf": 1.0,
#             "h1": h1_v,
#             "h12": h12_v,
#             "h2_h1": h2_h1_v,
#             "k": k,
#             "haf": haf_v,
#             "zns": zns,
#             "omega_max": omega_max,
#             "pi": pi_v,
#             "tajima_d": d_v,
#             "faywu_h": h_v,
#             "zeng_e": e_v,
#         },
#         index=[0],
#     )

#     if 6e5 in df_summaries.positions.values:
#         columns_to_set_nan = [
#             "h1",
#             "h12",
#             "h2_h1",
#             "k",
#             "haf",
#             "zns",
#             "omega_max",
#             "pi",
#             "tajima_d",
#             "faywu_h",
#             "zeng_e",
#         ]

#         df_summaries.loc[
#             df_summaries.positions == 6e5, columns_to_set_nan
#         ] = df_window.loc[df_window.positions == 6e5, columns_to_set_nan].values
#     else:
#         df_summaries = pd.merge(df_summaries, df_window, how="outer")

#     df_summaries.insert(0, "iter", i)

#     return df_summaries.sort_values("positions")


# def write_hap(ts, output_file, recombination_hapmap=None, sep=""):
#     hap_01, ac, biallelic_maks = filter_biallelics(HaplotypeArray(ts.genotype_matrix()))

#     # Save the array to the file
#     np.savetxt(output_file + ".hap", hap_01, fmt="%d", delimiter=sep, newline="\n")

#     # Compress the file using gzip through a subprocess
#     subprocess.run(["gzip", "-f", output_file + ".hap"])

#     if recombination_hapmap is not None:
#         pd.DataFrame(recombination_hapmap[biallelic_maks, :]).to_csv(
#             output_file + ".map.gz", index=False, header=False, sep=" "
#         )


# def write_discoal(ts, recombination_hapmap, output_file):
#     hap_01, ac, biallelic_maks = filter_biallelics(HaplotypeArray(ts.genotype_matrix()))

#     with open(output_file, "w") as f:
#         f.write("/discoal/discoal 50 1 1200000\n\n")
#         f.write("//\n")
#         f.write("segsites: " + str(hap_01.shape[0]) + "\n")
#         f.write(
#             "positions: "
#             + " ".join(
#                 ["{:.6f}".format(i) for i in recombination_hapmap[:, 2] / 1200000]
#             )
#             + "\n"
#         )
#         for i in hap_01.T:
#             f.write("".join(i.astype(str)) + "\n")


# def read_hap(hap_file, map_file):
#     hap = np.vstack(
#         [
#             np.array(list((map(int, i[0]))))
#             for i in pd.read_csv(hap_file, header=None).values
#         ]
#     )

#     rec_map = pd.read_csv(map_file, sep=" ", header=None).values

#     return hap, rec_map

# def summary_statistics(sims, nthreads=1, normalize=False):
#     """Summary

#     Args:
#         sims (TYPE): Description
#         nthreads (TYPE): Description

#     Returns:
#         TYPE: Description
#     """
#     # neutral_stats = pool_stats(isnull
#     #     calculate_region_stats, sims.neutral, nthreads, "neutral"
#     # )

#     pars = [(i[0], i[1]) for i in sims]

#     params = np.row_stack(tuple(zip(*sims))[-1])

#     # Log the start of the scheduling
#     logging.info("Scheduling simulations")

#     # Use joblib to parallelize the execution
#     iter_stats = Parallel(n_jobs=nthreads, verbose=2)(
#         delayed(calculate_stats)(ts, rec_map, index)
#         for index, (ts, rec_map) in enumerate(pars)
#     )

#     # Ensure params order
#     idx, df_fv = zip(*iter_stats)
#     df_fv = pd.concat(df_fv).reset_index(drop=True)
#     # df_fv.index = np.repeat(idx,5)

#     if normalize:
#         df_fv.iloc[:, :] = np.apply_along_axis(normalize_row, 0, df_fv.values)
#         # df_fv.loc[:, df_fv.columns.str.contains("haf")] = (
#         #     df_fv.loc[:, df_fv.columns.str.contains("haf")] / 10
#         # )

#     summ_stats = pd.concat(
#         [
#             pd.DataFrame(
#                 np.repeat(params, 5, axis=0), columns=["s", "t", "f_i", "f_t"]
#             ),
#             df_fv,
#         ],
#         axis=1,
#     )
#     summ_stats.s = -np.log(summ_stats.s)
#     return summ_stats.fillna(0)

#     # num_nans = summ_stats.isnull().sum(axis=1) > 5

#     # return summ_stats[~num_nans].fillna(0)

#     # sweep_stats = pool_stats(sims, nthreads)

#     # return summ_stats


# files = glob.glob("/home/jmurgamoreno/*hard*")

# out = []
# for f in files:
#     tmp = np.array(f.split("/")[-1].split(".txt")[0].split("_"))

#     df = pd.read_csv(f)

#     for column in df.columns:
#         df[column] = df[column] / df[column].abs().max()

#     df[["time", "status"]] = tmp[[0, -1]]
#     df = df.reset_index()

#     d = pd.melt(
#         pd.concat([df.iloc[:, 0], df.iloc[:, 5:]], axis=1),
#         id_vars=["time", "status", "index"],
#     )

#     d[["stat", "window"]] = d.variable.str.split("_w", expand=True)
#     d = d.loc[:, ["index", "time", "status", "value", "stat", "window"]]
#     # d = d.groupby(['time','status','stat','window']).value.mean().reset_index()
#     d.window = pd.Categorical(
#         d.window, categories=["50000", "100000", "200000", "500000", "1000000"]
#     )

#     out.append(d)

# df = pd.concat(out)

##############
