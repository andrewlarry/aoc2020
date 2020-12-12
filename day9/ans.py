from typing import Dict, List, Optional, Tuple

def _parse_input() -> List[int]:
    with open('day9/input.txt') as f:
        return [int(ln.strip()) for ln in f.readlines()]

def _two_sum_exists(nums: List[int], target: int) -> bool:
    if len(nums) < 2:
        return False

    diffs = set()
    for num in nums:
        if num in diffs:
            return True
        diffs.add(target - num)

    return False

def _contiguous_sum(nums: List[int], target: int) -> Tuple[int, int]:
    if len(nums) < 2:
        return -1, -1
    
    curr_sum = sum(nums[0:2])
    start, end = 0, 1
    
    while end < len(nums) - 1:
        while curr_sum > target and start < end:
            curr_sum -= nums[start]
            start += 1
        
        if curr_sum == target and end - start > 0:
            return start, end
        
        end += 1
        curr_sum += nums[end]
        
    return -1, -1
        
def part1(nums: List[int], preamble: int) -> int:
    for i in range(preamble, len(nums)):
        chunk = nums[i-preamble:i]
        if not _two_sum_exists(chunk, nums[i]):
            return nums[i]
    
    return -1

def part2(nums: List[int], target: int) -> int:
    start, end = _contiguous_sum(nums, target)
    chunk = nums[start:end]
    return min(chunk) + max(chunk)

if __name__ == '__main__':
    print('AoC 2020 Day 9\n')
    nums = _parse_input()
    preamble = 25

    invalid_number = part1(nums, preamble)
    print('Solving part 1...')
    print(f'The answer is: {invalid_number}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(nums, invalid_number)}\n')
