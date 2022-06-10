from Card import Card
from CardDeck import CardDeck
from Column import Column
from DonePile import DonePile
from LogicPack.GameLogic import GameLogic
from Table import Table

cardDeck = CardDeck()
table = Table()
cardDeck.dealTestDeck()
draw = None


def deal():
    for column in table.columns:
        card = cardDeck.deck.pop(0)
        column.cards.append(card)

    for x in range(1,7):
        card = cardDeck.deck.pop(0)
        table.columns[x].cards.append(card)

    for x in range(2,7):
        card = cardDeck.deck.pop(0)
        table.columns[x].cards.append(card)

    for x in range(3,7):
        card = cardDeck.deck.pop(0)
        table.columns[x].cards.append(card)

    for x in range(4,7):
        card = cardDeck.deck.pop(0)
        table.columns[x].cards.append(card)

    for x in range(5,7):
        card = cardDeck.deck.pop(0)
        table.columns[x].cards.append(card)

    for x in range(6,7):
        card = cardDeck.deck.pop(0)
        table.columns[x].cards.append(card)

def printTable():
    for column in table.columns:
        if len(column.cards) != 0:
            card = column.getLastCard()
            if card.isShown == False:
                card.turn()
        for idx, var in enumerate(table.columns):
            print("Column ", idx + 1)
            for x in var.cards:
                if (x.isShown == True):
                    print("[", x.getValue(), x.getFaction(), "]", end=" ")
                else:
                    print("[]", end=" ")
            print("\n")
    for x in table.donePiles:
        if len(x.cards) == 0:
            print("Donepile: ", x.getFaction())
        else:
            print("Donepile: ", x.cards[-1].value, x.getFaction())

    print("Draw: ", draw.value, draw.faction)


def makeMove(suggestion):
    if suggestion.sugCode == 1:
        print("Intercolumn move")
        for column in table.columns:
            idx = 0
            for card in column.cards:
                if card == suggestion.fromCard:
                    moveColumn = column.cards[idx:]
                    for x in moveColumn:
                        suggestion.toColumn.cards.append(x)
                    del column.cards[idx:]
                    return
                else:
                    idx = idx + 1
    if suggestion.sugCode == 2:
        print("Donepile move")
        for column in table.columns:
            if len(column.cards) != 0:
                lastCard = column.getLastCard()
                if lastCard == suggestion.fromCard:
                    suggestion.toColumn.cards.append(suggestion.fromCard)
                    del column.cards[-1]
    if suggestion.sugCode == 3:
        print("draw move")
        card = cardDeck.pullTopCard()
        suggestion.toColumn.cards.append(card)
    if suggestion.sugCode == 4:
        print("Implement card pull")





gameLogic = GameLogic()
deal()
draw = cardDeck.getTopCard()

while True:
    printTable()
    suggestion = gameLogic.getSuggestion(table, draw)
    if suggestion != None:
        makeMove(suggestion)

    input("Press for next move")

