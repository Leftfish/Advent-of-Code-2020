print('Day 11 of Advent of Code!')


EMPTY = 'L'
TAKEN = '#'
FLOOR = '.'


def make_map(lines):
    extended = [['.'] + list(row) + ['.'] for row in lines]
    width = len(lines[0])
    empty_row = ['.'] * (width + 2)
    extended.insert(0, empty_row)
    extended.append(empty_row)

    return extended


def count_adjacent_p1(y, x, arr):
    adjacent = []
    coords = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
    for coord in coords:
        y, x = coord
        if arr[y][x] == TAKEN:
            adjacent.append(coord)
    return adjacent


def count_adjacent_p2(y, x, arr):
    adjacent = []
    # UP
    dy = y
    while dy > 0:
        dy -= 1
        if arr[dy][x] == TAKEN:
            adjacent.append((dy, x))
            break
        elif arr[dy][x] == EMPTY:
            break
    # DOWN
    dy = y
    while dy < len(arr)-1:
        dy += 1
        if arr[dy][x] == TAKEN:
            adjacent.append((dy, x))
            break
        elif arr[dy][x] == EMPTY:
            break
    # RIGHT
    dx = x
    while dx < len(arr[0])-1:
        dx += 1
        if arr[y][dx] == TAKEN:
            adjacent.append((y, dx))
            break
        elif arr[y][dx] == EMPTY:
            break
    # LEFT
    dx = x
    while dx > 0:
        dx -= 1
        if arr[y][dx] == TAKEN:
            adjacent.append((y, dx))
            break
        elif arr[y][dx] == EMPTY:
            break
    # RIGHT-DOWN
    dx, dy = x, y
    while dy < len(arr)-1 and dx < len(arr[0])-1:
        dx += 1
        dy += 1
        if arr[dy][dx] == TAKEN:
            adjacent.append((dy, dx))
            break
        elif arr[dy][dx] == EMPTY:
            break

    # RIGHT-UP
    dx, dy = x, y
    while dy > 0 and dx < len(arr[0])-1:
        dx += 1
        dy -= 1
        if arr[dy][dx] == TAKEN:
            adjacent.append((dy, dx))
            break
        elif arr[dy][dx] == EMPTY:
            break

    # LEFT-DOWN
    dx, dy = x, y
    while dy < len(arr)-1 and dx > 0:
        dx -= 1
        dy += 1
        if arr[dy][dx] == TAKEN:
            adjacent.append((dy, dx))
            break
        elif arr[dy][dx] == EMPTY:
            break

    # LEFT-UP
    dx, dy = x, y
    while dy > 0 and dx > 0:
        dx -= 1
        dy -= 1
        if arr[dy][dx] == TAKEN:
            adjacent.append((dy, dx))
            break
        elif arr[dy][dx] == EMPTY:
            break

    return adjacent


def check_seats(arr, counter, limit):
    to_take = []
    to_leave = []
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == EMPTY:
                adjacent = counter(y, x, arr)
                if len(adjacent) == 0:
                    to_take.append((y, x))
            elif arr[y][x] == TAKEN:
                adjacent = counter(y, x, arr)
                if len(adjacent) >= limit:
                    to_leave.append((y, x))
    return to_take, to_leave


def update_seats(arr, to_take, to_leave):
    for coord in to_take:
        y, x = coord
        arr[y][x] = TAKEN
    for coord in to_leave:
        y, x = coord
        arr[y][x] = EMPTY
    return arr


def simulate_seating(arr, counter, limit):
    while True:
        to_take, to_leave = check_seats(arr, counter, limit)
        if to_take or to_leave:
            arr = update_seats(arr, to_take, to_leave)
        else:
            flattened = ''.join((''.join(row) for row in arr))
            return flattened.count(TAKEN)


test_layout = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

t1 = make_map(test_layout.split('\n'))
t2 = make_map(test_layout.split('\n'))
print('---------------')
print('Tests...')
print('Occupied seats, part 1:', simulate_seating(t1, count_adjacent_p1, 4) == 37)
print('Occupied seats, part 2:', simulate_seating(t2, count_adjacent_p2, 5) == 26)
print('---------------------')


with open('input', mode='r') as inp:
    print('Solution...')
    test = [line.rstrip() for line in inp.readlines()]
    p1 = make_map(test)
    p2 = make_map(test)
    print('Occupied seats, part 1:', simulate_seating(p1, count_adjacent_p1, 4))
    print('Occupied seats, part 2:', simulate_seating(p2, count_adjacent_p2, 5))
