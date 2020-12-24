from re import findall

print('Day 24 of Advent of Code!')

def setup_cubes(start):
    cubes = set()

    for x in range(len(start[0])):
        for y in range(len(start)):
            if start[y][x] == '#':
                cube = (x, y, 0)
                cubes.add(cube)
    return cubes


def get_adjacent(x, y, z):
    adjacents = set()
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                adj_x = x + dx
                adj_y = y + dy
                adj_z = z + dz
                adjacent = (adj_x, adj_y, adj_z)
                if (x, y, z) != adjacent:
                    adjacents.add(adjacent)
    return adjacents

def conway_3d(start, rounds, printout=False):
    active, inactive = setup_cubes(start), set()

    for rnd in range(rounds):
        to_check = set()
        to_active = set()
        to_inactive = set()
        
        for cube in active:
            to_check.add(cube)
            to_check |= get_adjacent(*cube)

        for cube in to_check:
            adjacents = get_adjacent(*cube)
            adj_occupied = len(adjacents & active)

            if cube in active:
                if adj_occupied not in (2, 3):
                    to_inactive.add(cube)
            else:
                if adj_occupied == 3:
                    to_active.add(cube)

        if printout:
            print("To active:", to_active)
            print("To inactive:", to_inactive)

        for cube in to_active:
            active.add(cube)
        for cube in to_inactive:
            active.remove(cube)

        if printout:
            print(f'Round {rnd}, cubes {len(active)}')

    return active


test = '''.#.
..#
###'''

print("Tests...")

start = [list(l) for l in test.splitlines()]
print(len(conway_3d(start, 6, True)))
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    cubes = [l.rstrip() for l in inp.readlines()]
    print(len(conway_3d(inp.read(), 6, False)))
