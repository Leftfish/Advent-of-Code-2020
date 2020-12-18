print('Day 18 of Advent of Code!')


exp = "1 + (2 * 3) + (4 * (5 + 6))"
exp = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

OPS = {'+': 2, '-': 2, '*': 1, '/': 1}

def parse_expression(tokens, mode=1):
    queue = []
    stack = []
    if mode == 1:
        ops = {'+': 1, '-': 1, '*': 1, '/': 1}
    else:
        ops = {'+': 2, '-': 2, '*': 1, '/': 1}
    for token in tokens:
        if token in OPS:
            while stack and stack[-1] in ops:
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
        elif token in OPS:
            sec = stack.pop()
            fir = stack.pop()
            expr = " ".join([fir, token, sec])
            res = eval(expr)
            stack.append(str(res))

    return int(stack[-1])


print(evaluate_expression(parse_expression(list(exp.replace(" ", "")))))

with open('input', mode='r') as inp:
    print('Solution...')
    test = [l.rstrip() for l in inp.readlines()]
    s = 0
    for l in test:
        s += evaluate_expression(parse_expression(list(l.replace(" ", ""))))
    print(s)