import sys
import numpy as np
import math
import re

def main(path):
    result = 0
    on = True
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            # print(f"{i=} {line=}")
            for m in re.finditer(r"(don't\(\)|do\(\)|mul\(([0-9]+),([0-9]+)\))", line):
                # print(m.group())
                if m.group(0) == "do()":
                    on = True
                elif m.group(0) == "don't()":
                    on = False
                elif on:
                    result += int(m.group(2)) * int(m.group(3))
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
