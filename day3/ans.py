from functools import reduce
from typing import List, Tuple

def _parse_input() -> List[str]:
    with open('day3/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def _traverse(grid: List[str], move: Tuple[int, int]) -> int:
    right, down = move
    horz, vert = 0, 0

    tree_count = 0
    while vert < len(grid):
        if grid[vert][horz] == '#':
            tree_count += 1
        vert += down
        horz = (horz + right) % len(grid[0])

    return tree_count

def part1(grid: List[str]) -> int:
    return _traverse(grid, (3, 1))

def part2(grid: List[str]) -> int:
    return reduce(
        lambda acc, mv: acc * _traverse(grid, mv),
        [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2)],
        1
    )

if __name__ == '__main__':
    print('AoC 2020 Day 3\n')
    grid = _parse_input()

    print('Solving part 1...')
    print(f'The answer is: {part1(grid)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(grid)}\n')
