# Basic blackjack simulating python scripts

This repository contains basic scripts to simulate the card game blackjack. It is all code for the ECE 2260 project done by Samuel D'Antonio and Gilbert Argueta.

## What is Blackjack?
Blackjack is a card game that is very popular in casinos and online betting. The end goal is to have a higher amount of points than an opponent’s hand. At the start of the round, you will receive 2 cards from the dealer, and you will add the point value of each together. After you calculate your score, you have 2 options: you can ‘hit’ which means the dealer gives you another card, and if you for some reason you point value goes over 21 that is called a ‘bust’ or you have the option to ‘stand ’, which means that you will keep the cards you have, and go against the dealer. You will always be able to see the dealer's first card, so you can also make your decision based on that. There are more actions you can take like doubling down and splitting but for this project we will keep the actions limited to hitting and standing.
As for rules for this project we will be using only 1 card deck, which means 4 of each card type, the cards are as follows, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K & A. The card values of number 2-10 are their respective number Ex: a 3 has a point value of 3. J (Jack), Q (Queen), and K (King) have a value of 10, and A (Ace) has a value of either 11 or 1.

## Simulation Rules & Parameters
For our Monte Carlo Simulations we have built a Soft/Hard state when receiving cards. A hard state is when the hand doesn’t have an Ace or it has an Ace and it must be counted as 1 to prevent the hand from being over 21. A soft hand is an ace that is counted as an 11.

For our game the dealer is instructed that they must hit on anything lower than 17. Anything higher or equal to 17 they must stand on, this includes both soft and hard 17. For the program we check if anyone has an initial hand score of 21, before any other action is done. 

As for expected net units please refer to [Expected Net Return and Monte Carlo Explanations](https://docs.google.com/document/d/103JBr-ownDSd63dBVNNg6Gm51m3ouOhEO3hXnW1Rpm4/edit?tab=t.0#heading=h.o7010k5jmm7p).

## *How the Monte Carlo Simulation will work*

The simulation will test players standing from numbers 3-20 (this is considered the threshold), under each strategy the logic is as follow:
The players will always hit if the hand total is less than the threshold
Once the threshold is reach, the player will stand if the dealers upcard is 2 through 6
If the dealer’s upcard is 7 through Ace, and the player’s hand total is greater than or equal to 17, the player will take one additional card, and then stop.
## *Reason for Player Standing or Hitting*
We first came up with these rules after reading the article: “Unlock Winning Strategies: Learn to Leverage the Dealer’s Upcard in Blackjack”[1], and it recommended if the dealer’s upcard was 2-6 to stand, and higher than 6 to hit. So we decided to run a simulation with 100,000 trial per upcard to see the expected probabilities and the results were as follow:

*Table 1*
| Dealer's Upcard | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Bist Rate % | 35.05 | 37.29 | 39.20 | 41.84 | 41.98 | 26.53 | 24.57 | 23.09 | 21.19 | 11.68 |
| Getting (17-21) | 64.95 | 62.71 | 60.80 | 58.16 | 58.02 | 73.47 | 75.43 | 76.91 | 78.81 | 88.32 |

As seen in Table 1 when a dealer shows a low card (2-6) they have a higher chance of busting, the reason the percentage is so high is because they need to draw multiple times to reach the 17 that they must stand on.

Since there are only 2 options in blackjack for the dealer bust, or reach their range of (17-21). We can determine the probability of reach threshold is:  100 - Bust Rate % , we have the bust rate for the simulation, the results for getting 17-21 are displayed in Table 1.

Following that logic we can see from the data in Table 1 that whenever a dealer shows a high card (7-Ace) they have a higher chance of getting a hand value that they can stand on (17-21). And we decided they should take the extra hit in this project.

## How to use this code

The monteCarlo.py file is a basic example of a Montecarlo simulation. 
The blackJack.py file is the simulation for the conditions outlined in this file and the project.
The bust rate.py file calculates the bust rate of the dealer based on their upcard.
The plotResults.py file takes the genrated CSV files and outputs two plots: one of the blackJack.py output and the other of the bust rate.py output 
The strategyHeat.py file is a hardcoded script that generates a heatmap of all hit stand situations


In order to display the results as plots, run: 
```
source venv/bin/activate
```
to set up the virtual enviornment.

Then run:

```
python blackJack.py
```

This program will ask you for a seed and if you would like to display the results live in the terminal. 
Respond to it, and it will output the results to a csv file.

Then run:
```
python bust_rate.py
```
The results from this scrip will be stored in a CSV file.

Once that is done, run:
```
python plotResults.py
```
The plots will apear on screen and be saved as .png files in the working directory.


If you want the strategy heatmap, run:
```
python strategyHeat.py
```
The heatmap will then show up on screen and be saved as a .png to the working directory.

## Expected Net Return and Monte Carlo Explanations
The expected net probabilities change every time whenever a new card is drawn so if we calculate every possibility it would take a long time and is inefficient. Thus for this project we will calculate expected values using the Monte Carlo Simulations.

For this project we will define random variable R as the net return from one one hand. And the possible outcomes are as follow:

*Table 3*

| Loss = -1           R = -1 | Push = 0       (R = 0) | Win = +1           R = +1 |
| :---: | :---: | :---: |


Thus the theoretical expected net return would be probability of winning a hand - probability of losing a hand which is represented as: E[R] = P(win) - P(loss)

## *Empirical Probability/ Law of Large Numbers in Monte Carlo Simulations* 
For the Monte Carlo simulation we are going to be relying on Empirical Probability which estimates the likelihood of an outcome based on a large number of trials. Thus the formula is the following:

$$
\text{P(win)} =\frac{\text{Numbers of Hands won}}{\text{Total number of hands played}}
$$

P(win) is represented as the estimated probability

To estimate the quality, the Monte Carlo program runs a simulation of 100,000 hands per each strategy, and we use multiple trials to estimate the underlying probability due to the Law of Large Numbers. Which states that as the number of independent trials increases, the win proportion converges to the true win probability, similar to the graph in extra credit question 8 in slide set 16.

##*Sample mean for net return*
With those results that we get from the Simulation it records the net return from each hand, which we will call $$R_i$$. Then using the $$R_i$$ for each hand we will calculate the sample mean to estimate the strategy's overall expected net return. Which is represented as the following formula:
$$
Average R = \frac{1}{n} \sum_{i=1}^{n}R_i
$$

Confidence Interval
For safety we also use a 95% confidence interval, we use a confidence interval to describe sampling uncertainty in the mean return. Because it measures how much the estimates can possibly vary because the simulation uses a certain number of random hands. We use the confidence interval for the mean return using Standard Deviation. Which is represented as the following formula:
$$
Confidence Interval= Net R \pm 1.96 \frac{s}{\sqrt{n}}
$$
s is the the standard deviation of the return

By comparing the estimated Net Return for all the different strategies/thresholds we are able to find which strategy gives the most viable return.

## References
[1] V. H. Royer, “Unlock winning strategies: Learn to leverage the dealer’s upcard in blackjack,” Casino.org, Sep. 30, 2024. Accessed: Nov. 13, 2026. [Online]. Available:[https://www.casino.org/blog/dealers-upcard-blackjack/](https://www.casino.org/blog/dealers-upcard-blackjack/) 
