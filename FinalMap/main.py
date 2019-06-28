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
    longStart = -19.09
    latiStart = 33.39


    return longStart,latiStart,longEnd,latiEnd

def analysisRequire(coordinate):
    longStart,latiStart,longEnd,latiEnd = coordinate
    longTemp = longStart
    latiTemp = latiStart
    longGap = 0.003050
    latiGap = 0.003220
    #requireList = [[],[]]
    i = 0

    if longStart > longEnd:
        if latiStart > latiEnd:
            pass
        else:
            latiMid = latiStart
            latiStart = latiEnd
            latiEnd = latiStart
    else:
        if latiStart > latiEnd:
            longMid = longStart
            longStart = longEnd
            longEnd = longStart
        else:
            latiMid = latiStart
            latiStart = latiEnd
            latiEnd = latiStart

    requireList = [[],[]]
    while (True):
        latiTemp = latiStart
        while (True):
            requireList[i].append((longTemp, latiTemp))
            print("Add", longTemp," , " ,latiTemp)
            print(requireList)
            latiTemp -= latiGap
            if latiTemp < latiEnd:
                requireList[i].append((longTemp, latiTemp))
                break
        i += 1
        longTemp = longTemp - longGap
        if longTemp + longGap < longEnd:
            break
    return requireList


if __name__ == "__main__":
    coordinate = inputRead()
    analysisRequire(coordinate)
    fileList = analysisRequire(coordinate)
    print (fileList)


    longitude = -19.094900
    latitude = 33.3905603


    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='En8MaCZbEtnirUlnbkZncKBm2RqecjwClCzLOVK8WcYN'
    )

    image = imageGet(longitude,latitude)

    image.convert('RGB').save("res/1.jpg")
    original = open_image('res/1.jpg')
    new = convert_primary(original)
    save_image(new, 'res/new.png')





