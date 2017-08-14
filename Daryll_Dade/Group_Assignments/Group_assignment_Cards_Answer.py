# Create a deck of Cards and assign hands to players
# Daryll, Kyle, Kevin

class Deck(object):
    def __init__(self):
        self.deck = []
        suits =['Hearts','Clubs','Diamonds','Spades']
        values =[2,3,4,5,6,7,8,9,10,'Jack', 'Queen','King','Ace']
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))

class Card(object):
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

class Player(object):
    def __init__(self, name, hand):
        pass

a = Deck()
for card in a.deck:
    print "{} of {}".format(card.value, card.suit)
