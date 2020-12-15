from collections import defaultdict


print('Day 15 of Advent of Code!')


def run_game(initial, turns=2020):
    results = defaultdict(lambda: (0, 0))
    prev = None
    current = initial[0]
    time = 1

    while time <= turns:
        if time <= len(initial):
            prev = current
            current = initial[time-1]
            results[current] = (0, time)
        else:
            prev = current
            if results[prev][0] == 0:
                current = 0
            else:
                current = results[prev][1] - results[prev][0]
            prev_time = results[current][1]
            results[current] = (prev_time, time)
        if time == turns:
            return current
        time += 1


print('Tests...')
print('Number after 2020 turns: ', run_game([0, 3, 6], 2020) == 436)
print('---------------------')
print('Solution...')
puzzle = [15, 5, 1, 4, 7, 0]
print('Number after 2020 turns: ', run_game(puzzle, 2020))
print('Number after 30000000 turns: ', run_game(puzzle, 30000000))
