from tkinter import *
from PIL import ImageTk, Image

# Ask user for maze size
gridSize = int(input("How many rows and columns for the maze?: "))

root = Tk()
# set variables to parsable image references
hWall = ImageTk.PhotoImage(Image.open("./assets/hori-wall.png"))
vWall = ImageTk.PhotoImage(Image.open("./assets/vert-wall.png"))

canvas= Canvas(root, width=35*gridSize, height=35*gridSize)
canvas.pack()

# Define wall image length and width in pixels
cellWidth = 35
wallSize = 2

ydist = 2

# loop through wall placment using user defined size
for i in range(int(gridSize + 1)):
    xdist = 2
    for j in range(int(gridSize)):
        canvas.create_image(xdist,ydist,anchor=NW,image=hWall)
        xdist += 33
    ydist += 33

xdist = 2

for i in range(int(gridSize + 1)):
    ydist = 2
    for j in range(int(gridSize)):
        canvas.create_image(xdist,ydist,anchor=NW,image=vWall)
        ydist += 33
    xdist += 33

root.mainloop()