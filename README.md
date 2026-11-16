# Basic blackjack simulating python scripts

This repository contains basic scripts to simulate the card game blackjack. It is all code for the ECE 2260 project done by Samuel D'Antonio and Gilbert Argueta.

# What is Blackjack?
Blackjack is a card game that is very popular in casinos and online betting. The end goal is to have a higher amount of points than an opponent’s hand. At the start of the round, you will receive 2 cards from the dealer, and you will add the point value of each together. After you calculate your score, you have 2 options: you can ‘hit’ which means the dealer gives you another card, and if you for some reason you point value goes over 21 that is called a ‘bust’ or you have the option to ‘stand ’, which means that you will keep the cards you have, and go against the dealer. You will always be able to see the dealer's first card, so you can also make your decision based on that. There are more actions you can take like doubling down and splitting but for this project we will keep the actions limited to hitting and standing.
As for rules for this project we will be using only 1 card deck, which means 4 of each card type, the cards are as follows, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K & A. The card values of number 2-10 are their respective number Ex: a 3 has a point value of 3. J (Jack), Q (Queen), and K (King) have a value of 10, and A (Ace) has a value of either 11 or 1.

# Simulation Rules & Parameters
For our Monte Carlo Simulations we have built a Soft/Hard state when receiving cards. A hard state is when the hand doesn’t have an Ace or it has an Ace and it must be counted as 1 to prevent the hand from being over 21. A soft hand is an ace that is counted as an 11.

For our game the dealer is instructed that they must hit on anything lower than 17. Anything higher or equal to 17 they must stand on, this includes both soft and hard 17. For the program we check if anyone has an initial hand score of 21, before any other action is done. 

As for expected net units please refer to [Expected Net Return and Monte Carlo Explanations]https://docs.google.com/document/d/103JBr-ownDSd63dBVNNg6Gm51m3ouOhEO3hXnW1Rpm4/edit?tab=t.0#heading=h.o7010k5jmm7p.
 
