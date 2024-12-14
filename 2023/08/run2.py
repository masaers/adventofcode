import sys
import re
import math

LR = {
    'L': 0,
    'R': 1,
}
def main():
    result = 0
    path = "input"
    # path = "example2"
    states = []
    with open(path, "r") as f:
        seq = [ LR[x] for x in f.readline() if x in LR ]
        for line in f.readlines():
            if match := re.search("(...) = \((...), (...)\)", line):
                states.append((match.group(1), (match.group(2), match.group(3))))
        trans = { k: v for k, v in states }
        state = [ s for s, _ in states if s.endswith("A") ]
        print(f"{seq=}")
        print(f"{state=}")
        while not all([ s.endswith("Z") for s in state ]):
            d = seq[result % len(seq)]
            state = [ trans[s][d] for s in state ]
            if sum([ s.endswith('Z') for s in state ]) > 1:
                print(f"{result=} {sum([ s.endswith('Z') for s in state ])}")
            result += 1
            # print(f"{state=}")
    print(result)
    
    
if __name__ == "__main__": main()
