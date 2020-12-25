print('Day 25 of Advent of Code!')

DIVISOR = 20201227
BASE_SUBJECT = 7
LIMIT = 5_000_000

def get_loop_size(public_key, subject):
    value, i = 1, 0
    while True:
        i += 1
        value *= subject
        value %= DIVISOR
        if value == public_key:
            return i
        if i > LIMIT:
            print('Looks like you need a bigger limit...')
            return -1


def transform_key(public_key, loop_size):
    value = 1
    subject = public_key
    for _ in range(loop_size):
        value *= subject
        value %= DIVISOR
    return value
    

def loop_generator(subject):
    value = 1
    while True:
        value *= subject
        value %= DIVISOR
        yield value

def get_loop_size_alt(pub_key, subject):
    for i, candidate in enumerate(loop_generator(subject), 1):
        if candidate == pub_key:
            return i


card_pub = 8987316
door_pub = 14681524

card_loop = get_loop_size(card_pub, BASE_SUBJECT)
door_loop = get_loop_size(door_pub, BASE_SUBJECT)
encryption_key = transform_key(door_pub, card_loop)
encryption_key_door = transform_key(card_pub, door_loop)
print(f'METHOD 1 (naive): Encryption key {encryption_key}, encryption key (door) {encryption_key_door}. Authentication {encryption_key == encryption_key_door}.')

card_loop = get_loop_size_alt(card_pub, BASE_SUBJECT)
door_loop = get_loop_size_alt(door_pub, BASE_SUBJECT)
encryption_key = pow(card_pub, door_loop, DIVISOR)
encryption_key_door = pow(card_pub, door_loop, DIVISOR)
print(f'METHOD 2 (with generators): Encryption key {encryption_key}, encryption key (door) {encryption_key_door}. Authentication {encryption_key == encryption_key_door}.')