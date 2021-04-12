import sys

# take the reverse complement of a dna string


def revComp(dna):
    return str(dna).translate(str.maketrans("ATGC", "TACG"))[::-1]

# return the annealing temperature of a sequence


def anneal_temp(dna):
    temp = 0
    for i in dna:
      if (i == "A" or i == "T"):
          temp += 2
      if (i == "G" or i == "C"):
          temp += 4
    return temp
  
# parse a FASTA formated file into a vector of strings


def parseInput(fileName):
    eof = False
    data = []
    fileBuffer = open(fileName, 'r')
    while eof is False:
        temp = fileBuffer.readline()
        if temp == '':
            eof = True
            break
        else:
            data.append(temp)
    fileBuffer.close()
    for i in data:
        if i[0] == '>':
            data.remove(i)
    data = [j[:-1] for j in data]
    return data
  
# output primers


def main():
    for arg in sys.argv[1:]:
        seq_1 = str(parseInput(arg)).lstrip("['")
        seq_1 = seq_1[1341:2060]
        print(seq_1[0:22])
        print("===========================================")
        primer1 = revComp(seq_1[0:22])
        print(primer1)
        print("===========================================")
        seq_2 = seq_1[297:]
        print(seq_2[0:22])
        print("===========================================")
        primer2 = revComp(seq_2[0:22])
        print(primer2)

if __name__ == "__main__":
    main()
