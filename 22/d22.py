from collections import deque

print('Day 21 of Advent of Code!')


test = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

test = '''Player 1:
43
19

Player 2:
2
29
14'''

def parse_decks(data):
    player1, player2 = data.split('\n\n')
    player1 = deque(map(int, player1.splitlines()[1:]))
    player2 = deque(map(int, player2.splitlines()[1:]))
    return player1, player2

   
def play_game(p1, p2):
    rnd = 1
    
    while p1 and p2:
        print("Round {}".format(rnd))
        rnd += 1
        p1_card = p1.popleft()
        p2_card = p2.popleft()

        if p1_card > p2_card:
            p1.extend((p1_card, p2_card))
        elif p2_card > p1_card:
            p2.extend((p2_card, p1_card))
        else:
            raise ValueError("Draw!")
    return p1 if p1 else p2


def calc_score_pt1(deck):
    score = 0
    for i, card in enumerate(reversed(deck), start=1):
        score += card * i
    return score


print('Tests...')
p1, p2 = parse_decks(test)
print(calc_score_pt1(play_game(p1.copy(), p2.copy())))
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    p1, p2 = parse_decks(inp.read())
    #print(calc_score_pt1(play_game(p1.copy(), p2.copy())))
