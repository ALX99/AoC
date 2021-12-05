from typing import Dict, List, Optional


class Point:
    x: int
    y: int

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x, self.y = x, y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def parse_coords(self, coord: str) -> None:
        split = coord.split(",")
        self.x = int(split[0])
        self.y = int(split[1])


class Line:
    orig: Point
    dest: Point

    def __init__(self, orig: Point, dest: Point) -> None:
        self.orig, self.dest = orig, dest

    def __str__(self) -> str:
        return f"{self.orig} -> {self.dest}"

    def plot_horz_or_vert(self) -> List[Point]:
        ret: List[Point] = []
        if self.orig.x == self.dest.x:
            for y in range(
                min(self.orig.y, self.dest.y), max(self.orig.y, self.dest.y) + 1
            ):
                ret.append(Point(self.orig.x, y))
            return ret
        if self.orig.y == self.dest.y:
            for x in range(
                min(self.orig.x, self.dest.x), max(self.orig.x, self.dest.x) + 1
            ):
                ret.append(Point(x, self.orig.y))
            return ret
        return []

    def plot_all(self) -> List[Point]:
        ret: List[Point] = self.plot_horz_or_vert()
        if ret != []:
            return ret

        x_diff = abs(self.orig.x - self.dest.x)
        y_diff = abs(self.orig.y - self.dest.y)
        if x_diff != y_diff:
            return ret

        x = self.orig.x
        y = self.orig.y
        ret.append(Point(x,y))
        while x != self.dest.x and y != self.dest.y:
            x += 1 if x < self.dest.x else -1
            y += 1 if y < self.dest.y else -1
            ret.append(Point(x, y))
        return ret


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def main():
    liness = read_file("input.txt")
    lines: List[Line] = []
    max_x, max_y = 0, 0
    for line in liness:
        split_line = line.split(" -> ")
        p1, p2 = Point(), Point()
        p1.parse_coords(split_line[0])
        p2.parse_coords(split_line[1])
        lines.append(Line(p1, p2))
        max_x = max(max_x, p1.x, p2.x)
        max_y = max(max_y, p1.y, p2.y)

    grid: List[List[int]] = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    at_least_2 = 0
    for line in lines:
        for point in line.plot_horz_or_vert():
            grid[point.y][point.x] += 1
            if grid[point.y][point.x] == 2:
                at_least_2 += 1

    print(f"Asnwer to Q1 is {at_least_2}")

    grid: List[List[int]] = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    at_least_2 = 0
    for line in lines:
        for point in line.plot_all():
            grid[point.y][point.x] += 1
            if grid[point.y][point.x] == 2:
                at_least_2 += 1

    print(f"Asnwer to Q2 is {at_least_2}")


if __name__ == "__main__":
    main()
