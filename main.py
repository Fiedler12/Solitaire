from LogicPack.GameLogic import GameLogic
from Table import Table
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
from matplotlib import pyplot as plt

from TensorFlow1.models.research.object_detection.utils import label_map_util
## Might not need this one below. But we have it.
from TensorFlow1.models.research.object_detection.utils import visualization_utils as vis_util

MODEL_NAME = 'inference_graph'
IMAGE_NAME = 'test1.jpg'

CWD_PATH = os.getcwd()

## Path to our model.
PATH_TO_CKPT = os.path.join(CWD_PATH, 'venv', 'TensorFlow1', 'models', 'research', 'object_detection', MODEL_NAME,
                            'frozen_inference_graph.pb')

## Path to our labels
PATH_TO_LABELS = os.path.join(CWD_PATH, 'venv', 'TensorFlow1', 'models', 'research', 'object_detection', 'training',
                              'labelmap.pbtxt')

PATH_TO_IMAGE = os.path.join(CWD_PATH, IMAGE_NAME)

## Number of different classes we expect.
NUM_CLASSES = 52

## Path to the names of our classes being loaded in here.
## We match this to categories so they have an index.
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.compat.v1.Session(graph=detection_graph)

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

## Data we need:
"""
* Pixel indices for each column in our webcam so we can easily read it. 
* ie. from x-y column 1
* If there is no card found in that column we assume it empty
"""

img_height = 1080
img_width = 1920

image = cv2.imread(PATH_TO_IMAGE)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_expanded = np.expand_dims(image_rgb, axis=0)

