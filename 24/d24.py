print('Day 24 of Advent of Code!')


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
    adj = set()
    for move in DIRS.values():
        adj.add((x + move[0], y + move[1], z + move[2]))
    return adj

def conway_hex(tiles, days, printout=True):
    pass


black = setup_tiles(tiles)
white = set()

day = 1
days = 100

for _ in range(days):

    to_black = set()
    to_white = set()
    to_check = set()
    for tile in black | white:
        to_check.add(tile)
        to_check |= get_adjacent(*tile)

    for tile in to_check:
        adjacents = get_adjacent(*tile)
        adj_black = adjacents & black
        if tile in black:
            if len(adj_black) < 1 or len(adj_black) > 2:
                to_white.add(tile)
        else:
            if len(adj_black) == 2:
                to_black.add(tile)

    for t in to_black:
        black.add(t)
    for t in to_white:
        black.remove(t)

    #if printout:
    print(f'Day {day}, black tiles {len(black)}')
    
    day += 1

    #return black



'''
najpierw ustaw czarne kafelki
zrób zbiór do sprawdzenia z:
    - obecnie znanych
    - wszystkich ich adj
potem dla każdego z listy sprawdzaj adj
-> część do listy to_black
-> część do listy to_white
flip jednocześnie
'''
    


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
#print('Conway Hex:', len(conway_hex(tiles, 100, False)))
print('---------------------')


with open('input', mode='r') as inp:
    print('Solution...')
    tiles = [l.rstrip() for l in inp.readlines()]
    #print('Flipped tiles:', len(setup_tiles(tiles)))
    black = setup_tiles(tiles)
    white = set()

    day = 1
    days = 100

    for _ in range(days):

        to_black = set()
        to_white = set()
        to_check = set()
        for tile in black | white:
            to_check.add(tile)
            to_check |= get_adjacent(*tile)

        for tile in to_check:
            adjacents = get_adjacent(*tile)
            adj_black = adjacents & black
            if tile in black:
                if len(adj_black) < 1 or len(adj_black) > 2:
                    to_white.add(tile)
            else:
                if len(adj_black) == 2:
                    to_black.add(tile)

        for t in to_black:
            black.add(t)
        for t in to_white:
            black.remove(t)

        #if printout:
        print(f'Day {day}, black tiles {len(black)}')
        
        day += 1

        #return black