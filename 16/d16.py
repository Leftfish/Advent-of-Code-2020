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

def split_nearby_tickets(notes):
    split = notes.find('nearby tickets') + 16
    tickets = notes[split:]
    notes = notes[:split-18]
    return notes, tickets

def parse_tickets(tickets):
    nearby_tickets = []
    for line in tickets.split('\n'):
        ticket = set(map(int, line.split(',')))
        nearby_tickets.append(ticket)
    return nearby_tickets

def split_my_ticket(notes):
    split = notes.find('your ticket') + 13
    my_ticket = notes[split:]
    notes = notes[:split-15]
    return notes, my_ticket

def parse_my_ticket(my_ticket):
    return set(my_ticket.split(','))

def parse_rules(notes):
    rules = {}
    for line in notes.split('\n'):
        name, lmin, lmax, hmin, hmax = re.match(r'([\w|\s]+): (\d+)-(\d+) or (\d+)-(\d+)',line).groups()
        numbers = set(range(int(lmin), int(lmax)+1)) | set(range(int(hmin), int(hmax)+1))
        rules[name] = numbers
    return rules

def parse_notes(notes):
    notes, nearby_tickets = split_nearby_tickets(test)
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

rules, my_ticket, nearby_tickets = parse_notes(test)

s = 0
for ticket in nearby_tickets:
    s += sum(check_ticket(ticket, rules))
print(s)

print('Tests...')
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    test = inp.read()

    rules, my_ticket, nearby_tickets = parse_notes(test)

    s = 0
    for ticket in nearby_tickets:
        s += sum(check_ticket(ticket, rules))
    print(s)
    
    