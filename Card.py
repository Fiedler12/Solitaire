class Card:
    def __init__(self, cardValue, faction, isShown):
        self.cardValue = cardValue
        self.faction = faction
        self.isShown = isShown


    def turn(self):
        if self.isShown == False:
            self.isShown = True
        else:
            self.isShown = False