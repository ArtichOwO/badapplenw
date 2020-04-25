from kandinsky import *
from time import *

pal=[(0,0,0),(255,255,255)]
im=[] # Copy here the value of im (use bad apple.py before to generate it)
r=0
y=0
x=0
while r<len(im):
  c1=im[r]
  c2=c1[1]
  c3=pal[c2]
  nbPx1=im[r]
  nbPx2=nbPx1[0]
  for j in range(nbPx2):
    if x>=320:
      x=0
      y+=16
      if y>=222:
        y=0
        sleep(0.1)
    fill_rect(x,y,16,16,c3)
    x+=16
  r+=1
