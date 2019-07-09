from tkinter import *
import imageGet
from PIL import Image, ImageTk
import numpy as np
import json
import os


latitudeMove = 0.003220
longtudeMove = 0.003050

#startX,startY,endX,endY
locationList = []
#_____________________________________________#
#Change here to move the test to left
testx= -20
testy= 0
#_____________________________________________#
latitude = 33.3905603 + testx*latitudeMove
longitude = -19.094900 - testy*longtudeMove




def ui_process():
    global root
    root = Tk()
    root.geometry("800x900+500+100")
    global longitude,latitude
    global title
    textString = "location: " + str(latitude) + "  " + str(longitude)
    title = Label(root, text= textString)
    title.place(x=400, y=40, anchor="center") #location

    aerialPhoto = imageGet.imageGet(longitude, latitude)
    photoimg = ImageTk.PhotoImage(aerialPhoto, size="600x600")
    global canvas
    canvas = Canvas(width=600, height=600)
    canvas.place(x=400, y=350, anchor="center")
    canvas.create_image((0,0),image=photoimg, anchor = NW)
    canvas.configure(bg = "systemTransparent")
    #canvas.create_line(0, 0, 600, 600)
    canvas.bind("<Button-1>",start1)
    canvas.bind("<ButtonRelease-1>",end1)
    Skip = Button(root, text="Skip", command = lambda: skip(),font=('Helvetica', '20'),highlightbackground='#FF5733' ,height=5, width=20)
    Skip.place(x=30,y=700)
    Save = Button(root, text="Save", command = lambda: save(),font=('Helvetica', '20'),highlightbackground='#3DFF33' ,height=5, width=20)
    Save.place(x=530, y=700)

    mainloop()

def skip():
    global longitude, latitude
    longitude += 0.003050
    aerialPhoto = imageGet.imageGet(longitude, latitude)
    photoimg = ImageTk.PhotoImage(aerialPhoto, size="600x600")
    canvas.delete("all")
    canvas.create_image((0,0),image=photoimg, anchor = NW)
    root.update()
    locationList = []

def save():
    global longitude, latitude,locationList
    saveJson()
    saveImage()
    longitude += 0.003050
    aerialPhoto = imageGet.imageGet(longitude, latitude)
    photoimg = ImageTk.PhotoImage(aerialPhoto, size="600x600")
    canvas.delete("all")
    canvas.create_image((0, 0), image=photoimg, anchor=NW)
    root.update()
    locationList = []

def saveJson():
    global locationList
    objectDataList = []
    for i in locationList:
        print(i)
        #print(type(i[3]))
        top = i[0]
        height = i[1]
        left = i[2]
        width = i[3]
        object = {"object": "building", "location": {"top": top, "height": height, "left": left, "width": width}
        }
        objectDataList.append(object)


    result = json.dumps({"objects": objectDataList}
                   , separators=(',', ':'))
    print(result)
    global longitude, latitude
    Long = str(longitude)[0:7]
    Lati = str(latitude)[0:7]

    text_file = open("Data/Model/Json/"+ Long + "&" + Lati + ".json", "w")
    text_file.write(result)
    text_file.close()

'''
{
    "objects":[
        {
            "object":"Cookie",
            "location":{
                "top":10,
                "height":10,
                "left":22,
                "width":10
            }
        }
    ]
}
'''

def saveImage():
    global longitude, latitude, temp
    Long = str(longitude)[0:7]
    Lati = str(latitude)[0:7]
    fileName ="Data/Model/Image/" + Long + "&" + Lati + ".png"
    aerialPhoto = imageGet.imageGet(longitude, latitude)
    aerialPhoto.convert('RGB').save(fileName)

    #aerialPhoto.save(fileName)




def start1(event):
    print("start:", event.x, event.y)
    global startX,startY
    startX = event.x
    startY = event.y


def end1(event):
    print("end:", event.x, event.y)
    global endX,endY,startY,startX
    endX = event.x
    endY = event.y
    location = [startY,endY-startY,startX,endX-startX]
    print(location)
    global locationList
    locationList.append(location)
    print(locationList)

    global canvas
    canvas.create_rectangle(startX, startY,endX,endY, outline='green',width=5)



if __name__=="__main__":
    ui_process()
    #saveImage()
    #saveJson()



