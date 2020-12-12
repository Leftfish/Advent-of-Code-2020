print('Day 12 of Advent of Code!')

FW = 'F'
NO = 'N'
SO = 'S'
EA = 'E'
WE = 'W'
TR = 'R'
TL = 'L'
DIRS = {NO: (0, 1), SO: (0, -1), WE: (-1, 0), EA: (1, 0)}
TURNS = (TR, TL)


def travel(moves, x=0, y=0, heading=90):
    headings_to_dirs = {0: NO, 90: EA, 180: SO, 270: WE}

    for move in moves:
        op, val = move[0], int(move[1:])
        if op in DIRS:
            x += DIRS[op][0] * val
            y += DIRS[op][1] * val
        elif op in TURNS:
            heading = (heading + val) % 360 if op == TR else (heading - val) % 360
        elif op == FW:
            course = headings_to_dirs[heading]
            x += DIRS[course][0] * val
            y += DIRS[course][1] * val
        else:
            raise ValueError("Invalid command!")
    return x, y


def travel_waypoint(moves, wx, wy, x=0, y=0):
    for move in moves:
        op, val = move[0], int(move[1:])
        waypoints = {0: (wx, wy), 90: (wy, -wx), 180: (-wx, -wy), 270: (-wy, wx)}
        if op in DIRS:
            wx += DIRS[op][0] * val
            wy += DIRS[op][1] * val
        elif op in TURNS:
            turn = val % 360 if op == TR else (360 - val) % 360
            wx, wy = waypoints[turn]
        elif op == FW:
            x += val * wx
            y += val * wy
        else:
            raise ValueError("Invalid command!", move, x, y, wx, wy)
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
print('Distance with waypoint:', calc_manhattan(*travel_waypoint(moves, 10, 1)) == 286)
print('---------------------')


with open('input', mode='r') as inp:
    print('Solution...')
    moves = [line.rstrip() for line in inp.readlines()]
    print('Distance without waypoint:', calc_manhattan(*travel(moves)))
    print('Distance with waypoint:', calc_manhattan(*travel_waypoint(moves, 10, 1)))
