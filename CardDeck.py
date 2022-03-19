from random import randint

from Card import Card


class CardDeck:
    def __init__(self):
        factions = ["H", "S", "C", "D"]
        self.deck = []
        self.topCard = 0
        for x in range(4):
            for y in range(13):
                card = Card()
                card.faction = factions[x]
                card.value = y
                if card.faction == ("H" or "D"):
                    card.isRed = True
                self.deck.append(card)

    def mix(self):
        for x in range(300):
            rand1 = randint(0, 51)
            tempCard = self.deck[rand1]
            self.deck.pop(rand1)
            self.deck.append(tempCard)

    def getTopCard(self):
        card = self.deck[self.topCard]
        self.topCard = self.topCard + 1
        return card
