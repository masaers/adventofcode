import sys
import numpy as np
import math
import re
import copy


def main(path):
    result = 0
    frag = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line[:-1]
            frag = [ int(x) for x in line ]
    # print(f"{frag=}")
    files = []
    free = []
    i, j = 1, 2
    pos = frag[0]
    while j < len(frag):
        # print(f"{i=} {j=} {pos=} {frag[i]=} {frag[j]=}")
        free.append([pos, frag[i]])
        pos += frag[i]
        files.append([pos, frag[j], j // 2])
        pos += frag[j]
        i += 2
        j += 2
    # print(f"{files=} {free=} {pos=}")
    for i in range(len(files)-1, -1, -1):
        for j in range(len(free)):
            if files[i][1] <= free[j][1] and free[j][0] < files[i][0]:
                files[i][0] = free[j][0]
                free[j][1] -= files[i][1]
                free[j][0] += files[i][1]
                break
        # print(f"{i=} {files[i]=} {free=}")
    for pos, sz, i in files:
        for j in range(sz):
            result += (pos+j) * i
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
