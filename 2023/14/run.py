import sys
import re
import math
import numpy as np
import copy

def encode(lines):
    result = []
    for line in lines:
        for c in line:
            if c == ".": result.append("0")
            if c == "O": result.append("1")
    # for i in range(len(result) % 8):
    #     result.append("0")
    result = int("".join(result), 2)
    return np.base_repr(result, 36)

def load(lines):
    result = 0
    for i, line in enumerate(lines):
        result += line.count("O") * (len(lines) - i)
    return result

def roll(lines, srci, srcj, trgi, trgj):
    if lines[srci][srcj] == "O" and lines[trgi][trgj] == ".":
        lines[srci][srcj], lines[trgi][trgj] = lines[trgi][trgj], lines[srci][srcj]
        return 1
    return 0

def north(lines):
    result = 0
    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            result += roll(lines, i, j, i-1, j)
    return result
def west(lines):
    result = 0
    for i in range(len(lines)):
        for j in range(1, len(lines[i])):
            result += roll(lines, i, j, i, j-1)
    return result
def south(lines):
    result = 0
    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            result += roll(lines, i-1, j, i, j)
    return result
def east(lines):
    result = 0
    for i in range(len(lines)):
        for j in range(1, len(lines[i])):
            result += roll(lines, i, j-1, i, j)
    return result

def cycle(lines, hlist, hdict):
    changes = north(lines)
    while changes != 0:
        changes = north(lines)
    changes = west(lines)
    while changes != 0:
        changes = west(lines)
    changes = south(lines)
    while changes != 0:
        changes = south(lines)
    changes = east(lines)
    while changes != 0:
        changes = east(lines)
    enc = encode(lines)
    hlist.append(enc)
    if enc not in hdict:
        hdict[enc] = 1
    else:
        hdict[enc] += 1

def cycle_len(hlist, hdict):
    if hdict[hlist[-1]] <= 2:
        return 0
    for i in range(1, len(hlist)-1):
        a = len(hlist) - 1 - i
        if hlist[-1] == hlist[a]:
            break
    b = len(hlist) - 1 - (2*i)
    if b < 0 or hlist[a] != hlist[b]:
        return 0
    for i in range(a-b):
        if hlist[a+i] != hlist[b+i]:
            return 0
    return a-b

def main(path):
    target = 1_000_000_000
    result = 0
    with open(path, "r") as f:
        lines = []
        for i, line in enumerate(f.readlines()):
            line = [ x for x in line[:-1] ]
            lines.append(line)
    # print("\n".join(["".join(x) for x in lines] + [""]))
    enc = encode(lines)
    hlist = [ enc ]
    hdict = { enc: 1 }
    while (c := cycle_len(hlist, hdict)) == 0:
        cycle(lines, hlist, hdict)
    # print(f"{c=}")
    # print(f"{(target - (len(hlist) - c)) % c=}")
    for _ in range((target - (len(hlist) - 1 - c)) % c):
        cycle(lines, hlist, hdict)
    # for i, h in enumerate(hlist):
    #     print(f"{i:2} {h}")
    result = load(lines)
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