# Perform the actual detection by running the model with the image as input

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

    for x in range(1, 7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(2, 7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(3, 7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(4, 7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(5, 7):
        card = card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(6, 7):
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
    ## Or it might just be fine to make it a global variable we define. We'll see.


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


def revealCard(card, id):
    if id == 1:
        card.isShown = True
        card.faction = "D"
        card.value = 1
        card.getColor()
    elif id == 2:
        card.isShown = True
        card.faction = "H"
        card.value = 1
        card.getColor()
    elif id == 3:
        card.isShown = True
        card.faction = "C"
        card.value = 1
        card.getColor()
    elif id == 4:
        card.isShown = True
        card.faction = "S"
        card.value = 1
        card.getColor()
    elif id == 5:
        card.isShown = True
        card.faction = "D"
        card.value = 2
        card.getColor()
    elif id == 6:
        card.isShown = True
        card.faction = "H"
        card.value = 2
        card.getColor()
    elif id == 7:
        card.isShown = True
        card.faction = "C"
        card.value = 2
        card.getColor()
    elif id == 8:
        card.isShown = True
        card.faction = "S"
        card.value = 2
        card.getColor()
    elif id == 9:
        card.isShown = True
        card.faction = "D"
        card.value = 3
        card.getColor()
    elif id == 10:
        card.isShown = True
        card.faction = "H"
        card.value = 3
        card.getColor()
    elif id == 11:
        card.isShown = True
        card.faction = "C"
        card.value = 3
        card.getColor()
    elif id == 12:
        card.isShown = True
        card.faction = "S"
        card.value = 3
        card.getColor()
    elif id == 13:
        card.isShown = True
        card.faction = "D"
        card.value = 4
        card.getColor()
    elif id == 14:
        card.isShown = True
        card.faction = "H"
        card.value = 4
        card.getColor()
    elif id == 15:
        card.isShown = True
        card.faction = "C"
        card.value = 4
        card.getColor()
    elif id == 16:
        card.isShown = True
        card.faction = "S"
        card.value = 4
        card.getColor()
    elif id == 17:
        card.isShown = True
        card.faction = "D"
        card.value = 5
        card.getColor()
    elif id == 18:
        card.isShown = True
        card.faction = "H"
        card.value = 5
        card.getColor()
    elif id == 19:
        card.isShown = True
        card.faction = "C"
        card.value = 5
        card.getColor()
    elif id == 20:
        card.isShown = True
        card.faction = "S"
        card.value = 5
        card.getColor()
    elif id == 21:
        card.isShown = True
        card.faction = "D"
        card.value = 6
        card.getColor()
    elif id == 22:
        card.isShown = True
        card.faction = "H"
        card.value = 6
        card.getColor()
    elif id == 23:
        card.isShown = True
        card.faction = "C"
        card.value = 6
        card.getColor()
    elif id == 24:
        card.isShown = True
        card.faction = "S"
        card.value = 6
        card.getColor()
    elif id == 25:
        card.isShown = True
        card.faction = "D"
        card.value = 7
        card.getColor()
    elif id == 26:
        card.isShown = True
        card.faction = "H"
        card.value = 7
        card.getColor()
    elif id == 27:
        card.isShown = True
        card.faction = "C"
        card.value = 7
        card.getColor()
    elif id == 28:
        card.isShown = True
        card.faction = "S"
        card.value = 7
        card.getColor()
    elif id == 29:
        card.isShown = True
        card.faction = "D"
        card.value = 8
        card.getColor()
    elif id == 30:
        card.isShown = True
        card.faction = "H"
        card.value = 8
        card.getColor()
    elif id == 31:
        card.isShown = True
        card.faction = "C"
        card.value = 8
        card.getColor()
    elif id == 32:
        card.isShown = True
        card.faction = "S"
        card.value = 8
        card.getColor()
    elif id == 33:
        card.isShown = True
        card.faction = "D"
        card.value = 9
        card.getColor()
    elif id == 34:
        card.isShown = True
        card.faction = "H"
        card.value = 9
        card.getColor()
    elif id == 35:
        card.isShown = True
        card.faction = "C"
        card.value = 9
        card.getColor()
    elif id == 36:
        card.isShown = True
        card.faction = "S"
        card.value = 9
        card.getColor()
    elif id == 37:
        card.isShown = True
        card.faction = "D"
        card.value = 10
        card.getColor()
    elif id == 38:
        card.isShown = True
        card.faction = "H"
        card.value = 10
        card.getColor()
    elif id == 39:
        card.isShown = True
        card.faction = "C"
        card.value = 10
        card.getColor()
    elif id == 40:
        card.isShown = True
        card.faction = "S"
        card.value = 10
        card.getColor()
    elif id == 41:
        card.isShown = True
        card.faction = "D"
        card.value = 11
        card.getColor()
    elif id == 42:
        card.isShown = True
        card.faction = "H"
        card.value = 11
        card.getColor()
    elif id == 43:
        card.isShown = True
        card.faction = "C"
        card.value = 11
        card.getColor()
    elif id == 44:
        card.isShown = True
        card.faction = "S"
        card.value = 11
        card.getColor()
    elif id == 45:
        card.isShown = True
        card.faction = "D"
        card.value = 12
        card.getColor()
    elif id == 46:
        card.isShown = True
        card.faction = "H"
        card.value = 12
        card.getColor()
    elif id == 47:
        card.isShown = True
        card.faction = "C"
        card.value = 12
        card.getColor()
    elif id == 48:
        card.isShown = True
        card.faction = "S"
        card.value = 12
        card.getColor()
    elif id == 49:
        card.isShown = True
        card.faction = "D"
        card.value = 13
        card.getColor()
    elif id == 50:
        card.isShown = True
        card.faction = "H"
        card.value = 13
        card.getColor()
    elif id == 51:
        card.isShown = True
        card.faction = "C"
        card.value = 13
        card.getColor()
    elif id == 52:
        card.isShown = True
        card.faction = "S"
        card.value = 13
        card.getColor()

def fetchPicture():
    vidcap = cv2.VideoCapture(0)
    if vidcap.isOpened:
        print("Camera open")
        ret, frame = vidcap.read()
        if ret:
            cv2.imshow("Frame", frame)
        else:
                print("Frame error")
    else:
        print("Unable to access camera")




def performImageProcessing():
    image = cv2.imread(PATH_TO_IMAGE)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)

    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})
    idx = 0

    realBoxes = np.squeeze(boxes)
    realScores = np.squeeze(scores)
    realClasses = np.squeeze(classes).astype(np.int32)

    for x in realScores:
        if x < 0.70:
            break
        idx = idx + 1

    return realBoxes[:idx], realScores[:idx], realClasses[:idx]


boxes, scores, classes = performImageProcessing()

print(boxes)

"""
input("Set up your cards")
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
"""
