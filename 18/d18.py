print('Day 18 of Advent of Code!')

def parse_expression(tokens, mode=1):
    queue, stack = [], []
    ops = {'+': 1, '*': 1} if mode == 1 else {'+': 2, '*': 1}
    for token in tokens:
        if token in ops:
            while stack and stack[-1] in ops:
                if ops[token] <= ops[stack[-1]]:
                    queue.append(stack.pop())
                break
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                queue.append(stack.pop())
            stack.pop()
        else:
            queue.append(token)
    while stack:
        queue.append(stack.pop())
    return queue


def evaluate_expression(queue):
    stack = []
    for token in queue:
        if token.isnumeric():
            stack.append(token)
        elif token in '+*':
            second = stack.pop()
            first = stack.pop()
            expression = " ".join([first, token, second])
            res = eval(expression)
            stack.append(str(res))
    return int(stack[-1])

test_exp = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
print("Part 1: 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) = 12240:", evaluate_expression(parse_expression(list(test_exp.replace(" ", "")), mode=1)) == 12240)
print("Part 2: 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) = 669060:", evaluate_expression(parse_expression(list(test_exp.replace(" ", "")), mode=2)) == 669060)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    test = [l.rstrip() for l in inp.readlines()]
    print("Part 1:", sum(evaluate_expression(parse_expression(list(line.replace(" ", "")), mode=1)) for line in test))
    print("Part 2:", sum(evaluate_expression(parse_expression(list(line.replace(" ", "")), mode=2)) for line in test))
