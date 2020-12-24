print('Day 17 of Advent of Code!')


def setup_cubes(start, part1=True):
    cubes = set()

    for x in range(len(start[0])):
        for y in range(len(start)):
            if start[y][x] == '#':
                if part1:
                    cube = (x, y, 0)
                else:
                    cube = (x, y, 0, 0)
                cubes.add(cube)
    return cubes


def get_adjacent(x, y, z, w=0, part1=True):
    adjacents = set()
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if part1:
                    adj_x = x + dx
                    adj_y = y + dy
                    adj_z = z + dz
                    adjacent = (adj_x, adj_y, adj_z)
                    if (x, y, z) != adjacent:
                        adjacents.add(adjacent)
                else:
                    for dw in (-1, 0, 1):
                        adj_x = x + dx
                        adj_y = y + dy
                        adj_z = z + dz
                        adj_w = w + dw
                        adjacent = (adj_x, adj_y, adj_z, adj_w)
                        if (x, y, z, w) != adjacent:
                            adjacents.add(adjacent)
    return adjacents


def conway_multi_dimensional(start, rounds, printout=False, part1=True):
    active = setup_cubes(start, part1)

    for rnd in range(rounds):
        to_check = set()
        to_active = set()
        to_inactive = set()

        for cube in active:
            to_check.add(cube)
            to_check |= get_adjacent(*cube, part1)

        for cube in to_check:
            adjacents = get_adjacent(*cube, part1)
            adj_occupied = len(adjacents & active)

            if cube in active:
                if adj_occupied not in (2, 3):
                    to_inactive.add(cube)
            else:
                if adj_occupied == 3:
                    to_active.add(cube)

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

print('Tests...')

start = [list(l) for l in test.splitlines()]
print('Conway 3D after 6 rounds:', len(conway_multi_dimensional(start, 6, printout=False, part1=True)) == 112)
print('Conway 4D after 6 rounds:', len(conway_multi_dimensional(start, 6, printout=False, part1=False)) == 848)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    cubes = [list(l.rstrip()) for l in inp.readlines()]
    print('Conway 3D after 6 rounds:', len(conway_multi_dimensional(cubes, 6, printout=False, part1=True)))
    print('Conway 4D after 6 rounds:', len(conway_multi_dimensional(cubes, 6, printout=False, part1=False)))
