from Card import Card
from CardDeck import CardDeck
from Column import Column

cardDeck = CardDeck()
columns = []


def initColumns():
    for x in range(7):
        column = Column()
        columns.append(column)


def dealCards():
    t = 0
    for x in range(7):
        for x in columns:
            if (x <= t):
                topCard = cardDeck.deck[0]
                cardDeck.deck.pop(0)
                if (columns[x].getCard != None):
                    layOnColumn(x, topCard)
                else:
                    lastCard = Card(columns[x].getCard)
                    while (lastCard != None):
                        lastCard = lastCard.nextCard
                    layCard(lastCard, topCard)
            t = + 1


def layOnColumn(column, newCard):
    column.firstCard = newCard
    newCard.prevCard = column

def layCard(lastCard, newCard):
    lastCard.nextCard = newCard
    newCard.prevCard = lastCard

def printTable():
    t = int(0)
    while(True):
        for x in columns:
            printCard = Card(columns[x].firstCard)
            for y in range(0,t):
                printCard = printCard.nextCard
            t = + 1


def printCard(column, i):
    currentCard = column.firstCard
    for x in range(i):
        currentCard = currentCard.nextCard
    return currentCard

def printLine(t):
    for x in range(7):
        printCard(columns[x], t)


cardDeck.mix()
dealCards()
initColumns()
