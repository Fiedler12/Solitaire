from Card import Card
from CardDeck import CardDeck
from Column import Column
from DonePile import DonePile
from LogicPack.GameLogic import GameLogic
from Table import Table

cardDeck = CardDeck()
table = Table()
cardDeck.mix()


def deal():
    for idx, val in enumerate(table.columns):
        for i in range(idx + 1):
            val.cards.append(cardDeck.getTopCard())
    for y in table.columns:
        lastIdx = len(y.cards) - 1
        y.cards[lastIdx].turn()

def printTable():
    for idx, var in enumerate(table.columns):
        print("Column ", idx + 1)
        for x in var.cards:
            if (x.isShown == True):
                print("[", x.getValue(), x.getFaction(), "]", end=" ")
            else:
                print("[]", end=" ")
        print("\n")
    for x in table.donePiles:
        print("Donepile: ", x.getFaction())


gameLogic = GameLogic(table)
deal()
printTable()
gameLogic.getSuggestion()


