import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from blackJack import player_should_hit
STAND_ON = 12 

#Labels
x_labels=[2,3,4,5,6,7,8,9,10,11]
y_labels=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

data = np.zeros((len(y_labels), len(x_labels)))

# Outer loop: each row is a player hand total (4 through 20).
for i, total in enumerate(y_labels):
    # Inner loop: each column is a dealer upcard (2 through 11, where 11 = Ace).
    for j, upcard in enumerate(x_labels):
        # Ask the real strategy function what to do for this situation.
        data[i][j] = 1 if player_should_hit([total], upcard, STAND_ON) else 0


# Generate the heatmap
bj=sns.heatmap(
    data,
    annot=True,        # Show numbers inside cells
    fmt=".0f",         # Format numbers to no decimal places, since only using 0 and 1
    cmap='RdBu',   # Color palette (e.g., 'viridis', 'YlGnBu', 'RdBu')
     
    linewidths=0.5,     # Add thin lines between cells
    xticklabels=x_labels,  # Individual column labels
    yticklabels=y_labels 
)

plt.suptitle("BlackJack Strategy Heatmap")
bj.set_title("1=hit,0=stand")
bj.set_xlabel("Dealer Upcard")
bj.set_ylabel("Total Player Hand Value")
plt.savefig("strategyHeatmap.png")
plt.show()
