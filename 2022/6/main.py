from os import wait
from collections import deque
from typing import Deque, Dict, List, Set


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def main():
    lines = read_file("input.txt")

    a: Deque[str] = deque()
    for c in lines[0][:4]:
        a.append(c)

    i = 0
    for i, c in enumerate(lines[0][4:]):
        a.popleft()
        a.append(c)
        if len(a) == len(set(a)):
            i = i + 5
            break
    print("part one", i)

    a: Deque[str] = deque()
    for c in lines[0][:14]:
        a.append(c)

    i = 0
    for i, c in enumerate(lines[0][14:]):
        a.popleft()
        a.append(c)
        if len(a) == len(set(a)):
            i = i + 15
            break
    print("part two", i)


if __name__ == "__main__":
    main()
