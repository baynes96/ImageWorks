'''
Created on Feb 25, 2020

@author: nicomp
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO

def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        print:("Load _Image(): Unable to open" + filename)
        return None

def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        print:("Save_Image(): Unable to open" + filename)
        
    
def crop_image(imageObject, cropRegion):
    im = Image.open("SiriusAndViolet.jpg")  
    im_c = im.crop((200,300,400,500)) # (left, top, right, bottom) it's a tuple!
    return im_c
