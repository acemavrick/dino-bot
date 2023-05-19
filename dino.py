# https://scratch.mit.edu/projects/546041977/
import time

from helper import *
from time import *

input("top bound")
sx, sy = position()

input("bottom bound")
ey = position().y

h = ey - sy

input("dino1")
d1 = position()
input("dino2")
d2 = position()

ytocheck = [0, h // 3 - 3, h - 1]
print("Activate window. Starting in:")
countdown(2)

speed = 0
fps = 60
# width is 250px
w = 300
ta = sta = position().x
stime = time()
wlist = []
wp = 0
targetwp = 270
while True:
    # iterate through checking all pixels in the column sx:sx+2
    cta = position().x
    w = cta-sx
    cim = screenshot(region=(sx, sy, w , h)).convert("L")
    f = cim.getpixel((0, 0))
    found = 0
    for x in range(w - 1, 0, -2):
        for y in ytocheck:
            if cim.getpixel((x, y)) != f:
                press("SPACE")
                wp = x
                wlist.append(x)
                print(wp)
                found = 1
                break
        if found:
            break
    if found:
        while pixel(d1.x, d1.y) == pixel(d2.x, d2.y):
            continue
