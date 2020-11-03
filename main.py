import math
import random
import tkinter as tk
from Kmeans import *
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import Canvas


class class1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="black")
        self.geometry("1200x700")
        self.title("Colour Palette")
        self.upload = Button(self, height=3, width=20, text="UPLOAD IMAGE", bg="gold", fg="Black", command=UploadAction)
        self.upload.place(x=100, y=400)


def draw_colors(colors_list):
    canvas = Canvas(width=550, height=59, bg="white")
    canvas.create_rectangle(5, 2, 105, 60, fill=colors_list[0])
    canvas.create_rectangle(115, 2, 215, 60, fill=colors_list[1])
    canvas.create_rectangle(225, 2, 325, 60, fill=colors_list[2])
    canvas.create_rectangle(335, 2, 435, 60, fill=colors_list[3])
    canvas.create_rectangle(445, 2, 545, 60, fill=colors_list[4])
    canvas.place(x=600, y=570)


def rgb_to_hex(rgb):
  return '#%s' % ''.join(('%02x' % p for p in rgb))


def get_colors(filename, n_colors=3):
    points = get_points(filename)
    clusters = KMeans(n_clusters=n_colors).fit(points)
    clusters.sort(key=lambda c: len(c.points), reverse=True)
    rgbs = [map(int, c.center.coordinates) for c in clusters]
    return list(map(rgb_to_hex, rgbs))


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    image = image.resize((550, 550))
    image = ImageTk.PhotoImage(image)
    panel = Label(root, image=image)
    panel.image = image
    panel.place(x=600, y=0)
    colors = get_colors(filename, n_colors=5)
    draw_colors(colors)



if __name__ == '__main__':
    root = class1()
    root.mainloop()
