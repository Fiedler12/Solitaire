class Card:
    def __init__(self):
        self.faction = None
        self.value = None
        self.isShown = False
        self.isRed = False

    def turn(self):
        if isShown == False:
            self.isShown = True
        else:
            self.isShown = False

    def getFaction(self):
        return self.faction

    def getValue(self):
        return self.value

    def turn(self):
        if (self.isShown == True):
            self.isShown = False
        else:
            self.isShown = True