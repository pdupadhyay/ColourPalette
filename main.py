import math
import random
import tkinter as tk
from Kmeans import *
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


class class1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="white")
        self.geometry("1200x700")
        self.title("Colour Palette")
        self.upload = Button(self, height=3, width=20, text="UPLOAD IMAGE", bg="Cyan", fg="White", command=UploadAction)
        self.upload.place(x=100, y=400)





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
    color_label1 = Label(root, text=colors[0])
    color_label1.place(x=600, y=600)
    color_label2 = Label(root, text=colors[1])
    color_label2.place(x=700, y=600)
    color_label3 = Label(root, text=colors[2])
    color_label3.place(x=800, y=600)
    color_label4 = Label(root, text=colors[3])
    color_label4.place(x=900, y=600)
    color_label5 = Label(root, text=colors[4])
    color_label5.place(x=1000, y=600)



if __name__ == '__main__':
    root = class1()
    root.mainloop()
#    get_colors("./test_pic1.jpg")
