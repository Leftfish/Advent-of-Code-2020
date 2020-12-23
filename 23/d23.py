print('Day 23 of Advent of Code!')


def setup_game_round_1(inp):
    i = 0
    cups = {}
    c = list(map(int, inp))

    for j in range(1, len(c)):
        cups[c[i]] = c[j]
        i += 1
        if i == len(c)-1:
            cups[c[i]] = c[0]
    return cups


def setup_game_round_2(inp, max_cup):
    i = 0
    cups = {}
    c = list(map(int, inp))

    for j in range(1, len(c)):
        cups[c[i]] = c[j]
        i += 1
        if i == len(c)-1:
            cups[c[i]] = max(c) + 1

    for k in range(max(c)+1, max_cup):
        cups[k] = k+1

    cups[max_cup] = c[0]

    return cups


def get_labels(cups, start):
    res = ''
    current = start
    while len(res) < len(cups):
        res += str(cups[current])
        current = cups[current]
    return res[:-1]


def play_round(cups, current):
    one = cups[current]
    two = cups[one]
    three = cups[two]

    pickup = (one, two, three)
    
    destination = current - 1
    if destination < 1:
            destination = max(cups.keys())
    
    while destination in pickup:
        destination -= 1
        if destination < 1:
            destination = max(cups.keys())

    # Current points to next after the third picked up
    cups[current] = cups[three]
    # Third cup picked up points to where destiantion used to point
    cups[three] = cups[destination]
    # Destination now points to first picked up
    cups[destination] = one


def play_game(inp, rounds, part1=True, part2=1000000):
    cups = setup_game_round_1(inp) if part1 else setup_game_round_2(inp, part2)
    current = int(inp[0])
    rnd = 1

    for _ in range(rounds):
        if rnd != 1:
            current = cups[current]
        play_round(cups, current)

        if not part1 and rnd % 2500000 == 0:
            print(f'Current round: {rnd:,}')

        rnd += 1

    return get_labels(cups, 1) if part1 else cups[1] * cups[cups[1]]


print('Solution...')
cup_labels = '974618352'
print('Game with 9 cups and 100 rounds...')
print('ResultL', play_game(cup_labels, 100))
print('Game with 1,000,000 cups and 10,000,000 rounds...')
print('Result: ', play_game(cup_labels, 10000000, part1=False))
