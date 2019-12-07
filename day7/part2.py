from typing import List, Optional, Tuple

import argparse
import itertools


def get_program(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        program = [int(i) for i in f.readline().split(',')]
    return program


class Amplifier:

    def __init__(self, program: List[int], phase: int):
        self._program = program
        self._pos = 0
        self._phase = phase
        self._ran_once = False
        self.halted = False

    def _parse_opcode(self, opcode: int) -> Tuple[int, List[int]]:
        opcode = str(opcode)
        instruction = int(''.join(opcode[-2:]))
        modes = [int(d) for d in opcode[:-2]]
        modes = [0 for _ in range(3-len(opcode[:-2]))] + modes
        return instruction, modes

    def run(self, input_signal: int) -> Optional[int]:
        instruction, modes = self._parse_opcode(self._program[self._pos])
        while instruction != 99:
            if instruction not in [3, 4]:
                if modes[2]:
                    param1 = self._program[self._pos+1]
                else:
                    param1 = self._program[self._program[self._pos+1]]
                if modes[1]:
                    param2 = self._program[self._pos+2]
                else:
                    param2 = self._program[self._program[self._pos+2]]
            if instruction == 1:
                self._program[self._program[self._pos+3]] = param1 + param2
                self._pos += 4
            elif instruction == 2:
                self._program[self._program[self._pos+3]] = param1 * param2
                self._pos += 4
            elif instruction == 3:
                if self._ran_once:
                    self._program[self._program[self._pos+1]] = input_signal
                else:
                    self._program[self._program[self._pos+1]] = self._phase
                    self._ran_once = True
                self._pos += 2
            elif instruction == 4:
                self._pos += 2
                return self._program[self._program[self._pos-1]]
            elif instruction == 5:  
                self._pos = param2 if param1 else self._pos + 3
            elif instruction == 6:
                self._pos = param2 if not param1 else self._pos + 3        
            elif instruction == 7:
                self._program[self._program[self._pos+3]] = param1 < param2
                self._pos += 4
            elif instruction == 8:
                self._program[self._program[self._pos+3]] = param1 == param2
                self._pos += 4
            instruction, modes = self._parse_opcode(self._program[self._pos])
        self.halted = True


def run_amplifiers(program: List[int], phase_sequence: List[int]) -> int:
    input_signal = 0
    amplifiers = [Amplifier(program[:], phase_setting)
                  for phase_setting in phase_sequence]
    while not amplifiers[-1].halted:
        for amplifier in amplifiers:
            input_signal = amplifier.run(input_signal)
        if input_signal:
            output = input_signal
    return output


def main():
    program = get_program(args.input)
    print(max((run_amplifiers(program, phase_sequence) 
               for phase_sequence in itertools.permutations([5, 6, 7, 8, 9]))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filepath to input file.')
    args = parser.parse_args()
    main()