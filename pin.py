
import tkinter as tk
from PIL import Image, ImageTk
import random
STEP=10
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

img = Image.open("bit.png").convert("RGBA")
img2 = Image.open("pin.png").convert("RGBA")
data = img.getdata()
new_data = []

for pixel in data:
    # se for preto puro, fica transparente
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(pixel)

img.putdata(new_data)

data = img2.getdata()
new_data = []

for pixel in data:
    # se for preto puro, fica transparente
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(pixel)

img2.putdata(new_data)


pic = ImageTk.PhotoImage(img)
pic2 = ImageTk.PhotoImage(img2)
xy=[]
for n in range(20):
    xx=int(random.random()*600)
    yy=int(random.random()*400)
    xy=xy+[xx]+[yy]
rect = canvas.create_image(50, 50, image=pic)
lens=int(len(xy)//2)
for n in range(0,lens):
    h=canvas.create_image(xy[n*2], xy[n*2+1], image=pic2)
def move(event):
    if event.keysym == "Up":
        canvas.move(rect, 0, -STEP)
    elif event.keysym == "Down":
        canvas.move(rect, 0, STEP)
    elif event.keysym == "Left":
        canvas.move(rect, -STEP, 0)
    elif event.keysym == "Right":
        canvas.move(rect, STEP, 0)

# Capturar teclas
root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

root.mainloop()
