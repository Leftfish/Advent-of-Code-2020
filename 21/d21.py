from collections import defaultdict

print('Day 21 of Advent of Code!')


def parse_line(line):
    left, right = line.split(' (contains ')
    ingredients = left.split(' ')
    allergens = right[:-1].split(', ')
    return ingredients, set(allergens)


def separate_suspicious_and_safe(meals):
    ingedient_counter = defaultdict(int)
    allergen_to_ingredient = defaultdict(set)
    all_ingredients = set()

    for meal in meals:
        ingredients, allergens = parse_line(meal)
        all_ingredients |= set(ingredients)
        for allergen in allergens:
            if allergen not in allergen_to_ingredient:
                allergen_to_ingredient[allergen] = set(ingredients)
            else:
                allergen_to_ingredient[allergen] &= set(ingredients)
        for ingredient in ingredients:
            ingedient_counter[ingredient] += 1

    dangerous = set()
    for s in allergen_to_ingredient.values():
        dangerous.update(s)

    not_dangerous = all_ingredients - dangerous

    return sum(ingedient_counter[ingredient] for ingredient in not_dangerous), allergen_to_ingredient


def sieve_ingredients_with_allergenes(allergen_to_ingredient):
    while True:
        for k in allergen_to_ingredient:
            if len(allergen_to_ingredient[k]) == 1:
                to_del = list(allergen_to_ingredient[k])[-1]
                for kp in allergen_to_ingredient:
                    if kp != k and to_del in allergen_to_ingredient[kp]:
                        allergen_to_ingredient[kp].remove(to_del) 
        if sum(len(v) for v in allergen_to_ingredient.values()) == len(allergen_to_ingredient.values()):
            break
    return allergen_to_ingredient


def get_canonical_list(allergen_to_ingredient):
    ingredient_to_allergen = {list(item[1])[0]: item[0] for item in allergen_to_ingredient.items()}
    sorted_items = sorted(ingredient_to_allergen.items(), key=lambda item: item[1])
    return ','.join(item[0] for item in sorted_items)


test = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''

lines = [l for l in test.split('\n')]

safe, suspicious = separate_suspicious_and_safe(lines)
allergen_to_ingredient = sieve_ingredients_with_allergenes(suspicious)

print('Tests...')
print('Number of safe ingredients', safe == 5)
print('Canonical list:', get_canonical_list(allergen_to_ingredient) == 'mxmxvkd,sqjhc,fvjkl')
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    lines = [l.rstrip() for l in inp.readlines()]

    safe, suspicious = separate_suspicious_and_safe(lines)
    allergen_to_ingredient = sieve_ingredients_with_allergenes(suspicious)

    print('Number of safe ingredients:', safe)
    print('Canonical list:', get_canonical_list(allergen_to_ingredient))