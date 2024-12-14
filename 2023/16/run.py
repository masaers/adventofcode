import sys
import re
import math
import numpy as np
import copy


def main(path):
    result = 0
    lines = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            lines.append([ x for x in line[:-1] ])
    # print("\n".join([ "".join(x) for x in lines ]))
    history = {}
    beams = [ (0, 0, 1, 0) ]
    energ = np.zeros((len(lines), len(lines[0])), dtype=bool)
    while beams:
        new_beams = []
        # print(f"{beams=}")
        for beam in beams:
            x, y, dx, dy = beam
            if beam in history:
                continue
            if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                continue
            history[beam] = True
            energ[y][x] = True
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
        # print(energ)
    result = np.sum(energ)
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
