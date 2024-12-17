import sys
import numpy as np
import math
import re
import copy
import collections
import functools
import scipy
import heapq

register_map = {
    "A": 0,
    "B": 1,
    "C": 2,
}

def combo(reg, op):
    if op < 4:
        return op
    if op < 7:
        return reg[op-4]
    raise ValueError(f"Illegal combo operand {op=}")

def adv(reg, op, p, tape):
    reg[0] = reg[0] // (2**combo(reg, op))
    return p + 2

def bxl(reg, op, p, tape):
    reg[1] = reg[1] ^ op
    return p + 2

def bst(reg, op, p, tape):
    reg[1] = combo(reg, op) % 8
    return p + 2

def jnz(reg, op, p, tape):
    if reg[0] == 0:
        return p + 2
    else:
        return op

def bxc(reg, op, p, tape):
    reg[1] = reg[1] ^ reg[2]
    return p + 2

def out(reg, op, p, tape):
    tape.append(str(combo(reg, op) % 8))
    return p + 2

def bdv(reg, op, p, tape):
    reg[1] = reg[0] // (2**combo(reg, op))
    return p + 2

def cdv(reg, op, p, tape):
    reg[2] = reg[0] // (2**combo(reg, op))
    return p + 2


opcodes = [ adv, bxl, bst, jnz, bxc, out, bdv, cdv ]

def run(reg, program):
    tape = []
    p = 0
    while p+1 < len(program):
        p = opcodes[program[p]](reg, program[p+1], p, tape)
        # print(f"{p=} {reg=} {tape=}")
    return ",".join(tape)

def main(path):
    result = 0
    reg = [ 0 for _ in register_map ]
    program = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if m := re.match(r"Register ([ABC]): ([0-9]+)", line):
                reg[register_map[m.group(1)]] = int(m.group(2))
            elif m := re.match(r"Program: ([,0-9]+)", line):
                program = [ int(x) for x in m.group(1).split(",") ]
            else:
                pass
    print(f"{reg=} {program=}")
    result = run(reg, program)
    # 0,5,1,7,6,4,0,2,7 is not right
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
