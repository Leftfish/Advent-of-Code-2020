print('Day 5 of Advent of Code!')


def binary_search(seq):
    l, r = 0, 2**(len(seq)) - 1
    for char in seq:
        if char in 'FL':
            r -= (r - l + 1) / 2
        elif char in 'BR':
            l += (r - l + 1) / 2
    return l if l == r else -1


def calculate_seat_id(ticket):
    return int(binary_search(ticket[:-3]) * 8 + binary_search(ticket[-3:]))

test_tickets = [('BFFFBBFRRR', 567), ('FFFBBBFRRR', 119), ('BBFFBBFRLL', 820)]

print('Tests...')
for t in test_tickets:
    print('{}: {}'.format(t[0], calculate_seat_id(t[0]) == t[1]))
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    tickets = inp.readlines()
    ids = sorted([calculate_seat_id(t.rstrip()) for t in tickets])
    print('Max ID: {}'.format(ids[-1]))
    for i in range(1, len(ids)):
        if ids[i] != ids[i-1] + 1:
            print('My ID: {}'.format(ids[i]-1))
            break
