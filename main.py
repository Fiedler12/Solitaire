from Card import Card
from LogicPack.GameLogic import GameLogic
from Table import Table
import os
import cv2
import numpy as np
import tensorflow as tf
import sys

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from TensorFlow2.models.research.object_detection.utils import label_map_util
## Might not need this one below. But we have it.
from TensorFlow2.models.research.object_detection.utils import visualization_utils as vis_util

print("starting fetch")
vidcap = cv2.VideoCapture(0)
print("1")

vidcap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vidcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Camera ready")

MODEL_NAME = 'inference_graph'
IMAGE_NAME = 'test1.jpg'

CWD_PATH = os.getcwd()

## Path to our model.
PATH_TO_CKPT = os.path.join(CWD_PATH,  'TensorFlow2', 'models', 'research', 'object_detection', MODEL_NAME,
                            'frozen_inference_graph.pb')

## Path to our labels
PATH_TO_LABELS = os.path.join(CWD_PATH,  'TensorFlow2', 'models', 'research', 'object_detection', 'training',
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
columnIdx = []

column1 = [0.0, 0.1406]
columnIdx.append(column1)

column2 = [0.1406, 0.2656]
columnIdx.append(column2)

column3 = [0.2656, 0.3828]
columnIdx.append(column3)

column4 = [0.3828, 0.50]
columnIdx.append(column4)

column5 = [0.50, 0.6171]
columnIdx.append(column5)

column6 = [0.6171, 0.7444]
columnIdx.append(column6)

column7 = [0.7444, 0.8516]
columnIdx.append(column7)

column8 = [0.8516, 0.9688]
columnIdx.append(column8)

img_height = 1080
img_width = 1920

image = cv2.imread(PATH_TO_IMAGE)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_expanded = np.expand_dims(image_rgb, axis=0)

# Perform the actual detection by running the model with the image as input

table = Table()
stack = []
draw = []
drawCount = 24
state = -1
gameLogic = GameLogic()

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
        card = Card(False, None, None)
        column.cards.append(card)

    for x in range(1, 7):
        card = Card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(2, 7):
        card = Card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(3, 7):
        card = Card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(4, 7):
        card = Card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(5, 7):
        card = Card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(6, 7):
        card = Card(False, None, None)
        table.columns[x].cards.append(card)

    for x in range(0,24):
        card = Card(False, None, None)
        stack.append(card)

    drawCards()


## Here we read the last card in a column with a specific index. Might have to take the dataset in this method.
def readColumn(index):
    ## We will take index of the column and maybe the data we found. Dunno yet.
    print("finding card matching column ", index)
    idx = 0
    for x in boxes:
        if x[1] > columnIdx[index][0] and x[3] < columnIdx[index][1]:
            print("Card found")
            table.columns[index-1].cards[-1].revealCard(classes[idx])
            table.columns[index - 1].cards[-1].getColor()
            print("card is now found to be ", table.columns[index - 1].cards[-1].faction, table.columns[index - 1].cards[-1].value)
            break
        idx = idx + 1
    if table.columns[index - 1].cards[-1].value == None:
        input("Unable to read column ", index, " please adjust and press enter")
        fetchPicture()
        readColumn(index)



def readDraw():
    ## What we will call to find the drawn card.
    print("Finding draw")
    idx = 0
    for x in boxes:
        if x[1] > columnIdx[0][0] and x[3] < columnIdx[0][1]:
            print("draw found")
            draw[-1].revealCard(classes[idx])
            draw[-1].getColor()
            print("Draw is ", draw[-1].faction, draw[-1].value)
        idx = idx + 1
    if draw[-1].value == None:
        input("Draw not found. Adjust and press enter")
        fetchPicture()
        readDraw()



def makeMove(suggestion):
    if (len(stack) + len(draw) == 3) and len(draw) != 3:
        print("turn talon final time")
        drawCards()
        return
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
        print("Donepile move: ", suggestion.fromCard.value, suggestion.fromCard.faction)
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
        ## Decrement drawCount
    if suggestion.sugCode == 4:
        print("Pull new card")
        drawCards()
    if suggestion.sugCode == 5:
        card = draw.pop(-1)
        suggestion.toColumn.cards.append(card)


## We will loop through our table analyzing which cards needs to be defined.
## We do this by looping through the last card in each column. If it is undefined, we call readColumn() whith the matching index.
def findMissingCard():
    idx = 1
    if draw[-1].isShown == False:
        readDraw()

    for column in table.columns:
        if len(column.cards) != 0:
            card = column.cards[-1]
            if card.isShown == False:
                readColumn(idx)
                break
            idx = idx + 1




def fetchPicture():
    if vidcap.isOpened:
        print("Camera open")
        ret, frame = vidcap.read()
        if ret:
            return frame
        else:
                print("Frame error")
    else:
        print("Unable to access camera")


def performImageProcessing(image):
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


def printTable():
    for column in table.columns:
        if len(column.cards) != 0:
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

    if draw != None:
        print("Draw: ", draw[-1].value, draw[-1].faction)

def drawCards():
    if len(stack) >= 3:
        for x in range(3):
            card = stack.pop(0)
            draw.append(card)
    else:
        emptyDraw()


def emptyDraw():
    if len(stack) > 0:
        for x in range(len(draw) - 1):
            if (stack != 0):
                card = draw.pop(0)
                stack.append(card)
    else:
        for x in range(len(draw)):
            card = draw.pop(0)
            stack.append(card)
    drawCards()


deal()

while True:
    input("Input to take and scan")
    image = fetchPicture()
    boxes, scores, classes = performImageProcessing(image)
    ## Set up everything for snapshot
    ## We make sure that everything is showing when we ask for a snaphot
    ## We will start by being in state -1 Where we will scan
    if state == -1:
        idx = 1
        for column in table.columns:
            readColumn(idx)
            idx = idx + 1
        readDraw()
        printTable()
        state = 0
        suggestion = gameLogic.getSuggestion(table, draw[-1])
        makeMove(suggestion)

    elif state == 0:
        findMissingCard()
        if draw[-1].value == None:
            readDraw()
        printTable()
        if len(draw) + len(stack) != 0:
            suggestion = gameLogic.getSuggestion(table, draw[-1])
            makeMove(suggestion)
        else:
            suggestion = gameLogic.getEndSuggestion(table)
            makeMove(suggestion)
        ## This is a regular round.


