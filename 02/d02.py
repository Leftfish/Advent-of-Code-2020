from collections import Counter
from re import match

print("Day 2 of Advent of Code!")

def parse_line(line):
    parsed = match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    policy = (parsed[2], int(parsed[0]), int(parsed[1]))
    password = parsed[3]
    return policy, password

def validate_password_count(policy, password):
    c = Counter(password)
    char = policy[0]
    mn, mx = policy[1], policy[2]
    if char not in c or c[char] < mn or c[char] > mx:
        return False
    return True

def validate_password_positional(policy, password):
    char = policy[0]
    pos1, pos2 = policy[1]-1, policy[2]-1
    first = password[pos1] if pos1 < len(password) else None
    second = password[pos2] if pos2 < len(password) else None
    return (first == char) ^ (second == char)

print("Tests...")

test_lines = [("1-3 a: abcde", True, True), ("1-3 b: cdefg", False, False), ("2-9 c: ccccccccc", True, False)]

for l in test_lines:
    policy, password = parse_line(l[0])
    print(l[0])
    print("Part 1:", validate_password_count(policy, password) == l[1])
    print("Part 2:", validate_password_positional(policy, password) == l[2])

print("---------------------")

print("Solution...")

with open("input", mode = 'r') as inp:
    score_part1, score_part2 = 0, 0
    for line in inp:
        policy, password = parse_line(line.rstrip())
        if validate_password_count(policy, password):
            score_part1 += 1
        if validate_password_positional(policy, password):
            score_part2 += 1
    print("Valid passwords (counter):", score_part1, "\nValid passwords (positional):", score_part2)
