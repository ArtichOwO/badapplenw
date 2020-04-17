from PIL import Image
from numpy import *

im = Image.open("test.png")
width, height = im.size
image = list(im.getdata())
print(image)
print("----------------------------------------------------------------------")
print("Length img: "+str(len(image)))
print("----------------------------------------------------------------------")

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

print("img =",imageCompressee)
