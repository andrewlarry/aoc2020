from typing import List, Tuple

def _parse_input() -> List[str]:
    with open('day12/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def _turn(start: int, direction: str, amount: int) -> int:
    incr = amount if direction == 'L' else 360 - amount
    return (start + incr) % 360

def _move(degree: int, amount: int) -> Tuple[int, int]:
    if degree == 0:
        move = (0, amount)
    elif degree == 90:
        move = (amount, 0)
    elif degree == 180:
        move = (0, -1 * amount)
    else:
        move = (-1 * amount, 0)
    return move

def _quadrant_multipliers(position: Tuple[int, int], degrees: int) -> Tuple[int, int]:
    ns, ew = position
    ns_sign, ew_sign = 0, 0
    
    if ns >= 0 and ew >= 0:
        ns_sign = 1 if degrees in [0, 90] else -1
        ew_sign = 1 if degrees in [0, 270] else -1
    elif ns >= 0 and ew < 0:
        ns_sign = 1 if degrees in [0, 270] else -1
        ew_sign = -1 if degrees in [0, 90] else 1
    elif ns < 0 and ew < 0:
        ns_sign = -1 if degrees in [0, 90] else 1
        ew_sign = -1 if degrees in [0, 270] else 1
    else:
        ns_sign = -1 if degrees in [0, 270] else 1
        ew_sign = 1 if degrees in [0, 90] else -1    
    return ns_sign, ew_sign

def _turn_waypoint(position: Tuple[int, int], direction: str, amount: int) -> int:
    degrees = _turn(0, direction, amount)
    ns, ew = _quadrant_multipliers(position, degrees)
    
    if degrees == 0:
        end = (ns * abs(position[0]), ew * abs(position[1]))
    elif degrees == 90:
        end = (ns * abs(position[1]), ew * abs(position[0]))
    elif degrees == 180:
        end = (ns * abs(position[0]), ew * abs(position[1]))
    else:
        end = (ns * abs(position[1]), ew * abs(position[0]))
    return end

def part1(instructions: List[str]) -> int:
    position = (0, 0)
    direction_map = {'N': 90, 'S': 270, 'E': 0, 'W': 180, 'F': 0}
    
    for instruction in instructions:
        action, amount = instruction[0], int(instruction[1:])
        if action in ['L', 'R']:
            new_degrees = _turn(direction_map['F'], action, amount)
            direction_map['F'] = new_degrees
        else:
            ns, ew = _move(direction_map[action], amount)
            position = (position[0] + ns, position[1] + ew)

    return abs(position[0]) + abs(position[1])

def part2(instructions: List[str]) -> int:
    waypoint, position = (1, 10), (0, 0)
    direction_map = {'N': 90, 'S': 270, 'E': 0, 'W': 180}
    
    for instruction in instructions:
        action, amount = instruction[0], int(instruction[1:])
        if action == 'F':
            position = (amount * waypoint[0] + position[0],
                        amount * waypoint[1] + position[1])
        elif action in ['L', 'R']:
            waypoint = _turn_waypoint(waypoint, action, amount)
        else:
            ns, ew = _move(direction_map[action], amount)
            waypoint = (ns + waypoint[0], ew + waypoint[1])
    
    return abs(position[0]) + abs(position[1])

if __name__ == '__main__':
    print('AoC 2020 Day 12\n')
    instructions = _parse_input()
    
    print('Solving part 1...')
    print(f'The answer is: {part1(instructions)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(instructions)}\n')
