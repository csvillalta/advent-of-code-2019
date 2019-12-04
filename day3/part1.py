from typing import List, Set, Tuple

import argparse
import math


def get_input(filepath: str) -> Tuple[List[str], List[str]]:
    with open(filepath, 'r') as f:
        first_wire = f.readline().rstrip('\n').split(',')
        second_wire = f.readline().split(',')
    return first_wire, second_wire


def process_path(start: Tuple[int, int], path: str) -> List[Tuple[int, int]]:
    direction = path[0]
    length = int(path[1:])

    if direction == "U":
        return [(start[0], start[1]+i) for i in range(1, length+1)]
    elif direction == "D":
        return [(start[0], start[1]-i) for i in range(1, length+1)]
    elif direction == "R":
        return [(start[0]+i, start[1]) for i in range(1, length+1)]
    elif direction == "L":
        return [(start[0]-i, start[1]) for i in range(1, length+1)]


def process_wire(wire: List[str]) -> Set[Tuple[int, int]]:
    start = (0, 0)
    points = []
    for path in wire:
        new_points = process_path(start, path)
        points += new_points
        start = points[-1]
    return set(points)


def manhattan_distance(first_point: Tuple[int, int], second_point: Tuple[int, int]) -> int:
    return abs(first_point[0]-second_point[0]) + abs(first_point[1]-second_point[1])


def main():
    first_wire, second_wire = get_input(args.input)
    first_wire_points = process_wire(first_wire)
    second_wire_points = process_wire(second_wire)
    intersection_points = first_wire_points.intersection(second_wire_points)

    closest_intersection = math.inf
    for point in intersection_points:
        distance = manhattan_distance(point, (0, 0))
        if distance < closest_intersection:
            closest_intersection = distance
    print(closest_intersection)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()