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
    path = np.zeros_like(walls)
    path[tuple(start)] = True
    q = [ (cost, start, delta) ]
    queued = { (tuple(start), delta): [cost, path] }
    while q:
        cost, pos, delta = heapq.heappop(q)
        best_cost, path = queued[tuple(pos), delta]
        # if best_cost < cost:
        #     continue
        # queued.add((tuple(pos), delta))
        # print(f"{cost=} {pos=} {delta=}")
        if np.all(pos == end):
            yield cost, path
        else:
            for new_pos, new_delta, step_cost in steps(walls, pos, delta):
                # print(f"{new_pos=} {new_delta=} {step_cost=} {step_count=}")
                new_cost = cost + step_cost
                new_path = copy.deepcopy(path)
                new_path[tuple(new_pos)] = True
                key = (tuple(new_pos), new_delta)
                if key not in queued:
                    queued[key] = [new_cost, new_path]
                    heapq.heappush(q, (new_cost, tuple(new_pos), new_delta))
                elif new_cost == queued[key][0]:
                    queued[key][1] = np.logical_or(queued[key][1], new_path)
                elif new_cost < queued[key][0]:
                    queued[key] = [new_cost, new_path]

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
    for cost, path in explore(walls, start, end):
        # print(f"{cost=} {path.astype(int)=}")
        result = np.sum(path)
        break
    # 505 is too high
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
