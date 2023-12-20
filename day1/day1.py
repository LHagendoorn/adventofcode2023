import operator
import re


def find_number(inp: str):
    for x in inp:
        if x.isnumeric():
            return x



def solve_it():
    with open("./input.txt") as f:
        scrambled = f.readlines()
    total = 0
    for line in scrambled:
        for tupe_s, tupe_i in tupes:
            line = line.replace(tupe_s, tupe_i)
        total += int(f"{find_number(line)}{find_number(line[::-1])}")
    print(total)


# def find_number_regex(line):
#     matchstr = r"(\d)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
#     hits = re.findall(matchstr, line)
#     return hits

tupes = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
    *[(str(i), str(i)) for i in range(1,10)]
]

def find_number_two(line, reversed=False):
    numbs = []
    if reversed:
        line = line[::-1]
    for t, t2 in tupes:
        if reversed:
            t = t[::-1]
        if (idx := line.find(t)) >= 0:
            numbs.append((t2, idx))
    numbs = sorted(numbs, key=operator.itemgetter(1))
    return numbs[0][0]


def solve_it_two():
    with open("./input.txt") as f:
        scrambled = f.readlines()
    total = 0
    for line in scrambled:
        total += int(f"{find_number_two(line)}{find_number_two(line, True)}")

    print(total)


if __name__=="__main__":
    solve_it_two()