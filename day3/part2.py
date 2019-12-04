from typing import Dict, List, Tuple

import argparse
import math


def get_input(filepath: str) -> Tuple[List[str], List[str]]:
    with open(filepath, 'r') as f:
        first_wire = f.readline().rstrip('\n').split(',')
        second_wire = f.readline().split(',')
    return first_wire, second_wire


def process_path(points: Dict[Tuple[int, int], int], 
                 steps: int, path: str) -> int:
    # The next line only works in Python 3.6+ where dictiories remember order.
    start = list(points.keys())[-1] if points else (0, 0)

    direction = path[0]
    length = int(path[1:])

    if direction == "U":
        new_points = [(start[0], start[1]+i) for i in range(1, length+1)]
    elif direction == "D":
        new_points = [(start[0], start[1]-i) for i in range(1, length+1)]
    elif direction == "R":
        new_points = [(start[0]+i, start[1]) for i in range(1, length+1)]
    elif direction == "L":
        new_points = [(start[0]-i, start[1]) for i in range(1, length+1)]

    for point in new_points:
        steps += 1
        if point not in points:
            points[point] = steps
    return steps


def process_wire(wire: List[str]) -> Dict[Tuple[int, int], int]:
    steps = 0
    points = {}
    for path in wire:
        steps = process_path(points, steps, path)
    return points


def main():
    first_wire, second_wire = get_input(args.input)
    first_wire_points = process_wire(first_wire)
    second_wire_points = process_wire(second_wire)
    intersections = first_wire_points.keys() & second_wire_points.keys()
    print(min((first_wire_points[point] + second_wire_points[point] 
               for point in intersections)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()