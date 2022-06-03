class DonePile():
    def __init__(self, faction):
        self.cards = []
        self.faction = faction
    def getFaction(self):
        return self.faction