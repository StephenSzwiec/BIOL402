import sys
from re import search, finditer
from Bio.Seq import Seq, translate


# parse FASTA file into vector of sequence strings
def parseInput(fileName):
    eof = False
    temp = ''
    data = ''
    with open(fileName) as f:
        while eof is not True:
            temp = f.readline()
            if temp == '':
                eof = True
                break
            if temp[0] == '>':
                continue
            else:
                data = data + temp.rstrip()
    return data


# dictionary to slap mRNA into AAs
def codon_table(seq_type='rna'):
    bases = ['U', 'C', 'A', 'G'] if seq_type == 'rna' else ['T', 'C', 'A', 'G']
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))
    return codon_table


# reverse complement of a string
def revComp(seq):
    if 'U' in seq:
        seq_dict = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    else:
        seq_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([seq_dict[base] for base in reversed(seq)])


# transcription of dna
def transcribe(dna):
    return str(dna).translate(str.maketrans("ATGC", "UACG"))


# give all 6 ORF reads and return peptides
def raw_translate(seq):
    table = codon_table('dna')
    peptides = ['' for x in range(6)]
    rev = revComp(seq)
    for i in range(3):
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            if (len(codon) < 3):
                continue
            else:
                peptides[i] += table.get(codon, '-')
        for j in range(i, len(seq), 3):
            codon = rev[j:j+3]
            if (len(codon) < 3):
                continue
            else:
                peptides[i+3] += table.get(codon, '-')
    return peptides


# given raw peptide reads, return valid ORFs
def orf_reader(pep):
    found = []
    output = []
    for i in pep:
        for j in finditer("M", i):
            found += [i[j.start():]]
        for k in found:
            m = search('M[A-Z]*\*', k)
            #m = search('M[A-Z]*\*', k)
            if m is not None:
                output.append(m.group().rstrip('*'))
            #else:
                #output.append(k)
    return list(set(output))


# magic happening
def main():
    buff = []
    for arg in sys.argv[1:]:
        seq = parseInput(arg)
        for i in orf_reader(raw_translate(seq)):
            buff += [i]
        for j in sorted(buff):
            print(j)


if __name__ == "__main__":
    main()
