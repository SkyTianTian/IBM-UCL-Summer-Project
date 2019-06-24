import requests as req
from PIL import Image
from io import BytesIO

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
