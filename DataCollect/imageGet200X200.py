from io import BytesIO

import requests as req
from PIL import Image


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
