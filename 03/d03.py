from functools import reduce
from operator import mul

print("Day 3 of Advent of Code!")

def traverse_map(map_input, dirs):
    map_lines = map_input.split('\n')
    w, h = 0, 0
    right, down = dirs
    line_length = len(map_lines[0])
    trees = 0

    while h < len(map_lines):
        current = map_lines[h][w]
        if current == "#":
            trees += 1
        w = (w + right) % line_length
        h += down
    return trees

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

directions = [(1,1), (3,1), (5,1), (7,1), (1,2)]
max_step_right = max((d[0] for d in directions))

print("Tests...")
print("Trees in one slope:", traverse_map(test_pattern, (3,1)) == 7)
print("Product of multiple slopes:", reduce(mul, (traverse_map(test_pattern, d) for d in directions)) == 336)

with open("input", mode = 'r') as inp:
    print("Solution...")
    final_map = inp.read()
    print("Trees in one slope:", traverse_map(final_map, (3,1)))
    print("Product of multiple slopes:", reduce(mul, (traverse_map(final_map, d) for d in directions)))
