import random
random.shuffle
#card represent all individual cards
class Card(object):
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

#holds all 52 cards
class Deck(object):
	def __init__(self):
		self.deck = []
		suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
		values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack,' 'Queen', 'King', 'Ace' ]
		for suit in suits:
			for value in values:
				self.deck.append(Card(value, suit))

	def shuffle(self):
		random.shuffle(self.deck)

#contains player hand
class Player(object):
	def __init__(self,name):
		self.name = name
		self.hand =
