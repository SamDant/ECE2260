#impprt needed libraries
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import array


#global settings decleration 
N_TRIALS=100000
STAND_ON=17
SEED=42 #Ensures repeatable hands so that different stand_on values can be compared accuratly. Using the same seed allowseach strategy to be tested against the same sequence of shuffled decks.

#Declaring base values for one suit. Each suit has one Ace and four 10-valued cards: 10, Jack, Queen, King.
CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#Create and shuffle a new deck. pop() draws without replacement. Assumed this as the odds to redraw a card are near zero.
def make_deck(rng):
    deck=CARD_VALUES*4
    rng.shuffle(deck)
    return deck

#optimize hand if an ace is present
def hand_value(hand):
    total=sum(hand)
    aces=hand.count(11)

    while total>21 and aces>0:
        total -=10
        aces-=1
    return total

#Baseline strategy. True means hit, false means stand.

#def player_should_hit(hand, dealer_upcard, stand_on):
#   return hand_value(hand)<stand_on

#This first strategy ignores the  dealer_upcard, but this variable is available for a future strategy. The strategy only receives information the player sees.

#New strategy. includes dealer_upcard logic
#Based on the dealers upcard, what should the player do?

#Looks at dealers upcard and determines, based on probability, the percent chance of dealer busting with the upcard.
#Based on that probability, the strategy decides to hit or stand depending on your card value and dealer_upcard
def player_should_hit(hand, dealer_upcard, stand_on):
    total = hand_value(hand)
    #If bust, dont hit
    if total > 21:
        return False
    #If not at stand_on value, hit
    if total < stand_on:
        return True
    #If not at stand_on value, but total is >=17 and dealer upcard is at least a 7, hit
    return dealer_upcard > 6 and total<17

#Play one hand and return net profint per 1-unit initial stake
def play_hand(deck,stand_on=17):
    #Deal hand
    player=[deck.pop()]
    dealer=[deck.pop()]
    player.append(deck.pop())
    dealer.append(deck.pop())
    #Define blackjack
    player_blackjack=hand_value(player)==21
    dealer_blackjack=hand_value(dealer)==21
    #Check blackjack
    if player_blackjack and dealer_blackjack:
        return 0.0
    if dealer_blackjack:
        return -1.0;
    if player_blackjack:
        return 1.0

    #Player turn
    while player_should_hit(player, dealer[0], stand_on):
        extra_hit = (dealer[0] > 6 and hand_value(player) >= stand_on)
        player.append(deck.pop())
        if hand_value(player) > 21:
            return -1.0


    #Dealer turn
    while hand_value(dealer)<17:
        dealer.append(deck.pop())

    player_total=hand_value(player)
    dealer_total=hand_value(dealer)

    if dealer_total > 21 or player_total > dealer_total:
        return 1.0
    if player_total < dealer_total:
        return -1.0
    return 0.0

#Run a full simulation (eg play # of hands with a given strategy and calculate results)
def simulate(n_trials=N_TRIALS, stand_on=STAND_ON, seed=SEED):
    """Run independent hands and summarize results for this policy."""
    if not isinstance(n_trials, int) or n_trials < 2:
        raise ValueError("n_trials must be an integer of at least 2.")
    if not isinstance(stand_on, int) or not 2 <= stand_on <= 21:
        raise ValueError("stand_on must be an integer from 2 through 21.")

    # Initialize ONCE, outside the loop. Re-seeding each hand repeats it.
    rng = random.Random(seed)
    wins = losses = pushes = 0
    total_profit = 0.0
    total_profit_squared = 0.0

    for _ in range(n_trials):
        deck = make_deck(rng)
        profit = play_hand(deck, stand_on)

        if profit > 0:
            wins += 1
        elif profit < 0:
            losses += 1
        else:
            pushes += 1

        total_profit += profit
        total_profit_squared += profit ** 2

    mean_profit = total_profit / n_trials
    sample_variance = max(
        0.0,
        (total_profit_squared - n_trials * mean_profit ** 2) / (n_trials - 1),
    )
    standard_error = math.sqrt(sample_variance / n_trials)

    return {
        "hands": n_trials,
        "wins": wins,
        "losses": losses,
        "pushes": pushes,
        "win_rate": wins / n_trials,
        "loss_rate": losses / n_trials,
        "push_rate": pushes / n_trials,
        "mean_profit": mean_profit,
        "standard_error": standard_error,
        "ci95_low": mean_profit - 1.96 * standard_error,
        "ci95_high": mean_profit + 1.96 * standard_error,
        "stand_on": stand_on,
        "seed": seed,
    }

def main():
    #UI and simulation call
    print("Simplified blackjack Monte Carlo simulation")
    seed = int(input("Enter the random seed: "))
    print("Fresh single deck per hand; dealer stands on all 17s; 1:1 blackjack.")
    print("Fixed 1-unit stake; hit/stand only; no split/double/surrender/insurance.")
    showVals=int(input("Would you like to display each run in terminal? Y=1/n=0: "))
    stats=[]    
    sOn=3
    i=0
    if seed ==0:
                 seed=SEED
    while sOn<21:
        stats.append(simulate(N_TRIALS,sOn,seed))
        if showVals==1:
            print()
            print("-----NEXT SIM-----")
            print(f"Player policy: hit below {sOn}; stand at {sOn} or higher.")
            print(f"Hands: {stats[i]['hands']:,} | Seed: {stats[i]['seed']}")
            print(f"Win rate:  {stats[i]['win_rate']:.2%} ({stats[i]['wins']:,} hands)")
            print(f"Loss rate: {stats[i]['loss_rate']:.2%} ({stats[i]['losses']:,} hands)")
            print(f"Push rate: {stats[i]['push_rate']:.2%} ({stats[i]['pushes']:,} hands)")
            print(f"Average net profit: {stats[i]['mean_profit']:+.5f} units per hand")
            print(f"Average net return per initial stake: {stats[i]['mean_profit']:+.2%}")
            print(
                "Approx. 95% confidence interval for mean profit: "
                f"[{stats[i]['ci95_low']:+.5f}, {stats[i]['ci95_high']:+.5f}] units per hand"
            )
            print()
        sOn += 1
        i += 1

    print("The interval measures sampling uncertainty under this model.")
    pd.DataFrame(stats).to_csv("blackjack_results.csv", index=False)
    print("Saved results to blackjack_results.csv")

if __name__ == "__main__":
    main()
