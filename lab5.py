import sys

# given a DNA string, return complement


def revComp(dna):
    return str(dna).translate(str.maketrans("ATGC", "TACG"))[::-1]

# open the data file, chop into array of lines, close the file


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

# accepts plaintext inputs


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
