import math
import random

#settings decleration
N_TRIALS=100000
STAND_ON=17
SEED=42 #

# Each suit has one Ace and four 10-valued cards: 10, Jack, Queen, King.
CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#Create and shuffle a new deck. pop() will draw without replacement.
def make_deck(rng):
    deck=CARD_VALUES*4
    rng.shuffle(deck)
    return deck

#optimize hand if an ace is present
def hand_value(hand):
    tital=sum(hand)
    aces=hand.count(11)

    while total>21 and aces>0:
        total -=10
        aces-=1
    return total

#baseline logic. true means hit, false means stand. 
#    This first policy ignores dealer_upcard, but it is available for a future strategy. The policy only receives information the player sees.
def player_should_hit(hand, dealer_upcard, stand_on):
    return hand_value(hand)<stand_on

#play one hand and return net profint per 1-unit initial stake
def play_hand(deck,stand_on=17):
    player=[deck.pop()]
    dealer=[deck.pop()]
    player.append(deck.pop())
    dealer.append(deck.pop())

    player_blackjack=hand_value(player)==21
    dealer_blackjack=hand_value(dealer)==21

    if player_blackjack and dealer_blackjack:
        return 0.0
    if dealer_blackjack:
        return -1.0;
    if player_blackjack:
        return 1.5

    while player_should_hit(player,dealer[0],stand_on):
        player.append(deck.pop())
        if hand_value(player)>21:
            return -1.0

    while hand_value(dealer)<17:
        dealer.append(deck.pop())

    player_total=hand_value(player)
    dealer_total=hand_value(dealer)

    if dealer_total > 21 or player_total > dealer_total:
        return 1.0
    if player_total < dealer_total:
        return -1.0
    return 0.0


