import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data =np.zeros((18,10))
x_labels=[2,3,4,5,6,7,8,9,10,11]
y_labels=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(len(y_labels)):
    for j in range(len(x_labels)):
        if y_labels[i]<=13:
            data[i][j]=1
        elif x_labels[j]>6 and y_labels[i]>=17:
            data[i][j]=1
        else:
            data[i][j]=0
# Generate the heatmap
bj=sns.heatmap(
    data,
    annot=True,        # Show numbers inside cells
    fmt=".2f",         # Format numbers to 2 decimal places
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
