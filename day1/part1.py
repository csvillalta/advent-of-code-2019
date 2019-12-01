from typing import List

import argparse


def get_input(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        input = f.readlines()
    input = [int(x) for x in input]
    return input


def main():
    input = get_input(args.input)
    fuel_requirements = [(x//3)-2 for x in input]
    print(sum(fuel_requirements))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Filepath to input file.")
    args = parser.parse_args()
    main()