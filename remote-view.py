import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random
import sys
import requests

print(sys.argv[1])
credit = json.load(open('cred.json', "r"))


#https://api.iextrading.com/1.0/stock/snap/book?filter=lastSalePrice
#params = {'function': 'TIME_SERIES_INTRADAY', 'symbol': 'MSFT', 'interval': '1min', 'apikey': credit["api_key"]}
#print(credit)
symbol = sys.argv[1]
response = requests.get("https://api.iextrading.com/1.0/stock/{}/book?filter=lastSalePrice".format(symbol))
response = response.json()
mostRecentPrice = response["trades"][0]["price"]

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




images = makeImageSets(getImages())
print(mostRecentPrice)
print(images[0])
print(images[1])
newPrice = delay_response()
print newPrice
randImage = selectRandomImage(images[0], images[1], mostRecentPrice, newPrice)
print(randImage)
