class Card:
    def __init__(self):
        self.faction = None
        self.value = None
        self.isShown = False
        self.prevCard = None
        self.nextCard = None

    def turn(self):
        if isShown == False:
            self.isShown = True
        else:
            self.isShown = False