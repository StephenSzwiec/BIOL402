import sys


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


# reverse complement of a string
def revComp(seq):
    if 'U' in seq:
        seq_dict = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    else:
        seq_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([seq_dict[base] for base in reversed(seq)])


# returns True if own revcomp palindrome
def isRevComp(seq):
    return (seq == revComp(seq))


# returns list of position and lengths of strings matching its own revcomp
def RestrictionSites(seq):
    resultList = []
    for i in range(4, 13):
        for j in range(0, len(seq) - i + 1):
            if (isRevComp(seq[j:j + i])):
                resultList.append(str(j+1) + ' ' + str(i))
    return resultList


# magic happening
def main():
    for arg in sys.argv[1:]:
        dna = parseInput(arg)
        for i in RestrictionSites(dna):
            print(i)


if __name__ == "__main__":
    main()
