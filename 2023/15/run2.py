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
    hmap = {}
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            # print(f"{line=}")
            for cmd in line[:-1].split(","):
                # print(f"{cmd=}")
                if m := re.match("([^=]*)=([0-9]+)", cmd):
                    # print(f"{m.group(1)=} {m.group(2)=}")
                    h = hash(m.group(1))
                    if h in hmap:
                        found = False
                        for i, (x, f) in enumerate(hmap[h]):
                            if x == m.group(1):
                                hmap[h][i] = ( m.group(1), int(m.group(2)) )
                                found = True
                                break
                        if not found:
                            hmap[h].append((m.group(1), int(m.group(2))))
                    else:
                        hmap[h] = [ ( m.group(1), int(m.group(2)) ) ]
                elif m := re.match("(.*)-", cmd):
                    h = hash(m.group(1))
                    if h in hmap:
                        idx = []
                        for i, x in enumerate(hmap[h]):
                            if x[0] == m.group(1):
                                idx.append(i)
                        for i in reversed(idx):
                            hmap[h] = hmap[h][:i] + hmap[h][i+1:]
                else:
                    print(f"ERROR!")        
                # print(f"{hmap=}")
        for i, xs in hmap.items():
            for j, x in enumerate(xs):
                # print(f"{i=} {j=} {x[1]=}")
                result += (i+1) * (j+1) * x[1]
                # print(f"{result=}")
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
