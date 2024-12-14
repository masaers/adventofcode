import numpy as np
import sys


def main():
    lines = []
    with open("input", "r") as f:
        for line in f.readlines():
            lines.append(line[:-1])
    # print(lines)
    # print([ len(x) for x in lines ])
    sum = 0
    for i, line in enumerate(lines):
        # print(f"{i=} {line=}")
        j = 0
        while j < len(line):
            next_j = j+1
            if line[j] in "0123456789":
                n = int(line[j])
                while next_j < len(line) and line[next_j] in "0123456789":
                    n *= 10
                    n += int(line[next_j])
                    next_j += 1
                nr = False
                for ii in range(max(i-1, 0), min(i+2, len(lines))):
                    lline = lines[ii]
                    for jj in range(max(j-1, 0), min(next_j+1, len(lline))):
                        cc = lline[jj]
                        nr = nr or (cc not in "0123456789.")
                sum += n if nr else 0
                # print(f"{n=} {nr=}")
            j = next_j
    print(sum)
if __name__ == "__main__": main()
