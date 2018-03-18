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
def delay_response(symbol):
    time.sleep(15)
    response2 = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD".format(symbol))
    response2 = response2.json()
    mostRecentPrice = response2["USD"]
    newestPrice = response2["USD"]
    return newestPrice


#cryptoList = requests.get("https://www.cryptocompare.com/api/data/coinlist/")
#cryptoList = cryptoList.json()
#cryptoList = [i for i in cryptoList["Data"]]
#cryptoList = ['TRX', 'XRP', 'ETH', 'BTC', 'LTC']

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
    change = price2 - price1
    if(change > 0):
        return random.choice(upSet)
    elif(change < 0):
        return random.choice(downSet)
    else:
        return 'no change'


#API call to ticker here
'''
mostRecentTradeID = None
while 1:
    response = requests.get("https://api.iextrading.com/1.0/stock/{}/book?filter=lastSalePrice".format(symbol))
    response = response.json()
    mostRecentPrice = response["trades"][0]["price"]

    tradeID = response["trades"][0]["tradeId"]
    if mostRecentTradeID != tradeID:
        print("$" + str(mostRecentPrice))
        mostRecentTradeID = tradeID
'''

if __name__ == "__main__":

    images = makeImageSets(getImages())
    print("Downset\n", images[1], "Upset\n", images[0])
    response1 = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD".format(symbol))
    response1 = response1.json()
    mostRecentPrice = response1["USD"]
    print(mostRecentPrice)
    newPrice = delay_response(symbol)
    print(newPrice)
    randImage = selectRandomImage(images[0], images[1], mostRecentPrice, newPrice)
    image = Image.open("./images/{}".format(randImage))
    image.show()
    #print(randImage)
