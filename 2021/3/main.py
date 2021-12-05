from typing import Dict, List


def read_file(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]


def generator_string(bit_pos: int, generator_type: str, lines: List[str]) -> str:
    if len(lines) == 1:
        return lines[0]

    lines_dict: Dict[int, int]
    lines_dict = {}
    zero_counter = 0
    for i, line in enumerate(lines):
        lines_dict[i] = int(line[bit_pos])
        if lines_dict[i] == 0:
            zero_counter += 1
        else:
            zero_counter -= 1

    keep = 1 if generator_type == "oxygen" else 0
    if generator_type == "oxygen" and zero_counter > 0:
        keep = 0
    if generator_type == "co2" and zero_counter > 0:
        keep = 1

    lines_to_keep = []
    for k, v in lines_dict.items():
        if v == keep:
            lines_to_keep.append(lines[k])

    return generator_string(bit_pos + 1, generator_type, lines_to_keep)


def main():
    lines = read_file("input.txt")
    final_num = ""
    for i in range(len(lines[0])):
        zero_counter = 0
        for line in lines:
            if int(line[i]) == 0:
                zero_counter += 1
            else:
                zero_counter -= 1
        if zero_counter >= 1:
            final_num += "0"
        else:
            final_num += "1"

    print(f"Answer for Q1 {final_num}")
    oxygen = generator_string(0, "oxygen", lines)
    co2 = generator_string(0, "co2", lines)

    print(f"Oxygen: {oxygen}, co2: {co2}")


if __name__ == "__main__":
    main()
