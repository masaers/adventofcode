import sys
import re
import math

def intersection(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            yield a[i]
            i += 1
            j += 1
        else:
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
    return

def add_copies(copies, fcopies, sect):
    for i, _ in enumerate(sect):
        if i < len(fcopies):
            fcopies[i] += copies
        else:
            fcopies.append(copies)
    return fcopies

def offset(values, ranges):
    result = []
    for value in values:
        for a, z, offset in ranges:
            if a <= value < z:
                value += offset
                break
        result.append(value)
    return result

def main():
    result = 1
    lines = []
    # with open("example", "r") as f:
    with open("input", "r") as f:
        for line in f.readlines():
            line = [ x for x in re.split(":?\s+", line) if x ]
            # print(line)
            lines.append([ int("".join(line[1:])) ])
    data = [ x for x in zip(lines[0], lines[1]) ]
    # print(data)
    for t, d in data:
        q = math.sqrt(t**2 - 4*d)
        a = 0.5 * (t-q) + 1e-7
        z = 0.5 * (t+q) - 1e-7
        # print(f"{a=} {z=}")
        a = max(0, int(math.ceil(a)))
        z = min(t, int(math.floor(z)))
        # print(f"{a=} {z=}")
        r = 1 + z - a
        # print(f"{r=}")
        result *= r
    print(result)

    
if __name__ == "__main__": main()
