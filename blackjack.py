# Blackjack game project

from random import shuffle

print("Welcome to Blackjack!!\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
stop = False
game_memory = {}

def who_won(players_hand, dealers_hand):
    player_total = sum(players_hand)
    dealer_total = sum(dealers_hand)

    if player_total > 21 and dealer_total < 21:
        return f"""
Your final hand: {players_hand}, final score: {player_total}
Computer's final hand: {dealers_hand}, final score: {dealer_total}
You Lost
"""
    elif player_total > 21 and dealer_total > 21:
        return f"""
Your final hand: {players_hand}, final score: {player_total}
Computer's final hand: {dealers_hand}, final score: {dealer_total}
It's a loss for all involved
"""
    elif player_total == 21 and dealer_total == 21:
        return f"""
Your final hand: {players_hand}, final score: {player_total}
Computer's final hand: {dealers_hand}, final score: {dealer_total}
It's a draw
"""
    elif player_total == dealer_total and dealer_total < 21:
        return f"""
Your final hand: {players_hand}, final score: {player_total}
Computer's final hand: {dealers_hand}, final score: {dealer_total}
It's a draw
"""
    elif dealer_total > player_total and dealer_total <= 21:
        return f"""
Your final hand: {players_hand}, final score: {player_total}
Computer's final hand: {dealers_hand}, final score: {dealer_total}
You Lost
"""
    else:
        return f"""
Your final hand: {players_hand}, final score: {player_total}
Computer's final hand: {dealers_hand}, final score: {dealer_total}
You Won
"""

def display_hands(players_hand, dealers_hand):
    print(f"""
Your cards: {players_hand}, current score: {sum(players_hand)}
Computer's first card: {dealers_hand[0]}
""")

def save_hands(memory, dealers_hand, players_hand = None,  dealer_only = False):
    if not memory:
        memory['player'] = players_hand
        memory["dealer"] = dealers_hand
    elif dealer_only:
        memory['dealer'].append(dealers_hand)
    else:
        memory['player'].append(players_hand)
        memory['dealer'].append(dealers_hand)

shuffle(cards)

while not stop:
    if len(cards) < 4:
        confirmation = input("The deck is low on cards. Type 'y' to get regenerate deck, type 'n' to end game: ")

        if confirmation not in ['no', 'n'] :
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            shuffle(cards)
        else:
            stop = True
            print(who_won(game_memory['player'], game_memory['dealer']))
            continue

    if game_memory:
        players_current_hand = cards.pop()
        dealers_current_hand = cards.pop()
    else:
        players_current_hand = [cards.pop(), cards.pop()]
        dealers_current_hand = [cards.pop(), cards.pop()]

    save_hands(game_memory, dealers_current_hand, players_current_hand)

    display_hands(game_memory['player'], game_memory['dealer'])

    confirmation = input("Type 'y' to get another card, type 'n' to pass: ")

    if confirmation in ['no', 'n']:
        while sum(game_memory['dealer']) < 17:
            dealers_current_hand = cards.pop()
            save_hands(game_memory, dealers_current_hand, dealer_only=True)
            
        print(who_won(game_memory['player'], game_memory['dealer']))
        stop = True
    else:
        continue