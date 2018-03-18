import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random
import sys
import requests


credit = json.load(open('cred.json', "r"))


#https://api.iextrading.com/1.0/stock/snap/book?filter=lastSalePrice
#params = {'function': 'TIME_SERIES_INTRADAY', 'symbol': 'MSFT', 'interval': '1min', 'apikey': credit["api_key"]}
#print(credit)
symbol = sys.argv[1]
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
mostRecentTradeID = None
while 1:
    response = requests.get("https://api.iextrading.com/1.0/stock/{}/book?filter=lastSalePrice".format(symbol))
    response = response.json()
    mostRecentPrice = response["trades"][0]["price"]

    tradeID = response["trades"][0]["tradeId"]
    if mostRecentTradeID != tradeID:
        print("$" + str(mostRecentPrice))
        mostRecentTradeID = tradeID

images = makeImageSets(getImages())
