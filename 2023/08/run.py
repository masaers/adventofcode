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
    # path = "example"
    states = []
    with open(path, "r") as f:
        seq = [ LR[x] for x in f.readline() if x in LR ]
        # print(f"{seq=}")
        for line in f.readlines():
            # print(f"{line=}")
            if match := re.search("(...) = \((...), (...)\)", line):
                # print(f"{match.group(1)=} {match.group(2)=} {match.group(3)=}")
                states.append((match.group(1), (match.group(2), match.group(3))))
        trans = { k: v for k, v in states }
        goal = "ZZZ" #states[-1][0]
        state = "AAA" # states[0][0]
        print(f"{state=} {goal=}")
        while state != goal:
            # print(f"{state=} {result=} {seq[result % len(seq)]=}")
            state = trans[state][seq[result % len(seq)]]
            result += 1
    print(result)

    
if __name__ == "__main__": main()
