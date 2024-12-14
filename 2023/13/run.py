import sys
import re
import math
import numpy as np
import copy

def transpose(lines):
    result = [ [] for _ in lines[0] ]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            result[j].append(lines[i][j])
    result = [ "".join(x) for x in result ]
    return result

def mirrors(xs):
    result = []
    for i in range(1, len(xs)):
        good = True
        for sz in range(min(i, len(xs)-i)):
            if xs[i-1-sz] != xs[i+sz]:
                good = False
                break
        if good:
            result.append(i)
    return result
            
def main(path):
    result = 0
    pats = []
    with open(path, "r") as f:
        pat = { "lines": [], "cols": [] }
        lines = []
        rows = []
        for i, line in enumerate(f.readlines()):
            line = line[:-1]
            # print(f"{line=}")
            if not line:
                pats.append((copy.deepcopy(rows), [ int(x, 2) for x in transpose(lines) ]))
                rows = []
                lines = []
                continue
            line = line.replace(".", "0")
            line = line.replace("#", "1")
            lines.append(line)
            rows.append(int(line, 2))
        pats.append((rows, [ int(x, 2) for x in transpose(lines) ]))
    # print(f"{pats=}")
    for rows, cols in pats:
        # print(f"{rows=}")
        for m in mirrors(rows):
            # print(f"{m=}")
            result += 100 * m
        # print(f"{cols=}")
        for m in mirrors(cols):
            # print(f"{m=}")
            result += m
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
