import math
TILESIZE = 32 #Constant Value for the size of our tiles.

ROWS = 10 #For 2D Render, this is the amount of rows we are allowing for a single instance.
COLS = 15 #For 2D Render, this is the amount of columns we are allowing for a single instance.

WINDOW_WIDTH = COLS * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE

FOV = 60 * (math.pi / 180) #60 Degrees in Radians

RES = 4 #This is the amount of rectangles we are seeing on the screen.
NUM_RAYS = WINDOW_WIDTH // RES

