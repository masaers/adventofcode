import sys
import numpy as np
import math
import re

def main(path):
    a = []
    b = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            if m := re.match("([0-9]+) *([0-9]+)", line[:-1]):
                a.append(int(m.group(1)))
                b.append(int(m.group(2)))
    a = sorted(a)
    b = sorted(b)
    result = 0
    for x, y in zip(a, b):
        result += max(x, y) - min(x, y)
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
