import sys
import numpy as np
import math
import re
import copy
import collections

moves = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def main(path):
    result = 0
    board = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            board.append([ int(x) for x in line[:-1] ])
    I = len(board)
    J = len(board[0])
    # print(board)
    # print('\n'.join([ ''.join([str(y) for y in x]) for x in board ]))
    queue = collections.deque()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 0:
                queue.append((i, j, cell, (i, j)))
    while queue:
        i, j, n, start = queue.popleft()
        if n == 9:
            result += 1
            continue
        for di, dj in moves:
            if 0 <= (i+di) < I and 0 <= (j+dj) < J and board[i+di][j+dj] == n+1:
                queue.append((i+di, j+dj, n+1, start))
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
