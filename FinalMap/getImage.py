import requests as req
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from colorTransfer import *

from watson import *

def partSelect(No):

    lX = (((No-1)%3))*200
    lY = ((No-1)//3)*200
    rX = lX + 200
    rY = lY + 200
    return lX,lY,rX,rY

def imageGet(long,lati):
    zoom = 18
    key = "AIzaSyA9T9FyJ5-hPO6SBDkKO_tUucBvy6M0emk"

    URL_Comp = "https://maps.googleapis.com/maps/api/staticmap?" + "center=" + str(long) + "," + str(
        lati) + "&zoom=" + str(zoom) + "&size=600x640&maptype=satellite&key=" + key
    print(URL_Comp)
    response = req.get(URL_Comp)
    image = Image.open(BytesIO(response.content))
    image_cut = image.crop((0, 0, 600, 600))
    #image_cut.show()
    return(image_cut)

def imageSpiltGet(long,lati,No):
    zoom = 18
    key = "AIzaSyA9T9FyJ5-hPO6SBDkKO_tUucBvy6M0emk"

    URL_Comp = "https://maps.googleapis.com/maps/api/staticmap?" + "center=" + str(long) + "," + str(
        lati) + "&zoom=" + str(zoom) + "&size=600x640&maptype=satellite&key=" + key

    response = req.get(URL_Comp)
    image = Image.open(BytesIO(response.content))
    image_cut = image.crop(partSelect(No))
    return image_cut

def saveSplit(image,row,col):
    for i in range(1,10):
        image_cut = image.crop(partSelect(i))
        fileName = "res/"+str(row) + "_"+ str(col) + "_" + str(i) +".jpg"
        image_cut.convert('RGB').save(fileName)

def saveSplitLearn(image,row,col):
    for i in range(1,10):
        image_cut = image.crop(partSelect(i))
        fileName = "res/"+str(row) + "_"+ str(col) + "_" + str(i) +".jpg"
        image_cut.convert('RGB').save(fileName)



def downloadImage(fileList):
    row = 0
    for i in fileList:
        col = 0
        for j in i:
            image = imageGet(j[0],j[1])
            saveSplit(image,row,col)
            col += 1
        row = row + 1

def mergeImage(row,col):
    newImage = Image.new("RGB", (600, 600))
    for i in range(1,10):
        fileName = "res/" + str(row) + "_" + str(col) + "_" + str(i) + ".jpg"
        im = Image.open(fileName)
        newImage.paste(im,box=(partSelect(i)))
        bigFileName = "res/"+ str(row) + "_" + str(col) + ".jpg"
        newImage.convert('RGB').save(bigFileName)
        print("Generate file: ", bigFileName)
        #test Part


def generateMap(fileList):
    longlen = len(fileList)
    latilen = len(fileList[0])
    newImage = Image.new("RGB",(latilen*600,longlen*600))
    for i in range(0,longlen):
        for j in range(0,latilen):
            mergeImage(i,j)
            bigFileName = "res/" + str(i) + "_" + str(j) + ".jpg"
            im = Image.open(bigFileName)
            newImage.paste(im, box=((j)*600,(i)*600))
    newImage.convert('RGB').save("res/final.jpg")

def learn(fileList):
    longlen = len(fileList)
    latilen = len(fileList[0])
    map = Image.open("res/final.jpg")
    for long in range(0, longlen):
        for lati in range(0, latilen):
            for i in range(1, 10):
                fileName = str(long) + "_" + str(lati) + "_" + str(i)
                result = trainWithFile(fileName)
                print(result)
                if result > 0.4:
                    im = Image.open("res/" + fileName + ".jpg")
                    imTrans = convert_primary(im)
                    #imTrans.show()
                    LONG = long*600 + ((i-1)//3)*200
                    LATI = lati*600 + ((i-1)%3)*200
                    map.paste(imTrans, box = (LATI,LONG))
    map.convert('RGB').save("res/finalTransfered.jpg")












if __name__ == "__main__":
    #fileList = [[(-19.09, 33.38734)]]
    #downloadImage([[(-19.09, 33.38734)]])
    #mergeImage(0,0)
    #imageGet(-19.09, 33.38734).show()
    fileList = [[(-19.094, 33.39056), (-19.094, 33.39378)],
                [(-19.097050000000003, 33.39056), (-19.097050000000003, 33.39378)]]
    downloadImage(fileList)
    generateMap(fileList)
    learn(fileList)


