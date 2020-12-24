print('Day 24 of Advent of Code!')


NW = (0, 1, -1)
NE = (1, 0, -1)
W = (-1, 1, 0)
E = (1, -1, 0)
SW = (-1, 0, 1)
SE = (0, -1, 1)

DIRS = {'w': W, 'e': E, 'nw': NW, 'ne': NE, 'se': SE, 'sw': SW}


def parse_tile(tile, dirs):
    moves = []
    i = 0

    while i < len(tile):
        pair = tile[i:i+2]
        if pair in ('nw', 'ne', 'sw', 'se'):
            moves.append(dirs[pair])
            i += 2
        else:
            moves.append(dirs[tile[i]])
            i += 1

    return moves


def flip_tile(tile, dirs):
    moves = parse_tile(tile, dirs)
    x, y, z = 0, 0, 0

    for move in moves:
        x += move[0]
        y += move[1]
        z += move[2]

    return x, y, z


def setup_tiles(tiles):
    black = set()

    for tile in tiles:
        flipped = flip_tile(tile, DIRS)
        if flipped not in black:
            black.add(flipped)
        else:
            black.remove(flipped)

    return black


def get_adjacent(x, y, z):
    return {(x + move[0], y + move[1], z + move[2]) for move in DIRS.values()}


def conway_hex(tiles, days, printout=False):
    day = 1
    black, white = setup_tiles(tiles), set()

    for _ in range(days):
        to_black = set()
        to_white = set()
        to_check = set()

        for tile in black | white:
            to_check.add(tile)
            to_check |= get_adjacent(*tile)

        for tile in to_check:
            adjacents = get_adjacent(*tile)
            adj_black = len(adjacents & black)

            if tile in black:
                if adj_black not in (1, 2):
                    to_white.add(tile)
            else:
                if adj_black == 2:
                    to_black.add(tile)

        for tile in to_black:
            black.add(tile)
        for tile in to_white:
            black.remove(tile)

        if printout:
            print(f'Day {day}, black tiles {len(black)}')

        day += 1

    return black


test = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''

print("Tests...")
tiles = test.splitlines()
initial = setup_tiles(tiles)
print('Flipped tiles:', len(initial))
print('Conway Hex:', len(conway_hex(tiles, 100, False)) == 2208)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    tiles = [l.rstrip() for l in inp.readlines()]
    print('Flipped tiles:', len(setup_tiles(tiles)))
    print('Conway Hex:', len(conway_hex(tiles, 100, False)))
