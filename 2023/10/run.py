import sys
import re
import math
import numpy as np

pipes = {
    "|": [[0, -1], [0, +1]],
    "-": [[-1, 0], [+1, 0]],
    "L": [[+1, 0], [0, -1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[-1, 0], [0, +1]],
    "F": [[+1, 0], [0, +1]],
}
pipes = { k: np.array(v) for k, v in pipes.items() }

def main(path):
    result = 0
    lines = []
    with open(path, "r") as f:
        for line in f.readlines():
            lines.append([ x for x in line[:-1] ])
        X = len(lines[0])
        Y = len(lines)
    for y in range(Y):
        for x in range(X):
            if lines[y][x] == "S":
                x0 = x
                y0 = y
    start = np.array([ x0, y0 ])
    pos = []
    for x in range(max(0, x0-1), min(X, x0+2)):
        for y in range(max(0, y0-1), min(Y, y0+2)):
            if not lines[y][x] in pipes:
                continue
            xy = np.array([ x, y ])
            if np.all(xy + pipes[lines[y][x]][0] == start):
                pos.append([ start, xy ])
            if np.all(xy + pipes[lines[y][x]][1] == start):
                pos.append([ start, xy ])

    while not np.all(np.logical_or(pos[0][-1] == pos[1][-1], pos[0][-1] == pos[1][-2])):
        for path in pos:
            tile = lines[path[-1][1]][path[-1][0]]
            if tile in pipes:
                targets = path[-1] + pipes[tile]
                path.append(targets[~np.all(targets == path[-2], axis=1)][0])
    result = len(pos[0]) - 1
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
