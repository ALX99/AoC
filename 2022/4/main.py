from os import wait
from typing import Dict, List, Set


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


class Elf:
    start: int = 0
    end: int = 0

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"


def main():
    lines = read_file("input.txt")
    elves: List[List[Elf]] = [[]]
    for i, line in enumerate(lines):
        if i >= len(elves):
            elves.append([])
        for res in line.split(","):
            s = res.split("-")
            elves[i].append(Elf(int(s[0]), int(s[1])))

    score = 0
    for i, elf in enumerate(elves):
        if elf[0].start >= elf[1].start and elf[0].end <= elf[1].end:
            score += 1
        elif elf[1].start >= elf[0].start and elf[1].end <= elf[0].end:
            score += 1
    print(score)

    score = 0
    for i, elf in enumerate(elves):
        e1 = [i for i in range(elf[0].start, elf[0].end + 1)]
        e2 = [i for i in range(elf[1].start, elf[1].end + 1)]
        if any([i for i in e1 if i in e2]):
            score += 1
    print(score)


if __name__ == "__main__":
    main()
