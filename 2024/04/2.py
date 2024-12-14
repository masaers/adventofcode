import sys
import numpy as np
import math
import re

def main(path):
    result = 0
    matrix = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            matrix.append([ x for x in line[:-1] ])
    # print(matrix)
    I = len(matrix)
    J = len(matrix[0])
    # D = 3
    # print(f"{I=} {J=} {D=}")
    ok = [ "MMSS", "MSMS", "SSMM", "SMSM" ]
    for i in range(1, I-1):
        for j in range(1, J-1):
            if matrix[i][j] != "A":
                continue
            if "".join([ matrix[i-1][j-1], matrix[i-1][j+1], matrix[i+1][j-1], matrix[i+1][j+1] ]) in ok:
                result += 1
    # 2098 too high
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
