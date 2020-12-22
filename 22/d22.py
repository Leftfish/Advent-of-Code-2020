from collections import deque
from itertools import islice

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

def parse_decks(data):
    player1, player2 = data.split('\n\n')
    player1 = deque(map(int, player1.splitlines()[1:]))
    player2 = deque(map(int, player2.splitlines()[1:]))
    return player1, player2

   
def play_game(p1, p2):
    while p1 and p2:
        p1_card = p1.popleft()
        p2_card = p2.popleft()

        if p1_card > p2_card:
            p1.extend((p1_card, p2_card))
        elif p2_card > p1_card:
            p2.extend((p2_card, p1_card))
        else:
            raise ValueError("Draw!")
    
    return p1 if p1 else p2


def play_game_rec(p1, p2, debug=False):
    if debug:
        print("!!! NEW GAME")
    rnd = 1
    used_p1 = set()
    used_p2 = set()

    while p1 and p2:
        if debug:
            print("Round {}".format(rnd))
        if tuple(p1) in used_p1 or tuple(p2) in used_p2:
            return p1, 1
        else:
            used_p1.add(tuple(p1))
            used_p2.add(tuple(p2))
        
        p1_card = p1.popleft()
        p2_card = p2.popleft()
        if debug:
            print(f"P1 plays {p1_card} P2 plays {p2_card}")

        go_recursive = p1_card <= len(p1) and p2_card <= len(p2)
        rec_score = 0

        if go_recursive:
            p1_rec = deque(islice(p1, 0, p1_card))
            p2_rec = deque(islice(p2, 0, p2_card))
            if debug:
                print("REC with", p1_rec, p2_rec)
            rec_score = play_game_rec(p1_rec, p2_rec)[1]
            if debug:
                print("BACK")


        if rec_score == 1: 
            p1.extend((p1_card, p2_card))
            if debug:
                print("Player 1 wins round thanks to rec ", rnd)
                print("P1", p1)
                print("P2", p2)
        elif rec_score == 2:
            p2.extend((p2_card, p1_card))
            if debug:
                print("Player 2  wins round thanks to rec ", rnd)
                print("P1", p1)
                print("P2", p2)
        elif p1_card > p2_card:
            p1.extend((p1_card, p2_card))
            if debug:
                print("Player 1  wins round ", rnd)
                print("P1", p1)
                print("P2", p2)
        elif p2_card > p1_card:
            p2.extend((p2_card, p1_card))
            if debug:
                print("Player 2  wins round ", rnd)
                print("P1", p1)
                print("P2", p2)
        else:
            raise ValueError("Draw!")
        rnd += 1

    if p1:
        #print("### P1 wins game")
        
        return p1, 1
    else:
        #print("### P2 wins game")
        return p2, 2

def calc_score(deck):
    score = 0
    for i, card in enumerate(reversed(deck), start=1):
        score += card * i
    return score


print('Tests...')
p1, p2 = parse_decks(test)
print(calc_score(play_game(p1.copy(), p2.copy())))
print(calc_score(play_game_rec(p1.copy(), p2.copy())[0]))
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    decks = inp.read()
    p1, p2 = parse_decks(decks)
    #print(calc_score(play_game(p1.copy(), p2.copy())))
    print(calc_score(play_game_rec(p1.copy(), p2.copy())[0]))
