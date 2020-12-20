import re


print('Day 19 of Advent of Code!')


def parse_rules(raw_rules):
    rules = {}
    for rule in raw_rules:
        num, rule = rule.split(': ')
        r = rule.split(' ')
        for i in range(len(r)):
            if '"' in r[i]:
                r[i] = r[i][1:-1]
        rules[num] = r
    return rules


def make_regex(r, rules):
    if rules[r][0] in 'ab':
        return rules[r][0]
    group = '('
    for rule in rules[r]:
        if rule == '|':
            group += rule
        else:
            group += make_regex(rule, rules)
    group += ')'
    return group


def count_part1(regex, messages):
    return sum(1 for message in messages if re.fullmatch(regex, message))


def count_part2(r42, r31, messages):
    counter, repeat = 0, 1
    while True:
        current = counter
        regex = r'({0}+{0}{{{2}}}{1}{{{2}}})'.format(r42, r31, repeat)
        for message in messages:
            if re.fullmatch(regex, message):
                counter += 1
        if counter == current:
            break
        repeat += 1
    return counter

test = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''

raw_rules, messages = test.split('\n\n')
raw_rules = raw_rules.split('\n')
messages = messages.split('\n')
rules = parse_rules(raw_rules)

regex = r'^{}$'.format(make_regex('0', rules))
r42 = r'{}'.format(make_regex('42', rules))
r31 = r'{}'.format(make_regex('31', rules))

print('Tests...')
print('Proper messages, part 1:', count_part1(regex, messages) == 3)
print('Proper messages, part 2:', count_part2(r42, r31, messages) == 12)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    raw_rules, messages = inp.read().split('\n\n')
    raw_rules = raw_rules.split('\n')
    messages = messages.split('\n')

    rules = parse_rules(raw_rules)
    regex = r'^{}$'.format(make_regex('0', rules))
    r42 = r'{}'.format(make_regex('42', rules))
    r31 = r'{}'.format(make_regex('31', rules))

    print('Proper messages, part 1:', count_part1(regex, messages))
    print('Proper messages, part 2:', count_part2(r42, r31, messages))
