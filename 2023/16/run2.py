import sys
import re
import math
import numpy as np
import copy


def energ_map(lines, init_beam):
    result = np.zeros((len(lines), len(lines[0])), dtype=bool)
    history = {}
    beams = [ init_beam ]
    while beams:
        new_beams = []
        for beam in beams:
            x, y, dx, dy = beam
            if beam in history:
                continue
            if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                continue
            history[beam] = True
            result[y][x] = True
            if lines[y][x] == ".":
                new_beams.append((x+dx, y+dy, +dx, +dy))
                continue
            if lines[y][x] == "\\":
                new_beams.append((x+dy, y+dx, +dy, +dx))
                continue
            if lines[y][x] == "/":
                new_beams.append((x-dy, y-dx, -dy, -dx))
                continue
            if lines[y][x] == "-":
                if dy != 0:
                    new_beams.append((x+dy, y, +dy, 0))
                    new_beams.append((x-dy, y, -dy, 0))
                else:
                    new_beams.append((x+dx, y+dy, dx, dy))
                continue
            if lines[y][x] == "|":
                if dx != 0:
                    new_beams.append((x, y+dx, 0, +dx))
                    new_beams.append((x, y-dx, 0, -dx))
                else:
                    new_beams.append((x+dx, y+dy, dx, dy))
                continue
        beams = new_beams
    return result
    
def main(path):
    result = 0
    lines = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            lines.append([ x for x in line[:-1] ])
    for x in range(len(lines[0])):
        result = max(result, np.sum(energ_map(lines, (x, 0, 0, 1))))
        result = max(result, np.sum(energ_map(lines, (x, len(lines)-1, 0, -1))))
    for y in range(len(lines)):
        result = max(result, np.sum(energ_map(lines, (0, y, 1, 0))))
        result = max(result, np.sum(energ_map(lines, (len(lines[0])-1, y, -1, 0))))
        
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
