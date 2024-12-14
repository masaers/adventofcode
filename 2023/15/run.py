import sys
import re
import math
import numpy as np
import copy


def hash(string):
    result = 0
    for c in string:
        result += ord(c)
        result *= 17
        result %= 256
    return result

def main(path):
    result = 0
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            result += sum([ hash(s) for s in line[:-1].split(",") ])
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
