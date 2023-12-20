import math
import re
from collections import defaultdict

import numpy as np


def parse_input():
    with open("./input.txt") as f:
        inputlines = f.read().splitlines()
    return inputlines


def solve_part_1(input_lines):
    grid = np.array([list(i) for i in inputlines]).astype(str)
    boolgrid = np.copy(grid)
    boolgrid[boolgrid == "."] = "0"
    boolgrid = ~np.char.isnumeric(boolgrid)

    parts = 0
    for idx, line in enumerate(inputlines):
        for number in re.finditer(r'(\d+)', line):
            span = number.span()
            print(grid[max(idx-1, 0):min(idx+2, 139), max(0, span[0]-1):min(139, span[1]+1)])
            if boolgrid[max(idx-1, 0):min(idx+2, 139), max(0, span[0]-1):min(139, span[1]+1)].any():
                parts += int(number.group())
    print(parts)


def solve_part_2(input_lines):
    grid = np.array([list(i) for i in input_lines]).astype(str)
    boolgrid = np.copy(grid)
    boolgrid = np.where(boolgrid == "*", True, False)
    idxgrid = np.arange(0, math.prod(boolgrid.shape)).reshape(boolgrid.shape)


    gears = defaultdict(list)
    for idx, line in enumerate(input_lines):
        for number in re.finditer(r'(\d+)', line):
            span = number.span()
            print(grid[max(idx - 1, 0):min(idx + 2, 139), max(0, span[0] - 1):min(139, span[1] + 1)])
            boolsection = boolgrid[max(idx - 1, 0):min(idx + 2, 139), max(0, span[0] - 1):min(139, span[1] + 1)]
            for k in idxgrid[max(idx - 1, 0):min(idx + 2, 139), max(0, span[0] - 1):min(139, span[1] + 1)][boolsection]:
                gears[k].append(int(number.group()))

    dupes_only = sum([math.prod(v) for k,v in gears.items() if len(v) == 2])

    print(dupes_only)

if __name__ == "__main__":
    inputlines = parse_input()
    solve_part_2(inputlines)