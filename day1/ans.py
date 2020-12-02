from typing import List, Optional, Tuple

def _parse_input() -> List[int]:
    with open('day1/input.txt') as f:
        return [int(ln.strip()) for ln in f.readlines()]

def _find_two_nums(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    if len(nums) < 2:
        return None

    num_map = {}
    for num in nums:
        if num in num_map:
            return (num, num_map[num])
        num_map[target - num] = num

    return None

def part1(nums: List[int], target: int) -> Optional[int]:
    two = _find_two_nums(nums, target)
    if two is None:
        return None

    return two[0] * two[1]

def part2(nums: List[int], target: int) -> Optional[int]:
    if len(nums) < 3:
        return None

    for i in range(len(nums)):
        rest = nums[:i] + nums[i+1:]
        other_nums = _find_two_nums(rest, target - nums[i])
        if other_nums is not None:
            return nums[i] * other_nums[0] * other_nums[1]

    return None

if __name__ == '__main__':
    print('AoC 2020 Day 1\n')

    nums = _parse_input()
    target = 2020

    print('Solving part 1...')
    print(f'The answer is: {part1(nums, target)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(nums, target)}\n')
