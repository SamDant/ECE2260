import pandas as pd
import matplotlib.pyplot as plot

#plot for blackjack_results.csv

df=pd.read_csv("blackjack_results.csv")

plot.figure(figsize=(10,8))
plot.bar(df["stand_on"],df["win_rate"],color="steelblue")

seed=df["seed"]

plot.title("Player Win Rate by Hand Value to Stand with given seed: "+str(seed[0]))
plot.xlabel("Stand On")
plot.ylabel("Win Rate (*100=%)")
plot.tight_layout()


plot.savefig("blackJack_winRatexStandOn.png")
plot.show()

#plot 2 for blackjack_results.csv

plot.figure(figsize=(10,8))
plot.bar(df["stand_on"],df["mean_profit"],color="steelblue")

seed=df["seed"]

plot.title("Player Mean Profit by Hand Value to Stand with given seed: "+str(seed[0]))
plot.xlabel("Stand On")
plot.ylabel("Mean Profit (Given 1 unit initial stake)")
plot.tight_layout()


plot.savefig("blackJack_winRatexMeanProfit.png")
plot.show()

#plot for dealer_bust_rates.csv

df2=pd.read_csv("dealer_bust_rates.csv")

plot.figure(figsize=(10,8))
plot.bar(df2["Dealer_Upcard"],df2["Bust_Rate_Percent"],color="red")

plot.title("Dealer Bust Rate by Dealer Upcard with seed: 42")
plot.xlabel("Dealer Upcard")
plot.ylabel("Dealer Bust Rate (%)")
plot.tight_layout()

plot.savefig("dealerBustRatexDealerUpCard.png")
plot.show()
