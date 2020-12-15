from functools import reduce
from typing import Callable, List

def _parse_input() -> List[str]:
    with open('day11/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def _adj_seat_decision(grid: List[str], i: int, j: int) -> str:
    if grid[i][j] == '.':
        return '.'
    
    checks = []
    if i == 0:
        if j > 0:
            checks.extend([(i, j-1), (i+1, j-1)])
        if j < len(grid[i]) - 1:
            checks.extend([(i, j+1), (i+1, j+1)])   
        checks.extend([(i+1, j)])
    elif i == len(grid) - 1:
        if j > 0:
            checks.extend([(i, j-1), (i-1, j-1)])
        if j < len(grid[i]) - 1:
            checks.extend([(i, j+1), (i-1, j+1)])
        checks.extend([(i-1, j)])
    else:
        if j > 0:
            checks.extend([(i, j-1), (i+1, j-1), (i-1, j-1)])
        if j < len(grid[i]) - 1:
            checks.extend([(i, j+1), (i+1, j+1), (i-1, j+1)])
        checks.extend([(i+1, j), (i-1, j)])
    
    count = 0
    for row, seat in checks:
        if grid[row][seat] == '#':
            count += 1
            
    if grid[i][j] == 'L' and count == 0:
        decision = '#'
    elif grid[i][j] == '#' and count >= 4:
        decision = 'L'
    else:
        decision = grid[i][j]

    return decision

def _vis_seat_decision(grid: List[str], i: int, j: int) -> str:
    if grid[i][j] == '.':
        return '.'
    
    def _check_seat(row: int, col: int) -> int:
        if grid[row][col] == 'L':
            result = 0
        elif grid[row][col] == '#':
            result = 1
        else:
            result = -1
        return result
    
    count = 0

    row = i - 1
    while row >= 0:
        decision = _check_seat(row, j)
        if decision >= 0:
            count += decision
            break
        row -= 1

    row = i + 1
    while row < len(grid):
        decision = _check_seat(row, j)
        if decision >= 0:
            count += decision
            break
        row += 1
            
    col = j - 1
    while col >= 0:
        decision = _check_seat(i, col)
        if decision >= 0:
            count += decision
            break
        col -= 1
    
    col = j + 1
    while col < len(grid[i]):
        decision = _check_seat(i, col)
        if decision >= 0:
            count += decision
            break
        col += 1
    
    row, col = i - 1, j - 1
    while row >= 0 and col >= 0:
        decision = _check_seat(row, col)
        if decision >= 0:
            count += decision
            break
        row -= 1
        col -= 1
    
    row, col = i - 1, j + 1
    while row >= 0 and col < len(grid[i]):
        decision = _check_seat(row, col)
        if decision >= 0:
            count += decision
            break
        row -= 1
        col += 1
    
    row, col = i + 1, j + 1
    while row < len(grid) and col < len(grid[i]):
        decision = _check_seat(row, col)
        if decision >= 0:
            count += decision
            break
        row += 1
        col += 1
    
    row, col = i + 1, j - 1
    while row < len(grid) and col >= 0:
        decision = _check_seat(row, col)
        if decision >= 0:
            count += decision
            break
        row += 1
        col -= 1
    
    if grid[i][j] == 'L' and count == 0:
        decision = '#'
    elif grid[i][j] == '#' and count >= 5:
        decision = 'L'
    else:
        decision = grid[i][j]

    return decision

def _occupy_seats(grid: List[str],
                  seat_decider: Callable[[List[str], int, int], str]) -> List[str]:
    next_grid = []
    for i in range(len(grid)):
        next_row = ''
        for j in range(len(grid[i])):
            next_row += seat_decider(grid, i, j)
        next_grid.append(next_row)
        
    return next_grid

def _count_seated(grid: List[str]) -> int:
    return reduce(
        lambda acc, row: acc + row.count('#'),
        grid,
        0
    )
    
def _solve(grid: List[str], seat_decider: Callable[[List[str], int, int], str]) -> int:
    last_grid, next_grid = grid.copy(), _occupy_seats(grid.copy(), seat_decider)
    
    while last_grid != next_grid:
        last_grid = next_grid.copy()
        next_grid = _occupy_seats(last_grid, seat_decider)
        
    return _count_seated(next_grid)
           
def part1(grid: List[str]) -> int:
    return _solve(grid, _adj_seat_decision)

def part2(grid: List[str]) -> int:
    return _solve(grid, _vis_seat_decision)
        
if __name__ == '__main__':
    print('AoC 2020 Day 11\n')
    grid = _parse_input()
    
    print('Solving part 1...')
    print(f'The answer is: {part1(grid)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(grid)}\n')
