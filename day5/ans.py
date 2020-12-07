import bisect
import math
from typing import List

SEAT_MULTIPLIER = 8

def _parse_input() -> List[str]:
    with open('day5/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def _read(seq: str, start: int, end: int, before_char: str) -> int:
    if len(seq) == 0:
        return start

    mid = start + (end - start) / 2
    if seq[0] == before_char:
        return _read(seq[1:], start, math.floor(mid), before_char)
    else:
        return _read(seq[1:], math.ceil(mid), end, before_char)

def _read_row(row: str) -> int:
    return _read(row, 0, 127, 'F')

def _read_col(col: str) -> int:
    return _read(col, 0, 8, 'L')

def read_pass(boarding_pass: str) -> int:
    return SEAT_MULTIPLIER * _read_row(boarding_pass[:7]) + _read_col(boarding_pass[7:])

def part1(boarding_passes: List[str]) -> int:
    mx = 0
    for bp in boarding_passes:
        _id =  read_pass(bp)
        if _id > mx:
            mx = _id

    return mx

def part2(boarding_passes: List[str]) -> int:
    ids = []
    for bp in boarding_passes:
        bisect.insort(ids, read_pass(bp))

    for i in range(len(ids) - 1):
        if ids[i+1] - ids[i] > 1:
            return ids[i] + 1

    return -1

if __name__ == '__main__':
    print('AoC 2020 Day 5\n')
    boarding_passes = _parse_input()

    print('Solving part 1...')
    print(f'The answer is: {part1(boarding_passes)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(boarding_passes)}\n')
