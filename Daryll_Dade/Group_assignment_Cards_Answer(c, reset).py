import random
# Create a deck of Cards and assign hands to players

class Deck(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self.deck = []
        suits =['Hearts','Clubs','Diamonds','Spades']
        values =[2,3,4,5,6,7,8,9,10,'Jack', 'Queen','King','Ace']
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))
    def shuffle(self):
        random.shuffle(self.deck)

    def calculateValue(self, card):
        if card.value == 'King' or 'Queen' or 'Jack':
            value = 10

    def deal(self, players, num):
        for i in range(num):
            for player in players:
                player.hand.append(self.deck.pop())


class Card(object):
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

a = Deck()
a.shuffle()
print 'After Shuffle:'
for card in a.deck:
    print "{} of {}".format(card.value, card.suit)
a.reset()
print 'After Reset'
for card in a.deck:
    print "{} of {}".format(card.value, card.suit)


# player1= Player('Player1')
# player2= Player('Player2')
# player3= Player('Player3')
# players = [player1, player2, player3]

# a.deal(players, 2)
# for player in players:
#     print '*' *50
#     print "{}'s hand contains:".format(player.name)
#     for card in player.hand:
#         print "{} of {}".format(card.value, card.suit)
