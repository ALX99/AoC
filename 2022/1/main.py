from typing import Dict, List, Set


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def main():
    lines = read_file("input.txt")

    curr = 0
    carry = []
    for line in lines:
        if line == "":
            carry.append(curr)
            curr = 0
            continue
        curr += int(line)

    carry.sort()
    print("first part", carry[-1])
    print("second part", sum(carry[-3:]))


if __name__ == "__main__":
    main()
