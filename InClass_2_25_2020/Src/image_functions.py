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
        return None
    
