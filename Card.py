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

def revealCard(self, id):
    if id == 1:
        self.isShown = True
        self.faction = "D"
        self.value = 1
        self.getColor()
    elif id == 2:
        self.isShown = True
        self.faction = "H"
        self.value = 1
        self.getColor()
    elif id == 3:
        self.isShown = True
        self.faction = "C"
        self.value = 1
        self.getColor()
    elif id == 4:
        self.isShown = True
        self.faction = "S"
        self.value = 1
        self.getColor()
    elif id == 5:
        self.isShown = True
        self.faction = "D"
        self.value = 2
        self.getColor()
    elif id == 6:
        self.isShown = True
        self.faction = "H"
        self.value = 2
        self.getColor()
    elif id == 7:
        self.isShown = True
        self.faction = "C"
        self.value = 2
        self.getColor()
    elif id == 8:
        self.isShown = True
        self.faction = "S"
        self.value = 2
        self.getColor()
    elif id == 9:
        self.isShown = True
        self.faction = "D"
        self.value = 3
        self.getColor()
    elif id == 10:
        self.isShown = True
        self.faction = "H"
        self.value = 3
        self.getColor()
    elif id == 11:
        self.isShown = True
        self.faction = "C"
        self.value = 3
        self.getColor()
    elif id == 12:
        self.isShown = True
        self.faction = "S"
        self.value = 3
        self.getColor()
    elif id == 13:
        self.isShown = True
        self.faction = "D"
        self.value = 4
        self.getColor()
    elif id == 14:
        self.isShown = True
        self.faction = "H"
        self.value = 4
        self.getColor()
    elif id == 15:
        self.isShown = True
        self.faction = "C"
        self.value = 4
        self.getColor()
    elif id == 16:
        self.isShown = True
        self.faction = "S"
        self.value = 4
        self.getColor()
    elif id == 17:
        self.isShown = True
        self.faction = "D"
        self.value = 5
        self.getColor()
    elif id == 18:
        self.isShown = True
        self.faction = "H"
        self.value = 5
        self.getColor()
    elif id == 19:
        self.isShown = True
        self.faction = "C"
        self.value = 5
        self.getColor()
    elif id == 20:
        self.isShown = True
        self.faction = "S"
        self.value = 5
        self.getColor()
    elif id == 21:
        self.isShown = True
        self.faction = "D"
        self.value = 6
        self.getColor()
    elif id == 22:
        self.isShown = True
        self.faction = "H"
        self.value = 6
        self.getColor()
    elif id == 23:
        self.isShown = True
        self.faction = "C"
        self.value = 6
        self.getColor()
    elif id == 24:
        self.isShown = True
        self.faction = "S"
        self.value = 6
        self.getColor()
    elif id == 25:
        self.isShown = True
        self.faction = "D"
        self.value = 7
        self.getColor()
    elif id == 26:
        self.isShown = True
        self.faction = "H"
        self.value = 7
        self.getColor()
    elif id == 27:
        self.isShown = True
        self.faction = "C"
        self.value = 7
        self.getColor()
    elif id == 28:
        self.isShown = True
        self.faction = "S"
        self.value = 7
        self.getColor()
    elif id == 29:
        self.isShown = True
        self.faction = "D"
        self.value = 8
        self.getColor()
    elif id == 30:
        self.isShown = True
        self.faction = "H"
        self.value = 8
        self.getColor()
    elif id == 31:
        self.isShown = True
        self.faction = "C"
        self.value = 8
        self.getColor()
    elif id == 32:
        self.isShown = True
        self.faction = "S"
        self.value = 8
        self.getColor()
    elif id == 33:
        self.isShown = True
        self.faction = "D"
        self.value = 9
        self.getColor()
    elif id == 34:
        self.isShown = True
        self.faction = "H"
        self.value = 9
        self.getColor()
    elif id == 35:
        self.isShown = True
        self.faction = "C"
        self.value = 9
        self.getColor()
    elif id == 36:
        self.isShown = True
        self.faction = "S"
        self.value = 9
        self.getColor()
    elif id == 37:
        self.isShown = True
        self.faction = "D"
        self.value = 10
        self.getColor()
    elif id == 38:
        self.isShown = True
        self.faction = "H"
        self.value = 10
        self.getColor()
    elif id == 39:
        self.isShown = True
        self.faction = "C"
        self.value = 10
        self.getColor()
    elif id == 40:
        self.isShown = True
        self.faction = "S"
        self.value = 10
        self.getColor()
    elif id == 41:
        self.isShown = True
        self.faction = "D"
        self.value = 11
        self.getColor()
    elif id == 42:
        self.isShown = True
        self.faction = "H"
        self.value = 11
        self.getColor()
    elif id == 43:
        self.isShown = True
        self.faction = "C"
        self.value = 11
        self.getColor()
    elif id == 44:
        self.isShown = True
        self.faction = "S"
        self.value = 11
        self.getColor()
    elif id == 45:
        self.isShown = True
        self.faction = "D"
        self.value = 12
        self.getColor()
    elif id == 46:
        self.isShown = True
        self.faction = "H"
        self.value = 12
        self.getColor()
    elif id == 47:
        self.isShown = True
        self.faction = "C"
        self.value = 12
        self.getColor()
    elif id == 48:
        self.isShown = True
        self.faction = "S"
        self.value = 12
        self.getColor()
    elif id == 49:
        self.isShown = True
        self.faction = "D"
        self.value = 13
        self.getColor()
    elif id == 50:
        self.isShown = True
        self.faction = "H"
        self.value = 13
        self.getColor()
    elif id == 51:
        self.isShown = True
        self.faction = "C"
        self.value = 13
        self.getColor()
    elif id == 52:
        self.isShown = True
        self.faction = "S"
        self.value = 13
        self.getColor()
