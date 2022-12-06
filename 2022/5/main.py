import re
from os import wait
from typing import Dict, List, Set


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def uhh(crates: List[str]) -> Dict[int, List[str]]:
    # World's best parsing
    boxes: Dict[int, List[str]] = {}
    for entry in crates:
        count = 1
        wtCount = 0
        skip = False
        hmm = entry.split(" ")
        for i, en in enumerate(hmm):
            if skip:
                skip = False
                continue
            if en == "":
                if i == 0:
                    count -= 1
                wtCount += 1
                if wtCount % 3 == 0:
                    count += 1
            else:
                if count in boxes:
                    boxes[count].append(en)
                else:
                    boxes[count] = [en]
                if i + 1 < len(hmm) and hmm[i + 1] == "":
                    skip = True
                count += 1
    for k in boxes:
        boxes[k].reverse()
    return boxes


def main():
    lines = read_file("input.txt")
    crates: List[str] = []

    for line in lines:
        if line == "":
            break
        crates.append(line)

    cols = 0
    for en in crates[-1].split(" "):
        try:
            cols = int(en)
        except Exception:
            continue
    print(f"cols: {cols}")

    print("part one")
    boxes = uhh(crates[:-1])

    ok = False
    for line in lines:
        if not ok and line == "":
            ok = True
        elif ok:
            ms = re.findall(r"\d+", line)
            print(f"move {ms[0]} from {int(ms[1])} to {int(ms[2])}")
            for _ in range(int(ms[0])):
                boxes[int(ms[2])].append(boxes[int(ms[1])].pop())

    for k, v in boxes.items():
        print(k, v[-1])

    print("part two")
    boxes = uhh(crates[:-1])

    ok = False
    for line in lines:
        if not ok and line == "":
            ok = True
        elif ok:
            ms = re.findall(r"\d+", line)
            print(f"move {ms[0]} from {int(ms[1])} to {int(ms[2])}")
            tmp = []
            for _ in range(int(ms[0])):
                tmp.append(boxes[int(ms[1])].pop())
            tmp.reverse()
            boxes[int(ms[2])].extend(tmp)

    for k, v in boxes.items():
        print(k, v[-1])


if __name__ == "__main__":
    main()
