from typing import Dict, List, Tuple


class Directory:
    path: str = ""
    dirs = []
    files: List[Tuple[str, int]] = []

    def __init__(self, path: str) -> None:
        self.path = path
        pass


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def main():
    lines = read_file("input.txt")

    dirs_and_sizes: Dict[str, int] = {}
    currPath = []
    for line in lines:
        if line[:4] == "$ cd":
            to = line[5:]
            if to == "/":
                currPath = ["/"]
            elif to == "..":
                currPath.pop()
            else:
                currPath.append(to)
        elif line[:3] == "dir":
            dirPath = "/".join(currPath)[1:]
            dirPath = dirPath if dirPath != "" else "/"

            # Make sure dir gets registered
            if dirPath not in dirs_and_sizes:
                dirs_and_sizes[dirPath] = 0
        elif line[:4] == "$ ls":
            continue
        else:
            dirPath = "/".join(currPath)[1:]
            dirPath = dirPath if dirPath != "" else "/"

            if dirPath in dirs_and_sizes:
                dirs_and_sizes[dirPath] += int(line.split(" ")[0])
            else:
                dirs_and_sizes[dirPath] = int(line.split(" ")[0])

    curr_disk_size = 0
    dirs_totsizes: Dict[str, int] = {}
    for d, s in dirs_and_sizes.items():
        curr_disk_size += s
        dir_size = s

        # Find other directorise contained within d1
        for d2, s2 in dirs_and_sizes.items():
            if len(d2) > len(d) and d2[: len(d)] == d:
                dir_size += s2

        dirs_totsizes[d] = dir_size

    lim = 100000
    score = 0
    for d, s in dirs_totsizes.items():
        if s <= lim:
            score += s

    print("part 1", score)

    fs_size = 70000000
    min = -1
    for d, s in dirs_totsizes.items():
        if (fs_size - curr_disk_size) + s > 30000000:
            if min == -1 or s < min:
                min = s

    print("part 2", min)


if __name__ == "__main__":
    main()
