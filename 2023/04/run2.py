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
    fcopies = []
    # with open("example", "r") as f:
    with open("input", "r") as f:
        for line in f.readlines():
            copies = 1 + (fcopies.pop(0) if fcopies else 0)
            _, line = line.split(":")
            win, own = line.split("|")
            win = sorted([ int(x) for x in re.split("\W+", win) if x ])
            own = sorted([ int(x) for x in re.split("\W+", own) if x ])
            sect = [ x for x in intersection(win, own) ]
            fcopies = add_copies(copies, fcopies, sect)
            sum += copies
    print(sum)
if __name__ == "__main__": main()
