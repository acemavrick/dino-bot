# module containing useful functions for pyautogui projects

from pyautogui import *
from time import *

screensize = size()


def ask_region():
    """Asks the user for a region (top left, bottom right) and returns it"""

    _ = input("Top-left corner")
    tlx, tly = position()
    _ = input("Bottom-right corner")
    blx, bly = position()

    return [tlx, tly, blx - tlx, bly - tly]


def ask_screenshot(name):
    """Creates a screenshot and saves it in a file with name "name".png"""
    print(f"Creating {name}.png")
    region = ask_region()
    countdown(3)
    screenshot(f"{name}.png", region)
    print(f"done, {name}.png")


def find_grey(name, bounds=None):
    """Finds the image on the screen, greyscale. Default bounds in None"""
    if not bounds:
        global screensize
        bounds = screensize
    return locateOnScreen(f"{name}.png", grayscale=True)
