import sys
import numpy as np

def is_safe(x):
    D = np.diff(x)
    A = np.abs(D)
    return np.sign(np.max(D)) == np.sign(np.min(D)) and 0 < np.min(A) and np.max(A) <= 3
    
def main(path):
    safe = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            x = np.array([ int(x) for x in line[:-1].split(" ") ])
            # print(f"{i=} {x=}")
            if is_safe(x):
                safe.append(x)
            else:
                for j in range(len(x)):
                    _x = np.concatenate([x[:j], x[j+1:]])
                    # print(f"{j=} {_x=}")
                    if is_safe(_x):
                        safe.append(x)
                        break
    print(len(safe))
    # 286, 289 too low
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
