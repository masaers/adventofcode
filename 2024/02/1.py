import sys
import numpy as np

def main(path):
    safe = []
    unsafe = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            L = np.array([ int(x) for x in line[:-1].split(" ") ])
            D = np.diff(L)
            if np.sign(np.max(D)) != np.sign(np.min(D)):
                unsafe.append(L)
                continue
            A = np.abs(D)
            if np.min(A) == 0 or 3 < np.max(A):
                unsafe.append(L)
            else:
                safe.append(L)
    print(len(safe))

if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        main(path)
