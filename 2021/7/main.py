import math
from typing import Dict, List


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def part1(crab_posses: List[int]):
    crab_posses.sort()
    median = crab_posses[len(crab_posses) // 2]
    energy = sum([abs(crab - median) for crab in crab_posses])
    print(f"Asnwer to Q1 is {energy}")


def part2(crab_posses: List[int]):
    max_pos = max(crab_posses)
    hm: Dict[int, int] = {}

    least = 99999999
    pos = 0
    for i in range(max_pos + 1):
        hm[i] = 0
        for crab in crab_posses:
            steps = abs(crab - i)
            hm[i] += ((steps * steps) + steps) // 2
            if hm[i] > least:
                break
        if hm[i] < least:
            least = hm[i]
            pos = i

    print(f"Crabs move to {pos} with a cost of {least}")
    print(f"Asnwer to Q2 is {least}")


def main():
    lines = read_file("input.txt")
    crab_posses = [int(i) for i in lines[0].split(",")]
    part1(crab_posses.copy())
    part2(crab_posses.copy())


if __name__ == "__main__":
    main()
