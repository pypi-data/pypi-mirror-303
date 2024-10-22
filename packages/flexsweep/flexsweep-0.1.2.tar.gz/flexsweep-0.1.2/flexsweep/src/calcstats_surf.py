from collections import Counter
import sys
from tskit import load
from allel import HaplotypeArray
from pathlib import Path
import numpy as np
import os


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
    header = "\n".join([header_line, "", "//"])

    num_segsites = hap_01.shape[0]

    segsites_line = f"segsites: {num_segsites}"

    positions = np.array([pos / 1.2e6 for pos in position_masked])
    positions_line = "positions: " + " ".join(f"{pos:.6f}" for pos in positions)

    haplotypes_block = []
    for hap in hap_01.T:
        haplotypes_block.append("".join(map(str, hap)))

    output_file = os.path.splitext(ts)[0] + ".ms"
    with open(output_file, "w") as f:
        f.write(
            "\n".join(
                [header, segsites_line, positions_line, "\n".join(haplotypes_block)]
            )
        )

    return output_file


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
ms_file = ts_to_ms(file1)

f2 = open(ms_file + ".stats", "w")
f = open(ms_file, "r")
g = f.readlines()
popsize = int(g[0].split(" ")[1])
pop = popsize + 2
for i in range(len(g)):
    segs = []
    data = []
    if g[i][0:3] == "seg":
        segs = g[i + 1].rstrip(" \n").lstrip("positions: ").split(" ")
        segs = list(map(float, segs))
        seglistlen = len(segs)
        if seglistlen > 660:
            mid = int(seglistlen / 2)
            data = g[i + 2 : i + pop]
            oneten = seglistlen / 10
            ranges = range(-320, 330, 5)
            for win in range(128):
                midsnp = []
                winsegs = []
                for eachline in data:
                    midsnp.append(eachline[mid])
                    winsegs.append(eachline[mid + ranges[win] : mid + ranges[win + 2]])

                pi = hetfunc(winsegs)
                avepi = pi / len(winsegs[0])
                f2.write(str(avepi))
                f2.write(",")

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
                f2.write(str(h1))
                f2.write(",")
                f2.write(str(h12))
                f2.write(",")
                f2.write(str(h21))
                f2.write(",")
                for eachhapfreq in hapfreq:
                    f2.write(str(eachhapfreq) + ",")
                if lenhlist < 5:
                    numzeros = 5 - lenhlist
                    for eachzero in range(numzeros):
                        f2.write(str(0.0) + ",")

            f2.write("\n")
        else:
            pass


f.close()
f2.close()
