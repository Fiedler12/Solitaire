from CardDeck import CardDeck
from Column import Column

cardDeck = CardDeck()
columns = []

def dealCards():
    for x in range(7):
        column = Column()
        columns.append(column)
        for x in columns:
            topCard = cardDeck.deck[0]
            cardDeck.deck.pop(0)
            layOnColumn(x, topCard)


def layOnColumn(column, newCard):
     column.firstCard = newCard
     newCard.prevCard = column


cardDeck.mix()
dealCards()
for x in columns:
    print()