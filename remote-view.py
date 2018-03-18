import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random
import sys
import requests
from PIL import Image

symbol = sys.argv[1]
response1 = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD".format(symbol))
#response = requests.get("https://api.iextrading.com/1.0/stock/{}/book?filter=lastSalePrice".format(symbol))
response1 = response1.json()
time.sleep(30)
response2 = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD".format(symbol))
response2 = response2.json()
#print(response)
mostRecentPrice = response1["USD"]

def delay_response():
    #can change depending on time limit
    #newestPrice = response["trades"][0]["price"]
    newestPrice = response2["USD"]
    return newestPrice

def getImages():

    return os.listdir("./images/")


def makeImageSets(images):
    newImages = list(images)
    random.shuffle(newImages)
    random.shuffle(newImages)
    upSet = newImages[0:15]
    downSet = newImages[15:29]

    return upSet, downSet

def selectRandomImage(upSet, downSet, price1, price2):
    change = price1 - price2
    if(change > 0):
        return random.choice(upSet)
    elif(change < 0):
        return random.choice(downSet)
    else:
        return 'no change'




images = makeImageSets(getImages())
print(mostRecentPrice)
print(images[0])
print(images[1])
newPrice = delay_response()
print newPrice
randImage = selectRandomImage(images[0], images[1], mostRecentPrice, newPrice)
print(randImage)
