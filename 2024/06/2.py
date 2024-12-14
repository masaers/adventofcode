import sys
import numpy as np
import math
import re
import copy

GUARD = {
    "^": (-1, 0, ">"),
    ">": (0, +1, "v"),
    "v": (+1, 0, "<"),
    "<": (0, -1, "^"),
}

def find_guard(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in GUARD:
                return i, j, matrix[i][j]

def is_done(matrix, guard, gi, gj, history):
    if gi < 0 or len(matrix) <= gi:
        return True, True
    if gj < 0 or len(matrix[0]) <= gj:
        return True, True
    if (gi, gj) in history and history[(gi, gj)].get(guard, False):
        # print(f"{gi=} {gj=} {guard=} {history[(gi, gj)]=}")
        return True, False
    return False, False

def mark(i, j, guard, history):
    # print(f"mark({i=}, {j=}, {guard=}, history)")
    if (i, j) not in history:
        history[(i, j)] = {}
    history[(i, j)][guard] = True
    return

def move(matrix, guard, gi, gj, history):
    di, dj, next_g = GUARD[guard]
    # print(f"{di=} {dj=} {next_g=}")
    done, outside = is_done(matrix, guard, gi+di, gj+dj, history)
    mark(gi, gj, guard, history)
    if done:
        return guard, gi, gj, done, outside
    if matrix[gi+di][gj+dj] == "#":
        return next_g, gi, gj, done, outside
    return guard, gi+di, gj+dj, done, outside

def run(board, gi, gj, guard):
    history = {}
    done = False
    outside = False
    while not done:
        guard, gi, gj, done, outside = move(board, guard, gi, gj, history)
    return outside, history
    
def main(path):
    result = 0
    board = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            board.append([ x for x in line[:-1] ])
    I = len(board)
    J = len(board[0])
    gi, gj, guard = find_guard(board)
    board[gi][gj] = "."
    outside, history = run(board, gi, gj, guard)
    assert(outside)
    for i, j in history:
        board[i][j] = "#"
        outside, _ = run(board, gi, gj, guard)
        if not outside:
            result += 1
        board[i][j] = "."
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
