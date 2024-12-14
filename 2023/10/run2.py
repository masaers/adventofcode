import sys
import re
import math
import numpy as np

pipes = {
    "|": [[0, -1], [0, +1]],
    "-": [[-1, 0], [+1, 0]],
    "J": [[-1, 0], [0, -1]],
    "L": [[+1, 0], [0, -1]],
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
    on_loop = np.zeros((Y, X), dtype=bool)
    for path in pos:
        for p in path:
            on_loop[p[1]][p[0]] = True
    # print(f"{on_loop.astype(np.uint8)=}")

    q = np.zeros((Y, X), dtype=bool)
    for y in range(Y):
        inside = False
        prev_bend = ""
        for x in range(X):
            q[y][x] = inside
            if not on_loop[y][x]:
                continue
            if lines[y][x] == "|":
                inside = not inside
                continue
            if lines[y][x] in ["F", "L"]:
                prev_bend = lines[y][x]
                continue
            if lines[y][x] == "J":
                if prev_bend == "F":
                    inside = not inside
                prev_bend = ""
            if lines[y][x] == "7":
                if prev_bend == "L":
                    inside = not inside
                prev_bend = ""
    result = np.sum(np.logical_and(q, ~on_loop))
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
