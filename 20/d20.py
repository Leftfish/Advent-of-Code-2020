
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
        self.adj_top = None
        self.adj_btm = None
        self.adj_rgt = None
        self.adj_lft = None
        self.id = parsed[0]
        self.shape = parsed[1]
        self.top, self.bottom, self.left, self.right = self._calc_borders()
        self.adjacents = (self.adj_top, self.adj_btm, self.adj_lft, self.adj_rgt)
        
    def __str__(self):
        state = f"Tile ID: {self.id}. Adjacents: TOP {repr(self.adj_top)}, BOT {repr(self.adj_btm)}, RGT {repr(self.adj_rgt)}, LFT {repr(self.adj_lft)}."
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


def connect(A, B, side):
    if B not in A.adjacents and A not in B.adjacents:
        if side == 'R' and A.right == B.left:
            print("Dla", A.id, "znalazłem dopasowanie z prawej", B.id)
            A.adj_rgt = B
            B.adj_lft = A
            return True
        elif side == 'L' and A.left == B.right  and not (A.adj_lft or B.adj_rgt):
            print("Dla", A.id, "znalazłem dopasowanie z lewej", B.id)
            A.adj_lft = B
            B.adj_rgt = A
            return True
        elif side == 'T' and A.top == B.bottom  and not (A.adj_top or B.adj_btm):
            print("Dla", A.id, "znalazłem dopasowanie z góry", B.id)
            A.adj_top = B
            B.adj_btm = A
            return True
        elif side == 'B' and A.bottom == B.top and not (A.adj_btm or B.adj_top):
            print("Dla", A.id, "znalazłem dopasowanie z dołu", B.id)
            A.adj_btm = B
            B.adj_top = A
            return True

def find_adj(check, tiles, side):
    for tile in tiles:
        if check != tile:
            if connect(check, tile, side):
                return
            for _ in range(3):
                tile.rot_left()    
                if connect(check, tile, side):
                    return
            tile.flip()
            if connect(check, tile, side):
                return
            else:
                for _ in range(3):
                    tile.rot_left()    
                    if connect(check, tile, side):
                        return

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





with open('input', mode='r') as inp:

    tiles = make_tiles(inp.read())
    edgecount = defaultdict(int)

    for check in tiles:
        print(f"Sprawdzam {check.id}")
        for d in ("TBLR"):
            count_adj(check, tiles, d, edgecount)
    print(edgecount)
    prod = 1
    for k in edgecount:
        if edgecount[k] == 2:
            prod *= k

    print(prod)


'''
1) weź T1 z listy
2) iteruj przez wszystkie tile
3) znaleziona 
4) czy prawa pasuje to lewej? (ew. dół do góry, góra do dołu, lewa do prawej)
    5) - tak: doczep T2 jako right w T1, doczep T1 jako left do T2
    6) - nie:
        7) > czy jest frozen? 
            - tak: porzuć, idź to następnej
            - nie: obróć raz w lewo i wróć do 4)
            > czy obróciłeś 4 razy?
                - flip i wróć do 4)
        8) czy obróciłeś 4 razy przed i po flipie i nadal nie pasuje?
            - tak: porzuć, idź to następnej
    9) jak doszedłeś

------
1) weź początek mapy
2) zakolejkuj jego adjacenty
3) dla każdego powtórz poszukiwania tam,gdzie nie ma adjc
4) jak liczba sprawdzonych == liczba kafli - finisz

'''

#do zrobienia mapy użyjemy concatenate: najpierw rzędy, potem rzędy wg. axis=0  
#T = Tile(raw_tile)
#T.flip()
#T2 = Tile(raw_tile)
#x = np.concatenate((T.shape, T2.shape), axis=1)