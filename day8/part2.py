from typing import Any, List, Tuple

import argparse
import math

import matplotlib.pyplot as plt


def get_input(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()


def split_list(alist: List[Any], interval: int) -> List[List[Any]]:
    return [alist[i: i+interval] for i in range(0, len(alist), interval)]


def convert_layer(flat_layer: List[str]) -> List[int]:
    return [int(c) for c in flat_layer]


def get_flat_layers(input: str, layer_size: int) -> List[List[int]]:
    flat_layers = split_list(input, layer_size)
    return [convert_layer(layer) for layer in flat_layers]


def get_color(color1: int, color2: int) -> int:
    return color2 if color1 == 2 else color1


def main():
    input = get_input(args.input)
    height, width = 6, 25
    layer_size = height*width
    flat_layers = get_flat_layers(input, layer_size)
    image = [2 for _ in range(layer_size)]
    for layer in flat_layers:
        image = [get_color(color1, color2) 
                 for color1, color2 in zip(image, layer)]
    image = split_list(image, width) 
    plt.imshow(image, cmap='binary')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()