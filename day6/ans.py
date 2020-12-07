from collections import Counter
from typing import List

def _parse_input() -> List[str]:
    with open('day6/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def _combine_groups(answers: List[str]) -> List[List[str]]:
    groups = []
    group = []
    for ans in answers:
        if ans == '':
            groups.append(group)
            group = []
        else:
            group.append(ans)

    if len(group) > 0:
        groups.append(group)

    return groups

def part1(groups: List[List[str]]) -> int:
    count = 0
    for group in groups:
        unique = set()
        for ans in group:
            unique.update(list(ans))

        count += len(unique)

    return count

def part2(groups: List[List[str]]) -> int:
    count = 0
    for group in groups:
        group_counts = Counter()
        for ans in group:
            for c in ans:
                group_counts[c] += 1
                if group_counts[c] == len(group):
                    count += 1

    return count

if __name__ == '__main__':
    print('AoC 2020 Day 6\n')
    groups = _combine_groups(_parse_input())

    print('Solving part 1...')
    print(f'The answer is: {part1(groups)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(groups)}\n')
