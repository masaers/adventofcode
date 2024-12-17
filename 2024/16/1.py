import sys
import numpy as np
import math
import re
import copy
import collections
import functools
import scipy
import heapq

directions = [ # ++ = clockwise, -- = ccw
    np.array([  0, +1 ]), # E
    np.array([ -1,  0 ]), # S
    np.array([  0, -1 ]), # W
    np.array([ +1,  0 ]), # N
]

def steps(walls, pos, delta):
    yield pos, ((delta + 1) % len(directions)), 1000
    yield pos, ((delta - 1) % len(directions)), 1000
    new_pos = pos + directions[delta]
    if not walls[tuple(new_pos)]:
        yield new_pos, delta, 1

def explore(walls, start, end, delta=0, cost=0):
    q = [ (cost, start, delta) ]
    queued = set([ (tuple(start), delta) ])
    while q:
        cost, pos, delta = heapq.heappop(q)
        if np.all(pos == end):
            return cost
        for new_pos, new_delta, step_cost in steps(walls, pos, delta):
            if (tuple(new_pos), new_delta) not in queued:
                heapq.heappush(q, (cost + step_cost, tuple(new_pos), new_delta))
                queued.add((tuple(new_pos), new_delta))
    raise RuntimeError(f"No valid move(s) to get from {start=} to {end=}")


def main(path):
    result = 0
    board = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            board.append([ x for x in line ])
    # print(f"{board=}")
    walls = np.array(board) == "#"
    start = np.r_[np.nonzero(np.array(board) == "S")]
    end = np.r_[np.nonzero(np.array(board) == "E")]
    delta = 0
    # print(f"{walls=} {start=} {end=}")
    result = explore(walls, start, end)
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
