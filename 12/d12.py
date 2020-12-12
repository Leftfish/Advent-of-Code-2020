print('Day 12 of Advent of Code!')

FW = 'F'
NO = 'N'
SO = 'S'
EA = 'E'
WE = 'W'
TR = 'R'
TL = 'L'


def travel(moves, x=0, y=0, heading=90):
    dirs = {NO: (0, 1), SO: (0, -1), WE: (-1, 0), EA: (1, 0)}
    headings_to_dirs = {0: NO, 90: EA, 180: SO, 270: WE}

    for move in moves:
        op = move[0]
        val = int(move[1:])
        if op in dirs:
            x += dirs[op][0] * val
            y += dirs[op][1] * val
        elif op == FW:
            course = headings_to_dirs[heading]
            x += dirs[course][0] * val
            y += dirs[course][1] * val
        elif op == TR:
            heading = (heading + val) % 360
        elif op == TL:
            heading = (heading - val) % 360
        else:
            raise ValueError("Invalid command!")
    return x, y


def travel_waypoint(moves, wx, wy, x=0, y=0):
    for move in moves:
        op, val = move[0], int(move[1:])

        if op == FW:
            x += val * wx
            y += val * wy
        elif op == NO:
            wy += val
        elif op == SO:
            wy -= val
        elif op == WE:
            wx -= val
        elif op == EA:
            wx += val
        elif op == TR:
            for _ in range(val // 90):
                wx, wy = wy, -wx
        elif op == TL:
            for _ in range(val // 90):
                wx, wy = -wy, wx
        else:
            raise ValueError("Invalid command!")
    return x, y


def calc_manhattan(x, y, start_x=0, start_y=0):
    return abs(x-start_x) + abs(y-start_y)


test = '''F10
N3
F7
R90
F11'''

moves = [line.rstrip() for line in test.split('\n')]

print('Tests...')
print('Distance without waypoint:', calc_manhattan(*travel(moves)) == 25)
print('Distance without waypoint:', calc_manhattan(*travel_waypoint(moves, 10, 1)) == 286)
print('---------------------')


with open('input', mode='r') as inp:
    print('Solution...')
    moves = [line.rstrip() for line in inp.readlines()]
    print('Distance without waypoint:', calc_manhattan(*travel(moves)))
    print('Distance without waypoint:', calc_manhattan(*travel_waypoint(moves, 10, 1)))
