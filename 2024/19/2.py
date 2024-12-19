import sys
import numpy as np
import math
import re
import copy
import collections
import functools
import scipy
import heapq
import yaml

def matches(towels, pattern):
    chart = { 0: 1 }
    q = [ 0 ]
    while q:
        # print(f"{q=}")
        z = heapq.heappop(q)
        for towel in towels:
            if pattern[z:].startswith(towel):
                key = z + len(towel)
                if key not in chart:
                    heapq.heappush(q, key)
                chart[key] = chart.get(key, 0) + chart[z]
    # print(f"{chart=}")
    return chart.get(len(pattern), 0)

def main(path):
    result = 0
    towels = []
    patterns = []
    with open(path, "r") as f:
        count = 0
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if not line:
                continue
            if re.match(r".*,.*", line):
                towels = [ x.strip() for x in line.split(",") ]
            else:
                patterns.append(line)
    for pattern in patterns:
        result += matches(towels, pattern)
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
