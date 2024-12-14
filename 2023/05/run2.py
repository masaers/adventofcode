import sys
import re

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
    for A, Z in values:
        for a, z, offset in ranges:
            if A < a <= Z:
                result.append(( A, a ))
                A = a
            if a <= A < z:
                result.append(( A+offset, min(Z, z)+offset ))
                A = min(Z, z)
        if A != Z:
            result.append(( A, Z ))
    return result

def main():
    sum = 0
    maps = {}
    source = ""
    target = ""
    ranges = []
    with open("input", "r") as f:
    # with open("example", "r") as f:
        for line in f.readlines():
            line = line[:-1]
            # print(line)
            if line.startswith("seeds:"):
                _, seeds = re.split(":\s*", line)
                seeds = [ int(x) for x in seeds.split(" ") ]
                seeds = [ (seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2) ]
                print(f"{seeds=}")
            elif re.match(".* map:", line):
                line, _ = re.split("\s*map:", line)
                source, target = re.split("-to-", line)
                ranges = []
                # print(f"{source=} {target=}")
            elif line:
                t, s, n = [ int(x) for x in re.split("\s+", line) if x ]
                ranges.append((s, s+n, t-s))
                # print(f"{s=} {t=} {n=}")
            else:
                # print(f"{source=} {target=} {ranges=}")
                maps[source] = { "target": target, "ranges": sorted(ranges) }
        if ranges:
            maps[source] = { "target": target, "ranges": sorted(ranges) }

    kind = "seed"
    values = seeds
    # print(maps)
    while kind != "location":
        data = maps[kind]
        # print(f"{kind=} {values=} {data=}")
        values = offset(values, data["ranges"])
        kind = data["target"]
    print(sorted(values)[0][0])

if __name__ == "__main__": main()
