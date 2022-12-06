from os import wait
from typing import Dict, List, Set


class Rucksack:
    compartment_1: str = ""
    compartment_2: str = ""
    priority: int = 0

    def __init__(self, line: str) -> None:
        size = len(line)
        self.compartment_1 = line[: size // 2]
        self.compartment_2 = line[size // 2 :]

        intersect = [x for x in self.compartment_1 if x in self.compartment_2]
        for x in set(intersect):
            if x.isupper():
                print(
                    "add",
                    x,
                    int.from_bytes(bytes(x, "utf8"), "little") - 38,
                )
                self.priority += int.from_bytes(bytes(x, "utf8"), "little") - 38
            else:
                print(
                    "add",
                    x,
                    int.from_bytes(bytes(x, "utf8"), "little") - 96,
                )
                self.priority += int.from_bytes(bytes(x, "utf8"), "little") - 96

    def get_all(self) -> str:
        return self.compartment_1 + self.compartment_2


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def main():
    lines = read_file("input.txt")
    rucksacks: List[Rucksack] = []
    for line in lines:
        rucksacks.append(Rucksack(line))

    score = 0
    for rucksack in rucksacks:
        score += rucksack.priority

    print(score)

    score = 0
    for i in range(0, len(rucksacks), 3):
        intersect = [
            x
            for x in rucksacks[i].get_all()
            if x in rucksacks[i + 1].get_all() and x in rucksacks[i + 2].get_all()
        ]
        for x in set(intersect):
            if x.isupper():
                score += int.from_bytes(bytes(x, "utf8"), "little") - 38
            else:
                score += int.from_bytes(bytes(x, "utf8"), "little") - 96

    print(score)


if __name__ == "__main__":
    main()
