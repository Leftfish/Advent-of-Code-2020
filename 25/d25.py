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
    
card_pub = 8987316
door_pub = 14681524

card_loop = get_loop_size(card_pub, BASE_SUBJECT)
door_loop = get_loop_size(door_pub, BASE_SUBJECT)
encryption_key = transform_key(door_pub, card_loop)
encryption_key_door = transform_key(card_pub, door_loop)

print(f'Encryption key {encryption_key}, encryption key (door) {encryption_key_door}. Authentication {encryption_key == encryption_key_door}.')