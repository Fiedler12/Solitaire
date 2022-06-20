class Card:
    def __init__(self, isshown, value, faction):
        self.isShown = isshown
        self.faction = faction
        self.value = value
        self.isRed = False
        self.getColor()

    def getFaction(self):
        return self.faction

    def getValue(self):
        return self.value

    def getColor(self):
        if self.faction == 'H' or self.faction == 'D':
            self.isRed = True
        else:
            self.isRed = False


