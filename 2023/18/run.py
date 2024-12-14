import sys
import re
import math
import numpy as np
import copy
import heapq

def traversed(x, y, dx, dy, n):
    for i in range(n):
        x += dx
        y += dy
        yield x, y
    return

# UR F (0, -1) + (+1, 0) = (+1, -1)
# UL 7 (0, -1) + (-1, 0) = (-1, -1)
# DR L (0, +1) + (+1, 0) = (+1, +1)
# DL J (0, +1) + (-1, 0) = (-1, +1)
# URu F-J* diff
# URd F-7* same
# ULu *L-7 diff
# ULd *F-7 same
# DRu L-J* same
# DRd L-7* diff
# 
direction = {
    "U": (0, -1),
    "D": (0, +1),
    "R": (+1, 0),
    "L": (-1, 0),
}

move = {
    "U": lambda x, y, n: (x, y - n),
    "D": lambda x, y, n: (x, y + n),
    "R": lambda x, y, n: (x + n, y),
    "L": lambda x, y, n: (x - n, y),
}

def adjusted_bounds(minx, maxx, miny, maxy, x, y):
    return (min(minx, x), max(maxx, x), min(miny, y), max(maxy, y))

# def scanline_discrete_blocks(edge, axis=-1):
#     edge = edge.astype(np.int32)
#     diff = np.diff(edge, prepend=0, axis=axis) - np.diff(edge, append=0, axis=axis)
#     return np.logical_or(edge, np.cumsum(np.minimum(1, edge * diff), axis=axis) % 2)

def main(path):
    result = 0
    cmd = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            if m := re.match("([UDRL]) ([0-9]+) \(#(..)(..)(..)\)", line[:-1]):
                d = m.group(1)
                n = int(m.group(2))
                r = int(m.group(3), 16)
                g = int(m.group(3), 16)
                b = int(m.group(3), 16)
                cmd.append((d, n, r, g, b))
            else:
                print("ERROR!")
    # print(f"{cmd=}")
    bounds = (0,0,0,0)
    x = 0
    y = 0
    for d, n, r, g, b in cmd:
        x, y, = move[d](x, y, n)
        bounds = adjusted_bounds(*bounds, x, y)
    # print(f"{x=} {y=} {bounds=}")
    if x != 0 or y != 0:
        print(f"ERROR expected {x=}==0 and {y=}==0 (loop condition)")
    x -= bounds[0]
    y -= bounds[2]
    bounds = (bounds[0] - bounds[0],
              bounds[1] - bounds[0],
              bounds[2] - bounds[2],
              bounds[3] - bounds[2])
    # print(f"{x=} {y=} {bounds=}")
    board = np.zeros((bounds[1]+1, bounds[3]+1), dtype=bool)
    # bd = np.zeros((bounds[1]+1, bounds[3]+1, 2), dtype=np.int32)
    bdx = np.zeros_like(board, dtype=np.int32)
    dx0 = 0
    dy0 = 0
    for i, (d, n, r, g, b) in enumerate(cmd):
        dx, dy = direction[d]
        bdx[x][y] -= direction[cmd[i-2][0]][0]
        # bd[x][y] -= direction[cmd[i-2][0]]
        for x, y in traversed(x, y, dx, dy, n):
            board[x][y] = True
            bdx[x][y] += dx
            # bd[x][y] += (dx, dy)
    print("\n".join([ "".join([ str(y) for y in x ]) for x in board.astype(np.int32) ]))
    print(f"{np.abs(bdx)=}")
    print(f"{np.cumsum(np.abs(bdx),axis=1)=}")
    # print(f"{(np.cumsum(np.abs(bdx),axis=1) % 2) + board=}")
    # inside = scanline_discrete_blocks(board, axis=-1)
    # result = np.sum(inside)
    result = np.sum(((np.cumsum(np.abs(bdx), axis=1) % 2) + board) != 0)
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
