from typing import Dict, List


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def main():
    lines = read_file("input.txt")
    forward = 0
    up = 0
    down = 0
    for line in lines:
        if "forward" in line:
            forward += int(line.split(" ")[1])
        elif "up" in line:
            up += int(line.split(" ")[1])
        elif "down" in line:
            down += int(line.split(" ")[1])

    print(f"Answer for Q1 {forward*(down-up)}")

    aim = 0
    forward = 0
    down = 0
    for line in lines:
        if "forward" in line:
            res = int(line.split(" ")[1])
            forward += res
            down += aim * res
        elif "up" in line:
            aim -= int(line.split(" ")[1])
        elif "down" in line:
            aim += int(line.split(" ")[1])

    print(f"Answer for Q2 {forward*down}")


if __name__ == "__main__":
    main()
