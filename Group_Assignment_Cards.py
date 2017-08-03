class Cards(object):
    def __init__(self, suit, number, value):
        self.suit = suit
        self.number = number
        self.value = value

    def valuefunction(self):
        valuefunction =[]
        numfunction = []
        self.suit = "Hearts"
        for i in range (1,13):
            numfunction.append(i)
            if i > 10:
                value=10
            valuefunction.append(value)

        print valfunction
        return hearts

class Deck(object):
    def __init__(self, cards):
        self.deck =[]
        suites=[hearts, diamonds, spades, clubs]
        values =[2,3,4,5,6,7,8,9,10,'Jack','king','queen','ace']
        for suit in suites:
            for value in values:
        def printDeck(self):

        return self

class Player(object):
    def __init__(self, name, cards):
        hand = []
        pass


# hearts = Cards(hearts, numfunction, valuefunction)
# clubs = Cards(clubs, numfunction, valuefunction)
# spades = Cards(spades, numfunction, valuefunction)
# diamonds= Cards(diamonds, numfunction, valuefunction)
