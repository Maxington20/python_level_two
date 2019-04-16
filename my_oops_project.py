from random import shuffle


SUITES = 'H C S D'.split()
FACES = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# initialize player ones points, player two's points, and the hand count
p1Points = 0
p2Points = 0
count = 1

deck = []

# for each suit in suites
for suit in SUITES:
    # for each face in faces
    for face in FACES:
        # add a new card to the deck (total of 52 cards)
        deck.append(face+ " " +suit)

# Shuffle up the order of the deck
shuffle(deck)

# first player's hand
handOne = [] 
for x in range(26):
    handOne.append(deck[x])

print()

# second player's hand
handTwo = []
for x in range(26,52):
    handTwo.append(deck[x])


# each player draw a card
def draw_card(hand):
    """
    Draw a card and turn it into a 2 item list, value in position 0, and
    suite in position 1
    """
    if hand.__len__() > 1:
        card = hand[-1]
        hand.pop()
    else:
        card = hand[0]

    card = card.split()
    return card


# verify if a face card was drawn
def check_face_card(card):
    """
    If the drawn card is a face card, assign it a numerical value
    """
    if card[0] == 'J':
         card[0] = 11

    elif card[0] == 'Q':
         card[0] = 12
    
    elif card[0] == 'K':
        card[0] = 13
    
    elif card[0] == 'A':
        card[0] = 14
    
    else:
        card[0] = int(card[0])
    return card

while count <= 26:
    p1Card = draw_card(handOne)
    p2Card = draw_card(handTwo)

    print(f"Hand #: {count}  -  Players one's card: {p1Card} - Player two's card: {p2Card}")

    p1Card = check_face_card(p1Card)
    p2Card = check_face_card(p2Card)

    if p1Card[0] > p2Card[0]:
        print("Player one wins this hand")
        p1Points += 1

    elif p2Card[0] > p1Card[0]:
        print("Player two wins this hand")
        p2Points += 1

    else:
        print("War!")
    
    count +=1


print()
if p1Points > p2Points:
    print(f"Player one wins with a score of {p1Points} to {p2Points}")

else:
    print(f"Player two wins with a score of {p2Points} to {p1Points}")