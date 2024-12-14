import sys
import numpy as np
import math
import re
import copy
import collections
import functools
import scipy

def first_free(mask):
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if not mask[i][j]:
                return i, j
    return None, None

deltas = [
    np.array([-1, 0], dtype=int),
    np.array([+1, 0], dtype=int),
    np.array([0, -1], dtype=int),
    np.array([0, +1], dtype=int),
]
def flood_fill(board, i, j):
    q = collections.deque([ np.array([i, j], dtype=int) ])
    result = np.zeros_like(board, dtype=bool)
    queued = np.zeros_like(board, dtype=bool)
    queued[i, j] = True
    count = 0
    while q:
        count += 1
        v0 = q.popleft()
        result[tuple(v0)] = True
        for d in deltas:
            v1 = v0 + d
            if True \
               and np.all(0 <= v1) \
               and np.all(v1 < board.shape) \
               and not queued[tuple(v1)] \
               and board[tuple(v0)] == board[tuple(v1)] \
               :
                q.append(v1)
                queued[tuple(v1)] = True
    return result

def all_patches(board):
    mask = np.zeros((len(board), len(board[0])), dtype=bool)
    while not np.all(mask):
        i, j = first_free(mask)
        patch = flood_fill(board, i, j)
        yield board[i][j], patch
        mask = np.logical_or(mask, patch)
    return

def area(patch):
    return np.sum(patch)

def perimeter(patch):
    return np.sum(np.diff(patch, prepend=False, append=False, axis=0)) \
        +  np.sum(np.diff(patch, prepend=False, append=False, axis=1)) \
        ;

def corners(patch):
    result = 0
    shape = (2, 2)
    patch = np.pad(patch, 1)
    sv = tuple(np.subtract(patch.shape, shape) + 1) + shape
    view = np.lib.stride_tricks.as_strided(patch, sv, patch.strides * 2)
    view = view.reshape((-1,) + shape)
    uniq_corners = np.sum(view, axis=(1,2))
    uniq_corners = np.sum(np.logical_or(uniq_corners == 1, uniq_corners == 3))
    shared_corners = np.sum(np.all(view == np.array([ [ True, False ], [ False, True ] ]), axis=(1,2))) \
        +            np.sum(np.all(view == np.array([ [ False, True ], [ True, False ] ]), axis=(1,2)))
    result = uniq_corners + 2*shared_corners
    # print(f"{patch.shape=} {view.shape=} {shared_corners=}")
    return result

def main(path):
    result = 0
    board = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            board.append([ c for c in line.strip() ])
    board = np.array(board)
    for crop, patch in all_patches(board):
        # print(f"{crop=} {area(patch)=} {perimeter(patch)=} {corners(patch)=}")
        # print(patch)
        result += area(patch) * corners(patch)
        # break
        # 824242 too low
        # 826686 too low
        # 830516
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
