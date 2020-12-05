import turtle
import re
from time import sleep
from random import choice

print("Day 4 of Advent of Code!")

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
    valid_passports = []
    for entry in entries:
        if is_valid_entry(entry, oblig_fields):
            has_required_fields += 1
            passport = create_passport(entry, year_fields)
            if validate_passport(passport, year_fields, eye_field, passport_id_field, hair_color_field, height_field):
                valid_passports.append(passport)
    return has_required_fields, valid_passports

def draw_person(t, passport):
    def execute_moves(moves):
        for mv in moves:
            mv[0](mv[1]) if mv[1] else mv[0]()

    def draw_eye():
        t.fillcolor(eye_color)
        t.begin_fill()
        for _ in range(4):
            t.fd(20)
            t.rt(90)
        t.end_fill()
    
    eye_palette = {'amb': '#FFBF00', 'blu': '#85abce', 'brn': '#b86e07', 'gry': '#8f8b85', 'grn': '#32cd32', 'hzl': '#8e7618', 'oth': '#ff0000'}
    eye_color = eye_palette[passport['ecl']]
    hair_size = choice(range(5, 35))
    hair_color = passport['hcl']
    mouth_color = '#000000'
    tongue_color = '#FF0000'
    skin_tone = choice(['#fdf5e2', '#fbefba', '#ffd6a4', '#c68642', '#4b3932'])
    height_data = passport['hgt']
    
    if height_data.endswith('cm'):
        height = '{} cm ({} in)'.format(height_data[:-2], int(int(height_data[:-2]) / 2.54))
    else:
        height = '{} cm ({} in)'.format(int(int(height_data[:-2]) * 2.54), height_data[:-2])

    # Set up
    t.clear()
    t.penup()
    t.goto(-80, 120)
    t.setheading(0)
    # Face
    t.fillcolor(skin_tone)
    t.begin_fill()
    for _ in range(4):
        t.fd(160)
        t.rt(90)
    t.end_fill()
    # Hair
    hair = [(t.begin_fill, None), (t.fillcolor, hair_color), (t.fd, 160), (t.rt,90), (t.fd, hair_size), (t.rt,90), (t.fd, 160), (t.rt,90), (t.fd, hair_size), (t.end_fill, None)]
    execute_moves(hair)
    t.setheading(0)
    # Transfer to eyes
    transfer_eyes = [(t.fd, 40), (t.rt,90), (t.fd, 40)]
    execute_moves(transfer_eyes)
    # Eyes
    draw_eye()
    t.setheading(0)
    t.fd(60)
    draw_eye()
    # Transfer to mouth
    transfer_mouth = [(t.fd, 20), (t.rt,90), (t.fd, 60), (t.lt, 90)]
    execute_moves(transfer_mouth)
    # Mouth
    mouth = [(t.fillcolor, mouth_color), (t.begin_fill, None), (t.fd, 20), (t.rt,90), (t.fd, 20), (t.rt,90), (t.fd, 20), (t.lt, 90), (t.fd, 20), (t.rt,90), (t.fd, 80), (t.rt,90), (t.fd, 20), (t.lt, 90), (t.fd, 20), (t.rt,90), (t.fd, 20), (t.rt,90), (t.fd, 100), (t.end_fill, None)]
    execute_moves(mouth)
    # Tongue
    tongue = [(t.fillcolor, tongue_color), (t.rt,90), (t.fd, 20), (t.rt,90), (t.fd, 35), (t.begin_fill, None), (t.fd, 30), (t.rt,90), (t.fd, 10), (t.rt,90), (t.fd, 35), (t.rt,90), (t.fd, 10), (t.end_fill, None)]
    execute_moves(tongue)
    # Write information
    t.goto(t.xcor()-80, t.ycor()-60)
    t.write("Year of birth: {}".format(passport['byr']))
    t.sety(t.ycor()-15)
    t.write("Passport issued in: {}".format(passport['iyr']))
    t.sety(t.ycor()-15)
    t.write("Passport valid until: {}".format(passport['eyr']))
    t.sety(t.ycor()-15)
    t.write("Passport ID: {}".format(passport['pid']))
    t.sety(t.ycor()-15)
    t.write("Height: {}".format(height))

def animate_passports(valid_passports):
    t = turtle.Turtle()
    s = turtle.Screen()
    s.setup(width=340, height=400)
    s.title("Day 4 of Advent of Code 2020!")
    s.screensize(300, 360)
    t.speed(0)
    t.hideturtle()
    for passp in valid_passports:
        draw_person(t, passp)
        sleep(2)
    s.exitonclick()

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
print("Bad passports OK:", len(validate_batch(bad_test_passports.split('\n\n'), OBLIG_FIELDS, YEAR_FIELDS, EYE_FIELD, PASSPORT_ID_FIELD, HAIR_COLOR_FIELD, HEIGHT_FIELD)[1]) == 0)
print("Good passports OK:", len(validate_batch(good_test_passports.split('\n\n'), OBLIG_FIELDS, YEAR_FIELDS, EYE_FIELD, PASSPORT_ID_FIELD, HAIR_COLOR_FIELD, HEIGHT_FIELD)[1]) == len(good_test_passports.split('\n\n')))
print("---------------------")
 
with open("input", mode = 'r') as inp:
    print("Solution...")
    entries = inp.read().split('\n\n')
    has_fields, valid_passports = validate_batch(entries, OBLIG_FIELDS, YEAR_FIELDS, EYE_FIELD, PASSPORT_ID_FIELD, HAIR_COLOR_FIELD, HEIGHT_FIELD)
    print("{} have required fields, {} are valid.".format(has_fields, len(valid_passports)))
    animate_passports(valid_passports)
