from Card import Card
from CardDeck import CardDeck
from Column import Column
from DonePile import DonePile
from LogicPack.GameLogic import GameLogic
from Table import Table

cardDeck = CardDeck()
table = Table()
cardDeck.mix()
donePiles = []
gameLogic = GameLogic()


def deal():
    for idx, val in enumerate(table.columns):
        for i in range(idx + 1):
            val.cards.append(cardDeck.getTopCard())
    for y in table.columns:
        lastIdx = len(y.cards) - 1
        y.cards[lastIdx].turn()
    factions = ["H", "D", "S", "C"]
    for x in range(4):
        newPile = DonePile(factions[x])
        donePiles.append(newPile)

def printTable():
    for idx, var in enumerate(table.columns):
        print("Column ", idx + 1)
        for x in var.cards:
            if (x.isShown == True):
                print("[", x.getValue(), x.getFaction(), "]", end=" ")
            else:
                print("[]", end=" ")
        print("\n")
    for x in donePiles:
        print("Donepile: ", x.getFaction())

deal()
printTable()
