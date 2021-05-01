#!/usr/bin/python

import sys
from Bio.Seq import Seq, translate
from re import finditer


# read a single line and grab the dna sequence
def parseInput(fileName):
    with open(fileName) as f:
        seq = Seq((f.readline()).rstrip())
    return seq


# find possible starting positions for ORF, then output longest
def longest_orf_read(seq):
    ORF = []
    for i in finditer("ATG", str(seq)):
        ORF += [translate(seq[i.start():], table=1, stop_symbol='', to_stop=True)]
    for j in finditer("ATG", str(seq.reverse_complement())):
        ORF += [translate(seq.reverse_complement()[j.start():], table=1, stop_symbol='', to_stop=True)]

    return max(map(str,ORF), key=len)


# magic happening
def main():
    for arg in sys.argv[1:]:
        print(longest_orf_read(parseInput(arg)))


if __name__ == "__main__":
    main()
