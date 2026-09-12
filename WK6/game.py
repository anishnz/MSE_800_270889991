"""Console Blackjack game (player vs. computer).

Full, playable implementation of the Blackjack house rules described
below. The player is dealt two cards and can keep asking for more ("hit")
until they choose to stop ("stand"), bust (go over 21), or get dealt a
natural blackjack. The computer then draws automatically until its score
is 17 or higher. `compare()` works out and prints the winner.

"""

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

# os: used to clear the console screen between games.
import os
# random: used to pick a random card out of the deck each time one is dealt.
import random

# Import the pre-made ASCII-art banner from art.py so it can be printed
# each time a new game starts.
from art import logo

# The "deck": a plain list of card values. There are more 10s than any
# other value (10, Jack, Queen, King all count as 10), which is why 10
# appears four times. Because cards are drawn with random.choice() and
# never removed, the deck is effectively infinite/unlimited in size, and
# every draw has the same odds as described in the house rules above.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    # random.choice() picks one random element from the cards list without
    # removing it, so the same value can be drawn again later.
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    # A 2-card hand that totals 21 is a blackjack. We represent that with 0
    # so it can be checked with a simple falsy/zero comparison later on.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If drawing an Ace as 11 pushes the hand over 21, count it as 1 instead.
    # cards.remove(11) deletes the FIRST 11 found in the list, and
    # cards.append(1) adds a 1 in its place so the Ace is now counted low.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Normal case: the score is simply the sum of every card in the hand.
    return sum(cards)


def compare(user_score, computer_score):
    """Compare the user's score to the computer's score and return the result."""
    # Each branch below covers one possible outcome. Order matters: the
    # blackjack (0) and bust (>21) checks are handled before the plain
    # "highest score wins" comparison at the bottom.
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over 21. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over 21. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    # Show the ASCII-art banner at the start of every round.
    print(logo)
    # Each player's hand starts as an empty list of card values.
    user_cards = []
    computer_cards = []
    # Flag used to control the main "hit or stand" loop below.
    is_game_over = False

    # Deal the opening hand: 2 cards each, one at a time, alternating
    # between the user and the computer (matches real dealing order).
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Main loop: keeps asking the user whether to draw another card,
    # until the game ends (blackjack, bust, or the user chooses to stop).
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show the user's full hand/score, but only reveal the computer's
        # FIRST card (as in real Blackjack, the dealer's other card(s)
        # stay hidden until the round ends).
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        # The round ends immediately if either side has a blackjack (0)
        # or if the user has already gone over 21.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user whether they want another card ("hit") or to
            # stop drawing ("stand").
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn: it keeps drawing as long as its score is under 17
    # (and it doesn't already have a blackjack).
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Reveal both final hands and scores, then print the outcome.
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Top-level program loop: keeps offering new rounds until the user types
# anything other than "y". input() blocks and waits for the user to type
# a response and press Enter.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # Clear the console before each new round so the previous round's
    # output doesn't clutter the screen. 'cls' is the Windows clear
    # command, 'clear' is the Unix/macOS equivalent; os.name tells us
    # which platform we're running on ('nt' = Windows).
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()

# Runs once the user answers anything other than 'y' to end the program.
print("Thanks for playing!")
