import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random
import sys
import requests



#credit = json.load(open('cred.json', "r"))
#symbol = sys.argv[1]
#response = requests.get("https://api.iextrading.com/1.0/stock/{}/book?filter=lastSalePrice".format(symbol))
#response = response.json()
#mostRecentPrice = response["trades"][0]["price"]

cryptoList = requests.get("https://www.cryptocompare.com/api/data/coinlist/")
cryptoList = cryptoList.json()
cryptoList = [i for i in cryptoList["Data"]]
print(cryptoList)



def delay_response():
    time.sleep(10)#can change depending on time limit
    newestPrice = response["trades"][0]["price"]
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

'''
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


if __name__ == "__main__":
    images = makeImageSets(getImages())
    print(mostRecentPrice)
    print(images[0])
    print(images[1])
    newPrice = delay_response()
    print newPrice
    randImage = selectRandomImage(images[0], images[1], mostRecentPrice, newPrice)
    print(randImage)
'''
