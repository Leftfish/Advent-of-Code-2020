from re import findall
from collections import defaultdict


print('Day 14 of Advent of Code!')


def create_mask(pattern):
    d = {}
    for i, char in enumerate(pattern):
        if char != 'X':
            d[i] = int(char)
        else:
            d[i] = char
    return d


def to_36bit_array(n):
    b = bin(n)[2:].zfill(36)
    return list(map(int, b))


def apply_mask(value, mask):
    buffer = [0] * 36
    to_write = to_36bit_array(value)
    for i in range(len(buffer)):
        if i in mask and mask[i] != 'X':
            buffer[i] = mask[i]
        else:
            buffer[i] = to_write[i]
    buffer = ''.join(map(str, buffer))
    return buffer


def apply_mask_to_addr(value, mask):
    buffer = [0] * 36
    to_write = to_36bit_array(value)
    for i in range(len(buffer)):
        if i in mask and mask[i]:
            buffer[i] = mask[i]
        else:
            buffer[i] = to_write[i]
    buffer = ''.join(map(str, buffer))
    return buffer


def create_addr_lst(val, mask):
    addr = apply_mask_to_addr(val, mask)
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


def run_program(program, memory, mode):
    mask = 'X' * 36
    for line in program:
        op, val, addr = parse_line(line)
        if op == 'mask':
            mask = create_mask(val)
        else:
            if mode == 1:
                to_write = int('0b' + apply_mask(val, mask), 2)
                update_memory(memory, addr, to_write)
            elif mode == 2:
                addresses = create_addr_lst(addr, mask)
                for address in addresses:
                    update_memory(memory, address, val)
            else:
                raise ValueError("Invalid mode (only supports mode 1 or 2)")
    return sum(memory.values())
        

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
print("Sum of values:", run_program(data, memory, mode=1) == 165)
print("Sum of values:", run_program(data_2, memory_2, mode=2) == 208)

print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    data = [l.rstrip() for l in inp.readlines()]
    memory = defaultdict(int)
    memory_2 = defaultdict(int)
    print("Sum of values:", run_program(data, memory, mode=1))
    print("Sum of values:", run_program(data, memory_2, mode=2))
