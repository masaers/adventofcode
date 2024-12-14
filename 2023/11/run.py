import sys
import re
import math
import numpy as np

def main(path):
    result = 0
    galaxies = []
    lines = {}
    cols = {}
    expansion = 2
    expansion = 1_000_000
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            for j, c in enumerate(line):
                if c == "#":
                    galaxies.append((i, j))
                    lines[i] = True
                    cols[j] = True
    # print(f"{galaxies=}")
    I = max(lines.keys()) + 1
    J = max(cols.keys()) + 1
    # print(f"{I=} {J=}")
    # lines = sorted(lines.keys())
    # cols = sorted(cols.keys())
    # print(f"{lines=}")
    # print(f"{cols=}")
    di = np.array([ 1 if i in lines else expansion for i in range(I) ])
    dj = np.array([ 1 if j in cols  else expansion for j in range(J) ])
    # print(f"{di=} {dj=}")
    di = np.cumsum(di)
    dj = np.cumsum(dj)
    for a in range(len(galaxies)):
        A = galaxies[a]
        for b in range(a+1, len(galaxies)):
            B = galaxies[b]
            dist = np.abs(di[A[0]] - di[B[0]]) + np.abs(dj[A[1]] - dj[B[1]])
            # print(f"{A=} {B=} {dist=}")
            result += dist
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
