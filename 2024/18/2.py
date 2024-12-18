import sys
import numpy as np
import math
import re
import copy
import collections
import functools
import scipy
import heapq


def moves(x, y, Y, X):
    if 0 < x: yield x-1, y
    if 0 < y: yield x, y-1
    if x < X-1: yield x+1, y
    if y < Y-1: yield x, y+1
    
def explore(board, after):
    # print(board)
    best = { (0, 0): 0 }
    # best = np.zeros_like(board, dtype=int)
    q = [ (0, 0, 0) ]
    while q:
        steps, x, y = heapq.heappop(q)
        # print(f"{steps=} {x=} {y=}")
        # print(f"{q=}")
        if x+1 == board.shape[1] and y+1 == board.shape[0]:
            return steps
        for next_x, next_y in moves(x, y, *board.shape):
            if after < board[next_y, next_x]:
                if (next_y, next_x) not in best or (steps+1) < best[next_y, next_x]:
                    best[next_y, next_x] = steps+1
                    heapq.heappush(q, (steps+1, next_x, next_y))
    return None

def main(path):
    result = 0
    size = 7
    after = 12
    size = 71
    after = 1024
    board = np.zeros((size, size), dtype=int)
    with open(path, "r") as f:
        count = 0
        for i, line in enumerate(f.readlines()):
            if m := re.match(r"([0-9]+),([0-9]+)", line):
                count += 1
                board[int(m.group(2)), int(m.group(1))] = count
    board[board == 0] = count*size*size
    lo = 0
    hi = count+1
    mid = lo + (hi-lo)//2
    while lo != mid and mid != hi:
        # print(f"{lo=} {mid=} {hi=}")
        if explore(board, mid):
            lo = mid
        else:
            hi = mid
        mid = lo + (hi-lo)//2
    # print(f"{lo=} {mid=} {hi=}")
    # print(f"{board=}")
    result = ",".join([ str(x) for x in reversed(np.argwhere(board == mid+1)[0]) ])
    # print(f"{np.argwhere(board == mid+1)=}")
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
