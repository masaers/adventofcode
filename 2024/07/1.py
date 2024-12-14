import sys
import numpy as np
import math
import re
import copy

def all_comb(numbers, results=None):
    if not numbers: return results
    if results is None:
        return all_comb(numbers[1:], numbers[:1])
    result = []
    for r in results:
        result += all_comb(numbers[1:], [r + numbers[0]])
        result += all_comb(numbers[1:], [r * numbers[0]])
    return result

def main(path):
    result = 0
    eqs = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            if m := re.match(r"([0-9]+):\s*(.*)", line[:-1]):
                eqs.append((int(m.group(1)), [int(x) for x in m.group(2).split(" ")]))
    # print(f"{eqs=}")
    for eq in eqs:
        # print(f"{eq=}")
        # print(f"{all_comb(eq[1])=}")
        for r in all_comb(eq[1]):
            if r == eq[0]:
                result += r
                break
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
