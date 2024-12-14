import sys
import numpy as np
import math
import re
import copy
import collections
import functools


def main(path):
    result = 0
    robots = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if m := re.match(r"p=([0-9]+),([0-9]+) v=([-0-9]+),([-0-9]+)", line):
                robots.append([ int(m.group(x)) for x in range(1,5) ])
    # print(f"{robots=}")
    X = 101 
    Y = 103 
    # X = 11
    # Y = 7
    T = 100
    pos = [ ( (x+T*dx) % X, (y+T*dy) % Y ) for x, y, dx, dy in robots ]
    # print(f"{pos=}")
    DX = X // 2
    DY = Y // 2
    count = [ 0, 0, 0, 0 ]
    for x, y in pos:
        if 0 <= x < DX:
            if 0 <= y < DY:
                count[0] += 1
            elif DY < y < Y:
                count[1] += 1
        elif DX < x < X:
            if 0 <= y < DY:
                count[2] += 1
            elif DY < y < Y:
                count[3] += 1
    # print(f"{count=}")
    result = count[0]
    for c in count[1:]:
        result *= c
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
