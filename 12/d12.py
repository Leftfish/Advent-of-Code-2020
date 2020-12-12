print('Day 12 of Advent of Code!')

FW = 'F'
NO = 'N'
SO = 'S'
EA = 'E'
WE = 'W'
TR = 'R'
TL = 'L'


def travel(coords, x=0, y=0, heading=90):
    for coord in coords:
        op = coord[0]
        val = int(coord[1:])
        if op == NO or (op == FW and heading == 0):
            y += val
        elif op == SO or (op == FW and heading == 180):
            y -= val
        elif op == WE or (op == FW and heading == 270):
            x += val
        elif op == EA or (op == FW and heading == 90):
            x -= val
        elif op == TR:
            heading = (heading + val) % 360
        elif op == TL:
            heading = (heading - val) % 360
        else:
            raise ValueError("Invalid command!")
    return x, y


def travel_waypoint(coords, wx, wy, x=0, y=0):
    for coord in coords:
        op, val = coord[0], int(coord[1:])

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

coords = [line.rstrip() for line in test.split('\n')]

print('Tests...')
print('Distance without waypoint:', calc_manhattan(*travel(coords)) == 25)
print('Distance without waypoint:', calc_manhattan(*travel_waypoint(coords, 10, 1)) == 286)
print('---------------------')


with open('input', mode='r') as inp:
    print('Solution...')
    coords = [line.rstrip() for line in inp.readlines()]
    print('Distance without waypoint:', calc_manhattan(*travel(coords)))
    print('Distance without waypoint:', calc_manhattan(*travel_waypoint(coords, 10, 1)))
