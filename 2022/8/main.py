from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def main():
    lines = read_file("input.txt")

    forest: List[List[int]] = []
    for line in lines:
        tree_line: List[int] = []
        for tree_height in line:
            tree_line.append(int(tree_height))
        forest.append(tree_line)

    visible_count = 0
    h = len(forest)
    w = len(forest[0])
    for y in range(h):
        row = forest[y]
        for x in range(w):
            col = [forest[i][x] for i in range(h)]
            tree_height = forest[y][x]

            if (
                all(t < tree_height for t in row[:x])
                or all(t < tree_height for t in row[x + 1 :])
                or all(t < tree_height for t in col[:y])
                or all(t < tree_height for t in col[y + 1 :])
            ):
                visible_count += 1

    print(visible_count)

    highscore = 0
    for y in range(h):
        row: List[int] = forest[y]
        for x in range(w):
            col = [forest[i][x] for i in range(h)]
            tree_height = forest[y][x]
            score = []

            def lol(a: List[int], l: int, h: int) -> int:
                c = 0
                # Check left side
                for i, t in enumerate(a):
                    if t >= h:
                        break
                    c = i + 1 if i == l else i + 2
                return c

            # Left
            score.append(lol(reversed(row[:x]), len(row[:x]) - 1, tree_height))
            # Right
            score.append(lol(row[x + 1 :], len(row[x + 1 :]) - 1, tree_height))
            # Above
            score.append(lol(reversed(col[:y]), len(col[:y]) - 1, tree_height))
            # Below
            score.append(lol(col[y + 1 :], len(col[y + 1 :]) - 1, tree_height))

            res = 1
            for i in score:
                res *= i
            highscore = max(highscore, res)

    print(highscore)


if __name__ == "__main__":
    main()
