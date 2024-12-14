import sys
import re

def intersection(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            yield a[i]
            i += 1
            j += 1
        else:
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
    return

def add_copies(copies, fcopies, sect):
    for i, _ in enumerate(sect):
        if i < len(fcopies):
            fcopies[i] += copies
        else:
            fcopies.append(copies)
    return fcopies

def main():
    sum = 0
    lines = []
    with open("input", "r") as f:
        for line in f.readlines():
            line = line[:-1]
            if line:
                lines.append(line)
        print(lines)
    print(sum)
if __name__ == "__main__": main()
