import tkinter as tk
import imageGet
import sys
from PIL import Image, ImageTk

longitude = -19.094900
latitude = 33.3905603



def hasRoad(image,long,lati,No):
    print("Saved in Road")
    global longitude,latitude,image2
    longitude += 0.003050
    Long= str(long)[0:7]
    Lati= str(lati)[0:7]
    image.save('Data/Road/'+Long+"&"+Lati+"&"+str(No)+'.png')
    image2 = imageGet.imageGet(longitude, latitude)
    #image2.show()
    img = ImageTk.PhotoImage(image2)
    label_img.configure(image=img)
    label_img.image = img
    window.update()



def noRoad(image,long,lati,No):
    print("Saved in Field")
    global longitude, latitude, image2
    longitude += 0.003050
    Long = str(long)[0:7]
    Lati = str(lati)[0:7]
    image.save('Data/Field/'+Long+"&"+Lati+"&"+str(No)+'.png')
    image2 = imageGet.imageGet(longitude, latitude)
    # image2.show()
    img = ImageTk.PhotoImage(image2)
    label_img.configure(image=img)
    label_img.image = img
    window.update()

def callback(longitude,latitude):
    global img
    print("Call Back")
    img = imageGet.imageGet(longitude,latitude)
    label_img.configure(image = img)
    label_img.image = img

image2 = imageGet.imageGet(longitude,latitude)
window = tk.Tk() #create a window
window.title("Human Learning ")
window.geometry("600x700")
image2.show()
var = tk.StringVar()
img = ImageTk.PhotoImage(image2)
label_img = tk.Label(window,image=img)
label_img.pack()
button = tk.Button(window, command=lambda: hasRoad(image2,longitude,latitude,4),text = 'Yes', font=('Helvetica', '20') ,highlightbackground='#3DFF33' ,height=5, width=20)
#button.bind("<Next>", callback)
button.pack(padx=20, side=tk.LEFT)
button = tk.Button(window, text = 'No', command=lambda: noRoad(image2,longitude,latitude,4),font=('Helvetica', '20'),highlightbackground='#FF5733' ,height=5, width=20)
button.pack(padx=20, side=tk.RIGHT)

bon = False

window.mainloop()

