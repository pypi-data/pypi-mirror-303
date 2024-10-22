import subprocess
from pathlib import Path
from tskit import load
from collections import Counter

# from summaries import open_tree


class TreeInference:
    def __init__(self, simulations):
        self.output_folder = None
        self.simulations = simulations
        self.num_samples = 50
        self.samples = None
        self.M = 1
        self.poplabels = None
        self.genetic_map = 1.10429476e-08
        self.region = "chr2:135212517-136412517"
        self.mutation_rate = 1.29e-08
        self.Ne = 1e4
        self.gen_time = 28
        self.nthreads = 1
        self.relate = "/home/jmurgamoreno/software/relate/"
        self.clues = "/home/jmurgamoreno/software/CLUES2/"

    def run_inference(self, clues=True):
        assert self.output_folder is not None, "Check simulation folder"

        samples = np.char.add("tsk_", np.arange(self.num_samples).astype(str))

        sweep_samples = pd.DataFrame(
            {"ID1": samples, "ID2": samples, "missing": np.repeat(0, self.num_samples)}
        )

        # Use the `loc` function along with `insert` to add the row at the top
        new_row = pd.Series(
            [0] * len(sweep_samples.columns), index=sweep_samples.columns
        )

        # Inserting the row at the top
        sweep_samples.loc[-1] = new_row
        sweep_samples.index = sweep_samples.index + 1
        sweep_samples = sweep_samples.sort_index()

        sweep_samples.to_csv(
            self.output_folder + "/sweep.samples", na_rep="NA", index=False, sep="\t"
        )
        self.samples = self.output_folder + "/sweep.samples"

        sweep_labels = pd.DataFrame(
            {
                "sample": samples,
                "population": np.repeat("g1", self.num_samples),
                "group": np.repeat("g1", self.num_samples),
                "sex": np.repeat(np.nan, self.num_samples),
            }
        )

        sweep_labels.to_csv(
            self.output_folder + "/sweep.poplabels", na_rep="NA", index=False, sep="\t"
        )
        self.poplabels = self.output_folder + "/sweep.poplabels"

        tmp_map = deepcopy(self.genetic_map)
        try:
            chrom = self.region.split(":")[0]
            region = list(map(int, self.region.split(":")[1].split("-")))
            r_map = pd.read_csv(self.genetic_map, sep=" ").iloc[:, 1:]
            r_map.columns = ["pos", "rate", "cm"]
            r_map = r_map[(r_map.pos >= region[0]) & (r_map.pos <= region[1])]

            new_map = pd.DataFrame(
                {
                    "new_pos": np.arange(1, int(1.2e6 + 1)),
                    "pos": np.arange(region[0], region[1]),
                }
            )
            new_map = pd.merge(r_map, new_map).loc[:, ["new_pos", "rate", "cm"]]

            new_map.to_csv(
                self.output_folder + "/genetic_map.txt", index=False, sep="\t"
            )
            self.genetic_map = self.output_folder + "/genetic_map.txt"
        except:
            r_map = msprime.RateMap.uniform(1.2e6, self.genetic_map)
            positions = np.arange(0, 1.2e6, 1e5)

            # df_map = pd.DataFrame(
            #     {
            #         "pos": [positions],
            #         "rate": np.repeat(self.genetic_map, positions.size) * 1e6,
            #         "cm": r_map.get_cumulative_mass(positions),
            #     }
            # )
            df_map = pd.DataFrame(
                {
                    "pos": [0, 1.2e6],
                    "rate": [1, 1],
                    "cm": [0, 1.2],
                }
            )
            df_map.to_csv(
                self.output_folder + "/genetic_map.txt", index=False, sep="\t"
            )
            self.genetic_map = self.output_folder + "/genetic_map.txt"

        # pars = [(i[0], i[1]) for i in self.simulations]
        # params = pd.DataFrame(
        #     tuple(zip(*self.simulations))[-1],
        #     columns=["s", "t", "t_end", "f_i", "f_t"],
        # )

        trees, rec_maps, params = list(zip(*self.simulations))
        params = pd.DataFrame(params, columns=["s", "t", "t_end", "f_i", "_f_t", "f_t"])
        # params = params[params.f_t < 1]

        # trees = [trees[i] for i in params.index]
        # rec_maps = [rec_maps[i] for i in params.index]

        haps, positions = zip(
            *Parallel(n_jobs=self.nthreads, backend="threading", verbose=5)(
                delayed(self.write_hap)(ts, rec_map)
                for (ts, rec_map) in zip(trees, rec_maps)
            )
        )

        params["position"] = positions
        # Change dir to run relate
        os.chdir(self.output_folder + "/sweeps")

        # relate
        df_relate = Parallel(
            n_jobs=self.nthreads, backend="multiprocessing", verbose=5
        )(
            delayed(self.run_relate)(hap, param)
            for (hap, param) in zip(haps, params.to_numpy())
        )

        df_relate = pd.concat(df_relate)
        df_relate = df_relate.loc[:, ["iter", "variant_age", "age_begin", "age_end"]]

        # # tsinfer
        # Parallel(n_jobs=self.nthreads, backend="multiprocessing", verbose=1)(
        #     delayed(self.run_tsinfer)(ts) for ts in trees
        # )

        if clues:
            df_clues = Parallel(
                n_jobs=self.nthreads, backend="multiprocessing", verbose=2
            )(
                delayed(self.run_clues)(hap, param)
                for (hap, param) in zip(haps, params.to_numpy())
            )

            df_clues = (
                pd.concat(df_clues)
                .reset_index(drop=True)
                .loc[
                    :,
                    [
                        "iter",
                        "logLR",
                        "-log10(p-value)",
                        "SelectionMLE1",
                        "SelectionTrue",
                    ],
                ]
            )

        # Removes tmp files
        tmp_remove = [
            os.remove(i) for i in list(set(glob.glob("*")) - set(glob.glob("*trees")))
        ]

        self.genetic_map = tmp_map

        return pd.merge(df_relate, df_clues, on="iter", how="outer")

    def write_hap(self, ts, rec_map, i=1, position=6e5):
        try:
            i = int(Path(ts).stem.split("_")[-1])
        except:
            i = np.random.randint(1e4)

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

        df_hap = pd.DataFrame(hap_01)

        try:
            variants = np.row_stack([v.alleles[:2] for v in ts.variants()])
        except:
            variants = np.row_stack([v.alleles[:2] for v in load(ts).variants()])

        variants = pd.DataFrame(variants[biallelic_maks])
        df_hap = pd.concat(
            [pd.DataFrame(position_masked).astype(int), variants, df_hap], axis=1
        )

        df_hap.insert(
            0, "SNP", np.char.add("SNP", np.arange(position_masked.size).astype(str))
        )

        df_hap.insert(0, "CHROM", 1)

        df_hap.to_csv(
            self.output_folder + "/sweeps/sweep_" + str(i) + ".haps",
            index=False,
            sep=" ",
            header=False,
        )

        if df_hap[df_hap.iloc[:, 2] == position].empty:
            freqs = df_hap.iloc[:, 5:].mean(axis=1)
            position = self.find_nearest(
                df_hap[freqs > 0.8].iloc[:, 2].values, position
            )

            df_hap[df_hap.iloc[:, 2] == position].iloc[:, 5:].T.to_csv(
                self.output_folder + "/sweeps/derived_" + str(i) + ".txt",
                index=False,
                header=False,
            )
        else:
            df_hap[df_hap.iloc[:, 2] == position].iloc[:, 5:].T.to_csv(
                self.output_folder + "/sweeps/derived_" + str(i) + ".txt",
                index=False,
                header=False,
            )

        self.get_coal_times(ts, position, "relate", i)

        return self.output_folder + "/sweeps/sweep_" + str(i) + ".haps", position

    def run_relate(self, hap, param, i=1):
        _s, _t, _t_end, _f_i, _og_f_t, _f_t, position = param

        i = int(Path(hap).stem.split("_")[-1])

        # Run Relate
        subprocess.run(
            [
                self.relate + "/bin/Relate",
                "--mode",
                "All",
                "-m",
                str(self.mutation_rate),
                "-N",
                str(2 * int(self.Ne)),
                "--haps",
                hap,
                "--sample",
                self.samples,
                "--map",
                self.genetic_map,
                "-o",
                "sweep_" + str(i),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.run(
            [
                self.relate
                + "/scripts/EstimatePopulationSize/EstimatePopulationSize.sh",
                "-i",
                "sweep_" + str(i),
                "-m",
                str(self.mutation_rate),
                "--poplabels",
                self.poplabels,
                "-o",
                "sweep_" + str(i) + "_popsize",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.run(
            [
                self.relate + "/scripts/SampleBranchLengths/SampleBranchLengths.sh",
                "-i",
                "sweep_" + str(i),
                "-o",
                "sweep_" + str(i) + "_resample",
                "-m",
                str(self.mutation_rate),
                "--coal",
                "sweep_" + str(i) + "_popsize.coal",
                "--num_samples",
                str(self.M),
                "--format",
                "n",
                "--first_bp",
                str(int(position)),
                "--last_bp",
                str(int(position)),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        df_ages = pd.read_csv("sweep_" + str(i) + ".mut", sep=";")
        df_ages.insert(0, "variant_age", df_ages.iloc[:, 8:10].mean(1))
        df_ages.insert(0, "iter", i)

        return df_ages[df_ages.pos_of_snp == position]

    def run_clues(self, hap, param, i=1):
        _s, _t, _t_end, _f_i, _og_f_t, _f_t, position = param

        i = int(Path(hap).stem.split("_")[-1])

        t_limit = 2000 if _t <= 2000 else 5000

        # CLUES2
        subprocess.run(
            [
                "python",
                self.clues + "RelateToCLUES.py",
                "--RelateSamples",
                "sweep_" + str(i) + "_resample.newick",
                "--DerivedFile",
                "derived_" + str(i) + ".txt",
                "--out",
                "coal_" + str(i),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        clues_cmd = [
            "python",
            self.clues + "/inference.py",
            "--popFreq",
            str(_f_t),
            "--N",
            str(self.Ne * 2),
            "--tCutoff",
            str(t_limit),
        ]
        if t_limit == 5000:
            clues_cmd += ["--timeBins", "2000"]

        subprocess.run(
            clues_cmd
            + [
                "--times",
                "coal_" + str(i) + "_relate_true_times.txt",
                "--out",
                "sweep_" + str(i) + "_relate_true",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # subprocess.run(
        #     clues_cmd
        #     + [
        #         "--times",
        #         "coal_" + str(i) + "_tsinfer_true_times.txt",
        #         "--out",
        #         "sweep_" + str(i) + "_tsinfer_true",
        #     ],
        #     stdout=subprocess.DEVNULL,
        #     stderr=subprocess.DEVNULL,
        # )

        subprocess.run(
            clues_cmd
            + ["--times", "coal_" + str(i) + "_times.txt", "--out", "sweep_" + str(i)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        try:
            df_traj_true = pd.read_csv(
                "sweep_" + str(i) + "_relate_true_inference.txt", sep="\t"
            )
            df_traj = pd.read_csv("sweep_" + str(i) + "_inference.txt", sep="\t")
            df_traj.insert(0, "iter", i)
            if t_limit == 5000:
                df_traj = df_traj.loc[
                    :,
                    [
                        "iter",
                        "logLR",
                        "-log10(p-value)",
                        "Epoch2_start",
                        "Epoch2_end",
                        "SelectionMLE2",
                    ],
                ]
                df_traj.insert(6, "SelectionTrue", df_traj_true.SelectionMLE2)
                df_traj.rename(
                    {
                        "Epoch2_start": "Epoch1_start",
                        "Epoch2_end": "Epoch1_end",
                        "SelectionMLE2": "SelectionMLE1",
                    },
                    axis="columns",
                    inplace=True,
                )
            else:
                df_traj.insert(6, "SelectionTrue", df_traj_true.SelectionMLE1)

            df_traj.iloc[:, -2:] *= 2
        except:
            df_traj = pd.DataFrame(
                {
                    "iter": i,
                    "logLR": np.nan,
                    "-log10(p-value)": np.nan,
                    "Epoch1_start": np.nan,
                    "Epoch1_end": np.nan,
                    "SelectionMLE1": np.nan,
                    "SelectionTrue": np.nan,
                },
                index=[0],
            )

        # except:
        #     df_age_traj = pd.DataFrame(
        #         {
        #             "index": i,
        #             "iter": np.nan,
        #             "pos_of_snp": np.nan,
        #             "age_begin": np.nan,
        #             "age_end": np.nan,
        #             "variant_age": np.nan,
        #             "logLR": np.nan,
        #             "-log10(p-value)": np.nan,
        #             "Epoch1_start": np.nan,
        #             "Epoch1_end": np.nan,
        #             "SelectionMLE1": np.nan,
        #         },
        #         index=[0],
        #     )

        return df_traj

    def get_coal_times(self, ts, position, output, i=1):
        try:
            ts_loaded = load(ts)
        except:
            ts_loaded = ts

        tsb = ts_loaded.at(position)
        hap = np.column_stack([ts_loaded.sites_position, ts_loaded.genotype_matrix()])
        is_derived = hap[hap[:, 0] == position, 1:].flatten().astype(int)

        anc_times = []
        der_times = []
        crossnode = []

        for j in range(is_derived.size - 1):
            for k in range(j + 1, len(is_derived)):
                node_time = tsb.mrca(j, k)
                if is_derived[j] == 1 and is_derived[k] == 1:
                    der_times.append(node_time)
                elif is_derived[j] == 0 and is_derived[k] == 0:
                    anc_times.append(node_time)
                else:
                    crossnode.append(node_time)

        anc_times = np.unique(anc_times)
        der_times = np.unique(der_times)
        crossnode = np.unique(crossnode)

        new_anc_times = [0.0] * len(anc_times)
        new_der_times = [0.0] * len(der_times)
        new_crossnode = [0.0] * len(crossnode)

        # convert from nodes to times
        for j in range(len(anc_times)):
            if anc_times[j] < 0:
                print("PROBLEM2")
            else:
                new_anc_times[j] = float(tsb.time(anc_times[j]))

        for j in range(len(der_times)):
            new_der_times[j] = float(tsb.time(der_times[j]))
        for j in range(len(crossnode)):
            new_crossnode[j] = float(tsb.time(crossnode[j]))
        new_der_times.append(new_crossnode[0])
        new_anc_times.sort()
        new_der_times.sort()

        if (len(new_der_times) + len(new_anc_times) + 1) != len(list(tsb.leaves())):
            print("PROBLEM7")

        anc_coal = ""
        der_coal = ""
        for time in new_anc_times:
            anc_coal = anc_coal + str(time) + ","
        for time in new_der_times:
            der_coal = der_coal + str(time) + ","

        f = open(
            self.output_folder
            + "/sweeps/coal_"
            + str(i)
            + "_"
            + output
            + "_true_times.txt",
            "w",
        )

        f.writelines(
            der_coal[0 : (len(der_coal) - 1)]
            + "\n"
            + anc_coal[0 : (len(anc_coal) - 1)]
            + "\n"
        )  # added indexing to remove comma at the end
        f.close()

    def find_nearest(self, array, value):
        idx = np.searchsorted(array, value, side="left")
        if idx > 0 and (
            idx == len(array)
            or math.fabs(value - array[idx - 1]) < math.fabs(value - array[idx])
        ):
            return array[idx - 1]
        else:
            return array[idx]

    def run_tsinfer(self, ts, i=1):
        i = int(Path(ts).stem.split("_")[-1])

        ts_loaded = load(ts)

        with tsinfer.SampleData(
            path="sweep_" + str(i) + ".samples",
            sequence_length=ts_loaded.sequence_length,
            num_flush_threads=2,
        ) as sim_sample_data:
            for var in ts_loaded.variants():
                sim_sample_data.add_site(var.site.position, var.genotypes, var.alleles)

        inferred_ts = tsinfer.infer(sim_sample_data)

        # Simplify tsinfer trees
        inferred_ts_simpl = inferred_ts.simplify(keep_unary=False)

        dated_ts_simpl = tsdate.date(
            inferred_ts_simpl, Ne=10000, mutation_rate=1.29e-08, ignore_oldest_root=True
        )

        self.get_coal_times(dated_ts_simpl, 6e5, "tsinfer", i)


class Surfdawave:
    def __init__(self, simulations):
        self.output_folder = None
        self.simulations = simulations
        self.nthreads = 1
        self.surfdawave = "/home/jmurgamoreno/software/surfdawave/"
        self.python = "/home/jmurgamoreno/miniforge3/bin/python"
        self.Rscript = "/home/jmurgamoreno/miniforge3/bin/Rscript"

    def run_inference(self):
        assert self.output_folder is not None, "Check simulation folder"

        trees, rec_maps, params = list(zip(*self.simulations))
        params = pd.DataFrame(
            params, columns=["s", "t", "t_end", "f_i", "f_t", "f_t_end"]
        )
        models = {
            "hard_old_complete": 0,
            "hard_old_incomplete": 1,
            "hard_young_complete": 2,
            "hard_young_incomplete": 3,
        }
        params["model"] = "sweep"

        params.loc[
            (params.t >= 2000) & (params.f_t >= 0.9), "model"
        ] = "hard_old_complete"
        params.loc[
            (params.t >= 2000) & (params.f_t < 0.9), "model"
        ] = "hard_old_incomplete"
        params.loc[
            (params.t < 2000) & (params.f_t >= 0.9), "model"
        ] = "hard_young_complete"
        params.loc[
            (params.t < 2000) & (params.f_t < 0.9), "model"
        ] = "hard_young_incomplete"
        params.model = params.model.apply(lambda r: models[r])

        df_stats_list = Parallel(n_jobs=self.nthreads, verbose=2)(
            delayed(surf_summaries)(ts, rec_map)
            for (ts, rec_map) in zip(trees, rec_maps)
        )

        df_stats = pd.concat(df_stats_list).reset_index(drop=True)
        df_stats["model"] = params.model.astype(str)

        df_stats.sample(5000).to_csv(
            self.surfdawave + "/sweep_surf_stats", header=None, index=None
        )
        subprocess.run(
            [
                self.Rscript,
                self.surfdawave + "/FDAclass.R",
                self.surfdawave + "/sweep_surf_stats",
            ]
        )


def surf_summaries(ts, rec_map):
    np_ms = ts_to_ms(ts, rec_map).values.flatten()

    popsize = int(np_ms[0].split(" ")[1])
    segs = np_ms[3]
    segs = segs.lstrip("positions: ").split(" ")
    segs = list(map(float, segs))
    seglistlen = len(segs)

    data = np_ms[4:].tolist()

    mid = int(seglistlen / 2)
    oneten = seglistlen / 10
    ranges = list(range(-320, 330, 5))
    stats = []
    for win in range(128):
        midsnp = []
        winsegs = []

        for eachline in data:
            midsnp.append(eachline[mid])
            winsegs.append(eachline[mid + ranges[win] : mid + ranges[win + 2]])

        pi = hetfunc(winsegs)
        avepi = pi / len(winsegs[0])
        count = Counter(winsegs)
        counts = []

        for l in set(winsegs):
            counts.append(count[l])
        sortedcount = sorted(counts, reverse=True)
        hlist = []
        for each in sortedcount:
            hlist.append(each)
        lenhlist = len(hlist)
        hapnum = 0
        hapfreq = []

        while hapnum < 5 and hapnum < lenhlist:
            hapfreq.append(hlist[hapnum] / float(popsize))
            hapnum += 1

        hlist2 = [eachH / (float(len(winsegs))) for eachH in hlist]
        hsqlist = [j**2 for j in hlist2]

        h2sq = hsqlist[1:]
        h2sum = float(sum(h2sq))
        h1 = float(sum(hsqlist))
        h21 = h2sum / h1
        one = hlist2[0]
        two = hlist2[1]
        h12sqlist = h2sq[1:]
        h12part1 = (one + two) * (one + two)
        h12part2 = sum(h12sqlist)
        h12 = h12part1 + h12part2

        if lenhlist < 5:
            numzeros = 5 - lenhlist

            win_stat = np.array([avepi, h1, h12, h21] + hapfreq + [0] * numzeros)
        else:
            win_stat = np.array([avepi, h1, h12, h21] + hapfreq)

        stats.append(win_stat)

    return pd.DataFrame(np.concatenate(stats)).T


def ts_to_ms(ts, rec_map, i=1, ms_file=None):
    i = int(Path(ts).stem.split("_")[-1])

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

    header_line = "ms " + str(hap_01.shape[1]) + " 1"
    # header = "\n".join([header_line, "", "//"])
    header = "".join(
        [
            header_line,
            "",
        ]
    )

    num_segsites = hap_01.shape[0]

    segsites_line = f"segsites: {num_segsites}"

    positions = np.array([pos / 1.2e6 for pos in position_masked])
    positions_line = "positions: " + " ".join(f"{pos:.6f}" for pos in positions)

    haplotypes_block = []
    for hap in hap_01.T:
        haplotypes_block.append("".join(map(str, hap)))

    output_file = os.path.splitext(ts)[0] + ".ms"

    df_ms = pd.concat(
        [
            pd.DataFrame([header, "//", segsites_line, positions_line]),
            pd.DataFrame(haplotypes_block),
        ]
    )

    if (ms_file is not None) and (isinstance(ms_file, str)):
        df_ms.to_csv(ms_file, index=False, sep=",", header=None)

    # with open(output_file, "w") as f:
    #     f.write(
    #         "\n".join(
    #             [header, segsites_line, positions_line, "\n".join(haplotypes_block)]
    #         )
    #     )

    return df_ms


def hetfunc(datasamp):
    heter = 0
    for tt in range(len(datasamp[0])):
        cou = 0
        for ttt in range(len(datasamp)):
            cou += float(datasamp[ttt][tt])
        p = cou / float(len(datasamp))

        heter += (2 * p) * (1 - p)
    return heter
