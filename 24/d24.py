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

tiles = test.splitlines()

def flip_tile(tile, dirs):
    moves = parse_tile(tile, dirs)
    x, y, z = 0, 0, 0
    for move in moves:
        x += move[0]
        y += move[1]
        z += move[2]
    return x, y, z

def count_flipped_tiles(tiles):
    black = set()
    for tile in tiles:
        flipped = flip_tile(tile, DIRS)
        if flipped not in black:
            black.add(flipped)
        else:
            black.remove(flipped)
    return len(black)

with open('input', mode='r') as inp:
    print('Solution...')
    tiles = [l.rstrip() for l in inp.readlines()]
    print(count_flipped_tiles(tiles))