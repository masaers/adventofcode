import sys
import re

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
                # print(f"{seeds=}")
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
    while kind != "location":
        data = maps[kind]
        # print(f"{kind=} {values=} {data=}")
        values = offset(values, data["ranges"])
        kind = data["target"]
    print(sorted(values)[0])

if __name__ == "__main__": main()
