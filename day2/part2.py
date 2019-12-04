from typing import List, Tuple

import argparse


def get_memory(memory_path: str) -> List[int]:
    with open(memory_path, 'r') as f:
        memory = [int(x) for x in f.readline().split(',')]
    return memory


def run_program(memory: List[int], noun: int, verb: int) -> int:
    memory[1] = noun
    memory[2] = verb
    pos = 0
    while memory[pos] != 99:
        addr1, addr2, addr3 = memory[pos+1], memory[pos+2], memory[pos+3]
        if memory[pos] == 1:
            memory[addr3] = memory[addr1] + memory[addr2]
        elif memory[pos] == 2:
            memory[addr3] = memory[addr1] * memory[addr2]
        pos += 4
    return memory[0]


def find_parameters(input_path: str, desired_output: int) -> Tuple[int, int]:
    for noun in range(100):
        for verb in range(100):
            output = run_program(get_memory(input_path), noun, verb)
            if output == desired_output:
                return noun, verb


def main():
    noun, verb = find_parameters(args.input, 19690720)
    print(100 * noun + verb)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()

