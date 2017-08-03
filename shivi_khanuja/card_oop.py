class Card(object):
    def __init__(self, face, num):
        # face_card = (' ', 'diamond', 'heart', 'ace', 'space')
        # num_card = ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J')
        self.face_card = face
        self.num_card = num



class Deck(object):
    def __init__(self):
        self.reset()

    def reset(self):
        face_card = ('diamond', 'heart', 'ace', 'spades')
        num_card = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J')
        self.deck = []
        for face in face_card:
            for num in num_card:
                print "putting {} of {} into deck".format(num, face)
                self.deck.append(Card(num, face))

deck = Deck()
print len(deck.deck)
deck.reset()

#  print "Deck contains {} of {}".format(deck.deck[0].num_card, deck.deck[0].face_card)
          



