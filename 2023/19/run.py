import sys
import re
import math
import numpy as np
import copy
import heapq

def parse_cond(cond):
    if m := re.match("([amsx])([<>])([0-9]+):(.+)", cond):
        aspect = m.group(1)
        op = m.group(2)
        value = int(m.group(3))
        target = m.group(4)
        if op == "<":
            return lambda part: target if part[aspect] < value else None
        if op == ">":
            return lambda part: target if part[aspect] > value else None
    else:
        return lambda part: cond
    raise RuntimeError(f"Bad condition {cond=}")

def main(path):
    result = 0
    states = {}
    parts = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if m := re.match("([^{]+){([^}]+)}", line):
                state = m.group(1)
                cond = [ parse_cond(c) for c in m.group(2).split(",") ]
                states[state] = cond
            elif not line:
                pass
            else:
                parts.append({ a: int(v) for a, v in re.findall("([amsx])=([0-9]+)", line) })
    # print(f"{states=}")
    # print(f"{parts=}")
    for part in parts:
        # print(f"{part=}")
        state = "in"
        while state and state not in (["A", "R"]):
            for f in states[state]:
                if f(part):
                    state = f(part)
                    break
            # print(f"{state=}")
        if state == "A":
            for a, v in part.items():
                result += v
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
