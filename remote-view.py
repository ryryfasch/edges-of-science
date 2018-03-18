import os
import sys
#from PyQt4.QtGui import *
import time
import json
import random
import sys
import requests
from PIL import Image

if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()




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
    showPIL(image)
    #print(randImage)
