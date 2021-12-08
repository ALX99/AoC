from typing import Dict, List, Set


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def determine_nums(signals: List[str], outputs: List[str]) -> int:
    signals_in_num: Dict[int, Set[str]] = {}
    for signal in signals:
        l = len(signal)
        if l == 2:
            signals_in_num[1] = {letter for letter in signal}
        elif l == 3:
            signals_in_num[7] = {letter for letter in signal}
        elif l == 4:
            signals_in_num[4] = {letter for letter in signal}
        elif l == 7:
            signals_in_num[8] = {letter for letter in signal}

    four_diff = signals_in_num[4].difference(signals_in_num[1])
    for letters in signals:
        l = len(letters)
        v = {letter for letter in letters}
        if l == 5:
            if v.issuperset(signals_in_num[1]):
                signals_in_num[3] = v
            elif v.issuperset(four_diff):
                signals_in_num[5] = v
            else:
                signals_in_num[2] = v
        elif l == 6:
            if not v.issuperset(signals_in_num[1]):
                signals_in_num[6] = v
            elif v.issuperset(four_diff):
                signals_in_num[9] = v
            else:
                signals_in_num[0] = v

    res = 0
    for output in outputs:
        for k, v in signals_in_num.items():
            if len(v) == len(output) and all([letter in v for letter in output]):
                res = (res * 10) + k

    return res


def main():
    lines = read_file("input.txt")

    signal_patterns: List[List[str]] = []
    digit_output: List[List[str]] = []
    for line in lines:
        res = line.split(" | ")
        signal_patterns.append(res[0].split(" "))
        digit_output.append(res[1].split(" "))

    cntr = 0
    for digits in digit_output:
        for digit in digits:
            l = len(digit)
            if l == 2 or l == 3 or l == 4 or l == 7:
                cntr += 1
    print(f"Answer to Q1 is {cntr}")
    res = 0
    for i in range(len(signal_patterns)):
        res += determine_nums(signal_patterns[i], digit_output[i])
    print(f"Answer to Q2 is {res}")


if __name__ == "__main__":
    main()
