from Table import Table

class GameLogic:
    def __init__(self, table):
        self.table = table
        self.sugFound = False

    def getSuggestion(self):
        self.checkForFoundation()
        if (not self.sugFound):
            self.checkForColumnMoves()

        if (not self.sugFound):
            print("No move found")





    def checkForFoundation(self):
        for column in self.table.columns:
            if (self.sugFound):
                break
            card = column.getLastCard()
            faction = card.faction
            for donePile in self.table.donePiles:
                if donePile.faction == faction:
                    if donePile.cards:
                        print("not implemented")
                    else:
                        if card.value == 0:
                            print("move: ", card.value, card.faction, "to donePile")
                            self.sugFound = True
                            break

    def checkForColumnMoves(self):
        print("Checking for inter-column moves")
        for column in self.table.columns:
            if (self.sugFound):
                break
            for card in column.cards:
                if card.isShown:
                    print("Checking ", card.value, card.faction, " for moves.")
                    for checkColumn in self.table.columns:
                        if checkColumn != column:
                            print("Excluding current column")
                            sugCard = checkColumn.getLastCard()
                            if card.value + 1 == sugCard.value and card.isRed != sugCard.isRed:
                                print("Move found")
                                self.sugFound = True
                                print("move: ", card.value, card.faction, "to ", sugCard.value, sugCard.faction)
                                break


