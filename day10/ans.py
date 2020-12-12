from collections import Counter
from functools import lru_cache
from typing import List, Tuple

def _parse_input() -> List[int]:
    with open('day10/input.txt') as f:
        return [int(ln.strip()) for ln in f.readlines()]

def _sort_ratings(ratings: List[int]) -> Tuple[int]:
    s = sorted([0] + ratings)
    s.append(s[-1] + 3)
    return tuple(s)

@lru_cache(maxsize=None)
def _traverse(ratings: List[int], index: int) -> int:
    if index == len(ratings) - 1:
        return 1
    
    count = 0
    next_index = index + 1
    while next_index < len(ratings) and ratings[next_index] - ratings[index] <= 3:
        count += _traverse(ratings, next_index)
        next_index += 1
    
    return count
    
def part1(ratings: List[int]) -> int:
    chain = _sort_ratings(ratings)
    
    counts = Counter()
    for i in range(1, len(chain)):
        diff = chain[i] - chain[i-1]
        counts[diff] += 1
    
    return counts[1] * counts[3]

def part2(ratings: List[int]) -> int:
    return _traverse(_sort_ratings(ratings), 0)
    
if __name__ == '__main__':
    print('AoC 2020 Day 10\n')
    ratings = _parse_input()
    
    print('Solving part 1...')
    print(f'The answer is: {part1(ratings)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(ratings)}\n')
