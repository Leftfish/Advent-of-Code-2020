from re import findall
from collections import defaultdict


print('Day 14 of Advent of Code!')


def create_mask(pattern):
    mask = {}
    for i, char in enumerate(pattern):
        if char != 'X':
            mask[i] = int(char)
        else:
            mask[i] = char
    return mask


def to_bit_array(n, bits):
    b = bin(n)[2:].zfill(bits)
    bit_array = list(map(int, b))
    return bit_array


def apply_mask(value, mask, bits, mode=1):
    buffer = [0] * bits
    to_write = to_bit_array(value, bits)
    for i in range(len(buffer)):
        if mode == 1 and mask[i] != 'X':
            buffer[i] = mask[i]
        elif mode == 2 and mask[i]:
            buffer[i] = mask[i]
        else:
            buffer[i] = to_write[i]
    buffer = ''.join(map(str, buffer))
    return buffer


def create_addr_lst(val, mask, bits):
    addr = apply_mask(val, mask, bits, mode=2)
    floats = addr.count('X')
    permutes = [bin(x)[2:].rjust(floats, '0') for x in range(2**floats)]

    addr_list = []

    for p in permutes:
        addr_tolist = list(addr)
        i = 0
        for j in range(len(addr)):
            bit = p[i]
            if addr_tolist[j] == 'X':
                addr_tolist[j] = bit
                i += 1
                if i >= len(p):
                    break
        addr_list.append(''.join(addr_tolist))

    return list(int(a, 2) for a in addr_list)


def update_memory(memory, address, value):
    memory[address] = value


def parse_line(line):
    l = line.split(' = ')
    op, val, addr = l[0], None, None
    if op == 'mask':
        val = l[1]
    else:
        val = int(l[1])
        addr = int(findall(r'\d+', op)[0])
    return op, val, addr


def run_program(program, memory, bits, mode):
    mask = 'X' * bits
    for line in program:
        op, val, addr = parse_line(line)
        if op == 'mask':
            mask = create_mask(val)
        else:
            if mode == 1:
                to_write = int('0b' + apply_mask(val, mask, bits, mode=1), 2)
                update_memory(memory, addr, to_write)
            elif mode == 2:
                addresses = create_addr_lst(addr, mask, bits)
                for address in addresses:
                    update_memory(memory, address, val)
            else:
                raise ValueError("Invalid mode (only supports mode 1 or 2)")
    return memory


test = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

test_2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

print('Tests...')
data = test.split('\n')
data_2 = test_2.split('\n')
memory = defaultdict(int)
memory_2 = defaultdict(int)
bits = 36
print("Sum of values:", sum(run_program(data, memory, bits, mode=1).values()) == 165)
print("Sum of values:", sum(run_program(data_2, memory_2, bits, mode=2).values()) == 208)

print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    data = [l.rstrip() for l in inp.readlines()]
    memory = defaultdict(int)
    memory_2 = defaultdict(int)
    print("Sum of values:", sum(run_program(data, memory, bits, mode=1).values()))
    print("Sum of values:", sum(run_program(data, memory_2, bits, mode=2).values()))
