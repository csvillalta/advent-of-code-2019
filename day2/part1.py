from typing import List

import argparse


def get_input(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        input = [int(x) for x in f.readline().split(',')]
    return input


def process(input: List[int]) -> int:
    input[1] = 12
    input[2] = 2
    pos = 0
    while input[pos] != 99:
        if input[pos] == 1:
            input[input[pos+3]] = input[input[pos+1]] + input[input[pos+2]]
            pos += 4
        elif input[pos] == 2:
            input[input[pos+3]] = input[input[pos+1]] * input[input[pos+2]]
            pos += 4
    return input[0]


def main():
    print(process(get_input(args.input)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()