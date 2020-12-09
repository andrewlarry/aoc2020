from typing import Dict, List, Optional, Set

def _parse_input() -> List[str]:
    with open('day8/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def inspect(instructions: List[str], index: int, acc: int, visited: Set[int]) -> int:
    if index in visited:
        return acc

    instruction, op = instructions[index].split(' ')
    sign = op[0]

    next_index = index + 1
    next_acc = acc
    if instruction == 'acc':
        if sign == '+':
            next_acc += int(op[1:])
        else:
            next_acc -= int(op[1:])
    elif instruction == 'jmp':
        if sign == '+':
            next_index = index + int(op[1:])
        else:
            next_index = index - int(op[1:])
    
    visited.add(index)
    return inspect(instructions, next_index, next_acc, visited)

def execute(instructions: List[str],index: int, acc: int, visited: Set[int], edited: bool) -> int:
    if index >= len(instructions):
        return acc
    
    if index in visited:
        return -1
    
    visited.add(index)

    instruction, op = instructions[index].split(' ')
    sign, num = op[0], int(op[1:].strip())

    if instruction == 'acc':
        if sign == '+':
            next_acc = acc + num
        else:
            next_acc = acc - num

        return execute(instructions, index + 1, next_acc, visited, edited)
    else:
        if sign == '+':
            next_index = index + num
        else:
            next_index = index - num

        indexes = {'jmp': next_index, 'nop': index + 1}
        other_instruction = 'jmp' if instruction == 'nop' else 'nop'

        attempt = execute(instructions, indexes[instruction], acc, visited, edited)
        if attempt == -1 and not edited:
            attempt = execute(instructions, indexes[other_instruction], acc, visited, True)
        
        return attempt

def part1(instructions: List[str]) -> int:
    return inspect(instructions, 0, 0, set())

def part2(instructions: List[str]) -> int:
    return execute(instructions, 0, 0, set(), dict())

if __name__ == '__main__':
    print('AoC 2020 Day 8\n')
    instructions = _parse_input()

    print('Solving part 1...')
    print(f'The answer is: {part1(instructions)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(instructions)}\n')
