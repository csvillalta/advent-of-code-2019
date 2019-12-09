from typing import Iterable

import argparse
import math


def get_input(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()


def get_flat_layers(input: str, layer_size: int) -> Iterable[str]:
    return (input[i:i+layer_size] for i in range(0, len(input), layer_size))


def main():
    input = get_input(args.input)
    flat_layers = get_flat_layers(input, 6*25)
    fewest_zeroes = math.inf
    best_layer = None
    for layer in flat_layers:
        layer_zeroes = layer.count('0')
        if layer_zeroes < fewest_zeroes:
            fewest_zeroes = layer_zeroes
            best_layer = layer
    print(best_layer.count('1') * best_layer.count('2'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()