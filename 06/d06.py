from functools import reduce

print('Day 6 of Advent of Code!')


def count_anyone(forms):
    return sum(len(set(form.replace('\n', ''))) for form in forms.split('\n\n'))


def count_everyone(forms):
    return sum((len(reduce(lambda a, b: a & b, (set(x) for x in form.split('\n')))) for form in forms.split('\n\n')))

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

print('Tests...')
print('Sum of ANY YES answers in test forms:', count_anyone(test_forms) == 11)
print('Sum of ALL YES answers in test forms:', count_everyone(test_forms) == 6)
print('---------------------')

with open('input', mode='r') as inp:
    forms = inp.read()
    print('Solution...')
    print('Sum of ANY YES answers in forms:', count_anyone(forms))
    print('Sum of ALL YES answers in forms:', count_everyone(forms))
