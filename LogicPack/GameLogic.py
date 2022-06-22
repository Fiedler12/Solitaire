from LogicPack.Suggestion import Suggestion
from Table import Table


class GameLogic:
    def __init__(self):
        self.table = None
        self.sugFound = False
        self.draw = None

    def getSuggestion(self, table, draw):
        self.table = table
        self.draw = draw
        suggestion = None

        if (not self.sugFound):
            suggestion = self.checkForEmptyColumn()

        if (not self.sugFound):
            suggestion = self.checkForKingColumnMove()

        if (not self.sugFound):
            suggestion = self.checkForColumnMoves()

        if (not self.sugFound):
            suggestion = self.checkDraw()

        if (not self.sugFound):
            suggestion = self.checkForFoundation()

        if (not self.sugFound):
            print("No move found. Pull card.")
            suggestion = Suggestion(4, None, None)

        self.sugFound = False
        self.draw = None
        self.table = None
        return suggestion

    def getEndSuggestion(self, table):
        self.table = table
        suggestion = None

        if (not self.sugFound):
            suggestion = self.checkForEmptyColumn()

        if (not self.sugFound):
            suggestion = self.checkForKingColumnMove()

        if (not self.sugFound):
            suggestion = self.checkForColumnMoves()

        if (not self.sugFound):
            suggestion = self.checkForFoundation()

        if (not self.sugFound):
            print("No move found. Pull card. Does not solve")

        self.sugFound = False
        self.table = None
        return suggestion


    def checkForKingColumnMove(self):
        for column in self.table.columns:
            if len(column.cards) != 0:
                if column.cards[0].value == 13 and column.cards[0].isShown:
                    cardDest = column.cards[-1]
                    for checkColumn in self.table.columns:
                        if len(checkColumn.cards) != 0:
                            if self.sugFound:
                                break
                            if checkColumn != column:
                                checkCard = checkColumn.getFirstShown()
                                if (checkCard.value + 1 == cardDest.value) and (checkCard.isRed != cardDest.isRed):
                                    print("Move found")
                                    print("Move: ", checkCard.value, checkCard.faction, "to: ", cardDest.value,
                                          cardDest.faction)
                                    return Suggestion(1, checkCard, column)
        return None

    def checkForFoundation(self):
        if not self.sugFound:
            for column in self.table.columns:
                if len(column.cards) != 0:
                    card = column.cards[-1]
                    for donePile in self.table.donePiles:
                        if donePile.faction == card.faction:
                            if len(donePile.cards) + 1 == card.value:
                                self.sugFound = True
                                return Suggestion(2, card, donePile)


    def checkForColumnMoves(self):
        for column in reversed(self.table.columns):
            if len(column.cards) != 0:
                if (self.sugFound):
                    break
                for card in column.cards:
                    if card.isShown:
                        for checkColumn in self.table.columns:
                            if self.sugFound:
                                break
                            if (checkColumn != column) and (len(checkColumn.cards) != 0):
                                sugCard = checkColumn.getLastCard()
                                if sugCard.value == card.value + 1 and card.isRed != sugCard.isRed:
                                    print("Move found")
                                    self.sugFound = True
                                    print("move: ", card.value, card.faction, "to ", sugCard.value, sugCard.faction)
                                    return Suggestion(1, card, checkColumn)
                        break
        return None

    def checkDraw(self):
        if self.draw.value is not None:
            if self.draw.value == 13:
                for column in self.table.columns:
                    if len(column.cards) == 0:
                        self.sugFound = True
                        print("Move found")
                        print("move: ", self.draw.value, self.draw.faction, "to empty column.")
                        return Suggestion(3, self.draw, column)
            for column in self.table.columns:
                if self.draw.value != 3:
                    if len(column.cards) != 0:
                        checkCard = column.cards[-1]
                        if (self.draw.value + 1 == checkCard.value) and (self.draw.isRed != checkCard.isRed):
                            self.sugFound = True
                            print("Move found")
                            print("move: ", self.draw.value, self.draw.faction, "to: ", checkCard.value,
                                  checkCard.faction)
                            return Suggestion(3, self.draw, column)
            for donePile in self.table.donePiles:
                if donePile.faction == self.draw.faction:
                    if len(donePile.cards) + 1 == self.draw.value:
                        self.sugFound = True
                        print("Move found")
                        print("Move draw to done pile")
                        return Suggestion(5, self.draw, donePile)

            return None

    def checkForEmptyColumn(self):
        for column in self.table.columns:
            if len(column.cards) == 0:
                for otherColumn in self.table.columns:
                    if otherColumn != column:
                            if len(otherColumn.cards) > 0:
                                if otherColumn.cards[0].value != 13:
                                    card = otherColumn.getFirstShown()
                                    if (card.value == 13) and card.isShown:
                                        self.sugFound = True
                                        print("Move found")
                                        print("Move: ", card.value, card.faction, " to empty column.")
                                        return Suggestion(1, card, column)
        return None
