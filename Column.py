class Column():
    def __init__(self):
        self.cards = []


    def getCard(self, i):
        return self.cards[i]

    def getCards(self):
        return self.cards

    def getLastCard(self):
        return self.cards[-1]
