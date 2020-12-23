print('Day 23 of Advent of Code!')



test = "389125467"
test = "974618352"

def parse_cups(inp):
    cups = {}
    c = list(map(int, inp))

    i = 0
    for j in range(1, len(c)):
        cups[c[i]] = c[j]
        i += 1
        if i == len(c)-1:
            cups[c[i]] = c[0]
    return cups

def print_cups(cups, start):
    res = ''
    current = start
    while len(res) < 9:
        res += str(cups[current])
        current = cups[current]
    return res



def play_round(cups, current, debug=False):
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
    

    if debug:
        print("Before round:", print_cups(cups, 7))
        print(f"Current cup: {current}")
        print(f"Pickups: {pickup}")
        print(f"Destination: {destination}")
    cups[current] = cups[three]
    next_after_dest = cups[destination]
    if debug:
        print(f"Next after destinaton is {next_after_dest}.")
    cups[destination] = one
    '''if debug:
        print(f"One is {one}. Desination is {destination}. Now cups[destination] is {cups[destination]}.")
        print(f"Cups[one] is {cups[one]}")
        print(f"Cups[two] is {cups[two]}")
        print(f"Cups[three] is {cups[three]}")'''
    cups[three] = next_after_dest
    #if debug:
    print("After round:", print_cups(cups, 1))
    '''if print_cups(cups, 1)[:-1] == '92658374':
        print("!!!!")
    if print_cups(cups, 1):-1] == '67384529':
        print("!!!!")'''   

cups = parse_cups(test)
current = int(test[0])
rnd = 1
for _ in range(100):
    if rnd != 1:
        current = cups[current]
    print(f"NEW ROUND {rnd}. Current {current}. Cups before: {print_cups(cups, 1)}")
    play_round(cups, current, debug=False)
    rnd += 1
    

## 758932641

print('Tests...')
print('---------------------')


print('Solution...')
