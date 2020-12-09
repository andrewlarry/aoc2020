from typing import Dict, List, Set

class BagTree:
    def __init__(self, color: str, children: List[str]) -> None:
        self.color = color
        self.children = children

def _parse_input() -> List[str]:
    with open('day7/input.txt') as f:
        return [ln.strip() for ln in f.readlines()]

def _parse_rules(rules: List[str]) -> List[BagTree]:
    bag_trees = {}
    for rule in rules:
        parts = rule.split('bags contain')
        color = parts[0].strip()

        if color not in bag_trees:
            bag_trees[color] = BagTree(color, [])
        
        tree = bag_trees[color]

        children = parts[1].strip().split(',')
        for child in children:
            child_parts = child.strip().split(' ')
            bag_count = child_parts[0]
            if bag_count == 'no':
                continue

            child_color = ' '.join(child_parts[1:-1])
            if child_color not in bag_trees:
                bag_trees[child_color] = BagTree(child_color, [])
            
            tree.children.extend(int(bag_count) * [bag_trees[child_color]])
    
    return list(bag_trees.values())

def path_exists(bag_tree: BagTree, target: str, visited: Set[str]) -> bool:
    if len(bag_tree.children) == 0 or bag_tree.color in visited:
        return False

    if bag_tree.color == target:
        return True
    
    for child in bag_tree.children:
        if path_exists(child, target, visited):
            return True
    
    visited.add(bag_tree.color)
    return False

def tree_size(bag_tree: BagTree, memo: Dict[str, int]) -> int:
    if len(bag_tree.children) == 0:
        return 0
    
    if bag_tree.color in memo:
        return memo[bag_tree.color]

    size = 0
    for child in bag_tree.children:
        size += (1 + tree_size(child, memo))
    
    memo[bag_tree.color] = size
    return size

def part1(bag_trees: List[BagTree], target: str) -> int:
    count = 0
    for tree in bag_trees:
        if tree.color != target:
            count += int(path_exists(tree, target, set()))

    return count

def part2(bag_trees: List[BagTree], target: str) -> int:
    bag_tree = next(bt for bt in bag_trees if bt.color == target)
    return tree_size(bag_tree, {})

if __name__ == '__main__':
    print('AoC 2020 Day 7\n')
    target = 'shiny gold'
    bag_trees = _parse_rules(_parse_input())

    print('Solving part 1...')
    print(f'The answer is: {part1(bag_trees, target)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(bag_trees, target)}\n')
