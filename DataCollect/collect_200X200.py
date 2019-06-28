import tkinter as tk

from PIL import Image, ImageTk

import imageGet200X200

latitudeMove = 0.003220
longtudeMove = 0.003050
longitude = -19.094900
#_____________________________________________#
#Change here to move the test to left
testx= -3
testy= 0
#_____________________________________________#
latitude = 33.3905603 + testx*latitudeMove
longitude = -19.094900 - testy*longtudeMove

temp = Image.new("RGB",(100,100))

class counter(object):
    def __init__(self):
        self.No = 1
        self.Counter = 1
        print("!")

    def __iter__(self):
        return self

    def getNo(self):
        return self.No

    def setNo(self,No):
        self.No = No

    def next(self):
        if self.No != 9:

            self.No += 1

            return self.No

        else:
            self.No = 1
            print("Update Picture")
            global longitude
            longitude += 0.003050
            return self.No

def hasRoad(counterA,image,No):
    print("Saved in Road")
    global longitude,latitude,temp
    Long= str(longitude)[0:7]
    Lati= str(latitude)[0:7]
    temp.save('Data/Road/'+Long+"&"+Lati+"&"+str(counterA.getNo())+'.png')
    No = counterA.next()
    print(counterA.getNo())
    if No == 1:
        imageShow = imageGet200X200.imageGet(longitude,latitude)
        imageShow.show()
    image = imageGet200X200.imageSpiltGet(longitude, latitude,No)
    #image2.show()
    temp = image.crop()
    img = ImageTk.PhotoImage(image)
    label_img.configure(image=img)
    label_img.image = img
    window.update()



def noRoad(counterA,image,No):
    print("Saved in Field")
    global longitude, latitude,temp
    Long = str(longitude)[0:7]
    Lati = str(latitude)[0:7]
    temp.save('Data/Field/' + Long + "&" + Lati + "&" + str(counterA.getNo()) + '.png')
    No = counterA.next()
    print(counterA.getNo())
    if No == 1:
        imageShow = imageGet200X200.imageGet(longitude, latitude)
        imageShow.show()
    image = imageGet200X200.imageSpiltGet(longitude, latitude, No)
    # image2.show()
    temp = image.crop()
    img = ImageTk.PhotoImage(image)
    label_img.configure(image=img)
    label_img.image = img
    window.update()

def test(counterA,image,No):
    print("Saved in Field")
    global longitude, latitude,temp
    Long = str(longitude)[0:7]
    Lati = str(latitude)[0:7]
    temp.save('Data/Test/' + Long + "&" + Lati + "&" + str(counterA.getNo()) + '.png')
    No = counterA.next()
    print(counterA.getNo())
    if No == 1:
        imageShow = imageGet200X200.imageGet(longitude, latitude)
        imageShow.show()
    image = imageGet200X200.imageSpiltGet(longitude, latitude, No)
    # image2.show()
    temp = image.crop()
    img = ImageTk.PhotoImage(image)
    label_img.configure(image=img)
    label_img.image = img
    window.update()



window = tk.Tk() #create a window
window.title("Human Learning ")
window.geometry("600x700")
var = tk.StringVar()
counterA = counter() #create a new Counter class
counterA.setNo(1)
No = counterA.getNo()
if No == 1:
    imageShow = imageGet200X200.imageGet(longitude, latitude)
    imageShow.show()
image = imageGet200X200.imageSpiltGet(longitude,latitude,No)
img = ImageTk.PhotoImage(image)
label_img = tk.Label(window,image=img)
label_img.pack()

button = tk.Button(window, command=lambda: hasRoad(counterA,image,No),text = 'Yes', font=('Helvetica', '20') ,highlightbackground='#3DFF33' ,height=5, width=20)
button.pack(padx=20)
button = tk.Button(window, text = 'No', command=lambda: noRoad(counterA,image,No),font=('Helvetica', '20'),highlightbackground='#FF5733' ,height=5, width=20)
button.pack(padx=20)
button = tk.Button(window, text = 'Test', command=lambda: test(counterA,image,No),font=('Helvetica', '20'),highlightbackground='#FF5733' ,height=5, width=20)
button.pack(padx=20)

bon = False

window.mainloop()



