#!/usr/bin/python

import sys
from Bio import Entrez
from entrez_api import entrez_setup


# given a file, create a list of lines
def parseInput(filename):
    eof = False
    data = []
    with open(filename) as f:
        while (eof is not True):
            temp = f.readline()
            if (temp == ''):
                eof = True
                break
            else:
                data += [temp.rstrip()]
    return data


# search Entrez for records given a genus, start date, and end date from a file
def entrez_genus_by_dates(genus, begin, end):
    entrez_setup()
    handle = Entrez.esearch(db='nucleotide', term=genus+"[ORGN]", mindate=begin, maxdate=end, datetype='pdat')
    record = Entrez.read(handle)
    return record['Count']


def main():
    for arg in sys.argv[1:]:
        lines = parseInput(arg)
        print(lines)
        out = entrez_genus_by_dates(lines[0], lines[1], lines[2])
        print(out)

if __name__ == "__main__":
    main()
