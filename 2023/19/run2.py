import sys
import re
import math
import numpy as np
import copy
import heapq
import yaml
import collections

def parse_cond(cond):
    if m := re.match("([amsx])([<>])([0-9]+):(.+)", cond):
        aspect = m.group(1)
        op = m.group(2)
        value = int(m.group(3))
        target = m.group(4)
        if op == "<":
            return aspect, np.arange(0, 4000) < value, target
        if op == ">":
            return aspect, np.arange(0, 4000) > value, target
    else:
        return "a", True, cond
    raise RuntimeError(f"Bad condition {cond=}")

def merge_parts(a, b):
    result = False
    for aspect in "amsx":
        mask = np.logical_or(a[aspect], b[aspect])
        if np.any(mask != a[aspect]):
            result = True
            a[aspect] = mask
    return result

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
    trans = { "A": {}, "R": {} }
    for state, conds in states.items():
        # print(f"{state=} {conds=}")
        trans[state] = {}
        part = { a: True for a in "amsx" }
        for a, mask, next_state in conds:
            next_part = copy.deepcopy(part)
            next_part[a] = part[a] &  mask
            part[a]      = part[a] & ~mask
            trans[state][next_state] = next_part
    print(f"{trans=}")
    status = { s: { a: True if s == "in" else False for a in "amsx" } for s in trans }
    queue = collections.deque()
    queue.append("in")
    while queue:
        print(f"{queue[0]=}")
        astate = queue.popleft()
        for zstate, apart in trans[astate].items():
            zpart = { a: status[astate][a] & apart[a] for a in "amsx" }
            print(f"{apart=} {zpart=}")
            if merge_parts(status[zstate], zpart):
                queue.append(zstate)
    result = 1
    print(f"{status['A']=}")
    for aspect, mask in status["A"].items():
        print(f"{aspect=} {np.sum(mask)=}")
        result *= np.sum(mask)
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
