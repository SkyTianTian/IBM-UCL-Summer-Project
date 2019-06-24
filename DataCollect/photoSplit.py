import requests as req
from PIL import Image
from io import BytesIO

def partSelect(No):
    lX = ((No-1)%6)*100
    lY = (No//6)*100
    rX = lX + 100
    rY = lY + 100
    return lX,lY,rX,rY




longitude = -19.094900
latitude = 33.3905603
zoom = 18
key = "AIzaSyA9T9FyJ5-hPO6SBDkKO_tUucBvy6M0emk"


URL="https://maps.googleapis.com/maps/api/staticmap?center=-19.094900,33.3905603&zoom=18&size=600x640&maptype=satellite&key=AIzaSyA9T9FyJ5-hPO6SBDkKO_tUucBvy6M0emk"
URL_Comp = "https://maps.googleapis.com/maps/api/staticmap?"+"center="+str(longitude)+","+str(latitude)+"&zoom="+str(zoom)+"&size=600x640&maptype=satellite&key="+key
print(URL_Comp)
response = req.get(URL_Comp)
image = Image.open(BytesIO(response.content))
image_cut = image.crop((0, 0, 600, 600))
image_cut.show()
image_Crop_Test = image_cut.crop(partSelect(2))
image_Crop_Test2 = image_cut.crop(partSelect(3))
image_Crop_Merge = Image.new('RGB',(200,100))
image_Crop_Merge.paste(image_Crop_Test)
image_Crop_Merge.paste(image_Crop_Test2 , box=(100,0))






print(type(image_Crop_Merge))
image_Crop_Merge.show()