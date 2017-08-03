import random
class card(object):
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    
        
# a = card('ace', 'spade') 
# print "we have the {} of {}".format(a.value, a.suit)       

class Deck(object):
    def __init__(self):
        self.reset()
        self.shuffle()
        
    def reset(self):    
        self.deck = []
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        values = [2,3,4,5,6,7,8,9,10, 'jack', 'king', 'queen', 'ace']
        for suit in suits:
            for value in values:
                self.deck.append(card(value, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, players, num):
        for i in range(num): 
            for player in players:
                card = self.deck.pop()
                player.hand.append(card)

                    



class player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []




a = Deck()
a.shuffle()
print 'after shuffle'
# print a.deck                
for card in a.deck:
    print '{} of {}'.format(card.value, card.suit)


ody = player('ody')
amayah = player('amayah')
kwene = player('kwene')   
players = [ody, amayah, kwene]

a.deal(players, 2)

for player in players:
    print '*'*50
    print "{}'s hand contains:".format(player.name)
    for card in player.hand:
        print "{} of {}".format(card.value, card.suit)

print "deck contains {} cards".format(len(a.deck))       

# a.reset
# print 'after reset:'
# for card in a.deck:
#     print '{} of {}'.format(card.value, card.suit)