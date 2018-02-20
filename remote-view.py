import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random


#data = json.load(open('cred.json'))

def getImages():

    return os.listdir("./images/")


def makeImageSets(images):
    newImages = list(images)
    random.shuffle(newImages)
    random.shuffle(newImages)
    upSet = newImages[0:15]
    downSet = newImages[15:29]

    return upSet, downSet

#def selectRandomImage(ticker, upSet, downSet):
#API call to ticker here

print(makeImageSets(getImages()))
