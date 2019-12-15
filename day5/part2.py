from typing import List, Tuple

import argparse


def get_program(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        program = [int(i) for i in f.readline().split(',')]
    return program


def parse_opcode(opcode: int) -> Tuple[int, List[int]]:
    opcode = str(opcode)
    instruction = int(''.join(opcode[-2:]))
    modes = [int(d) for d in opcode[:-2]]
    modes = [0 for _ in range(3-len(opcode[:-2]))] + modes
    return instruction, modes


def run(program: List[int]):
    pos = 0
    instruction, modes = parse_opcode(program[pos])
    while instruction != 99:
        param1 = program[pos+1] if modes[2] else program[program[pos+1]]
        if pos+2 < len(program):
            param2 = program[pos+2] if modes[1] else program[program[pos+2]]
        if instruction == 1:
            program[program[pos+3]] = param1 + param2
            pos += 4
        elif instruction == 2:
            program[program[pos+3]] = param1 * param2
            pos += 4
        elif instruction == 3:
            user_input = int(input('Enter input: '))
            program[program[pos+1]] = user_input
            pos += 2
        elif instruction == 4:
            print(program[program[pos+1]])
            pos += 2
        elif instruction == 5:
            pos = param2 if param1 else pos + 3
        elif instruction == 6:
            pos = param2 if not param1 else pos + 3        
        elif instruction == 7:
            program[program[pos+3]] = param1 < param2
            pos += 4
        elif instruction == 8:
            program[program[pos+3]] = param1 == param2
            pos += 4
        instruction, modes = parse_opcode(program[pos])


def main():
    run(get_program(args.input))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()