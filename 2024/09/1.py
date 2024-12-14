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
    fid = 0
    last_fid = len(frag) // 2
    pos = 0
    first = 0
    last = len(frag)
    while first < len(frag):
        # print(f"{fid=} {last_fid=} {pos=} {first=} {result=} {frag[first:]=}")
        next_pos = pos + frag[first]
        for i in range(pos, next_pos):
            result += i * fid
        pos = next_pos
        first += 1
        fid += 1
        if not first < len(frag):
            break
        next_pos = pos + frag[first]
        for i in range(pos, next_pos):
            while frag[-1] == 0:
                frag.pop()
                frag.pop()
                last_fid -= 1
            result += i * last_fid
            frag[-1] -= 1
        pos = next_pos
        first += 1
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
