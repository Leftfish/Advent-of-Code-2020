import re

def is_valid_entry(entry, oblig_fields):
    return all(field in entry for field in oblig_fields)

def create_passport(line, year_fields):
    passport = {}
    for l in line.split():
        k = l[:3]
        v = int(l[4:]) if k in year_fields else l[4:]
        passport[k] = v
    return passport

def validate_passport(passport, year_fields, eye_field, passport_id_field, hair_color_field, height_field):
    for k in passport:
        entry = passport[k]
        if k in year_fields and not (year_fields[k][1] >= entry >= year_fields[k][0]):
            return False
        if k in eye_field and entry not in eye_field[k]:
            return False 
        if k in passport_id_field and not re.fullmatch(passport_id_field[k], entry):
            return False
        if k in hair_color_field and not re.fullmatch(hair_color_field[k], entry):
            return False
        if k in height_field:
            unit = entry[-2:]
            heights = height_field[k]
            if unit not in heights:
                return False
            else:
                height = int(entry[:-2])
                min_height, max_height = int(heights[unit][0]), int(heights[unit][1])
                if not max_height >= height >= min_height:
                    return False
    return True

def validate_batch(entries, oblig_fields, year_fields, eye_field, passport_id_field, hair_color_field, height_field):
    has_required_fields = 0
    valid = 0
    for entry in entries:
        if is_valid_entry(entry, oblig_fields):
            has_required_fields += 1
            passport = create_passport(entry, year_fields)
            if validate_passport(passport, year_fields, eye_field, passport_id_field, hair_color_field, height_field):
                valid += 1
    return has_required_fields, valid

OBLIG_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
YEAR_FIELDS = {'byr': (1920, 2002), 'iyr': (2010, 2020), 'eyr': (2020, 2030)}
EYE_FIELD = {'ecl': ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')}
HEIGHT_FIELD = {'hgt': {'in': (59, 76), 'cm': (150, 193)}}
HAIR_COLOR_FIELD = {'hcl': r'#[0-9a-f]{6}'}
PASSPORT_ID_FIELD = {'pid': r'\d{9}'}
OPTIONAL_FIELDS = ('cid')

bad_test_passports = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

good_test_passports = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

print("Tests...")
print("Bad passports OK:", validate_batch(bad_test_passports.split('\n\n'), OBLIG_FIELDS, YEAR_FIELDS, EYE_FIELD, PASSPORT_ID_FIELD, HAIR_COLOR_FIELD, HEIGHT_FIELD)[1] == 0)
print("Good passports OK:", validate_batch(good_test_passports.split('\n\n'), OBLIG_FIELDS, YEAR_FIELDS, EYE_FIELD, PASSPORT_ID_FIELD, HAIR_COLOR_FIELD, HEIGHT_FIELD)[1] == len(good_test_passports.split('\n\n')))

with open("input", mode = 'r') as inp:
    print("Solution...")
    entries = inp.read().split('\n\n')
    results = validate_batch(entries, OBLIG_FIELDS, YEAR_FIELDS, EYE_FIELD, PASSPORT_ID_FIELD, HAIR_COLOR_FIELD, HEIGHT_FIELD)
    print("{} have required fields, {} are valid.".format(*results))
