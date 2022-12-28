from tkinter import *
from PIL import ImageTk, Image

# Ask user for maze size
gridSize = int(input("How many rows and columns for the maze?: "))


root = Tk()
root.config(height=35*gridSize + 20, width=35*gridSize + 20)
# set variables to parsable image references
hWall = ImageTk.PhotoImage(Image.open("./assets/hori-wall.png"))
vWall = ImageTk.PhotoImage(Image.open("./assets/vert-wall.png"))
cell = ImageTk.PhotoImage(Image.open("./assets/cell.png"))
potion = ImageTk.PhotoImage(Image.open("./assets/potion.png"))
coin = ImageTk.PhotoImage(Image.open("./assets/coin.png"))

canvas= Canvas(root, width=35*gridSize + 20, height=35*gridSize + 20)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

# Define wall image length and width in pixels
cellWidth = 35
wallSize = 2

ydist = 2

# loop through wall placment using user defined size
#runs 4 times
for i in range(int(gridSize + 1)):
    xdist = 2
    for j in range(int(gridSize)):
        if i < gridSize:
            canvas.create_image(xdist +1,ydist+1,anchor=NW,image=cell)
        canvas.create_image(xdist,ydist,anchor=NW,image=hWall)
        xdist += 35
    ydist += 35

xdist = 2

for i in range(int(gridSize + 1)):
    ydist = 4
    for j in range(int(gridSize)):
        canvas.create_image(xdist,ydist,anchor=NW,image=vWall)
        ydist += 35
    xdist += 35

root.mainloop()