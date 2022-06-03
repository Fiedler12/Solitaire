from Column import Column
from DonePile import DonePile


class Table():
    def __init__(self):
        self.columns = []
        self.donePiles = []
        for x in range(7):
            column = Column()
            self.columns.append(column)
        factions = ["H", "D", "S", "C"]
        for x in range(4):
            newPile = DonePile(factions[x])
            self.donePiles.append(newPile)