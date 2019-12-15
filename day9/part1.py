from typing import List, Tuple

import argparse


def get_program(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        program = [int(i) for i in f.readline().split(',')]
        # TODO: Increase memory dynamically instead.
        program += [0 for _ in range(100000)]
    return program


def parse_opcode(opcode: int) -> Tuple[int, List[int]]:
    opcode = str(opcode)
    instruction = int(''.join(opcode[-2:]))
    modes = [int(d) for d in opcode[:-2]]
    modes = [0 for _ in range(3-len(opcode[:-2]))] + modes
    return instruction, modes


def get_param(
    program: List[int], 
    pos: int, 
    relative_base: int, 
    param_pos: int, 
    mode: int) -> int:
    if param_pos != 3:
        if mode == 0:
            return program[program[pos+param_pos]]
        elif mode == 1:
            return program[pos+param_pos]
        elif mode == 2:
            return program[relative_base+program[pos+param_pos]]
    else:
        if mode == 0 or mode == 1:
            return program[pos+param_pos]
        elif mode == 2:
            return relative_base+program[pos+param_pos]

def run(program: List[int]):
    relative_base = 0
    pos = 0
    instruction, modes = parse_opcode(program[pos])
    while instruction != 99:
        param1 = get_param(program, pos, relative_base, 1, modes[2])
        if pos+2 < len(program):
            param2 =  get_param(program, pos, relative_base, 2, modes[1])
        if pos+3 < len(program):
            param3 =  get_param(program, pos, relative_base, 3, modes[0])
            
        if instruction == 1:
            program[param3] = param1 + param2
            pos += 4
        elif instruction == 2:
            program[param3] = param1 * param2
            pos += 4
        elif instruction == 3:
            user_input = int(input('Enter input: '))
            if modes[2] == 2:
                program[relative_base+program[pos+1]] = user_input
            else:
                program[program[pos+1]] = user_input
            pos += 2
        elif instruction == 4:
            if modes[2] == 2:
                print(program[relative_base+program[pos+1]])
            else:
                print(program[program[pos+1]])
            pos += 2
        elif instruction == 5:
            pos = param2 if param1 else pos + 3
        elif instruction == 6:
            pos = param2 if not param1 else pos + 3        
        elif instruction == 7:
            program[param3] = param1 < param2
            pos += 4
        elif instruction == 8:
            program[param3] = param1 == param2
            pos += 4
        elif instruction == 9:
            relative_base += param1
            pos += 2

        instruction, modes = parse_opcode(program[pos])


def main():
    run(get_program(args.input))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()