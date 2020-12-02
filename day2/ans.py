from typing import Callable, List, Tuple

Policy = Tuple[str, int, int]

def _parse_input() -> List[str]:
    with open('day2/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def _parse_policy(policy_str: str) -> Policy:
    parts = policy_str.split(' ')
    nums = parts[0].split('-')
    return parts[1], int(nums[0]), int(nums[1])

def _solver(rows: List[str], validator: Callable[[str, Policy], bool]) -> int:
    count = 0
    for row in rows:
        parts = row.split(':')
        if validator(parts[1].strip(), _parse_policy(parts[0].strip())):
            count += 1

    return count

def part1(rows: List[str]) -> int:
    def validator(password: str, policy: Policy) -> bool:
        char, mn, mx = policy
        count = 0
        for c in password:
            if c == char:
                count += 1

        return mn <= count <= mx

    return _solver(rows, validator)

def part2(rows: List[str]) -> int:
    def validator(password: str, policy: Policy) -> bool:
        char, first, second = policy
        return (password[first - 1] == char) ^ (password[second - 1] == char)

    return _solver(rows, validator)

if __name__ == '__main__':
    print('AoC 2020 Day 2\n')
    rows = _parse_input()

    print('Solving part 1...')
    print(f'The answer is: {part1(rows)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(rows)}\n')
