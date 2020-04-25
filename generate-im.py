from PIL import Image
from numpy import *
from time import *

# Put this file in the folder where are located the images
# Img name exemple = bad-apple 023.bmp
# Img resolution = 20px*14px
# PNG files doesn't work

image=[]
# change the "for" values to match with the number of available img
for o in range(1,51):
    imcount=str(o).zfill(3)
    im = Image.open("bad-apple "+imcount+".bmp")
    width, height = im.size
    image=image+list(im.getdata())
print(image)
print("-----------------------------------------------------------------------")

imageCompressee=[]
nbPixelIdems=1
memPixel=None

for i in range(len(image)):
    if memPixel == image[i]:
        nbPixelIdems+=1
    else:
        if i != 0:
            if memPixel == 0:
                imageCompressee.append([nbPixelIdems,1])
            else:
                imageCompressee.append([nbPixelIdems,0])

        nbPixelIdems = 1
    memPixel = image[i]
            
    if i == len(image)-1:
        if memPixel == 0:
            imageCompressee.append([nbPixelIdems,1])
        else:
            imageCompressee.append([nbPixelIdems,0])
im = imageCompressee
print("im =",imageCompressee)

# Copy im to the NW script

