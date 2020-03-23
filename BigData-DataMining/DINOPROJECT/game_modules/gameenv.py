import time as ti
import pyautogui as pag
import numpy as np



#
# # GLOBALS
# NUMBER_OF_WHITE_PIXELS = 69573  # determined with landscape function
#
#
# class gamescreen:
#
#      def __init__(self):
#          self.startobj = (154, 78)
#          self.dinoobj = (122, 167)
#          # self.LEFT = self.dinoobj[0] + 90
#         # self.TOP = self.dinoobj[1]
#         # self.RIGHT = self.dinoobj[0] + 95
#         # self.BOTTOM = self.dinoobj[1] + 5
#         self.LEFT = self.dinoobj[0] + 36
#         self.TOP = self.dinoobj[1] + 112
#         self.RIGHT = self.dinoobj[0] + 118
#         self.BOTTOM = self.dinoobj[1] + 175
#
#
#         def getcoordinates(self):
#             x, y = pag.position()
#         return x, y
#
#
#     def startover(self):
#         print("Restarting the Dino game")
#         pag.click(self.startobj[0], self.startobj[1])
#         pag.keyDown("down")
#
#
#     # def gettingpixels(image, left, top, width, height):
#     #     colors = []
#     #     if image:
#     #         for x in range(left, left + width + 1):
#     #             for y in range(top, top + height + 1):
#     #                 tuples = image.getpixel((x, y))
#     #                 print(tuples)
#     #                 colors.extend(tuples)
#     #     return colors
#
#
#     def avoidobstacles(self):
#         pag.keyUp("down")
#         pag.keyDown("space")
#         ti.sleep(0.095)
#         print("Jump done")
#         pag.keyUp("space")
#         pag.keyDown("down")  #staying down to avoid birds
#
#
#     def getlandscape(self):
#         landscape_bis = pag.screenshot(region=(self.LEFT, self.TOP, self.RIGHT, self.BOTTOM))
#         white_pixels = np.array(landscape_bis)
#         compute = np.count_nonzero(white_pixels == 83)
#         print("compute :", compute)
#         return compute
#
#
#     def play_current_game(self):
#         sum_graypixels = self.getlandscape()
#         return sum_graypixels
#
#
#     def main(self):
#         print("Running the main function")
#         print("Press CTRL-C to quit")
#         self.startover()
#         self.play_current_game()
#         try:
#             self.startover()
#             self.play_current_game()
#             while True:
#                 if self.play_current_game() > 0 :
#                    self.avoidobstacles()
#                    ti.sleep(0.06)
#         except KeyboardInterrupt:\
#             print("Ended game")
#
# None