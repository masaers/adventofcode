import numpy as np
import sys


def main():
    lines = []
    # with open("example", "r") as f:
    with open("input", "r") as f:
        for line in f.readlines():
            lines.append(line[:-1])
    # print(lines)
    sum = 0
    parts = [ [] for _ in lines ]
    gears = []
    for i, line in enumerate(lines):
        # print(f"{i=} {line=}")
        j = 0
        while j < len(line):
            next_j = j+1
            if line[j] == "*":
                gears.append((i, j))
            elif line[j] in "0123456789":
                n = int(line[j])
                while next_j < len(line) and line[next_j] in "0123456789":
                    n *= 10
                    n += int(line[next_j])
                    next_j += 1
                parts[i].append((j, next_j, n))
            j = next_j
    # print(parts)
    # print(gears)
    for gi, gj in gears:
        # print(f"{gi=} {gj=}")
        gparts = []
        for pi in range(max(gi-1, 0), min(gi+2, len(parts))):
            # print(f"{pi=}")
            for pja, pjz, pn in parts[pi]:
                # print(f"{pja=} {pjz=} {pn=}")
                if pja-1 <= gj <= pjz:
                    gparts.append(pn)
        # print(f"{gparts=}")
        if len(gparts) == 2:
            sum += gparts[0] * gparts[1]
    print(sum)
if __name__ == "__main__": main()
