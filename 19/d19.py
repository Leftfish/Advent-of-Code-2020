import re

print('Day 19 of Advent of Code!')


test = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

raw_rules, messages = test.split('\n\n')
raw_rules = raw_rules.split('\n')
messages = messages.split('\n')

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

rules = parse_rules(raw_rules)
regex = r'^{}$'.format(make_regex('0', rules))

print('Tests...')
print('Proper messages, part 1:', sum(1 for message in messages if re.match(regex, message)) == 2)    
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    raw_rules, messages = inp.read().split('\n\n')
    raw_rules = raw_rules.split('\n')
    messages = messages.split('\n')
    
    rules = parse_rules(raw_rules)
    regex = r'^{}$'.format(make_regex('0', rules))
    print('Proper messages, part 1:', sum(1 for message in messages if re.match(regex, message)))     
    