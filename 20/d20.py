
from collections import defaultdict
import numpy as np
import re

test = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''


def parse_tile(tile):
    lines = tile.splitlines()
    tile_id = int(re.findall(r'\d+', lines[0])[0])
    arr = []
    for line in lines[1:]:
        int_line = []
        for c in line:
            if c == '.': int_line.append(0)
            else: int_line.append(1)
        arr.append(int_line)
    shape = np.array(arr)

    return tile_id, shape


def make_tiles(inp):
    raw_tiles = inp.split('\n\n')
    parsed_tiles = []
    for t in raw_tiles:
        parsed_tiles.append(Tile(t))
    return parsed_tiles


class Tile:
    def __init__(self, raw_tile):
        parsed = parse_tile(raw_tile)
        self.id = parsed[0]
        self.shape = parsed[1]
        self.top, self.bottom, self.left, self.right = self._calc_borders()
        self.frozen = False
        
    def __str__(self):
        state = f"Tile ID: {self.id}."
        state += f'\n\n {self.shape}'
        return state
    
    def __repr__(self):
        return str(self.id)

    def _calc_borders(self):
        top = '0b' +  ''.join(map(str,  self.shape[0]))
        bottom = '0b' +  ''.join(map(str,  self.shape[-1]))
        left = '0b' +  ''.join(map(str,  self.shape[:,0]))
        right = '0b' +  ''.join(map(str,  self.shape[:,-1]))
        borders = (int(border, 2) for border in (top, bottom, left, right))
        return borders

    def rot_left(self):
        self.shape = np.rot90(self.shape, 1)
        self.top, self.bottom, self.left, self.right = self._calc_borders()

    def flip(self):
        self.shape = np.flipud(self.shape)        
        self.top, self.bottom, self.left, self.right = self._calc_borders()


def check_connection(A, B, side):
    if side == 'R' and A.right == B.left:
        return True
    elif side == 'L' and A.left == B.right:
        return True
    elif side == 'T' and A.top == B.bottom:
        return True
    elif side == 'B' and A.bottom == B.top:
        return True


def count_adj(check, tiles, side, edgecount):
    for tile in tiles:
        if check != tile:
            if check_connection(check, tile, side):
                edgecount[check.id] += 1
                return
            for _ in range(3):
                tile.rot_left()    
                if check_connection(check, tile, side):
                    edgecount[check.id] += 1
                    return
            tile.flip()
            if check_connection(check, tile, side):
                edgecount[check.id] += 1
                return
            else:
                for _ in range(3):
                    tile.rot_left()    
                    if check_connection(check, tile, side):
                        edgecount[check.id] += 1
                        return

def find_adj(check, tiles, side):
    for tile in tiles:
        if check != tile:
            if check_connection(check, tile, side): 
                tile.frozen = True
                return tile
            elif not tile.frozen:
                for _ in range(3):
                    tile.rot_left()    
                    if check_connection(check, tile, side): 
                        tile.frozen = True
                        return tile
                tile.flip()
                if check_connection(check, tile, side): 
                    tile.frozen = True
                    return tile
                else:
                    for _ in range(3):
                        tile.rot_left()    
                        if check_connection(check, tile, side): 
                            tile.frozen = True
                            return tile

def find_corners(tiles):
    edgecount = defaultdict(int)
    for check in tiles:
        for d in ("TBLR"):
            count_adj(check, tiles, d, edgecount)
    prod = 1
    for k in edgecount:
        if edgecount[k] == 2:
            prod *= k
    corners = [T for T in tiles if edgecount[T.id] == 2]
    return corners


def initiate_row(corners):
    # we find the initial(top-left) corner and initialize row with its copy
    for corner in corners:
        if find_adj(corner, tiles, 'R') and (len(corners) == 1 or find_adj(corner, tiles, 'B')):
            current_leftmost = corner
            next_row = find_adj(corner, tiles, 'B')
            break
    return current_leftmost, next_row


def make_row(init_tile, tiles, row):
    while True:
        next_right = find_adj(init_tile, tiles, 'R')
        if not next_right:
            break
        else:
            next_in_row = np.copy(next_right.shape)#[1:9, 1:9])
            row = np.concatenate((row, next_in_row), axis=1)
            init_tile = next_right
    return row

tiles = make_tiles(test)
corners = find_corners(tiles)

while True:
    current_leftmost, next_row = initiate_row(corners)
    row_init = np.copy(current_leftmost.shape)#[1:9, 1:9]
    row = make_row(current_leftmost, tiles, row_init)
    corners = [next_row]
    print(row)
    if not next_row:
        break
