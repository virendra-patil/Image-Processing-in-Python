from __future__ import print_function
import os, sys
from PIL import Image
from PIL import PSDraw
from PIL import TarIO
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageStat
from pylab import *

image_file = input("Enter the name of the TIFF Image to be manipulated: ")
p = -1
while(p == -1):
    case = input("Enter Your Choice:\n 'a': Open Image File\n 'b': Resize Image File\n 'c': Image Histogram\n 'd': Display Image Attributes\n 'e': Change Mode of image into 'L'\n 'f' : Change Mode of image into 'RGB'\n 'g': Change Contrast of Image\n 'h': Rotate Image\n 'i': Blur Image\n 'j': Contour of Image\n 'k': Image Convolution\n 'l': Calculate Mean\n 'm': Calculate Median\n 'n': Calculate Variance\n 'o': Calculate Root Mean Square\n 'p': Calculate Standard Deviation\n 'q': Crop Image\n 'r': Exit\n")
    im = Image.open(image_file)

    if case == 'a':
        im.show()

    elif case == 'b':
        x = input("Enter breadth:\n")
        a = int(x)
        y = input("Enter length:\n")
        b = int(y)
        out1 = im.resize((a, b))
        out1.show()

    elif case == 'c':
        out2 = im.histogram()
        print(out2)

    elif case == 'd':
        print("Format of image: ", im.format,"\n Size of Image: ", im.size,"\n Mode of Image: ", im.mode)

    elif case == 'e':
        out4 = im.convert("L")
        print("\n Mode of Image: ", out4.mode)
        out4.show() 

    elif case == 'f':
        out5 = im.convert("RGB")
        print("\n Mode of Image: ", out5.mode)
        out5.show()

    elif case == 'g':
        choice = input("'1': Increase contrast by 50%:\n'2': Decrease contrast by 50%:\n")
        if choice == '1':
            out6 = im.point(lambda i: i * 1.5)
            out6.show()
        elif choice == '2':
            out7 = im.point(lambda i: i * 0.2)
            out7.show()

    elif case == 'h':
        choice = input("'1': Rotate Image by 45 degree:\n'2': Rotate Image by 90 degree:\n'3': Rotate Image by 135 degree:\n'4': Rotate Image by 180 degree:\n")
        if choice == '1':
            out8 = im.rotate(45)
            out8.show()
        elif choice == '2':
            out9 = im.rotate(90)
            out9.show()
        elif choice == '3':
            out10 = im.rotate(135)
            out10.show()
        elif choice == '4':
            out11 = im.rotate(180)
            out11.show()
            
    elif case == 'i':
        out12 = im.filter(ImageFilter.BLUR)
        out12.show()

    elif case == 'j':
        out13 = array(im.convert('L'))
        figure()
        gray()
        contour(out13, origin='image')
        axis('equal')
        axis('off')
        show()
  
    elif case == 'k':
        out14 = im.filter(ImageFilter.Kernel((3,3),(0,-1,0,-1,10,-1,0,-1,0),scale=None,offset=0))
        out14.show()

    elif case == 'l':
        out15 = ImageStat.Stat(im)
        print(out15.mean)

    elif case == 'm':
        out15 = ImageStat.Stat(im)
        print(out15.median)

    elif case == 'n':
        out15 = ImageStat.Stat(im)
        print(out15.var)

    elif case == 'o':
        out15 = ImageStat.Stat(im)
        print(out15.rms)

    elif case == 'p':
        out15 = ImageStat.Stat(im)
        print(out15.stddev)
 
    elif case == 'q':
        x = input("Enter breadth:\n")
        a = int(x)
        y = input("Enter length:\n")
        b = int(y)
        out1 = im.crop((a,a,b,b))
        out1.show()

    elif case == 'r':
        p = 0
