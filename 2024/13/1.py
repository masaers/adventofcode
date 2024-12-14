import sys
import numpy as np
import math
import re
import copy
import collections
import functools


def main(path):
    result = 0
    claws = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            # print(f"{line=}")
            if m := re.match(r"Button A: X\+([0-9]+), Y\+([0-9]+)", line):
                claws.append( [ np.array([int(m.group(1)), int(m.group(2))]) ] )
            elif m := re.match(r"Button B: X\+([0-9]+), Y\+([0-9]+)", line):
                claws[-1].append(np.array([ int(m.group(1)), int(m.group(2)) ]))
            elif m := re.match(r"Prize: X=([0-9]+), Y=([0-9]+)", line):
                claws[-1].append(np.array([ int(m.group(1)), int(m.group(2)) ]))
    # print(f"{claws=}")
    cost = np.array([3, 1])
    for a, b, prize in claws:
        c = np.array([
            ( prize[0]*b[1] - prize[1]*b[0] ) / ( a[0]*b[1] - a[1]*b[0] ),
            ( a[0]*prize[1] - a[1]*prize[0] ) / ( a[0]*b[1] - a[1]*b[0] ),
        ])
        if np.all(c.astype(int) == c):
            result += np.sum(cost * c)
            # print(f"{a=} {b=} {prize=} {c=}")
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
