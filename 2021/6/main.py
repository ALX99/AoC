from typing import Dict, List


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]

def calc_fishes(days: int, lantern_fishes: Dict[int, int]) -> int:
    for _ in range(days):
        new_fishes = lantern_fishes[0]
        lantern_fishes[0] = 0
        for i in range(1, 9):
            fish_count = lantern_fishes[i]
            if fish_count == 0:
                continue
            lantern_fishes[i] -= fish_count
            lantern_fishes[i - 1] += fish_count
        lantern_fishes[8] += new_fishes
        lantern_fishes[6] += new_fishes
    res = 0
    for _, v in lantern_fishes.items():
        res += v
    return res

def main():
    lines = read_file("input.txt")

    lantern_fishes: Dict[int, int] = {}
    for i in range(9):
        lantern_fishes[i] = 0

    for i in lines[0].split(","):
        lantern_fishes[int(i)] += 1

    print(f"Asnwer to Q1 is {calc_fishes(80,lantern_fishes.copy())}")
    print(f"Asnwer to Q2 is {calc_fishes(256,lantern_fishes.copy())}")


if __name__ == "__main__":
    main()
