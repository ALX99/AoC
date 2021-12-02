from typing import Dict, List


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def main():
    lines = read_file("input.txt")
    larger = 0

    for i, num in enumerate(lines):
        if i > 0 and int(num) > int(lines[i - 1]):
            larger += 1

    print(f"Answer for Q1 {larger}")

    larger = 0
    three_num: Dict[int, List[int]]
    three_num = {}

    for i, _ in enumerate(lines):
        three_num[i] = [int(num) for num in lines[i : i + 3]]

    for i, nums in three_num.items():
        if i > 0 and sum(nums) > sum(three_num[i - 1]):
            larger += 1

    print(f"Answer for Q2 {larger}")


if __name__ == "__main__":
    main()
