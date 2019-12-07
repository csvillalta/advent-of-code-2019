from typing import List, Tuple

import argparse
import networkx as nx


def get_input(filepath: str) -> nx.Graph:
    with open(filepath, 'r') as f:
        input = [tuple(s.rstrip().split(')')) for s in f.readlines()]
    return nx.Graph(input)


def main():
    G = get_input(args.input)
    # Subtract 2 to exclude 'YOU' and 'SAN' nodes.
    print(nx.algorithms.shortest_path_length(G, 'YOU', 'SAN') - 2) 


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()