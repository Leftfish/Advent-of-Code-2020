from functools import reduce
from operator import mul

print("Day 3 of Advent of Code!")

def extend_map(map_lines, max_step_right):
    height = len(map_lines)
    width = len(map_lines[0])
    ratio = max_step_right * height // width

    for i in range(height):
        map_lines[i] *= ratio
    
    return map_lines

def traverse_map(map_lines, dirs):
    w, h = 0, 0
    right, down = dirs
    trees = 0
    while h < len(map_lines) and w < len(map_lines[0]):
        if map_lines[h][w] == '#':
            trees += 1
        w += right
        h += down
    return trees

directions = [(1,1), (3,1), (5,1), (7,1), (1,2)]
max_step_right = max((d[0] for d in directions))

test_pattern = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

test_map = extend_map(test_pattern.split('\n'), max_step_right)

print("Tests...")
print("Trees in one slope:", traverse_map(test_map, (3,1)) == 7)
print("Product of multiple slopes:", reduce(mul, (traverse_map(test_map, d) for d in directions)) == 336)

print("Solution...")
with open("input", mode = 'r') as inp:
    map_lines = [line.rstrip() for line in inp]
    final_map = extend_map(map_lines, max_step_right)
    print("Trees in one slope:", traverse_map(final_map, (3,1)))
    print("Product of multiple slopes:", reduce(mul, (traverse_map(final_map, d) for d in directions)))
