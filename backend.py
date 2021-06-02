#importation des libraries
import math
import os
import sys
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import glob
from flaskv4 import app
import shutil

#app = Flask(__name__)

def usk2(path):

    UPLOAD_FOLDER = os.path.dirname(__file__)
    #path vers la partie statique 
    path = app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER + "/static/images"
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256
    ##########
    scaleFactor = 0.09
    oneCharWidth = 18
    oneCharHeight = 18

    def converImageToAscii(path):    

        def getChar(inputInt):
            return charArray[math.floor(inputInt*interval)]

        text_file = open("out.txt", "w")
        im = Image.open(path + "/new.jpg")
        fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
        width, height = im.size
        im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
        width, height = im.size
        pix = im.load()
        outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
        d = ImageDraw.Draw(outputImage)
        for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]
                h = int(r/3 + g/3 + b/3)
                pix[j, i] = (h, h, h)
                text_file.write(getChar(h))
                d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
            text_file.write('\n')
        text_file.close()
        outputImage.save('output.png')

    listeusk2 = ["out.txt", "output.png"]
    #ICI PATH A MODIFIER
    path2 = "C:/Users/Navarro/Desktop/flaskv4/flaskv4/static/images"

    for elements in listeusk2:
        if elements in os.listdir(path2):
            os.remove(path2+"/out.txt")
            os.remove(path2+"/output.png")
            converImageToAscii(path)
            #ICI PATH A MODIFIER
            shutil.move("C:/Users/Navarro/Desktop/flaskv4/out.txt", "C:/Users/Navarro/Desktop/flaskv4/flaskv4/static/images")
            shutil.move("C:/Users/Navarro/Desktop/flaskv4/output.png", "C:/Users/Navarro/Desktop/flaskv4/flaskv4/static/images")
        else:
            converImageToAscii(path)
            #ICI PATH A MODIFIER
            shutil.move("C:/Users/Navarro/Desktop/flaskv4/out.txt", "C:/Users/Navarro/Desktop/flaskv4/flaskv4/static/images")
            shutil.move("C:/Users/Navarro/Desktop/flaskv4/output.png", "C:/Users/Navarro/Desktop/flaskv4/flaskv4/static/images")

         
