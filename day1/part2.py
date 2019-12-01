from typing import List

import argparse


def get_input(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        input = f.readlines()
    input = [int(x) for x in input]
    return input


def calculate_fuel_requirement(input: int) -> int:
    fuel_requirement = (input//3)-2
    if fuel_requirement > 0:
        return fuel_requirement + calculate_fuel_requirement(fuel_requirement)
    return 0


def main():
    input = get_input(args.input)
    fuel_requirements = [calculate_fuel_requirement(x) for x in input]
    print(sum(fuel_requirements))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Filepath to input file.")
    args = parser.parse_args()
    main()