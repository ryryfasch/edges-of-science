import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random
import urllib2
import requests


credit = json.load(open('cred.json'))
params = {'function': 'TIME_SERIES_INTRADAY', 'symbol': 'MSFT', 'interval': '1min', 'apikey': credit.api_key}
print(credit)

def getImages():

    return os.listdir("./images/")


def makeImageSets(images):
    newImages = list(images)
    random.shuffle(newImages)
    random.shuffle(newImages)
    upSet = newImages[0:15]
    downSet = newImages[15:29]

    return upSet, downSet

def selectRandomImage(ticker, upSet, downSet):

    if(ticker > 1):
        return random.choice(upSet)
    else:
        return random.choice(downSet)

#API call to ticker here


response = requests.get("https://www.alphavantage.co/query", params=params)
#print(response.json())

images = makeImageSets(getImages())
