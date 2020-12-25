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
        self.adj_top = None
        self.adj_btm = None
        self.adj_rgt = None
        self.adj_lft = None
        self.id = parsed[0]
        self.shape = parsed[1]
        self.top, self.bottom, self.left, self.right = self._calc_borders()
        
    def __str__(self):
        state = f"Tile ID: {self.id}. Adjacents: {repr(self.adj_top)}, {repr(self.adj_btm)}, {repr(self.adj_rgt)}, {repr(self.adj_lft)}."
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

    def is_set(self):
        return any((self.adj_top, self.adj_btm, self.adj_lft, self.adj_rgt))

    def rot_left(self):
        self.shape = np.rot90(self.shape, 1)
        self.top, self.bottom, self.left, self.right = self._calc_borders()

    def flip(self):
        self.shape = np.flipud(self.shape)        
        self.top, self.bottom, self.left, self.right = self._calc_borders()


tiles = make_tiles(test)
for t in tiles:
    print(t)
    print('\n')


#do zrobienia mapy użyjemy concatenate: najpierw rzędy, potem rzędy wg. axis=0
#T = Tile(raw_tile)
#T.flip()
#T2 = Tile(raw_tile)
#x = np.concatenate((T.shape, T2.shape), axis=1)