#imports 

##for UI
import tkinter
from tkinter import *
from tkinter import tix
import tkinter as tk

##for Image process
import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from PIL import *
from PIL import Image, ImageFont, ImageDraw

##for path track
import os

##for email

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import smtplib



class Application(Frame) :
    def __init__(self, master):
        """initialize the frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        
    def fileSelect(self):
        self.fileName = filedialog.askopenfilename(filetypes = ( ("JPEG", ".jpg"),("PNG IMage", ".png"),("GIF Image", ".GIF"),("all Files","*.*")))
        print(self.fileName)

        return self.fileName
         

    def imageMaker(self):

        self.fileName = self.fileName

        #bring in text from widget

        text = self.cardTextStr.get()
        print(text)

        self.img = PIL.Image.open(self.fileName)
        self.draw = PIL.ImageDraw.Draw(self.img)

        Size = self.fontSize.get()
        size = int(Size)
        print(size)
        self.font = ImageFont.truetype('MORPHEUS.TTF',size, encoding="unic") #change the TTF for text effect
                                                                           #The number is the font size

        Red = self.colorRed.get()
        r = int(Red)
        print(r)

        Green = self.colorGreen.get()
        g = int(Green)
        print(g)

        Blue = self.colorBlue.get()
        b = int(Blue)
        print(b)

        xA = self.horz.get()
        x = int(xA)
        print(x)

        yA = self.vert.get()
        y = int(yA)
        print(y)
        
        self.draw.text((x,y), text, (r,g,b), font=self.font)
        self.doodle = self.img.save('postcard.jpg')
        return self.doodle

        
##Show Image script on button click##        
    def showImage(self):
                
        self.postCard = os.path.abspath("postcard.jpg")
        print(self.postCard)

        im = PIL.Image.open(self.postCard)
        im.show()
        

    def create_widgets(self):
        """create button, text and entry widgets"""
        self.selectFile_button = Button(self, text = "Please Pick a File", command = self.fileSelect)
        self.selectFile_button.grid(row = 0, column = 1, columnspan = 3, sticky = W)

        #User imput text
        self.cardTextStr = StringVar()
        self.postcardTextLabel = Label(self,text = "Enter your E-Postcard's text").grid(row=2,column=0,sticky=W)
        self.cardText = Entry(self, textvariable = self.cardTextStr).grid()

        #user input font size
        self.fontSize = StringVar()
        self.fontSizeLabel = Label(self,text = "Enter the font size").grid(row=2,column=2,sticky=W)
        self.cardTextSize = Entry(self, textvariable = self.fontSize).grid(row=3,column=2,sticky=W)

        #user input color red value
        self.colorRed = StringVar()
        self.colorRedLabel = Label(self,text = "Enter the red value").grid(row=5,column=0,sticky=W)
        self.cardTextColorRed = Entry(self, textvariable = self.colorRed).grid(row=6,column=0,sticky=W)

        #user input color green value
        self.colorGreen = StringVar()
        self.colorGreenLabel = Label(self,text = "Enter the green value").grid(row=5,column=1,sticky=W)
        self.cardTextColorGreen = Entry(self, textvariable = self.colorGreen).grid(row=6,column=1,sticky=W)

        #user input color blue value
        self.colorBlue = StringVar()
        self.colorBlueLabel = Label(self,text = "Enter the blue value").grid(row=5,column=2,sticky=W)
        self.cardTextColorBlue = Entry(self, textvariable = self.colorBlue).grid(row=6,column=2,sticky=W)

        #user input horizonal value
        self.horz = StringVar()
        self.horzLabel = Label(self,text = "Enter the whore value").grid(row=7,column=0,sticky=W)
        self.cardTextHorz = Entry(self, textvariable = self.horz).grid(row=8,column=0,sticky=W)

        #user input vertical value
        self.vert = StringVar()
        self.vertLabel = Label(self,text = "Enter the vertical value").grid(row=7,column=2,sticky=W)
        self.cardTextVert = Entry(self, textvariable = self.vert).grid(row=8,column=2,sticky=W)

        #render button
        self.renderCard_button = Button(self, text = "Render Out your custom card", command = self.imageMaker)
        self.renderCard_button.grid(row = 15, column = 0, columnspan = 2, sticky = W)

        #view the image
        self.view_button = Button(self, text = "view Image", command =  self.showImage)
        self.view_button.grid(row = 15, column = 2, columnspan = 1, sticky = W)

        return self.cardText
        return self.cardTextSize
        return self.toEmail
        return self.fromEmail

root = Tk()
root.title("Postcard")
root.geometry("400x250")
app = Application(root)

root.mainloop()


  

    
