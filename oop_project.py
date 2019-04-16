"""
Card game war. deck divided evenly, with each player receiving
26 cards, dealt one at a time, face down. Anyone may deal firt
Each player palces his stack of cards face down, in from of him.

The Play:

Each player turns up a card at the same time and the player with
the higher cards takes both cards and puts them, face down,
on the bottom of his stack.

If the cards are the same rank, it is war. Each player turns up
three cards face down and one card face up. the player with
higher cards takes both piles (six cards). if the turned up cards are again
the same rank, each player places another card face down
and turns another card faace up. The player with the higher
card takes all 10 cards, and so on.


"""

from random import shuffle

# Two useful variables for creating cards
SUITE = 'H D S C'.split()

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the deck class. This object will create a deck of cards
    to initiate play. You can then use this deck list of cards to
    split in half and give to the players. It will use 
    SUITE and RANKS to create the deck. It should also have
    a method for splitting/cutting the deck in half and 
    shuffling the deck
    """

    def __init__(self, SUITE,RANKS):
        self.deck = []
        for num in range(14):
            for suite in range(5):
                self.deck.append(SUITE[suite],RANKS(num))
    
    def __str__(self):
        return(self.deck)


class Hand:
    """
    This is the hand class. Each player has a hand, and can
    add or remove cards from that hand. There should be an
    add and remove card method here.
    """


class Player:
    """
    This is the player class, which takes in a name and an 
    instance of a hand class object. the player can then play cards
    and check if they still have cards.
    """

# GAME PLAY
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war
deck = Deck(SUITE,RANKS)

print(deck)
