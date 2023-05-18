# https://scratch.mit.edu/projects/546041977/

from helper import *
from time import *

input("top bound")
sx, sy = position()

input("bottom bound")
ey = position().y

h = ey - sy

ytocheck = [0, h // 3 - 3, h - 1]
print("Activate window. Starting in:")
countdown(2)

ta = position().x
while True:
    # iterate through checking all pixels in the column sx:sx+2
    cta = position().x
    if ta == cta:
        ta += 3
        moveRel(1, 0)
    else:
        ta = cta
    cim = screenshot(region=(sx, sy, ta - sx, h)).convert("L")
    f = cim.getpixel((0, 0))
    found = 0
    for x in range(ta - sx - 1, 0, -3):
        for y in ytocheck:
            if cim.getpixel((x, y)) != f:
                press("SPACE")
                print("clicked", end="")
                found = 1
                break
        if found:
            break
    print("\r", end="")
