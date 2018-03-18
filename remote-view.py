import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random
import sys
import requests
'''
symbol = sys.argv[1]
response1 = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD".format(symbol))
#response = requests.get("https://api.iextrading.com/1.0/stock/{}/book?filter=lastSalePrice".format(symbol))
response1 = response1.json()
time.sleep(30)
response2 = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD".format(symbol))
response2 = response2.json()
#print(response)
mostRecentPrice = response1["USD"]
'''

def delay_response():
    #newestPrice = response["trades"][0]["price"]
    newestPrice = response2["USD"]
    return newestPrice


#cryptoList = requests.get("https://www.cryptocompare.com/api/data/coinlist/")
#cryptoList = cryptoList.json()
#cryptoList = [i for i in cryptoList["Data"]]
cryptoList = ['TRX', 'XRP', 'ETH', 'BTC', 'LTC']

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


#API call to ticker here
mostRecentTradeID = None
'''while 1:
    response = requests.get("https://api.iextrading.com/1.0/stock/{}/book?filter=lastSalePrice".format(symbol))
    response = response.json()
    mostRecentPrice = response["trades"][0]["price"]

    tradeID = response["trades"][0]["tradeId"]
    if mostRecentTradeID != tradeID:
        print("$" + str(mostRecentPrice))
        mostRecentTradeID = tradeID'''


if __name__ == "__main__":
    images = makeImageSets(getImages())
    symbol = random.sample(cryptoList, 1)
    print("Up set\n", images[0], "\nDown set", images[1])
    response1 = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD".format(symbol))
    response1 = response1.json()
    print(response1)
    firstPrice = response1["USD"]
    print(symbol, firstPrice, type(firstPrice))
