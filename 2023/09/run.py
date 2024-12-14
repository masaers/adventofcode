import sys
import re
import math

def main():
    result = 0
    path = "input"
    # path = "example"
    with open(path, "r") as f:
        for line in f.readlines():
            line = [ int(x) for x in re.split("\s+", line) if x ]
            # print(line)
            for d in range(1, len(line)):
                if all([ x == 0 for x in line[:-d] ]):
                    break
                for i in range(0, len(line)-d):
                    line[i] = line[i+1] - line[i]
                # print(f"{line=}")
            result += sum(line)
    print(result)
    
    
if __name__ == "__main__": main()
