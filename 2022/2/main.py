from os import wait
from typing import Dict, List, Set


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def main():
    scores = {"X": 1, "Y": 2, "Z": 3}

    win = {"X": "C", "Y": "A", "Z": "B"}
    draw = {"X": "A", "Y": "B", "Z": "C"}
    same = {"A": "X", "B": "Y", "C": "Z"}

    lose = {"A": "Z", "B": "X", "C": "Y"}
    pwin = {"A": "Y", "B": "Z", "C": "X"}

    score = 0
    lines = read_file("input.txt")
    for line in lines:
        split = line.split()
        score += scores.get(split[1])
        if win.get(split[1]) == split[0]:
            score += 6
        elif draw.get(split[1]) == split[0]:
            score += 3
    print(score)

    score = 0
    for line in lines:
        split = line.split()
        play = "VV"
        if split[1] == "X":
            play = lose.get(split[0])
        elif split[1] == "Y":
            play = same.get(split[0])
            score += 3
        else:
            score += 6
            play = pwin.get(split[0])
        score += scores.get(play)
    print(score)


if __name__ == "__main__":
    main()
