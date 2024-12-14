import sys
import numpy as np
import math
import re
import copy
import collections
import functools
import scipy

def square_patches(matrix, shape=(2, 2), pad=0):
    if pad:
        matrix = np.pad(matrix, pad)
    sv = tuple(np.subtract(matrix.shape, shape) + 1) + shape
    view = np.lib.stride_tricks.as_strided(matrix, sv, matrix.strides * 2)
    view = view.reshape((-1,) + shape)

def main(path):
    result = 0
    robots = []
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if m := re.match(r"p=([0-9]+),([0-9]+) v=([-0-9]+),([-0-9]+)", line):
                robots.append([ int(m.group(x)) for x in range(1,5) ])
    # print(f"{robots=}")
    X = 101 
    Y = 103 
    # X = 11
    # Y = 7
    T = 100
    densities = []
    kernel = np.array([ [ -1, -1, -1 ],
                        [ -1,  9, -1 ],
                        [ -1, -1, -1 ] ])
    for T in range(X*Y):
        m = np.zeros((X, Y))
        for x, y, dx, dy in robots:
            m[(x+T*dx) % X, (y+T*dy) % Y] = 1
        c = scipy.signal.convolve2d(m, kernel)
        densities.append((np.sum(c), T))
    for i, (v, T) in enumerate(reversed(sorted(densities))):
        pos = [ ( (x+T*dx) % X, (y+T*dy) % Y ) for x, y, dx, dy in robots ]
        posi = set(pos)
        print(f"{T=} {v=}")
        for y in range(Y):
            print("".join("#" if (x,y) in posi else "." for x in range(X)))
        if i == 0:
            break
    return result
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path == "-":
            path = "/dev/stdin"
        print(main(path))
