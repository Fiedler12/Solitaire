import random
from random import randint

from Card import Card


class CardDeck:
    def __init__(self):
        self.deck = []


    def mix(self):
        random.seed(49)
        for x in range(300):
            rand1 = randint(0, 51)
            tempCard = self.deck[rand1]
            self.deck.pop(rand1)
            self.deck.append(tempCard)

    def getTopCard(self):
        card = self.deck.pop(0)
        return card

    def getNormalDeck(self):
        factions = ['H', 'S', 'C', 'D']
        for x in range(4):
            for y in range(13):
                card = Card(y, factions[x])
                self.deck.append(card)

    def dealTestDeck(self):
        self.appendCard(10, "H")
        self.appendCard(0, "C")
        self.appendCard(11, "H")
        self.appendCard(7, "D")
        self.appendCard(5, "S")
        self.appendCard(5, "H")
        self.appendCard(2, "C")
        self.appendCard(6, "S")
        self.appendCard(7, "C")
        self.appendCard(1, "C")
        self.appendCard(6, "H")
        self.appendCard(1, "H")
        self.appendCard(6, "C")
        self.appendCard(3, "C")
        """
        self.appendCard(11, "C")
        self.appendCard(12, "H")
        self.appendCard(10, "S")
        self.appendCard(8, "C")
        self.appendCard(9, "S")
        self.appendCard(5, "D")
        self.appendCard(2, "D")
        self.appendCard(5, "C")
        self.appendCard(0, "S")
        self.appendCard(9, "C")
        self.appendCard(9, "D")
        self.appendCard(2, "S")
        self.appendCard(0, "D")
        self.appendCard(7, "H")
        self.appendCard(3, "H")
        self.appendCard(1, "D")
        self.appendCard(3, "D")
        self.appendCard(4, "C")
        self.appendCard(12, "C")
        self.appendCard(12, "S")
        self.appendCard(8, "S")
        self.appendCard(4, "D")
        self.appendCard(9, "H")
        self.appendCard(11, "S")
        self.appendCard(6, "D")
        self.appendCard(0, "H")
        self.appendCard(8, "D")
        self.appendCard(12, "D")
        self.appendCard(2, "H")
        self.appendCard(10, "C")
        self.appendCard(7, "S")
        self.appendCard(11, "D")
        self.appendCard(10, "D")
        self.appendCard(8, "H")
        self.appendCard(1, "S")
        self.appendCard(3, "S")
        self.appendCard(4, "H")
        self.appendCard(4, "S")
        """


    def appendCard(self, value, faction):
        newCard = Card(value, faction)
        self.deck.append(newCard)


    def printDeck(self):
        for card in self.deck:
            print(card.value + 1, card.faction)
