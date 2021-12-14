# Seven-segment display
# https://github.com/mjspeck/advent-of-code-21/blob/main/day_08.py

import sys
from copy import copy
from collections import defaultdict, namedtuple
from typing import Dict, List, Set, Tuple

FILE = sys.argv[1]
LETTERS = "abcdefg"

DIGITS = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

def get_entry_letter_mappings(single_input: List[str]) -> Dict[str, str]:

    """
    steps:
    identify a: in 3-digit number but not in 2-digit number
    identify d: in all 5-digit numbers, but only in 2 6-digit numbers
    identify c: only letter in two 5-digit and two 6-digit numbers
    identify f: other letter in 2-digit number
    identify g: only other number in all 6-digit and 5-digit numbers that isn't a
    identify b: in all 6-digit and only 1 5-digit
    identify e: only one remaining
    """
    remaining_letters = copy(LETTERS)
    true_mappings = {}

    lens: defaultdict[int, List[Set]] = defaultdict(list)

    for i in single_input:
        lens[len(i)].append(set(i))

    assert len(lens[2]) == 1, "failed for lens 2"
    assert len(lens[3]) == 1, "failed for lens 3"
    assert len(lens[4]) == 1, "failed for lens 4"
    assert len(lens[5]) == 3, "failed for lens 5"
    assert len(lens[6]) == 3, "failed for lens 6"
    assert len(lens[7]) == 1, "failed for lens 7"

    # identify a: in 3-digit number but not in 2-digit number

    three_minus_2 = lens[3][0] - lens[2][0]
    assert len(three_minus_2) == 1, "identifying a failed"
    true_mappings["a"] = three_minus_2.pop()
    remaining_letters = remaining_letters.replace(true_mappings["a"], "")

    # identify d: in all 5-digit numbers, but only in 2 6-digit numbers
    for letter in remaining_letters:
        in_all_5 = all([letter in thing for thing in lens[5]])
        in_two_2 = len(list(filter(lambda x: letter in x, lens[6]))) == 2
        if in_all_5 and in_two_2:
            true_mappings["d"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["d"], "")

    # identify c: only letter in two 5-digit and two 6-digit numbers
    for letter in remaining_letters:
        in_two_5 = len(list(filter(lambda x: letter in x, lens[5]))) == 2
        in_two_6 = len(list(filter(lambda x: letter in x, lens[6]))) == 2

        if in_two_5 and in_two_6:
            true_mappings["c"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["c"], "")

    # identify f: other letter in 2-digit number

    two_letter = copy(lens[2]).pop()
    for letter in remaining_letters:
        if letter in two_letter:
            true_mappings["f"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["f"], "")

    # identify g: only other number in all 6-digit and 5-digit numbers that isn't a

    for letter in remaining_letters:
        in_all_6 = all([letter in x for x in lens[6]])
        in_all_5 = all([letter in x for x in lens[5]])

        if in_all_6 and in_all_5:
            true_mappings["g"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["g"], "")

    # identify b: in all 6-digit and only 1 5-digit

    for letter in remaining_letters:
        in_all_6 = all([letter in x for x in lens[6]])
        in_one_5 = len(list(filter(lambda x: letter in x, lens[5]))) == 1

        if in_all_6 and in_one_5:
            true_mappings["b"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["b"], "")

    # identify e: last remaining
    true_mappings["e"] = remaining_letters
    reversed_mappings = {value: key for (key, value) in true_mappings.items()}
    return reversed_mappings

def map_output_to_digit(output: str, mapping: Dict[str, str]) -> str:
    correct_output = ""
    for letter in output:
        correct_output += mapping[letter]

    correct_output_sorted = "".join(sorted(correct_output))
    digit = DIGITS[correct_output_sorted]
    return digit

def parse_input(input_strings: List[str]) -> Tuple[List[List[str]], List[List[str]]]:
    inputs, outputs = list(zip(*map(lambda x: x.split(" | "), input_strings)))
    inputs = list(map(lambda x: x.split(), inputs))
    outputs = list(map(lambda x: x.split(), outputs))
    return inputs, outputs

def solve_puzzle_2(inputs: List[List[str]], outputs: List[List[str]]) -> int:
    outputs_sum = 0
    for input_sequence, output_sequence in zip(inputs, outputs):
        mapping = get_entry_letter_mappings(input_sequence)
        full_output = ""
        for output in output_sequence:
            digit = map_output_to_digit(output, mapping)
            full_output += digit
        output_num = int(full_output)
        outputs_sum += output_num
    return outputs_sum

if __name__ == "__main__":

    with open(FILE) as f:
        data = f.readlines()
    inputs, outputs = parse_input(data)

    puzzle_2_answer = solve_puzzle_2(inputs, outputs)
    print(f"Answer for puzzle 1: {puzzle_2_answer}")
