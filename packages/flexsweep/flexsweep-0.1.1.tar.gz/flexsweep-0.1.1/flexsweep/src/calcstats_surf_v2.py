from collections import Counter
import sys
from tskit import load
from allel import HaplotypeArray
from pathlib import Path
import numpy as np
import os
import pandas as pd


def open_tree(ts):
    try:
        hap = HaplotypeArray(ts.genotype_matrix())
    except:
        try:
            hap = HaplotypeArray(ts)
        except:
            hap = HaplotypeArray(load(ts).genotype_matrix())

    # HAP matrix centered to analyse whole chromosome
    hap_01, ac, biallelic_mask = filter_biallelics(hap)
    hap_int = hap_01.astype(np.int8)
    position_masked = load(ts).sites_position[biallelic_mask]
    sequence_length = int(1.2e6)

    return (
        hap_01,
        position_masked,
    )


def filter_biallelics(hap):
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


def ts_to_ms(ts, i=1):
    i = int(Path(ts).stem.split("_")[-1])

    (
        hap_01,
        position_masked,
    ) = open_tree(ts)

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
            pd.DataFrame([header, " ", "//", segsites_line, positions_line]),
            pd.DataFrame(haplotypes_block),
        ]
    )

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


# Modification to open tskit.tree, write the ms and then proceed
file1 = sys.argv[1]
np_ms = ts_to_ms(file1).values.flatten()

# f2 = open(ms_file + ".stats", "w")
# f = open(ms_file, "r")
popsize = int(np_ms[0].split(" ")[1])
segs = np_ms[4]
segs = segs.lstrip("positions: ").split(" ")
segs = list(map(float, segs))
seglistlen = len(segs)

data = np_ms[5:].tolist()

mid = int(seglistlen / 2)
oneten = seglistlen / 10
ranges = range(-320, 330, 5)
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

    # for eachhapfreq in hapfreq:
    #     f2.write(str(eachhapfreq) + ",")
    # if lenhlist < 5:
    #     numzeros = 5 - lenhlist
    #     for eachzero in range(numzeros):
    #         f2.write(str(0.0) + ",")

    if lenhlist < 5:
        numzeros = 5 - lenhlist

        win_stat = np.array([avepi, h1, h12, h21] + hapfreq + [0] * numzeros)
    else:
        win_stat = np.array([avepi, h1, h12, h21] + hapfreq)

    stats.append(win_stat)

pd.DataFrame(np.concatenate(stats)).T.to_csv(
    os.path.splitext(file1)[0] + ".ms.stats", header=False, index=False
)
