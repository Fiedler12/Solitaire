class Card:
    def __init__(self, value, faction):
        self.faction = faction
        self.value = value
        self.isShown = False
        self.isRed = False
        self.getColor()



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

    def getColor(self):
        if self.faction == 'H' or self.faction == 'D':
            self.isRed = True
