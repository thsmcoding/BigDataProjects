from game_modules.gameenv import gamescreen
import pyautogui as pag
import os
import time as ti
import selenium


def main():
    print("Starting main function execution")
    mybot = gamescreen()
    mybot.main()
    # make_screenshot()


def getcolor(x, y):
    return pag.pixel(x, y)


def make_screenshot():
    currentDirectory = os.getcwd()
    path_tail = '/img/screenshot' + str(int(ti.time())) + '.png'
    path = os.path.abspath(os.path.join(currentDirectory, os.pardir))
    path += ''.join(path_tail)
    print(path)
    landscape_bis = pag.screenshot(path)


def getcoordinates(self):
    x, y = pag.position()
    return x, y


if __name__ == '__main__':
    main()
