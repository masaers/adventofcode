import sys
import re
import math
import numpy as np
import copy
import heapq

#     V
#     2
# > 1 0 3 <
#     4
#     ^

def move(lines, cost, x, y, dx, dy, X, Y, steps=3):
    for i in range(steps):
        x += dx
        y += dy
        if 0 <= x < X and 0 <= y < Y:
            cost += lines[y][x]
            yield cost + (X-1-x) + (Y-1-y), cost, x, y

def main(path):
    result = 0
    lines = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            lines.append([ int(x) for x in line[:-1] ])
    # print(f"{lines=}")
    X = len(lines[0])
    Y = len(lines)
    items = {} # ( 0, 0, 0 ): X-1 + Y-1 }
    beam = [ (0, 0, 0, 0, 0) ]
    while len(beam) != 0:
        prio, cost, x, y, d = heapq.heappop(beam)
        # print(f"{prio=} {x=} {y=} {d=}")
        if (x, y, d) in items:
            continue
        items[(x, y, d)] = prio
        if x == X-1 and y == Y-1:
            break
        if d == 0 or d % 2 == 0:
            for prio2, cost2, x2, y2 in move(lines, cost, x, y, +1, 0, X, Y):
                heapq.heappush(beam, (prio2, cost2, x2, y2, 1))
            for prio2, cost2, x2, y2 in move(lines, cost, x, y, -1, 0, X, Y):
                heapq.heappush(beam, (prio2, cost2, x2, y2, 1))
        if d == 0 or d % 2 == 1:
            for prio2, cost2, x2, y2 in move(lines, cost, x, y, 0, +1, X, Y):
                heapq.heappush(beam, (prio2, cost2, x2, y2, 2))
            for prio2, cost2, x2, y2 in move(lines, cost, x, y, 0, -1, X, Y):
                heapq.heappush(beam, (prio2, cost2, x2, y2, 2))
        # print(f"{beam=}")
    result = prio
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
