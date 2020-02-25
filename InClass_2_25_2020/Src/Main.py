'''
Created on Feb 25, 2020

@author: bayneslc
'''
from image_functions import *
# open an image file. The default path is where this python module is
im = Image.open("SiriusAndViolet.jpg")
print(im.width, im.height, im.mode, im.format)  # Display some info about the image

#my_image = load_image("SiriusAndViolet.jpg")
#my_image.show(my_image)

#make use of crop image
# 1. Load an image
# 2. Call crop_image and save what it returns
# 3. Call show to display the results

im = Image.open("SiriusAndViolet.jpg")
im_c = im.crop((200,300,400,500))
im.show()

