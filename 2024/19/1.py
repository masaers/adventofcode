# For some reason Python's regular expression engine is unable to
# handle this in reasonable time, so I switched to Perl, which had no
# problems running the below idea (see 1.perl).
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
    # print(f"{towels=} {patterns=}")
    regex = "^(" + "|".join(towels) + ")+$"
    r = re.compile(regex)
    # print(f"{regex=}")
    for pattern in patterns:
        if re.match(r, pattern):
            result += 1
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
