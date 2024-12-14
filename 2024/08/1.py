import sys
import numpy as np
import math
import re
import copy

def main(path):
    result = 0
    board = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line[:-1]
            board.append([])
            for j in range(len(line)):
                board[i].append(line[j])
    # print("\n".join([ "".join(x) for x in board ]))
    I = len(board)
    J = len(board[0])
    antennas = {}
    for i in range(I):
        for j in range(J):
            if board[i][j] != ".":
                if board[i][j] not in antennas:
                    antennas[board[i][j]] = []
                antennas[board[i][j]].append((i, j))
    # print(f"{antennas=}")
    antinodes = {}
    for freq, locs in antennas.items():
        for a in locs:
            for b in locs:
                if a == b: continue
                di = a[0] - b[0]
                dj = a[1] - b[1]
                i = a[0] + di
                j = a[1] + dj
                if 0 <= i < I and 0 <= j < J:
                    antinodes[(i, j)] = True
    result = len(antinodes)
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
