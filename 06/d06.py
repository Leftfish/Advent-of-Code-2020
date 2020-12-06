from functools import reduce

print("Day 6 of Advent of Code!")

def count_anyone(form):
    return len(set(form.replace('\n', '')))

def count_everyone(form):
    return len(reduce(lambda a, b: a & b, (set(x) for x in form.split('\n'))))

test_forms = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

print("Tests...")
forms = test_forms.split('\n\n')
print("Sum of ANY YES answers in test forms:", sum([count_anyone(form) for form in forms]) == 11)
print("Sum of ALL YES answers in forms:", sum([count_everyone(form) for form in forms]) == 6)
print("---------------------")

with open("input", mode = 'r') as inp:
    print("Solution...")
    forms = inp.read().split('\n\n')
    print("Sum of ANY YES answers in forms:", sum([count_anyone(form) for form in forms]))
    print("Sum of ALL YES answers in forms:", sum([count_everyone(form) for form in forms]))
