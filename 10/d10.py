from collections import defaultdict

print('Day 10 of Advent of Code!')


def check_joltages(joltages, end):
    ones = 0
    threes = 0
    joltages = joltages + [end+3]
    diffs = []
    for i in range(len(joltages)-1):
        cur = joltages[i]
        nxt = joltages[i + 1]
        diffs.append(nxt - cur)
        if nxt - cur == 1:
            ones += 1
        elif nxt - cur == 3:
            threes += 1
        elif nxt - cur >= 4:
            return 0, 0
        if i == len(joltages):
            print(joltages[i])
    return ones, threes, diffs


def sum_diffs_permutations(diffs):
    d = defaultdict(int)
    buffer = []
    for i in range(len(diffs)):
        if diffs[i] == 1:
            buffer.append(diffs[i])
        elif diffs[i] == 3:
            if len(buffer) > 1:
                d[len(buffer)] += 1
            buffer = []
    d[len(buffer)] += 1
    ''' This is such an UGLY hack which rests upon knowing
    that permutations occur only after multiple jumps of 1,
    that there are at most four consecutive ones and in how
    many ways you can make the jump by 2, 3 and 4.'''
    return 7**d[4] * 4**d[3] * 2**d[2] 


test_joltages = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

print('Tests...')
joltages = [0] + sorted([int(i) for i in test_joltages.split('\n')])
results = check_joltages(joltages, joltages[-1])
print('Multiply jumps:', results[0] * results[1])
print('Possible paths:', sum_diffs_permutations(results[2]))
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    joltages = [0] + sorted([int(i) for i in inp.readlines()])
    results = check_joltages(joltages, joltages[-1])
    print('Multiply jumps:', results[0] * results[1])
    print('Possible paths:', sum_diffs_permutations(results[2]))
