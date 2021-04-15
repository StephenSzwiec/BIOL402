import sys

def hamming_distance(s, t):
    dh = 0
    for i in range(0,len(s),1):
        a = s[i]
        b = t[i]
        if a != b:
            dh += 1
    return dh

def parseInput(fileName):
    eof = False
    temp = ""
    data = []

    with open(fileName) as f:
        while eof is not True:
            temp = f.readline()
            if temp == '':
                break
            data = data + [temp.rstrip()]
    return data

def main():
    dist = 0
    for arg in sys.argv[1:]:
        strings = parseInput(arg)
        dist = hamming_distance(strings[0], strings[1])
    print(dist)

if __name__ == "__main__":
    main()
