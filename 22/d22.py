from collections import deque
from itertools import islice

print('Day 22 of Advent of Code!')

PLAYER_1 = 'PLAYER 1'
PLAYER_2 = 'PLAYER 2'

def parse_decks(data):
    player1, player2 = data.split('\n\n')
    player1_deck = deque(map(int, player1.splitlines()[1:]))
    player2_deck = deque(map(int, player2.splitlines()[1:]))
    return player1_deck, player2_deck


def play_game(player1_deck, player2_deck):
    while player1_deck and player2_deck:
        p1_card = player1_deck.popleft()
        p2_card = player2_deck.popleft()

        if p1_card > p2_card:
            player1_deck.extend((p1_card, p2_card))
        elif p2_card > p1_card:
            player2_deck.extend((p2_card, p1_card))
        else:
            raise ValueError('Draw! Something not right with the input decks.')

    return player1_deck if player1_deck else player2_deck


def play_game_rec(player1_deck, player2_deck, debug=False):
    used_p1 = set()
    used_p2 = set()

    while player1_deck and player2_deck:

        check_deck_p1, check_deck_p2 = tuple(player1_deck), tuple(player2_deck)

        if check_deck_p1 in used_p1 or check_deck_p2 in used_p2:
            return (player1_deck, PLAYER_1)
        else:
            used_p1.add(check_deck_p1)
            used_p2.add(check_deck_p2)

        p1_card = player1_deck.popleft()
        p2_card = player2_deck.popleft()

        recursive_score = None

        if p1_card <= len(player1_deck) and p2_card <= len(player2_deck):
            p1_rec_deck = deque(islice(player1_deck, 0, p1_card))
            p2_rec_deck = deque(islice(player2_deck, 0, p2_card))
            
            if max(p1_rec_deck) > max(p2_rec_deck):
                recursive_score = PLAYER_1
            else:
                recursive_score = play_game_rec(p1_rec_deck, p2_rec_deck)[1]

        if recursive_score == PLAYER_1:
            player1_deck.extend((p1_card, p2_card))
        elif recursive_score == PLAYER_2:
            player2_deck.extend((p2_card, p1_card))
        elif p1_card > p2_card:
            player1_deck.extend((p1_card, p2_card))
        elif p2_card > p1_card:
            player2_deck.extend((p2_card, p1_card))
        else:
            raise ValueError('Draw! Something not right with the input decks.')

    return (player1_deck, PLAYER_1) if player1_deck else (player2_deck, PLAYER_2)


def calc_score(winning_deck):
    score = 0
    for i, card in enumerate(reversed(winning_deck), start=1):
        score += card * i
    return score


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

print('Tests...')
p1, p2 = parse_decks(test)
print('Score without recursion:', calc_score(play_game(p1.copy(), p2.copy())) == 306)
print('Score with recursion:', calc_score(play_game_rec(p1.copy(), p2.copy())[0]) == 291)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    decks = inp.read()
    p1, p2 = parse_decks(decks)
    print('Score without recursion:', calc_score(play_game(p1.copy(), p2.copy())))
    print('Score with recursion:', calc_score(play_game_rec(p1.copy(), p2.copy())[0]))
