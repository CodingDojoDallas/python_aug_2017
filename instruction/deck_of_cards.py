import random
# Card Class
    #represent ONE card
    #attributes:
        #suit
        #value

#Deck Class
    #hold 52 card objects
    #attributes:
        #deck (array)

#Player Class  
    #interact with the cards and/or the deck
    #attributes
        #name
        #hand (array)

class Card(object):
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

class Deck(object):
    def __init__(self):
        self.reset()
        self.shuffle()

    def reset(self):
        self.deck = []
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'King', 'Queen', 'Ace']
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))
        return self
    
    def shuffle(self):
        random.shuffle(self.deck)
        return self

    def deal(self, players, num):
        for i in range(num):
            for player in players:
                card = self.deck.pop()
                player.hand.append(card)
        return self


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []


a = Deck()
for card in a.deck:
    print "{} of {}".format(card.value, card.suit)

cody = Player('Cody')
bob = Player('Bob')
karen = Player('Kevin')
players = [cody, bob, karen]

a.deal(players, 2)

for player in players:
    print '*'*50
    print "{}'s hand contains:".format(player.name)
    for card in player.hand:
        print "{} of {}".format(card.value, card.suit)
print '*'*50
print "Deck now contains {} cards".format(len(a.deck))