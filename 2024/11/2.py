import sys
import numpy as np
import math
import re
import copy
import collections
import functools


@functools.cache
def expand(n, times):
    if times == 0:
        return 1
    else:
        if n == 0:
            return expand(1, times-1)
        else:
            strn = str(n)
            if len(strn) % 2 == 0:
                div = len(strn) // 2
                return expand(int(strn[:div]), times-1) + expand(int(strn[div:]), times-1)
            else:
                return expand(n * 2024, times-1)
            
def main(path):
    result = 0
    numbers = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            numbers = [ int(x) for x in line.split(" ") ]
    # print(f"{numbers=}")
    result = sum([ expand(n, 75) for n in numbers ])
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
