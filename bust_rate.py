import random
import csv

# settings declaration
N_TRIALS = 100000
SEED = 42

# Each suit has one Ace and four 10-valued cards: 10, Jack, Queen, King.
CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# Create and shuffle a new deck. pop() will draw without replacement.
def make_deck(rng):
    deck = CARD_VALUES * 4
    rng.shuffle(deck)
    return deck

# optimize hand if an ace is present
def hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def calculate_dealer_bust_rates(n_trials=N_TRIALS, seed=SEED):
    # Initialize just once, outside the loop.
    rng = random.Random(seed)
    results = []
    
    # This tests every possible dealer upcard (2 through 11)
    for upcard in range(2, 12):
        busts = 0

        #Removes visible upcard from the deck and dealer draws their second 
        for _ in range(n_trials):
            deck = make_deck(rng)
            deck.remove(upcard) 
            dealer = [upcard, deck.pop()] 
            
            # dealer's turn (hits below 17)
            while hand_value(dealer) < 17:
                dealer.append(deck.pop())
                
            # Check if dealer busted
            if hand_value(dealer) > 21:
                busts += 1
                
        # Calculate empirical probability
        bust_rate_percent = (busts / n_trials) * 100
        
        # Save as a row for the CSV
        results.append({
            "Dealer_Upcard": upcard,
            "Bust_Rate_Percent": round(bust_rate_percent, 2)
        })
        
    return results #will return a list of dictionaries with bust rates for each upcard

#Printing the results to console and saving to CSV
if __name__ == "__main__":
    print("Simulating dealer bust probabilities based on upcard...")
    bust_rates_data = calculate_dealer_bust_rates()
        
    # Export to CSV 
    with open("dealer_bust_rates.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Dealer_Upcard", "Bust_Rate_Percent"])
        writer.writeheader()
        writer.writerows(bust_rates_data)
        
    print("\nSaved results to dealer_bust_rates.csv")