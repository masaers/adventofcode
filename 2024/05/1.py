import sys
import numpy as np
import math
import re

def main(path):
    result = 0
    before = {}
    after = {}
    seqs = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            if m := re.match(r"([0-9]+)\|([0-9]+)", line):
                a = int(m.group(1))
                z = int(m.group(2))
                if z not in before: before[z] = []
                if a not in after:  after[a]  = []
                before[z].append(a)
                after[a].append(z)
            else:
                try:
                    seq = [ int(x) for x in line[:-1].split(",") ]
                    if seq:
                        seqs.append(seq)
                except:
                    pass
    for seq in seqs:
        ok = True
        for i in range(len(seq)):
            for j in range(i, len(seq)):
                if seq[j] in after and seq[i] in after[seq[j]]:
                    ok = False
                if seq[i] in before and seq[j] in before[seq[i]]:
                    ok = False
                if not ok: break
            if not ok: break
        if ok:
            result += seq[len(seq) // 2]
    print(result)
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
