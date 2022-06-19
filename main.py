from Card import Card
from CardDeck import CardDeck
from Column import Column
from DonePile import DonePile
from LogicPack.GameLogic import GameLogic
from Table import Table
import cv2


## Data we need:
"""
* Pixel indices for each column in our webcam so we can easily read it. 
* ie. from x-y column 1
* If there is no card found in that column we assume it empty
"""


table = Table()
draw = None
drawCount = 24
state = -1
gameLogic = GameLogic()
frame = None


"""
cardDeck = CardDeck()
cardDeck.getNormalDeck()
cardDeck.mix()
cardDeck.printDeck()


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

    if len(draw) != 0:
        print("Draw: ", draw[-1].value, draw[-1].faction)


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
        card = draw.pop(-1)
        suggestion.toColumn.cards.append(card)
    if suggestion.sugCode == 4:
        drawCards()
        print("Implement card pull")
    if suggestion.sugCode == 5:
        card = draw.pop(-1)
        suggestion.toColumn.cards.append(card)


def drawCards():
    if len(cardDeck.deck) >= 3:
        for x in range(3):
            card = cardDeck.deck.pop(0)
            draw.append(card)
    else:
        emptyDraw()


def emptyDraw():
    if len(cardDeck.deck) > 0:
        for x in range(len(draw) - 1):
            if (cardDeck.deck != 0):
                card = draw.pop(0)
                cardDeck.deck.append(card)
    else:
        for x in range(len(draw)):
            card = draw.pop(0)
            cardDeck.deck.append(card)
    drawCards()



gameLogic = GameLogic()
deal()
drawCards()



while True:
    print(type(table.donePiles[0]))
    printTable()
    if len(draw) == 0:
        drawCards()

    suggestion = gameLogic.getSuggestion(table, draw[-1])

    if suggestion != None:
        makeMove(suggestion)
    input("Press for next move")
"""

def deal():
    for column in table.columns:
        card = card(False, None, None)
        column.cards.append(card)

    for x in range(1,7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(2,7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(3,7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(4,7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(5,7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(6,7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)


## Here we read the last card in a column with a specific index. Might have to take the dataset in this method.
def readColumn(index):
    ## We will take index of the column and maybe the data we found. Dunno yet.
    print("not implemented")

def readDraw():
    ## What we will call to find the drawn card.
    print("not implemented")

def getFrame():
    ## Use opencv to get a relevant frame from our webcam.
    ## Maybe we should display it first
    print("not implemented")
    ## We will return the frame here.
    ## Or it might just be fine to make it a global variable.

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
        card = draw
        suggestion.toColumn.cards.append(card)
        ## Decrement drawCount
    if suggestion.sugCode == 4:
        print("Pull new card")
    if suggestion.sugCode == 5:
        card = draw.pop(-1)
        suggestion.toColumn.cards.append(card)

## We will loop through our table analyzing which cards needs to be defined.
## We do this by looping through the last card in each column. If it is undefined, we call readColumn() whith the matching index.
def findMissingCard():
    idx = 0
    for column in table.columns:
        card = column.cards[-1]
        if card.isShown == False:
            readColumn(idx)
            break
        idx = idx + 1


while True:
    input("wait for input")
    ## Set up everything for snapshot
    ## We make sure that everything is showing when we ask for a snaphot
    ## We will start by being in state -1 Where we will scan
    if state == -1:
        idx = 0
        for column in table.columns:
            readColumn(idx)
            idx + 1
        readDraw()
        state == 0
        gameLogic.getSuggestion(table, draw)
    ## Call
    elif state == 0:
        ## This is a regular round.
        print("Not implemented")




