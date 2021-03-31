#!/usr/bin/python

import sys
import Bio.Seq

# given an mRNA string, return protein sequence from first ORF

def parseInput(fileName):

    eof = False
    temp = ""
    data = []

    with open(fileName) as f:
        while True:
            c = f.read(3)
            if c == "\n":
                break
            if not c:
                break
            data = data + [c]

    return data

# dictionary for mRNA to AAs

mrna_aa = {
        "UUU": "F",
        "UUC": "F",
        "UUA": "L",
        "UUG": "L",
        "UCU": "S",
        "UCC": "S",
        "UCA": "S",
        "UCG": "S",
        "UAU": "Y",
        "UAC": "Y",
        "UAA": "Stop",
        "UAG": "Stop",
        "UGU": "C",
        "UGC": "C",
        "UGA": "Stop",
        "UGG": "W",
        "CUU": "L",
        "CUC": "L",
        "CUA": "L",
        "CUG": "L",
        "CCU": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "CAU": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGU": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AUU": "I",
        "AUC": "I",
        "AUA": "I",
        "AUG": "M",
        "ACU": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "AAU": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "AGU": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GUU": "V",
        "GUC": "V",
        "GUA": "V",
        "GUG": "V",
        "GCU": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "GAU": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "GGU": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G"
}

def main():
    string_out = ""
    for arg in sys.argv[1::]:
        codons = parseInput(arg)
        print(codons)
        for i in codons:
            string_out = string_out + mrna_aa[i]
        print(string_out)


if __name__ == "__main__":
    main()
