import sys
import numpy as np
import math
import re

def main(path):
    result = 0
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            for m in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", line):
                result += int(m.group(1)) * int(m.group(2))
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
