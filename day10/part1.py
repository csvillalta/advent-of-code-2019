from typing import Iterable, List, Tuple

import argparse
import math


def get_input(filepath: str) -> List[List[str]]:
    with open(filepath, 'r') as f:
        grid = []
        for line in f.readlines():
            grid.append([c for c in line.rstrip()])
        return grid


def gcd(a: int, b: int):
    """Euclidean Algorithm"""
    while b != 0:
        a, b = b, a%b
    return a


def get_asteroid_coordinates(map: List[List[str]]) -> List[Tuple[int, int]]:
    asteroid_coordinates = []
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == '#':
                asteroid_coordinates.append((col, row))
    return asteroid_coordinates


def reduce_coordinate(coordinate: Tuple[int, int]) -> Tuple[int, int]:
    divisor = abs(gcd(*coordinate))
    return (coordinate[0]/divisor, coordinate[1]/divisor)


def translate_coordinate(coordinate: Tuple[int, int], 
                         translation: Tuple[int, int]) -> Tuple[int, int]:
    return (coordinate[0]-translation[0], coordinate[1]-translation[1])


def count_visible_asteroids(asteroid: Tuple[int, int], 
                            asteroids: List[Tuple[int, int]]) -> int:
    translated_asteroids = [translate_coordinate(c, asteroid) 
                            for c in asteroids]
    translated_asteroids.remove((0, 0))
    reduced_asteroids = [reduce_coordinate(c) for c in translated_asteroids]
    return len(set(reduced_asteroids))


def main():
    map = get_input(args.input)
    asteroid_coordinates = get_asteroid_coordinates(map)
    max_coordinate = None
    max_asteroids = -math.inf
    for coordinate in asteroid_coordinates:
        asteroids = count_visible_asteroids(coordinate, asteroid_coordinates)
        if asteroids > max_asteroids:
            max_asteroids = asteroids
            max_coordinate = coordinate
    
    print(max_coordinate)
    print(max_asteroids)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()


