import sys
import re
import math
import numpy as np

def search(string, groups, memo):
    # print(f"search({string=}, {groups=})")
    if not string:
        return 0 if groups else 1
    if not groups:
        return 0 if "#" in string else 1
    if len(string) < groups[0]:
        return 0
    m = memo.get((string, len(groups)))
    if m is not None:
        return m
    if string[0] == ".":
        return search(string[1:], groups, memo)
    # print(f"{string[:groups[0]].replace('?', '#')=}")
    result = 0
    if string[0] == "?":
        result += search(string[1:], groups, memo)
    if string[:groups[0]].replace("?", "#") == "#" * groups[0]:
        if groups[0] == len(string) and len(groups) == 1:
            result += 1
        if groups[0] < len(string) and string[groups[0]] != "#":
            result += search(string[groups[0]+1:], groups[1:], memo)
    # print(f"{result=}")
    memo[(string, len(groups))] = result
    return result
        
def main(path):
    result = 0
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            # print(f"{line=}")
            string, groups = line.split(" ")
            # n = search(string, [ int(x) for x in groups.split(",") ], {})
            n = search("?".join([ string ] * 5), [ int(x) for x in groups.split(",") ] * 5, {})
            # print(f"{n=}")
            result += n
    print(result)
    
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        main(path)
