import requests as req
from PIL import Image
from io import BytesIO

longitude = -19.094900
latitude = 33.390563
zoom = 18
key = "AIzaSyA9T9FyJ5-hPO6SBDkKO_tUucBvy6M0emk"


URL="https://maps.googleapis.com/maps/api/staticmap?center=-19.094900,33.3905603&zoom=18&size=600x640&maptype=satellite&key=AIzaSyA9T9FyJ5-hPO6SBDkKO_tUucBvy6M0emk"
URL_Comp = "https://maps.googleapis.com/maps/api/staticmap?"+"center="+str(longitude)+","+str(latitude)+"&zoom="+str(zoom)+"&size=600x640&maptype=satellite&key="+key
#print(URL_Comp)
response = req.get(URL_Comp)
image = Image.open(BytesIO(response.content))
image_cut1 = image.crop((0, 0, 600, 600))



a = 0.003220
latitude = 33.390563 + a
URL_Comp = "https://maps.googleapis.com/maps/api/staticmap?"+"center="+str(longitude)+","+str(latitude)+"&zoom="+str(zoom)+"&size=600x640&maptype=satellite&key="+key
response = req.get(URL_Comp)
image = Image.open(BytesIO(response.content))
image_cut2 = image.crop((0, 0, 600, 600))
finalImage =Image.new("RGB",(1200,600))
finalImage.paste(image_cut1)
finalImage.paste(image_cut2,box=(600,0))
img_array1=image_cut1.load()
img_array2=image_cut2.load()
#print(img_array1[599,600])
#print(img_array2[599,0])

check = True
'''
while (check):
    print("Testing Before: ", a)
    a += 0.000001
    longitude = -19.094900 - a
    URL_Comp = "https://maps.googleapis.com/maps/api/staticmap?" + "center=" + str(longitude) + "," + str(
        latitude) + "&zoom=" + str(zoom) + "&size=600x640&maptype=satellite&key=" + key
    response = req.get(URL_Comp)
    image = Image.open(BytesIO(response.content))
    img_array2 = image.load()
    check2 = True
    print("Testing: ",a)
    for i in range (0,599):
        if abs(img_array1[i,600] - img_array2[i,0]) < 10:
            check2 = False
            print(i," : ",img_array1[i, 600],img_array2[i, 0])
            break
    if check2:
        check = False
        print(a)
'''

finalImage.show()