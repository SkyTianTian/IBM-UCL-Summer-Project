from watson_developer_cloud import VisualRecognitionV3
from getImage import *
from Color_Trans import *

import json
import io


def inputRead():
    #longStart = float(input("Please you put the longtitude of your start point: "))
    #latiStart = float(input("Please you put the latitude of your start point: "))
    #longEnd = input("Please you put the longtitude of your end point: ")
    #latiEnd = input("Please you put the latitude of your end point: ")
    longEnd = -19.094900
    latiEnd = 33.390560
    longStart = -19.094000
    latiStart = 33.39080


    return longStart,latiStart,longEnd,latiEnd

def analysisRequire(coordinate):
    longStart,latiStart,longEnd,latiEnd = coordinate
    longGap = 0.003050
    latiGap = 0.003220
    #requireList = [[],[]]


    if longStart > longEnd:
        if latiStart < latiEnd:
            print("Change nothing")
            pass
        else:
            print("Change Long")
            latiMid = latiStart
            latiStart = latiEnd
            latiEnd = latiStart
    else:
        print("Change")
        if latiStart < latiEnd:
            longMid = longStart
            longStart = longEnd
            longEnd = longStart
        else:
            print("Change Lati and Long")
            latiMid = latiStart
            latiStart = latiEnd
            latiEnd = latiStart
            longMid = longStart
            longStart = longEnd
            longEnd = longStart

    longTemp = longStart
    latiTemp = latiStart
    i = 0
    requireList = [[]]

    while (True):
        latiTemp = latiStart
        print(i)
        while (True):
            print(i)
            requireList[i].append((longTemp, latiTemp))
            print("Add", longTemp," , " ,latiTemp)
            print(requireList)
            if latiTemp > latiEnd:
             #   requireList[i].append((longTemp, latiTemp))
                break
            latiTemp += latiGap
        i += 1
        print(i,": i+1")
        if longTemp < longEnd:
            break
        longTemp = longTemp - longGap
        requireList.append([])
    return requireList


if __name__ == "__main__":
    coordinate = inputRead()
    analysisRequire(coordinate)
    fileList = analysisRequire(coordinate)
    #downloadImage(fileList)

    longitude = -19.094900
    latitude = 33.3905603


    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='En8MaCZbEtnirUlnbkZncKBm2RqecjwClCzLOVK8WcYN'
    )
'''
    image = imageGet(longitude,latitude)

    image.convert('RGB').save("res/1.jpg")
    original = open_image('res/1.jpg')
    new = convert_primary(original)
    save_image(new, 'res/new.png')
'''




