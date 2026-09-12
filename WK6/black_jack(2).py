# NOTE ON THIS FILE:
# This is an UNFINISHED starter/skeleton version of the Blackjack exercise
# (the numbered "Hint" comments below are the original exercise's
# step-by-step instructions for what to write). Only comments have been
# added here to explain what each existing line/hint is for - no logic has
# been added, removed, or changed, so the functions below are exactly as
# incomplete as they were before (deal_card(), calculate_score() and
# play_game() have no real body yet, and compare() has no body at all).
# As a result this file still cannot be run/compiled successfully; that
# is a pre-existing condition of the unfinished template, not something
# introduced by these comments. A completed, working version of the same
# game (with the deck, scoring and comparison logic filled in) lives in
# this same folder as game.py.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


# random: intended to be used later to randomly pick a card from the deck.
import random
# Import the ASCII-art banner defined in art.py, to be printed when a
# game starts (see Hint 14 below).
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    # Body not yet written: this function is only a docstring right now,
    # so calling it currently returns None instead of an actual card.
    # It is meant to end up using random.choice() on a "cards" deck list
    # (see the completed version in game.py) to return one random card
    # value each time it's called.

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    # Body not yet written beyond the hints below: right now this function
    # is only a docstring, so calling it currently returns None instead of
    # a score.
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


# compare() is meant to implement the logic described in Hint 13 above
# (decide the winner from user_score vs computer_score), but the function
# body has not been written at all yet - not even a docstring - which is
# why this file cannot currently be compiled/run (a function definition
# needs at least one statement in its body). This is left exactly as it
# was found; no statement has been added here.
def compare(user_score, computer_score):



def play_game():

    # Body not yet written beyond the hints below: play_game() is meant to
    # run one full round of the game by following Hints 5 and 9-12 in order.
    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List.
    # If no, then the game has ended.
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.
# input() blocks until the user types a response and presses Enter; the
# loop keeps starting new rounds for as long as the answer is exactly "y".
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
