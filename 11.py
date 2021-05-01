#!/usr/bin/python
import sys


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


# return all locations of substring t in s
def substr_positions(s, t):
    positions = []
    for i in range(0, len(s)):
        if s[i:i+len(t)] == t:
            positions += [str(i+1)+' ']
    return positions


def main():
    for arg in sys.argv[1:]:
        lines = parseInput(arg)
        pos = substr_positions(lines[0], lines[1])
        out = ""
        for i in pos:
            out += i
        print(out)


if __name__ == "__main__":
    main()
