from typing import List, Tuple

import argparse
import networkx as nx


def get_input(filepath: str) -> nx.DiGraph:
    with open(filepath, 'r') as f:
        input = [tuple(s.rstrip().split(')')) for s in f.readlines()]
    return nx.DiGraph(input)


def main():
    G = get_input(args.input)
    print(sum((nx.algorithms.shortest_path_length(G, 'COM', node) 
               for node in G.nodes if node != 'COM')))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()