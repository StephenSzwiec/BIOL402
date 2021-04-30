import sys
from Bio import SeqIO


# read in a fasta file and output an array of seqs
def parseInput(filename):
    seqs = list(SeqIO.parse(filename, "fasta"))
    return seqs


# return the error of an attempted hamming distance
# error limited to some integer err_limit
def hamming_dist(a, b, err_limit):
    error = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            error += 1
            if (error > err_limit):
                return error
    return error


# return the suboptimal alignments of two repeats 32-40bp in length
def subo(a, b):
    number_final = 0
    for i in range(32, 41):
        for j in range(len(a) - i):
            number = 0
            for k in range(len(b) - i):
                if (hamming_dist(a[j:j+i], b[k:k+i], 5) <= 3):
                    number += 1
                    #print(a[j:j+i])
                    if (number > number_final):
                        number_final = number
    return number_final


# magic
def main():
    for arg in sys.argv[1:]:
        reads = parseInput(arg)
        print(subo(str(reads[1].seq), str(reads[0].seq)))
        print(subo(str(reads[0].seq), str(reads[1].seq)))


if __name__ == "__main__":
    main()
