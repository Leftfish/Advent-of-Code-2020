print('Day 8 of Advent of Code!')


test_program = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


def parse_commands(inp):
    program = inp.split('\n')
    commands = []
    i = 0
    for command in program:
        parsed = command.split()
        commands.append([i, parsed[0], int(parsed[1])])
        i += 1
    return commands


def run_program(commands, part=1):
    executed = set()
    pointer = 0
    acc = 0
    while pointer <= len(commands)-1:
        current = commands[pointer]
        op, arg = current[1], current[2]
        if pointer in executed:
            if part == 1:
                return None, acc
            elif part == 2:
                return False, acc
        if op == 'nop':
            executed.add(pointer)
            pointer += 1
        elif op == 'acc':
            executed.add(pointer)
            acc += arg
            pointer += 1
        elif op == 'jmp':
            executed.add(pointer)
            pointer += arg
    if part == 2:
        return True, acc


def find_suspect_operations(commands):
    suspects = []
    for command in commands:
        op_id, op = command[0], command[1]
        if op in ('nop', 'jmp'):
            suspects.append(op_id)
    return suspects


def debug(program):
    suspects = find_suspect_operations(program)
    for s in suspects:
        op = program[s][1]
        if op == 'nop':
            new_prog = [op[:] for op in program]
            new_prog[s][1] = 'jmp'
            result = run_program(new_prog, part=2)
            if result[0]:
                print('Switched nop to jmp at {}.'.format(s))
                return result[1]
            continue
        elif op == 'jmp':
            new_prog = [op[:] for op in program]
            new_prog[s][1] = 'nop'
            result = run_program(new_prog, part=2)
            if result[0]:
                print('Switched jmp to nop at {}.'.format(s))
                return result[1]
            continue

print('Tests...')
program = parse_commands(test_program)
print('Accumulator state after first loop:', run_program(program)[1])
print('Accumulator state after debug:', debug(program))
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    program = parse_commands(inp.read())
    print('Accumulator state after first loop:', run_program(program)[1])
    print('Accumulator state after debug:', debug(program))
