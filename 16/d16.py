import re

print('Day 16 of Advent of Code!')


test = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

test_2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

def split_nearby_tickets(notes):
    split = notes.find('nearby tickets') + 16
    tickets = notes[split:]
    notes = notes[:split-18]
    return notes, tickets

def parse_tickets(tickets):
    nearby_tickets = []
    for line in tickets.split('\n'):
        ticket = list(map(int, line.split(',')))
        nearby_tickets.append(ticket)
    return nearby_tickets

def split_my_ticket(notes):
    split = notes.find('your ticket') + 13
    my_ticket = notes[split:]
    notes = notes[:split-15]
    return notes, my_ticket

def parse_my_ticket(my_ticket):
    return list(my_ticket.split(','))

def parse_rules(notes):
    rules = {}
    for line in notes.split('\n'):
        name, lmin, lmax, hmin, hmax = re.match(r'([\w|\s]+): (\d+)-(\d+) or (\d+)-(\d+)',line).groups()
        numbers = set(range(int(lmin), int(lmax)+1)) | set(range(int(hmin), int(hmax)+1))
        rules[name] = numbers
    return rules

def parse_notes(notes):
    notes, nearby_tickets = split_nearby_tickets(notes)
    notes, my_ticket = split_my_ticket(notes)
    nearby_tickets = parse_tickets(nearby_tickets)
    my_ticket = parse_my_ticket(my_ticket)
    rules = parse_rules(notes)
    return rules, my_ticket, nearby_tickets

def check_ticket(ticket, rules):
    invalid_values = set()
    all_rules = set()
    for rule in rules:
        all_rules.update(rules[rule])
    for digit in ticket:
        if digit not in all_rules:
            invalid_values.add(digit)
    return invalid_values

def find_valid_tickets(tickets, rules):
    valid_tickets = []
    s = 0
    for ticket in nearby_tickets:
        checksum = sum(check_ticket(ticket, rules))
        if checksum == 0:
            valid_tickets.append(ticket)
        else:
            s += checksum
    return s, valid_tickets

def find_candidates(field, tickets, rules):
    not_valid = []
    for ticket in tickets:
        for f in range(len(tickets[0])):
            if ticket[f] not in rules[field]:
                not_valid.append(f)
    return not_valid

def go(fields, tickets, rules):
    r = {}
    checker = set(range(len(tickets[0])))
    for field in fields:
        res = set(find_candidates(field, valid_tickets, rules))
        r[field] = checker - res
    return r

print('Tests...')
rules, my_ticket, nearby_tickets = parse_notes(test)
solution_pt1, valid_tickets = find_valid_tickets(nearby_tickets, rules)
print("Sum of invalid fields:", solution_pt1 == 71)

rules, my_ticket, nearby_tickets = parse_notes(test_2)
_, valid_tickets = find_valid_tickets(nearby_tickets, rules)
fields = rules.keys()
#go(fields, valid_tickets, rules)

print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    test = inp.read()

    rules, my_ticket, nearby_tickets = parse_notes(test)
    solution_pt1, valid_tickets = find_valid_tickets(nearby_tickets, rules)
    print("Sum of invalid fields:", solution_pt1)
    fields = rules.keys()
    candidates = go(fields, valid_tickets, rules)
    sorted_candidates = {k: v for k, v in sorted(candidates.items(), key=lambda item: len(item[1]))}
    seen = set()
    result = {}
    for field in sorted_candidates:
        vals = sorted_candidates[field]
        proper = vals - seen
        result[field] = proper
        seen.update(proper)
    print(result)
    res = 1
    for k in result:
        if "departure" in k:
            res *= int(my_ticket[sum(result[k])])
    print(res)

    
    