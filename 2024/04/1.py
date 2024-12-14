import sys
import numpy as np
import math
import re

def main(path):
    result = 0
    word = "XMAS"
    drow = "".join([x for x in reversed(word)])
    matrix = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            matrix.append([ x for x in line[:-1] ])
    # print(matrix)
    I = len(matrix)
    J = len(matrix[0])
    D = len(word)
    # print(f"{I=} {J=} {D=}")
    for i1, i2 in zip(range(I), range(D, I+1)):
        # print(f"{i1=} {i2=}")
        for j in range(J):
            w = "".join([ matrix[i][j] for i in range(i1, i2) ])
            result += (1 if w == word else 0)
            result += (1 if w == drow else 0)
        for j1, j2 in zip(range(J), range(D, J+1)):
            w = "".join([ matrix[i][j] for i, j in zip(range(i1, i2), range(j1, j2)) ])
            # print(f"{w=}")
            result += (1 if w == word else 0)
            result += (1 if w == drow else 0)
            w = "".join([ matrix[i][j] for i, j in zip(range(i1, i2), range(j2-1, j1-1, -1)) ])
            # print(f"{w=}")
            result += (1 if w == word else 0)
            result += (1 if w == drow else 0)
    for j1, j2 in zip(range(J), range(D, J+1)):
        # print(f"{j1=} {j2=}")
        for i in range(I):
            w = "".join([ matrix[i][j] for j in range(j1, j2) ])
            result += (1 if w == word else 0)
            result += (1 if w == drow else 0)
                    
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
