import random
from art import logo

def deal_card():
    """return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """take  a  list of cards from cards and return the result of the cards by calculating form"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(u_score, c_score):
    if c_score == u_score:
        return "Draw"
    elif c_score  == 0:
        return"you loose"
    elif u_score == 0:
        return "you won"
    elif  u_score >21:
        return "you loss"
    elif c_score > 21:
        return "opponent went over you win"
    elif u_score > c_score:
        return "you win "
    else:
        return "you lose"

def play_game_again():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    user_score= -1
    computer_score= -1
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards{user_cards} , current score {user_score}")
        print(f"computer's first card :{computer_cards[0]}")

