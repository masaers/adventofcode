import sys
import numpy as np
import math
import re

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
        return True
    if gj < 0 or len(matrix[0]) <= gj:
        return True
    if (gi, gj) in history and history[(gi, gj)].get(guard, False):
        # print(f"{gi=} {gj=} {guard=} {history[(gi, gj)]=}")
        return True
    return False

def mark(i, j, guard, history):
    # print(f"mark({i=}, {j=}, {guard=}, history)")
    if (i, j) not in history:
        history[(i, j)] = {}
    history[(i, j)][guard] = True
    return

def move(matrix, guard, gi, gj, history):
    di, dj, next_g = GUARD[guard]
    # print(f"{di=} {dj=} {next_g=}")
    done = is_done(matrix, guard, gi+di, gj+dj, history)
    mark(gi, gj, guard, history)
    if done:
        return guard, gi, gj, done
    if matrix[gi+di][gj+dj] == "#":
        return next_g, gi, gj, done
    return guard, gi+di, gj+dj, done
    
def main(path):
    result = 0
    board = []
    history = {}
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            board.append([ x for x in line[:-1] ])
    I = len(board)
    J = len(board[0])
    gi, gj, guard = find_guard(board)
    done = False
    # print("\n".join([ "".join(row) for row in board ]))
    while not done:
        # print(f"{guard=} {gi=} {gj=} {done=}")
        guard, gi, gj, done = move(board, guard, gi, gj, history)
    # print(f"{guard=} {gi=} {gj=} {done=}")
    result = len(history)
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
