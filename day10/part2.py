from typing import Dict, Iterable, List, Tuple

import argparse
import heapq
import math


def get_input(filepath: str) -> List[List[str]]:
    with open(filepath, 'r') as f:
        grid = []
        for line in f.readlines():
            grid.append([c for c in line.rstrip()])
        return grid


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def translate(self, x_translate: int, y_translate: int):
        self.x -= x_translate
        self.y -= y_translate

    
    def get_angle(self):
        return math.degrees(math.atan2(self.x, -self.y)) % 360

    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)


def get_asteroid_coordinates(map: List[List[str]]) -> List[Coordinate]:
    asteroid_coordinates = []
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == '#':
                asteroid_coordinates.append(Coordinate(col, row))
    return asteroid_coordinates


def group_coordinates_by_angle(
    asteroid_coordinates: List[Coordinate]) -> Dict[float, List[Coordinate]]:
    angle_dict = {}
    for coordinate in asteroid_coordinates:
        coordinate_angle = coordinate.get_angle()
        if coordinate_angle in angle_dict:
            heapq.heappush(angle_dict[coordinate_angle], coordinate)
        else:
            angle_dict[coordinate_angle] = [coordinate]
    
    return angle_dict


def main():
    map = get_input(args.input)
    asteroid_coordinates = get_asteroid_coordinates(map)
    for coordinate in asteroid_coordinates:
        # (28, 29) is the best location found in part1.py
        coordinate.translate(28, 29)

    angle_dict = group_coordinates_by_angle(asteroid_coordinates)
    count = 0
    answer = None
    while True:
        for angle in sorted(angle_dict.keys()):
            coordinates = angle_dict[angle]
            if len(coordinates) == 0:
                continue
            else:
                answer = heapq.heappop(angle_dict[angle])
                count += 1
                if count == 200:
                    answer.translate(-28, -29)
                    print(answer.x*100 + answer.y)
                    exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()


