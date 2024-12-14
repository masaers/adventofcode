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

    
def main():
    sum = 0
    # with open("example", "r") as f:
    with open("input", "r") as f:
        for line in f.readlines():
            _, line = line.split(":")
            win, own = line.split("|")
            win = sorted([ int(x) for x in re.split("\W+", win) if x ])
            own = sorted([ int(x) for x in re.split("\W+", own) if x ])
            sect = [ x for x in intersection(win, own) ]
            if sect:
                sum += 2 ** (len(sect)-1)
            # print(f"{win=} {own=} {sect=}")
    print(sum)
if __name__ == "__main__": main()
