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

    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling the deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])
        


class Hand:
    """
    This is the hand class. Each player has a hand, and can
    add or remove cards from that hand. There should be an
    add and remove card method here.
    """
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Contains {self.cards}"

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    This is the player class, which takes in a name and an 
    instance of a hand class object. the player can then play cards
    and check if they still have cards.
    """

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print (f"{self.name} has placed: {drawn_card}")
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        REturn true is player still has cards left
        """

        return len(self.hand.cards) != 0

# GAME PLAY
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war
d = Deck()

d.shuffle()
half1,half2 = d.split_in_half()

comp = Player("computer",Hand(half1))

name = input("What is your name?")

user = Player(name,Hand(half2))

totalRounds = 0
warCount = 0

while user.still_has_cards() and comp.still_has_cards():
    totalRounds += 1
    print("Time for a new round")
    print("here are the current standings")
    print(f"{user.name} has the count: {str(len(user.hand.cards))}")
    print(f"{comp.name} has the count: {str(len(comp.hand.cards))}")
    print("Play a card")
    print("\n")
    
    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        warCount += 1
        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)

        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)

        else:
            comp.hand.add(table_cards)

print(f"Game over, number of rounds: {str(totalRounds)}")
print(f"A war happened {str(warCount)} times")
print("Does the computer still have cards? ")
print(str(comp.still_has_cards()))
print("Does the user still have cards? ")
print(str(user.still_has_cards()))

