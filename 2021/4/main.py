from typing import Dict, List


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line for line in file.readlines()]


def load_boards(lines: List[str]) -> List[List[List[int]]]:
    boards: List[List[List[int]]]
    boards = []
    board: List[List[int]]
    board = []
    for line in lines:
        nums = [int(i) for i in line.split(" ") if i.strip().isnumeric()]
        if line == "\n":
            if len(board) != 0:
                boards.append(board)
            board = []
        if len(nums) != 0:
            board.append(nums)

    boards.append(board)
    return boards


# bruteforce lol
def check_wins(
    draws: List[int], boards: List[List[List[int]]]
) -> List[List[List[int]]]:
    wins = []
    for board in boards:
        for bl in board:
            if all([num in draws for num in bl]):
                wins.append(board)
        for i, _ in enumerate(board[0]):
            if all([board[j][i] in draws for j, _ in enumerate(board)]):
                wins.append(board)
    return wins


def calc_points(draws: List[int], board: List[List[int]]) -> int:
    add = 0
    for bl in board:
        for num in bl:
            if num in draws:
                continue
            add += num
    return add * draws[len(draws) - 1]


def main():
    lines = read_file("input.txt")
    draw_order = [int(i) for i in lines[0].split(",")]
    boards = load_boards(lines[1 : len(lines)])

    draws = []
    for num in draw_order:
        draws.append(num)
        wins = check_wins(draws, boards)
        if len(wins) != 0:
            print(f"Answer to Q1 is {calc_points(draws,wins[0])}")
            break

    last_win = []
    new_boards = boards.copy()
    for num in draw_order:
        draws.append(num)
        wins = check_wins(draws, new_boards)
        for win in wins:
            last_win = win
            if win in new_boards:
                new_boards.remove(win)
        if len(new_boards) == 0:
            print(f"Answer to Q2 is {calc_points(draws,last_win)}")
            break



if __name__ == "__main__":
    main()
