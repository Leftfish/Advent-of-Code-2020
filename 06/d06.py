from collections import Counter

print("Day 6 of Advent of Code!")

def count_anyone(form):
    return len(set(form.replace('\n', '')))

def count_everyone(forms):
    res = 0
    for group in forms:
        num_forms = len(group.split('\n'))
        all_forms = ''.join(group.replace('\n', ''))
        c = Counter(all_forms)
        res += sum([1 for k in c if c[k] == num_forms])
    return res

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
print("Sum of YES answers in test forms:", sum([count_anyone(form) for form in forms]) == 11)
print("Sum of ALL YES answers in forms:", count_everyone(forms) == 6)
print("---------------------")

with open("input", mode = 'r') as inp:
    print("Solution...")
    forms = inp.read().split('\n\n')
    print("Sum of ANY YES answers in forms:", sum([count_anyone(form) for form in forms]))
    print("Sum of ALL YES answers in forms:", count_everyone(forms))
