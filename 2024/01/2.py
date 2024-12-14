import sys
import numpy as np
import math
import re

def inc(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

def main(path):
    a = {}
    b = {}
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            if m := re.match("([0-9]+) *([0-9]+)", line[:-1]):
                inc(a, int(m.group(1)))
                inc(b, int(m.group(2)))
    result = 0
    for x in a:
        if x in b:
            result += x * a[x] * b[x]
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
