import sys
import re
import math
import numpy as np
import copy
import heapq

move = {
    "U": lambda x, y, n: (x, y - n),
    "D": lambda x, y, n: (x, y + n),
    "R": lambda x, y, n: (x + n, y),
    "L": lambda x, y, n: (x - n, y),
}

def shoelace_polygon_double_area(x, y):
    return np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def main(path):
    result = 0
    cmd = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            if m := re.match("([UDRL]) ([0-9]+) \(#(.....)(.)\)", line[:-1]):
                d = "RDLU"[int(m.group(4))]
                n = int(m.group(3), 16)
                cmd.append((d, n))
            else:
                print("ERROR!")
    # print(f"{cmd=}")
    x = 0
    y = 0
    vertices = [(x, y)]
    perimeter = 0
    for d, n in cmd:
        x, y, = move[d](x, y, n)
        vertices.append((x, y))
        perimeter += n
    # perimeter -= 1
    print(f"{perimeter=}")
    # print(f"{vertices=}")
    A = shoelace_polygon_double_area(np.array([ x for x, _ in vertices ]),
                                     np.array([ y for _, y in vertices ]))
    A = A // 2
    print(f"{A=}")
    result = A + 1 - perimeter // 2
    result += perimeter
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
