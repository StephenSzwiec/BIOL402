import sys

# given a DNA string, return complement


def revComp(dna):
    temp = dna.translate(str.maketrans("ATGC", "TACG"))
    return temp[::-1]

# open the data file, chop into array of lines, close the file


def parseInput(fileName):

    eof = False
    temp = []
    data = []

    fileBuffer = open(fileName, 'r')
    while eof is False:
        stream = fileBuffer.readline()
        if stream == '':
            eof = True
            break
        else:
            temp.append(stream)
    fileBuffer.close()

    for i in temp:
        if i[0] == '>':
            temp.remove(i)

    for j in range(0,len(temp),2):
        data.append(temp[j].rstrip() + temp[j+1].rstrip())

    return data


# iterate through data and return to accumulator


def accComp(someList):
    acc = 0
    for i in someList:
        if i == revComp(i):
            acc = acc + 1
        else:
            continue
    return acc


# accepts plaintext inputs

def main():
    acc2 = 0
    for arg in sys.argv[1:]:
        test = parseInput(arg)
        for i in test:
            print(i)
            print(revComp(i))
            if i == revComp(i):
                acc2 = acc2 + 1
                print(acc2)
            print("===========================")
    print("the total is:")
    print(acc2)

if __name__ == "__main__":
    main()
